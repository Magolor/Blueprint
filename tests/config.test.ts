import { describe, expect, it } from "vitest";

import { DEFAULT_CONFIG, defineConfig, loadConfig } from "../src/index.js";

describe("configuration", () => {
  it("resolves defaults and detached environment overrides", () => {
    expect(loadConfig({})).toEqual(DEFAULT_CONFIG);
    expect(Object.isFrozen(DEFAULT_CONFIG.project)).toBe(true);
    const environment = { BLUEPRINT_PROJECT_NAME: " Acme ", BLUEPRINT_OUTPUT: "json" };
    const config = loadConfig(environment);
    environment.BLUEPRINT_PROJECT_NAME = "Changed";
    expect(config).toEqual({ project: { name: "Acme" }, cli: { output: "json" } });
    expect(Object.isFrozen(config.cli)).toBe(true);
  });

  it.each([
    [null, "config must be an object"],
    [{ project: [], cli: { output: "text" } }, "config.project must be an object"],
    [{ project: { name: " " }, cli: { output: "text" } }, "config.project.name"],
    [{ project: { name: "Acme" }, cli: { output: "xml" } }, "config.cli.output"],
  ])("rejects invalid input %j", (input, message) => {
    expect(() => defineConfig(input)).toThrow(String(message));
  });
});
