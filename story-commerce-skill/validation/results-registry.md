# BENCHMARK RESULTS REGISTRY｜真实生成结果登记

> 只记录真实生成结果。未生成不得填PASS。

当前阶段：`BENCHMARK V1｜DIAGNOSTIC`

评分：`PASS / PARTIAL / FAIL / N/A / NOT_RUN`

---

# 1. Summary

| Case | Scene | Product | Scene Recognition | Product Lock | Action | Space/Physics | Performance | Proof | Commercial Clarity | Story Engagement | Emotional Payoff | Audio Causality | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B1-S01-P1 | S01 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S01-P2 | S01 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S01-P3 | S01 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P1 | S04 | AirPods Pro 2 | PASS | PARTIAL* | PARTIAL | FAIL | PARTIAL | PARTIAL | FAIL | FAIL | FAIL | PASS | FAIL / STRUCTURE RESET |
| B1-S04-P2 | S04 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P3 | S04 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P1 | S07 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P2 | S07 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P3 | S07 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P1 | S12 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P2 | S12 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P3 | S12 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

`*` B1-S04-P1 Attempt 1–5均为 `TEXT_ONLY`；Product Lock只能做模型默认外观观察，不能作为Reference Asset Lock验证证据。

---

# 2. Case Records

## B1-S04-P1｜Attempt 1
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v1

SCENE_RECOGNITION: PARTIAL
PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
ACTION_EXECUTION: PARTIAL
SPATIAL_PHYSICAL_CONTINUITY: FAIL
PERFORMANCE_REACTION: PARTIAL
PROOF_FIDELITY: PARTIAL
COMMERCIAL_CLARITY: PARTIAL
STORY_ENGAGEMENT: FAIL

FAILURE PATTERNS: GF15 / GF16 / GF17
FINAL CASE STATUS: FAIL / RETEST

---

## B1-S04-P1｜Attempt 2
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v2

SCENE_RECOGNITION: PARTIAL
PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
ACTION_EXECUTION: PARTIAL
SPATIAL_PHYSICAL_CONTINUITY: FAIL
PERFORMANCE_REACTION: FAIL
PROOF_FIDELITY: FAIL
COMMERCIAL_CLARITY: FAIL
STORY_ENGAGEMENT: FAIL
EMOTIONAL_PAYOFF: FAIL
AUDIO_CAUSALITY: FAIL

FAILURE PATTERNS: GF15 / GF16 / GF17 / GF18 / GF19 / GF20 / GF21 / GF22
FINAL CASE STATUS: FAIL / COMMERCIAL RESET

---

## B1-S04-P1｜Attempt 3
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v3｜Commercial Reset｜ANC

COMMERCIAL FOCUS:
- Pain：开放办公室杂音干扰专注
- Selling Point：Active Noise Cancellation
- Architecture：SA01 Problem → Solution
- R-level：R0
- Emotional Payoff：混乱 → 专注 → 掌控

SCENE_RECOGNITION: PASS
PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
ACTION_EXECUTION: PASS
SPATIAL_PHYSICAL_CONTINUITY: FAIL
PERFORMANCE_REACTION: PASS
PROOF_FIDELITY: PASS
COMMERCIAL_CLARITY: PASS
STORY_ENGAGEMENT: PARTIAL
EMOTIONAL_PAYOFF: PASS
AUDIO_CAUSALITY: PASS

FAILURE PATTERNS:
GF15 MITIGATED / GF16 CONFIRMED / GF17 MITIGATED / GF18 MITIGATED / GF19 MITIGATED / GF20 MITIGATED / GF21 MITIGATED / GF22 CONFIRMED / GF23 CONFIRMED

FINAL CASE STATUS: PARTIAL / STORY RETEST

---

## B1-S04-P1｜Attempt 4｜Run A + Run B
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s × 2 generations
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v4｜R1 Surprise + Post-Proof Continuation

SCENE_RECOGNITION: PASS
PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
ACTION_EXECUTION: PARTIAL
SPATIAL_PHYSICAL_CONTINUITY: FAIL
PERFORMANCE_REACTION: PASS
PROOF_FIDELITY: PASS
COMMERCIAL_CLARITY: PASS
STORY_ENGAGEMENT: FAIL
EMOTIONAL_PAYOFF: PARTIAL
AUDIO_CAUSALITY: PASS

FAILURE PATTERNS:
GF22 / GF23 / GF24 / GF25

Evidence:
- 首3秒多个亚秒物理镜头被模型插值成False Hard Cut Morph；
- 10–21s背景事件增加但主角/产品/观众理解没有高价值变化，出现TV Drama Drift。

FINAL CASE STATUS: FAIL / AD PACING RESET

---

## B1-S04-P1｜Attempt 5
DATE: 2026-09-04
MODEL / VERSION: Seedance 2.5
DURATION: 30s
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v5｜Ad Density Reset

COMMERCIAL INTENT:
- Pain：开放办公室噪音干扰专注
- Intended Selling Point：Active Noise Cancellation
- Architecture：SA01 Problem → Solution
- Intended Emotional Payoff：噪音压力 → 戴耳机 → 专注掌控

### SCENE_RECOGNITION: PASS
现代开放办公室清楚可读。

### PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
纯文生下AirPods Pro 2大体可识别，但仍无Reference Asset，不能验证真正Product Lock。

### ACTION_EXECUTION: PARTIAL
拿起、打开、佩戴等大动作总体执行，但5–6s出现一台并非剧情所需的真实摄影机/三脚架，被模型从元机位描述字面生成进场景。

### SPATIAL_PHYSICAL_CONTINUITY: FAIL
1. 连续镜头机位先后落在女主左前、右前/右侧、左后/OTS等不同半区，没有中性镜头或可见过轴过程，形成明显180°越轴；
2. 约22s普通无动力办公手推车无人推动却自行滑过，违反动力来源；
3. 5–6s可见摄影器材进入画面，破坏场景真实性。

### PERFORMANCE_REACTION: PARTIAL
人物自然，但开场并没有把“噪音压力”真正演到人物身上。女主从第一秒就偏冷静、稳定，缺少可感知的困扰/目标受阻，因此没有形成强情绪感染。

### PROOF_FIDELITY: PARTIAL
Prompt意图是ANC，但成片只表现“戴耳机后继续工作”。前后声音/行为状态的差异不够强，产品作用没有形成不可错认的因果Proof。

### COMMERCIAL_CLARITY: FAIL
即使Prompt只锁ANC，观众仍很难仅靠成片明确回答“这条到底在卖什么”。说明`Selling Point存在于Prompt`不等于`Benefit被观众解码`。

### STORY_ENGAGEMENT: FAIL
开场虽然有助理+办公室噪音，但没有形成强可感知情绪或紧迫动作；中后段仍以人物办公状态展示为主，广告抓力不足。

### EMOTIONAL_PAYOFF: FAIL
“混乱→掌控”的预设情绪没有真正建立，因为开场人物几乎没有被噪音影响，后段自然也没有足够的释放/爽感。

### AUDIO_CAUSALITY: PASS
没有复现Attempt 2的远处对白/耳机听觉矛盾；主要问题是Benefit表达不够可感，而不是声音物理因果明显错误。

PRIMARY FAILURE TYPE:
SKILL_RULE + PROMPT_COMPILER + DURATION_FIT

FAILURE PATTERNS:
- GF26｜180° Axis Crossing / Camera Hemisphere Drift
- GF27｜Unmotivated Prop Motion / Missing Motive Force
- GF28｜Benefit Decodability Failure / Pain-to-Payoff Contrast弱
- GF29｜Duration-to-Story Misfit / 单卖点被强行拉30秒
- GF30｜Meta-camera Instruction Literalized as Prop

ROOT CAUSE:
1. Skill此前只有“机位侧/操作面”规则，没有正式180°主轴线与允许机位半区；
2. Prompt为了画面忙碌写“推车经过”，却没有明确“谁推/什么动力”；
3. Commercial Decision虽然锁了ANC，但没有强制检查观众能否通过成片清楚解码Benefit；
4. 开场只有噪音事件，没有先让噪音造成一个清楚、可见的任务阻力，因此情绪不感染；
5. 单一ANC利益在约8–12s就能表达完成，连续多次证明30s会诱发填时长、电视剧化、重复状态；
6. “摄影机和人物看向同一方向”等元语言被SD字面解释成场景摄影器材。

FIX:
- Camera×Action加入180° Axis Lock / Axis Ledger；
- 加入Motive Force Gate；普通推车必须有人推，自驱则明确机器人底盘；
- 加入Meta-Camera Guard，机位用“画面从…观察/OTS”表达，避免把摄影机写成动作主体；
- 新增Benefit Decodability Gate：产品前必须有可感知Problem Cost，产品后必须有立即可读State Change；
- 新增Duration Fit Gate：单一卖点在12–18s自然完成时，不为模型支持30s强行拉长；30s必须有第二个真实高价值商业Beat，否则缩短。

RETEST REQUIRED: YES
RETEST TARGET: B1-S04-P1 Attempt 6｜15s Benefit-Decoding + Axis-Lock Reset
FINAL CASE STATUS: FAIL / STRUCTURE RESET

---

# 3. Case记录模板

```text
## <CASE ID>｜Attempt <n>
DATE:
MODEL / VERSION:
DURATION:
ASSET MODE:
PROMPT REVISION:

SCENE_RECOGNITION:
PRODUCT_LOCK:
ACTION_EXECUTION:
SPATIAL_PHYSICAL_CONTINUITY:
PERFORMANCE_REACTION:
PROOF_FIDELITY:
COMMERCIAL_CLARITY:
STORY_ENGAGEMENT:
EMOTIONAL_PAYOFF:
AUDIO_CAUSALITY:

PRIMARY FAILURE TYPE:
FAILURE PATTERNS:
ROOT CAUSE:
FIX:
RETEST REQUIRED:
FINAL CASE STATUS:
```

---

# 4. 修改证据规则

- 商业信息写在Prompt里，不代表观众能从成片解码出来；必须以观众视角复核。
- 任何连续空间镜头必须审核180°轴线。
- 任何普通道具移动必须有可见/合理动力来源。
- 单卖点若在前半已经自然讲完，优先缩短，不用“继续工作/继续使用”填满30秒。

---

# 5. 当前状态

已运行：
- Attempt 1｜FAIL / RETEST
- Attempt 2｜FAIL / COMMERCIAL RESET
- Attempt 3｜PARTIAL / STORY RETEST
- Attempt 4 Run A+B｜FAIL / AD PACING RESET
- Attempt 5｜FAIL / STRUCTURE RESET

下一步：
- Attempt 6改为约15秒，锁单一180°机位半区，强化Pain→Benefit的可感知情绪/行为反差，不再继续强做30秒。

其他Case：`NOT_RUN`
