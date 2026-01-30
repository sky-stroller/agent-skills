# General Skills 通用技能集合

这是一个通用技能（Skills）仓库，包含了可扩展 AI 助手能力的模块化技能包。每个技能都是独立的、自包含的包，提供专业知识、工作流程和工具集成。

## 📋 目录

- [General Skills 通用技能集合](#general-skills-通用技能集合)
  - [📋 目录](#-目录)
  - [什么是 Skill](#什么是-skill)
    - [技能的核心价值](#技能的核心价值)
    - [Agent Skills 开放规范](#agent-skills-开放规范)
  - [技能列表](#技能列表)
    - [1. 📦 Skill Creator (技能创建器)](#1--skill-creator-技能创建器)
    - [2. 🔧 Skill Installer (技能安装器)](#2--skill-installer-技能安装器)
    - [3. 🗄️ SQLite DB Ops (SQLite 数据库操作)](#3-️-sqlite-db-ops-sqlite-数据库操作)
    - [4. 🤖 OMO Model Manager (oh-my-opencode 模型管理器)](#4--omo-model-manager-oh-my-opencode-模型管理器)
  - [快速开始](#快速开始)
    - [在 AI 助手中使用技能](#在-ai-助手中使用技能)
    - [标准技能结构](#标准技能结构)
  - [核心原则](#核心原则)
    - [1. 简洁至上](#1-简洁至上)
    - [2. 渐进式披露](#2-渐进式披露)
    - [3. 适当的自由度](#3-适当的自由度)
  - [贡献指南](#贡献指南)
    - [贡献新技能](#贡献新技能)
    - [改进现有技能](#改进现有技能)
  - [最佳实践](#最佳实践)
  - [技能设计模式](#技能设计模式)
  - [支持](#支持)

## 什么是 Skill

技能（Skills）是模块化的、自包含的包，通过提供专业知识、工作流程和工具来扩展 **AI 助手**的能力。它们遵循 [Agent Skills 开放规范](https://agentskills.io)，是为 AI 编程助手设计的"入职指南"——将通用 AI 助手转变为配备特定领域程序性知识的专业代理。

### 技能的核心价值

技能为 AI 助手提供：

1. **专业工作流程** - 特定领域的多步骤操作流程
2. **工具集成** - 处理特定文件格式或 API 的详细说明
3. **领域专业知识** - 项目特定的知识、架构、业务逻辑
4. **打包资源** - 可复用的脚本、参考文档和资产文件

### Agent Skills 开放规范

本仓库遵循 **[Agent Skills 开放规范](https://agentskills.io)**，这是一个开放的、供应商中立的规范，定义了 AI 编程助手如何发现、加载和使用技能。

## 技能列表

### 1. 📦 Skill Creator (技能创建器)

创建和更新技能的完整指南，提供技能设计的最佳实践、模板和自动化工具。

**核心功能**: 技能初始化、验证、打包
**位置**: [`skills/skill-creator/`](skills/skill-creator/)
**详细文档**: [查看完整说明 →](docs/skill-creator.md)

### 2. 🔧 Skill Installer (技能安装器)

通用的技能安装工具，帮助用户从各种来源安装技能到不同的 AI 助手。

**核心功能**: 列出技能、安装技能、多平台支持
**位置**: [`skills/skill-installer/`](skills/skill-installer/)
**详细文档**: [查看完整说明 →](docs/skill-installer.md)

### 3. 🗄️ SQLite DB Ops (SQLite 数据库操作)

完整的 SQLite 数据库操作工具，提供全面的增删改查 (CRUD) 功能。

**核心功能**: 数据库 CRUD、批量操作、自定义 SQL
**位置**: [`skills/sqlite-db-ops/`](skills/sqlite-db-ops/)
**详细文档**: [查看完整说明 →](docs/sqlite-db-ops.md)

### 4. 🤖 OMO Model Manager (oh-my-opencode 模型管理器)

管理 oh-my-opencode 的 agent 和 category 模型配置，便于在提供商订阅变更时快速调整。

**核心功能**: 查看配置、修改模型、批量替换提供商、查看可用模型
**位置**: [`skills/omo-model-manager/`](skills/omo-model-manager/)
**详细文档**: [查看完整说明 →](docs/omo-model-manager.md)

## 快速开始

### 在 AI 助手中使用技能

技能专为 AI 编程助手设计，由 AI 助手自动发现和使用。以下是主流 AI 编程助手的技能使用指南：

| AI 助手 | 技能使用指南 |
|---------|-------------|
| **Roo Code** | [Skills 文档](https://docs.roocode.com/features/skills) |
| **Cursor** | [Skills 文档](https://cursor.com/cn/docs/context/skills) |
| **Claude Code** | [Skills 文档](https://code.claude.com/docs/en/skills) |
| **VS Code Copilot** | [Agent Skills 文档](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| **Codex** | [Skills 文档](https://developers.openai.com/codex/skills/) |
| **Antigravity** | [Skills 文档](https://antigravity.google/docs/skills) |

**安装方式**（具体步骤因 AI 助手而异）：
1. 将技能目录复制到 AI 助手的技能路径
2. 或使用 AI 助手的技能管理命令安装
3. AI 助手会自动发现并加载技能

**推荐阅读顺序**:
- **初次使用**：先查看你使用的 AI 助手的技能文档
- **安装技能**：阅读 [Skill Installer](docs/skill-installer.md) 了解如何安装技能
- **了解技能**：阅读 [SQLite DB Ops](docs/sqlite-db-ops.md) 了解技能示例
- **管理 oh-my-opencode 模型**：阅读 [OMO Model Manager](docs/omo-model-manager.md) 调整 agent/category 模型配置
- **创建技能**：阅读 [Skill Creator](docs/skill-creator.md) 学习技能开发

### 标准技能结构

每个技能遵循以下标准结构：

```
skill-name/
├── SKILL.md              # 必需：技能文档（包含 YAML 前置元数据）
├── scripts/              # 可选：可执行脚本（Python/Bash/等）
├── references/           # 可选：参考文档（按需加载到上下文）
└── assets/               # 可选：资产文件（模板、图片等，用于输出）
```

## 核心原则

### 1. 简洁至上

上下文窗口是公共资源。默认假设：AI 助手已经非常智能。只添加助手尚未掌握的上下文。

### 2. 渐进式披露

通过三级加载系统管理上下文：
- 元数据始终可见
- SKILL.md 在触发时加载
- 资源按需加载

### 3. 适当的自由度

根据任务的脆弱性和可变性匹配具体程度：
- **高自由度**（文本说明）- 多种方法有效时
- **中等自由度**（伪代码或带参数的脚本）- 存在首选模式时
- **低自由度**（特定脚本）- 操作脆弱或需要一致性时

## 贡献指南

欢迎贡献新技能或改进现有技能！

### 贡献新技能

**方式一：使用 skill-creator 技能创建（推荐）**

直接在 AI 助手中触发 skill-creator 技能，按照引导创建新技能。该技能提供：
- 交互式技能初始化流程
- 自动生成标准技能结构
- 内置验证和打包工具
- 最佳实践指导

**方式二：根据 Agent Skills 官方规范手动创建**

1. 参考 [Agent Skills 开放规范](https://agentskills.io) 了解技能标准
2. 按照[标准技能结构](#标准技能结构)创建技能目录
3. 编写符合规范的 [`SKILL.md`](skills/skill-creator/SKILL.md:1)
4. 添加必要的脚本、参考文档和资产文件
5. 使用 [`package_skill.py`](skills/skill-creator/scripts/package_skill.py) 验证技能
6. 提交 Pull Request

### 改进现有技能

1. 在实际使用中发现改进点
2. 更新相关文件
3. 测试变更
4. 提交 Pull Request

## 最佳实践

1. **保持 SKILL.md 精简** - 目标在 500 行以内
2. **使用参数化脚本** - 提高可重用性
3. **提供清晰示例** - 具体胜于抽象
4. **文档化触发场景** - 在 description 中明确说明何时使用
5. **测试脚本** - 确保所有脚本可以正常运行
6. **避免重复** - 信息应该只在一个地方维护

## 技能设计模式

详见 [`skills/skill-creator/SKILL.md`](skills/skill-creator/SKILL.md)，包括：

- 工作流程导向模式
- 任务导向模式
- 参考/指南模式
- 能力导向模式

## 支持

如有问题或建议，请：
1. 查看相关技能的 SKILL.md 文档
2. 查看 Skill Creator 指南
3. 提交 Issue 或 Pull Request
