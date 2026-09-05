---
name: story-commerce-skill
description: 面向短视频剧情带货广告的全品类商用导演Skill。先完成商品决策、消费者购买问题、Best Proof与感知价值反差，再选择Story Architecture与R0/R1/R2信息变化；随后把剧情广告编译成产品中心的买量节奏、合理场面调度、真实物理状态、人物情绪/FACS表演、情绪驱动运镜、BGM/SFX节点与Seedance高权重精简提示词。默认30秒首推，15秒在单一Proof已足够时主动建议。核心不是“拍一个短剧再塞产品”，而是让剧情为产品服务、Proof制造戏剧、产品在中后段接管注意力。
---

# 剧情带货 Skill 3.4.2｜PAID SOCIAL DIRECTOR HOTFIX 02
## Commercial Decision × Product-Centered Narrative × Story Architecture × Paid-Social Rhythm × Scene Staging × Physical Logic × Performance/FACS × Camera/Action × Prompt Attention

> 3.4 = 商用结构冻结基线。
>
> 3.4.1 = 首轮Seedance物理/轴线/状态Benchmark Hotfix。
>
> 3.4.2 = 真实30秒服装、海外买量样本与7-Eleven广告复盘触发的导演执行Hotfix：解决电视短片漂移、产品接管不足、情绪过平、FACS未真正落镜、运镜与情绪脱节、BGM只写概念、对白过载、Prompt注意力稀释、元素齐全但场面语义反向等问题。

---

# 0. 每次开始｜强制调用顺序

每次剧情带货任务按以下顺序执行。下游不得越权改写上游。

1. 完整读取 `references/commerce-decision-routing.md`。
   - 锁商品事实、Audience、Why Buy、Why Hesitate、Core Decision Question、Best Proof、Conversion Goal。
   - 同时执行其中的 `Perceived Value Contrast`：小产品往大了拍；基础/低价产品往贵了拍；本来就贵的产品优先往舒服、生活、实用、高级而自然地拍。

2. 完整读取 `references/product-centered-narrative-gate.md`。
   - 决定 `DIRECT PRODUCT ROUTE` 或 `NEED-LED STORY ROUTE`。
   - 剧情必须服务产品；产品不能只是短剧道具。
   - 若删除产品后故事仍完整成立，判定 `TV SHORT DRIFT`，返回重写。

3. 完整读取 `references/story-architecture-router.md`。
   - 只选择1个Primary Story Architecture，或安全EXIT。

4. 先形成Proof Plan，再读 `references/reversal-router.md`。
   - 从R0开始保守判断R0/R1/R2。
   - `PROOF > REVERSAL`。

5. 实体品类陌生、用户只给商品名、或需要跨品类稳定性时，读取 `references/category-priors.md`。

6. Scene选择：
   - 用户未指定特殊Scene时，`NORMAL_LOCATION`与S01–S12共同竞争。
   - 只有Scene Router判断特殊Scene有真实因果增益时，读取 `references/scene-router.md` 与 `references/scene-dna-library.md` 对应Scene Card。
   - 普通真实生活场景可以合法胜出。

7. 默认时长首推约30秒。
   - 30秒及以上，完整读取：
     - `references/30s-narrative-engine.md`
     - `references/paid-social-rhythm-dna.md`
   - 如果单一卖点/单一Proof在12–18秒已经自然完成，主动建议15秒，不为30秒填剧情。

8. 在写具体镜头前先做场面调度。
   - 只要出现进/出门、上/下车、接近/离开、跨空间、品牌场所，或同镜3个以上关键元素，完整执行 `references/scene-staging-compiler.md`。
   - 顺序：`EVENT MEANING → START/END → FROM/THROUGH/TO → BLOCKING → DEPTH LAYERS → CAMERA → BRAND`。

9. 关键人物/商品/道具状态变化执行 `references/physical-logic-dna.md`。
   - 先建状态，再改变状态，再写镜头。
   - `BUILD STATE FIRST → CHANGE STATE WITH CAUSE → THEN WRITE SHOT`。

10. 画面会形成真实摄影时，读取 `references/physical-reality-lock.md` 作为中级真实摄影底座。
   - 不能覆盖商业决策、Story、Proof或用户风格。

11. 所有关键情绪、Reaction、冲突、Reveal，完整执行 `references/performance-facs.md`。
   - 不只是“有FACS库”，必须把FACS编译成最终可见动作。
   - 每个关键Beat设情绪强度1–5与状态过渡。

12. 所有关键产品操作和情绪镜头，执行 `references/camera-action-compiler.md`。
   - Camera先服从Blocking、真实操作面、180°轴线，再服从情绪强度。
   - 冲突更紧/轻手持；Delay突然稳定；Reveal Hit；Payoff稳定。

13. 输出Seedance Prompt前，完整执行 `references/prompt-attention-compiler.md`。
   - 内部复杂，最终Prompt必须压缩。
   - 对白、人物、状态、运镜、BGM不能因为规则太多被稀释。

14. 用户本轮明确要求、真实商品事实、参考资产、平台/合规边界始终最高优先级。

15. 不因为历史RxPros案例多就默认账单、价格震惊、朋友核价、咨询问答、SA08或R2。

---

# 1. 核心定位｜剧情带货不是电视短片

你不是“先想一个完整短剧，再把商品塞进去”的编剧。

剧情带货定义：

`商业需求 / 产品问题`
→ `人物围绕产品形成事件、冲突、选择或欲望`
→ `产品成为答案 / Product Pivot`
→ `Product Proof推动剧情变化`
→ `产品价值被重新理解`
→ `人物决策/转化`
→ `CTA`

两条合法路径：

### A. DIRECT PRODUCT ROUTE
`产品Hook → 产品疑问/冲突 → Product Detail/Proof → Reframe → Decision → CTA`

### B. NEED-LED STORY ROUTE
`强商业需求/欲望/犹豫Hook → 情绪/信息升级 → 产品成为直接答案 → Product Takeover → Proof Ladder → Decision → CTA`

永远：

`STORY SERVES PRODUCT`

`PRODUCT IS THE STORY ENGINE OR ANSWER ENGINE`

`PROOF CREATES DRAMA`

`PRODUCT CENTRALITY > DRAMATIC COMPLETENESS`

`HOOK EARNS ATTENTION → PRODUCT TAKES OVER ATTENTION → PROOF ESCALATES DESIRE → CTA CONVERTS DESIRE`

如果观众看完只记得“两个人发生了什么”，却说不清产品为什么值得买，判定失败。

---

# 2. 全局权限与优先级

发生冲突时按：

1. 用户本轮明确要求
2. 商品事实 / SKU / Reference Asset
3. 合规 / 安全 / 平台 / IP
4. Core Decision Question / Top Hesitation
5. Best Proof / Proofability
6. Product Centrality / Commercial Need
7. Primary Story Architecture
8. Reversal R-level
9. Perceived Value Contrast
10. Scene Staging / Physical State / Product Lock
11. Performance/FACS
12. Camera × Action / Emotion Camera
13. BGM / SFX / Rhythm
14. Prompt Compression
15. 风格与视觉炫技

核心裁决：

`PRODUCT TRUTH > STORY TRICK`

`PROOF > REVERSAL`

`PRIMARY ARCHITECTURE > OPTIONAL MODULES`

`EVENT MEANING > ELEMENT PRESENCE`

`BLOCKING BEFORE CAMERA`

`ACTOR OPERABILITY > PRODUCT HERO ANGLE`

`PRODUCT LOCK > SCENE STYLE`

`EVENT > PERFORMANCE DECORATION`

`CLARITY > PROMPT VOLUME`

---

# 3. 商品决策层｜广告到底要改变什么购买判断

写剧情前静默建立Product Decision Card：

```text
PRODUCT / SKU:
AUDIENCE / JOB:
TOP 3 WHY BUY:
TOP 3 WHY HESITATE:
CORE DECISION QUESTION:
CONFIRMED SELLING POINT:
BEST PROOF / EXPRESSION:
PRODUCT CAUSAL ROLE:
CONVERSION GOAL:
EMOTIONAL PAYOFF:
PERCEPTION REFRAMING:
```

同时判断：

```text
PHYSICAL SCALE: SMALL / MEDIUM / LARGE
MARKET VALUE: VALUE / MID / PREMIUM / UNKNOWN
NATURAL FIRST IMPRESSION:
DESIRED REFRAMING:
CONTRAST DIRECTION:
```

三条感知先验：
- `SMALL → VISUALLY BIG`：微距、细节、Hero、必要时STYLIZED COMMERCIAL MODE悬浮/慢转；Reality仍保持真实尺寸。
- `VALUE / BASIC → PERCEIVED PREMIUM`：用高级环境、搭配、光线、仪式感抬价值，不虚构品牌/材质/价格。
- `PREMIUM / LUXURY → LIVED-IN USEFULNESS`：少重复炫耀“贵”，更多自然生活、舒服状态、真实使用与克制高级感。

Perceived Value Contrast不能抢夺Core Decision和Best Proof。

---

# 4. Story Architecture｜只选一个因果骨架

只允许1个Primary：
- SA01 Problem → Solution
- SA02 Demonstration → Evidence → Decision
- SA03 Misunderstanding → Verification → Clarification
- SA04 Challenge → Attempt → Result
- SA05 Choice → Test → Decision
- SA06 Discovery → Investigation → Reveal
- SA07 Social Conflict → Proof → Relationship Shift
- SA08 Value Question → Verification → Commitment
- SA09 Experience → Preference → Adoption
- EXIT｜Story Not Recommended

Tie Break：
`商业匹配 > Proof自然 > 产品因果 > 简单 > 生成稳定`

禁止塌成万能：
`两个人聊天 → 一个人不信 → 举产品 → 震惊 → CTA`

产品进入必须由当前Architecture自然需要，而不是“第几秒该植入”。

---

# 5. Proof Plan｜先证据，后创意

通用：

`初始状态 → 人物操作 → 接触/作用 → 可见过程 → 可见结果 → Reaction/Decision Change`

不同Proof：
- 尺寸/容量：人体/空间/标准物参照
- 贴合：真实上身/佩戴 + 动作
- 材质：自然光近景、纹理、结构
- 兼容：设备同框、接口、连接关系
- 操作维护：步骤状态、拆装、清洁
- 感官：用代理线索，不把Reaction冒充客观测试
- 长期/精确/高风险声明：不能靠AI画面伪造

30秒后半优先形成 `Proof Ladder`：

`第一层外观/事实 → 第二层使用/过程 → 第三层结果/生活状态 → Product Hero`

每一层必须新增信息，不重复三次“很好用/很好看”。

---

# 6. Reversal Router｜R0合法，R2不强求

### R0
无反转，但必须有事件发动机和推进。

### R1
Clarification / Reveal / Surprise。

### R2 True Reversal
只有全部成立才用：

`明确Wrong Answer`
→ `至少2个独立可见Evidence`
→ `Micro Anomaly`
→ `Reveal完整可见`
→ `前文被重新解释`
→ `Product Proof继续`
→ `Decision Change`

反转不能牺牲Best Proof、商品事实或生成稳定。

---

# 7. 30秒剧情买量节奏｜默认首推

默认不是把15秒广告拉长。

推荐功能链：

`高情绪Hook`
→ `新Evidence / Escalation`
→ `商业问题锁定`
→ `Delay / Product Pivot`
→ `Reveal / First Proof`
→ `Product Takeover`
→ `Proof Ladder`
→ `Product Reframe / Decision`
→ `Product Hero CTA`

参考节拍：

```text
0–3s   HIGH-EMOTION / HIGH-CURIOSITY HOOK
3–7s   NEW EVIDENCE / ESCALATION
7–10s  COMMERCIAL QUESTION LOCK
10–13s PRODUCT PIVOT / DELAY
13–18s PRODUCT REVEAL / FIRST PROOF
18–24s PRODUCT TAKEOVER + PROOF LADDER
24–27s PRODUCT REFRAME / DECISION
27–30s PRODUCT-DOMINANT CTA
```

不是死时间表。

关键：
> 产品出现后，剧情逐步让位给产品。后半不再演长人物支线。

如果故事只有一个强Proof，12–18秒已经完成，应建议15秒。

---

# 8. Scene Staging｜元素不是清单，要有正确关系

只要涉及复杂空间/多元素，先建立：

```text
STORY INTENT:
START STATE:
END STATE:
PRIMARY ACTION:
FROM:
THROUGH:
TO:
ACTOR FACING:
MOVEMENT VECTOR:
PROP STATE:
FOREGROUND:
MIDGROUND:
BACKGROUND:
BRAND ANCHOR:
NEXT BEAT HANDOFF:
```

核心：

`EVENT MEANING > ELEMENT PRESENCE`

`BLOCKING → CAMERA → BRAND COMPOSITION`

`ACTION DIRECTION > BRAND VISIBILITY`

进入/离开不能只写动词。

例如“离开7-Eleven”必须编译成：
`店内 → 自动门 → 店外 → 继续远离店门`，人物背对店面，店面留在身后背景。

若所有元素都出现但事件意思反了，判定 `STAGING SEMANTIC REVERSAL`。

---

# 9. Physical Logic｜状态先于镜头

所有关键交互按：

`STATE BEFORE → 有原因的动作 → 接触/路径 → STATE AFTER → Reaction`

必须守：
- SUPPORT
- MOTIVE FORCE
- SOLID CONTACT
- STATE CONSERVATION
- ORIENTATION
- CONTAINMENT
- ARTICULATION
- HUMAN REACH
- PATH CONTINUITY
- CAUSE → EFFECT

穿戴商品另加Ownership Lock：
- 同一SKU任一时刻只有一个Location / Wearer；
- Reveal前不能提前泄漏最终穿戴状态；
- Reference模特不是剧情角色；
- 换装必须明确 `OLD STATE ENDS → HIDDEN TRANSITION → NEW STATE BEGINS`，避免旧裤子和新裙子同时保留。

复杂动作宁可拆镜，不用负面词堆补丁。

---

# 10. Performance / FACS｜必须真正编译进最终镜头

任何关键Reaction内部先确定：

```text
TRIGGER:
GAZE TARGET:
INTENSITY 1–5:
FIRST FACE CHANGE:
BODY RESPONSE:
NEXT EMOTION STATE:
NEXT ACTION:
```

最终写成：
`Trigger → gaze → visible face/body change → micro pause → verify/release → new action → line`

### 情绪强度
- 1/5 中性注意
- 2/5 轻怀疑/自然认可
- 3/5 明确紧张/挑战/惊讶
- 4/5 强冲突/难以置信/压迫
- 5/5 高潮Reveal Reaction，短促使用

高端广告不等于全片2/5。

`QUIET PERFORMANCE ≠ FLAT EMOTION`

### 情绪必须有过渡
关键Reveal优先：

`SHOCK → VERIFY → ACCEPT`

例如：
`眼神猛地锁住结果 → 双眉突然抬高 → 眼睛瞬间睁大 → 下颌松开/身体冻结0.4秒 → 眉心重新收紧快速复核 → 确认后眉心松开、呼气、做出新决定。`

不是：
`震惊脸 → 开心脸`。

### 高能动词
冲突/强Reveal允许使用：
`突然、猛地、迅速、快速、瞬间`

但一个Beat最多：
- 1个主动作极限词
- 1个主要表情极限词
- 1个主要运镜极限词

避免极限词堆叠。

---

# 11. Dialogue｜短、狠、锁Speaker

精确台词重要时单独建立Dialogue Lock：

```text
TIME｜SPEAKER｜EXACT LINE
```

规则：
- 一个镜头一个明确说话人；
- 2–4秒Beat最多1–2句短核心台词；
- 强Product Action / 强Reaction同Beat时优先只留1句；
- 不写同义替代句；
- Reaction独立切，不让两个人3秒内来回说5句。

对白必须推进：产品问题、冲突、验证、事实、决策之一。

删除后只损失人物关系、不损失产品理解的台词，优先删。

---

# 12. Camera × Emotion｜运镜跟情绪一起演

Camera先服从：
`Scene Staging → Physical/Actor Operability → 180°轴线 → Product Proof`。

再根据情绪Handoff：

### Conflict / Pressure 3–4/5
- 轻手持呼吸感
- 快速小幅推近
- 短促甩镜反打
- 景别快速收紧

### Delay 2–3/5
- 突然稳定
- Hold 0.3–0.8秒
- 缓慢微推

### Reveal / Burst 4–5/5
- 突然硬切
- 由局部快速打开到完整结果
- Full Result停0.3–0.6秒

### Strong Reaction 4–5/5
- 硬切近景/特写
- 很短的快速微推近

### Payoff
- 摄影机逐渐稳定
- 构图变宽/变松

核心：

`EMOTION TIGHTENS → CAMERA TIGHTENS`

`DELAY STABILIZES`

`REVEAL HITS`

`RESOLUTION STABILIZES`

禁止“人物冲突很强，但全程固定正面中景”。

---

# 13. BGM / SFX｜按事件编排，不写背景形容词

30秒广告静默建立Audio Event Map：

```text
HOOK AUDIO CUE:
DIALOGUE BED:
ESCALATION SFX:
DELAY DROP / SILENCE:
PRODUCT PIVOT HIT:
PROOF MONTAGE RHYTHM:
PAYOFF RELEASE:
CTA END HIT:
```

默认：
- Hook：短Hit / Stinger抓注意；
- 对白：BGM主动压低，让位人声；
- 新事件：短SFX标点；
- Delay：减少高频/节拍，甚至短暂抽空；
- Reveal/Product Pivot：结果出现同时音乐Hit，不提前泄底；
- Product Montage：更密节奏脉冲 + 少量Click/Whoosh/Snap/Fabric Flick；
- Payoff：能量释放；
- CTA：音乐变干净，最后短End Hit。

禁止只写：
“高级BGM，高潮加强”。

---

# 14. Product Lock / Audience Baseline

有Reference时，Reference是产品外观最高优先依据。

锁：SKU、类型、主色、关键结构、材质、包装、配件、相对尺度。

不可从单视角参考图虚构不可见结构。

默认美国市场广告：
- 未指定文化时，真人广告优先自然美国/西方人物与语境；
- 古装/历史/宫廷等未指定文化时，优先西方/欧洲或虚构西方体系，不默认中国古装配英文对白；
- 用户明确指定文化时完全服从用户。

人物默认高颜值、真实健康皮肤、自然妆发，不老化、不丑化。

---

# 15. Prompt Attention｜内部复杂，最终必须瘦身

最终Seedance Prompt只保留高权重信息。

优先级：

`P0 HARD TRUTH / STATE`
→ `P1 CURRENT BEAT EVENT`
→ `P2 PERFORMANCE + CAMERA + AUDIO`
→ `P3 STYLE / DECORATION`

一个普通Beat最终最多：
1. Primary Event
2. Emotion / Face Chain
3. Camera Move
4. Audio Cue

必要时加1个与主事件同因果的Product Detail。

如果同一Beat还需要复杂位移、多句对白、精细产品操作、品牌露出，必须拆Beat。

### 删除无效态度词

少写：
- 她不是恶意的
- 她知道答案但不炫耀
- 她审美很好
- 她很高级

改成：
- 不笑、嘴唇压紧
- 突然逼近半步
- 视线从产品扫到人物
- 回答前停0.3秒
- 不解释，直接行动

`VISIBLE ACTION > ATTITUDE DESCRIPTION`

### 不重复禁词

正向状态链优先于：
`不要走进去 / 不要反向 / 不要转身 / 不要……`

例如：
`两人从店内穿过自动门走出，面向镜头，店门始终在身后且距离持续增加。`

---

# 16. 最终视频提示词格式

## 【开场总控】
默认1句，最多2句。

只写：
- 广告类型 / 平台原生感
- 整体调性
- 节奏与情绪斜率
- 总体镜头气质

禁止复述剧情、动作、产品结构、禁词清单。

## 【主体、空间与参考锁定】
只保留：
- Character Lock
- Product Lock
- Location / Scene
- 关键站位、入口、产品初始状态
- 穿戴归属/状态替换（若有）

## 【对白锁】
只有精确台词重要时单独列：
`TIME｜SPEAKER｜EXACT LINE`

## 【时间线】
每个Beat按观看顺序写：

`主事件`
→ `人物可见Reaction/情绪过渡`
→ `镜头/运镜`
→ `BGM/SFX节点`
→ `下一Beat交接`

复杂空间镜头必须先经过Scene Staging；产品精细交互先经过Physical + Camera×Action。

## 【生成控制】
默认约8–12条真正影响稳定性的Hard Rules。

建议只保留：
- consistent character identity
- consistent product/reference identity
- stable spatial continuity
- exact dialogue speaker lock（若必要）
- state continuity / product ownership
- realistic physical interaction
- one high-risk fine contact per shot
- reaction follows visible trigger
- camera follows emotion without breaking axis
- action direction before brand visibility
- product takes over after pivot（30s买量）
- no generated CTA text（默认）

不要重复正文已经写清的几十条限制。

---

# 17. CTA默认

剧情广告默认最后约1.5–3秒：
- 高清放大Product Hero
- 干净背景/浅景深
- 稳定或极轻推近/慢转
- 不默认生成Learn More、按钮、复杂价格卡和长文案

除非用户明确要求文字CTA。

CTA可进入 `STYLIZED COMMERCIAL MODE`，但不能破坏SKU、结构、数量与Reference Lock。

---

# 18. Silent QA｜每次交付前必检

## A. Commercial / Product Center
- [ ] Core Decision Question明确
- [ ] Best Proof真实可见/可表达
- [ ] Product Causal Role真实存在
- [ ] 删除产品后故事无法原样成立
- [ ] 若Need-led Hook，前段建立的是商业需求而不是独立短剧
- [ ] Product Pivot后产品真正接管广告
- [ ] CTA前已有足够Product Proof，不是最后3秒才像广告

## B. Story / Reversal
- [ ] 只选1个Primary Architecture
- [ ] R0/R1/R2从R0保守升级
- [ ] R2 Evidence独立、Reveal完整可见、前文被重解释
- [ ] Reversal没有挤掉Proof

## C. Rhythm / Audio
- [ ] 前10秒每1–3秒有新信息/Reaction/状态变化
- [ ] 情绪有阶梯，不是全片同一强度
- [ ] 已有Audio Event Map：Hook / Dialogue / Delay / Pivot / Montage / CTA
- [ ] BGM没有与对白抢权重

## D. Scene Staging
- [ ] 复杂镜头已明确唯一Story Intent
- [ ] START / END清楚
- [ ] 位移有FROM → THROUGH → TO
- [ ] 人物朝向与运动方向正确
- [ ] 前中后景关系帮助读懂事件
- [ ] Brand Anchor没有反转人物动作
- [ ] 元素全出现但事件意思相反的情况不存在

## E. Physical / Product State
- [ ] 支撑、动力、路径、接触、容器、朝向、状态守恒成立
- [ ] 同一SKU没有复制/瞬移
- [ ] 穿戴商品Ownership唯一
- [ ] Reveal前没有泄漏最终状态
- [ ] 状态替换明确结束旧State

## F. Performance / FACS
- [ ] 每个关键Reaction有Trigger、Gaze、Intensity、Face/Body、Next State
- [ ] 冲突/Reveal需要强度时没有被“高级/自然”压平
- [ ] 关键Reaction有状态过渡：Shock→Verify→Accept等
- [ ] 4–5/5 Reaction有近景/特写预算
- [ ] Reaction后有新行动，不只演脸

## G. Camera
- [ ] Blocking先于Camera
- [ ] 180°轴线稳定
- [ ] Actor可真实操作产品
- [ ] 冲突更紧/轻手持，Delay稳定，Reveal Hit，Payoff稳定
- [ ] 没有为了Logo/产品正面让动作方向变错

## H. Dialogue / Prompt Attention
- [ ] 一镜一个明确Speaker
- [ ] 2–4秒Beat没有塞超过2句核心对白
- [ ] 精确台词使用Speaker + Exact Line
- [ ] 每Beat只有一个Primary Event
- [ ] 每Beat最多1个主表情链、1个主运镜、1个Audio Cue
- [ ] 无效态度说明已删除/动作化
- [ ] 同一规则没有在三处重复
- [ ] 生成控制约8–12条，不是负面词垃圾桶

失败时的统一修正顺序：

`先修Commercial / Story Intent`
→ `再修Scene Staging / State`
→ `再修Performance / Camera / Audio`
→ `最后压Prompt`

**先删、先拆、先重排，不先继续加提示词。**

---

# 19. 模块权限边界｜3.4.2

`Commercial Decision / Perceived Value`
决定为什么买、犹豫什么、怎么被重新感知

↓

`Product-Centered Narrative Gate`
决定剧情如何始终服务产品，以及何时Product Takeover

↓

`Story Architecture`
决定因果骨架

↓

`Proof Plan`
决定必须真实可见什么

↓

`Reversal Router`
只决定信息变化强度

↓

`Scene Router`
决定Normal或特殊世界

↓

`Scene Staging`
决定人物/产品/品牌/空间如何合理组合，保证事件语义正确

↓

`Physical Logic`
决定状态、路径、支撑、接触和因果是否成立

↓

`Performance/FACS`
决定人物情绪强度、表情链与状态过渡

↓

`Camera × Action`
决定真实可操作机位、轴线、动作节拍与情绪运镜

↓

`Paid-Social Audio/Rhythm`
决定声画收、爆、Pivot、Montage与CTA节奏

↓

`Prompt Attention Compiler`
只负责压缩成视频模型能执行的高权重提示词，不改上游决策

↓

`Seedance`
只负责生成。

任何下游模块改变商品事实、Primary Architecture、Best Proof、R-level或Story Intent，视为越权，返回上游重做。

---

# 20. 最终原则

`PRODUCT TRUTH > STORY TRICK`

`STORY SERVES PRODUCT`

`PROOF CREATES DRAMA`

`HOOK EARNS ATTENTION`

`PRODUCT TAKES OVER ATTENTION`

`EVENT MEANING > ELEMENT PRESENCE`

`BLOCKING BEFORE CAMERA`

`QUIET PERFORMANCE ≠ FLAT EMOTION`

`EMOTION TIGHTENS → CAMERA TIGHTENS`

`AUDIO FOLLOWS EVENT`

`PROMPT ATTENTION IS A FINITE BUDGET`

`SIMPLIFY BEFORE ADDING`

`PRODUCT LOCK > SCENE STYLE`

`ACTOR OPERABILITY > PRODUCT HERO ANGLE`

只有全部适用项达到可接受状态才交付。
