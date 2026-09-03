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
| B1-S04-P1 | S04 | AirPods Pro 2 | PASS | PARTIAL* | PARTIAL | FAIL | PASS | PASS | PASS | FAIL | PARTIAL | PASS | FAIL / AD PACING RESET |
| B1-S04-P2 | S04 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P3 | S04 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P1 | S07 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P2 | S07 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P3 | S07 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P1 | S12 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P2 | S12 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P3 | S12 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

`*` B1-S04-P1 Attempt 1–4均为 `TEXT_ONLY`；Product Lock只能做模型默认外观观察，不能作为Reference Asset Lock验证证据。

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

PRIMARY FAILURE TYPE: PROMPT_COMPILER
SECONDARY ROOT CAUSE: SKILL_RULE_GAP + BENCHMARK_DESIGN
FAILURE PATTERNS: GF15 / GF16 / GF17

FIX:
- 新增Camera×Action Compiler；
- 关键开盒改OTS；
- 精细动作拆分；
- Attempt 2强化Story Driver。

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

PRIMARY FAILURE TYPE: SKILL_RULE
SECONDARY ROOT CAUSE: BENCHMARK_DESIGN + PROMPT_COMPILER
FAILURE PATTERNS: GF15 / GF16 / GF17 / GF18 / GF19 / GF20 / GF21 / GF22

ROOT CAUSE:
Commercial Decision被技术测试目的取代；拿取/佩戴/收纳被误当成消费者购买理由。

FIX:
Commercial Validity Gate；Why Buy/Pain/Selling Point/Emotional Payoff前置；动作Tempo、声音因果、Object State Ledger。

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

Evidence:
- 0–10s“办公室噪音→戴AirPods→噪音减弱→进入专注”商业因果清楚；
- 主体操作没有明显穿模，动作节拍明显改善；
- 11–23s连续维持“已经专注”，出现Post-Proof Plateau；
- 27–30s女主耳朵仍有一对耳机，但打开盒内又生成一对，GF22复制问题。

FAILURE PATTERNS:
GF15 MITIGATED / GF16 CONFIRMED / GF17 MITIGATED / GF18 MITIGATED / GF19 MITIGATED / GF20 MITIGATED / GF21 MITIGATED / GF22 CONFIRMED / GF23 CONFIRMED

FIX:
- Post-Proof Continuation Check；
- Hero Shot服从Object State Ledger；
- Attempt 4只修中后段推进与Hero State。

FINAL CASE STATUS: PARTIAL / STORY RETEST

---

## B1-S04-P1｜Attempt 4｜Run A + Run B

DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s × 2 generations
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v4｜R1 Surprise + Post-Proof Continuation

COMMERCIAL FOCUS:
- Pain：开放办公室噪音干扰专注
- Selling Point：Active Noise Cancellation
- Architecture：SA01 Problem → Solution
- R-level：R1 Surprise
- Intended Payoff：噪音→ANC→专注→摘一只噪音回归→“Nope.”→重新戴回

### SCENE_RECOGNITION: PASS
Evidence:
两次生成都能清楚识别开放式美国办公室；打印机、办公设备、同事与桌面工作状态继续支持S04语境。

### PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
Evidence:
两次纯文生都保持白色AirPods Pro 2的大体识别；仍无Reference Asset输入，不能验证参考锁定。

### ACTION_EXECUTION: PARTIAL
Evidence:
拿起、开盒、佩戴、单只摘下、重新戴回的大动作总体被执行；后半单耳取下/戴回没有复现Attempt 2的明显耳机仓状态瞬移。但开场多微镜头和助理进入没有稳定按“独立硬切镜头”执行。

### SPATIAL_PHYSICAL_CONTINUITY: FAIL
Evidence:
Run B在约0.5–1.1s尤其明显：打印机/办公设备/移动物体被模型做成连续横向模糊与空间插值，而不是提示词要求的独立硬切，产生“物体穿过画面/镜头”的穿模感。Run A较轻，但0–3s仍存在微镜头之间空间重置过快、助理几乎直接出现在女主身后的跳跃感。两次同Prompt都说明首3秒微镜头负载过高。

### PERFORMANCE_REACTION: PASS
Evidence:
女主整体仍保持专业、积极，没有退回“不耐烦主角”；单耳摘下后的短促反应和重新戴回基本可读。

### PROOF_FIDELITY: PASS
Evidence:
ANC作为唯一卖点仍然清楚；戴上后环境声/工作状态变化，以及后段单耳摘下再重新戴回，继续围绕同一利益，没有换卖点。

### COMMERCIAL_CLARITY: PASS
Evidence:
两版仍然能理解“办公室噪音→AirPods Pro 2主动降噪→恢复专注”。商业决策没有回退。

### STORY_ENGAGEMENT: FAIL
Evidence:
虽然Attempt 4增加了掉文件、打印机再次提示、通话、会议结束、摘耳机、Nope等事件，但从约10s到21s两次生成都长时间停留在女主同一中近景中打字/说话，事件多数发生在背景且没有改变女主的即时目标或动作。观感从短视频广告变成自然主义办公室电视剧覆盖，广告的即时抓力反而弱于Attempt 3。

### EMOTIONAL_PAYOFF: PARTIAL
Evidence:
“Nope→重新戴回”的轻Surprise/Comedy方向成立，但发生得太晚（约23–27s），此前十多秒已经掉出广告节奏，Payoff无法挽回中段流失。

### AUDIO_CAUSALITY: PASS
Evidence:
没有复现Attempt 2的远处助理贴脸对白/戴耳机仍直接回应问题；主要声音逻辑仍围绕ANC主观听觉变化。

PRIMARY FAILURE TYPE:
PROMPT_COMPILER / AD_PACING

SECONDARY ROOT CAUSE:
HOOK_MICRO_SHOT_OVERLOAD + STORY_CONTINUATION_OVERCORRECTION

FAILURE PATTERNS:
- GF22｜本版未复现结尾复制，但仍需跨Case复测后才能MITIGATED
- GF23｜仍CONFIRMED：Attempt 4证明“增加更多背景事件”本身不能解决Post-Proof Plateau
- GF24｜新增：Sub-second Micro-shot Interpolation / False Continuity
- GF25｜新增：Commercial Beat Density Collapse / TV Drama Drift

ROOT CAUSE:
1. 把“短视频节奏快”错误翻译成0–3s连续多个0.7s左右独立物理镜头；SD2.5有时不会真正硬切，而会在不同空间/物体间插值，产生穿模感；
2. 为修GF23，加入太多完整的自然主义办公室事件，但这些事件多数只是背景发生，没有直接改变主角行动、产品状态或商业判断；
3. “ANC后镜头稳定”被过度执行成10秒以上同类中近景，声音安静被错误映射成视觉也要安静；
4. R1 Surprise本身方向没错，但被安排到约21s以后，广告最有趣的第二次声音反差来得过晚；
5. 30秒被按电视剧式“铺事件→演完整→再下一个事件”填满，而不是广告式高密度商业Beat压缩。

FIX:
- Hook改用`一个强主镜头 + 多声音/背景事件同时发生`，不再用3个亚秒级独立物理镜头硬拼；
- 关键首镜人物/助理若需要互动，人物从首帧即处于可执行位置，避免1秒内再走门、靠近、说长句；
- 新增Commercial Beat Density Gate：通常每2–3秒必须出现新信息、新动作、新产品状态、新反差或Payoff；
- `Audio Calm ≠ Visual Slow`：ANC后的声音可以安静，镜头/信息节奏仍可快速；
- Post-Proof新事件必须直接改变主角动作、判断、产品状态或观众对Benefit的理解；纯背景掉文件/路人忙碌不能独占长Beat；
- R1 Surprise提前到Proof后2–4秒内，而不是拖到20秒以后；
- 30秒若没有足够高价值商业Beat，宁可缩短，不用电视剧式场面填时长。

RETEST REQUIRED: YES
RETEST TARGET: B1-S04-P1 Attempt 5｜Ad Density Reset
FINAL CASE STATUS: FAIL / AD PACING RESET

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

如果商业问题、Proof和情绪成立，但观感变成电视剧：
> 检查Commercial Beat Density、镜头信息变化与Post-Proof事件是否真正改变人物/产品/判断。不要用更多自然主义场面填时长。

---

# 5. 当前状态

已运行：
- B1-S04-P1 Attempt 1｜FAIL / RETEST
- B1-S04-P1 Attempt 2｜FAIL / COMMERCIAL RESET
- B1-S04-P1 Attempt 3｜PARTIAL / STORY RETEST
- B1-S04-P1 Attempt 4 Run A + B｜FAIL / AD PACING RESET

下一步：
- B1-S04-P1 Attempt 5｜保留已验证的ANC商业决策，但重做Hook镜头策略与整条Commercial Beat Density；不再用多个亚秒物理镜头制造“快”，不再用完整电视剧式办公室事件填满中段。

其他Case：`NOT_RUN`
