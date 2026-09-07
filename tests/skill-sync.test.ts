import { spawnSync } from "node:child_process";
import { chmod, copyFile, mkdir, mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { afterEach, describe, expect, it } from "vitest";

const roots: string[] = [];
const sourceScript = resolve(fileURLToPath(new URL("../scripts/check-skill-sync.bash", import.meta.url)));

interface CommandResult {
  readonly status: number | null;
  readonly stdout: string;
  readonly stderr: string;
}

function execute(root: string, command: string, arguments_: readonly string[], environment = {}): CommandResult {
  const result = spawnSync(command, arguments_, {
    cwd: root,
    encoding: "utf8",
    env: { ...process.env, ...environment },
  });
  return { status: result.status, stdout: result.stdout, stderr: result.stderr };
}

function git(root: string, ...arguments_: string[]): void {
  const result = execute(root, "git", arguments_);
  if (result.status !== 0) throw new Error(result.stderr);
}

async function createFixture(): Promise<{ repository: string; script: string }> {
  const root = await mkdtemp(join(tmpdir(), "blueprint-skill-sync-"));
  roots.push(root);
  const repository = join(root, "repository");
  const remote = join(root, "remote.git");
  const script = join(repository, "scripts/check-skill-sync.bash");
  await mkdir(join(repository, ".agents/skills/heaven-style"), { recursive: true });
  await mkdir(join(repository, "scripts"), { recursive: true });
  await writeFile(join(repository, ".agents/skills/heaven-style/SKILL.md"), "version: 1\n");
  await copyFile(sourceScript, script);
  await chmod(script, 0o755);
  git(repository, "init", "--initial-branch=legacy");
  git(repository, "config", "user.name", "Blueprint Test");
  git(repository, "config", "user.email", "blueprint@example.invalid");
  git(repository, "add", ".");
  git(repository, "commit", "-m", "Initial skill");
  git(repository, "branch", "next");
  git(root, "init", "--bare", remote);
  git(repository, "remote", "add", "origin", remote);
  git(repository, "push", "origin", "legacy", "next");
  return { repository, script };
}

afterEach(async () => {
  await Promise.all(roots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

describe("heaven-style branch synchronization", () => {
  it("accepts configurable local branch arguments", async () => {
    const fixture = await createFixture();

    const result = execute(fixture.repository, "bash", [fixture.script, "legacy,next"]);

    expect(result.status).toBe(0);
    expect(result.stdout).toContain("byte-identical across 2 branches");
    expect(result.stdout).toContain("legacy=");
    expect(result.stdout).toContain("next=");
  });

  it("fetches configured remote branches and rejects divergent trees", async () => {
    const fixture = await createFixture();
    git(fixture.repository, "switch", "next");
    await writeFile(join(fixture.repository, ".agents/skills/heaven-style/SKILL.md"), "version: 2\n");
    git(fixture.repository, "add", ".agents/skills/heaven-style/SKILL.md");
    git(fixture.repository, "commit", "-m", "Diverge skill");
    git(fixture.repository, "push", "origin", "next");
    git(fixture.repository, "switch", "legacy");
    git(fixture.repository, "branch", "-D", "next");

    const result = execute(fixture.repository, "bash", [fixture.script], {
      HEAVEN_STYLE_BRANCHES: "legacy,next",
      HEAVEN_STYLE_CURRENT_BRANCH: "legacy",
      HEAVEN_STYLE_FETCH_REMOTE: "origin",
    });

    expect(result.status).toBe(1);
    expect(result.stderr).toContain("differs across configured branches");
    expect(result.stderr).toContain("legacy=");
    expect(result.stderr).toContain("next=");
  });

  it("rejects an uncommitted skill edit on the current configured branch", async () => {
    const fixture = await createFixture();
    await writeFile(join(fixture.repository, ".agents/skills/heaven-style/SKILL.md"), "version: dirty\n");

    const result = execute(fixture.repository, "bash", [fixture.script, "legacy", "next"], {
      HEAVEN_STYLE_CURRENT_BRANCH: "legacy",
    });

    expect(result.status).toBe(1);
    expect(result.stderr).toContain("has uncommitted changes on legacy");
  });
});
