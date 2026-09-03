# BENCHMARK RESULTS REGISTRY｜真实生成结果登记

> 只记录真实生成结果。未生成不得填PASS。

当前阶段：`BENCHMARK V1｜DIAGNOSTIC`

评分：`PASS / PARTIAL / FAIL / N/A / NOT_RUN`

---

# 1. Summary

| Case | Scene | Product | Scene Recognition | Product Lock | Action | Space/Physics | Performance | Proof | Commercial Clarity | Story Engagement | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B1-S01-P1 | S01 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S01-P2 | S01 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S01-P3 | S01 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P1 | S04 | AirPods Pro 2 | PARTIAL | PARTIAL* | PARTIAL | FAIL | PARTIAL | PARTIAL | PARTIAL | FAIL | FAIL / RETEST |
| B1-S04-P2 | S04 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P3 | S04 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P1 | S07 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P2 | S07 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P3 | S07 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P1 | S12 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P2 | S12 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P3 | S12 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

`*` B1-S04-P1 Attempt 1 为 `TEXT_ONLY`，没有把用户提供的产品参考图送入Seedance，因此Product Lock只能记录观察结果，**不能作为Reference Asset Lock验证通过的证据**。

---

# 2. Case Records

## B1-S04-P1｜Attempt 1

DATE:
2026-09-03

MODEL / VERSION:
Seedance 2.5

DURATION:
30s

PRODUCT:
Apple AirPods Pro 2｜White

ASSET MODE:
TEXT_ONLY

ASSETS:
用户此前提供了产品图片，但本次实际生成未传参考图；Seedance仅依据文字产品名/外观描述生成。

PROMPT REVISION:
B1-v1

### SCENE_RECOGNITION: PARTIAL
Evidence:
现代企业办公室的视觉环境清楚，人物在办公桌前工作；但S04真正的Deadline / Client / Professional Pressure没有形成足够可见的因果事件，办公室更接近Location而不是完全发动的Office DNA。

### PRODUCT_LOCK: PARTIAL
Evidence:
白色AirPods Pro 2样式、充电盒和两只短柄入耳式耳机大体可识别，尺度总体接近掌心小物；但本次为纯文生，不能验证参考资产锁定能力，精细内部结构与手部接触时也存在失真。

### ACTION_EXECUTION: PARTIAL
Evidence:
拿盒→开盒→取耳机→佩戴→工作→取下→放回的大动作顺序基本生成；但关键“开盒/取出/放回”动作存在操作方向和手部接触错误，不能视为完整执行成功。

### SPATIAL_PHYSICAL_CONTINUITY: FAIL
Evidence:
打开耳机盒时，盒内结构朝向镜头而不是人物，人物实际面对盒盖背面，属于操作面与机位冲突；取出耳机和放回耳机时均出现手指/产品穿插或接触失真。

### PERFORMANCE_REACTION: PARTIAL
Evidence:
人物整体克制自然，没有夸张瞪眼；但“Client call now”没有制造足够明显的紧迫感，人物状态变化偏弱，几乎一直维持同一种平静办公状态。

### PROOF_FIDELITY: PARTIAL
Evidence:
开盒、取出、佩戴、收纳过程在画面中可见；但开盒操作方向不合理、精细取放穿模，使“真实使用流程”这一Proof受到破坏。

### COMMERCIAL_CLARITY: PARTIAL
Evidence:
可以理解为职场女性在办公室使用AirPods，但产品为什么在此刻必须介入、它如何推动任务完成，表达偏弱，更像办公使用展示而非完整剧情带货广告。

### STORY_ENGAGEMENT: FAIL
Evidence:
前段虽然文本设定有“Client call now”，成片没有形成足够可见的Deadline/关系压力/未完成事件；全片主要是坐着工作→拿耳机→戴上→继续工作→收纳，剧情能量太平，缺少继续观看动力。

PRIMARY FAILURE TYPE:
PROMPT_COMPILER

SECONDARY ROOT CAUSE:
SKILL_RULE_GAP + BENCHMARK_DESIGN

FAILURE PATTERNS:
GF15｜Proof镜头与人物操作面冲突
GF16｜小物体×手指精细取放穿模
GF17｜Story Driver存在但没有被视觉化，剧情变平

ROOT CAUSE:
1. 提示词反复强调“清楚展示耳机盒内部”，但没有先锁人物操作侧与机位，模型为了观众展示牺牲人物真实使用方向；
2. 同一产品流程包含多次厘米级小物体精细抓取，且缺少“一镜一项高风险接触”的拆分；
3. 为了做稳定性诊断，把R0错误地写成了低事件强度，S04的Deadline/Client Driver主要停留在一句台词里；
4. 【开场总控】塞入大量产品/生成禁止项，违背主Skill“只写虚化导演概念”的既有原则。

FIX:
- 新增 `references/camera-action-compiler.md`；
- 关键开盒改为人物肩后OTS/操作侧近景，人物与观众看到同一工作面；
- 小物体取放改成单次接触、稳定支撑、必要时动作匹配切镜；
- Attempt 2强化SA04本身的可见Deadline/Client事件，不通过升级R1/R2制造刺激；
- Benchmark新增 STORY_ENGAGEMENT；
- 开场总控收缩为默认1句、最多2句，生成限制全部后移。

RETEST REQUIRED:
YES

RETEST TARGET:
B1-S04-P1 Attempt 2

FINAL CASE STATUS:
FAIL / RETEST

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
PASS / PARTIAL / FAIL
Evidence:

PRODUCT_LOCK:
PASS / PARTIAL / FAIL / N/A
Evidence:

ACTION_EXECUTION:
PASS / PARTIAL / FAIL
Evidence:

SPATIAL_PHYSICAL_CONTINUITY:
PASS / PARTIAL / FAIL
Evidence:

PERFORMANCE_REACTION:
PASS / PARTIAL / FAIL
Evidence:

PROOF_FIDELITY:
PASS / PARTIAL / FAIL
Evidence:

COMMERCIAL_CLARITY:
PASS / PARTIAL / FAIL
Evidence:

STORY_ENGAGEMENT:
PASS / PARTIAL / FAIL
Evidence:

PRIMARY FAILURE TYPE:
SKILL_RULE / PROMPT_COMPILER / MODEL_LIMIT / RANDOM_GENERATION / PRODUCT_ASSET_LIMIT / NONE

FAILURE PATTERNS:
GFxx...

ROOT CAUSE:

FIX:

RETEST REQUIRED:
YES / NO

FINAL CASE STATUS:
PASS / PARTIAL / FAIL / STOPPED
```

---

# 4. 修改证据规则

任何对SSOT的修改，在这里留下：

```text
CHANGE ID:
TRIGGER CASE(S):
OBSERVED FAILURE:
ROOT CAUSE:
FILES CHANGED:
EXPECTED IMPROVEMENT:
RETEST CASE(S):
RETEST RESULT:
```

原则：

> 没有真实Case证据，不因为单次“看起来可能更好”继续膨胀核心Skill。

---

# 5. 当前状态

Benchmark V1已开始真实生成。

已运行：
- B1-S04-P1 Attempt 1｜FAIL / RETEST

其他Case：`NOT_RUN`

不得根据理论回归结果填充真实生成PASS。
