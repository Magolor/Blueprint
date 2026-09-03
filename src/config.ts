/** Complete configuration for one starter project operation. */
export interface ProjectConfig {
  readonly project: {
    readonly name: string;
  };
  readonly cli: {
    readonly output: "text" | "json";
  };
}

const DEFAULT_PROJECT_NAME = "Blueprint";

function freezeConfig(config: ProjectConfig): Readonly<ProjectConfig> {
  return Object.freeze({
    project: Object.freeze({ ...config.project }),
    cli: Object.freeze({ ...config.cli }),
  });
}

/** Default configuration for one starter project operation. */
export const DEFAULT_CONFIG = freezeConfig({
  project: { name: DEFAULT_PROJECT_NAME },
  cli: { output: "text" },
});

function requireRecord(value: unknown, path: string): Record<string, unknown> {
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    throw new TypeError(`${path} must be an object`);
  }
  return value as Record<string, unknown>;
}

function requireProjectName(value: unknown): string {
  if (typeof value !== "string" || value.trim().length === 0) {
    throw new TypeError("config.project.name must be a non-empty string");
  }
  return value.trim();
}

function requireOutput(value: unknown): ProjectConfig["cli"]["output"] {
  if (value !== "text" && value !== "json") {
    throw new TypeError('config.cli.output must be either "text" or "json"');
  }
  return value;
}

/**
 * Validate, detach, and freeze one complete configuration value.
 *
 * @throws {TypeError} When a required field is absent or invalid.
 */
export function defineConfig(value: unknown): Readonly<ProjectConfig> {
  const config = requireRecord(value, "config");
  const project = requireRecord(config.project, "config.project");
  const cli = requireRecord(config.cli, "config.cli");
  return freezeConfig({
    project: { name: requireProjectName(project.name) },
    cli: { output: requireOutput(cli.output) },
  });
}

/**
 * Build a detached configuration snapshot from process-style environment variables.
 *
 * @throws {TypeError} When an environment value is invalid.
 */
export function loadConfig(environment: NodeJS.ProcessEnv = process.env): Readonly<ProjectConfig> {
  return defineConfig({
    project: { name: environment.BLUEPRINT_PROJECT_NAME ?? DEFAULT_CONFIG.project.name },
    cli: { output: environment.BLUEPRINT_OUTPUT ?? DEFAULT_CONFIG.cli.output },
  });
}
