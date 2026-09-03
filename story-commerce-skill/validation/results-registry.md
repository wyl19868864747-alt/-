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
| B1-S04-P1 | S04 | AirPods Pro 2 | PARTIAL | PARTIAL* | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL / COMMERCIAL RESET |
| B1-S04-P2 | S04 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P3 | S04 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P1 | S07 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P2 | S07 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P3 | S07 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P1 | S12 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P2 | S12 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P3 | S12 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

`*` B1-S04-P1 Attempt 1/2均为 `TEXT_ONLY`；Product Lock观察只能说明模型默认生成大体可识别，不能作为Reference Asset Lock验证证据。

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

### SCENE_RECOGNITION: PARTIAL
Evidence:
现代企业办公室视觉清楚，助理/女上司/电脑/玻璃办公区关系可读；但S04更多仍是Location。所谓Client提前并没有真正形成与产品核心利益绑定的商业事件。

### PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
Evidence:
AirPods Pro 2外形、白色盒体、两只短柄耳机大体可识别；仍为TEXT_ONLY，不能验证Reference Asset Lock。

### ACTION_EXECUTION: PARTIAL
Evidence:
Attempt 1的开盒操作方向明显改善，OTS机位让人物和镜头能从同一工作面看到盒内；但约11–14s的佩戴动作明显过慢，失去年轻利落的节拍。25–26s收纳阶段又出现状态/精细交互错误。

### SPATIAL_PHYSICAL_CONTINUITY: FAIL
Evidence:
约25s仍能看到两只耳机处于佩戴/手持连续状态，26s近景中另一只耳机已经无可见动作地出现在充电仓，属于Hidden State Teleport；收纳接触仍有穿模/状态不连续。

### PERFORMANCE_REACTION: FAIL
Evidence:
开场助理提醒后，主角呈现不耐烦/嫌烦式情绪，压力被错误地写成主角负面人格；19–20s主角侧眼+笑意的状态语义不清，既不像专注工作，也没有清楚笑点/关系变化。全片缺乏明确情绪弧。

### PROOF_FIDELITY: FAIL
Evidence:
视频展示了开盒、佩戴、使用、收纳，但这些只是产品操作，不等于消费者为什么买AirPods Pro 2。没有清楚证明或表达一个核心购买利益。

### COMMERCIAL_CLARITY: FAIL
Evidence:
仅看成片无法判断核心卖点究竟是降噪、续航、音质、通话、颜值、便携还是其他。产品出现很多，但商业信息为零散操作。

### STORY_ENGAGEMENT: FAIL
Evidence:
开场Hook仍弱；“助理跑来提醒客户提前”没有带来足够视觉吸引力，也没有与产品优势形成强因果。中段进入拿起→戴上→工作→摘下→放回的平铺流程。

### EMOTIONAL_PAYOFF: FAIL
Evidence:
没有形成明确的“混乱→掌控”“焦虑→安心”“被打扰→专注”“惊讶→爽”等情绪变化。人物动作很多，但观众没有被带到一个清楚的情绪终点。

### AUDIO_CAUSALITY: FAIL
Evidence:
23–24s助理处于画外/较远位置，声音虽然整体音量并非最高，但缺少明确距离、方向和房间空间感，主观上仍像贴近镜头录制；同时主角仍处于佩戴耳机状态，却能直接清楚回应外部讲话，没有建立合理听觉条件。

PRIMARY FAILURE TYPE: SKILL_RULE
SECONDARY ROOT CAUSE: BENCHMARK_DESIGN + PROMPT_COMPILER

FAILURE PATTERNS:
- GF15｜Attempt 2目标问题已解决，转MITIGATED
- GF16｜小物体精细取放穿模继续存在
- GF17｜Story Driver仍未产生吸引力
- GF18｜伪商业问题：把易生成操作步骤当卖点
- GF19｜外部压力被写成主角负面人格
- GF20｜简单微动作时间预算过长
- GF21｜空间声音与听觉因果不成立
- GF22｜成对物体状态瞬移

ROOT CAUSE:
1. **最严重：Commercial Decision被Benchmark测试目的取代。** 为了测试开盒/佩戴/收纳，选择了并非AirPods Pro 2核心Why Buy的“快速取用/收纳”作为故事中心；
2. Prompt虽然强化了Deadline，却没有先确定一个真实产品卖点和用户痛点，因此Story Architecture没有商业目标可服务；
3. 普通商用广告中把紧张写成女主“不耐烦”，损害人物代入感；
4. 11–14s给简单佩戴动作过多时间，模型自然慢慢演满；
5. 19–20s“余光+干幽默”是抽象关系表演，没有清楚动作语义，模型生成含混的侧眼/笑意；
6. 23–24s没有写Speaker Distance / Direction / Hearing Plausibility；
7. 25–26s没有逐只追踪左右耳机状态。

FIX:
- Benchmark加入Commercial Validity Gate；
- 每条先锁Why Buy / Pain-Hesitation / Confirmed Selling Point / Emotional Payoff；
- 区分`STORY-COMMERCE BENCHMARK`和`TECHNICAL DIAGNOSTIC CLIP`；
- 加入Tension Source ≠ Protagonist Negativity；
- 加入Action Tempo Gate；
- 加入Audio Spatial Causality Gate；
- 加入Object State Ledger；
- Attempt 3不再沿Attempt 2补镜头，执行`COMMERCIAL RESET`。

RETEST REQUIRED: YES
RETEST TARGET: B1-S04-P1 Attempt 3｜Commercial Reset
FINAL CASE STATUS: FAIL / COMMERCIAL RESET

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

> **停止镜头级补丁，回到商品决策重新设计。**

---

# 5. 当前状态

Benchmark V1已开始真实生成。

已运行：
- B1-S04-P1 Attempt 1｜FAIL / RETEST
- B1-S04-P1 Attempt 2｜FAIL / COMMERCIAL RESET

下一步：
- B1-S04-P1 Attempt 3｜必须从真实消费者购买问题重新设计，而不是继续修第二版剧情。

其他Case：`NOT_RUN`
