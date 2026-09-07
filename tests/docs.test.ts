import { mkdtemp, mkdir, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";

import { afterEach, describe, expect, it } from "vitest";

import { validateDocs } from "../scripts/docs.js";

const roots: string[] = [];

async function createFixture(): Promise<string> {
  const root = await mkdtemp(join(tmpdir(), "blueprint-docs-"));
  roots.push(root);
  await mkdir(join(root, "docs/plans"), { recursive: true });
  await mkdir(join(root, "docs/scratch"), { recursive: true });
  await writeFile(join(root, "README.en.md"), "# Fixture\n");
  await writeFile(join(root, "AGENTS.md"), "# Agents\n");
  await writeFile(join(root, "CONTRIBUTING.md"), "# Contributing\n");
  await writeFile(join(root, "docs/README.md"), "# Engineering\n");
  await writeFile(join(root, "docs/DEVLOG.md"), "# Development Log\n\n## 2026-08-14\n\n- Next: none\n");
  await writeFile(
    join(root, "docs/tasks.yaml"),
    "schema: heaven.tasks/v1\nproject: Fixture\nupdated: 2026-08-14\ntasks: []\n",
  );
  await writeFile(join(root, "docs/plans/README.md"), "# Plans\n");
  await writeFile(join(root, "docs/scratch/README.md"), "# Scratch\n");
  return root;
}

afterEach(async () => {
  await Promise.all(roots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

describe("documentation contract", () => {
  it("accepts a minimal valid documentation surface", async () => {
    const root = await createFixture();

    expect(validateDocs(root, new Date("2026-08-14T00:00:00.000Z")).errors).toEqual([]);
  });

  it("reports broken repository-local links", async () => {
    const root = await createFixture();
    await writeFile(join(root, "README.en.md"), "[missing](missing.md)\n");

    expect(validateDocs(root).errors).toContain("LINK_MISSING: README.en.md -> missing.md");
  });

  it("accepts draft and postponed work with an explicit resume condition", async () => {
    const root = await createFixture();
    await writeFile(
      join(root, "docs/tasks.yaml"),
      [
        "schema: heaven.tasks/v1",
        "project: Fixture",
        "updated: 2026-08-14",
        "tasks:",
        "  - id: FX-001",
        "    title: Draft an outcome",
        "    status: draft",
        "    priority: P2",
        "    updated: 2026-08-14",
        "    acceptance: [Outcome is accepted.]",
        "    depends_on: []",
        "    links: []",
        "  - id: FX-002",
        "    title: Resume after release",
        "    status: postponed",
        "    priority: P3",
        "    updated: 2026-08-14",
        "    resume_when: Version 2 ships.",
        "    acceptance: [Compatibility is verified.]",
        "    depends_on: []",
        "    links: []",
        "",
      ].join("\n"),
    );

    expect(validateDocs(root, new Date("2026-08-14T00:00:00.000Z")).errors).toEqual([]);
  });
});
