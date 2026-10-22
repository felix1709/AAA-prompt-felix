# 负面词分类库

> 用途：写第4站九层的 `⑨避免`、或给 FLUX/SD 配负向词时使用。
> 核心：**按当前这张图最可能的崩法选，不要贴整库。**

---

## 一、先看模型怎么吃负面词（决定写在哪）

同样是"不要塑料皮肤"，五个模型的写法完全不同：

| 模型 | 负向机制 | 怎么写 |
|---|---|---|
| **Seedance**（视频） | 不支持独立负向字段 | 靠正向描述排除；**不要**自动加"无噪点/无水印/HDR"通用包 |
| **FLUX / SD** | 有独立负向提示词 | 英文逗号分隔，配权重 `(...)` |
| **Midjourney V8.2** | `--no` 参数 | 只放**短的、具体的、能干净排除**的词；不要放多词短语 |
| **GPT Image 2.5** | 没有独立字段 | 融进对应的那句话里（"车库保持普通当代感，不要赛博朋克打光"） |
| **Seedream 5.0 Pro** | 正向空间指令之后直接写排除 | 写具体防崩，不写通用质量词 |
| **Nano Banana** | 没有独立负向语法 | 写成指令内的直接约束，不要套 MJ 参数 |

> 写错地方 = 白写。

---

## 二、六类清单（按崩法选，不按风格选）

### 1. 通用合成感

`concept art`、`digital illustration`、`CGI appearance`、`3D render`、`game rendering`、`video game screenshot`、`plastic surfaces`、`clean digital image`、`oversharpening`、`HDR look`、`overprocessed colors`

**什么时候用**：画面一看就是 AI 图 / 概念图 / 游戏截图。

### 2. 人像与摆拍

`hero pose`、`model-like expression`、`looking directly at camera`、`beauty retouching`、`plastic skin`、`perfect facial symmetry`、`perfectly styled clothing`、`promotional portrait`、`fashion editorial`

**什么时候用**：有主角、有人物特写时。**纯空镜不要用这一组。**

### 3. 构图

`poster composition`、`perfectly centered subject`、`perfect symmetry`、`overly balanced composition`、`clean empty background`、`excessive subject separation`、`artificial shallow depth of field`、`trailer-style framing`

**什么时候用**：画面太"正"、像海报时。
**注意**：用户要的就是海报 / 定妆照 → **一条都别加**。

### 4. 灯光

`unmotivated rim light`、`artificial cinematic lighting`、`decorative volumetric light`、`excessive lens flare`、`neon glow`、`crushed blacks`、`blown highlights`、`teal-and-orange grading`

**什么时候用**：光没有出处、暗部死黑、高光死白、青橙调。

### 5. 城市与科幻

`generic cyberpunk neon`、`holographic interfaces`、`fantasy architecture`、`clean futuristic city`、`empty polished streets`、`luxury commercial cityscape`

**什么时候用**：场景是当代 / 近未来城市，却总被加上霓虹和全息屏。

### 6. 解剖与重复（技术崩坏）

`distorted hands`、`extra fingers`、`duplicated people`、`duplicated objects`、`unnatural posture`、`facial artifacts`

**什么时候用**：只在目标模型确实容易出错时加。**不要默认全上**——有些模型看到这些词反而更容易出错。

---

## 三、选择规则（五步）

1. 先选 **3–5 个**最可能发生的**类别**，不要逐条抄。
2. 加**主体相关**的（有人物 → 摆拍与磨皮）。
3. 加**场景相关**的（未来城市 → 霓虹与全息）。
4. 只在需要时加**技术崩坏词**。
5. **删掉互相矛盾的**。例：要近景特写，就不要禁"浅景深"；要海报感，就不要禁"居中构图"。

**总量参考：10–20 个短词，不要更多。**

---

## 四、和 AAA 现有规则的接口

| 现有规则 | 关系 |
|---|---|
| 九层 `⑨避免` | 从上面选 3–5 类，写**针对这张图**的一行；**不要写"不过饱和/不HDR"这种万金油** |
| `anti-ai-look.md` | 先改正向写法；负面词是兜底，不是主力 |
| **单帧禁止颗粒 / 噪点** | 不要在单帧里写"no grain"来抵消别的词——AAA 本来就不写颗粒，别自相矛盾 |
| Seedance 5.5 诊断 | 归因到「Prompt 问题」且确实是负面词缺失时，才回来补 |

---

## 五、常见错法

| 错法 | 后果 |
|---|---|
| 整个库贴上去 | 词与词互相打架，模型只能说"都别画"，画面变空 |
| 给所有风格都加"不要过饱和" | 有些风格就是要饱和（2D 赛璐璐、胶片阳光） |
| 在 Midjourney 用长句 `--no` | 会被拆开单独解释，产生矛盾 |
| 在 GPT Image 里以为有负向字段 | 压根不生效 |
| 用负面词代替正向设计 | 画面只会"少点什么"，不会"多对什么" |
| 一句提示词里同时禁"浅景深"又要"背景虚化" | 自相矛盾 |

---

## 六、自检

- [ ] 负向词写在了该模型真正支持的机制里
- [ ] 只选了 3–5 类，没有贴整库
- [ ] 加了主体相关和场景相关的那几类
- [ ] 没有和用户想达到的效果互相矛盾
- [ ] 没有把"万金油质量词"塞进 ⑨避免
- [ ] 单帧里没有出现与「禁止颗粒」冲突的写法
