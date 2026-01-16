# Skill Creator (技能创建器)

## 概述

Skill Creator 是一个完整的技能创建和管理工具集，提供技能设计的最佳实践、模板和自动化工具。它帮助你快速创建、验证和打包符合规范的技能。

## 适用场景

- 创建新的自定义技能
- 更新和改进现有技能
- 学习技能设计模式和最佳实践
- 理解技能架构和组织方式
- 验证技能结构的正确性
- 打包技能为可分发的 `.skill` 文件

## 核心工具

### 1. init_skill.py - 技能初始化工具

**位置**: [`skills/skill-creator/scripts/init_skill.py`](../skills/skill-creator/scripts/init_skill.py)

**功能**: 从模板创建新技能目录结构

**用法**:
```bash
skills/skill-creator/scripts/init_skill.py <skill-name> --path <output-directory> \
  [--resources scripts,references,assets] [--examples]
```

**参数说明**:
- `<skill-name>` - 技能名称（将自动规范化为小写连字符格式）
- `--path` - 技能目录的输出路径（必需）
- `--resources` - 要创建的资源目录，逗号分隔（可选）
- `--examples` - 在资源目录中创建示例文件（可选）

**示例**:

创建基础技能（仅 SKILL.md）:
```bash
python3 skills/skill-creator/scripts/init_skill.py my-skill --path .
```

创建包含脚本和参考文档的技能:
```bash
python3 skills/skill-creator/scripts/init_skill.py my-skill --path . \
  --resources scripts,references
```

创建完整技能（包含所有资源类型和示例）:
```bash
python3 skills/skill-creator/scripts/init_skill.py my-skill --path . \
  --resources scripts,references,assets --examples
```

**生成的结构**:
```
my-skill/
├── SKILL.md              # 技能文档模板（包含 TODO 提示）
├── scripts/              # 可执行脚本目录（如果指定）
│   └── example.py       # 示例脚本（如果使用 --examples）
├── references/           # 参考文档目录（如果指定）
│   └── api_reference.md # 示例参考文档（如果使用 --examples）
└── assets/               # 资产文件目录（如果指定）
    └── example_asset.txt # 示例资产（如果使用 --examples）
```

### 2. package_skill.py - 技能打包工具

**位置**: [`skills/skill-creator/scripts/package_skill.py`](../skills/skill-creator/scripts/package_skill.py)

**功能**: 验证并打包技能为 `.skill` 文件（带 .skill 扩展名的 zip 文件）

**用法**:
```bash
skills/skill-creator/scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

**参数说明**:
- `<path/to/skill-folder>` - 技能目录路径（必需）
- `[output-directory]` - 输出目录（可选，默认为当前目录）

**示例**:

打包技能到当前目录:
```bash
python3 skills/skill-creator/scripts/package_skill.py ./my-skill
```

打包技能到指定目录:
```bash
python3 skills/skill-creator/scripts/package_skill.py ./my-skill ./dist
```

**验证检查**:

打包脚本会自动验证以下内容：
- YAML 前置元数据格式和必需字段（name、description）
- 技能命名规范（小写、连字符、长度限制）
- 目录结构正确性
- Description 的完整性和质量
- 文件组织和资源引用

如果验证失败，脚本会报告错误并退出。修复错误后重新运行打包命令。

### 3. quick_validate.py - 快速验证工具

**位置**: [`skills/skill-creator/scripts/quick_validate.py`](../skills/skill-creator/scripts/quick_validate.py)

**功能**: 快速验证技能结构而不打包

**用法**:
```bash
skills/skill-creator/scripts/quick_validate.py <path/to/skill-folder>
```

**示例**:
```bash
python3 skills/skill-creator/scripts/quick_validate.py ./my-skill
```

## 技能创建工作流程

### 步骤 1: 理解需求

明确技能应该支持的具体用例。提出以下问题：
- 这个技能要解决什么问题？
- 用户会在什么场景下使用它？
- 需要哪些具体功能？

### 步骤 2: 规划资源

分析需要包含哪些可重用资源：
- **scripts/** - 需要重复编写的代码（如 PDF 旋转、数据处理）
- **references/** - 详细的参考材料（如 API 文档、数据库架构）
- **assets/** - 输出中使用的文件（如模板、图标、字体）

### 步骤 3: 初始化技能

使用 `init_skill.py` 创建技能框架：

```bash
python3 skills/skill-creator/scripts/init_skill.py <skill-name> --path . \
  --resources <需要的资源类型> [--examples]
```

### 步骤 4: 编辑 SKILL.md

完成 SKILL.md 中的所有 TODO 项：

**前置元数据（YAML）**:
```yaml
---
name: skill-name
description: 详细描述技能的功能和使用时机。包括 WHEN 信息 - 具体的触发场景、文件类型或任务。
---
```

**正文内容**:
- 选择合适的组织模式（工作流程、任务、参考、能力）
- 提供清晰的示例
- 引用脚本和资源
- 保持简洁（目标 <500 行）

### 步骤 5: 添加资源

根据规划添加实际的资源文件：
- 在 `scripts/` 中添加可执行脚本
- 在 `references/` 中添加参考文档
- 在 `assets/` 中添加模板或资产文件

**重要**: 删除不需要的示例文件。

### 步骤 6: 测试脚本

运行所有脚本确保它们正常工作：
```bash
python3 my-skill/scripts/my_script.py --help
python3 my-skill/scripts/my_script.py <测试参数>
```

### 步骤 7: 验证和打包

验证技能结构：
```bash
python3 skills/skill-creator/scripts/quick_validate.py ./my-skill
```

打包技能：
```bash
python3 skills/skill-creator/scripts/package_skill.py ./my-skill
```

### 步骤 8: 迭代改进

在实际使用中测试技能，根据反馈进行改进。

## 技能设计模式

### 1. 工作流程导向模式

**适用于**: 有明确步骤的顺序流程

**结构**:
```markdown
## Overview
## Workflow Decision Tree
## Step 1: ...
## Step 2: ...
```

**示例**: DOCX 技能（读取 → 创建 → 编辑）

### 2. 任务导向模式

**适用于**: 提供不同操作/能力的工具集

**结构**:
```markdown
## Overview
## Quick Start
## Task Category 1
## Task Category 2
```

**示例**: PDF 技能（合并、拆分、提取文本）

### 3. 参考/指南模式

**适用于**: 标准、规范或要求

**结构**:
```markdown
## Overview
## Guidelines
## Specifications
## Usage
```

**示例**: 品牌指南（颜色、字体、特性）

### 4. 能力导向模式

**适用于**: 集成系统的多个相关功能

**结构**:
```markdown
## Overview
## Core Capabilities
### 1. Feature
### 2. Feature
```

**示例**: 产品管理技能

## 核心设计原则

### 1. 简洁至上

上下文窗口是公共资源。只添加 AI 助手不具备的知识。

**检查点**:
- "AI 助手真的需要这个解释吗？"
- "这段文字值得占用 token 吗？"

### 2. 渐进式披露

使用三级加载系统：
1. **元数据** - 始终在上下文（~100 词）
2. **SKILL.md 正文** - 技能触发时加载（<5k 词）
3. **资源文件** - 按需加载（无限制）

保持 SKILL.md 在 500 行以内。将详细内容分离到 references/ 文件。

### 3. 适当的自由度

根据任务性质设置具体程度：

| 自由度 | 形式 | 适用场景 |
|--------|------|----------|
| 高 | 文本说明 | 多种方法有效，依赖上下文决策 |
| 中 | 伪代码/带参数脚本 | 存在首选模式，允许一定变化 |
| 低 | 具体脚本 | 操作脆弱，需要一致性 |

## 最佳实践

### SKILL.md 编写

1. **使用祈使语气** - "创建表"而不是"创建表格的方法"
2. **提供具体示例** - 真实用例胜于抽象描述
3. **引用资源** - 明确说明何时使用哪个脚本或参考文档
4. **避免嵌套引用** - 所有引用从 SKILL.md 直接链接
5. **包含目录** - 对于 >100 行的参考文件添加目录

### 资源组织

1. **scripts/** - 可执行、经过测试、有清晰的帮助信息
2. **references/** - 结构化、可搜索、按主题组织
3. **assets/** - 说明用途、提供使用示例

### 命名规范

1. **技能名称** - 小写、连字符、描述性（如 `pdf-editor`）
2. **脚本文件** - 下划线、动词开头（如 `rotate_pdf.py`）
3. **参考文档** - 下划线、主题名（如 `api_reference.md`）

## 常见问题

### Q: 何时应该创建新技能？

**A**: 当你发现自己重复执行相同的工作流程，或需要特定领域的专业知识时。

### Q: 技能和脚本的区别是什么？

**A**: 技能是完整的知识包（包括工作流程、说明、脚本）。脚本只是可执行代码。

### Q: SKILL.md 应该多长？

**A**: 目标在 500 行以内。超过时，将详细内容移到 references/ 文件。

### Q: 何时使用 references/ vs assets/?

**A**: 
- **references/** - AI 助手需要读取的文档（API 文档、架构）
- **assets/** - 输出中使用的文件（模板、图片）

### Q: 如何组织大型技能？

**A**: 使用域或框架来组织 references/（如 `references/aws.md`、`references/gcp.md`）

## 参考资源

- 完整指南: [`skills/skill-creator/SKILL.md`](../skills/skill-creator/SKILL.md)
- 初始化脚本: [`init_skill.py`](../skills/skill-creator/scripts/init_skill.py)
- 打包脚本: [`package_skill.py`](../skills/skill-creator/scripts/package_skill.py)
- 验证脚本: [`quick_validate.py`](../skills/skill-creator/scripts/quick_validate.py)

## 示例技能

参考仓库中的其他技能了解实际应用：
- [SQLite DB Ops](sqlite-db-ops.md) - 数据库操作技能，展示脚本使用
- 更多技能示例请参见各技能目录

---

**最后更新**: 2026-01-14
