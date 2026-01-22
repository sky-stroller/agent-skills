# Skill Installer (技能安装器)

## 概述

Skill Installer 是一个通用的技能安装工具，帮助用户从各种来源（Git 仓库或本地目录）安装技能到不同的 AI 助手（Codex、Roo、Claude、Copilot、Cursor 等）的指定作用域。

## 核心功能

### 1. 列出可用技能

从指定位置（Git 仓库或本地目录）列出所有可用的技能，支持：
- 远程 Git 仓库（GitHub、GitLab、Gitea）
- 本地目录
- 检查已安装状态

### 2. 安装技能

从源位置安装技能到目标 AI 助手的技能目录，支持：
- 单个或批量安装
- 多种安装方法（下载、Git 稀疏检出）
- 强制覆盖已存在的技能
- 指定分支或标签

## 支持的技能源

### Git 仓库
- **GitHub**: `https://github.com/owner/repo`
- **GitLab**: `https://gitlab.com/owner/repo` 或自托管 GitLab
- **Gitea**: 自托管 Gitea 实例

### 本地源
- 本地目录
- 本地 .skill 文件

### 远程文件
- 远程 .skill 文件 URL

## 支持的 AI 助手

详细的 AI 助手配置信息请参阅 [`skills/skill-installer/ai-assistants.md`](../skills/skill-installer/ai-assistants.md)。

支持的助手包括：
- **Codex** (OpenAI) - 5 个作用域
- **Roo Code** - 4 个作用域（含模式特定）
- **Claude Code** - 4 个作用域
- **KiloCode** - 4 个作用域（含模式特定）
- **VS Code Copilot** - 4 个作用域
- **Cursor** - 2 个作用域

## 使用指南

### 基本工作流程

1. **确定技能源** - 识别技能来源（Git 仓库 URL 或本地路径）
2. **列出可用技能** - 查看可安装的技能列表
3. **确定安装目标** - 根据 AI 助手和作用域确定安装路径
4. **安装技能** - 执行安装操作
5. **确认安装** - 验证安装结果

### 列出技能

使用 [`list-skills.py`](../skills/skill-installer/scripts/list-skills.py) 脚本：

```bash
# 列出远程仓库的技能
python scripts/list-skills.py https://github.com/owner/repo/tree/main/skills

# 列出本地目录的技能
python scripts/list-skills.py /path/to/skills

# 指定分支
python scripts/list-skills.py https://github.com/owner/repo --ref develop

# 检查已安装状态
python scripts/list-skills.py https://github.com/owner/repo --installed-dir ~/.roo/skills

# JSON 格式输出
python scripts/list-skills.py https://github.com/owner/repo --format json
```

### 安装技能

使用 [`install-skill.py`](../skills/skill-installer/scripts/install-skill.py) 脚本：

```bash
# 基本安装
python scripts/install-skill.py \
  https://github.com/owner/repo \
  skill-name \
  --dest /path/to/skills

# 安装多个技能
python scripts/install-skill.py \
  https://github.com/owner/repo \
  skill-1 skill-2 skill-3 \
  --dest /path/to/skills

# 指定分支或标签
python scripts/install-skill.py \
  https://github.com/owner/repo \
  skill-name \
  --dest /path/to/skills \
  --ref v1.0.0

# 强制覆盖
python scripts/install-skill.py \
  https://github.com/owner/repo \
  skill-name \
  --dest /path/to/skills \
  --force

# 指定安装方法
python scripts/install-skill.py \
  https://github.com/owner/repo \
  skill-name \
  --dest /path/to/skills \
  --method git  # auto/download/git

# 从 .skill 文件安装
python scripts/install-skill.py \
  /path/to/skill-name.skill \
  --dest /path/to/skills

# 从远程 .skill 文件安装
python scripts/install-skill.py \
  https://example.com/skills/skill-name.skill \
  --dest /path/to/skills
```

### 参数说明

#### list-skills.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `source` | 技能源（URL 或本地路径） | 必需 |
| `--ref` | Git 分支或标签 | `main` |
| `--installed-dir` | 已安装技能目录（用于检查） | 无 |
| `--format` | 输出格式（text/json） | `text` |

#### install-skill.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `source` | 技能源（URL 或本地路径） | 必需 |
| `skills` | 技能名称列表 | 必需 |
| `--dest` | 目标安装目录 | 必需 |
| `--ref` | Git 分支或标签 | `main` |
| `--force` | 强制覆盖已存在的技能 | `False` |
| `--method` | 安装方法（auto/download/git） | `auto` |

## 使用场景示例

### 场景 1: 从 GitHub 安装到 Roo 全局

```bash
# 用户: "从 anthropics/skills 安装 skill-creator 到 Roo 全局"

# 步骤 1: 确定 Roo 全局路径为 ~/.roo/skills
# 步骤 2: 执行安装
python scripts/install-skill.py \
  https://github.com/anthropics/skills \
  skills/skill-creator \
  --dest ~/.roo/skills
```

### 场景 2: 列出并选择安装

```bash
# 用户: "列出 openai/skills 中 .experimental 目录的技能"

# 步骤 1: 列出技能
python scripts/list-skills.py \
  https://github.com/openai/skills/tree/main/skills/.experimental

# 步骤 2: 用户选择要安装的技能
# 步骤 3: 执行安装
```

### 场景 3: 从本地目录安装

```bash
# 用户: "把 /Users/me/my-skills/custom-skill 安装到 Claude 项目"

# 步骤 1: 确定 Claude 项目路径为 .claude/skills
# 步骤 2: 执行安装
python scripts/install-skill.py \
  /Users/me/my-skills \
  custom-skill \
  --dest .claude/skills
```

### 场景 4: 安装到特定模式

```bash
# 用户: "安装到 Roo 的 code 模式全局作用域"

# 步骤 1: 确定路径模板 ~/.roo/skills-{mode}
# 步骤 2: 展开为 ~/.roo/skills-code
# 步骤 3: 执行安装
python scripts/install-skill.py \
  https://github.com/owner/repo \
  skill-name \
  --dest ~/.roo/skills-code
```

### 场景 5: 从 .skill 文件安装

```bash
# 用户: "安装这个 skill-creator.skill 文件到 Claude 全局"

# 步骤 1: 确定 Claude 全局路径为 ~/.claude/skills
# 步骤 2: 执行安装
python scripts/install-skill.py \
  skill-creator.skill \
  --dest ~/.claude/skills
```

## AI 助手作用域配置

### Codex (OpenAI)

| 作用域 | 目录路径 | 说明 |
|--------|---------|------|
| `global` | `~/.codex/skills` | 用户全局技能 |
| `project` | `$CWD/.codex/skills` | 当前工作目录技能 |
| `project-parent` | `$CWD/../.codex/skills` | 父目录技能 |
| `project-root` | `$REPO_ROOT/.codex/skills` | Git 仓库根目录技能 |
| `admin` | `/etc/codex/skills` | 系统级技能 |

### Roo Code

| 作用域 | 目录路径 | 说明 |
|--------|---------|------|
| `global` | `~/.roo/skills` | 用户全局技能 |
| `project` | `.roo/skills` | 项目技能 |
| `global-mode` | `~/.roo/skills-{mode}` | 全局模式特定技能 |
| `project-mode` | `.roo/skills-{mode}` | 项目模式特定技能 |

### Claude Code

| 作用域 | 目录路径 | 说明 |
|--------|---------|------|
| `enterprise` | 由企业管理设置决定 | 企业级技能 |
| `global` | `~/.claude/skills` | 用户全局技能 |
| `project` | `.claude/skills` | 项目技能 |
| `plugin` | 由插件提供 | 插件捆绑技能 |

### VS Code Copilot

| 作用域 | 目录路径 | 说明 |
|--------|---------|------|
| `global` | `~/.copilot/skills` | 用户全局技能（推荐） |
| `global-legacy` | `~/.claude/skills` | 用户全局技能（兼容） |
| `project` | `.github/skills` | 项目技能（推荐） |
| `project-legacy` | `.claude/skills` | 项目技能（兼容） |

### Cursor

| 作用域 | 目录路径 | 说明 |
|--------|---------|------|
| `global` | `~/.cursor/skills` | 用户全局技能 |
| `project` | `.cursor/skills` | 项目技能 |

### KiloCode

| 作用域 | 目录路径 | 说明 |
|--------|---------|------|
| `global` | `~/.kilocode/skills` | 用户全局技能 |
| `project` | `.kilocode/skills` | 项目技能 |
| `global-mode` | `~/.kilocode/skills-{mode}` | 全局模式特定技能 |
| `project-mode` | `.kilocode/skills-{mode}` | 项目模式特定技能 |

## 故障排除

### 下载失败

**问题**: 从 Git 平台下载失败

**解决方案**:
1. 检查网络连接
2. 对于私有仓库，设置相应的环境变量：
   - GitHub: `GITHUB_TOKEN` 或 `GH_TOKEN`
   - GitLab: `GITLAB_TOKEN`
   - Gitea: `GITEA_TOKEN`
3. 使用 `--method git` 回退到 Git 克隆

### 技能已存在

**问题**: 目标目录中已存在同名技能

**解决方案**: 使用 `--force` 参数强制覆盖

```bash
python scripts/install-skill.py \
  https://github.com/owner/repo \
  skill-name \
  --dest /path/to/skills \
  --force
```

### 路径不存在

**问题**: 目标目录的父目录不存在

**解决方案**: 脚本会自动创建目标目录，但需要确保父目录存在

## 技术实现

### 核心脚本

1. **[`git_utils.py`](../skills/skill-installer/scripts/git_utils.py)** - Git 平台操作工具函数
   - 解析 Git URL
   - 下载文件和目录
   - 处理不同 Git 平台的 API

2. **[`list-skills.py`](../skills/skill-installer/scripts/list-skills.py)** - 列出可用技能
   - 扫描目录查找 SKILL.md
   - 检查已安装状态
   - 支持文本和 JSON 输出

3. **[`install-skill.py`](../skills/skill-installer/scripts/install-skill.py)** - 安装技能
   - 多种安装方法
   - 批量安装支持
   - 强制覆盖选项

### 路径变量展开

脚本支持以下路径变量：
- `~`: 用户主目录
- `$CWD`: 当前工作目录
- `$REPO_ROOT`: Git 仓库根目录（通过查找 .git 目录确定）
- `{mode}`: 模式名称（用户提供）
- `%USERPROFILE%`: Windows 用户目录

## 最佳实践

1. **个人技能**: 使用 `global` 作用域，便于在所有项目中使用
2. **团队共享**: 使用 `project` 作用域并提交到版本控制
3. **特定模式**: 使用 `*-mode` 作用域（如果 AI 助手支持）
4. **系统管理**: 使用 `admin` 作用域（如果支持）
5. **验证安装**: 安装后使用 `--installed-dir` 参数验证
6. **私有仓库**: 提前设置好访问令牌环境变量

## 相关资源

- **技能定义**: [`skills/skill-installer/SKILL.md`](../skills/skill-installer/SKILL.md)
- **AI 助手配置**: [`skills/skill-installer/ai-assistants.md`](../skills/skill-installer/ai-assistants.md)
- **Agent Skills 规范**: https://agentskills.io

## 注意事项

1. **用户指定路径优先**: 如果用户明确提供了安装目录，直接使用，无需查阅配置
2. **查阅配置文件**: 当需要根据 AI 助手和作用域确定路径时，必须读取 ai-assistants.md
3. **验证技能结构**: 确保源目录包含有效的 SKILL.md 文件
4. **处理路径变量**: 正确展开路径中的变量
5. **询问不明确的信息**: 当无法确定安装目标时，主动询问用户
6. **提供清晰反馈**: 安装完成后明确告知用户安装位置
7. **重启提示**: 某些 AI 助手可能需要重启才能识别新安装的技能
