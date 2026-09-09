---
name: blueprint
description: 使用 Python Blueprint 模板创建项目时阅读。
---

# Blueprint

[English](README.md) | 简体中文

## 概述

Blueprint 是严格的 Python 项目模板，提供一个 SDK、轻量 CLI 和 Heaven Style 智能体指南。本分支包含当前的 `0.2.0-alpha.1` 模板。

[![CI](https://github.com/Magolor/Blueprint/actions/workflows/code-quality.yml/badge.svg?branch=python)](https://github.com/Magolor/Blueprint/actions/workflows/code-quality.yml) [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Alpha](https://img.shields.io/badge/version-0.2.0--alpha.1-orange.svg)](CHANGELOG.md)

## 开始使用

在此上游仓库中，运行完整检查前请先获取两个产品分支。对于新模板仓库或解压后的归档，请先完成“创建自己的项目”，包括调整仅适用于上游的分支一致性检查。

请使用 Python 3.10 至 3.14 及 uv。

```bash
uv sync --all-extras --frozen
bash scripts/check.bash full
uv run bp --help
```

请通过已构建或已安装的包使用公开 SDK：

```python
from blueprint import get_project_info

print(get_project_info())
```

结果包含项目名称、版本和输出格式。配置经过验证且不可变。`BLUEPRINT_PROJECT_NAME` 和 `BLUEPRINT_OUTPUT` 控制 CLI 输出；支持 `text` 和 `json` 两种格式。

## 创建自己的项目

1. 从模板创建仓库，并选择所需的产品分支。
2. 更新清单、源码、测试和根目录文档中的包、导入、CLI、作者及仓库标识。
3. 替换 `AGENTS.md` 和 `BLUEPRINT.md` 中的上游政策，并更新引用信息、联系方式、徽章及发布责任。
4. 产品重命名时不要修改 Heaven Style。若项目不维护共享目录树约定，请移除双分支一致性检查。
5. 更新锁文件及生成的 README，然后运行上述完整检查命令。

## 目录职责

| 路径 | 用途 |
| --- | --- |
| `src/` | 一个原生 SDK 与 CLI 包。 |
| `tests/` | 公开行为、失败场景与工具契约。 |
| `scripts/` | 仓库检查、生成与发布准备。 |
| `docs/` | 工程指南、统一任务队列与开发证据。 |
| `.agents/skills/heaven-style/` | 规范的共享智能体指南。 |

仅在确有职责时添加目录或包。模板中的空目录不意味着需要应用框架、数据库、GUI 或服务。

## Heaven Style

使用以下命令安装或替换标准本地 Skill。TypeScript 模板仅为此独立 Python 工具使用 uv。

```bash
uv run python .agents/skills/heaven-style/scripts/install.py
```

默认目标为 `~/.agents/skills/heaven-style`。需要 Claude 插件桥接时使用 `--all-harnesses`。

## 发布与项目信息

`typescript` 是托管默认分支；`python` 是 Python 模板。两者的 Heaven Style 目录树相同。Python 包采用等价版本号 `0.2.0a1`。

经验证的模板归档请参阅[发布准备](docs/resources/release.md)。准备归档不会发布包或 GitHub 版本。

另请参阅[贡献指南](CONTRIBUTING.zh.md)、[支持](SUPPORT.zh.md)、[安全政策](SECURITY.zh.md)、[行为准则](CODE_OF_CONDUCT.zh.md)、[更新日志](CHANGELOG.zh.md)和[致谢](ACKNOWLEDGEMENTS.zh.md)。引用元数据见 [CITATION.cff](CITATION.cff)；项目采用 [MIT 许可证](LICENSE)。

[工程指南](docs/README.md)提供文档导航。`docs/tasks.yaml` 是唯一的实时任务队列。
