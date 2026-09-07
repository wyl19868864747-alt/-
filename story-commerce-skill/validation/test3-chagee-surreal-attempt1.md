# TEST 3｜CHAGEE 伯牙绝弦 × ST05 超现实创意广告风｜Attempt 1

状态：`PARTIAL / STYLE PASS, RHYTHM FAIL`

产品：霸王茶姬「伯牙绝弦」
用户确认卖点：`清爽不腻，茶底扎实`
时长：约15秒

## 真实成片观察

### Style
- ST05 超现实创意广告风可识别：真实摄影底座 + 单一琥珀色茶浪奇观成立。
- 产品蓝白杯身、黑色杯盖、品牌识别在多数镜头中稳定。
- 超现实机制基本没有把产品本体变形。

### Rhythm
失败。

真实成片主要镜头块约为：
- 0–1.8s：人物 + 产品建立；
- 1.8–3.9s：产品近景；
- 3.9–8.9s：喝第一口 + 茶浪扩散，单一镜头持续约5秒；
- 8.9–11.2s：人物Reaction近景；
- 11.2–15s：产品Hero，持续约3.8秒。

15秒里主要只有约5个镜头块，最长核心奇观镜头接近5秒，结尾Hero接近4秒。结果是：
- 明显慢动作 / TVC感；
- 信息密度低；
- 奇观在“展示”而不是“打击”；
- Reaction停留过长；
- Hero停留过长；
- 缺少聪明、利落、连续升级的paid-social节奏。

## Root cause

不是 ST05 视觉方向本身失败，而是 Prompt 的时间分配和动词选择把“超现实”误编译成了“缓慢奇观展示”。

原 Prompt 中：
- 6–9s 给茶浪完整3秒；
- 9–11.5s 给人物Reaction约2.5秒；
- 11.5–15s 给Hero约3.5秒；

三段都属于低信息持续镜头，叠加后自然产生慢TVC感。

### Candidate transferable rule

`SURREAL ≠ SLOW SPECTACLE`

`15S PAID SOCIAL = FAST CAUSAL COMPRESSION`

对15秒剧情带货：
- 默认约6–9个有价值视觉Beat；
- 普通Beat优先约0.8–2.0s；
- 非连续Proof必要镜头尽量不超过2.5s；
- Strong Reaction优先0.4–0.8s；
- 超现实Reveal优先0.5–1.2s完成“触发→异常→结果”；
- Product Hero通常1.0–1.5s足够；
- 每1–2秒必须新增状态、Proof、Reaction或视觉信息；
- 通过硬切、动作匹配切、短甩镜、快速推近、Snap SFX建立“聪明、紧凑”，不是机械1秒一镜。

ST05尤其应优先：
`NORMAL → TRIGGER → SURREAL HIT → RESULT → QUICK VERIFY → PRODUCT`
而不是：
`NORMAL → 长时间慢速奇观 → 长Reaction → 长Hero`。

## 下一步

只重测节奏，不改：
- 产品；
- 用户卖点；
- ST05 Style；
- 唯一“茶浪净场”机制。

重写为高密度约8 Beat版本，验证“强超现实风格 + 快节奏聪明买量节奏”能否同时成立。若通过，再考虑把上述 Candidate rule 晋升到 `paid-social-rhythm-dna.md`。