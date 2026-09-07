import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vitest";
import { parse } from "yaml";

const repositoryRoot = resolve(fileURLToPath(new URL("..", import.meta.url)));

function requireRecord(value: unknown, label: string): Record<string, unknown> {
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    throw new TypeError(`${label} must be a mapping`);
  }
  return value as Record<string, unknown>;
}

describe("GitHub CI", () => {
  it("exposes configurable heaven-style branch synchronization", async () => {
    const source = await readFile(resolve(repositoryRoot, ".github/workflows/heaven-style-sync.yml"), "utf8");
    const workflow = requireRecord(parse(source), "workflow");
    const triggers = requireRecord(workflow.on, "workflow.on");
    const dispatch = requireRecord(triggers.workflow_dispatch, "workflow_dispatch");
    const inputs = requireRecord(dispatch.inputs, "workflow_dispatch.inputs");
    const branches = requireRecord(inputs.branches, "workflow_dispatch.inputs.branches");
    const jobs = requireRecord(workflow.jobs, "workflow.jobs");
    const verify = requireRecord(jobs.verify, "workflow.jobs.verify");
    const environment = requireRecord(verify.env, "workflow.jobs.verify.env");

    expect(triggers).toHaveProperty("push");
    expect(triggers).toHaveProperty("pull_request");
    expect(branches.default).toBe("python typescript");
    expect(environment.HEAVEN_STYLE_BRANCHES).toContain("vars.HEAVEN_STYLE_BRANCHES");
    expect(environment.HEAVEN_STYLE_FETCH_REMOTE).toBe("origin");
    expect(source).toContain("bash scripts/check-skill-sync.bash");
  });
});
