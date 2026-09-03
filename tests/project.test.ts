import { describe, expect, it } from "vitest";

import { getProjectInfo, VERSION } from "../src/index.js";

describe("project information", () => {
  it("reports detached configured identity", () => {
    const input = { project: { name: "Example" }, cli: { output: "text" as const } };
    const info = getProjectInfo(input);
    input.project.name = "Changed";

    expect(info).toEqual({ name: "Example", version: VERSION, output: "text" });
    expect(Object.isFrozen(info)).toBe(true);
  });
});
