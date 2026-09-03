# SCENE INDEX｜Scene DNA 路由索引

## 0. 用途

本文件是 Scene Database 的**路由层**，不是执行型 Scene Card，也不是完整故事模板。

调用顺序：

`Commercial Decision → Story Architecture → Proof Plan → Reversal Router → Scene Router → Scene Index → 选中Scene → scene-dna-library.md对应Card`

Scene Index负责回答：

> **这个已经确定的商业问题、Story Architecture、Proof和R0/R1/R2，哪些Scene值得进入候选？**

执行细节仍由 `scene-dna-library.md` 提供；验证状态由 `scene-validation-registry.md` 提供。

---

# 1. 数据结构 V1.1

## A｜IDENTITY

- `SCENE_ID`
- `NAME_ZH`
- `NAME_EN`
- `STATUS`
- `PRIMARY_CLASS`
- `SECONDARY_CLASS_TAGS[]`
- `ERA`
- `REALISM_MODE`
- `BASE_VISUAL_DISTINCTIVENESS`

允许的状态：

`RESEARCH / TESTING_CANDIDATE / VALIDATED / RESTRICTED / RETIRED`

## B｜WORLD ENGINE

- `WORLD_ENGINE`
- `NATIVE_CONFLICT_TAGS[]`
- `NATIVE_CONFLICT_DESCRIPTION`
- `SOCIAL_RULES`
- `POWER_STRUCTURE`
- `NATIVE_TIME_PRESSURE`
- `NATIVE_INFORMATION_FLOW`
- `OBJECT_STATUS_LOGIC`
- `DNA_ACTIVATION_CONDITION`
- `SPACE_TOPOLOGY`
- `CONTINUITY_ANCHORS[]`

`DNA_ACTIVATION_CONDITION` 是硬检查：如果这些世界规则没有实际进入因果链，该空间只能算普通Location，不算调用Scene DNA。

## C｜COMMERCIAL ROUTING

- `DECISION_FIT`：D1–D10
- `ARCHITECTURE_FIT`：SA01–SA09
- `PROOF_FIT`：V1–V4
- `PROOF_MODES[]`
- `PRODUCT_ENTRY_MODES[]`
- `AUDIENCE_CONSTRAINTS[]`
- `REVERSAL_COMPATIBILITY`
- `SUPPORTED_REVERSAL_TYPES[]`
- `COMEDY_COMPATIBILITY`
- `ABSURDITY_COMPATIBILITY`
- `VISUAL_SPECTACLE_VALUE`

注意：
- 不存静态 `Audience Fit`；Character/Audience Fit由Router结合具体任务动态计算。
- `REVERSAL_COMPATIBILITY` 只表示Scene容得下R2，不表示本条广告应使用R2。R0/R1/R2已经由 `reversal-router.md` 先确定。

## D｜GENERATION ROUTING

- `GENERATION_RISKS`
- `SEEDANCE_LOCKS`
- `FAILURE_PATTERNS`

## E｜评分枚举

所有静态Fit统一使用：

`BLOCKED / LOW / MEDIUM / HIGH`

运行时可映射：

`BLOCKED = 淘汰`
`LOW = 0`
`MEDIUM = 1`
`HIGH = 2`

Safety BLOCKED永远高于总分。

---

# 2. Migration Status

当前12个Scene仍全部保留；本轮只完成3个Pilot结构化迁移，用于验证Schema与Router。

| ID | Scene | Index Migration | Routing Note |
|---|---|---|---|
| S01 | 架空古装宫廷 | PILOT_READY | 可使用结构化Index |
| S02 | 现代美国高中 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S03 | 架空古代战争军营 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S04 | 现代美国企业办公室 | PILOT_READY | 可使用结构化Index |
| S05 | 架空美国西部边疆贸易小镇 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S06 | 架空现代豪华上流晚宴 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S07 | 现代美国大型购物中心 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S08 | 架空未来都市·星际商业世界 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S09 | 架空复古美国公路Diner | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S10 | 架空高压真人竞赛节目 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S11 | 架空古代地中海公共市集 | PENDING_MIGRATION | 暂用legacy Scene Card / Safety Gate |
| S12 | 架空复古豪华长途列车 | PILOT_READY | 可使用结构化Index |

**过渡期规则**：在12个Scene全部迁移完成前，不得因为某Scene尚无结构化Index分数而自动淘汰它；未迁移Scene继续读取现有Scene Card和Scene Router先验。结构化Index仅对已迁移记录提供更精确比较。

---

# 3. S01｜架空古装宫廷

## IDENTITY

- `SCENE_ID`: S01
- `NAME_ZH`: 架空古装宫廷
- `NAME_EN`: FICTIONAL OLD-WORLD ROYAL COURT
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: SOCIAL_HIERARCHY
- `SECONDARY_CLASS_TAGS`: CEREMONIAL_PUBLIC_JUDGMENT, AUTHORITY, STATUS
- `ERA`: FICTIONAL_OLD_WORLD
- `REALISM_MODE`: NON_MAGICAL_STYLIZED_HISTORY
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE

- `WORLD_ENGINE`: 身份 + 等级 + 礼仪 + 公开审视 + 权力
- `NATIVE_CONFLICT_TAGS`: STATUS, ACCESS, AUTHORITY, OWNERSHIP, PUBLIC_JUDGMENT
- `NATIVE_CONFLICT_DESCRIPTION`: 谁能接近、发言、呈递、触碰；谁被公开纠正；谁获得或失去权威。
- `SOCIAL_RULES`: 接近、发言、递交、触碰、打断都受身份与礼仪限制；错误会被公开看见。
- `POWER_STRUCTURE`: HIGH_VERTICAL
- `NATIVE_TIME_PRESSURE`: LOW_MEDIUM
- `NATIVE_INFORMATION_FLOW`: LOWER_ROLE → STEWARD/AUTHORITY → RULER → COURT_REACTION
- `OBJECT_STATUS_LOGIC`: 普通商品一旦进入正式呈递程序，会获得礼仪、身份或权威意义。
- `DNA_ACTIVATION_CONDITION`: 至少一个必须进入因果链：礼仪许可 / 等级判断 / 公开呈递 / 权威裁决 / 身份权限。否则仅算古装Location。
- `SPACE_TOPOLOGY`: AXIAL
- `CONTINUITY_ANCHORS`: central_axis, raised_authority_position, ceremonial_entry, presentation_point, product_current_location

## COMMERCIAL ROUTING

### DECISION_FIT

- D1 空间尺寸: LOW
- D2 人体适配: MEDIUM
- D3 材质感官: MEDIUM
- D4 性能兼容: MEDIUM
- D5 机制维护: LOW
- D6 安全行为: LOW
- D7 食用仪式: MEDIUM
- D8 身份礼赠: HIGH
- D9 价值完整性: HIGH
- D10 安装物流: LOW

### ARCHITECTURE_FIT

- SA01: LOW
- SA02: MEDIUM
- SA03: HIGH
- SA04: LOW
- SA05: MEDIUM
- SA06: MEDIUM
- SA07: HIGH
- SA08: HIGH
- SA09: MEDIUM

### PROOF_FIT

- V1 直接可见: HIGH
- V2 过程可见: MEDIUM
- V3 代理可见: MEDIUM
- V4 不可画面直接证明: BLOCKED_AS_PROOF

- `PROOF_MODES`: PUBLIC_PRESENTATION, WORN_USE, HANDLED_INSPECTION, AUTHORITY_VERIFICATION, PACKAGE_CONTENT
- `PRODUCT_ENTRY_MODES`: TRIBUTE_ENTRY, WORN_ENTRY, DEMONSTRATION_ENTRY, LARGE_OBJECT_ENTRY
- `AUDIENCE_CONSTRAINTS`: no_real_royal_family_or_state_identity
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: IDENTITY, STATUS, OWNERSHIP, TARGET, AUTHORITY_KNOWLEDGE, VALUE
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING

`GENERATION_RISKS`:
- multi_character: HIGH
- handoff_interaction: HIGH
- product_historicalization: HIGH
- space_axis: MEDIUM
- product_scale_drift: MEDIUM
- text_generation: LOW

`SEEDANCE_LOCKS`:
- fictional non-magical old-world royal court
- axial hierarchy stays stable
- minimum necessary core performers
- modern product keeps exact real-world appearance

`FAILURE_PATTERNS`:
- automatic magic
- product becomes historical/fantasy redesign
- ceremonial tray/handoff intersections
- generic “everyone shocked” reaction
- excessive gold / fantasy-palace drift

---

# 4. S04｜现代美国企业办公室

## IDENTITY

- `SCENE_ID`: S04
- `NAME_ZH`: 现代美国企业办公室
- `NAME_EN`: MODERN CORPORATE OFFICE
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: WORKPLACE
- `SECONDARY_CLASS_TAGS`: TASK_PRESSURE, PROFESSIONAL_STATUS, HIERARCHY
- `ERA`: CONTEMPORARY
- `REALISM_MODE`: REALISTIC
- `BASE_VISUAL_DISTINCTIVENESS`: MEDIUM

## WORLD ENGINE

- `WORLD_ENGINE`: Deadline + 结果 + 职业体面 + 上下级 + 信息差
- `NATIVE_CONFLICT_TAGS`: DEADLINE, RESPONSIBILITY, COMPETENCE, CREDIT, AUTHORITY, INFORMATION_GAP
- `NATIVE_CONFLICT_DESCRIPTION`: 客户提前、演示失败、谁负责、谁更专业、谁拿到Credit、上下级判断被结果修正。
- `SOCIAL_RULES`: 时间即价值；结果优先；人物需要保持职业控制；层级判断可以被真实能力Proof改变。
- `POWER_STRUCTURE`: MEDIUM_VERTICAL
- `NATIVE_TIME_PRESSURE`: HIGH
- `NATIVE_INFORMATION_FLOW`: EMPLOYEE/COWORKER → MANAGER → CLIENT/EXECUTIVE
- `OBJECT_STATUS_LOGIC`: 商品价值主要由是否解决工作问题、提高效率或证明能力决定。
- `DNA_ACTIVATION_CONDITION`: 至少一个必须进入因果链：Deadline / Professional hierarchy / Client expectation / Competence judgment / Responsibility or Credit。否则只算普通Office Location。
- `SPACE_TOPOLOGY`: ROOM_NETWORK
- `CONTINUITY_ANCHORS`: meeting_room_door, primary_desk, glass_wall, client_entry, product_current_location

## COMMERCIAL ROUTING

### DECISION_FIT

- D1 空间尺寸: MEDIUM
- D2 人体适配: LOW
- D3 材质感官: LOW
- D4 性能兼容: HIGH
- D5 机制维护: HIGH
- D6 安全行为: MEDIUM
- D7 食用仪式: LOW
- D8 身份礼赠: MEDIUM
- D9 价值完整性: HIGH
- D10 安装物流: MEDIUM

### ARCHITECTURE_FIT

- SA01: HIGH
- SA02: HIGH
- SA03: MEDIUM
- SA04: HIGH
- SA05: MEDIUM
- SA06: MEDIUM
- SA07: MEDIUM
- SA08: HIGH
- SA09: MEDIUM

### PROOF_FIT

- V1 直接可见: HIGH
- V2 过程可见: HIGH
- V3 代理可见: MEDIUM
- V4 不可画面直接证明: BLOCKED_AS_PROOF

- `PROOF_MODES`: WORKFLOW_DEMO, COMPATIBILITY_TEST, DESK_USE, BEFORE_AFTER_TASK_STATE, PACKAGE_CONTENT
- `PRODUCT_ENTRY_MODES`: DESK_ITEM, WORK_BAG, DELIVERY_BOX, MEETING_DEMO, COWORKER_DISCOVERY, PROBLEM_SOLVER
- `AUDIENCE_CONSTRAINTS`: no_real_company_or_executive_identity
- `REVERSAL_COMPATIBILITY`: MEDIUM
- `SUPPORTED_REVERSAL_TYPES`: COMPETENCE, PROFESSIONAL_IDENTITY, RESPONSIBILITY, CREDIT, VALUE
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: MEDIUM
- `VISUAL_SPECTACLE_VALUE`: LOW_MEDIUM

## GENERATION ROUTING

`GENERATION_RISKS`:
- screen_text_gibberish: HIGH
- desk_asset_drift: HIGH
- glass_intersection: MEDIUM
- multi_character: MEDIUM
- handoff_interaction: MEDIUM
- space_continuity: MEDIUM

`SEEDANCE_LOCKS`:
- ordinary contemporary American corporate office
- real lived-in desk traces, not futuristic HQ
- minimum necessary core performers
- Proof shot stable and readable

`FAILURE_PATTERNS`:
- two people merely sitting and talking
- computer gibberish becomes focal
- glass/door intersections
- sitcom-style exaggerated office acting
- product appears with no work causality

---

# 5. S12｜架空复古豪华长途列车

## IDENTITY

- `SCENE_ID`: S12
- `NAME_ZH`: 架空复古豪华长途列车
- `NAME_EN`: FICTIONAL LUXURY LONG-DISTANCE TRAIN
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: CLOSED_TRANSIT
- `SECONDARY_CLASS_TAGS`: OWNERSHIP_MYSTERY, SOCIAL_HIERARCHY, TRAVEL
- `ERA`: FICTIONAL_RETRO
- `REALISM_MODE`: REALISTIC_STYLIZED
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE

- `WORLD_ENGINE`: 封闭移动 + 车厢顺序 + 物品归属 + 服务礼仪 + 下一站Deadline
- `NATIVE_CONFLICT_TAGS`: OWNERSHIP, ACCESS, PRIVACY, STATUS, MISIDENTIFICATION, INFORMATION_ASYMMETRY
- `NATIVE_CONFLICT_DESCRIPTION`: 拿错物品、送错车厢、无人认领、包厢/座位错误、下一站将到、陌生人被迫共处。
- `SOCIAL_RULES`: 人不能随时离开；空间线性；物品归属重要；Conductor/Attendant掌握空间真相；信息随人移动。
- `POWER_STRUCTURE`: LOW_MEDIUM_SERVICE_AUTHORITY
- `NATIVE_TIME_PRESSURE`: MEDIUM_HIGH
- `NATIVE_INFORMATION_FLOW`: CURRENT_CARRIAGE → ATTENDANT → ADJACENT_COMPARTMENT → PUBLIC_CAR → OWNER/AUTHORITY
- `OBJECT_STATUS_LOGIC`: 物品的位置、持有人和沿车厢移动的路径，本身就是归属与身份信息。
- `DNA_ACTIVATION_CONDITION`: 至少一个必须进入因果链：carriage order / ownership / attendant authority / next-stop pressure / object movement across compartments。否则只算豪华Train Location。
- `SPACE_TOPOLOGY`: LINEAR
- `CONTINUITY_ANCHORS`: corridor_direction, window_side, door_side, compartment_order, dining_car_direction, product_origin, product_current_location

## COMMERCIAL ROUTING

### DECISION_FIT

- D1 空间尺寸: MEDIUM
- D2 人体适配: LOW
- D3 材质感官: MEDIUM
- D4 性能兼容: MEDIUM
- D5 机制维护: LOW
- D6 安全行为: LOW
- D7 食用仪式: MEDIUM
- D8 身份礼赠: HIGH
- D9 价值完整性: MEDIUM
- D10 安装物流/便携: HIGH

### ARCHITECTURE_FIT

- SA01: MEDIUM
- SA02: LOW
- SA03: HIGH
- SA04: MEDIUM
- SA05: MEDIUM
- SA06: HIGH
- SA07: HIGH
- SA08: MEDIUM
- SA09: MEDIUM

### PROOF_FIT

- V1 直接可见: HIGH
- V2 过程可见: MEDIUM
- V3 代理可见: MEDIUM
- V4 不可画面直接证明: BLOCKED_AS_PROOF

- `PROOF_MODES`: PORTABLE_USE, OWNERSHIP_PROOF, LUGGAGE_REFERENCE, DINING_TABLE_USE, TRAVEL_ACCESS
- `PRODUCT_ENTRY_MODES`: MISDELIVERED_ITEM, LUGGAGE_REVEAL, PERSONAL_TRAVEL_ITEM, DINING_TABLE_DISCOVERY, ATTENDANT_DELIVERY, LOST_AND_FOUND
- `AUDIENCE_CONSTRAINTS`: no_real_rail_brand_route_or_highly_identifiable_train
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: OWNERSHIP, IDENTITY, PURPOSE, STATUS, DESTINATION, SOCIAL_JUDGMENT
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: MEDIUM
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING

`GENERATION_RISKS`:
- narrow_space: HIGH
- door_interaction: HIGH
- handoff_interaction: HIGH
- left_right_drift: HIGH
- multi_character: MEDIUM
- product_retro_redesign: HIGH

`SEEDANCE_LOCKS`:
- original fictional luxury train
- corridor orientation/window side/door side fixed
- outside scenery keeps subtle continuous movement
- minimum necessary core performers
- modern product stays unchanged

`FAILURE_PATTERNS`:
- carriage left/right flips
- product handoff intersections
- characters sway like a theme-park ride
- product becomes retro-designed
- scene auto-drifts into murder mystery

---

# 6. Router使用原则

1. Safety先淘汰 `BLOCKED`。
2. `DNA_ACTIVATION_CONDITION` 必须能被当前Story真正触发，否则特殊Scene降级为普通Location。
3. 静态Index只给先验；运行时仍计算具体 `Character Fit / Product Entry Fit / Generation Risk / Batch Diversity`。
4. 已确定R0/R1/R2后才看 `REVERSAL_COMPATIBILITY`；R0/R1不得因Scene支持R2而升级。
5. 比较特殊Scene与普通真实生活场景：如果特殊Scene不能明显增强商业理解、Story Architecture、Proof、Reaction或视觉区分度，则使用普通生活场景。
6. `BASE_VISUAL_DISTINCTIVENESS` 不能覆盖商业匹配度。
7. 同批Diversity Penalty应同时考虑 `PRIMARY_CLASS / SECONDARY_CLASS_TAGS / Reaction机制 / 空间类型`，不只看Scene ID是否重复。
8. 只有 `PILOT_READY` 或后续 `MIGRATED` 的结构化记录可参与完整Index评分；未迁移Scene不得因缺分被错误淘汰。