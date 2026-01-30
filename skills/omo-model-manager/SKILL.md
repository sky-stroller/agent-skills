---
name: omo-model-manager
description: 管理 oh-my-opencode 的 agent 和 category 模型配置。当用户需要查看当前模型配置、修改特定 agent/category 的模型、按提供商批量替换模型、或在取消/添加订阅时调整配置时使用此技能。触发关键词：oh-my-opencode 模型、agent 模型、更换模型、替换提供商、模型配置。
---

# oh-my-opencode 模型管理器

管理 oh-my-opencode 的 agent 和 category 模型配置，便于在提供商订阅变更时快速调整。

## 核心功能

1. **查看配置** - 列出当前所有 agent/category 的模型
2. **修改模型** - 设置特定 agent/category 的模型
3. **批量替换** - 按提供商前缀批量替换模型
4. **查看可用模型** - 从 opencode 获取所有可用模型列表

## 配置文件

- **oh-my-opencode 配置**: `~/.config/opencode/oh-my-opencode.json`
- **模型定义**: `~/.config/opencode/opencode.json`

## 使用流程

### 场景 1: 查看当前配置

```bash
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py list
```

显示所有 agent 和 category 的当前模型配置。

### 场景 2: 查看提供商使用情况

```bash
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py providers
```

按提供商分组显示哪些配置在使用该提供商。

### 场景 3: 查看可用模型

```bash
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py models
```

从 `opencode models` 命令获取所有可用模型。

### 场景 4: 修改单个 agent/category

```bash
# 修改 agent
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py set agent sisyphus google/antigravity-claude-opus-4-5-thinking max

# 修改 category
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py set category writing google/antigravity-gemini-3-flash
```

### 场景 5: 批量替换提供商

当取消某个提供商订阅时，批量替换为其他提供商：

```bash
# 预览将要进行的更改
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py replace github-copilot google

# 执行实际替换
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py replace github-copilot google --apply
```

### 场景 6: 查找特定提供商的配置

```bash
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py find github-copilot
```

## Agent 和 Category 参考

详细的 agent/category 说明和推荐模型请参阅 [references/models.md](references/models.md)。

### Agents

| Agent | 用途 |
|-------|------|
| sisyphus | 主 orchestrator |
| prometheus | 规划师 |
| metis | 计划顾问 |
| oracle | 架构/调试专家 |
| momus | 批评者 |
| librarian | 文档/代码搜索 |
| explore | 快速代码库探索 |
| atlas | 后台任务 |
| multimodal-looker | 图像分析 |

### Categories

| Category | 用途 |
|----------|------|
| visual-engineering | 视觉/UI 工程 |
| artistry | 艺术设计 |
| ultrabrain | 复杂推理 |
| quick | 快速任务 |
| writing | 写作 |
| unspecified-low | 未指定低优先级 |
| unspecified-high | 未指定高优先级 |

## 常见替换场景

### 取消 GitHub Copilot

```bash
# 查看使用 github-copilot 的配置
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py find github-copilot

# 替换为 google antigravity（需要手动映射模型名）
# 例如：github-copilot/claude-sonnet-4.5 → google/antigravity-claude-sonnet-4-5
```

### 取消 OpenAI

```bash
python ~/.claude/skills/omo-model-manager/scripts/manage_models.py find openai
# 手动替换为 github-copilot 或 google 的对应模型
```

## 脚本参考

- [`scripts/manage_models.py`](scripts/manage_models.py) - 主管理脚本
- [`references/models.md`](references/models.md) - 模型和提供商详细参考
