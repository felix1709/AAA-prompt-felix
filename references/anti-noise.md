# 噪点防治（Anti-Noise）

> 用途：GPT Image 家族（gpt-image-1 / 2 / 2.5）出图经常自带**颗粒噪点／脏纹理**。
> 本文给出「提示词层」的通用防护块，以及会诱发噪点的词表。
> **本项目默认：每一条生图提示词末尾都挂载 §2 的防护块。**
> 来源：OpenAI Developer Community 关于 gpt-image-1 反复编辑导致颗粒的讨论、AI_Cinematic_Prompt 适配器、以及多份中文实测流程文（见文末）。

---

## 一、先分清：噪点是模型造成的，还是提示词造成的

| 类型 | 症状 | 主因 |
|---|---|---|
| **提示词诱发的颗粒** | 全图均匀细沙、暗部发灰发脏 | 提示词里写了 grain / film / 8K / hyper-detailed / 欠曝 / 暗部厚重 |
| **编辑链累积的颗粒** | 越改越脏，第一版还干净 | 同一张图连续多轮高保真编辑，颗粒逐轮叠加 |
| **压缩引入的颗粒** | 下载后比生成时更脏 | 存成 JPEG/WebP，反复压缩 |
| **结构性纹理** | 鱼鳞／蜂窝／水波状的重复花纹 | 密度词写得过满（countless / hundreds of / intricate microtexture） |
| **暗底噪点** | 只在深色背景上明显 | 背景接近纯黑，暗部噪点最容易显形 |

**处理顺序**：先删诱发词 → 再挂防护块 → 再改流程（PNG、不连改）→ 最后才考虑后期降噪。
**不要**一上来就堆"no noise"，删词比加词有效。

---

## 二、通用防护块（每次生图都挂）

> 直接复制到提示词末尾。中文模型用中文版，英文模型用英文版。
> ⚠️ **`look-library.md` LOOK 卡 2（胶片暗房阳光风）不挂本防护块**——它要求「可见 35mm 胶片颗粒」，与本块的「没有胶片颗粒」直接冲突。该风格按卡 2 的写法，只去掉数码噪点与脏纹理部分。

### 中文版

```
画面干净通透，成像是数码渲染的干净质感：没有胶片颗粒、没有 ISO 噪点、没有灰尘与斑点纹理、没有高频杂纹、没有过度锐化。暗部深邃但干净，细节沉入黑色而不是糊成脏噪点，不要压成死黑。明暗过渡平滑，不出现色带。细节密度克制，重点处清晰锐利，其余保持柔和平滑，不要为了"干净"把该有的结构抹糊。
```

### 英文版

```
Clean, transparent digital imaging: no film grain, no ISO noise, no dust or speckle texture, no high-frequency microtexture, no oversharpening. Shadows are deep yet clean — detail sinks into black without turning muddy, never crushed to flat black. Smooth tonal gradients with no banding. Restrained detail density: crisp where it matters, soft and smooth elsewhere; do not smear structure for the sake of cleanliness.
```

---

## 三、诱发噪点的词（**不要写**）

### 3.1 直接诱发颗粒
`胶片颗粒` `颗粒感` ` gritty` `film grain` `grain` `noise` `ISO noise` `dust` `speckle` `颗粒质感`

### 3.2 间接诱发（更容易被忽略）
| 类别 | 词 | 为什么 |
|---|---|---|
| 胶片系 | `film emulation` `胶片模拟` `胶片质感` `Kodak 500T / 250D / Vision3` `vintage` `retro` `90s anime` | 模型会连"胶片颗粒"一起画出来 |
| 曝光系 | `underexposed` `crushed blacks` `欠曝` `暗部厚重` | 暗部一压就出噪 |
| 画质堆叠 | `8K` `ultra-detailed` `hyper-detailed` `razor sharp everywhere` `masterpiece` | 模型会用"假纹理"和"过度锐化"去堆细节 |
| 密度堆叠 | `countless` `hundreds of` `intricate microtexture` `每一处都精细` | 会生成鱼鳞／蜂窝状的重复纹理 |

**例外（仅此一处）：** `look-library.md` **LOOK 卡 2（胶片暗房阳光风）** 必须写「可见 35mm 胶片颗粒 / Kodak Portra 400」，这是该风格的核心成分，**不适用本节黑名单**。其他风格（包括用户临时说「想要颗粒」）一律按黑名单删词。

**改写规则：**
- 想要"暗" → 写 `暗部深邃但干净，细节沉入黑色而不发脏`，不写"欠曝／压黑"。
- 想要"质感" → 写具体的材质（丝绸、石材、金属），不写"颗粒/胶片质感"。
- 想要"清晰" → 写 `清晰锐利（光学锐度，非数字锐化）`，不写 8K/hyper-detailed。

---

## 四、流程层规则（同样重要）

1. **全程 PNG**。JPEG / WebP 反复编码会把颗粒带回来；输出格式优先 png。
2. **不要在同一张图上连续多轮"再干净一点"**。每多一轮就叠一层颗粒。需要精修就：存盘 → 重新上传 → 新的一轮。
3. **quality 不要用 low**。low 会直接糊掉纹理，medium 是底线，精修用 high。
4. **背景避免纯黑**。深灰（约 #3A3A3A）比纯黑更不容易暴露暗部噪点；需要纯黑时，务必同时写"暗部干净无噪点"。
5. **分辨率不是越高越好**。噪点在高分辨率下会被放大，2K 通常比 4K 更干净，除非确实需要 4K。
6. **reference 图别带噪**。把一张本身有颗粒的图当参考，噪点会被继承。

---

## 五、自检（出图前逐条过）

- [ ] 提示词里没有 §3 的任何诱发词？
- [ ] 末尾挂了 §2 的防护块？
- [ ] 参考图本身是干净的？
- [ ] 输出格式是 PNG？
- [ ] quality ≥ medium？
- [ ] 没有在同一张图上做第 3 轮以上的连改？

---

## 来源

- OpenAI Developer Community：*Multiple gpt-image-1 high fidelity edits lead to grainy result*（编辑链累积颗粒、压缩与 PNG 问题）
- `AI_Cinematic_Prompt` 适配器 `adapters/general.md`（明确列出 grain / film emulation / underexposed / crushed blacks 会诱发脏噪点，并给出整洁暗部的改写句）
- 中文实测流程整理：*GPT 出图全是噪点？两个思路解决*、*GPT 出图总是脏？这套流程能救回大部分"废图"*、*Image2 出图总有噪点？删掉这 4 个词*
- UCloud Modelverse《AI Image Prompt Writing Guide》（质量词堆叠与噪点关系）
