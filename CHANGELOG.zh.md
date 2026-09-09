---
name: blueprint-changelog
description: 查阅用户可见的 alpha 变更与发布状态。
---

# 更新日志

[English](CHANGELOG.md) | 简体中文

## 概述

本文件记录当前 alpha 模板。详细验证结果见[开发日志](docs/DEVLOG.md)。

## 0.2.0-alpha.1 — 发布候选版本

- 独立的 TypeScript 与 Python 模板，各自提供一个 SDK 和轻量 CLI。
- 严格的配置验证、不可变结果，以及有明确目标的行为与产物检查。
- Heaven Style 区分角色、工作流和任务，并提供具体的判断、评审与交接流程。
- 修正 Heaven Style：由领域对象拥有 API，分别展开五项 SOLID 原则，补全成对词汇与别名，并明确 clean 与共享工具规则的入口。
- KV 配置、包内静态资源、ORM 优先的 SQL、逻辑错误守卫、稳定前缀导入顺序与命名参数指导。
- 双语入口及社区文档、引用元数据，以及可重复生成的模板归档。

此 alpha 仅维护当前接口。Python 包版本写作 `0.2.0a1`；模板和 Skill 使用 `0.2.0-alpha.1`。发布状态以 GitHub 预发布记录为准。
