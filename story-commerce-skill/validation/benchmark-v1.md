# BENCHMARK V1｜4 Scene × 3 Real SKU 首轮诊断

> 目标：用最小测试集暴露最大结构问题。

本Benchmark只验证真实生成表现，不重新设计3.4核心架构。

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

`TEXT_ONLY` 可以用于测试故事、动作、机位和模型默认理解，但**不能作为Product Lock已验证通过的充分证据**。

如果计划要求参考资产但实际未使用，保留Attempt，标记测试条件偏差，不伪装成正式资产锁定测试。

## 2.3 每个Case只验证一个主要购买问题

每条只锁：
- 1 Core Decision Question
- 1 Best Proof
- 1 Primary Architecture
- 1 R-level

不为了“Benchmark看起来厉害”塞多个卖点。

## 2.4 R0不等于平

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

**稳定但无吸引力，不算Benchmark成功。**

## 2.5 Scene必须真正触发DNA

S01至少触发礼仪/等级/公开呈递/权威判断之一。

S04至少触发Deadline/Client/Professional hierarchy/Competence/Responsibility之一。

S07至少触发Discovery/Comparison/Try-on or Demo/Shopper Decision之一。

S12至少触发Carriage order/Ownership/Attendant authority/Next-stop pressure/Object movement之一。

否则测试无效，只是在对应背景生成产品广告。

## 2.6 每条都必须包含真实Proof

Proof必须来自真实商品事实。

若产品没有适合某Scene直接验证的卖点：
- 换购买问题；或
- 该Case标记 `NOT_SUITABLE`，不为了填满12格编造Proof。

## 2.7 产品操作镜头必须通过Camera × Action Gate

所有开盒、开盖、取出、放回、佩戴、插拔、拆装等关键动作执行 `references/camera-action-compiler.md`。

必须先判断：

`人物操作方向 → 产品工作面 → 机位所在侧 → Proof可见性`

不能为了“让镜头看清”把产品以人物无法使用的方向转给观众。

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

理由：
- 先从相对现实/自然适配Scene开始；
- 再逐步增加空间与风格复杂度；
- 如果前面已经发现产品资产锁定问题，不必浪费积分继续跑更复杂Scene。

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

CORE DECISION QUESTION:

PRIMARY ARCHITECTURE:

BEST PROOF:

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
Notes:

2. PRODUCT_LOCK:
PASS / PARTIAL / FAIL / N/A
Notes:

3. ACTION_EXECUTION:
PASS / PARTIAL / FAIL
Notes:

4. SPATIAL_PHYSICAL_CONTINUITY:
PASS / PARTIAL / FAIL
Notes:

5. PERFORMANCE_REACTION:
PASS / PARTIAL / FAIL
Notes:

6. PROOF_FIDELITY:
PASS / PARTIAL / FAIL
Notes:

7. COMMERCIAL_CLARITY:
PASS / PARTIAL / FAIL
Notes:

8. STORY_ENGAGEMENT:
PASS / PARTIAL / FAIL
Notes:
是否在前1–3秒建立继续观看的理由？Primary Driver是否被视觉化？剧情是否有推进而非平铺产品操作？

PRIMARY FAILURE TYPE:
SKILL_RULE / PROMPT_COMPILER / MODEL_LIMIT / RANDOM_GENERATION / PRODUCT_ASSET_LIMIT / NONE

FAILURE PATTERN IDS:
GFxx...

NEXT ACTION:
KEEP / PROMPT_FIX / SKILL_FIX / SIMPLIFY / SPLIT_SHOT / CHANGE_CAMERA / CHANGE_SCENE / RERUN / STOP
```

---

# 6. 首轮停止条件

出现以下情况可以暂停当前产品剩余复杂Case，先修问题：

- Product Lock连续2条FAIL
- 同一物理交互连续2条FAIL
- 同一Scene关键空间规则连续2条FAIL
- Proof连续被Scene/表演挤掉
- Story Engagement连续2条FAIL
- 同一个Prompt Compiler缺陷跨2条复现

不要为了“凑齐12条”继续烧生成积分。

---

# 7. 首轮完成标准

Benchmark V1 Diagnostic完成要求：
- 12个Case全部有结果，或有明确NOT_SUITABLE/STOP理由
- 每个Case都有统一8项评分
- 所有FAIL/PARTIAL都有Failure Type
- 可复用失败进入Failure Pattern库
- Skill修改都有对应失败证据，不凭感觉加规则
- Scene Validation Registry得到真实测试数据，但不自动VALIDATED

完成后再决定：
- 哪些Case复测
- 哪些Scene进入扩大验证
- 是否需要测试剩余8个Scene
