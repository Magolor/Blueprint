#!/usr/bin/env node

import { pathToFileURL } from "node:url";

import { getProjectInfo, loadConfig, VERSION } from "./index.js";

const HELP = `Blueprint ${VERSION}

Usage:
  bp info [--json]   Print package information
  bp --version       Print the package version
  bp --help          Show this help
`;

type CliCommand =
  | { readonly kind: "help" }
  | { readonly kind: "version" }
  | { readonly kind: "info"; readonly output: "configured" | "json" };

class CliUsageError extends Error {}

function parseArguments(arguments_: readonly string[]): CliCommand {
  if (arguments_.length === 0) return { kind: "help" };
  if (arguments_.length === 1 && (arguments_[0] === "--help" || arguments_[0] === "-h")) return { kind: "help" };
  if (arguments_.length === 1 && (arguments_[0] === "--version" || arguments_[0] === "-v")) {
    return { kind: "version" };
  }
  if (arguments_.length === 1 && arguments_[0] === "info") return { kind: "info", output: "configured" };
  if (arguments_.length === 2 && arguments_[0] === "info" && arguments_[1] === "--json") {
    return { kind: "info", output: "json" };
  }
  throw new CliUsageError(`Invalid arguments: ${arguments_.join(" ")}`);
}

/** Adapt one closed CLI command to the public Blueprint SDK. */
export function run(
  arguments_: readonly string[],
  write: (value: string) => void = console.log,
  environment: NodeJS.ProcessEnv = process.env,
): number {
  try {
    const command = parseArguments(arguments_);
    switch (command.kind) {
      case "help":
        write(HELP.trimEnd());
        return 0;
      case "version":
        write(VERSION);
        return 0;
      case "info": {
        const config = loadConfig(environment);
        const info = getProjectInfo(config);
        write(
          command.output === "json" || config.cli.output === "json"
            ? JSON.stringify(info)
            : `${info.name} ${info.version}`,
        );
        return 0;
      }
    }
  } catch (error) {
    if (!(error instanceof CliUsageError)) throw error;
    write(`${error.message}\n\n${HELP.trimEnd()}`);
    return 2;
  }
}

const invokedPath = process.argv[1];
if (invokedPath !== undefined && import.meta.url === pathToFileURL(invokedPath).href) {
  process.exitCode = run(process.argv.slice(2));
}
