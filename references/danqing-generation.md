# 丹青执行层（Danqing Generation）

> 用途：把 AAA 产出的提示词**真正跑出图/视频**。
> 通道：全局 MCP `danqing-mcp`（服务名 `danqing-aigc`，85 个工具）。
> 前提：已用 `claude mcp login danqing-mcp` 完成 OAuth；**新装或刚登录后要重启会话**，工具才会出现。

---

## 一、先立三条执行纪律

1. **默认不出图。** AAA 的本职仍是产出提示词文本。只有用户明确说「生成 / 跑一下 / 直接出图 / 用这个出」才执行。
2. **执行前先报账。** 所有生成都扣积分。第一次执行前先跑 `list_credit_accounts`（+ `list_gateway_credit_accounts`），把可用账户和余额告诉用户，等他确认。
3. **一次只跑一张/一条。** 先验证提示词有效，再批量。不要在没有单张成功证据前开多条。

---

## 二、通用三步

```
① 上传（仅本地文件）→ get_upload_url
② 生成 → 对应工具，拿 taskId
③ 等结果 → check_task(taskId, wait=true，内部最多等 50s)
```

- `get_upload_url` 无输入参数，调用后按其返回的地址/说明上传，拿到临时 URL。**文件每日自动清理**。
- 已经是在线 URL 的，跳过第 ① 步。
- `check_task` 默认 `wait:true`，50 秒没完成会返回当前状态；用同一个 `taskId` 再调即可继续等。

---

## 三、模型 → 工具名对照

> ⚠️ **AAA 写的模型名不能直接当参数用**，必须映射到下面这张表。

### 图像

| AAA 里的模型 | 丹青工具 | 关键限制 |
|---|---|---|
| GPT Image 2.5 Flare | `gpt_image_2_5_flare` | 参考图 ≤10 张，prompt ≤5000 字符 |
| GPT Image 2.5 Sunburst | `gpt_image_2_5_sunburst` | 同上 |
| GPT Image 2（旧版兼容） | `gpt_image_2` | 参考图 ≤10 张 |
| **Seedream 5.0 Pro** | `doubao_seedream_5_pro` | 参考图 ≤10 张，prompt 建议 ≤300 汉字 |
| Seedream 5.0 Lite | `doubao_seedream_5_lite` | 支持组图，参考+生成共 ≤15 张 |
| **Nano Banana 2.1** | `nano_banana_2_1` | 参考图 ≤14 张，比例支持 1:8~8:1，1K/2K/4K |
| Nano Banana 2.0 | `nano_banana_2` | 参考图 ≤14 张 |
| Nano Banana Pro | `banana_pro` | 参考图 ≤10 张 |
| **Midjourney** | `midjourney_imagine` | **最高 V8.1**，见下方冲突说明 |
| FLUX / SD | —— | 丹青没有对应工具，走别的平台 |
| 即梦 | `jimeng_image_v4` | 参考图 ≤10 张 |
| Gemini | `gemini_25_flash` | 参考图 ≤5 张 |

### 视频

| AAA 里的模型 | 丹青工具 | 关键限制 |
|---|---|---|
| **Seedance 2.5（多模态参考）** | `seedance_2_5_all_in_one` | 4–30 秒，480p/720p，参考图 ≤30 张 |
| **Seedance 2.5（首尾帧）** | `seedance_2_5_first_last_video` | 同上，另有首/尾帧 URL |
| Seedance 2.0 | `seedance_2_all_in_one` / `seedance_2_first_last_video` | — |
| MiniMax H3 | `minimax_h3_all_in_one` / `minimax_h3_first_last_video` | 支持 2K |
| 可灵 | `kling_i2v` / `kling_o1_i2v` / `kling_first_last_video` | — |
| Runway | `runway_first_last_video` | — |
| Wan 3 | `wan_3_all_in` / `wan_3_first_last_video` | 最长 30 秒、1080P |
| 即梦 | `jimeng_i2v` / `jimeng_first_last_video` | — |

---

## 四、参数映射（AAA 产出 → 丹青字段）

### 单帧（第4站）

| AAA 的东西 | 落到哪个字段 | 注意 |
|---|---|---|
| 九层单帧正文 + 【全局质量提示词】 | `prompt` | 合成**一段连续文本**，不要带九层编号和 Markdown 符号 |
| 画幅比例 | `size`（GPT/Nano）/ `mjPicScale`（MJ） | Seedream 用 `size` 传 `1K`/`2K` 或具体像素 |
| 分辨率 | `resolution` | **默认 2K（2560×1440），不默认 UHD/4K**；各模型档位不同：GPT 有 UHD，Nano 有 4K，Seedream 只有 1K/2K。用户明确要求 4K/UHD 才升档 |
| 角色 / 场景 / 道具资产 | `imageUrls` 数组 | **顺序就是权重**，主参考放第一张 |
| 素材职责里的「不采用」 | 写进 `prompt` 正文 | 丹青没有单独的负向字段 |
| 第3站的表情版设定图 | `imageUrls` 第一张 | 该段戏就挂微笑版 |

**MJ 的参考图要分槽位**，不是一股脑塞 `inputImages`：

| 用途 | 字段 |
|---|---|
| 垫图（影响构图/内容） | `inputImages`（每项需 `url` + `weight`） |
| 角色一致性 | `roleImages`（weight 通常 100） |
| 风格参考 | `styleImages`（weight 通常 100） |

### 视频（第5站）

| AAA 的东西 | 落到哪个字段 |
|---|---|
| 视频提示词正文（阶段式） | `prompt` |
| 第5站 5.2 的「素材职责」 | 用 **`@图片N` / `@视频N` / `@角色N`** 在 prompt 里引用 |
| 首帧 / 尾帧 | `firstFrameImageUrl` / `lastFrameImageUrl` |
| 比例 | `ratio`（21:9/16:9/4:3/1:1/3:4/9:16/adaptive） |
| 时长 | `duration`（4–30 秒）；开了 `adaptiveDuration=1` 时该值失效 |
| 是否要声音 | `generateAudio`：`0` / `1`（**字符串，不是布尔**） |
| 角色参考 | `roles` 数组，配合 `@角色` 使用 |

---

## 五、分站路由

| 站 | 用户在做什么 | 调哪个 |
|---|---|---|
| 第3站 建资产 | 出角色四格设定图 / 场景 / 道具 | 一张一张跑单帧工具；多角度补图用 `multi_angle_generation` |
| 第4站 拆单帧 | 出每一镜的静帧 | 单帧工具，`imageUrls` 挂资产 |
| 第4站（线稿场景） | 线稿/白模 → 场景概念图 | `scene_concept_art`（需 styleReferenceImageUrl + whiteMoldImageUrl + prompt） |
| 第4站（线稿转控制图） | 线稿 → 深度/法线/边缘 | `depth_normal_curvature` |
| 第5站 生视频 | 静帧 → 视频 | 视频工具；有首尾帧用 `first_last`，多模态用 `all_in_one` |
| 第5.5站 诊断 | 查 AI 痕迹 / 查重 | `duplicate_check_ai_trace` / `duplicate_check_original` |
| 找参考 | 搜 Pinterest / ArtStation / 花瓣 | `search_images`（结果可直接喂 `reference-decode.md`） |

---

## 六、积分账户

| 工具 | 干什么 |
|---|---|
| `list_credit_accounts` | 列出个人 + 项目积分账户 |
| `list_gateway_credit_accounts` | 列出雷火网关积分（独立扣费来源） |
| `set_default_credit_account` | 把某个项目账户设为默认 |
| `set_default_gateway_account` | 把网关账户设为默认 |
| `clear_default_*` | 清除默认 |

- 不传 `accountId` = 扣个人积分。
- 个人积分不足时，先 `list_credit_accounts` 让用户选，再把选中的 `accountId` 逐个传进生成工具。
- **网关账户与项目默认账户互斥**，不能同时设。

---

## 七、已知冲突与限制

### ⚠️ Midjourney 版本对不上

- AAA 的 `model-adapters.md` 写 **V8.2**
- 丹青的 `midjourney_imagine` 只支持 **V6 / V6.1 / Niji6 / Niji7 / V7 / V8.1**

**执行时一律取 V8.1**，把 `mjModel: "V8.1"` 明确传进去。不要因为 AAA 写了 V8.2 就往参数里塞 V8.2。**版本以执行通道为准，不以文案为准。**

### 其他

| 限制 | 说明 |
|---|---|
| FLUX / SD 没有 | 丹青不提供，换平台 |
| Seedance 分辨率 | 只有 **480p / 720p**，没有 1080p |
| 视频时长上限 | 30 秒（Wan 3 也是 30 秒） |
| 参考图格式 | jpeg/png/webp，单张 ≤10MB；**透明 PNG 建议先转白底** |
| 比例范围 | 多数模型 0.33~3，Nano Banana 2.1 可到 1:8 |
| 本地文件 | 必须先 `get_upload_url`，丹青不收本地路径 |

---

## 八、未实测声明（重要）

这份文件里的**参数来自工具的 schema 定义，不是实际跑通的结果**。本次编写时：

- ✅ 已完成：MCP 登录、连接、列出 85 个工具、抓取参数 schema
- ❌ **未执行**：任何一次真实生成（会扣积分）
- ❓ 未确认：`get_upload_url` 的返回格式（该工具没有声明输入/输出 schema，需实际调用才知道）

**首次执行时按这个顺序验证**：

1. 先跑 `list_credit_accounts`，确认有余额
2. 跑一张最低成本的图（`quality: "low"` 或 `1K`）
3. 确认返回里有 `taskId`，再 `check_task`
4. 拿到图确认效果，再放大批量

如果第一次就失败，把错误原文记下来，补到本文件末尾——**不要靠猜改参数**。

---

## 九、执行前自检

- [ ] 用户明确要求"生成/出图/跑一下"，不是只是要提示词
- [ ] 已经报过积分账户，用户确认了
- [ ] 模型名映射到了正确的工具名
- [ ] MJ 用的是 V8.1，不是 V8.2
- [ ] prompt 是连续文本，没有九层编号、Markdown 符号
- [ ] 本地文件已经过 `get_upload_url`
- [ ] 参考图顺序 = 素材职责的优先级
- [ ] 只跑了一张/一条，没有直接批量
