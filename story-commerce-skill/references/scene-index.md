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

允许状态：
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
- 不存静态 `Audience Fit`；具体Character/Audience Fit由Router运行时计算。
- `REVERSAL_COMPATIBILITY` 只表示Scene容得下R2，不表示本条广告应该R2；R0/R1/R2已经由 `reversal-router.md` 先确定。

## D｜GENERATION ROUTING
- `GENERATION_RISKS`
- `SEEDANCE_LOCKS`
- `FAILURE_PATTERNS`

## E｜统一评分枚举

所有静态Fit统一使用：
`BLOCKED / LOW / MEDIUM / HIGH`

运行时映射：
`BLOCKED = 淘汰`
`LOW = 0`
`MEDIUM = 1`
`HIGH = 2`

Safety BLOCKED永远高于总分。

---

# 2. Migration Status

当前12个Scene已全部完成 V1.1 结构化Index迁移。迁移只表示**路由数据标准化**，不表示Seedance实际验证通过；真实验证状态仍以 `scene-validation-registry.md` 为准。

| ID | Scene | Index Migration |
|---|---|---|
| S01 | 架空古装宫廷 | MIGRATED |
| S02 | 现代美国高中 | MIGRATED |
| S03 | 架空古代战争军营 | MIGRATED |
| S04 | 现代美国企业办公室 | MIGRATED |
| S05 | 架空美国西部边疆贸易小镇 | MIGRATED |
| S06 | 架空现代豪华上流晚宴 | MIGRATED |
| S07 | 现代美国大型购物中心 | MIGRATED |
| S08 | 架空未来都市·星际商业世界 | MIGRATED |
| S09 | 架空复古美国公路Diner | MIGRATED |
| S10 | 架空高压真人竞赛节目 | MIGRATED |
| S11 | 架空古代地中海公共市集 | MIGRATED |
| S12 | 架空复古豪华长途列车 | MIGRATED |

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
- `SOCIAL_RULES`: 接近、发言、递交、触碰、打断受身份与礼仪限制；错误会被公开看见。
- `POWER_STRUCTURE`: HIGH
- `NATIVE_TIME_PRESSURE`: LOW
- `NATIVE_INFORMATION_FLOW`: LOWER_ROLE → STEWARD/AUTHORITY → RULER → COURT_REACTION
- `OBJECT_STATUS_LOGIC`: 普通商品一旦进入正式呈递程序，会获得礼仪、身份或权威意义。
- `DNA_ACTIVATION_CONDITION`: 礼仪许可 / 等级判断 / 公开呈递 / 权威裁决 / 身份权限至少一项进入因果链；否则仅算古装Location。
- `SPACE_TOPOLOGY`: AXIAL
- `CONTINUITY_ANCHORS`: central_axis, raised_authority_position, ceremonial_entry, presentation_point, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 LOW, D2 MEDIUM, D3 MEDIUM, D4 MEDIUM, D5 LOW, D6 LOW, D7 MEDIUM, D8 HIGH, D9 HIGH, D10 LOW
- `ARCHITECTURE_FIT`: SA01 LOW, SA02 MEDIUM, SA03 HIGH, SA04 LOW, SA05 MEDIUM, SA06 MEDIUM, SA07 HIGH, SA08 HIGH, SA09 MEDIUM
- `PROOF_FIT`: V1 HIGH, V2 MEDIUM, V3 MEDIUM, V4 BLOCKED
- `PROOF_MODES`: PUBLIC_PRESENTATION, WORN_USE, HANDLED_INSPECTION, AUTHORITY_VERIFICATION, PACKAGE_CONTENT
- `PRODUCT_ENTRY_MODES`: TRIBUTE_ENTRY, WORN_ENTRY, DEMONSTRATION_ENTRY, LARGE_OBJECT_ENTRY
- `AUDIENCE_CONSTRAINTS`: no_real_royal_family_or_state_identity
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: IDENTITY, STATUS, OWNERSHIP, TARGET, AUTHORITY_KNOWLEDGE, VALUE
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: multi_character HIGH; handoff_interaction HIGH; product_historicalization HIGH; space_axis MEDIUM; product_scale_drift MEDIUM
- `SEEDANCE_LOCKS`: fictional non-magical old-world court; axial hierarchy stable; minimum necessary performers; modern product unchanged
- `FAILURE_PATTERNS`: automatic magic; product historical/fantasy redesign; tray/handoff intersections; generic everyone-shocked reaction; fantasy-palace drift

---

# 4. S02｜现代美国高中

## IDENTITY
- `SCENE_ID`: S02
- `NAME_ZH`: 现代美国高中
- `NAME_EN`: MODERN AMERICAN HIGH SCHOOL
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: PEER_SOCIAL
- `SECONDARY_CLASS_TAGS`: PUBLIC_JUDGMENT, SCHOOL_RULES, TIME_PRESSURE
- `ERA`: CONTEMPORARY
- `REALISM_MODE`: REALISTIC
- `BASE_VISUAL_DISTINCTIVENESS`: MEDIUM

## WORLD ENGINE
- `WORLD_ENGINE`: 同伴评价 + 群体归属 + 公开尴尬 + 课堂规则 + 时间压力
- `NATIVE_CONFLICT_TAGS`: PEER_JUDGMENT, EMBARRASSMENT, GROUP_BELONGING, TEACHER_AUTHORITY, DEADLINE, WRONG_BLAME
- `NATIVE_CONFLICT_DESCRIPTION`: 迟到、被点名、课堂展示、圈层判断、老师误判、同伴公开评价会迅速扩散。
- `SOCIAL_RULES`: 同龄人快速注意异常；老师有局部规则权；铃声与换课制造时间压力。
- `POWER_STRUCTURE`: MEDIUM
- `NATIVE_TIME_PRESSURE`: HIGH
- `NATIVE_INFORMATION_FLOW`: STUDENT/FRIEND → PEERS → TEACHER/STAFF → GROUP_REACTION
- `OBJECT_STATUS_LOGIC`: 商品会因谁拥有、谁先使用、谁公开评价而获得社交意义。
- `DNA_ACTIVATION_CONDITION`: 同伴公开判断 / Teacher rule / Classroom demo / Public embarrassment / Bell deadline至少一项进入因果链；否则只算School Location。
- `SPACE_TOPOLOGY`: CORRIDOR_CLASSROOM_NETWORK
- `CONTINUITY_ANCHORS`: locker_bank, corridor_direction, classroom_door, primary_desk, teacher_position, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 HIGH, D3 MEDIUM, D4 MEDIUM, D5 LOW, D6 LOW, D7 MEDIUM, D8 HIGH, D9 MEDIUM, D10 LOW
- `ARCHITECTURE_FIT`: SA01 MEDIUM, SA02 MEDIUM, SA03 HIGH, SA04 MEDIUM, SA05 MEDIUM, SA06 MEDIUM, SA07 HIGH, SA08 MEDIUM, SA09 HIGH
- `PROOF_FIT`: V1 HIGH, V2 MEDIUM, V3 HIGH, V4 BLOCKED
- `PROOF_MODES`: WORN_USE, BACKPACK_REFERENCE, CLASS_DEMO, DESK_USE, PEER_VERIFICATION
- `PRODUCT_ENTRY_MODES`: BACKPACK, WORN, LOCKER_REVEAL, DESK, CLASS_DEMO, CAFETERIA
- `AUDIENCE_CONSTRAINTS`: 18_plus_adult_actors_as_seniors; BLOCK adult_medicine_weight_loss_alcohol_tobacco_gambling_adult_sexual_products_weapons
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: ABILITY, IDENTITY, OWNERSHIP, PURPOSE, SOCIAL_STATUS, RESULT
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: MEDIUM

## GENERATION ROUTING
- `GENERATION_RISKS`: background_crowd HIGH; locker_bag_interaction HIGH; age_ambiguity HIGH; character_identity_drift MEDIUM; school_space_drift MEDIUM
- `SEEDANCE_LOCKS`: generic contemporary American public high school; adult performers; background crowd subdued; Proof shot stable
- `FAILURE_PATTERNS`: teen/age ambiguity; Disney-style glamorization; locker/backpack intersections; background student deformation; peer reaction becomes synchronized mob

---

# 5. S03｜架空古代战争军营

## IDENTITY
- `SCENE_ID`: S03
- `NAME_ZH`: 架空古代战争军营
- `NAME_EN`: FICTIONAL ANCIENT CAMPAIGN WAR CAMP
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: TASK_PRESSURE
- `SECONDARY_CLASS_TAGS`: COMMAND_HIERARCHY, SUPPLY_LOGISTICS, RESOURCE_SCARCITY
- `ERA`: FICTIONAL_ANCIENT
- `REALISM_MODE`: NON_MAGICAL_STYLIZED_HISTORY
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE
- `WORLD_ENGINE`: 任务 + 命令链 + 时间压力 + 资源有限 + 信息不完整
- `NATIVE_CONFLICT_TAGS`: DEADLINE, COMMAND, SUPPLY_FAILURE, RESPONSIBILITY, INFORMATION_GAP, RESOURCE_LIMIT
- `NATIVE_CONFLICT_DESCRIPTION`: 命令变化、补给不足、情报错误、任务Deadline、谁负责、方案失败。
- `SOCIAL_RULES`: 任务优先；命令必须执行；资源有限；上级判断可被实际Proof纠正。
- `POWER_STRUCTURE`: HIGH
- `NATIVE_TIME_PRESSURE`: HIGH
- `NATIVE_INFORMATION_FLOW`: COMMANDER → OFFICER/QUARTERMASTER → MESSENGER/SOLDIER → FIELD_FEEDBACK
- `OBJECT_STATUS_LOGIC`: 商品只有进入任务、补给或执行链，才会被视为有战略价值的资源。
- `DNA_ACTIVATION_CONDITION`: Command / Supply / Deadline / Mission / Resource constraint至少一项进入因果链；否则只算古代Camp Location。
- `SPACE_TOPOLOGY`: COMMAND_HUB_AND_FIELD_PATH
- `CONTINUITY_ANCHORS`: tent_entrance, command_table, map_position, supply_area, exterior_route, product_origin

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 LOW, D3 LOW, D4 HIGH, D5 HIGH, D6 MEDIUM, D7 LOW, D8 LOW, D9 MEDIUM, D10 HIGH
- `ARCHITECTURE_FIT`: SA01 HIGH, SA02 HIGH, SA03 MEDIUM, SA04 HIGH, SA05 MEDIUM, SA06 MEDIUM, SA07 MEDIUM, SA08 MEDIUM, SA09 LOW
- `PROOF_FIT`: V1 HIGH, V2 HIGH, V3 LOW, V4 BLOCKED
- `PROOF_MODES`: FIELD_DEMO, TASK_COMPLETION, SUPPLY_CHECK, COMPATIBILITY_TEST, PACKING_LOGISTICS
- `PRODUCT_ENTRY_MODES`: SUPPLY_CRATE, PERSONAL_GEAR, EMERGENCY_DELIVERY, FIELD_DEMONSTRATION, QUARTERMASTER_INVENTORY
- `AUDIENCE_CONSTRAINTS`: no_real_military_identity; no_weapon_products
- `REVERSAL_COMPATIBILITY`: MEDIUM
- `SUPPORTED_REVERSAL_TYPES`: ABILITY, STRATEGIC_VALUE, IDENTITY, PURPOSE, RESULT, COMMAND_TARGET
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: automatic_combat HIGH; weapon_intrusion HIGH; product_historicalization HIGH; multi_character HIGH; symbol_hallucination HIGH; tent_space_drift MEDIUM
- `SEEDANCE_LOCKS`: pre-battle command camp; no active combat; war feeling from tent/map/supply/messenger; modern product unchanged
- `FAILURE_PATTERNS`: auto-battle; weapons dominate frame; real-looking military symbols; product ancient redesign; crowd face collapse

---

# 6. S04｜现代美国企业办公室

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
- `SOCIAL_RULES`: 时间即价值；结果优先；人物需要保持职业控制；层级判断可被真实Proof改变。
- `POWER_STRUCTURE`: MEDIUM
- `NATIVE_TIME_PRESSURE`: HIGH
- `NATIVE_INFORMATION_FLOW`: EMPLOYEE/COWORKER → MANAGER → CLIENT/EXECUTIVE
- `OBJECT_STATUS_LOGIC`: 商品价值主要由是否解决工作问题、提高效率或证明能力决定。
- `DNA_ACTIVATION_CONDITION`: Deadline / Professional hierarchy / Client expectation / Competence judgment / Responsibility or Credit至少一项进入因果链；否则只算Office Location。
- `SPACE_TOPOLOGY`: ROOM_NETWORK
- `CONTINUITY_ANCHORS`: meeting_room_door, primary_desk, glass_wall, client_entry, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 LOW, D3 LOW, D4 HIGH, D5 HIGH, D6 MEDIUM, D7 LOW, D8 MEDIUM, D9 HIGH, D10 MEDIUM
- `ARCHITECTURE_FIT`: SA01 HIGH, SA02 HIGH, SA03 MEDIUM, SA04 HIGH, SA05 MEDIUM, SA06 MEDIUM, SA07 MEDIUM, SA08 HIGH, SA09 MEDIUM
- `PROOF_FIT`: V1 HIGH, V2 HIGH, V3 MEDIUM, V4 BLOCKED
- `PROOF_MODES`: WORKFLOW_DEMO, COMPATIBILITY_TEST, DESK_USE, BEFORE_AFTER_TASK_STATE, PACKAGE_CONTENT
- `PRODUCT_ENTRY_MODES`: DESK_ITEM, WORK_BAG, DELIVERY_BOX, MEETING_DEMO, COWORKER_DISCOVERY, PROBLEM_SOLVER
- `AUDIENCE_CONSTRAINTS`: no_real_company_or_executive_identity
- `REVERSAL_COMPATIBILITY`: MEDIUM
- `SUPPORTED_REVERSAL_TYPES`: COMPETENCE, PROFESSIONAL_IDENTITY, RESPONSIBILITY, CREDIT, VALUE
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: MEDIUM
- `VISUAL_SPECTACLE_VALUE`: LOW

## GENERATION ROUTING
- `GENERATION_RISKS`: screen_text_gibberish HIGH; desk_asset_drift HIGH; glass_intersection MEDIUM; multi_character MEDIUM; handoff_interaction MEDIUM; space_continuity MEDIUM
- `SEEDANCE_LOCKS`: ordinary contemporary American office; lived-in desk traces; minimum necessary performers; Proof shot stable
- `FAILURE_PATTERNS`: two people merely talking; computer gibberish focal; glass/door intersections; exaggerated sitcom acting; product with no work causality

---

# 7. S05｜架空美国西部边疆贸易小镇

## IDENTITY
- `SCENE_ID`: S05
- `NAME_ZH`: 架空美国西部边疆贸易小镇
- `NAME_EN`: FICTIONAL AMERICAN FRONTIER TRADING TOWN
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: PRACTICAL_PUBLIC_JUDGMENT
- `SECONDARY_CLASS_TAGS`: FRONTIER_TRADING, REPUTATION, LIVE_TEST
- `ERA`: FICTIONAL_FRONTIER
- `REALISM_MODE`: NON_MAGICAL_STYLIZED_HISTORY
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE
- `WORLD_ENGINE`: 陌生人 + 名声 + 公开交易 + 实用主义判断
- `NATIVE_CONFLICT_TAGS`: REPUTATION, TRUST, VALUE, NEWCOMER_STATUS, PUBLIC_CHALLENGE, PRACTICAL_TEST
- `NATIVE_CONFLICT_DESCRIPTION`: 谁可信、新货值不值、外来者被低估、老办法与新办法竞争、公开质疑。
- `SOCIAL_RULES`: 名声即信用；少说多做；好不好现场试；陌生人进入即被判断。
- `POWER_STRUCTURE`: LOW
- `NATIVE_TIME_PRESSURE`: LOW
- `NATIVE_INFORMATION_FLOW`: NEWCOMER/STOREKEEPER → LOCAL_OBSERVER → STREET_REACTION
- `OBJECT_STATUS_LOGIC`: Claim没有价值，现场实用测试结果才决定商品与人物信誉。
- `DNA_ACTIVATION_CONDITION`: Public challenge / Trade judgment / Live practical test / Newcomer reputation至少一项进入因果链；否则只算Western Location。
- `SPACE_TOPOLOGY`: MAIN_STREET_LINEAR
- `CONTINUITY_ANCHORS`: store_door, counter, boardwalk_side, public_test_area, observer_positions, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 MEDIUM, D3 MEDIUM, D4 HIGH, D5 HIGH, D6 MEDIUM, D7 MEDIUM, D8 MEDIUM, D9 HIGH, D10 MEDIUM
- `ARCHITECTURE_FIT`: SA01 HIGH, SA02 HIGH, SA03 MEDIUM, SA04 MEDIUM, SA05 HIGH, SA06 MEDIUM, SA07 HIGH, SA08 HIGH, SA09 MEDIUM
- `PROOF_FIT`: V1 HIGH, V2 HIGH, V3 MEDIUM, V4 BLOCKED
- `PROOF_MODES`: PUBLIC_PRACTICAL_TEST, HANDLED_INSPECTION, COMPARISON, WORK_USE, SIZE_REFERENCE
- `PRODUCT_ENTRY_MODES`: STAGECOACH_DELIVERY, GENERAL_STORE_NEW_ARRIVAL, TRAVELER_PERSONAL_ITEM, TRADE_OFFER, WORK_PROBLEM_SOLVER
- `AUDIENCE_CONSTRAINTS`: no_weapon_products; no_indigenous_stereotypes_or_real_western_figures
- `REVERSAL_COMPATIBILITY`: MEDIUM
- `SUPPORTED_REVERSAL_TYPES`: ABILITY, REPUTATION, EXPERTISE, VALUE, OWNERSHIP, CROWD_POSITION
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: automatic_gunfight HIGH; product_westernization HIGH; dust_overload MEDIUM; crowd_drift MEDIUM; handoff_interaction MEDIUM
- `SEEDANCE_LOCKS`: weathered working frontier trading town; no gunfight; practical public testing; modern product unchanged
- `FAILURE_PATTERNS`: guns appear; theme-park western; identical cowboy costumes; product historical redesign; crowd teleportation

---

# 8. S06｜架空现代豪华上流晚宴

## IDENTITY
- `SCENE_ID`: S06
- `NAME_ZH`: 架空现代豪华上流晚宴
- `NAME_EN`: FICTIONAL HIGH-SOCIETY GRAND GALA
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: SOCIAL_STATUS
- `SECONDARY_CLASS_TAGS`: ATTENTION_ECONOMY, GIFTING, ETIQUETTE
- `ERA`: CONTEMPORARY_FICTIONAL
- `REALISM_MODE`: REALISTIC_STYLIZED
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE
- `WORLD_ENGINE`: 身份判断 + 品味 + 公开注视 + 社交体面 + Host认可
- `NATIVE_CONFLICT_TAGS`: STATUS, ETIQUETTE, ATTENTION, EXCLUSION, TASTE, SOCIAL_ACCEPTANCE
- `NATIVE_CONFLICT_DESCRIPTION`: 谁被邀请、谁被介绍、谁坐哪里、谁被忽略、谁犯礼仪错误、谁突然成为焦点。
- `SOCIAL_RULES`: 外表即信息；注意力是社交货币；人物看见但假装没看；攻击和怀疑保持礼貌。
- `POWER_STRUCTURE`: MEDIUM
- `NATIVE_TIME_PRESSURE`: LOW
- `NATIVE_INFORMATION_FLOW`: NEW_ARRIVAL/GUEST → TABLE_REACTION → HOST → WIDER_SOCIAL_ACCEPTANCE
- `OBJECT_STATUS_LOGIC`: 商品通过佩戴、礼赠、Host注意或社交反应获得品味与身份意义。
- `DNA_ACTIVATION_CONDITION`: Host recognition / Etiquette / Attention shift / Gift-social meaning / Silent exclusion至少一项进入因果链；否则只算Luxury Event Location。
- `SPACE_TOPOLOGY`: SOCIAL_FOCAL_ROOM
- `CONTINUITY_ANCHORS`: event_entrance, host_position, primary_table, social_focal_zone, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 LOW, D2 HIGH, D3 HIGH, D4 LOW, D5 LOW, D6 LOW, D7 HIGH, D8 HIGH, D9 HIGH, D10 LOW
- `ARCHITECTURE_FIT`: SA01 LOW, SA02 MEDIUM, SA03 HIGH, SA04 LOW, SA05 MEDIUM, SA06 MEDIUM, SA07 HIGH, SA08 HIGH, SA09 HIGH
- `PROOF_FIT`: V1 HIGH, V2 MEDIUM, V3 HIGH, V4 BLOCKED
- `PROOF_MODES`: WORN_USE, GIFT_REVEAL, MATERIAL_CLOSEUP, SOCIAL_REACTION_PROXY, PACKAGE_CONTENT
- `PRODUCT_ENTRY_MODES`: WORN, GIFT_BOX, PERSONAL_ITEM, TABLE_DISCOVERY, PUBLIC_DEMONSTRATION, ACCIDENT_SOLVER
- `AUDIENCE_CONSTRAINTS`: no_real_gala_charity_luxury_brand_or_celebrity_identity
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: IDENTITY, TASTE, ATTENTION, OWNERSHIP, EXPERTISE, SOCIAL_ACCEPTANCE
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: MEDIUM
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: multi_character HIGH; synchronized_crowd_reaction HIGH; fashion_shoot_drift HIGH; product_luxury_redesign HIGH; handoff_interaction MEDIUM
- `SEEDANCE_LOCKS`: private fictional gala; diverse adult guests; restrained luxury; distributed reactions; product unchanged
- `FAILURE_PATTERNS`: auto-red-carpet; collective head-turn; static fashion shoot; real-brand imitation; product becomes luxury fantasy redesign

---

# 9. S07｜现代美国大型购物中心

## IDENTITY
- `SCENE_ID`: S07
- `NAME_ZH`: 现代美国大型购物中心
- `NAME_EN`: MODERN AMERICAN SHOPPING MALL
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: CONSUMER_CHOICE
- `SECONDARY_CLASS_TAGS`: RETAIL_FLOW, COMPARISON, SOCIAL_PROOF
- `ERA`: CONTEMPORARY
- `REALISM_MODE`: REALISTIC
- `BASE_VISUAL_DISTINCTIVENESS`: MEDIUM

## WORLD ENGINE
- `WORLD_ENGINE`: 注意力竞争 + 比较 + 试用 + 选择 + 社会影响
- `NATIVE_CONFLICT_TAGS`: CHOICE, COMPARISON, ATTENTION, FRIEND_OPINION, SOCIAL_PROOF, DECISION_FATIGUE
- `NATIVE_CONFLICT_DESCRIPTION`: 去哪家、选哪个、朋友意见冲突、买不买、谁推荐错、试用后改选。
- `SOCIAL_RULES`: 比较和试用天然合法；消费者拥有选择权；陌生人Reaction可形成社会证明。
- `POWER_STRUCTURE`: LOW
- `NATIVE_TIME_PRESSURE`: LOW
- `NATIVE_INFORMATION_FLOW`: SHOPPER/FRIEND → ASSOCIATE/OTHER_SHOPPER → LOCAL_SOCIAL_PROOF
- `OBJECT_STATUS_LOGIC`: 商品价值在并列选择、试用和重新拿起/放回的过程中被判断。
- `DNA_ACTIVATION_CONDITION`: Discovery / Comparison / Try-on or Demo / Shopper flow interruption / Decision change至少一项进入因果链；否则只算Mall Location。
- `SPACE_TOPOLOGY`: FLOW_NETWORK
- `CONTINUITY_ANCHORS`: primary_storefront, display_zone, aisle_direction, demo_or_try_area, shopper_route, product_origin

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 HIGH, D3 HIGH, D4 HIGH, D5 MEDIUM, D6 LOW, D7 MEDIUM, D8 HIGH, D9 HIGH, D10 MEDIUM
- `ARCHITECTURE_FIT`: SA01 MEDIUM, SA02 HIGH, SA03 MEDIUM, SA04 MEDIUM, SA05 HIGH, SA06 HIGH, SA07 MEDIUM, SA08 HIGH, SA09 HIGH
- `PROOF_FIT`: V1 HIGH, V2 HIGH, V3 HIGH, V4 BLOCKED
- `PROOF_MODES`: TRY_ON, DEMO, SIDE_BY_SIDE_COMPARISON, SIZE_REFERENCE, MATERIAL_INSPECTION, SOCIAL_REACTION_PROXY
- `PRODUCT_ENTRY_MODES`: DISPLAY_DISCOVERY, SHOPPER_PERSONAL_ITEM, FRIEND_RECOMMENDATION, TRY_ON_OR_DEMO, POP_UP, SHOPPING_BAG, PROBLEM_SOLVER
- `AUDIENCE_CONSTRAINTS`: generic_storefronts_only; no_unverified_promotion_or_partnership
- `REVERSAL_COMPATIBILITY`: MEDIUM
- `SUPPORTED_REVERSAL_TYPES`: CHOICE, EXPERTISE, FRIEND_JUDGMENT, SOCIAL_PROOF, VALUE, RESULT
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: MEDIUM
- `VISUAL_SPECTACLE_VALUE`: MEDIUM

## GENERATION ROUTING
- `GENERATION_RISKS`: logo_hallucination HIGH; crowd_intersection HIGH; product_replication HIGH; mall_airport_drift MEDIUM; try_on_interaction HIGH; storefront_continuity MEDIUM
- `SEEDANCE_LOCKS`: bright contemporary American lifestyle mall; generic storefronts; controlled crowd; stable demo/try-on shot
- `FAILURE_PATTERNS`: real logos; mall becomes airport; infinite product copies; passerby teleportation; crowd collision; fake sale signs

---

# 10. S08｜架空未来都市·星际商业世界

## IDENTITY
- `SCENE_ID`: S08
- `NAME_ZH`: 架空未来都市·星际商业世界
- `NAME_EN`: FICTIONAL INTERPLANETARY COMMERCE METROPOLIS
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: SYSTEM_CLASSIFICATION
- `SECONDARY_CLASS_TAGS`: FUTURE_COMMERCE, PERMISSION, AUTOMATION
- `ERA`: FICTIONAL_FUTURE
- `REALISM_MODE`: FUNCTIONAL_SCI_FI
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE
- `WORLD_ENGINE`: 系统分类 + 身份权限 + 兼容 + 效率 + 人工复核
- `NATIVE_CONFLICT_TAGS`: CLASSIFICATION, PERMISSION, COMPATIBILITY, AUTOMATION_FAILURE, CARGO_ERROR, HUMAN_OVERRIDE
- `NATIVE_CONFLICT_DESCRIPTION`: 过检失败、权限错误、物流发错、系统误判、新旧技术不兼容、自动化异常。
- `SOCIAL_RULES`: 一切被识别和分类；系统有权威；真实Proof允许人工Override。
- `POWER_STRUCTURE`: SYSTEM_HIGH_HUMAN_OVERRIDE
- `NATIVE_TIME_PRESSURE`: MEDIUM
- `NATIVE_INFORMATION_FLOW`: SYSTEM_RESULT → STAFF/INSPECTOR → MANUAL_CHECK → OVERRIDE/RESUME
- `OBJECT_STATUS_LOGIC`: 商品通过系统分类结果与人工复核之间的差异获得故事意义，但世界技术不得成为商品功能。
- `DNA_ACTIVATION_CONDITION`: Scan/classification / Permission / Compatibility / System error / Human override至少一项进入因果链；否则只算Future Location。
- `SPACE_TOPOLOGY`: CHECKPOINT_FLOW
- `CONTINUITY_ANCHORS`: scan_station, gate, cargo_lane, manual_inspection_point, route_direction, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 LOW, D3 MEDIUM, D4 HIGH, D5 HIGH, D6 MEDIUM, D7 LOW, D8 MEDIUM, D9 MEDIUM, D10 HIGH
- `ARCHITECTURE_FIT`: SA01 MEDIUM, SA02 HIGH, SA03 HIGH, SA04 HIGH, SA05 MEDIUM, SA06 HIGH, SA07 MEDIUM, SA08 MEDIUM, SA09 LOW
- `PROOF_FIT`: V1 HIGH, V2 HIGH, V3 MEDIUM, V4 BLOCKED
- `PROOF_MODES`: COMPATIBILITY_TEST, MANUAL_INSPECTION, CLASSIFICATION_RESULT, CARGO_CHECK, ACTUAL_USE
- `PRODUCT_ENTRY_MODES`: INSPECTION_ITEM, CARGO_DELIVERY, OLD_EARTH_PERSONAL_ITEM, COMMERCE_DISPLAY, DAILY_USE, SYSTEM_CANNOT_CLASSIFY
- `AUDIENCE_CONSTRAINTS`: no_real_sci_fi_IP; WORLD_TECH_NEVER_PRODUCT_FACT
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: CLASSIFICATION, PERMISSION, TECH_VALUE, HUMAN_EXPERTISE, SYSTEM_OVERRIDE, OWNERSHIP
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: product_futurization HIGH; HUD_text_gibberish HIGH; world_tech_product_contamination HIGH; robot_clutter HIGH; pseudo_science_dialogue HIGH; environment_effects_occlusion MEDIUM
- `SEEDANCE_LOCKS`: bright lived-in human future commerce; HUD never blocks product; world tech separate from product; minimum necessary actors
- `FAILURE_PATTERNS`: automatic cyberpunk; product glows or gains AI; fake scanning claims; excessive robots; effects cover product; science gibberish

---

# 11. S09｜架空复古美国公路Diner

## IDENTITY
- `SCENE_ID`: S09
- `NAME_ZH`: 架空复古美国公路Diner
- `NAME_EN`: FICTIONAL MID-CENTURY AMERICAN ROADSIDE DINER
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: INFORMATION_SPREAD
- `SECONDARY_CLASS_TAGS`: LOCAL_SOCIAL, OVERHEARD_COMEDY, HOSPITALITY
- `ERA`: FICTIONAL_MID_CENTURY
- `REALISM_MODE`: REALISTIC_STYLIZED
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE
- `WORLD_ENGINE`: 空间距离近 + 熟客关系 + 陌生人进入 + 误听 + 横向信息传播
- `NATIVE_CONFLICT_TAGS`: OVERHEARD_INFO, MISUNDERSTANDING, NEWCOMER, WRONG_TABLE, SERVER_ROUTING, LOCAL_OPINION
- `NATIVE_CONFLICT_DESCRIPTION`: 上错餐、坐错位置、隔桌插话、服务员听错、陌生旅客被误解、熟客判断错。
- `SOCIAL_RULES`: 私聊容易被听见；Server跨人群移动，是天然Information Router；熟客自然插话。
- `POWER_STRUCTURE`: LOW
- `NATIVE_TIME_PRESSURE`: LOW
- `NATIVE_INFORMATION_FLOW`: BOOTH/TABLE → SERVER → COUNTER/REGULARS → WIDER_DINER
- `OBJECT_STATUS_LOGIC`: 商品的意义会因半句话、隔桌观察、Server转述和熟客判断在短距离内传播和改变。
- `DNA_ACTIVATION_CONDITION`: Overheard info / Server relay / Regular interruption / Wrong table assumption至少一项进入因果链；否则只算Diner Location。
- `SPACE_TOPOLOGY`: DUAL_ZONE_BOOTH_COUNTER
- `CONTINUITY_ANCHORS`: counter_side, primary_booth, entrance, server_path, kitchen_direction, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 LOW, D2 MEDIUM, D3 HIGH, D4 MEDIUM, D5 LOW, D6 LOW, D7 HIGH, D8 MEDIUM, D9 MEDIUM, D10 MEDIUM
- `ARCHITECTURE_FIT`: SA01 MEDIUM, SA02 MEDIUM, SA03 HIGH, SA04 LOW, SA05 MEDIUM, SA06 HIGH, SA07 HIGH, SA08 MEDIUM, SA09 HIGH
- `PROOF_FIT`: V1 HIGH, V2 MEDIUM, V3 HIGH, V4 BLOCKED
- `PROOF_MODES`: TABLE_USE, MATERIAL_OR_FOOD_PROXY, PERSONAL_ITEM_REVEAL, SMALL_PROBLEM_SOLVE, SOCIAL_REACTION_PROXY
- `PRODUCT_ENTRY_MODES`: TRAVELER_BAG, TABLE_PERSONAL_ITEM, NEW_DELIVERY, SERVER_DISCOVERY, NEIGHBOR_NOTICES, SMALL_PROBLEM_SOLVER
- `AUDIENCE_CONSTRAINTS`: adult_inclusive_cast; no_real_diner_or_beverage_brand; no_segregation_nostalgia
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: MISUNDERSTANDING, IDENTITY, RELATIONSHIP, PURPOSE, KNOWLEDGE, SOCIAL_JUDGMENT
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: MEDIUM

## GENERATION ROUTING
- `GENERATION_RISKS`: liquid_handling HIGH; tray_handoff HIGH; synchronized_reaction HIGH; product_retro_redesign HIGH; real_logo_hallucination HIGH
- `SEEDANCE_LOCKS`: compact lived-in roadside diner; booth/counter relation fixed; product remains modern; reactions spread laterally not simultaneously
- `FAILURE_PATTERNS`: theme-park nostalgia; real logos; everybody turns together; coffee/tray intersections; product becomes 1950s redesign

---

# 12. S10｜架空高压真人竞赛节目

## IDENTITY
- `SCENE_ID`: S10
- `NAME_ZH`: 架空高压真人竞赛节目
- `NAME_EN`: FICTIONAL HIGH-STAKES COMPETITION SHOW
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: COMPETITION
- `SECONDARY_CLASS_TAGS`: RULED_TASK, PUBLIC_RESULT, TIME_PRESSURE
- `ERA`: CONTEMPORARY_FICTIONAL
- `REALISM_MODE`: STYLIZED_REALITY_SHOW
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE
- `WORLD_ENGINE`: 明确规则 + 时间压力 + 公开执行 + 可见输赢
- `NATIVE_CONFLICT_TAGS`: RULE, COUNTDOWN, PERFORMANCE, MISREAD_RULE, RESULT, JUDGE_REVIEW
- `NATIVE_CONFLICT_DESCRIPTION`: 谁先完成、谁理解错规则、谁落后、提前庆祝、黑马领先、裁判复核。
- `SOCIAL_RULES`: Claim不算数直到测试；规则公开；结果必须一眼可见；Host控制开始/停止/确认。
- `POWER_STRUCTURE`: MEDIUM
- `NATIVE_TIME_PRESSURE`: HIGH
- `NATIVE_INFORMATION_FLOW`: HOST/RULE → CONTESTANTS → RESULT → JUDGE/HOST_CONFIRM → AUDIENCE
- `OBJECT_STATUS_LOGIC`: 商品只有进入公平、可观察、与真实卖点对应的任务，才能成为比赛工具或结果证据。
- `DNA_ACTIVATION_CONDITION`: Fair rule / Visible task / Countdown or result / Host or judge confirmation至少一项进入因果链；否则只算Game-show Location。
- `SPACE_TOPOLOGY`: FIXED_STAGE_LANES
- `CONTINUITY_ANCHORS`: host_position, lane_A, lane_B, task_table, result_zone, product_A_position, product_B_position

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 HIGH, D2 MEDIUM, D3 LOW, D4 HIGH, D5 HIGH, D6 LOW, D7 LOW, D8 LOW, D9 MEDIUM, D10 HIGH
- `ARCHITECTURE_FIT`: SA01 MEDIUM, SA02 HIGH, SA03 MEDIUM, SA04 HIGH, SA05 HIGH, SA06 MEDIUM, SA07 MEDIUM, SA08 MEDIUM, SA09 LOW
- `PROOF_FIT`: V1 HIGH, V2 HIGH, V3 LOW, V4 BLOCKED
- `PROOF_MODES`: FAIR_VISIBLE_TASK, SIDE_BY_SIDE_RESULT, SPEED_OR_COMPLETION_WHEN_VERIFIED, SIZE_OR_FIT_TEST, ASSEMBLY_OR_OPERATION_TEST
- `PRODUCT_ENTRY_MODES`: ASSIGNED_TOOL, PERSONAL_ADVANTAGE, MYSTERY_REVEAL, CHOICE_ROUND, RESCUE_ITEM, FINAL_ROUND_PRODUCT
- `AUDIENCE_CONSTRAINTS`: no_gambling_lottery_dangerous_challenge; no_unverified_metrics_or_superiority_claims
- `REVERSAL_COMPATIBILITY`: MEDIUM
- `SUPPORTED_REVERSAL_TYPES`: UNDERDOG_RESULT, CONFIDENCE, RULE_INTERPRETATION, TOOL, PERFORMANCE, WIN_LOSE
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: LED_text_gibberish HIGH; parallel_action HIGH; multi_character HIGH; unfair_test_logic HIGH; hallucinated_metrics HIGH; show_IP_imitation HIGH
- `SEEDANCE_LOCKS`: original challenge arena; fixed Host/A/B positions; independent clear Result Shot; only verified short-term visible tasks
- `FAILURE_PATTERNS`: copied real show; fake score text; challenge not tied to product fact; parallel-action intersections; unclear result; invented performance percentages

---

# 13. S11｜架空古代地中海公共市集

## IDENTITY
- `SCENE_ID`: S11
- `NAME_ZH`: 架空古代地中海公共市集
- `NAME_EN`: FICTIONAL ANCIENT MEDITERRANEAN MARKETPLACE
- `STATUS`: TESTING_CANDIDATE
- `PRIMARY_CLASS`: PUBLIC_MARKET
- `SECONDARY_CLASS_TAGS`: NEGOTIATION, REPUTATION, CROWD_JUDGMENT
- `ERA`: FICTIONAL_ANCIENT_MEDITERRANEAN
- `REALISM_MODE`: NON_MAGICAL_STYLIZED_HISTORY
- `BASE_VISUAL_DISTINCTIVENESS`: HIGH

## WORLD ENGINE
- `WORLD_ENGINE`: 公开叫卖 + 讨价还价 + 商人竞争 + 信誉 + 群众判断
- `NATIVE_CONFLICT_TAGS`: PRICE_VALUE, RIVALRY, REPUTATION, PUBLIC_CLAIM, PUBLIC_CHALLENGE, CROWD_JUDGMENT
- `NATIVE_CONFLICT_DESCRIPTION`: 争客、砍价、称量争议、外来商人被怀疑、Rival拆台、信誉争议。
- `SOCIAL_RULES`: 卖东西是公开表演；Claim会被当众挑战；信任靠亲手检查、公开演示和群众Reaction。
- `POWER_STRUCTURE`: LOW
- `NATIVE_TIME_PRESSURE`: LOW
- `NATIVE_INFORMATION_FLOW`: MERCHANT/BUYER → RIVAL → CROWD → PURCHASE_DECISION
- `OBJECT_STATUS_LOGIC`: 商品价值和商人信誉通过公开Claim、挑战、演示与群众改判形成。
- `DNA_ACTIVATION_CONDITION`: Public claim / Bargain / Rival challenge / Public demo / Crowd judgment至少一项进入因果链；否则只算Ancient Market Location。
- `SPACE_TOPOLOGY`: OPEN_MARKET_CLUSTER
- `CONTINUITY_ANCHORS`: main_stall, merchant_position, buyer_position, rival_position, crowd_semicircle, product_display_area

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 MEDIUM, D3 HIGH, D4 HIGH, D5 MEDIUM, D6 LOW, D7 HIGH, D8 MEDIUM, D9 HIGH, D10 MEDIUM
- `ARCHITECTURE_FIT`: SA01 MEDIUM, SA02 HIGH, SA03 HIGH, SA04 MEDIUM, SA05 HIGH, SA06 HIGH, SA07 HIGH, SA08 HIGH, SA09 MEDIUM
- `PROOF_FIT`: V1 HIGH, V2 HIGH, V3 MEDIUM, V4 BLOCKED
- `PROOF_MODES`: PUBLIC_DEMO, HANDLED_INSPECTION, COMPARISON, MATERIAL_INSPECTION, PACKAGE_OR_QUANTITY_CHECK
- `PRODUCT_ENTRY_MODES`: FOREIGN_TRADER_ARRIVAL, NEW_STALL_PRODUCT, WRAPPED_DELIVERY, TRAVELER_PERSONAL_ITEM, PUBLIC_DEMONSTRATION, RIVAL_COMPARISON
- `AUDIENCE_CONSTRAINTS`: no_real_religious_or_civilizational_identity; no_human_trade_or_ethnic_stereotypes
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: REPUTATION, RIVAL_POSITION, VALUE, OUTSIDER_STATUS, BUYER_POSITION, CROWD_POSITION
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: HIGH
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: crowd_complexity HIGH; civilization_mixing HIGH; product_ancient_redesign HIGH; product_replication HIGH; wrong_price_text HIGH; handoff_interaction MEDIUM
- `SEEDANCE_LOCKS`: coherent fictional Mediterranean-inspired market; minimum necessary foreground characters; modern product unchanged; public judgment remains legible
- `FAILURE_PATTERNS`: random civilization mashup; excessive crowd; product ancient redesign; copied product piles; invented price text; bargaining overwhelms Proof

---

# 14. S12｜架空复古豪华长途列车

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
- `POWER_STRUCTURE`: MEDIUM
- `NATIVE_TIME_PRESSURE`: HIGH
- `NATIVE_INFORMATION_FLOW`: CURRENT_CARRIAGE → ATTENDANT → ADJACENT_COMPARTMENT → PUBLIC_CAR → OWNER/AUTHORITY
- `OBJECT_STATUS_LOGIC`: 物品的位置、持有人和沿车厢移动的路径，本身就是归属与身份信息。
- `DNA_ACTIVATION_CONDITION`: Carriage order / Ownership / Attendant authority / Next-stop pressure / Object movement across compartments至少一项进入因果链；否则只算Train Location。
- `SPACE_TOPOLOGY`: LINEAR
- `CONTINUITY_ANCHORS`: corridor_direction, window_side, door_side, compartment_order, dining_car_direction, product_origin, product_current_location

## COMMERCIAL ROUTING
- `DECISION_FIT`: D1 MEDIUM, D2 LOW, D3 MEDIUM, D4 MEDIUM, D5 LOW, D6 LOW, D7 MEDIUM, D8 HIGH, D9 MEDIUM, D10 HIGH
- `ARCHITECTURE_FIT`: SA01 MEDIUM, SA02 LOW, SA03 HIGH, SA04 MEDIUM, SA05 MEDIUM, SA06 HIGH, SA07 HIGH, SA08 MEDIUM, SA09 MEDIUM
- `PROOF_FIT`: V1 HIGH, V2 MEDIUM, V3 MEDIUM, V4 BLOCKED
- `PROOF_MODES`: PORTABLE_USE, OWNERSHIP_PROOF, LUGGAGE_REFERENCE, DINING_TABLE_USE, TRAVEL_ACCESS
- `PRODUCT_ENTRY_MODES`: MISDELIVERED_ITEM, LUGGAGE_REVEAL, PERSONAL_TRAVEL_ITEM, DINING_TABLE_DISCOVERY, ATTENDANT_DELIVERY, LOST_AND_FOUND
- `AUDIENCE_CONSTRAINTS`: no_real_rail_brand_route_or_highly_identifiable_train
- `REVERSAL_COMPATIBILITY`: HIGH
- `SUPPORTED_REVERSAL_TYPES`: OWNERSHIP, IDENTITY, PURPOSE, STATUS, DESTINATION, SOCIAL_JUDGMENT
- `COMEDY_COMPATIBILITY`: HIGH
- `ABSURDITY_COMPATIBILITY`: MEDIUM
- `VISUAL_SPECTACLE_VALUE`: HIGH

## GENERATION ROUTING
- `GENERATION_RISKS`: narrow_space HIGH; door_interaction HIGH; handoff_interaction HIGH; left_right_drift HIGH; multi_character MEDIUM; product_retro_redesign HIGH
- `SEEDANCE_LOCKS`: original fictional luxury train; corridor/window/door orientation fixed; outside scenery subtly moves; minimum necessary performers; product unchanged
- `FAILURE_PATTERNS`: carriage left/right flips; handoff intersections; exaggerated train sway; product retro redesign; automatic murder mystery

---

# 15. Router使用原则

1. Safety先淘汰 `BLOCKED`。
2. `DNA_ACTIVATION_CONDITION` 必须能被当前Story真正触发，否则特殊Scene降级为普通Location。
3. 静态Index只给先验；运行时仍计算具体 `Character Fit / Product Entry Fit / Generation Risk / Batch Diversity`。
4. 已确定R0/R1/R2后才看 `REVERSAL_COMPATIBILITY`；R0/R1不得因Scene支持R2而升级。
5. 比较特殊Scene与普通真实生活场景：如果特殊Scene不能明显增强商业理解、Story Architecture、Proof、Reaction或视觉区分度，则使用普通生活场景。
6. `BASE_VISUAL_DISTINCTIVENESS` 不能覆盖商业匹配度。
7. 同批Diversity Penalty同时考虑 `PRIMARY_CLASS / SECONDARY_CLASS_TAGS / Reaction机制 / SPACE_TOPOLOGY / Product Entry机制`，不只看Scene ID。
8. Index迁移状态不等于Validation状态；12个Scene虽然都已MIGRATED，但仍全部是 `TESTING_CANDIDATE`。
