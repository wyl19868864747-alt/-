# 剧情带货 Skill｜真实生成验证区

> 目的：把 3.4 COMMERCIAL FREEZE 从“结构上合理”推进到“有真实 Seedance 证据支持”。

本目录不负责继续扩写创意理论。它只负责：

`真实商品 → 固定Benchmark → Seedance生成 → 视频复盘 → 失败归因 → Skill修正 → 复测 → Validation状态更新`

---

# 1. 当前验证阶段

当前阶段：`BENCHMARK V1｜DIAGNOSTIC`

先测试4个代表Scene：
- S01 架空古装宫廷：高视觉 / 等级 / 社会关系
- S04 现代美国企业办公室：现实 / 工作 / 任务
- S07 现代美国大型购物中心：消费选择 / 试用
- S12 架空复古豪华长途列车：复杂空间 / 移动 / 归属

每个Scene测试3类真实商品：
- P1：1个真实3C SKU
- P2：1个真实服装 SKU
- P3：1个真实日用品 SKU

共：`4 Scene × 3 SKU = 12 条首轮诊断视频`

这12条不是为了直接把Scene升级为VALIDATED，而是为了最快找出：
- Skill规则问题
- Prompt Compiler问题
- Seedance能力边界
- Scene-specific高风险动作

---

# 2. 用户负责什么

用户只负责三件事：

## A. 提供3个真实SKU
每个SKU尽量提供：
- 产品参考图 / 白底图 / 包装图（有多少给多少）
- 产品真实名称
- 真实尺寸 / 材质 / 结构 / 配件
- 允许说的核心卖点
- 禁止说或无法确认的信息
- 目标平台 / 时长（若有）

不要为了测试临时编造产品事实。

## B. 按我给的最终Seedance提示词生成
首轮一次只做1个Benchmark Case，不批量乱跑。

生成时尽量保持：
- 同一模型版本
- 同一基础生成设置
- 不自行改Prompt结构

这样失败才有比较价值。

## C. 把生成视频原文件上传回来
最好同时说明：
- 对应Case ID
- 是否一次生成 / 是否重试
- 若你肉眼已经看到明显问题，可顺手说一句

不需要你自己写长复盘。

---

# 3. Assistant负责什么

每个Case由Assistant负责：

1. 从真实SKU建立Product Truth Card
2. 选择该Benchmark需要验证的商业问题 / Story Architecture / Proof / R-level
3. 按指定Scene编译故事与Seedance提示词
4. 收到视频后逐项评分
5. 判断失败属于：
   - `SKILL_RULE`
   - `PROMPT_COMPILER`
   - `MODEL_LIMIT`
   - `RANDOM_GENERATION`
   - `PRODUCT_ASSET_LIMIT`
6. 把新失败模式登记进 `generation-failure-patterns.md`
7. 把本次结果写入 `results-registry.md`
8. 只有确认属于Skill/Compiler问题时才修改SSOT
9. 修改后只复测受影响Case，不无脑重跑全部12条
10. 当证据足够时更新 `scene-validation-registry.md`

核心原则：

> **不把所有失败都怪Prompt，也不把所有失败都靠加词解决。**

---

# 4. 固定评分

每条视频统一检查7项：

1. `SCENE_RECOGNITION`：一眼能否认出目标Scene，且不是只靠服装/背景
2. `PRODUCT_LOCK`：外观、颜色、比例、结构、包装是否稳定
3. `ACTION_EXECUTION`：关键动作是否按Prompt发生且顺序正确
4. `SPATIAL_PHYSICAL_CONTINUITY`：左右、入口、位置、接触、交接、尺度是否合理
5. `PERFORMANCE_REACTION`：Reaction是否自然、由Trigger触发、没有同步瞪眼/提前泄底
6. `PROOF_FIDELITY`：Best Proof是否清楚、没有被剧情/Scene/特效挤掉或伪造
7. `COMMERCIAL_CLARITY`：只看成片是否能理解人物为什么继续、产品在解决什么购买问题

评分只用：
- `PASS`
- `PARTIAL`
- `FAIL`
- `N/A`

不用100分制，避免假精确。

---

# 5. 首轮诊断规则

- 每个Case先生成1条。
- 首轮只找问题，不追求VALIDATED。
- 出现FAIL时先归因，再决定是否改Skill。
- 同一失败连续跨Case出现，优先升级为系统级Failure Pattern。
- 单次偶发畸变且Prompt/结构无明显诱因，可先标记 `RANDOM_GENERATION`，不立刻污染Skill。
- `MODEL_LIMIT`问题优先通过降低人物数、拆动作、换镜头结构、避开高风险交接解决，不靠堆砌负面词硬顶。

---

# 6. Scene升级原则

Benchmark V1通过不等于VALIDATED。

单Scene要升级VALIDATED，仍需在 `scene-validation-registry.md` 中满足硬条件，包括：
- 3C真实生成PASS
- 服装真实生成PASS
- 日用品真实生成PASS
- Scene Recognition PASS
- Product Lock PASS
- Space Continuity PASS
- Physical Interaction PASS
- 适用的多人/Handoff稳定性PASS
- Scene-specific Reaction PASS
- Safety / IP PASS

关键项仍为FAIL / NOT_TESTED时保持：
`TESTING_CANDIDATE`

---

# 7. 最终希望得到什么

完成这一阶段后，不是得到“12条漂亮视频”，而是得到：

- 哪些Scene真的稳定
- 哪些动作Seedance经常失败
- 哪些Prompt写法实际有效
- 哪些理论规则应该删掉
- 哪些Generation Risk应该被Router提前规避
- 哪些Scene可以从TESTING_CANDIDATE进入VALIDATED

最终Skill会从：

> “理论上知道怎么做”

升级为：

> **“知道哪些做法在真实生成里已经被验证，哪些地方模型会翻车，并会主动避开。”**
