# 风格资产库（LOOK 卡）

> 用途：第2站问风格时，从这里列预置 LOOK 卡供用户选择；用户也可描述新风格，由你现场生成一张新卡。
>
> 每张卡必备字段：配色 / 渲染 / 光线 / 质感 / 情绪 / 全局质量提示词 / 避免清单 / 特殊引擎关联。
> **全局质量提示词**选卡后贯穿全案，挂载到第3/4/5站每一段提示词末尾，全篇不改。
>
> **新增一张卡的方法**：按下方格式填满字段即可；「特殊引擎」栏填 `h3-PV-test-doubao` / `film-darkroom-prompt` / `无`。

---

## LOOK 卡 1：电影实拍写实　〔特殊引擎：无·主线默认〕

- **配色**：自然色，电影级调色，暗部有密度不发灰
- **渲染**：真人写实电影质感，35mm 电影镜头，真实胶片实拍
- **光线**：自然光影，浅景深，眼神光自然，环境光真实反射
- **质感**：真实皮肤纹理毛孔，自然布料褶皱，发丝物理真实，电影颗粒
- **情绪**：电影叙事沉浸感，镜头呼吸感

**全局质量提示词**：

```
真人写实风格，电影级摄影，自然光影，真实皮肤纹理毛孔，自然布料褶皱，环境光真实反射，浅景深，电影颗粒，35mm电影镜头，手持呼吸感，色温自然，肤色还原准确，发丝物理真实，自然运动模糊，电影级后期调色，高清晰度
```

**避免**：塑料皮肤，棚拍级完美布光，广告片质感，过度磨皮，CG感

**适用模型**：Seedance 2.0 / 5.0、通用生图

---

## LOOK 卡 2：胶片暗房阳光风　〔特殊引擎：film-darkroom-prompt〕

- **配色**：暖金阳光 + 奶白中间调 + 柔和暗角，边缘低反差
- **渲染**：胶片暗房放大印相，化学色调，放大机光源辉光
- **光线**：高光柔焦晕开、梦幻发光，太阳眩光/镜头光斑，逆光发光，树叶斑驳光
- **质感**：可见 35mm 胶片颗粒（Kodak Portra 400 取向），乳剂纹理
- **情绪**：明亮通透、温暖怀旧、青春阳光

**全局质量提示词**：

```
胶片暗房放大质感，化学色调，高光柔焦晕开，梦幻发光，可见35mm胶片颗粒，柯达Portra 400质感，温暖金色阳光，太阳眩光，逆光发光，树叶斑驳光，明亮通透的户外空气感，柔和暗角，奶白中间调，怀旧胶片摄影，高清晰度
```

**避免**：数码噪点，CG渲染，3D感，刺眼硬光，生硬闪光，过饱和，塑料皮肤，水印

**英文关键词（进入 film-darkroom 分支时替换主语言）**：
`shot on 35mm film, darkroom enlargement print, chemistry-toned print, soft focus on highlights, blooming highlights, halation, dreamy glow, visible organic film grain, Kodak Portra 400 texture, sun-drenched daylight, warm golden sunlight, lens flare, backlit glow, milky midtones, gentle vignette`

**适用模型**：Seedance 5.0、Midjourney、FLUX

---

## LOOK 卡 3：2D 赛璐璐 PV　〔特殊引擎：h3-PV-test-doubao〕

- **配色**：高饱和、色块分明（建议限定 2–4 色系，如黑白+亮粉等，由参考图决定）
- **渲染**：二维动画、赛璐璐平涂、厚描线、平面层次，无 3D 纵深
- **光线**：硬边阴影、轮廓光、速度线残影，无体积光
- **质感**：色块分明、线条干净利落、手绘背景质感
- **情绪**：热烈节奏感、青春冲击力、高速剪辑感

**全局质量提示词**：

```
二维动画风格，赛璐璐渲染，色块分明，线条干净利落，硬边阴影，平面层次感，风格化人物造型，手绘背景质感，高饱和色彩，清晰轮廓线，无噪点，无3D渲染痕迹，无照片质感，帧率流畅，画面干净通透
```

**避免**：3D纵深，体积光，真实肤质，镜头虚化，标准淡入淡出，素描灰调

**英文关键词（进入 h3 分支时替换主语言）**：
`flat 2D cel-animation, editorial graphic design, high saturation, thick outlines, pure flat color fills, halftone dot shadows, speed lines, hard cuts, no 3D geometry, no realistic depth, no soft lighting, no lens blur`

**适用模型**：MiniMax H3

---

## 附：特殊引擎自动关联

| 选到 | 自动进入第6站的引擎 |
|---|---|
| 2D 赛璐璐 PV（及类似 2D 高速 PV 风） | h3-PV-test-doubao |
| 胶片暗房阳光风 | film-darkroom-prompt |
| 电影实拍写实 / 其他自定义风格 | 主线默认，无特殊分支 |
