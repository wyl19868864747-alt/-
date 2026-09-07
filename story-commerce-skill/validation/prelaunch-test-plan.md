# PRELAUNCH TEST PLAN｜上架前最小高价值测试计划

当前阶段：`LISTING READY`

目标：停止实验室穷举。真实视频回归、跨品类文本压力、Style最小回归、ST05超现实专项修复与普通用户冷启动均已完成；后续进入真实用户案例驱动迭代。

---

# 1. 已完成验证

## 15秒单卖点
已通过真实AirPods案例证明：
- 单一强卖点在15s内可完成商业因果；
- Duration Fit有效；
- 180°轴线、Motive Force、Meta-Camera Guard、Benefit Decodability有效；
- 不再为了默认30s强行填时长。

## 30秒剧情广告
真实服装、羽毛裙、7-Eleven与容器案例已经覆盖并暴露/修复：
- Hook与持续冲突；
- 对白负载与Speaker Lock；
- Reaction与FACS；
- Delay → Burst；
- Product Pivot / Product Takeover；
- Proof Ladder；
- TV SHORT DRIFT；
- Prompt Attention稀释；
- Camera × Emotion；
- Audio Event Map；
- Scene Staging；
- Wearable Ownership / Reveal State；
- Physical Logic / State Conservation。

## Style Lock最小回归
ST01 美式原生手机实拍风、ST02 高端静奢广告风、ST05 超现实创意广告风已完成最小高价值真实测试。

已验证：
- 同一产品可在不同Style下形成明显视觉距离；
- Style可以强锁，但不能削弱完成Proof所需的真实动作；
- ST05需要产品语义、卖点因果、真实世界锚点、Reality Hold、世界状态连续性与明确Return Trigger；
- `REAL + IMPOSSIBLE = SURREAL`，背景替换/拼图不等于超现实视觉奇观；
- `SPECTACLE CAUSAL MEANING > SPECTACLE BEAUTY`。

## 三种物理产品形态
已有真实视频证据：
- 刚性小物：AirPods；
- 柔性服装：旅行夹克 / Reference羽毛裙；
- 容器与液体：沙拉酱摇摇瓶。

## Product Reference / Product Lock
Reference服装测试证明产品外观可以跨剧情保持主要识别特征，同时暴露并修复穿戴Ownership与Reveal泄漏问题。

## CTA / Audio Close
已形成稳定规则：
`CTA IS A TERMINAL STATE, NOT A NEW ACTION START`

最终CTA必须停止启动新事件，画面和音频同时完成收束：
`IMAGE CLOSE + AUDIO CLOSE = AD CLOSE`

## English Promotional Voiceover
当用户未要求无旁白、也未提供完整VO时：
- 根据已确认Product Truth与卖点自动生成英文宣传旁白；
- 旁白分布在前/中/后关键节点；
- 不逐镜解说；
- 不新增产品事实；
- 不与关键人物对白抢权重。

## 文本压力测试
`text-stress-benchmark-v1.md`已完成20类实体商品：
- 20/20有效路由；
- 无Story Architecture结构性崩坏；
- 无R2滥用；
- 无30s强迫症；
- 高风险/不可见Proof能被Guard；
- Perceived Value Contrast跨品类工作正常；
- Product-Centered Gate没有明显TV SHORT DRIFT。

---

# 2. 当前默认时长

用户未指定时长：
> **首推约30秒。**

但如果：
- 单一卖点；
- 单一强Proof；
- 12–18秒已经自然讲完；
- 继续延长只会重复使用/Reaction/背景事件；

则主动建议15秒。

`DEFAULT 30s`不能覆盖`DURATION FIT`。

---

# 3. 当前执行基线

不是完整短剧，而是：

`DRAMA / HOOK EARNS ATTENTION`
→ `PRODUCT PIVOT`
→ `PRODUCT TAKES OVER`
→ `PROOF ESCALATES DESIRE`
→ `CTA TERMINAL STATE`

中前段允许剧情与人物吸引注意力，但产品出现后必须成为广告视觉与因果主角。

---

# 4. 当前核心导演链

`Commercial Decision`
→ `Perceived Value Contrast`
→ `Product-Centered Narrative Gate`
→ `Story Architecture`
→ `Proof Plan`
→ `Reversal Router`
→ `Style Lock`
→ `Location Router`
→ `Scene Staging`
→ `Physical Logic`
→ `Performance / FACS`
→ `Camera × Emotion / Action`
→ `Audio / English Promotional Voiceover`
→ `Prompt Attention Compression`
→ `CTA Terminal State`
→ `Seedance Prompt`

ST05额外：
`Selling Point → Spectacle Decision Gate → Surreal Visual Compiler`

下游不能为了风格、情绪、镜头、奇观或反转改写Product Truth和Best Proof。

---

# 5. 最终普通用户冷启动

已执行：`final-cold-start-gate-v1.md`

模拟输入：
> “这是我的产品，一款黑色真皮女包，帮我做一条美国TikTok剧情带货广告。”

用户没有提供时长、Router、R-level、场景、FACS、运镜、BGM等内部参数。

Skill自动完成：
- Truth Lock / Unknown Guard；
- Core Decision；
- Best Proof / Expression；
- 15s Duration Fit；
- Direct Product Route；
- Story Architecture；
- R0；
- 默认ST01 Style；
- Location；
- Performance / Camera；
- English Promotional Voiceover；
- CTA Terminal State；
- 可直接生成的Seedance Prompt。

## 冷启动11项结果

1. 不先追问一堆内部参数：`PASS`
2. 自动识别真实购买问题：`PASS`
3. 不编造产品事实：`PASS`
4. 时长选择合理：`PASS`
5. 删除产品后剧情不能原样成立：`PASS`
6. 产品明确Takeover：`PASS`
7. Proof / Expression真实可见：`PASS`
8. 情绪、表情和运镜配合：`PASS`
9. 场面调度方向清楚：`PASS`
10. Prompt已压缩：`PASS`
11. 用户拿到即可直接生成：`PASS`

`FINAL COLD-START GATE = PASS`

---

# 6. 不再继续做的实验室测试

上架前停止：
- 12 Style × 多SKU穷举；
- 每个商品分别测试R0/R1/R2；
- 继续反复AirPods；
- 继续反复服装；
- 再生成多个容器案例；
- 继续反复伯牙绝弦/ST05；
- 为单次随机AI瑕疵重新扰动已通过结构。

后续只有真实用户高频、可复现、因果清楚的问题，才进入母版迭代。

---

# 7. 上架裁决

真实视频验证、三类产品形态、20类文本压力、Style Lock最小回归、ST05专项视觉决策、英文旁白、CTA收束与普通用户冷启动均已形成有效证据或明确规则。

> **`PRELAUNCH CANDIDATE → LISTING READY`**

从现在开始停止实验室研发，进入：

`商业上架 → 真实用户输入 → 失败归因 → 只修高频可复现问题`
