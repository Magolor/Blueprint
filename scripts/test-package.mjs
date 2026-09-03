import { mkdtemp, readdir, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const repositoryRoot = resolve(fileURLToPath(new URL("..", import.meta.url)));
const temporaryRoot = await mkdtemp(join(tmpdir(), "blueprint-package-"));
const packageManager = process.platform === "win32" ? "pnpm.cmd" : "pnpm";

function run(command, arguments_, cwd) {
  const result = spawnSync(command, arguments_, { cwd, encoding: "utf8", stdio: "pipe" });
  if (result.status !== 0) {
    process.stderr.write(result.stdout);
    process.stderr.write(result.stderr);
    throw new Error(`${command} ${arguments_.join(" ")} failed with exit code ${result.status}`);
  }
  return result.stdout.trim();
}

try {
  run(packageManager, ["pack", "--pack-destination", temporaryRoot], repositoryRoot);
  const archive = (await readdir(temporaryRoot)).find((name) => name.endsWith(".tgz"));
  if (archive === undefined) {
    throw new Error("pnpm pack did not produce an archive");
  }

  await writeFile(
    join(temporaryRoot, "package.json"),
    `${JSON.stringify({ private: true, type: "module" }, null, 2)}\n`,
  );
  run(packageManager, ["add", "--offline", `file:${join(temporaryRoot, archive)}`], temporaryRoot);
  const output = run(
    process.execPath,
    ["--input-type=module", "--eval", 'import { VERSION } from "@magolor/blueprint"; console.log(VERSION);'],
    temporaryRoot,
  );
  if (output !== "0.1.2.3") {
    throw new Error(`installed package reported unexpected version ${output}`);
  }
  run(packageManager, ["exec", "bp", "--version"], temporaryRoot);
  process.stdout.write(`Packed artifact verified (${archive}).\n`);
} finally {
  await rm(temporaryRoot, { recursive: true, force: true });
}
