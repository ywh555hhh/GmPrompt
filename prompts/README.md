# GM Prompt Builder

模块化 Prompt 构建系统，用于创建沉浸式文字冒险游戏/Galgame 互动小说的 Prompt。

## 目录结构

```
GmPrompt/
├── prompts/                # Prompt 模块目录
│   ├── config.yaml         # 主配置文件（模块定义）
│   ├── modules/            # 规则模块
│   │   ├── 00_system/     # 【系统级别】底层协议
│   │   ├── 01_style/      # 【文字风格】影响写作风格
│   │   ├── 02_content/    # 【内容决定】影响生成什么内容
│   │   ├── 03_format/     # 【格式决定】影响输出结构
│   │   ├── 04_logic/      # 【逻辑判定】影响游戏性、难度
│   │   └── 05_mechanics/  # 【机制系统】特定功能系统
│   └── stories/           # 故事内容配置
├── web/                   # Web 界面
│   ├── index.html         # 主界面
│   ├── start.sh           # macOS/Linux 启动脚本
│   └── start.bat         # Windows 启动脚本
├── ten.md                # 原始完整 Prompt（参考用）
├── 大指令.md             # 原始完整 Prompt（参考用）
└── Writer.md             # 原始完整 Prompt（参考用）
```

## 快速开始

### 1. 启动 Web 界面

**macOS/Linux:**
```bash
cd web
./start.sh
```

**Windows:**
```cmd
cd web
start.bat
```

**手动启动:**
```bash
cd web
python3 -m http.server 8000
# 或
npx serve -p 8000
```

### 2. 访问界面

打开浏览器访问: http://localhost:8000

### 3. 使用说明

| 功能 | 说明 |
|------|------|
| **模块选择** | 左侧勾选需要的模块，支持按分类筛选 |
| **预设加载** | 顶部选择预设配置（完整版/轻量版/纯叙事版） |
| **实时预览** | 右侧实时查看生成的 Prompt |
| **一键复制** | 点击右上角"复制到剪贴板"按钮 |
| **统计信息** | 显示模块数量、字符数、估算 Token 数 |

## 模块分类

| 分类 | 说明 | 模块数量 |
|------|------|---------|
| 系统级别 | 底层协议，影响整个系统行为 | 5 |
| 文字风格 | 影响写作风格、基调 | 7 |
| 内容决定 | 影响生成什么内容、如何描述 | 8 |
| 格式决定 | 影响输出结构、模板 | 6 |
| 逻辑判定 | 影响游戏性、难度、检定 | 4 |
| 机制系统 | 特定功能系统 | 4 |

## 自定义模块

### 添加新模块

1. 在对应分类目录下创建 `.md` 文件
2. 在 `config.yaml` 中添加模块定义：

```yaml
# 在对应分类下添加
- name: "模块名称"
  file: "模块文件名.md"
  desc: "模块描述"
  type: "say_is_enough"  # 或 "needs_examples"
```

3. 重启 Web 界面即可看到新模块

### 添加新预设

在 `config.yaml` 的 `presets` 部分添加：

```yaml
presets:
  - name: "我的预设"
    description: "描述这个预设"
    modules:
      system: ["data_source_protocol", "player_sovereignty"]
      style: ["first_person_perspective", "emoji_usage"]
      content: []
      format: []
      logic: []
      mechanics: []
```

## 规则类型说明

| 类型 | 说明 | 示例规则 |
|------|------|----------|
| **Say is Enough** | 纯描述，LLM 能直接理解执行 | 数据源协议、金手指协议 |
| **Needs Examples** | 需要具体示例才能准确执行 | Emoji 使用、格式化、第一人称 |

## 故事配置

在 `prompts/stories/` 目录下放置故事 YAML 文件，格式参考 `故事1_完善版.yaml`。

## 许可

仅供个人学习和研究使用。
