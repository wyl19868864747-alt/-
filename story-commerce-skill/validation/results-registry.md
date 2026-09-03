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
| B1-S04-P1 | S04 | AirPods Pro 2 | PASS | PARTIAL* | PASS | FAIL | PASS | PASS | PASS | PARTIAL | PASS | PASS | PARTIAL / STORY RETEST |
| B1-S04-P2 | S04 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P3 | S04 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P1 | S07 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P2 | S07 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P3 | S07 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P1 | S12 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P2 | S12 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P3 | S12 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

`*` B1-S04-P1 Attempt 1–3均为 `TEXT_ONLY`；Product Lock观察只能说明模型默认生成大体可识别，不能作为Reference Asset Lock验证证据。

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
- 办公室视觉成立，但Deadline / Client / Professional Pressure没有真正发动。

PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
- 产品大体可识别，但纯文生不能验证Reference Lock。

ACTION_EXECUTION: PARTIAL
- 大动作顺序基本生成；开盒/取出/放回存在方向/接触错误。

SPATIAL_PHYSICAL_CONTINUITY: FAIL
- 盒内朝镜头而背离人物；取出/放回穿模。

PERFORMANCE_REACTION: PARTIAL
- 克制，但状态变化弱。

PROOF_FIDELITY: PARTIAL
- 使用流程可见，但物理错误破坏Proof。

COMMERCIAL_CLARITY: PARTIAL
- 像办公室使用展示，产品为何必须介入表达弱。

STORY_ENGAGEMENT: FAIL
- 整体太平。

PRIMARY FAILURE TYPE: PROMPT_COMPILER
SECONDARY ROOT CAUSE: SKILL_RULE_GAP + BENCHMARK_DESIGN
FAILURE PATTERNS: GF15 / GF16 / GF17

FIX:
- 新增Camera×Action Compiler；
- Attempt 2强化机位、拆精细动作、增加Deadline与轻职场喜剧。

RETEST REQUIRED: YES
FINAL CASE STATUS: FAIL / RETEST

---

## B1-S04-P1｜Attempt 2

DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
ASSETS: 未实际传入产品参考图
PROMPT REVISION: B1-v2

SCENE_RECOGNITION: PARTIAL
- 办公室视觉清楚，但Client提前没有与产品核心利益绑定。

PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
- AirPods Pro 2大体可识别；纯文生不能验证Reference Lock。

ACTION_EXECUTION: PARTIAL
- 开盒操作方向改善，但佩戴动作过慢；收纳仍有错误。

SPATIAL_PHYSICAL_CONTINUITY: FAIL
- 25–26s出现Hidden State Teleport / 收纳穿模。

PERFORMANCE_REACTION: FAIL
- 主角被演成不耐烦；19–20s侧眼+笑意语义不清。

PROOF_FIDELITY: FAIL
- 展示很多操作，但没有证明一个核心购买利益。

COMMERCIAL_CLARITY: FAIL
- 无法判断究竟在卖降噪、续航、音质、通话、颜值还是便携。

STORY_ENGAGEMENT: FAIL
- Hook弱，中段平铺产品操作。

EMOTIONAL_PAYOFF: FAIL
- 没有清楚情绪弧。

AUDIO_CAUSALITY: FAIL
- 远处助理声音缺距离感；主角戴着耳机仍直接听清并回应。

PRIMARY FAILURE TYPE: SKILL_RULE
SECONDARY ROOT CAUSE: BENCHMARK_DESIGN + PROMPT_COMPILER
FAILURE PATTERNS: GF15 / GF16 / GF17 / GF18 / GF19 / GF20 / GF21 / GF22

FIX:
- Commercial Validity Gate；
- Why Buy / Pain / Selling Point / Emotional Payoff前置；
- Tension Source ≠ Protagonist Negativity；
- Action Tempo / Audio Spatial Causality / Object State Ledger；
- Attempt 3执行COMMERCIAL RESET。

RETEST REQUIRED: YES
FINAL CASE STATUS: FAIL / COMMERCIAL RESET

---

## B1-S04-P1｜Attempt 3

DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
ASSETS: 未实际传入产品参考图
PROMPT REVISION: B1-v3｜Commercial Reset｜ANC

COMMERCIAL FOCUS:
- Pain：开放办公室杂音干扰专注
- Selling Point：Active Noise Cancellation
- Architecture：SA01 Problem → Solution
- R-level：R0
- Emotional Payoff：混乱 → 专注 → 掌控

### SCENE_RECOGNITION: PASS
Evidence:
打印机、办公推车、开放工位、玻璃会议区、助理通知客户提前等共同建立真实现代办公室；办公室噪音与工作任务直接成为产品使用原因，S04不再只是背景皮肤。

### PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
Evidence:
纯文生下白色AirPods Pro 2外观、短柄耳机、充电盒大体可识别；本次仍无Reference Asset输入，因此不能把Reference Product Lock标PASS。结尾Hero Shot还出现耳机状态复制问题。

### ACTION_EXECUTION: PASS
Evidence:
拿起、开盒、快速佩戴的动作节拍明显优于Attempt 2；约7–8.5s佩戴快速，没有明显老年感；未观察到此前手指与耳机明显穿插。

### SPATIAL_PHYSICAL_CONTINUITY: FAIL
Evidence:
主体操作过程没有明显穿模，这是显著进步；但27–30s结尾出现新的状态冲突：女主仍明显佩戴耳机，而前景打开的充电盒又出现两只耳机，等于同一对耳机同时存在于耳朵和盒内。属于GF22的“复制版”而非传统穿模。

### PERFORMANCE_REACTION: PASS
Evidence:
女主面对客户提前和噪音压力保持高效、平稳，没有Attempt 2的不耐烦；戴上耳机后状态从外部干扰转为集中，结尾轻满意笑意也与情绪弧一致。

### PROOF_FIDELITY: PASS
Evidence:
本次终于只表达一个核心利益。约8.5–10s佩戴完成后，前景办公室噪音明显被压低为更远、更柔和的环境层，画面仍保留真实办公室活动，没有制造完全真空式静音；作为已确认ANC功能的广告化Benefit Expression成立。

### COMMERCIAL_CLARITY: PASS
Evidence:
即使不看脚本，也能理解“办公室太吵 → 戴AirPods Pro 2 → 环境干扰减弱 → 更专注”，核心卖点比前两版清楚很多。

### STORY_ENGAGEMENT: PARTIAL
Evidence:
0–10s明显变好：噪音Hook、客户提前、快速拿取/佩戴、声音世界切换形成完整推进。但核心Proof在约8.5–10s已经完成，11–23s主要是打字、记录、通话、背景助理视觉手势，连续处于同一个“已经专注”的状态，没有新的期待、阻力、关系变化、笑点或小Surprise，因此中段仍有明显平台期/出戏感。

### EMOTIONAL_PAYOFF: PASS
Evidence:
“办公室混乱 → 声音收束 → 专注掌控 → 轻满意”的情绪方向已经清楚，明显优于Attempt 2。

### AUDIO_CAUSALITY: PASS
Evidence:
ANC前后环境声层级有可感知差异；佩戴耳机后不再安排远处助理直接讲话，助理改用玻璃后的视觉手势，前版“戴耳机还能清楚听远处讲话”的物理矛盾没有复现。

PRIMARY FAILURE TYPE:
PROMPT_COMPILER / STORY_PACING

SECONDARY ROOT CAUSE:
CONTINUITY_STATE_GAP at Hero Shot

FAILURE PATTERNS:
- GF15｜持续MITIGATED
- GF16｜本版没有明显穿模，但未专门复测槽位精细放回，仍CONFIRMED
- GF17｜Hook/Driver问题MITIGATED
- GF18｜Commercial Focus问题MITIGATED
- GF19｜主角负面人格问题MITIGATED
- GF20｜动作慢问题MITIGATED
- GF21｜Audio Causality问题MITIGATED
- GF22｜仍CONFIRMED，结尾出现成对物体复制
- GF23｜新增：Post-Proof Plateau

ROOT CAUSE:
1. 这版商业决策已经正确，真正剩下的主要问题变成**30秒结构长度与Proof出现时机不匹配**；
2. 卖点约10秒已证明，后面没有新的因果Beat，只是维持“专注工作”；
3. R0本身不是问题，问题是`Proof → 后果/变化 → Emotional Payoff`中间缺了第二个有意义事件；
4. 结尾为了做经典Hero Shot，模型自动把两只耳机补回打开的盒内，违背前面“女主仍佩戴两只”的Object State Ledger。

FIX:
- Benchmark新增Post-Proof Continuation Check；
- 20–30s广告若Proof在前40–50%完成，后续必须出现与同一卖点直接相关的新因果Beat，否则缩短时长；
- 不强制R2，可用R0后果推进、轻Comedy或R1 Surprise；
- Hero Shot必须服从Object State Ledger；人物仍佩戴耳机时，结尾优先用闭合盒体或明确空槽，不生成“盒内完整两只耳机”的标准商品图。

RETEST REQUIRED: YES
RETEST TARGET: B1-S04-P1 Attempt 4｜Post-Proof Continuation
FINAL CASE STATUS: PARTIAL / STORY RETEST

---

# 3. Case记录模板

```text
## <CASE ID>｜Attempt <n>
DATE:
MODEL / VERSION:
DURATION:
ASSET MODE:
ASSETS:
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
SKILL_RULE / PROMPT_COMPILER / MODEL_LIMIT / RANDOM_GENERATION / PRODUCT_ASSET_LIMIT / NONE
FAILURE PATTERNS:
ROOT CAUSE:
FIX:
RETEST REQUIRED:
FINAL CASE STATUS:
```

---

# 4. 修改证据规则

没有真实Case证据，不继续膨胀核心Skill。

如果失败发生在Commercial Decision层：
> 停止镜头级补丁，回到商品决策重新设计。

如果商业问题、Proof与情绪已经成立但中段变平：
> 先检查Proof是否过早完成，再判断应增加后果Beat、轻Surprise/Comedy，还是直接缩短时长；不要条件反射升级R2。

---

# 5. 当前状态

Benchmark V1已开始真实生成。

已运行：
- B1-S04-P1 Attempt 1｜FAIL / RETEST
- B1-S04-P1 Attempt 2｜FAIL / COMMERCIAL RESET
- B1-S04-P1 Attempt 3｜PARTIAL / STORY RETEST

下一步：
- B1-S04-P1 Attempt 4｜只修Post-Proof Continuation + Hero State，不重做已经验证有效的Commercial Decision / ANC表达 / Camera×Action主链。

其他Case：`NOT_RUN`
