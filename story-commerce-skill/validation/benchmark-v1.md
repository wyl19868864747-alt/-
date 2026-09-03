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

不能因为宫廷/列车视觉需要就改变：
- 产品颜色
- 尺度
- 结构
- 包装
- 配件
- 真实功能

这样才能测出Scene对Product Lock的污染风险。

## 2.2 Asset Mode必须登记

每次Attempt必须写明：
- `REFERENCE_ASSET`：实际上传产品参考图并参与生成；
- `TEXT_ONLY`：纯文生，只靠型号/描述；
- `PARTIAL_REFERENCE`：只有部分资产参与。

`TEXT_ONLY`可以测试故事、动作、机位和模型默认理解，但**不能作为Product Lock已验证通过的充分证据**。

## 2.3 Commercial Validity Gate｜先证明“这广告值得拍”

每个Case在Story Architecture之前必须回答：

1. **真实Why Buy是什么？** 用户为什么会因为这个能力而想买？
2. **真实Pain / Hesitation是什么？** 它解决什么麻烦、担忧或选择问题？
3. **Confirmed Product Advantage是什么？** 必须来自真实产品事实。
4. **Best Proof / Best Expression是什么？** 视频能否诚实表达这个利益？
5. **Emotional Payoff是什么？** 观众最终应该感到爽、安心、轻松、惊喜、掌控、被理解，还是别的明确情绪？

硬规则：

> **产品操作步骤 ≠ 自动等于商业卖点。**

“打开、拿起、戴上、放回、收纳”只有在它本身就是消费者重要购买理由时，才能成为Core Decision Question；否则只能是执行动作/Proof载体。

如果只是想测手部穿模、开盒、佩戴等模型能力：

> 可以做 `TECHNICAL DIAGNOSTIC CLIP`，但不能把它伪装成剧情带货Benchmark并据此评价广告创意能力。

## 2.4 每个Case只验证一个主要购买问题

每条只锁：
- 1 Core Decision Question
- 1 Top Pain / Hesitation
- 1 Confirmed Selling Point
- 1 Best Proof / Expression
- 1 Primary Architecture
- 1 R-level
- 1 Emotional Payoff

不为了“Benchmark看起来厉害”塞多个卖点。

## 2.5 R0不等于平

Benchmark虽然优先诊断稳定性，但仍然是**剧情带货广告**。

必须保留当前Primary Architecture的Story Driver：
- SA04必须真的看见Deadline / Client / Professional consequence至少一项；
- SA07必须真的看见关系/地位变化压力；
- SA05必须真的有选择与比较；
- SA06必须真的有未知/调查。

前1–3秒至少建立一个：
- 正在发生的事件
- 未完成任务
- 可见压力
- 冲突/选择
- 异常状态

同时：

> **Tension Source ≠ Protagonist Negativity**

普通商用广告中，压力优先来自环境、任务、时间、关系或问题；主角应保持有能力、可喜欢、值得代入。除非用户明确要荒诞/黑色/抓马/反转，不用“不耐烦、丧气、嫌弃别人”承担Hook。

**稳定但无吸引力，不算Benchmark成功。**

## 2.6 Scene必须真正触发DNA

S01至少触发礼仪/等级/公开呈递/权威判断之一。

S04至少触发Deadline/Client/Professional hierarchy/Competence/Responsibility之一。

S07至少触发Discovery/Comparison/Try-on or Demo/Shopper Decision之一。

S12至少触发Carriage order/Ownership/Attendant authority/Next-stop pressure/Object movement之一。

否则测试无效，只是在对应背景生成产品广告。

## 2.7 每条都必须包含真实Proof / Benefit Expression

Proof必须来自真实商品事实。

若卖点属于主观/声音/长期/不可直接视觉证明：
- 允许使用诚实的感官/声音/行为表达；
- 不把代理表现写成精确客观测试；
- 必要时用官方已确认事实作为商业依据，但不伪造实验数据。

若产品没有适合某Scene表达的真实卖点：
- 换购买问题；或
- 该Case标记 `NOT_SUITABLE`。

## 2.8 产品操作镜头必须通过Camera × Action Gate

所有开盒、开盖、取出、放回、佩戴、插拔、拆装等关键动作执行 `references/camera-action-compiler.md`。

必须先判断：

`人物操作方向 → 产品工作面 → 机位所在侧 → Proof可见性`

不能为了“让镜头看清”把产品以人物无法使用的方向转给观众。

## 2.9 Action Tempo Gate｜动作时长必须符合能量

简单微动作不能因为分到3秒就被演员慢慢演满3秒。

高能/利落广告中：
- 拿起、抬手、单次佩戴、按一下、打开等简单动作，通常按约`0.5–1.2s`的视觉节拍设计；
- 需要蓄力时，把时间给“事件预备/视线锁定/声音Cue”，动作本身仍应短促；
- 复杂精细交互可以拆镜，但不要用“慢动作式完成”换稳定。

`蓄力高能感 = 预备 → 快速动作 → 清楚结果/切镜`

不是：`人物慢慢完成一个简单动作`。

## 2.10 Audio Spatial Causality Gate

任何对白/画外音必须锁：
- Speaker位置
- On-screen / Off-screen
- 与镜头/听者距离
- 声音方向
- 相对音量/房间感

如果人物佩戴耳机、隔着门/玻璃、处于远距离：

> 必须解释为什么她能听清，或不要让她直接听清。

不能靠“这是对白所以主角自动听见”。

若依赖Transparency / Conversation Awareness等真实产品功能，必须明确产品模式/触发条件，并确保事实准确。

## 2.11 Object State Ledger｜成对/多件商品逐Beat记账

对耳机、鞋、手套、两件配件等，必须逐Beat记录每一件在哪里。

例如：

`L earbud = left ear`
`R earbud = right ear`
`case = desk closed/open`

下一镜若状态改变，必须有：

`可见动作` 或 `明确动作匹配切`。

禁止：上一镜两只耳机都在耳朵，下一镜一只已经躺在盒里，没有任何取下过程。

**Hero Shot也必须服从Object State Ledger。** 不允许因为“标准商品图长这样”就把正在被人物佩戴/使用的配件重新复制回包装或盒体。

## 2.12 Post-Proof Continuation Check｜卖点证明后，故事还活着吗？

真实Benchmark发现：一条30秒广告即使Hook、Selling Point和Proof都正确，如果在8–10秒已经完成核心Benefit，后面十几秒只剩“继续工作 / 继续使用 / 继续微笑”，观众依然会觉得平。

如果Best Proof / Benefit Expression在总时长前约40–50%已经完成，后续必须二选一：

### A. 继续推进同一个商业因果
至少发生1个与当前Selling Point直接相关的新Beat，例如：
- Benefit产生真实后果；
- 人物关系/立场变化；
- 新的小阻力被同一个Benefit解决；
- 轻Surprise；
- Comedy Payoff；
- 新选择/新目标；
- Product Benefit导致新的Decision Change。

### B. 缩短广告
如果没有值得发生的新Beat：

> **直接缩成15–20秒，比用重复使用镜头填满30秒更好。**

硬规则：
- 不因为中段平就条件反射强制R2；
- R0可以通过`Proof → Consequence → Emotional Payoff`保持有趣；
- R1 Surprise / Comedy可以作为轻量增强，但必须继续服务同一个Selling Point；
- 禁止为了续命突然加入第二卖点；
- Proof后每4–6秒至少检查是否出现`新信息 / 新动作目标 / 新关系 / 新后果 / 新笑点`之一。

---

# 3. 推荐执行顺序

不要按Scene连续做完，优先按产品做，方便观察同一商品在不同世界中的Product Lock：

第一组 P1 3C：
1. B1-S04-P1
2. B1-S07-P1
3. B1-S12-P1
4. B1-S01-P1

第二组 P2 服装：
5. B1-S07-P2
6. B1-S12-P2
7. B1-S01-P2
8. B1-S04-P2

第三组 P3 日用品：
9. B1-S04-P3
10. B1-S07-P3
11. B1-S12-P3
12. B1-S01-P3

如果前面已经发现系统级问题，先修再继续，不为凑齐12条烧积分。

---

# 4. 每个Case的固定输入卡

```text
CASE ID:

PRODUCT TRUTH:
- SKU:
- Asset Mode: REFERENCE_ASSET / PARTIAL_REFERENCE / TEXT_ONLY
- Reference Assets:
- Size:
- Material:
- Structure:
- Accessories:
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
- Proof complete at:
- Next causal beat:
- Why it still serves the same selling point:

PRIMARY GENERATION RISK:
```

---

# 5. 每条视频固定评分表

```text
CASE ID:
GENERATION MODEL / VERSION:
ATTEMPT:
ASSET MODE:

1. SCENE_RECOGNITION:
PASS / PARTIAL / FAIL

2. PRODUCT_LOCK:
PASS / PARTIAL / FAIL / N/A

3. ACTION_EXECUTION:
PASS / PARTIAL / FAIL

4. SPATIAL_PHYSICAL_CONTINUITY:
PASS / PARTIAL / FAIL

5. PERFORMANCE_REACTION:
PASS / PARTIAL / FAIL

6. PROOF_FIDELITY:
PASS / PARTIAL / FAIL

7. COMMERCIAL_CLARITY:
PASS / PARTIAL / FAIL
是否一眼知道在卖哪个核心利益？

8. STORY_ENGAGEMENT:
PASS / PARTIAL / FAIL
前1–3秒是否有继续看的理由？Proof后是否仍有推进？

9. EMOTIONAL_PAYOFF:
PASS / PARTIAL / FAIL
是否能感到预设情绪，而不是只有人物动作？

10. AUDIO_CAUSALITY:
PASS / PARTIAL / FAIL / N/A
距离、方向、耳机/门/空间遮挡与听觉逻辑是否成立？

11. POST_PROOF_CONTINUATION:
PASS / PARTIAL / FAIL / N/A
若Proof在前半段完成，后续是否出现新的因果Beat，还是只重复“继续使用”？

PRIMARY FAILURE TYPE:
SKILL_RULE / PROMPT_COMPILER / MODEL_LIMIT / RANDOM_GENERATION / PRODUCT_ASSET_LIMIT / NONE

FAILURE PATTERN IDS:
GFxx...

NEXT ACTION:
KEEP / PROMPT_FIX / SKILL_FIX / COMMERCIAL_RESET / SIMPLIFY / SPLIT_SHOT / CHANGE_CAMERA / CHANGE_SCENE / SHORTEN / ADD_CONSEQUENCE / ADD_R1_SURPRISE / RERUN / STOP
```

---

# 6. 首轮停止条件

出现以下情况暂停当前产品剩余Case，先修问题：

- Core Decision / Selling Point本身不成立
- Product Lock连续2条FAIL
- 同一物理交互连续2条FAIL
- 同一Scene关键空间规则连续2条FAIL
- Commercial Clarity连续2条FAIL
- Story Engagement连续2条FAIL
- Proof在前半段完成但Post-Proof Continuation连续失败
- 同一Prompt Compiler缺陷跨2条复现

尤其：

> **如果Commercial Validity Gate失败，不允许继续在镜头层打补丁。回到商品决策层重做。**

---

# 7. 首轮完成标准

Benchmark V1 Diagnostic完成要求：
- 12个Case全部有结果，或有明确NOT_SUITABLE/STOP理由
- 每个Case执行统一评分
- 所有FAIL/PARTIAL都有Failure Type
- 可复用失败进入Failure Pattern库
- Skill修改都有对应失败证据，不凭感觉加规则
- Scene Validation Registry得到真实测试数据，但不自动VALIDATED

完成后再决定：
- 哪些Case复测
- 哪些Scene进入扩大验证
- 是否需要测试剩余8个Scene
