# TEST 3｜CHAGEE 伯牙绝弦 × ST05 超现实创意广告风｜Attempt 3

状态：`PARTIAL / SURREAL SCALE PASS, RHYTHM PASS, WORLD-STATE CONTINUITY PARTIAL`

产品：霸王茶姬「伯牙绝弦」
用户确认卖点：`清爽不腻，茶底扎实`
时长：15.04s

## 真实成片观察

### 1. Style / Spectacle
- `SURREAL SCALE GATE`：PASS。约4.5s后巨大绿色茶叶进入画面，5.5–6.0s形成完整巨型茶叶/茶园峡谷世界，静止单帧已明显属于现实中不可能存在的尺度奇观。
- `PRODUCT SEMANTIC MATERIAL`：PASS。主奇观从茶叶、茶园、奶白轻薄流线等产品相关语义生成，不再使用与伯牙绝弦不匹配的红色随机液体。
- `PRODUCT TONE MATCH`：PASS。绿色茶叶、清透空间、奶白轻薄元素与“清爽不腻，茶底扎实”方向一致。
- `GENERIC VFX`：PASS。成片已经从“真实剧情+光带”升级为“产品原料改写世界尺度”。

### 2. Reality Hold / Impact
- PASS / BASICALLY ACHIEVED。人物喝下第一口后，约4.2s仍处于完全真实环境，约4.5s开始巨大叶片世界突入，前后存在短真实窗口，形成视觉落差。
- 高能第一击比Attempt 2明显更成立。

### 3. Paid-social Rhythm
- PASS。主要硬切/明显镜头变化约发生在1.0s、2.0s、4.2s、5.1s、6.1s、7.25s、8.0s、10.4s、11.6s、12.4s附近，15秒内约10+个有效视觉段。
- 没有Attempt 1中5秒奇观慢展示 + 4秒Hero的问题。
- Reaction和Product detail明显缩短，整体更利落。

### 4. One Event / Camera Coverage
- PARTIAL PASS。开场产品→同一女生拿杯→喝→世界变化→继续持杯的主事件已经建立；机位变化多数是在同一事件上继续覆盖，不再完全像独立广告图拼贴。
- 产品与人物大部分镜头可维持同一事件语义。

### 5. World-state continuity
- PARTIAL / 主要剩余问题。
- 约4.5–6.0s进入巨型茶叶世界；约6.25–6.75s Reaction却突然回到真实室内；随后7.25–9.75s又重新回到绿色超现实背景/茶叶世界；约10.25s才再次回到真实环境。
- 也就是说：`SURREAL ON → REAL → SURREAL ON → REAL`，中间没有新的触发原因。
- 这会削弱“同一个世界被改写”的连续事件逻辑，仍有一点“不同画面拼接”的生成感。

## Root cause

现有Compiler已经锁了Action Spine和每镜继承状态，但没有把`SURREAL STATE`明确规定为持久状态。

模型把“Reaction特写”理解为允许切回干净真实背景，而不是“在已经进入的超现实世界里拍Reaction”。

## Transferable rule｜SURREAL STATE PERSISTENCE

一旦唯一主奇观从 `REAL` 进入 `SURREAL ON`：
- 所有后续机位、Reaction、产品ECU和使用镜头默认继续处于 `SURREAL ON`；
- 不能仅因为切近景/反应镜头就自动恢复真实世界；
- 只有明确写出的 `RETURN TRIGGER` 才允许从 `SURREAL ON → REAL`；
- 返回后不得再次无因进入 `SURREAL ON`，除非设计的是第二次有因触发，但ST05单一机制默认不允许第二次无必要触发。

推荐内部状态：
`REAL → REALITY HOLD → SURREAL ON → SURREAL ON (multi-angle coverage) → RETURN TRIGGER → REAL`

禁止：
`REAL → SURREAL → REAL → SURREAL → REAL`

## 当前裁决

Attempt 3不需要推翻ST05方向。

已经真实验证：
1. 产品语义奇观方向有效；
2. 巨物/世界化尺度有效；
3. 0.1–0.5s真实蓄力有效；
4. 15s高密度节奏可以与强超现实同时成立；
5. 下一处最小问题是“世界状态持久性”。

下一步若继续重测，只修 `SURREAL STATE PERSISTENCE`，不再改产品语义、奇观类型、节奏骨架或Action Spine。