import { describe, expect, it } from "vitest";

import { DEFAULT_CONFIG, defineConfig, loadConfig } from "../src/index.js";

describe("configuration", () => {
  it("loads immutable defaults", () => {
    expect(loadConfig({})).toEqual(DEFAULT_CONFIG);
    expect(Object.isFrozen(DEFAULT_CONFIG.project)).toBe(true);
  });

  it("validates environment-backed values", () => {
    expect(loadConfig({ BLUEPRINT_PROJECT_NAME: " Acme ", BLUEPRINT_OUTPUT: "json" })).toEqual({
      project: { name: "Acme" },
      cli: { output: "json" },
    });
  });

  it("rejects invalid external values", () => {
    expect(() => defineConfig({ project: { name: "" }, cli: { output: "xml" } })).toThrow(TypeError);
    expect(() => defineConfig({ project: [], cli: { output: "text" } })).toThrow("config.project must be an object");
  });
});
