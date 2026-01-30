# OMO Model Manager (oh-my-opencode 模型管理器)

## 概述

OMO Model Manager 是用于管理 **oh-my-opencode** 的 agent 和 category 模型配置的技能。通过命令行脚本，你可以查看当前配置、修改单个或批量替换模型，便于在提供商订阅变更（如取消 GitHub Copilot、添加 Google Antigravity）时快速调整。

## 适用场景

此技能适用于以下场景：

- 查看当前所有 agent/category 的模型配置
- 修改特定 agent 或 category 的模型
- 按提供商批量替换模型（如取消某提供商订阅后统一替换）
- 查看 opencode 提供的可用模型列表
- 查找使用某提供商的配置项

## 核心工具

### manage_models.py - 模型管理脚本

**位置**: [`skills/omo-model-manager/scripts/manage_models.py`](../skills/omo-model-manager/scripts/manage_models.py)

**功能**: 读写 `~/.config/opencode/oh-my-opencode.json`，支持列出、设置、替换、查找模型配置

**支持的子命令**:
- `list` - 列出所有 agent 和 category 的当前模型
- `providers` - 按提供商分组显示使用情况
- `models` - 从 opencode 获取可用模型列表
- `set` - 设置单个 agent 或 category 的模型
- `replace` - 按提供商前缀批量替换（支持 `--apply` 执行）
- `find` - 查找使用指定提供商的配置

## 配置文件

| 文件 | 说明 |
|------|------|
| `~/.config/opencode/oh-my-opencode.json` | oh-my-opencode 主配置（agent/category 模型映射） |
| `~/.config/opencode/opencode.json` | opencode 模型定义等 |

## 使用方法

### 1. 查看当前配置

```bash
python3 skills/omo-model-manager/scripts/manage_models.py list
```

显示所有 agent 和 category 的当前模型配置。

### 2. 查看提供商使用情况

```bash
python3 skills/omo-model-manager/scripts/manage_models.py providers
```

按提供商分组显示哪些配置在使用该提供商。

### 3. 查看可用模型

```bash
python3 skills/omo-model-manager/scripts/manage_models.py models
```

从 `opencode models` 命令获取所有可用模型（依赖本地 opencode CLI）。

### 4. 修改单个 agent 或 category

```bash
# 修改 agent
python3 skills/omo-model-manager/scripts/manage_models.py set agent sisyphus google/antigravity-claude-opus-4-5-thinking max

# 修改 category
python3 skills/omo-model-manager/scripts/manage_models.py set category writing google/antigravity-gemini-3-flash
```

### 5. 批量替换提供商

当取消某个提供商订阅时，可批量替换为其他提供商：

```bash
# 仅预览将要进行的更改（不写文件）
python3 skills/omo-model-manager/scripts/manage_models.py replace github-copilot google

# 执行实际替换并写回配置文件
python3 skills/omo-model-manager/scripts/manage_models.py replace github-copilot google --apply
```

### 6. 查找特定提供商的配置

```bash
python3 skills/omo-model-manager/scripts/manage_models.py find github-copilot
```

列出所有使用 `github-copilot` 的 agent/category 及当前模型。

## Agent 和 Category 参考

详细的 agent/category 说明和推荐模型请参阅技能内 [references/models.md](../skills/omo-model-manager/references/models.md)。

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

### 取消 GitHub Copilot 订阅

```bash
# 1. 查看使用 github-copilot 的配置
python3 skills/omo-model-manager/scripts/manage_models.py find github-copilot

# 2. 预览替换为 google 的变更
python3 skills/omo-model-manager/scripts/manage_models.py replace github-copilot google

# 3. 确认后执行替换
python3 skills/omo-model-manager/scripts/manage_models.py replace github-copilot google --apply
```

注意：不同提供商的模型 ID 可能需手动映射（如 `github-copilot/claude-sonnet-4.5` → `google/antigravity-claude-sonnet-4-5`），脚本按前缀替换，若目标提供商无对应模型需再单独 `set` 调整。

### 取消 OpenAI 订阅

```bash
python3 skills/omo-model-manager/scripts/manage_models.py find openai
# 根据输出逐个或批量替换为 github-copilot / google 的对应模型
```

### 新增 Google Antigravity 后统一迁移

```bash
# 先 list 或 providers 了解当前分布，再按需 replace 或逐项 set
python3 skills/omo-model-manager/scripts/manage_models.py providers
python3 skills/omo-model-manager/scripts/manage_models.py set agent sisyphus google/antigravity-claude-opus-4-5-thinking max
```

## 最佳实践

1. **先预览再写入**：`replace` 不加 `--apply` 时只打印将要修改的内容，确认无误后再加 `--apply`。
2. **备份配置**：执行批量替换前可复制 `~/.config/opencode/oh-my-opencode.json` 做备份。
3. **结合 models 子命令**：修改前用 `models` 查看当前 opencode 可用模型，避免写入无效 ID。

## 参考资源

- 技能文档: [`skills/omo-model-manager/SKILL.md`](../skills/omo-model-manager/SKILL.md)
- 脚本源码: [`manage_models.py`](../skills/omo-model-manager/scripts/manage_models.py)
- 模型与提供商参考: [`references/models.md`](../skills/omo-model-manager/references/models.md)

---

**最后更新**: 2026-01-30
