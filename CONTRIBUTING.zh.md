---
name: blueprint-contributing
description: 修改 Blueprint 代码或文档前阅读。
---

# 贡献指南

[English](CONTRIBUTING.md) | 简体中文

## 概述

请先阅读[仓库政策](AGENTS.md)和[工程指南](docs/README.md)。每次变更聚焦一个结果，开始需持续推进的工作前先查阅统一任务队列。

## 检查变更

请使用声明的运行时与包管理器。实现过程中运行相关检查，评审前运行完整检查。

```bash
uv sync --all-extras --frozen
bash scripts/check.bash full
```

请保留一个原生包和一个公开 SDK 入口。验证外部输入，保留有效的失败场景覆盖，并在接口变更时更新所有自有调用方。不要为已移除的 alpha 接口添加兼容别名。

## 文档与共享 Skill

英文页面为规范来源。请使 `.zh.md` 对应文件在含义、行结构和代码上保持一致。`README.md` 由 `README.en.md` 生成。

仅在 Blueprint 中编辑 Heaven Style，并将其完整目录树同步到两个产品分支。本地提交钩子检查候选变更；完整检查还验证两个已提交分支的一致性。

请使用拉取请求模板，说明行为、验证结果与重要限制。贡献内容采用 [MIT 许可证](LICENSE)。
