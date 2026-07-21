# Blueprint

Blueprint 是一个以 uv 为核心的 Python 起始项目模板，用于创建未来的仓库。

`README.en.md` 是英文 README 的权威来源。`README.md` 由 `scripts/sync-readme.bash` 和 Git pre-commit hook 从它生成。`README.zh.md` 等翻译文档通过仓库本地的文档翻译流程单独维护。

## 快速开始

```bash
bash scripts/sync-env.bash
bash scripts/flake.bash --ci
bash scripts/test.bash
uv build
```

## CLI

```bash
uv run bp --help
uv run bp --version
uv run bp setup
uv run bp init
uv run bp config list
uv run bp cfg get blueprint.project.name
uv run bp pj demos .temp --abs
uv run blueprint-gui --help
```

CLI 使用 HeavenBase 工具类处理项目配置和路径解析。

HeavenBase 被声明为普通运行时依赖，并通过 `requirements.txt` 从 PyPI 解析。本地 HeavenBase 开发可以运行 `scripts/sync-env.bash --heavenbase-source`，从 `HEAVENBASE_SOURCE`、`../HeavenBase/HeavenBase` 或 `HEAVENBASE_REPO_URL` 安装可编辑源码覆盖。

## 模板重命名

使用 `scripts/rename.bash` 将 Blueprint 改造成具体项目，并分别设置展示名、发行包名、导入包名和 CLI 名称：

```bash
bash scripts/rename.bash \
  --project-name "My Project" \
  --dist-name my-project \
  --import-name my_project \
  --cli-name my-tool \
  --yes
bash scripts/sync-env.bash
```

## 布局

| 路径 | 用途 |
|------|------|
| `src/blueprint/` | 可导入的 Python 包和默认 SDK 表面。 |
| `src/blueprint/version.py` | 包版本的单一来源。 |
| `src/blueprint/resources/` | 包资源文件。 |
| `src/blueprint/utils/` | 共享工具代码。 |
| `docs/README.md` | 项目文档菜单和权威地图。 |
| `docs/goals/` | 长期、中期和短期项目目标。 |
| `docs/DEVLOG.md` | 单一、滚动的开发变更与交接日志。 |
| `docs/tasks.template.yaml` | 模板模式下保持为空；初始化后提升为项目的 `docs/tasks.yaml`。 |
| `docs/scratch/` | 有所有者和过期时间的短期笔记。 |
| `docs/resources/` | 稳定的项目参考资料和背景。 |
| `docs/plans/` | 从属于单一任务权威的多阶段执行细节。 |
| `docs/reports/` | 审查、重构和调研的证据快照。 |
| `tests/` | 行为、文档契约与模板同步测试。 |
| `demos/` | 可运行的演示和项目起始示例。 |
| `demos/assets/` | 已提交的演示夹具。 |
| `demos/.temp/` | 被忽略的演示运行时数据。 |
| `.agents/skills/heaven-style/` | Blueprint 维护的 Heaven-style agent skill 权威源码。 |
| `.github/workflows/` | GitHub Actions CI。 |
| `.githooks/` | 用于 README 同步和本地格式检查的 Git hooks。 |
| `scripts/` | 可复用的 uv 脚本包装器。 |

## 环境策略

先编辑 `requirements.txt` 与 `requirements-dev.txt`。`pyproject.toml` 通过 setuptools 动态元数据读取它们；`bash scripts/sync-env.bash` 会刷新 `uv.lock`、`poetry.lock` 和 `environment-dev.yml`。

安装优先级：**uv → pip（requirements）→ pyproject → conda → poetry**。

1. **uv** — 运行 `bash scripts/sync-env.bash`（默认 `uv sync --all-extras`，安装运行时与全部 optional extras）。
2. **pip** — 使用 `requirements*.txt` 或 `pip install -e ".[dev]"`。
3. **pyproject** — 仅承载包元数据，不在此处重复写依赖 pin。
4. **conda** — 生成的 `environment-dev.yml` 仅包含 `-e ".[dev]"`。
5. **poetry** — 可选；安装 Poetry 后由 `bash scripts/sync-env.bash` 刷新 `poetry.lock`。

CI 应使用 `bash scripts/sync-env.bash --check --no-heavenbase` 作为生成文件漂移检查。

`scripts/sync-env.bash --heavenbase-source` 是本地 HeavenBase 开发的临时源码覆盖。当相邻 checkout 缺失、GitHub 或配置的远端为私有、SSH/HTTPS 凭据不可用、代理/VPN 阻断 Git，或远端分支无法快进时，它可能失败。普通模板用户应依赖 PyPI 依赖。

## Agent 设置

`AGENTS.md` 是新项目的脚手架。复制 Blueprint 后，应为真实项目重写它：指向项目文档地图，替换包路径和命令，记录 issue tracker 行为，并删除只属于模板的说明。

## 发布策略

Blueprint 不发布到同名的第三方 PyPI 项目。正式版本是位于已发布 `master` 头部、名称与 `src/blueprint/version.py` 完全一致的四段式 annotated tag：`v<version>`。`.github/workflows/release.yml` 会独立验证 tag、运行 Python 3.10–3.13 的完整源码检查、构建并测试 wheel 与 sdist，然后把不可覆盖的产物附加到 GitHub Release。

从干净的 `master` 分支发布：

```bash
bash scripts/release.bash
```

该脚本拒绝开发版本、脏工作区、非 `master` 分支、分叉历史、lightweight tag 和 tag/version 冲突；在需要时先推送 `master`，然后创建或复用 annotated tag 并推送它。对同一个已经发布的 tag 重跑是幂等的。

## 文档策略

文档分为四个明确表面：面向用户的 `README.en.md`（`README.md` 和包内副本由它生成）、面向工程师/agent/架构师的 `docs/README.md` 及其稳定资料、单一滚动的 `docs/DEVLOG.md`，以及会过期的 `docs/scratch/` 或本地 `.temp/notes/`。Blueprint 作为模板源码没有实时任务队列；`docs/tasks.template.yaml` 必须保持为空，只有 `scripts/rename.bash` 初始化具体项目时才会变成 `docs/tasks.yaml`。

英文 doc-sync 通过 `.agents/skills/heaven-style/references/tasks/doc-sync.md` 更新权威英文文档和生成文档。中文或其他语言翻译应在英文变更完成后，通过 `.agents/skills/heaven-style/references/tasks/doc-trans.md` 单独刷新。
