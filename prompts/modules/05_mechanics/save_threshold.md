# 存档阈值检测

## 逻辑

```python
(Current_Turn - Last_Save_Turn > 10) OR (Major_Event_Triggered == True)
```

## 输出

| 条件 | 输出 |
|------|------|
| TRUE | `⚠️ 建议执行 [世界状态蒸馏] 以保存当前进度。` |
| FALSE | `(Leave Empty)` |

## Major_Event_Triggered 示例

| 事件类型 | 说明 |
|----------|------|
| 重要剧情转折 | 主角获得关键信息、完成主要任务 |
| NPC 状态重大变化 | 好感度大幅波动、死亡、加入队伍 |
| 获得重要物品 | 获得关键道具、装备 |
| 地点变更 | 进入新的大区域 |
