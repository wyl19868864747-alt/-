# BENCHMARK V1｜4 Scene × 3 Real SKU 首轮诊断

> 目标：用最小测试集暴露最大结构问题。

本Benchmark验证真实生成表现，但**每个Case仍必须先是一条成立的剧情带货广告**。

---

# 1. 测试矩阵

3个真实SKU：3C / Apparel / Daily Goods。
4个代表Scene：S01宫廷 / S04办公室 / S07商场 / S12豪华列车。

Case：
- B1-S01-P1 / P2 / P3
- B1-S04-P1 / P2 / P3
- B1-S07-P1 / P2 / P3
- B1-S12-P1 / P2 / P3

---

# 2. 测试设计原则

## 2.1 Product Truth恒定
同一SKU跨Scene不得改变颜色、尺度、结构、包装、配件、真实功能。

## 2.2 Asset Mode
- REFERENCE_ASSET
- TEXT_ONLY
- PARTIAL_REFERENCE

TEXT_ONLY可测故事、动作、机位、模型默认理解，但不能作为Reference Product Lock PASS证据。

## 2.3 Commercial Validity Gate
Story Architecture之前必须回答：
1. Why Buy
2. Pain / Hesitation
3. Confirmed Product Advantage
4. Best Proof / Expression
5. Emotional Payoff

产品操作步骤不能自动冒充商业卖点。

## 2.4 单条只锁1个主要购买问题
只锁：
- 1 Core Decision Question
- 1 Top Pain / Hesitation
- 1 Confirmed Selling Point
- 1 Best Proof / Expression
- 1 Primary Architecture
- 1 R-level
- 1 Emotional Payoff

## 2.5 R0不等于平
前1–3秒至少建立事件/任务/压力/选择/异常之一。

`TENSION SOURCE ≠ PROTAGONIST NEGATIVITY`

## 2.6 Scene必须触发DNA
S01礼仪/等级/权威；S04 Deadline/Client/Competence；S07 Discovery/Comparison/Demo/Choice；S12 Carriage order/Ownership/Attendant/Next-stop/Object movement。

## 2.7 必须包含真实Proof / Benefit Expression
声音/感官类可用诚实声音/行为代理表达，但不伪造精确测试。

## 2.8 Camera × Action Gate
关键操作执行：
`人物操作方向 → 产品工作面 → 机位 → Proof可见性`

## 2.9 Action Tempo Gate
简单动作通常约0.5–1.2s视觉节拍。

## 2.10 Audio Spatial Causality Gate
对白/画外音锁speaker位置、距离、方向、相对音量/空间感。

## 2.11 Object State Ledger
成对/多件商品逐Beat记账；Hero Shot同样服从Ledger。

## 2.12 Hook Temporal Stability Gate
快节奏优先靠信息密度，不靠多个<1s独立物理空间重置。

优先：
- 一个强主镜头 + 多可见事件/声音层；
- 或少量稳定切镜，每个独立物理镜头尽量≥1.0–1.5s。

## 2.13 Post-Proof Continuation Check
Proof前40–50%完成时，后续必须有同Selling Point的新因果Beat；纯背景事件不算推进。

## 2.14 Commercial Beat Density Gate
通常每2–3秒至少出现一个新商业Beat：新信息 / 新动作 / 新产品状态 / 新反差 / 新Reaction / 新Payoff。

`Audio Calm ≠ Visual Slow`

30秒没有足够高价值Beat时，缩短优于电视剧式填时长。

## 2.15 180° Axis Continuity Gate
Attempt 5真实越轴后升级为硬检查。

每个连续空间先锁：
```text
PRIMARY AXIS:
ALLOWED CAMERA HALF:
SCREEN DIRECTION:
```

连续镜头只能在同一180°半区内变化。

合法跨轴仅允许：
- 可见移动穿轴；
- 中性轴线镜头；
- 画内明确建立新轴线。

不得为了“多角度”从左前→右前→左后随机跳机位。

## 2.16 Motive Force Gate
任何显著移动物体必须回答：
> **谁让它动？**

普通推车：必须有人推/拉。
自驱设备：必须明确电动底盘/机器人身份。
门、椅子、杯子、箱子等不能无原因自行运动。

## 2.17 Benefit Decodability Gate｜Prompt写对卖点还不够
写作完成后必须从观众视角检查：

1. Product Before前是否有明确Problem Cost？
2. Product介入是否直接解决这个Problem？
3. Product After是否出现立即可读State Change？
4. 不看结尾旁白，观众能否回答“这个产品刚刚帮了什么忙”？
5. 情绪Payoff是否来自Problem被解决？

若观众仍说不清卖点：Commercial Clarity FAIL，哪怕Prompt里明确写了Selling Point。

## 2.18 Duration Fit Gate｜时长由故事决定，不由模型上限决定
时长根据：
`Core Decision + Proof数量 + Architecture复杂度 + R-level + 高价值Beat数量`
决定。

默认：
- 单一强Proof + SA01/SA02 + R0/R1，若12–18s已自然完成，优先短版；
- 30s必须有第二个真实高价值商业Beat/Proof/关系变化；
- 不允许用继续工作、继续使用、背景走动把短故事拉成30s。

Benchmark允许改变时长来验证“正确广告结构”，只需登记DURATION。

## 2.19 Meta-Camera Guard
机位是元指令，不是场景道具。

推荐：
- `人物右肩后方OTS近景`
- `画面从同侧观察产品工作面`

避免：
- `摄影机站在人物面前`
- `摄影机和人物看向同一方向`

非拍摄剧情默认：`no visible filming equipment in scene`。

---

# 3. 推荐执行顺序

P1 3C：S04 → S07 → S12 → S01
P2 Apparel：S07 → S12 → S01 → S04
P3 Daily Goods：S04 → S07 → S12 → S01

发现系统级问题先修，不为凑齐12条烧积分。

---

# 4. 每个Case固定输入卡

```text
CASE ID:
DURATION:

PRODUCT TRUTH:
- SKU:
- Asset Mode:
- Reference Assets:
- Size / Material / Structure / Accessories:
- Confirmed Claims:
- Forbidden / Unknown Claims:

WHY BUY:
TOP PAIN / HESITATION:
CONFIRMED SELLING POINT:
CORE DECISION QUESTION:
EMOTIONAL PAYOFF:

PRIMARY ARCHITECTURE:
BEST PROOF / BENEFIT EXPRESSION:
R-LEVEL:

TARGET SCENE:
DNA ACTIVATION:
PRODUCT ENTRY:

BENEFIT DECODABILITY:
- Problem Cost before product:
- Product causal turn:
- Immediate state change after product:
- Can viewer identify benefit without final VO?:

DURATION FIT:
- Natural completion time:
- Why this duration is justified:
- Second high-value beat if >20s:

PRIMARY AXIS:
ALLOWED CAMERA HALF:
SCREEN DIRECTION:

HOOK TEMPORAL PLAN:
- Primary visual:
- Secondary events/sounds:
- Shot reset count first 3s:

CAMERA × ACTION PLAN:
- Key interaction:
- Actor operation side:
- Product working side:
- Camera side:
- Required cut:
- Action tempo:

MOVING PROP FORCE PLAN:
OBJECT STATE LEDGER:
AUDIO SPATIAL PLAN:
POST-PROOF CONTINUATION:
COMMERCIAL BEAT MAP:
META-CAMERA WORDING CHECK:

PRIMARY GENERATION RISK:
```

---

# 5. 每条视频固定评分表

```text
CASE ID:
GENERATION MODEL / VERSION:
ATTEMPT:
DURATION:
ASSET MODE:

1. SCENE_RECOGNITION: PASS / PARTIAL / FAIL
2. PRODUCT_LOCK: PASS / PARTIAL / FAIL / N/A
3. ACTION_EXECUTION: PASS / PARTIAL / FAIL
4. SPATIAL_PHYSICAL_CONTINUITY: PASS / PARTIAL / FAIL
5. PERFORMANCE_REACTION: PASS / PARTIAL / FAIL
6. PROOF_FIDELITY: PASS / PARTIAL / FAIL
7. COMMERCIAL_CLARITY: PASS / PARTIAL / FAIL
8. STORY_ENGAGEMENT: PASS / PARTIAL / FAIL
9. EMOTIONAL_PAYOFF: PASS / PARTIAL / FAIL
10. AUDIO_CAUSALITY: PASS / PARTIAL / FAIL / N/A

BENEFIT DECODABILITY CHECK:
- Problem Cost清楚吗？
- 产品因果转折清楚吗？
- After状态变化清楚吗？
- 不靠结尾VO能说出卖点吗？

AXIS CHECK:
- 主轴是否稳定？
- 是否出现无合法过渡越轴？

MOTIVE FORCE CHECK:
- 所有移动道具都有动力来源吗？

DURATION FIT CHECK:
- 是否为了时长加入填充？
- 当前故事是否应该更短？

META-CAMERA CHECK:
- 是否把机位元语言生成成真实摄影器材？

PRIMARY FAILURE TYPE:
FAILURE PATTERN IDS:
NEXT ACTION:
KEEP / PROMPT_FIX / SKILL_FIX / COMMERCIAL_RESET / AD_PACING_RESET / DURATION_RESET / AXIS_RESET / RERUN / STOP
```

---

# 6. 首轮停止条件

出现以下情况暂停当前产品剩余Case：
- Core Decision / Selling Point不成立
- Benefit连续无法被观众解码
- Product Lock连续2条FAIL
- 同一物理交互连续2条FAIL
- 无合法过渡的明显越轴
- 普通道具无动力自行移动
- Commercial Clarity连续2条FAIL
- Story Engagement连续2条FAIL
- 同一Prompt Compiler缺陷重复复现
- 30s多次依赖填充才能成立

如果商业逻辑正确但自然完成时间明显短于设定时长：执行`DURATION_RESET`，不继续加剧情填空。

---

# 7. 首轮完成标准

- 12个Case有结果或明确NOT_SUITABLE/STOP
- 所有FAIL/PARTIAL有Failure Type
- 可复用失败进入Failure Pattern库
- Skill修改有真实Case证据
- Scene Validation Registry得到真实数据但不自动VALIDATED
