# SCENE VALIDATION REGISTRY｜Scene验证状态表

## 0. 用途

本文件只负责记录Scene测试证据与状态，不负责Scene选择，也不负责执行DNA。

通过 `SCENE_ID` 与以下文件关联：
- 路由层：`scene-index.md`
- 执行层：`scene-dna-library.md`
- 调度层：`scene-router.md`

任何Scene只有在真实测试证据满足升级条件后，才允许从 `TESTING_CANDIDATE` 升级为 `VALIDATED`。

**理论设计成熟、结构QA通过、跨品类纸面可迁移，都不等于Seedance生成已验证。**

---

# 1. Validation Status枚举

Scene总状态：
`RESEARCH / TESTING_CANDIDATE / VALIDATED / RESTRICTED / RETIRED`

单项测试状态：
`PASS / FAIL / PARTIAL / NOT_TESTED / NOT_APPLICABLE`

内部设计检查：
`INTERNAL_PASS / INTERNAL_FAIL`

`INTERNAL_PASS`不得替代真实生成PASS。

---

# 2. 每个Scene必须记录的测试字段

## A｜STRUCTURAL QA
- `STRUCTURAL_RND`
- `HORIZONTAL_DIFFERENTIATION_QA`
- `CROSS_CATEGORY_INTERNAL_QA`

## B｜ACTUAL GENERATION TESTS
- `CROSS_PRODUCT_3C`
- `CROSS_PRODUCT_APPAREL`
- `CROSS_PRODUCT_DAILY_GOODS`
- `SCENE_RECOGNITION`
- `PRODUCT_LOCK`
- `SPACE_CONTINUITY`
- `PHYSICAL_INTERACTION`
- `MULTI_CHARACTER_STABILITY`
- `HANDOFF_STABILITY`
- `REACTION_CHAIN_EXECUTION`

## C｜SAFETY / IP
- `SAFETY_GATE`
- `IP_DISTINCTNESS`

## D｜EVIDENCE

每个实际PASS/PARTIAL/FAIL逐步补：
- 测试日期
- 测试商品
- 模型/版本
- Case / Attempt
- Asset Mode
- 失败模式
- 修复后是否复测

`TEXT_ONLY`可以支持Scene、动作、空间、Performance诊断，但不能单独把Reference Product Lock升级PASS。

---

# 3. VALIDATED升级硬条件

至少同时满足：
- [ ] 3C跨商品生成 PASS
- [ ] Apparel跨商品生成 PASS
- [ ] Daily Goods跨商品生成 PASS
- [ ] Scene Recognition PASS
- [ ] PRODUCT LOCK PASS
- [ ] Space Continuity PASS
- [ ] Physical Interaction PASS
- [ ] 关键多人/交接在适用时PASS
- [ ] Scene-specific Reaction PASS
- [ ] Safety Gate PASS
- [ ] IP Distinctness PASS
- [ ] 同一Scene换商品仍保持世界发动机
- [ ] 同一商品换Scene后故事因果明显改变

任一关键项FAIL或NOT_TESTED，继续 `TESTING_CANDIDATE`。

---

# 4. 当前12个Scene总表

| ID | Scene | Status | Structural R&D | Horizontal QA | Cross-Category Internal QA | Actual Generation |
|---|---|---|---|---|---|---|
| S01 | 架空古装宫廷 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S02 | 现代美国高中 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S03 | 架空古代战争军营 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S04 | 现代美国企业办公室 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | STARTED / FAIL-RETESTING |
| S05 | 架空美国西部边疆贸易小镇 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S06 | 架空现代豪华上流晚宴 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S07 | 现代美国大型购物中心 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S08 | 架空未来都市·星际商业世界 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S09 | 架空复古美国公路Diner | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S10 | 架空高压真人竞赛节目 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S11 | 架空古代地中海公共市集 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |
| S12 | 架空复古豪华长途列车 | TESTING_CANDIDATE | INTERNAL_PASS | INTERNAL_PASS | INTERNAL_PASS | NOT_TESTED |

---

# 5. 实际生成测试矩阵｜当前证据

| ID | 3C | Apparel | Daily Goods | Recognition | Product Lock | Space | Physical | Multi-Char | Handoff | Reaction |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S02 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S03 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S04 | FAIL | NOT_TESTED | NOT_TESTED | PARTIAL | NOT_TESTED* | FAIL | FAIL | PARTIAL | NOT_APPLICABLE | FAIL |
| S05 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S06 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S07 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S08 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S09 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S10 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S11 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |
| S12 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED |

`*` S04两次3C Attempt均为TEXT_ONLY，Reference Product Lock仍是NOT_TESTED。

---

# 6. S04实际证据

## B1-S04-P1｜Attempt 1

- 日期：2026-09-03
- 商品：Apple AirPods Pro 2｜White
- 模型：Seedance 2.5
- 时长：30s
- Asset Mode：TEXT_ONLY
- Scene Recognition：PARTIAL
- Space / Physical：FAIL
- Reaction：PARTIAL
- 关键失败：GF15 / GF16 / GF17
- 复测：Attempt 2

## B1-S04-P1｜Attempt 2

- 日期：2026-09-03
- 商品：Apple AirPods Pro 2｜White
- 模型：Seedance 2.5
- 时长：30s
- Asset Mode：TEXT_ONLY
- Scene Recognition：PARTIAL
- 3C Overall：FAIL
- Product Lock：NOT_TESTED as reference-lock evidence
- Space Continuity：FAIL
- Physical Interaction：FAIL
- Reaction：FAIL
- Multi-character：PARTIAL（人物身份稳定，但关系/行为语义不够清楚）
- Handoff：NOT_APPLICABLE
- 关键进展：
  - GF15开盒机位错误在Attempt 2未复现，转MITIGATED；
- 关键失败：
  - GF16 小物体精细取放仍不稳定
  - GF17 Story Driver仍弱
  - GF18 Commercial Decision被测试动作取代
  - GF19 主角负面情绪承担张力
  - GF20 佩戴动作节拍过慢
  - GF21 声音空间/听觉因果不成立
  - GF22 成对耳机状态瞬移
- 复测：REQUIRED｜Attempt 3必须Commercial Reset

详细证据：`validation/results-registry.md`

---

# 7. Index Migration记录

当前S01–S12全部迁移到 `scene-index.md` V1.1：

`S01 / S02 / S03 / S04 / S05 / S06 / S07 / S08 / S09 / S10 / S11 / S12 = MIGRATED`

Index迁移状态与Validation状态必须分开管理。
