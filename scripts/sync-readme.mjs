import { readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = resolve(fileURLToPath(new URL("..", import.meta.url)));
const source = resolve(repositoryRoot, "README.en.md");
const target = resolve(repositoryRoot, "README.md");
const expected = await readFile(source, "utf8");

if (process.argv.includes("--check")) {
  const actual = await readFile(target, "utf8");
  if (actual !== expected) {
    throw new Error("README.md is stale; run pnpm readme:sync");
  }
} else {
  await writeFile(target, expected);
  process.stdout.write("Synchronized README.md from README.en.md.\n");
}
