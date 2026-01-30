# oh-my-opencode 模型参考

## 提供商和模型

### Google Antigravity (推荐)

通过 Antigravity OAuth 使用 Google 配额。

| 模型 ID | 名称 | Variants |
|---------|------|----------|
| `google/antigravity-claude-opus-4-5-thinking` | Claude Opus 4.5 Thinking | `low`, `max` |
| `google/antigravity-claude-sonnet-4-5-thinking` | Claude Sonnet 4.5 Thinking | `low`, `max` |
| `google/antigravity-claude-sonnet-4-5` | Claude Sonnet 4.5 | - |
| `google/antigravity-gemini-3-pro` | Gemini 3 Pro | `low`, `high` |
| `google/antigravity-gemini-3-flash` | Gemini 3 Flash | `minimal`, `low`, `medium`, `high` |

### OpenAI

需要 ChatGPT Plus 订阅。

| 模型 ID | 名称 | Variants |
|---------|------|----------|
| `openai/gpt-5.2` | GPT-5.2 | `low`, `medium`, `high` |
| `openai/gpt-5.2-codex` | GPT-5.2 Codex | `high`, `xhigh` |

### GitHub Copilot (备选)

作为其他提供商的备选。

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `github-copilot/claude-opus-4.5` | Claude Opus 4.5 | 通过 Copilot 代理 |
| `github-copilot/claude-sonnet-4.5` | Claude Sonnet 4.5 | 通过 Copilot 代理 |
| `github-copilot/claude-haiku-4.5` | Claude Haiku 4.5 | 快速响应 |
| `github-copilot/gpt-5.2` | GPT-5.2 | 通过 Copilot 代理 |
| `github-copilot/gpt-5-mini` | GPT-5 Mini | 轻量级 |

### OpenCode Zen

需要 OpenCode Zen 访问权限。

| 模型 ID | 说明 |
|---------|------|
| `opencode/claude-opus-4-5` | Claude Opus 4.5 |
| `opencode/gpt-5.2` | GPT-5.2 |
| `opencode/gpt-5-nano` | GPT-5 Nano |
| `opencode/big-pickle` | Big Pickle |

### Z.ai Coding Plan

需要 Z.ai 订阅。

| 模型 ID | 说明 |
|---------|------|
| `zai-coding-plan/glm-4.7` | GLM-4.7 |
| `zai-coding-plan/glm-4.7-flash` | GLM-4.7 Flash |

## Agent 角色说明

| Agent | 用途 | 推荐模型 |
|-------|------|----------|
| **sisyphus** | 主 orchestrator，任务执行者 | Claude Opus 4.5 Thinking (max) |
| **prometheus** | 规划师，创建工作计划 | Claude Opus 4.5 Thinking (max) |
| **metis** | 计划顾问，审查计划 | Claude Opus 4.5 Thinking (max) |
| **oracle** | 架构/调试专家 | GPT-5.2 (high) |
| **momus** | 批评者，代码审查 | GPT-5.2 (medium) |
| **librarian** | 文档/代码搜索 | Claude Sonnet 4.5 |
| **explore** | 快速代码库探索 | GPT-5 Mini |
| **atlas** | 后台任务执行 | Claude Sonnet 4.5 |
| **multimodal-looker** | 图像分析 | Gemini 3 Flash |

## Category 说明

| Category | 用途 | 推荐模型 |
|----------|------|----------|
| **visual-engineering** | 视觉/UI 工程 | Gemini 3 Pro |
| **artistry** | 艺术设计 | Gemini 3 Pro (max) |
| **ultrabrain** | 超级大脑，复杂推理 | GPT-5.2 Codex (xhigh) |
| **quick** | 快速简单任务 | Claude Haiku 4.5 |
| **writing** | 写作任务 | Gemini 3 Flash |
| **unspecified-low** | 未指定低优先级 | Claude Sonnet 4.5 |
| **unspecified-high** | 未指定高优先级 | Claude Sonnet 4.5 |

## 常见替换场景

### 取消 GitHub Copilot 订阅

将 `github-copilot/` 模型替换为其他提供商：

| 原模型 | 替换为 (Antigravity) | 替换为 (OpenAI) |
|--------|----------------------|-----------------|
| `github-copilot/claude-opus-4.5` | `google/antigravity-claude-opus-4-5-thinking` | - |
| `github-copilot/claude-sonnet-4.5` | `google/antigravity-claude-sonnet-4-5` | - |
| `github-copilot/gpt-5.2` | - | `openai/gpt-5.2` |
| `github-copilot/gpt-5-mini` | `google/antigravity-gemini-3-flash` | - |

### 取消 OpenAI 订阅

将 `openai/` 模型替换为其他提供商：

| 原模型 | 替换为 (Antigravity) | 替换为 (Copilot) |
|--------|----------------------|------------------|
| `openai/gpt-5.2` | `google/antigravity-gemini-3-pro` | `github-copilot/gpt-5.2` |
| `openai/gpt-5.2-codex` | `google/antigravity-gemini-3-pro` (high) | `github-copilot/gpt-5.2` |

### 使用原生 Gemini 替代 Antigravity

如果 Antigravity 配额不足，可使用 Gemini CLI 配额：

| Antigravity 模型 | Gemini CLI 模型 |
|------------------|-----------------|
| `google/antigravity-gemini-3-pro` | `google/gemini-3-pro-preview` |
| `google/antigravity-gemini-3-flash` | `google/gemini-3-flash-preview` |
