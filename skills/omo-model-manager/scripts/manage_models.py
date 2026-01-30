#!/usr/bin/env python3
"""
oh-my-opencode 模型管理器

功能:
- 列出当前配置的所有 agent 和 category 的模型
- 修改特定 agent/category 的模型
- 按提供商批量替换模型
- 显示可用模型列表（从 opencode models 命令获取）

配置文件路径: ~/.config/opencode/oh-my-opencode.json
"""

import json
import sys
import subprocess
from pathlib import Path
from typing import Optional
from collections import defaultdict

# 配置文件路径
CONFIG_PATH = Path.home() / ".config" / "opencode" / "oh-my-opencode.json"


def load_config() -> dict:
    """加载 oh-my-opencode 配置"""
    if not CONFIG_PATH.exists():
        print(f"❌ 配置文件不存在: {CONFIG_PATH}")
        sys.exit(1)
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_config(config: dict) -> None:
    """保存配置到文件"""
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"✅ 配置已保存到: {CONFIG_PATH}")


def get_available_models() -> dict:
    """
    从 opencode models 命令获取所有可用模型
    返回按提供商分组的模型字典
    """
    try:
        result = subprocess.run(
            ["opencode", "models"],
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout + result.stderr

        models_by_provider = defaultdict(list)
        for line in output.strip().split('\n'):
            line = line.strip()
            # 跳过非模型行（如 hook 消息）
            if '/' in line and not line.startswith('[') and not line.startswith('opencode'):
                # 特殊处理 opencode/ 前缀的模型
                if line.startswith('opencode/'):
                    provider = 'opencode'
                    model = line
                else:
                    parts = line.split('/', 1)
                    if len(parts) == 2:
                        provider = parts[0]
                        model = line
                        models_by_provider[provider].append(model)
            elif line.startswith('opencode/'):
                models_by_provider['opencode'].append(line)

        return dict(models_by_provider)
    except subprocess.TimeoutExpired:
        print("⚠️  获取模型列表超时")
        return {}
    except FileNotFoundError:
        print("⚠️  未找到 opencode 命令")
        return {}
    except Exception as e:
        print(f"⚠️  获取模型列表失败: {e}")
        return {}


def list_current_config() -> None:
    """列出当前所有 agent 和 category 的模型配置"""
    config = load_config()

    print("=" * 60)
    print("📋 当前 oh-my-opencode 模型配置")
    print("=" * 60)

    # Agents
    print("\n🤖 Agents:")
    print("-" * 40)
    agents = config.get("agents", {})
    for name, cfg in agents.items():
        model = cfg.get("model", "未配置")
        variant = cfg.get("variant", "")
        variant_str = f" ({variant})" if variant else ""
        print(f"  {name:20} → {model}{variant_str}")

    # Categories
    print("\n📁 Categories:")
    print("-" * 40)
    categories = config.get("categories", {})
    for name, cfg in categories.items():
        model = cfg.get("model", "未配置")
        variant = cfg.get("variant", "")
        variant_str = f" ({variant})" if variant else ""
        print(f"  {name:20} → {model}{variant_str}")

    print()


def list_available_models() -> None:
    """列出所有可用的模型（从 opencode models 命令获取）"""
    print("=" * 60)
    print("📦 可用模型列表 (来自 opencode models)")
    print("=" * 60)

    models_by_provider = get_available_models()

    if not models_by_provider:
        print("\n⚠️  无法获取模型列表，请手动运行: opencode models")
        return

    # 提供商显示名称映射
    provider_names = {
        'anthropic': 'Anthropic (Claude)',
        'google': 'Google (Gemini / Antigravity)',
        'openai': 'OpenAI',
        'github-copilot': 'GitHub Copilot',
        'opencode': 'OpenCode'
    }

    for provider in sorted(models_by_provider.keys()):
        display_name = provider_names.get(provider, provider)
        models = models_by_provider[provider]
        print(f"\n🏷️  {display_name} ({len(models)} 个模型):")
        print("-" * 40)
        for model in sorted(models):
            print(f"  {model}")

    print()


def list_providers() -> None:
    """列出当前配置中使用的提供商统计"""
    config = load_config()

    provider_usage = defaultdict(list)

    for section in ["agents", "categories"]:
        for name, cfg in config.get(section, {}).items():
            model = cfg.get("model", "")
            if '/' in model:
                provider = model.split('/')[0]
                provider_usage[provider].append(f"[{section}] {name}")

    print("=" * 60)
    print("📊 提供商使用统计")
    print("=" * 60)

    for provider in sorted(provider_usage.keys()):
        items = provider_usage[provider]
        print(f"\n🏷️  {provider}/ ({len(items)} 个配置):")
        print("-" * 40)
        for item in items:
            print(f"  {item}")

    print()


def set_model(target_type: str, target_name: str, model: str, variant: Optional[str] = None) -> None:
    """
    设置特定 agent 或 category 的模型

    Args:
        target_type: 'agent' 或 'category'
        target_name: agent/category 名称
        model: 模型名称 (如 google/antigravity-claude-opus-4-5-thinking)
        variant: 可选的 variant (如 max, low, high)
    """
    config = load_config()

    key = "agents" if target_type == "agent" else "categories"

    if target_name not in config.get(key, {}):
        print(f"❌ 未找到 {target_type}: {target_name}")
        print(f"   可用的 {target_type}s: {', '.join(config.get(key, {}).keys())}")
        return

    old_model = config[key][target_name].get("model", "未配置")
    old_variant = config[key][target_name].get("variant", "")

    config[key][target_name]["model"] = model
    if variant:
        config[key][target_name]["variant"] = variant
    elif "variant" in config[key][target_name] and not variant:
        # 如果新模型没有指定 variant，保留原有的
        pass

    save_config(config)

    new_variant = config[key][target_name].get("variant", "")
    print(f"✅ 已更新 {target_type} '{target_name}':")
    print(f"   旧模型: {old_model}" + (f" ({old_variant})" if old_variant else ""))
    print(f"   新模型: {model}" + (f" ({new_variant})" if new_variant else ""))


def find_by_provider(provider: str) -> None:
    """
    查找使用指定提供商的所有配置

    Args:
        provider: 提供商前缀 (如 'github-copilot', 'google', 'openai')
    """
    config = load_config()
    affected = []

    for section in ["agents", "categories"]:
        for name, cfg in config.get(section, {}).items():
            model = cfg.get("model", "")
            variant = cfg.get("variant", "")
            if model.startswith(f"{provider}/"):
                variant_str = f" ({variant})" if variant else ""
                affected.append((section, name, model + variant_str))

    if affected:
        print(f"📋 使用 '{provider}/' 提供商的配置 ({len(affected)} 项):")
        print("-" * 50)
        for section, name, model in affected:
            print(f"  [{section:10}] {name:20} → {model}")
    else:
        print(f"ℹ️  未找到使用 '{provider}/' 提供商的配置")


def replace_provider(old_provider: str, new_provider: str, dry_run: bool = False) -> None:
    """
    批量替换提供商前缀

    Args:
        old_provider: 旧提供商前缀
        new_provider: 新提供商前缀
        dry_run: 如果为 True，只显示将要进行的更改，不实际执行
    """
    config = load_config()
    changes = []

    for section in ["agents", "categories"]:
        for name, cfg in config.get(section, {}).items():
            model = cfg.get("model", "")
            if model.startswith(f"{old_provider}/"):
                old_suffix = model.split("/", 1)[1]
                new_model = f"{new_provider}/{old_suffix}"
                changes.append((section, name, model, new_model))
                if not dry_run:
                    cfg["model"] = new_model

    if changes:
        action = "将要" if dry_run else "已"
        print(f"{'🔍 预览' if dry_run else '✅ 批量替换完成'}，共 {len(changes)} 项{action}更改:")
        print("-" * 60)
        for section, name, old_model, new_model in changes:
            print(f"  [{section:10}] {name:20}")
            print(f"    {old_model} → {new_model}")

        if not dry_run:
            save_config(config)
        else:
            print("\n💡 使用 --apply 参数执行实际替换")
    else:
        print(f"ℹ️  未找到使用 '{old_provider}/' 前缀的模型")


def print_usage():
    """打印使用说明"""
    print("""
oh-my-opencode 模型管理器

用法:
  python manage_models.py <命令> [参数...]

命令:
  list                    列出当前所有 agent 和 category 的模型配置
  models                  列出所有可用的模型（从 opencode models 获取）
  providers               列出当前配置中使用的提供商统计

  set <类型> <名称> <模型> [variant]
                          设置特定 agent/category 的模型
                          类型: agent 或 category

  find <提供商>            查找使用指定提供商的所有配置

  replace <旧提供商> <新提供商> [--apply]
                          批量替换提供商前缀
                          默认为预览模式，添加 --apply 执行实际替换

示例:
  # 查看当前配置
  python manage_models.py list
  python manage_models.py models
  python manage_models.py providers

  # 修改单个 agent/category
  python manage_models.py set agent sisyphus google/antigravity-claude-opus-4-5-thinking max
  python manage_models.py set category writing google/antigravity-gemini-3-flash

  # 查找和替换提供商
  python manage_models.py find github-copilot
  python manage_models.py replace github-copilot google          # 预览
  python manage_models.py replace github-copilot google --apply  # 执行
""")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "list":
        list_current_config()

    elif command == "models":
        list_available_models()

    elif command == "providers":
        list_providers()

    elif command == "set":
        if len(sys.argv) < 5:
            print("用法: python manage_models.py set <类型> <名称> <模型> [variant]")
            print("  类型: agent 或 category")
            sys.exit(1)
        target_type = sys.argv[2]
        target_name = sys.argv[3]
        model = sys.argv[4]
        variant = sys.argv[5] if len(sys.argv) > 5 else None
        set_model(target_type, target_name, model, variant)

    elif command == "find":
        if len(sys.argv) < 3:
            print("用法: python manage_models.py find <提供商>")
            sys.exit(1)
        find_by_provider(sys.argv[2])

    elif command == "replace":
        if len(sys.argv) < 4:
            print("用法: python manage_models.py replace <旧提供商> <新提供商> [--apply]")
            sys.exit(1)
        old_provider = sys.argv[2]
        new_provider = sys.argv[3]
        dry_run = "--apply" not in sys.argv
        replace_provider(old_provider, new_provider, dry_run)

    else:
        print(f"❌ 未知命令: {command}")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
