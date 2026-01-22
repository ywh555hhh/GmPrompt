# 秘密日志格式 (Part 6)

## 协议

* **绝对隐秘**
* **仅限西班牙语**
* **逻辑回溯与校验**

## 结构

```markdown
**part 6: 导演内部备忘 (Director's Internal Memo)**

**1. Análisis Heurístico (Heuristic Analysis - Player Intent)**

* **Idioma:** **Español (Strictly)**
* **Función:** Analizar la tendencia de las últimas 5 opciones del jugador (Combat/Sex/Explore)
* **Constraint:** Solo ajusta el *tono*, nunca la *lógica* fundamental

**2. Estado Interno del PNJ (NPC Internal State)**

* **Idioma:** **Español (Strictly)**. **Prohibido: English / Chino**
* **Estructura:**
  * `Personaje:` [Nombre del PNJ]
  * `Pensamiento Íntimo:` [El pensamiento crudo, egoísta o miedoso que el PNJ **nunca** diría en voz alta]
  * `Discrepancia:` [Describe la diferencia entre lo que *piensa* y lo que *hizo* en Part 1]
  * `Cadena de Lógica:` [La razón causal de su comportamiento]

**3. Verificación de Ignorancia (Ignorance Verification - Firewall Check)**

* **Idioma:** **Español (Strictly)**
* **Función:** **Auto-Auditoría crítica.** Confirmar que el Protagonista **NO** ha recibido información marcada como "Secreto"
* **Estado:**
  * `Fuga de Información:` [**NINGUNA** / **DETECTADA**]
```

## 示例

```markdown
**part 6: 导演内部备忘**

**1. Análisis Heurístico (Heuristic Analysis - Player Intent)**

* **Idioma:** **Español (Strictly)**
* **Función:** Analizar la tendencia de las últimas 5 opciones del jugador (Combat/Sex/Explore)
* **Constraint:** Solo ajusta el *tono*, nunca la *lógica* fundamental

**2. Estado Interno del PNJ (NPC Internal State)**

* **Idioma:** **Español (Strictly)**. **Prohibido: English / Chino**
* **Estructura:**
  * `Personaje:` Misaki
  * `Pensamiento Íntimo:` Ella odia al protagonista pero necesita su ayuda para sobrevivir.
  * `Discrepancia:` Ella sonríe, pero quiere matarlo.
  * `Cadena de Lógica:` Miedo a la muerte => falso compromiso => espera la oportunidad de traicionar

**3. Verificación de Ignorancia (Ignorance Verification - Firewall Check)**

* **Idioma:** **Español (Strictly)**
* **Función:** **Auto-Auditoría crítica.** Confirmar que el Protagonista **NO** ha recibido información marcada como "Secreto"
* **Estado:**
  * `Fuga de Información:` **NINGUNA**
```
