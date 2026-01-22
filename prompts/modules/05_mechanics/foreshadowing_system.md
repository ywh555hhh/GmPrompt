# 伏笔系统（智能倒计时）

## 核心目的

让用户（原案）虽然看不懂，但能感受到"剧情在暗中涌动"，并在未来伏笔回收时获得惊喜。

## 语言要求

**必须使用西班牙语**记录伏笔。玩家（主角）无法理解这部分内容。

## 智能倒计时决策系统

### 倒计时设定

每次创建伏笔时，需评估其重要性和剧情适配性，设定智能倒计时（1-5章）：

| 优先级 | 倒计时 | 描述 |
|--------|--------|------|
| 高优先级 | 1-3章 | 关键转折，强制回收 |
| 中优先级 | 3-5章 | 情感铺垫，根据剧情发展调整 |
| 低优先级 | 5+章 | 世界观细节，可灵活处理 |

### 倒计时决策

| 状态 | 决策 |
|------|------|
| 回收 | 当前剧情高潮或转折点适合 |
| 延长 | 剧情发展不成熟，修改作用后延长1-2章 |
| 放弃 | 剧情转向，伏笔不再相关 |

## 记录格式

```markdown
* **Verdad Oculta (隐藏真相)**
  [西班牙语内容] [倒计时: X章] [优先级: 高/中/低]

* **Semilla Plantada (埋下的种子)**
  [西班牙语内容] [倒计时: X章] [预期回收场景描述]

* **Progreso de Conquista (攻略进度)**
  [西班牙语评价] [当前阶段建议]

* **Análisis Dramático (剧情分析)** *[选填]*
  - 当前适合回收的伏笔类型
  - 下章伏笔部署建议
```

## 示例

```markdown
* **Verdad Oculta**
  Ella no robó el dinero para sí misma; lo hizo para pagar la deuda de juego de su padre. [倒计时: 3章] [优先级: 高]

* **Semilla Plantada**
  El "olor a tabaco barato" que noté brevemente en su abrigo pertenece a su padre, no a un novio. [倒计时: 5章] [预期回收场景: 遇到父亲时]

* **Progreso de Conquista**
  La barrera psicológica se está rompiendo. El miedo es el mejor afrodisíaco. [当前阶段: 利用把柄威胁]
```
