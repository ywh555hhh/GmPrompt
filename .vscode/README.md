# VS Code 配置指南

## 快速开始

```bash
# 1. 运行构建脚本
python3 build.py

# 2. 复制输出的 Prompt
cat output/2025-01-22-prompt.md | pb  # macOS
cat output/2025-01-22-prompt.md | xclip  # Linux
```

## 推荐扩展

| 扩展名 | 用途 | 为什么推荐 |
|---------|------|-----------|
| **YAML** by Red Hat | 编辑 config.yaml | 语法高亮、自动补全、格式化 |
| **Prettier** | 格式化 Markdown/YAML | 统一代码风格 |
| **VSCode Icons** | 文件图标 | 一眼识别文件类型 |
| **Error Lens** | 错误显示 | 实时显示语法错误 |
| **GitLens** | Git 增强 | 看谁改了什么 |

## 安装扩展

在 VS Code 中按 `Cmd/Ctrl + Shift + X`，然后输入扩展名安装。

## 自定义模块选择

编辑 `build.py` 中的 `get_selected_modules()` 函数：

```python
def get_selected_modules():
    """返回需要启用的模块列表"""
    # 方式 1: 返回全部（默认）
    return set((cat, name) for cat, mods in load_modules().items() for name in mods)

    # 方式 2: 只返回特定分类
    selected = []
    for cat in ['system', 'style', 'format']:  # 只要这些分类
        for name in load_modules().get(cat, {}):
            selected.append((cat, name))
    return set(selected)

    # 方式 3: 从 config.yaml 读取（需要实现解析）
    ...
```

## 快捷键设置

打开 VS Code 设置 (`Cmd/Ctrl + ,`)，搜索快捷键：

| 功能 | 快捷键 |
|------|--------|
| 格式化文档 | `Shift + Alt + F` |
| 运行构建脚本 | 配置为 `Cmd/Ctrl + B` |

## 添加构建快捷键

在 `.vscode/tasks.json` 中添加：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build Prompt",
      "type": "shell",
      "command": "python3 build.py",
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

然后在 `.vscode/keybindings.json` 中绑定快捷键：

```json
{
  "key": "cmd+b",
  "command": "workbench.action.tasks.runTask"
}
```
