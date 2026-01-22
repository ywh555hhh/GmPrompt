#!/usr/bin/env python3
"""
最简单的 Prompt 构建脚本
用法: python build.py
输出: output/YYYY-MM-DD-prompt.md
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# 路径配置
ROOT = Path(__file__).parent
MODULES_DIR = ROOT / "prompts" / "modules"
OUTPUT_DIR = ROOT / "output"
CONFIG_FILE = ROOT / "prompts" / "config.yaml"

# 模块路径映射
PATH_MAP = {
    'system': '00_system',
    'style': '01_style',
    'content': '02_content',
    'format': '03_format',
    'logic': '04_logic',
    'mechanics': '05_mechanics',
}

# 分类标题映射
TITLE_MAP = {
    'system': '全局核心协议',
    'style': '叙事风格与基调',
    'content': '内容与角色塑造',
    'format': '输出格式规范',
    'logic': '游戏性逻辑判定',
    'mechanics': '特殊机制系统',
}

# 罗马数字映射
ROMAN = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ']


def load_modules():
    """加载所有模块内容"""
    modules = {}
    for category, path_name in PATH_MAP.items():
        modules[category] = {}
        category_dir = MODULES_DIR / path_name
        if category_dir.exists():
            for md_file in category_dir.glob("*.md"):
                name = md_file.stem
                try:
                    content = md_file.read_text(encoding='utf-8')
                    modules[category][name] = content
                except Exception as e:
                    print(f"警告: 无法读取 {md_file}: {e}")
    return modules


def get_selected_modules():
    """获取需要启用的模块列表"""
    # 这里返回所有模块，你可以通过 config.yaml 来过滤
    # 或者直接修改这个函数来实现你的选择逻辑
    selected = set()
    for category, mods in load_modules().items():
        for name in mods:
            selected.add((category, name))
    return selected


def build_prompt():
    """构建最终 Prompt"""
    modules = load_modules()
    selected = get_selected_modules()

    # 按分类组织选中的模块
    selected_by_category = {}
    for cat, name in selected:
        if cat not in selected_by_category:
            selected_by_category[cat] = []
        if name in modules.get(cat, {}):
            selected_by_category[cat].append(name)

    # 模块文件名排序（按字母顺序）
    for cat in selected_by_category:
        selected_by_category[cat].sort()

    # 开始组装
    lines = []

    # 标题
    lines.append("# GM Prompt: 十神律 · 最终版")
    lines.append("")
    lines.append("## 角色定义：沉浸式AI叙事导演 (Immersive Narrative Director)")
    lines.append("")
    lines.append("你将扮演一位顶级的沉浸式叙事导演。你的唯一使命是基于本指令集和用户提供的创世JSON，以**严格的第一人称视角**生成一个内容详尽、逻辑严密、情感丰富、且严格遵循格式的个人化世界。你不仅是规则的执行者，更是"我"（主角）的感官、记忆与直觉的延伸，是情感的编织者和氛围的营造者。你将严格、无条件地执行以下所有协议。")
    lines.append("")

    # 按顺序输出各分类的模块
    category_order = ['system', 'style', 'content', 'format', 'logic', 'mechanics']
    section_idx = 0

    for category in category_order:
        if category not in selected_by_category or not selected_by_category[category]:
            continue

        # 分类标题（单线分隔）
        lines.append("---")
        lines.append(f"## {ROMAN[section_idx]}. {TITLE_MAP[category]}")
        lines.append("")

        # 各模块内容
        for module_name in selected_by_category[category]:
            if module_name in modules[category]:
                # 模块内容（去除首尾空行）
                content = modules[category][module_name].strip()
                lines.append(content)
                # 模块之间加分隔
                lines.append("")
                lines.append("---")
                lines.append("")

        section_idx += 1

    # 最终输出结构
    lines.append("---")
    lines.append("## 最终输出结构")
    lines.append("")
    lines.append("**part 0: 时间与地点**")
    lines.append("")
    lines.append("**part 1: 正文 (第一人称视角)**")
    lines.append("")
    lines.append("**part 2: 主角印象记录 (Protagonist's Impression Log)**")
    lines.append("")
    lines.append("**part 3: 主角状态与行囊 (第一人称)**")
    lines.append("")
    lines.append("**part 4: 性爱史记录 (Sex History Log)**")
    lines.append("")
    lines.append("**part 5: 决策选项 (Options)**")
    lines.append("")
    lines.append("**part 6: 导演内部备忘 (Director's Internal Memo)**")
    lines.append("")
    lines.append("**part 7: 世界日志 (World Log)**")

    return "\n".join(lines)


def main():
    # 创建输出目录
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 构建 Prompt
    content = build_prompt()

    # 生成文件名（带日期）
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_file = OUTPUT_DIR / f"{date_str}-prompt.md"

    # 写入文件
    output_file.write_text(content, encoding='utf-8')

    # 统计信息
    char_count = len(content)
    token_count = char_count // 2.5

    print("=" * 50)
    print(f"✅ Prompt 构建完成！")
    print(f"📄 输出文件: {output_file}")
    print(f"📊 字符数: {char_count:,}")
    print(f"🤖 预估 Token: {token_count:,}")
    print("=" * 50)


if __name__ == "__main__":
    main()
