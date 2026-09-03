import packageMetadata from "../package.json" with { type: "json" };

import { DEFAULT_CONFIG, defineConfig, type ProjectConfig } from "./config.js";

/** Blueprint's cross-branch project version. */
export const VERSION = packageMetadata.blueprintVersion;

/** Stable information about one configured starter project. */
export interface ProjectInfo {
  readonly name: string;
  readonly version: string;
  readonly output: ProjectConfig["cli"]["output"];
}

/** Validate one configuration value and return immutable project information. */
export function getProjectInfo(config: Readonly<ProjectConfig> = DEFAULT_CONFIG): Readonly<ProjectInfo> {
  const admitted = defineConfig(config);
  return Object.freeze({
    name: admitted.project.name,
    version: VERSION,
    output: admitted.cli.output,
  });
}
