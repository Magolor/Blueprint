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
uv run blueprint --help
uv run blueprint --version
uv run blueprint setup
uv run blueprint init
uv run blueprint config list
uv run blueprint cfg get blueprint.project.name
uv run blueprint pj demos .temp --abs
uv run blueprint-gui --help
```

CLI 使用 HeavenBase 工具类处理项目配置和路径解析。

HeavenBase 被声明为普通运行时依赖，并从 PyPI 解析（`heavenbase==0.1.1.0`）。本地 HeavenBase 开发可以运行 `scripts/sync-env.bash --heavenbase-source`，从 `HEAVENBASE_SOURCE`、`../HeavenBase/HeavenBase` 或 `HEAVENBASE_REPO_URL` 安装可编辑源码覆盖。

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
| `docs/resources/` | 稳定的项目参考资料和背景。 |
| `docs/progress/` | 按日期组织的进展文件夹，包含每日摘要和可选详细记录。 |
| `tests/` | 为空的测试根目录，供未来项目添加具体测试。 |
| `demos/` | 为空的演示根目录，供未来项目添加具体演示。 |
| `demos/assets/` | 已提交的演示夹具。 |
| `demos/.temp/` | 被忽略的演示运行时数据。 |
| `.agents/skills/heaven-style/` | 从 HeavenBase 复制的仓库本地 Heaven-style agent skill。 |
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

Blueprint 包含位于 `.github/workflows/release.yml` 的 PyPI trusted publishing 工作流。它只在推送到 `release` 分支且 head commit 消息包含 `[release]` 时运行。

首次发布前，需要在 PyPI 为 GitHub 仓库、`release.yml` 工作流和 `pypi` environment 配置信任发布，并在 GitHub 中创建同名 `pypi` environment。

从干净的 `master` 分支发布：

```bash
bash scripts/release.bash
```

该脚本会在 `master` 上创建或复用 `[release]` commit，推送 `master`，将 `release` 从 `master` 快进，然后推送 `release` 触发发布工作流。

## 文档策略

英文 doc-sync 通过 `.agents/skills/heaven-style/references/tasks/doc-sync.md` 更新权威英文文档和生成文档。中文或其他语言翻译应在英文变更完成后，通过 `.agents/skills/heaven-style/references/tasks/doc-trans.md` 单独刷新。
