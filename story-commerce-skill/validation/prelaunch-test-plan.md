# PRELAUNCH TEST PLAN｜上架前最小高价值测试计划

当前阶段：`FINAL COLD-START GATE`

目标：停止实验室穷举。真实视频回归、跨品类文本压力与Registry收口已经完成；上架前只剩普通用户冷启动验证。

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

## 三种物理产品形态
已有真实视频证据：
- 刚性小物：AirPods；
- 柔性服装：旅行夹克 / Reference羽毛裙；
- 容器与液体：沙拉酱摇摇瓶。

## Product Reference / Product Lock
Reference服装测试证明产品外观可以跨剧情保持主要识别特征，同时暴露并修复穿戴Ownership与Reveal泄漏问题。

## CTA
多轮真实生成已确认默认：
`最后约1.5–3s → 高清放大Product Hero → 无生成CTA文字`
是稳定基线。

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

# 3. 当前30秒执行基线

不是完整短剧，而是：

`DRAMA EARNS ATTENTION`
→ `PRODUCT PIVOT`
→ `PRODUCT TAKES OVER`
→ `PROOF ESCALATES DESIRE`
→ `CTA`

中前段允许剧情与人物吸引注意力，但产品出现后必须成为广告视觉与因果主角。

---

# 4. 当前核心导演链

`Commercial Decision`
→ `Perceived Value Contrast`
→ `Product-Centered Narrative Gate`
→ `Story Architecture`
→ `Proof Plan`
→ `Reversal Router`
→ `Paid-Social Rhythm`
→ `Scene Staging`
→ `Physical Logic`
→ `Performance / FACS`
→ `Camera × Emotion / Action`
→ `Audio Event Map`
→ `Prompt Attention Compression`
→ `Seedance Prompt`

下游不能为了风格、情绪、镜头或反转改写Product Truth和Best Proof。

---

# 5. 不再继续做的测试

上架前停止：
- 12 Scene × 多SKU穷举；
- 每个商品分别测试R0/R1/R2；
- 继续反复AirPods；
- 继续反复服装；
- 再生成多个容器案例；
- 为边际CTA或单次随机AI瑕疵重新扰动已通过结构。

除非冷启动暴露结构性缺陷，否则不新增3.4.3 Hotfix。

---

# 6. 最后唯一上架Gate｜普通用户冷启动

模拟一个完全不了解内部Skill结构的真实用户。

用户只给：
- 一个商品名称，或
- 一组商品参考图，或
- 一个简单商品卖点；

再说类似：
> “帮我做一条美国TikTok剧情带货广告。”

Skill必须在不要求用户理解以下内部概念的情况下自动完成：
- Duration Router；
- Direct / Need-led；
- Perceived Value Contrast；
- Story Architecture；
- R0/R1/R2；
- Product Pivot / Takeover；
- Proof Ladder；
- Scene Staging；
- FACS；
- Camera × Emotion；
- Audio Event Map；
- Prompt Attention。

## 冷启动PASS标准

1. 不先追问一堆内部参数；
2. 自动识别真实购买问题；
3. 不编造产品事实；
4. 时长选择合理，必要时主动从30s降15s；
5. 剧情删除产品后不能原样成立；
6. 产品中后段有明确Takeover；
7. Proof真实可见；
8. 人物情绪、表情和运镜真正配合；
9. 场面调度没有明显方向/元素关系错误；
10. 最终Prompt已经压缩，不把Skill全文倾倒给视频模型；
11. 用户拿到即可直接生成，而无需理解内部路由。

如果以上通过：

> `PRELAUNCH CANDIDATE → LISTING READY`

然后停止实验室研发，进入真实用户案例驱动迭代。

---

# 7. 当前结论

真实视频验证、三类产品形态、20类文本压力、3.4.2导演Hotfix与Registry收口均已完成。

**剩余工作只有：1次普通用户冷启动测试。**
