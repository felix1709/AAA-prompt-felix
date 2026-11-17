# 大师调用：按需触发，不是流程步骤

> 知识库 `E:\felix_work_2025\知识库\知识库\skills\masters\` 里有 11 位专业大师。
> **平时不调。** 只在两种情况下进场。

---

## 一、什么时候调

| 触发 | 说法 | 做法 |
|---|---|---|
| **用户主动开会** | 「开个会」「让大师看看」「评审一下」「这个方案怎么样」 | 相关大师同时进场，各出一份意见 |
| **产生歧义** | 我拿不准、skill 内部规则冲突、用户要求互相矛盾 | 自动调对应大师判断，并把结论说清楚 |

平时正常走六站流程，**不要把大师当检查点**。

---

## 二、歧义时找谁

| 问题 | 大师 | 路径 |
|---|---|---|
| 构图、机位、视线、调度、镜头连续性 | composition | `skills/masters/composition/SKILL.md` |
| 布光、光比、光源动机、氛围 | lighting | `skills/masters/lighting/SKILL.md` |
| 动作、姿态、重心、比例、表演可读性 | action | `skills/masters/action/SKILL.md` |
| 色彩脚本、镜头间色调统一 | color | `skills/masters/color/SKILL.md` |
| 剪辑节奏、合成、声音、交付规格 | post | `skills/masters/post/SKILL.md` |
| 造型、场景美术、视觉调性 | art | `skills/masters/art/SKILL.md` |
| 叙事、开场钩子、风格化、反转 | director | `skills/masters/director/SKILL.md` |
| 人物动机、对白、潜台词、关系节拍 | screenwriter | `skills/masters/screenwriter/SKILL.md` |
| 跨模型提示词转换 | prompt | `skills/masters/prompt/SKILL.md` |
| 3D 管线、软件选型 | technical | `skills/masters/technical/SKILL.md` |
| 知识库资料本身的质量核验 | auditor | `skills/masters/auditor/SKILL.md` |

---

## 三、怎么用

1. 读对应 `SKILL.md`，按它的「工作方法」和「输出结构」出意见
2. 大师的意见是**判断**，最终提示词仍按本 skill 的写法编译
3. 大师之间冲突时，按 `reference-decode.md` 的优先级处理：
   `用户锁定 > 新场景硬事实 > 大师建议 > 系统默认`
4. 不把大师的意见原文贴给用户，压成 3–5 条可执行结论

---

## 四、开会时的输出

多位大师同时进场时，固定格式：

```
【问题】一句话说清歧义点
【<大师1>】结论 + 理由（≤3 行）
【<大师2>】结论 + 理由（≤3 行）
【共识 / 分歧】如果分歧，说明分歧点是什么
【建议】一条可执行的下一步
```

不输出大师的完整分析，只输出结论。
