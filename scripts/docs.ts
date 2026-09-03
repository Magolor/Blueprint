import { spawnSync } from "node:child_process";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { dirname, relative, resolve, sep } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { parse } from "yaml";

const QUEUE_SCHEMA = "heaven.tasks/v1";
const OPEN_STATUSES = new Set(["draft", "ready", "active", "blocked", "postponed"]);
const PRIORITIES = new Set(["P0", "P1", "P2", "P3"]);
const REQUIRED_FILES = ["README.en.md", "docs/README.md", "docs/DEVLOG.md", "docs/tasks.yaml"];
const PLAN_STATUSES = new Set(["Planned", "In progress", "Blocked", "Done", "Superseded"]);
const TASK_ID_PATTERN = /^[A-Z][A-Z0-9]*-[0-9]{3,}$/u;

type RecordValue = Record<string, unknown>;

interface Task extends RecordValue {
  id: string;
}

function isRecord(value: unknown): value is RecordValue {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function readText(path: string): string {
  return readFileSync(path, "utf8");
}

function parseDate(value: unknown, field: string, errors: string[]): Date | undefined {
  const normalized = value instanceof Date ? value.toISOString().slice(0, 10) : value;
  if (typeof normalized !== "string" || !/^\d{4}-\d{2}-\d{2}$/u.test(normalized)) {
    errors.push(`DATE_INVALID: ${field} must be YYYY-MM-DD`);
    return undefined;
  }
  const parsed = new Date(`${normalized}T00:00:00.000Z`);
  if (Number.isNaN(parsed.valueOf()) || parsed.toISOString().slice(0, 10) !== normalized) {
    errors.push(`DATE_INVALID: ${field} must be YYYY-MM-DD`);
    return undefined;
  }
  return parsed;
}

function loadYaml(path: string, errors: string[]): unknown {
  try {
    return parse(readText(path));
  } catch (error) {
    errors.push(`YAML_INVALID: ${path}: ${error instanceof Error ? error.message : String(error)}`);
    return undefined;
  }
}

function listMarkdown(root: string): string[] {
  if (!existsSync(root)) return [];
  const paths: string[] = [];
  for (const entry of readdirSync(root, { withFileTypes: true })) {
    const path = resolve(root, entry.name);
    if (entry.isDirectory()) paths.push(...listMarkdown(path));
    else if (entry.isFile() && entry.name.endsWith(".md")) paths.push(path);
  }
  return paths.sort();
}

function gitFiles(root: string, prefix: string): string[] {
  const result = spawnSync("git", ["ls-files", "--", prefix], { cwd: root, encoding: "utf8" });
  return result.status === 0 ? result.stdout.split(/\r?\n/u).filter(Boolean) : [];
}

function isInside(root: string, candidate: string): boolean {
  const path = relative(root, candidate);
  return path === "" || (!path.startsWith(`..${sep}`) && path !== ".." && !path.startsWith(sep));
}

function validateStructure(root: string, errors: string[]): void {
  for (const path of REQUIRED_FILES) {
    if (!existsSync(resolve(root, path))) errors.push(`SURFACE_MISSING: ${path}`);
  }
  if (existsSync(resolve(root, "docs/progress")))
    errors.push("LEGACY_SURFACE: retire docs/progress into docs/DEVLOG.md");
  if (existsSync(resolve(root, ".temp"))) {
    for (const path of gitFiles(root, ".temp")) errors.push(`SCRATCH_TRACKED: ${path} must remain disposable`);
  }
}

function stringList(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string" && item.trim().length > 0);
}

function validateCycles(tasks: Map<string, Task>, field: "depends_on" | "parent", errors: string[]): void {
  for (const taskId of [...tasks.keys()].sort()) {
    const trail: string[] = [];
    const visit = (current: string): void => {
      const cycleStart = trail.indexOf(current);
      if (cycleStart >= 0) {
        const label = field === "parent" ? "TASK_PARENT_CYCLE" : "TASK_DEPENDENCY_CYCLE";
        errors.push(`${label}: ${[...trail.slice(cycleStart), current].join(" -> ")}`);
        return;
      }
      const task = tasks.get(current);
      if (task === undefined) return;
      trail.push(current);
      const next = task[field];
      if (field === "parent" && typeof next === "string") visit(next);
      if (field === "depends_on" && Array.isArray(next)) {
        for (const dependency of next) if (typeof dependency === "string") visit(dependency);
      }
      trail.pop();
    };
    visit(taskId);
  }
}

function validateTasks(root: string, errors: string[]): Task[] {
  const data = loadYaml(resolve(root, "docs/tasks.yaml"), errors);
  if (!isRecord(data)) {
    errors.push("QUEUE_ROOT: docs/tasks.yaml must contain a mapping");
    return [];
  }
  if (data.schema !== QUEUE_SCHEMA) errors.push(`QUEUE_SCHEMA: schema must be ${QUEUE_SCHEMA}`);
  if (typeof data.project !== "string" || data.project.trim().length === 0) {
    errors.push("QUEUE_PROJECT: project must be a non-empty string");
  }
  if (!Array.isArray(data.tasks)) {
    errors.push("QUEUE_TASKS: tasks must be a list");
    return [];
  }
  const queueUpdated = parseDate(data.updated, "queue.updated", errors);
  const tasks: Task[] = [];
  const seen = new Set<string>();
  for (const [position, candidate] of data.tasks.entries()) {
    if (!isRecord(candidate)) {
      errors.push(`TASK_MAPPING: tasks[${position}] must be a mapping`);
      continue;
    }
    if (typeof candidate.id !== "string" || !TASK_ID_PATTERN.test(candidate.id)) {
      errors.push(`TASK_ID: tasks[${position}].id must match ${TASK_ID_PATTERN.source}`);
      continue;
    }
    const task = candidate as Task;
    if (seen.has(task.id)) {
      errors.push(`TASK_DUPLICATE: ${task.id}`);
      continue;
    }
    seen.add(task.id);
    tasks.push(task);
    if (typeof task.title !== "string" || task.title.trim().length === 0)
      errors.push(`TASK_TITLE: ${task.id} needs a title`);
    if (typeof task.status !== "string" || !OPEN_STATUSES.has(task.status)) {
      errors.push(
        `TASK_STATUS: ${task.id} must use draft, ready, active, blocked, or postponed; closed work leaves the queue`,
      );
    }
    if (typeof task.priority !== "string" || !PRIORITIES.has(task.priority)) {
      errors.push(`TASK_PRIORITY: ${task.id} must use P0, P1, P2, or P3`);
    }
    const updated = parseDate(task.updated, `${task.id}.updated`, errors);
    if (queueUpdated !== undefined && updated !== undefined && updated > queueUpdated) {
      errors.push(`TASK_UPDATED: ${task.id} is newer than queue.updated`);
    }
    if (task.status === "active" && (typeof task.owner !== "string" || task.owner.trim().length === 0)) {
      errors.push(`TASK_OWNER: active task ${task.id} needs an owner`);
    }
    if (task.status === "blocked" && (typeof task.blocker !== "string" || task.blocker.trim().length === 0)) {
      errors.push(`TASK_BLOCKER: blocked task ${task.id} needs a blocker`);
    }
    if (task.status === "blocked" && (typeof task.unblock_when !== "string" || task.unblock_when.trim().length === 0)) {
      errors.push(`TASK_UNBLOCK: blocked task ${task.id} needs an observable unblock_when condition`);
    }
    if (task.status === "postponed" && (typeof task.resume_when !== "string" || task.resume_when.trim().length === 0)) {
      errors.push(`TASK_RESUME: postponed task ${task.id} needs an observable resume_when condition`);
    }
    if (!stringList(task.acceptance) || task.acceptance.length === 0) {
      errors.push(`TASK_ACCEPTANCE: ${task.id} needs a non-empty string list`);
    }
    for (const field of ["depends_on", "links"] as const) {
      if (!stringList(task[field] ?? []))
        errors.push(`TASK_${field.toUpperCase()}: ${task.id}.${field} must be a string list`);
    }
  }
  const byId = new Map(tasks.map((task) => [task.id, task]));
  for (const task of tasks) {
    if (task.parent !== undefined && task.parent !== null && typeof task.parent !== "string") {
      errors.push(`TASK_PARENT: ${task.id}.parent must be a task ID or null`);
    } else if (task.parent === task.id) errors.push(`TASK_SELF_PARENT: ${task.id}`);
    else if (typeof task.parent === "string" && !byId.has(task.parent))
      errors.push(`TASK_PARENT_MISSING: ${task.id} -> ${task.parent}`);
    if (Array.isArray(task.depends_on)) {
      for (const dependency of task.depends_on) {
        if (dependency === task.id) errors.push(`TASK_SELF_DEPENDENCY: ${task.id}`);
        else if (typeof dependency === "string" && !byId.has(dependency))
          errors.push(`TASK_DEPENDENCY_MISSING: ${task.id} -> ${dependency}`);
      }
    }
    if (Array.isArray(task.links)) {
      for (const link of task.links) {
        if (typeof link !== "string" || /^https?:\/\//u.test(link)) continue;
        const target = resolve(root, link);
        if (!isInside(root, target)) errors.push(`TASK_LINK_ESCAPE: ${task.id} -> ${link}`);
        else if (!existsSync(target)) errors.push(`TASK_LINK_MISSING: ${task.id} -> ${link}`);
      }
    }
  }
  validateCycles(byId, "depends_on", errors);
  validateCycles(byId, "parent", errors);
  return tasks;
}

function validateDevlog(root: string, taskIds: Set<string>, errors: string[]): void {
  const path = resolve(root, "docs/DEVLOG.md");
  if (!existsSync(path)) return;
  const text = readText(path);
  if (!text.startsWith("# Development Log\n"))
    errors.push("DEVLOG_HEADER: docs/DEVLOG.md must start with '# Development Log'");
  const headings = [...text.matchAll(/^##[ \t]+(\S+)(?:[ \t]+.*)?$/gmu)];
  if (headings.length === 0) {
    errors.push("DEVLOG_EMPTY: docs/DEVLOG.md needs at least one dated entry");
    return;
  }
  const dates: string[] = [];
  for (const [position, heading] of headings.entries()) {
    const label = heading[1] ?? "";
    if (!/^\d{4}-\d{2}-\d{2}$/u.test(label)) errors.push(`DEVLOG_DATE: invalid entry date ${label}`);
    dates.push(label);
    const start = (heading.index ?? 0) + heading[0].length;
    const end = headings[position + 1]?.index ?? text.length;
    const nextValues = [...text.slice(start, end).matchAll(/^- Next:\s*(.+)$/gmu)].map(
      (match) => match[1]?.trim() ?? "",
    );
    if (nextValues.length !== 1) errors.push(`DEVLOG_NEXT: entry ${label} needs exactly one '- Next:' line`);
    if (position === 0 && nextValues.length === 1 && nextValues[0]?.replaceAll("`", "").toLowerCase() !== "none") {
      const references = nextValues[0]?.match(/[A-Z][A-Z0-9]*-[0-9]{3,}/gu) ?? [];
      if (references.length === 0)
        errors.push(`DEVLOG_NEXT: '${nextValues[0]}' must reference an active task ID or none`);
      for (const taskId of references) if (!taskIds.has(taskId)) errors.push(`DEVLOG_TASK_MISSING: ${taskId}`);
    }
  }
  if (dates.join("\n") !== [...dates].sort().reverse().join("\n"))
    errors.push("DEVLOG_ORDER: dated entries must be newest first");
}

function validatePlans(root: string, tasks: Task[], errors: string[]): void {
  const owners = new Map<string, string[]>();
  for (const task of tasks) {
    if (!Array.isArray(task.links)) continue;
    for (const link of task.links) {
      if (typeof link !== "string") continue;
      owners.set(link, [...(owners.get(link) ?? []), task.id]);
    }
  }
  const activeByTask = new Map<string, string[]>();
  for (const path of listMarkdown(resolve(root, "docs/plans"))) {
    if (path.endsWith(`${sep}README.md`)) continue;
    const relativePath = relative(root, path).split(sep).join("/");
    const status = readText(path).match(/^- Status:\s*(.+?)\s*$/mu)?.[1];
    if (status === undefined) {
      errors.push(`PLAN_STATUS: ${relativePath} needs '- Status:'`);
      continue;
    }
    const planOwners = owners.get(relativePath) ?? [];
    if (["Planned", "In progress", "Blocked"].includes(status)) {
      if (planOwners.length !== 1)
        errors.push(`PLAN_QUEUE: ${relativePath} with status ${status} needs exactly one queue owner`);
      else activeByTask.set(planOwners[0] ?? "", [...(activeByTask.get(planOwners[0] ?? "") ?? []), relativePath]);
    }
    if (["Done", "Superseded"].includes(status) && planOwners.length > 0) {
      errors.push(`PLAN_CLOSED_QUEUED: ${relativePath} -> ${planOwners.join(", ")}`);
    }
    if (!PLAN_STATUSES.has(status)) errors.push(`PLAN_STATUS_INVALID: ${relativePath} -> ${status}`);
  }
  for (const [taskId, plans] of activeByTask) {
    if (plans.length > 1) errors.push(`TASK_MULTIPLE_PLANS: ${taskId} -> ${plans.sort().join(", ")}`);
  }
}

function validateScratch(root: string, today: Date, errors: string[]): void {
  for (const path of listMarkdown(resolve(root, "docs/scratch"))) {
    if (path.endsWith(`${sep}README.md`) || path.endsWith(".local.md") || path.split(sep).includes("local")) continue;
    const relativePath = relative(root, path).split(sep).join("/");
    const frontmatter = readText(path).match(/^---\s*\n([\s\S]*?)\n---\s*\n/u)?.[1];
    if (frontmatter === undefined) {
      errors.push(`SCRATCH_FRONTMATTER: ${relativePath}`);
      continue;
    }
    const metadata = parse(frontmatter);
    if (!isRecord(metadata) || metadata.status !== "scratch") {
      errors.push(`SCRATCH_STATUS: ${relativePath} must declare status: scratch`);
      continue;
    }
    const created = parseDate(metadata.created, `${relativePath}.created`, errors);
    const expires = parseDate(metadata.expires, `${relativePath}.expires`, errors);
    if (created !== undefined && expires !== undefined) {
      if (expires <= today)
        errors.push(`SCRATCH_EXPIRED: ${relativePath} expired on ${expires.toISOString().slice(0, 10)}`);
      if (expires.valueOf() > created.valueOf() + 45 * 86_400_000)
        errors.push(`SCRATCH_TTL: ${relativePath} may live for at most 45 days`);
    }
    if (typeof metadata.task !== "string" || metadata.task.trim().length === 0) {
      errors.push(`SCRATCH_TASK: ${relativePath} must name its owning task or direct request`);
    }
  }
}

function markdownLinks(text: string): string[] {
  const links: string[] = [];
  let fenced = false;
  for (const line of text.split(/\r?\n/u)) {
    if (line.trimStart().startsWith("```")) {
      fenced = !fenced;
      continue;
    }
    if (fenced) continue;
    for (const match of line.matchAll(/(?<!!)\[[^\]]+\]\(([^)]+)\)/gu)) {
      let target = match[1]?.trim() ?? "";
      if (target.startsWith("<") && target.endsWith(">")) target = target.slice(1, -1);
      else if (target.includes(' "')) target = target.split(' "', 1)[0] ?? "";
      links.push(target);
    }
  }
  return links;
}

function validateLinks(root: string, errors: string[]): void {
  const candidates = ["README.en.md", "AGENTS.md", "CONTRIBUTING.md"].map((path) => resolve(root, path));
  candidates.push(...listMarkdown(resolve(root, "docs")));
  for (const source of candidates) {
    if (!existsSync(source)) continue;
    for (const rawTarget of markdownLinks(readText(source))) {
      if (/^(#|https?:\/\/|mailto:|tel:)/u.test(rawTarget)) continue;
      const target = decodeURIComponent(rawTarget.split("#", 1)[0] ?? "");
      if (target.length === 0) continue;
      const relativeSource = relative(root, source).split(sep).join("/");
      if (target.startsWith("/")) errors.push(`LINK_ABSOLUTE: ${relativeSource} -> ${rawTarget}`);
      else {
        const resolved = resolve(dirname(source), target);
        if (!isInside(root, resolved)) errors.push(`LINK_ESCAPE: ${relativeSource} -> ${rawTarget}`);
        else if (!existsSync(resolved)) errors.push(`LINK_MISSING: ${relativeSource} -> ${rawTarget}`);
      }
    }
  }
}

export function validateDocs(root: string, today = new Date()): { errors: string[]; tasks: Task[] } {
  const normalizedRoot = resolve(root);
  const errors: string[] = [];
  validateStructure(normalizedRoot, errors);
  const tasks = validateTasks(normalizedRoot, errors);
  validateDevlog(normalizedRoot, new Set(tasks.map((task) => task.id)), errors);
  validatePlans(normalizedRoot, tasks, errors);
  validateScratch(normalizedRoot, today, errors);
  validateLinks(normalizedRoot, errors);
  return { errors: [...new Set(errors)].sort(), tasks };
}

function main(): number {
  const arguments_ = process.argv.slice(2);
  const command = arguments_[0];
  if (command !== "check" && command !== "tasks") {
    console.error("Usage: pnpm docs <check|tasks> [--ready] [--today YYYY-MM-DD]");
    return 2;
  }
  const todayIndex = arguments_.indexOf("--today");
  const todayValue = todayIndex >= 0 ? arguments_[todayIndex + 1] : undefined;
  const today = todayValue === undefined ? new Date() : new Date(`${todayValue}T00:00:00.000Z`);
  const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
  const result = validateDocs(root, today);
  if (result.errors.length > 0) {
    for (const error of result.errors) console.error(error);
    return 1;
  }
  if (command === "tasks") {
    const readyOnly = arguments_.includes("--ready");
    const selected = result.tasks.filter((task) => !readyOnly || (task.status === "ready" && !task.depends_on));
    if (selected.length === 0) console.log(readyOnly ? "No actionable tasks." : "Task queue is empty.");
    for (const task of selected)
      console.log(
        `${task.id} [${String(task.priority)} ${String(task.status)}] ${String(task.title)} — ${String(task.owner ?? "unassigned")}`,
      );
  } else console.log(`Documentation contract is valid (${result.tasks.length} active task(s)).`);
  return 0;
}

const invokedPath = process.argv[1];
if (invokedPath !== undefined && import.meta.url === pathToFileURL(resolve(invokedPath)).href) {
  process.exitCode = main();
}
