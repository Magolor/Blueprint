import { describe, expect, it, vi } from "vitest";

import { run } from "../src/cli.js";
import { VERSION } from "../src/index.js";

describe("CLI", () => {
  it("prints the package version", () => {
    const write = vi.fn();

    expect(run(["--version"], write)).toBe(0);
    expect(write).toHaveBeenCalledWith(VERSION);
  });

  it("prints configured information as text or JSON", () => {
    const write = vi.fn();

    expect(run(["info"], write, { BLUEPRINT_PROJECT_NAME: "Example" })).toBe(0);
    expect(run(["info", "--json"], write, { BLUEPRINT_PROJECT_NAME: "Example" })).toBe(0);
    expect(write).toHaveBeenNthCalledWith(1, `Example ${VERSION}`);
    expect(write).toHaveBeenNthCalledWith(2, JSON.stringify({ name: "Example", version: VERSION, output: "text" }));
  });

  it("rejects unknown commands and options", () => {
    const write = vi.fn();

    expect(run(["unknown"], write)).toBe(2);
    expect(run(["info", "--unknown"], write)).toBe(2);
    expect(write).toHaveBeenNthCalledWith(1, expect.stringContaining("Invalid arguments: unknown"));
    expect(write).toHaveBeenNthCalledWith(2, expect.stringContaining("Invalid arguments: info --unknown"));
  });
});
