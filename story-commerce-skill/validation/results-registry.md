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
| B1-S04-P1 | S04 | AirPods Pro 2 | PASS | PARTIAL* | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS / ACCEPTED |
| B1-S04-P2 | S04 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S04-P3 | S04 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P1 | S07 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P2 | S07 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S07-P3 | S07 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P1 | S12 | 3C | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P2 | S12 | Apparel | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| B1-S12-P3 | S12 | Daily Goods | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

`*` B1-S04-P1 Attempt 1–6均为 `TEXT_ONLY`；Product Lock只能做模型默认外观观察，不能作为Reference Asset Lock验证证据。

---

# 2. Case Records

## B1-S04-P1｜Attempt 1
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v1

RESULT:
- 开盒工作面与人物方向冲突；
- 取出/放回耳机穿模；
- 商业与剧情都偏平。

FAILURE PATTERNS: GF15 / GF16 / GF17
FINAL CASE STATUS: FAIL / RETEST

---

## B1-S04-P1｜Attempt 2
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v2

RESULT:
- OTS修正开盒方向；
- 佩戴过慢、收纳状态瞬移；
- 主角负面人格；
- 声音距离与听觉因果错误；
- 最严重：没有锁真实Why Buy，操作步骤被错当成卖点。

FAILURE PATTERNS: GF15 / GF16 / GF17 / GF18 / GF19 / GF20 / GF21 / GF22
FINAL CASE STATUS: FAIL / COMMERCIAL RESET

---

## B1-S04-P1｜Attempt 3
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v3｜Commercial Reset｜ANC

COMMERCIAL FOCUS:
- Pain：开放办公室杂音干扰专注
- Selling Point：Active Noise Cancellation
- Architecture：SA01 Problem → Solution
- Emotional Payoff：混乱 → 专注 → 掌控

RESULT:
- ANC商业因果首次清楚成立；
- 主体产品操作与表演明显改善；
- 约10s以后进入Post-Proof Plateau；
- 结尾出现耳机复制状态。

FINAL CASE STATUS: PARTIAL / STORY RETEST

---

## B1-S04-P1｜Attempt 4｜Run A + Run B
DATE: 2026-09-03
MODEL / VERSION: Seedance 2.5
DURATION: 30s × 2
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v4｜R1 Surprise + Post-Proof Continuation

RESULT:
- 两次生成均复现亚秒多物理镜头插值/假硬切；
- 为修中段平台期加入过多自然主义事件，反而形成TV Drama Drift；
- 商业卖点仍清楚，但广告抓力下降。

FAILURE PATTERNS: GF22 / GF23 / GF24 / GF25
FINAL CASE STATUS: FAIL / AD PACING RESET

---

## B1-S04-P1｜Attempt 5
DATE: 2026-09-04
MODEL / VERSION: Seedance 2.5
DURATION: 30s
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v5｜Ad Density Reset

RESULT:
- 开场情绪感染不足；
- 明显180°越轴；
- 普通无动力手推车自行移动；
- 元机位语言被字面生成成摄影机/三脚架；
- Prompt锁了ANC，但成片Benefit仍不够可解码；
- 单一卖点被强行拉成30s，继续出现时长不匹配。

FAILURE PATTERNS: GF26 / GF27 / GF28 / GF29 / GF30
FINAL CASE STATUS: FAIL / STRUCTURE RESET

---

## B1-S04-P1｜Attempt 6
DATE: 2026-09-04
MODEL / VERSION: Seedance 2.5
DURATION: 15s
PRODUCT: Apple AirPods Pro 2｜White
ASSET MODE: TEXT_ONLY
PROMPT REVISION: B1-v6｜15s Benefit-Decoding + Axis-Lock Reset

COMMERCIAL FOCUS:
- Pain：开放办公室噪音持续打断专注
- Selling Point：Active Noise Cancellation
- Architecture：SA01 Problem → Solution
- Emotional Payoff：被打断 → 戴上 → 噪音退远 → 恢复掌控

### SCENE_RECOGNITION: PASS
现代开放办公室清楚成立，打印机、电脑、背景员工与工作状态都服务真实办公语境。

### PRODUCT_LOCK: PARTIAL OBSERVATION ONLY
白色AirPods Pro 2外观与充电盒大体稳定可识别；仍为纯文生，因此不能验证Reference Asset Lock。

### ACTION_EXECUTION: PASS
拿起、开盒、佩戴的主动作清楚，未观察到前几版明显的小物体穿模或状态瞬移。

### SPATIAL_PHYSICAL_CONTINUITY: PASS
全片机位基本保持在同一拍摄半区，未观察到Attempt 5那种明显左前→右前→左后的越轴；未出现无人手推车、摄影设备入镜或明显无动力物体运动。

### PERFORMANCE_REACTION: PASS
开场噪音能够真实打断女主注意力；产品介入后，视线重新锁定电脑、动作恢复，情绪从被干扰到重新掌控可读。

### PROOF_FIDELITY: PASS
同一办公室视觉在前后保持，变化集中在声音层与人物注意力状态，ANC Benefit Expression清楚且没有引入第二卖点。

### COMMERCIAL_CLARITY: PASS
不依赖最后旁白也能基本理解：办公室噪音持续打断工作，戴上AirPods后干扰退远、专注恢复。

### STORY_ENGAGEMENT: PASS
15s时长与单一卖点匹配，删除了前几版长时间“继续办公”的填充段，故事因果在短时间内完成。

### EMOTIONAL_PAYOFF: PASS
Problem Cost与Product After之间有明显状态反差，整体比30s版本更有释放感与广告效率。

### AUDIO_CAUSALITY: PASS
ANC前后的环境声层级逻辑成立，没有远距离人物贴脸对白或佩戴耳机后错误响应外部声音的问题。

### CTA SALIENCE: PARTIAL｜ACCEPTED WITHOUT RERUN
13–15s CTA视觉显著性仍有提升空间，但用户明确决定不再重新生成，本条按可交付版本接受。CTA优化作为未来通用经验保留，不阻断本Case通过。

PRIMARY FAILURE TYPE: NONE

RETEST EVIDENCE:
- GF26 180°越轴：目标问题本版未复现；
- GF27 无动力道具运动：未复现；
- GF28 Benefit Decodability：明显改善并PASS；
- GF29 Duration-to-Story Misfit：15s版本解决；
- GF30 Meta-camera Literalization：未复现。

USER ACCEPTANCE:
- 2026-09-04：用户明确决定“不再重新生成了，这条算过”。

NEXT ACTION:
- 本Case停止复测；
- CTA视觉显著性作为后续广告通用优化项，不回滚本条已通过结论。

FINAL CASE STATUS: PASS / ACCEPTED

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
CTA_SALIENCE:

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
- 连续空间镜头必须审核180°轴线。
- 普通道具移动必须有可见/合理动力来源。
- 单卖点若在前半自然讲完，优先缩短，不用“继续工作/继续使用”填满30秒。
- **主体广告已经成立时，CTA弱可以作为局部优化项；若用户接受当前成片，不需要为了边际CTA提升重新扰动已经验证通过的商业因果、轴线和产品动作。**

---

# 5. 当前状态

已运行：
- Attempt 1｜FAIL / RETEST
- Attempt 2｜FAIL / COMMERCIAL RESET
- Attempt 3｜PARTIAL / STORY RETEST
- Attempt 4 Run A+B｜FAIL / AD PACING RESET
- Attempt 5｜FAIL / STRUCTURE RESET
- Attempt 6｜PASS / ACCEPTED

B1-S04-P1当前结论：
- 本Case已通过并停止复测；
- 15s单卖点结构明显优于强行30s；
- 180° Axis Lock、Motive Force、Benefit Decodability、Duration Fit与Meta-Camera Guard本次复测有效；
- Product Lock仍未经过Reference Asset验证；
- CTA视觉显著性保留为未来通用优化项，但不阻断本Case结案。

其他Case：`NOT_RUN`
