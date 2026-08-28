# 模型适配层

> 用途：第5站生视频 / 第6站特殊分支时，把统一构思转成各目标模型要求的格式。
> 原则：主线全中文；MiniMax H3、Midjourney、FLUX 输出英文；Seedance 可中可英。

---

## 1. Seedance 2.0（视频）

- **语言**：中文
- **格式**：六段式
  1. 视听限制（无背景音乐、纯现场环境音、禁止字幕水印）
  2. 语言台词
  3. 运镜手法（镜头是否移动/路径/与角色关系）
  4. 风格色调与光景
  5. 角色与场景设定
  6. 时间轴详细叙事（按秒拆：景别/动作/神态/台词/声音）
- **硬上限**：全文 ≤ 1900 字（含标点），超限按「时间轴 → 环境音 → 角色次要细节 → 台词 → 秒段合并」顺序压缩
- **禁忌**：无精确物理数值；距离/高度用身体参照（一臂距离/与眼平齐）、画面比例（人物占画面几成）替代

---

## 2. Seedance 5.0（视频 / 出图）

- **语言**：中文或英文均可
- **视频**：沿用上文六段式
- **出图参数**：
  - `size`：人像 `1024x1536` / 场景横构 `1536x1024` / 单体特写方形 `1024x1024`
  - `quality`：`high`
- 出图前做三项确认：四锚点/质量词齐全、无冲突硬光词、尺寸匹配主体

---

## 3. MiniMax H3（视频）

- **语言**：英文
- **模式**：
  - Ref2VA —— 参考图只提供风格（默认）
  - I2VA —— 首帧对齐；L2VA —— 尾帧对齐；FL2VA —— 首尾帧对齐
- **字段**（拼写严格）：
  `subject_definitions` + `summary` + `retention_analysis` + `detailed_description` + `overall_soundscape` + `non_diegetic_music`
- **总字符** ≤ 10000；分配：detailed_description 主配 4000-5000，音轨/音乐各 800-1000
- **每镜** 50-200 字符，多数镜头一句话，仅关键镜头两句
- **镜头数**：15s → 18-25 镜
- **音轨**：按阶段块写（Hook / Build / Climax / Freeze），不按逐镜时间戳
- 对话格式 `(S1) says: <d>[English] Text.</d>`；屏上文字用英文双引号

---

## 4. Midjourney（生图）

- **语言**：英文关键词 + 参数
- 参数：`--ar`（人像 3:4 / 场景 4:3）、`--style raw`、`--stylize 100~250`、`--v 6`
- 用自然关键词组，不写长句叙事

---

## 5. FLUX / Stable Diffusion（生图）

- **语言**：英文
- **格式**：正向 + 负向，权重写法 `(35mm film:1.1)`
- 正向：风格加权关键词在前，场景/角色/道具/构图在后
- 负向：digital noise, CGI, 3d render, sharp studio light, harsh flash, oversaturated, plastic skin, watermark, text, logo, extra limbs, deformed, low quality, jpeg artifacts

---

## 6. GPT Image（生图）

- **语言**：中文或英文自然语言散文（非关键词堆砌）
- 压缩提示词，保留完整句子结构
- 颗粒/光晕类词改为纯正向清晰度表述（避免触发噪点）
