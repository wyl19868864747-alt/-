# BENCHMARK V1｜4 Scene × 3 Real SKU 首轮诊断

> 目标：用最小测试集暴露最大结构问题。

本Benchmark验证真实生成表现，但**每个Case仍必须先是一条成立的剧情带货广告**。不能为了方便测试动作，把“开盒/拿起/佩戴/收纳”这种操作步骤冒充消费者购买理由。

---

# 1. 测试矩阵

使用3个真实SKU：
- `P1_3C`：用户提供的真实3C产品
- `P2_APPAREL`：用户提供的真实服装产品
- `P3_DAILY_GOODS`：用户提供的真实日用品

使用4个代表Scene：
- S01 宫廷
- S04 办公室
- S07 商场
- S12 豪华列车

Case ID：

| Case | Scene | Product |
|---|---|---|
| B1-S01-P1 | 宫廷 | 3C |
| B1-S01-P2 | 宫廷 | 服装 |
| B1-S01-P3 | 宫廷 | 日用品 |
| B1-S04-P1 | 办公室 | 3C |
| B1-S04-P2 | 办公室 | 服装 |
| B1-S04-P3 | 办公室 | 日用品 |
| B1-S07-P1 | 商场 | 3C |
| B1-S07-P2 | 商场 | 服装 |
| B1-S07-P3 | 商场 | 日用品 |
| B1-S12-P1 | 豪华列车 | 3C |
| B1-S12-P2 | 豪华列车 | 服装 |
| B1-S12-P3 | 豪华列车 | 日用品 |

---

# 2. 测试设计原则

## 2.1 同一SKU跨Scene保持完全相同的Product Truth
不能因为Scene视觉需要改变产品颜色、尺度、结构、包装、配件、真实功能。

## 2.2 Asset Mode必须登记
- `REFERENCE_ASSET`
- `TEXT_ONLY`
- `PARTIAL_REFERENCE`

TEXT_ONLY可测故事、动作、机位和模型默认理解，但不能作为Reference Product Lock验证通过证据。

## 2.3 Commercial Validity Gate｜先证明“这广告值得拍”
进入Story Architecture前必须回答：
1. Why Buy
2. Pain / Hesitation
3. Confirmed Product Advantage
4. Best Proof / Best Expression
5. Emotional Payoff

硬规则：
> **产品操作步骤 ≠ 自动等于商业卖点。**

如果只是测手部穿模、开盒、佩戴等能力，做`TECHNICAL DIAGNOSTIC CLIP`，不要伪装成剧情带货Benchmark。

## 2.4 每个Case只验证一个主要购买问题
每条只锁：
- 1 Core Decision Question
- 1 Top Pain / Hesitation
- 1 Confirmed Selling Point
- 1 Best Proof / Expression
- 1 Primary Architecture
- 1 R-level
- 1 Emotional Payoff

## 2.5 R0不等于平
前1–3秒至少建立一个：正在发生的事件 / 未完成任务 / 可见压力 / 冲突选择 / 异常状态。

`TENSION SOURCE ≠ PROTAGONIST NEGATIVITY`

普通商用广告中，压力优先来自环境、任务、时间、关系或问题；主角保持有能力、可喜欢、值得代入。

## 2.6 Scene必须真正触发DNA
S01礼仪/等级/权威；S04 Deadline/Client/Competence；S07 Discovery/Comparison/Demo/Choice；S12 Carriage order/Ownership/Attendant/Next-stop/Object movement。

## 2.7 每条必须包含真实Proof / Benefit Expression
若卖点属于声音/感官/长期/不可直接视觉证明，可用诚实的声音/行为代理表达，但不伪造精确测试。

## 2.8 Camera × Action Gate
所有开盒、开盖、取出、放回、佩戴、插拔、拆装等执行：

`人物操作方向 → 产品工作面 → 机位 → Proof可见性`

不能为了镜头看清而让人物从错误方向使用产品。

## 2.9 Action Tempo Gate
高能/利落广告中，拿起、抬手、单次佩戴、按一下、打开等简单动作通常约`0.5–1.2s`视觉节拍。

`蓄力高能感 = 预备 → 快速动作 → 清楚结果/切镜`

## 2.10 Audio Spatial Causality Gate
任何对白/画外音锁speaker位置、on/off-screen、距离、方向、相对音量/房间感。

人物佩戴耳机、隔门/玻璃、远距离时，必须解释为什么能听清，或不要让其直接听清。

## 2.11 Object State Ledger
耳机、鞋、手套、两件配件等逐Beat记账；任一状态改变必须有可见动作或明确动作匹配切。

**Hero Shot也必须服从Object State Ledger。**

## 2.12 Hook Temporal Stability Gate｜快不等于亚秒乱切
真实Attempt 4两次生成发现：0–3s连续多个0.7s左右的独立物理镜头，会提高Seedance在镜头间做插值/morph而不是真正Hard Cut的风险。

因此Hook优先：
- `一个强主镜头 + 同画面多个可见噪音源/事件 + 声音叠加`；
- 或最多少量清楚切镜，每个独立物理镜头尽量≥1.0–1.5s；
- 首镜人物互动时，关键人物可从首帧已经在可执行位置；
- 不在1秒内同时要求走门、靠近、说话、大物体移动、空间重置。

**快节奏优先靠感知信息密度，不靠不断重新生成空间。**

## 2.13 Post-Proof Continuation Check
如果Best Proof在总时长前40–50%已经完成，后面必须至少发生一个与同一Selling Point直接相关的新因果Beat。

Attempt 4新增硬教训：

> **“增加更多背景事件”不等于继续剧情。**

合法Continuation必须至少改变一项：
- 主角动作
- 主角判断/目标
- 产品状态
- 观众对Benefit的理解
- 商业关系/选择
- 情绪Payoff

纯背景掉文件、打印机继续响、路人走动只能作为短促Contrast证据，不能单独占用完整剧情段。

## 2.14 Commercial Beat Density Gate｜防电视剧化
短视频广告不是把一个场面自然演完整。

默认检查：
- 通常每`2–3秒`至少出现一个新商业Beat：新信息 / 新动作 / 新产品状态 / 新反差 / 新Reaction / 新Payoff；
- Beat指观众理解或期待发生变化，不是机械每2秒换景；
- 单一自然行为如打字、听、说、走路，如果连续约3秒却没有新商业信息，优先压缩；
- Surprise / Comedy若用于修Post-Proof Plateau，优先在Proof后`2–4秒`内出现；
- `Audio Calm ≠ Visual Slow`：产品让声音安静，不代表画面信息节奏也要放慢；
- 30秒没有足够高价值Beat时，缩短优于电视剧式填时长。

---

# 3. 推荐执行顺序

第一组 P1 3C：
1. B1-S04-P1
2. B1-S07-P1
3. B1-S12-P1
4. B1-S01-P1

第二组 P2服装：S07 → S12 → S01 → S04
第三组 P3日用品：S04 → S07 → S12 → S01

如果前面发现系统级问题，先修再继续，不为凑齐12条烧积分。

---

# 4. 每个Case固定输入卡

```text
CASE ID:

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

KEY CONTINUITY ANCHORS:

HOOK TEMPORAL PLAN:
- Primary visual:
- Secondary events/sounds:
- Shot reset count in first 3s:

CAMERA × ACTION PLAN:
- Key interaction:
- Actor operation side:
- Product working side:
- Camera side:
- Required cut:
- Action tempo:

OBJECT STATE LEDGER:
AUDIO SPATIAL PLAN:
POST-PROOF CONTINUATION:
COMMERCIAL BEAT MAP:
- 0–3s:
- 3–6s:
- 6–9s:
- 9–12s:
- 12–15s:
- 15–18s:
- 18–21s:
- 21–24s:
- 24–27s:
- 27–30s:

PRIMARY GENERATION RISK:
```

---

# 5. 每条视频固定评分表

```text
CASE ID:
GENERATION MODEL / VERSION:
ATTEMPT:
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

COMMERCIAL BEAT DENSITY CHECK:
- 是否存在>3s无新商业信息的自然主义段落？
- Proof后2–4s是否出现下一高价值Beat？
- 背景事件是否真的改变主角/产品/理解，而非装饰？
- 是否出现“电视剧式完整演场面”而非广告式压缩？

HOOK TEMPORAL STABILITY CHECK:
- 首3s是否因多亚秒物理镜头产生morph/假连续？
- 首镜空间是否可稳定执行？

PRIMARY FAILURE TYPE:
SKILL_RULE / PROMPT_COMPILER / MODEL_LIMIT / RANDOM_GENERATION / PRODUCT_ASSET_LIMIT / NONE

FAILURE PATTERN IDS:
GFxx...

NEXT ACTION:
KEEP / PROMPT_FIX / SKILL_FIX / COMMERCIAL_RESET / AD_PACING_RESET / SIMPLIFY / SPLIT_SHOT / CHANGE_CAMERA / CHANGE_SCENE / RERUN / STOP
```

---

# 6. 首轮停止条件

出现以下情况暂停当前产品剩余Case，先修：
- Core Decision / Selling Point不成立
- Product Lock连续2条FAIL
- 同一物理交互连续2条FAIL
- 同一Scene关键空间规则连续2条FAIL
- Commercial Clarity连续2条FAIL
- Story Engagement连续2条FAIL
- 同一Prompt Compiler缺陷跨2条复现
- 同一Prompt连续2次出现TV Drama Drift或Hook False Continuity

如果Commercial Validity失败：回商品决策。
如果商业清晰但观感电视剧化：执行`AD_PACING_RESET`，不是继续加更多剧情事件。

---

# 7. 首轮完成标准

- 12个Case有结果或明确NOT_SUITABLE/STOP
- 所有FAIL/PARTIAL有Failure Type
- 可复用失败进入Failure Pattern库
- Skill修改有真实Case证据
- Scene Validation Registry得到真实数据但不自动VALIDATED
