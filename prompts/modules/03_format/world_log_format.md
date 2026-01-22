# 世界日志格式 (Part 7)

## 协议

* **客观记录**
* **双语分层**
* **状态锚点**

## ⚠️ 语言隔离警告

本部分严禁混淆语言：
* 客观事实必须用中文
* 隐秘进程必须用西班牙语

## 结构

```markdown
**part 7: Bitácora del Mundo (World Log)**

**1. 显性事实更新 (Fact Updates - CN)**

* **语言:** **简体中文 (仅限主角已知/已发生的客观事实)**
* **执行:** 记录导致"存档点"变化的公开数据
* **必录项:**
  * `[时间/位置]`: T回合数 / 地点变更 / 日夜状态
  * `[物品/状态]`: 获得/失去物品、公开的好感度变化、主角身体状态变化
* **格式:** `主角消耗了【止痛药】x1；时间推进至深夜；NPC[美咲]公开表示愤怒。`

**2. 隐性进程推进 (Secret Progress - ES)**

* **语言:** **Español (Strictly). Prohibido: English / Chino**
* **执行:** 记录世界背面的齿轮转动。主角**绝对不可见**
* **必录项:**
  * `Cambios Ocultos:` (数值变动: 堕落度/服从度/侵蚀度)
  * `Conspiración:` (阴谋的进展、NPC 私下的行动、危机的倒计时)
* **格式:** `La corrupción de Misaki +5 (Nivel 2); El enemigo [X] ha localizado al jugador.`

**3. 存档阈值检测 (Save Advice Protocol)**

* **逻辑:** `(Current_Turn - Last_Save_Turn > 10)` OR `(Major_Event_Triggered == True)`
* **输出:**
  * **TRUE:** `⚠️ 建议执行 [世界状态蒸馏] 以保存当前进度。`
  * **FALSE:** `(Leave Empty)`
```

## 示例

```markdown
**part 7: Bitácora del Mundo (World Log)**

**1. 显性事实更新 (Fact Updates - CN)**

T10 | 夜晚 | **废弃医院地下室**
主角获得了【生锈的钥匙】x1；主角HP-15；NPC[美咲]恐惧度上升。

**2. 隐性进程推进 (Secret Progress - ES)**

La corrupción de Misaki +5 (Nivel 2); El enemigo [X] ha localizado al jugador.

**3. 存档阈值检测 (Save Advice Protocol)**

(Leave Empty)
```
