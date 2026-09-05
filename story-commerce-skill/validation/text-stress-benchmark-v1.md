# TEXT STRESS BENCHMARK V1｜20类实体商品纯文本压力测试

> 目标：不继续烧视频积分，直接验证剧情带货 Skill 3.4.2 在陌生实体商品进入时，是否还能稳定完成：时长判断、Direct/Need-led路由、Perceived Value Contrast、Story Architecture、R-level、Best Proof、Product Takeover、场景与高风险Proof边界。
>
> 评估原则：不是比谁的创意最花，而是找结构性退化——尤其检查是否又塌成“两个女人聊天→拿产品→震惊→CTA”、是否所有商品都被强行30秒、是否所有广告都强行R2、是否把不可见/不可证明的属性伪造成AI视频Proof。

---

# 1. 判定标准

每个Case检查：

1. `DURATION`：30s默认是否会在单Proof商品上主动降到15s；
2. `HOOK ROUTE`：DIRECT PRODUCT / NEED-LED是否合理；
3. `PERCEPTION`：SMALL→MAGNIFY、VALUE→VALUE_ELEVATION、PREMIUM→LUXURY_NORMALIZATION是否正确；
4. `ARCHITECTURE`：是否只选1个Primary Architecture；
5. `R-LEVEL`：是否从R0保守升级；
6. `BEST PROOF`：是否真实、可视、与购买问题一致；
7. `PRODUCT TAKEOVER`：30s中后段是否让产品接管，而不是继续短剧；
8. `RISK GUARD`：感官、健康、安全、精确性能等是否拒绝伪造Proof；
9. `TV SHORT DRIFT`：删除产品后剧情是否还能原样成立；
10. `GENERATION LOAD`：是否避免不必要的复杂交互。

判定：`PASS / PASS_WITH_GUARD / FAIL`

---

# 2. 20类商品路由结果

| ID | 商品Fixture | Scale × Value | 时长 | Hook Route | Primary Architecture | R-level | Best Proof / Expression | Perceived Value方向 | 关键Guard | 结果 |
|---|---|---|---:|---|---|---|---|---|---|---|
| T01 | 高端金属戒指 | SMALL × PREMIUM | 15s | DIRECT PRODUCT | SA09 Experience→Preference→Adoption | R0 | 手部真实比例 + 金属微距 + 日常佩戴动作 | MAGNIFY + LUXURY_NORMALIZATION | 不虚构宝石/材质等级 | PASS |
| T02 | 高端智能手表（已确认Always-On显示） | SMALL × PREMIUM | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 手腕真实佩戴 + 常亮界面可见 + 一次真实查看动作 | MAGNIFY + LUXURY_NORMALIZATION | 不延伸到未确认健康/运动精度 | PASS |
| T03 | 降噪无线耳机（单卖点ANC） | SMALL × PREMIUM | 15s | NEED-LED | SA01 Problem→Solution | R0/R1 | 同环境噪音前后 + 人物注意力状态变化 | MAGNIFY + LUXURY_NORMALIZATION | 单卖点已能15s讲完，不强拉30s | PASS |
| T04 | 基础低价白T | MEDIUM × VALUE | 30s | DIRECT PRODUCT | SA09 Experience→Preference→Adoption | R0 | 真实上身比例 + 2–3套高价值搭配 + 材质/领口细节 | VALUE_ELEVATION + VERSATILITY | 不虚构高价、奢侈品牌、材质 | PASS |
| T05 | 高端设计师羽毛短裙 | MEDIUM × PREMIUM | 30s | DIRECT PRODUCT | SA05 Choice→Test→Decision | R1/R2按Evidence决定 | 挂着外观→上身→侧面/动态→生活场景 | LIVED-IN LUXURY | Reveal后必须Product Takeover；穿戴Ownership唯一 | PASS |
| T06 | 高端皮质手袋 | MEDIUM × PREMIUM | 30s | DIRECT PRODUCT | SA05 Choice→Test→Decision | R1 | 外观→开口结构→放入已定义日常小件→携带轮廓 | LUXURY_NORMALIZATION + PRACTICAL ELEGANCE | 容量只证明实际放入的物件，不夸大“超大容量” | PASS |
| T07 | 中高价跑鞋 | MEDIUM × MID/PREMIUM | 30s | DIRECT PRODUCT | SA09 Experience→Preference→Adoption | R0 | 上脚比例 + 系带/脚跟锁定 + 走/轻跑的自然动作 | ASPIRATION × PROOF / lived-in use | 不宣称提速、减伤、治疗疼痛 | PASS |
| T08 | 高端香水 | SMALL × PREMIUM | 15s | DIRECT PRODUCT | SA09 Experience→Preference→Adoption | R0 | 瓶体微距、喷雾、人物/场景情绪作为感官代理 | MAGNIFY + LUXURY_NORMALIZATION | 气味无法被视频客观证明；Reaction只能代理主观体验 | PASS_WITH_GUARD |
| T09 | 高端护肤泵瓶精华 | SMALL × PREMIUM | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 泵头出料→质地微距→皮肤表面涂抹状态 | MAGNIFY + LUXURY_NORMALIZATION | 不用AI画面证明长期功效、抗老、医学结果 | PASS_WITH_GUARD |
| T10 | SPF防晒产品 | SMALL × MID/PREMIUM | 15s或EXIT | DIRECT PRODUCT | SA02仅限质地/涂抹；功效诉求则EXIT | R0 | 只可证明包装、挤出、延展、涂抹等可见事实 | MAGNIFY / balanced | 不能靠剧情画面证明SPF保护强度、长期防晒结果；若广告核心必须证明该功效，停止伪造Proof | PASS_WITH_GUARD |
| T11 | 保温杯 / 随行杯（已确认盖结构） | MEDIUM × MID | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 开盖/饮用/真实容器路径或已确认结构的操作Proof | ASPIRATION × PROOF | 不默认防漏/保温时长，除非事实确认 | PASS |
| T12 | 低价食品收纳盒套装 | MEDIUM × VALUE | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 明确物品装入→盖合→冰箱/橱柜真实堆叠 | VALUE_ELEVATION + ORDER | 不用“密封/防漏”除非产品事实确认 | PASS |
| T13 | 无线吸尘器 | LARGE × MID | 30s | NEED-LED | SA01 Problem→Solution | R0/R1 | 可见碎屑→产品经过同一路径→地面结果；第二Proof可用边角/家具下方若结构允许 | ASPIRATION × PROOF | 不编造吸力数值、电池时长 | PASS |
| T14 | 高端扫地机器人 | LARGE × PREMIUM | 30s | NEED-LED | SA01 Problem→Solution / SA04 Goal→Result二选一 | R0 | 有动力来源的自主移动 + 可见地面任务前后 | QUIET UTILITY | 不默认避障、拖地、自清洁等未确认能力；机器人自身动力必须明确 | PASS |
| T15 | 高端沙发 | LARGE × PREMIUM | 30s | DIRECT PRODUCT | SA05 Choice→Test→Decision | R0 | 人体/房间尺度 + 坐姿/多人使用关系 + 空间占地 | QUIET UTILITY | “舒服”是主观体验，不能把Reaction当客观舒适度证明；优先证明空间/使用关系 | PASS_WITH_GUARD |
| T16 | 中高价登机箱 | LARGE × MID/PREMIUM | 30s | NEED-LED / DIRECT均可 | SA04 Goal→Attempt→Result | R0/R1 | 固定物品集合装入→拉链闭合→真实拉行路径 | ASPIRATION × PROOF / lived-in travel | 不用“能装X天”替代具体物品Proof；轮子/扩容需确认 | PASS |
| T17 | 宠物慢食碗 | MEDIUM × VALUE/MID | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 狗真实与迷宫结构互动，只展示行为路径 | VALUE_ELEVATION + BEHAVIOR CONTEXT | 不用单次AI狗行为证明“科学减慢X%/更健康”；若核心卖点是量化效果需真实证据 | PASS_WITH_GUARD |
| T18 | 高端主厨刀 | MEDIUM × PREMIUM | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 安全厨房场景下切番茄/香草的单一清楚切割Proof + 刀身细节 | LUXURY_NORMALIZATION + DETAIL | 不宣称长期锋利度、专业认证；一镜一项精细接触 | PASS |
| T19 | 已确认不粘涂层煎锅 | MEDIUM × MID | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 蛋/食材在真实锅面烹饪后的可见释放动作 | ASPIRATION × PROOF | 不暗示“零油”“永久不粘”除非确认；火源/锅具支撑合理 | PASS |
| T20 | 移动电源（已确认常规有线充电兼容） | SMALL/MEDIUM × MID | 15s | DIRECT PRODUCT | SA02 Demonstration→Evidence→Decision | R0 | 接线→手机出现真实充电状态→产品与手机同框 | MAGNIFY + PROOF | 不暗示快充瓦数/次数/续航量，除非确认 | PASS |

---

# 3. 横向结果

## 3.1 时长Router没有“30秒强迫症”

20个Case中：
- 约8个更适合30s：T04/T05/T06/T07/T13/T14/T15/T16；
- 其余大多单卖点、单Proof，15s更自然；
- T10在核心功效不可由AI视频证明时允许EXIT或只退回可见质地表达。

结论：
> `DEFAULT 30s`没有压过`DURATION FIT`。这点通过。

## 3.2 Story Architecture没有塌成万能双人质疑模板

实际出现：
- SA01：耳机、吸尘器、扫地机器人；
- SA02：手表、护肤、容器、刀具、锅、移动电源等；
- SA04：登机箱；
- SA05：羽毛裙、手袋、沙发；
- SA09：戒指、白T、跑鞋、香水。

没有必要为了“看起来像剧情”把SA02硬改成两人聊天。

结论：PASS。

## 3.3 R2没有被滥用

大多数Case正确停留R0；
只有服装/手袋等存在真实“第一印象→验证→改判”空间时才考虑R1/R2，且仍需Evidence Gate。

结论：PASS。

## 3.4 Perceived Value Contrast跨品类工作正常

覆盖：
- SMALL：戒指/手表/耳机/香水/护肤/防晒/移动电源 → MAGNIFY；
- VALUE：白T/收纳盒/宠物碗 → VALUE_ELEVATION；
- PREMIUM：戒指/手表/羽毛裙/手袋/香水/沙发 → LUXURY_NORMALIZATION / QUIET UTILITY。

没有发现“高级产品继续无限堆奢华”或“基础产品只拍便宜实用”的结构回退。

结论：PASS。

## 3.5 高风险/不可见Proof边界工作正常

重点Guard Case：
- 香水：只能用主观感官代理；
- 护肤：不证明长期功效；
- SPF防晒：不伪造保护强度；
- 沙发：不把人物笑容当客观舒适度测量；
- 宠物慢食碗：不把单次AI行为当科学效果证明。

结论：PASS。

## 3.6 Product-Centered Gate没有明显TV SHORT DRIFT

所有30s Case均可明确回答：
- 前段产品问题/商业需求是什么；
- Product Pivot在哪；
- 后半Proof Ladder是什么；
- 删除产品后故事为什么无法原样成立。

结论：PASS。

---

# 4. 本轮发现的非阻断性提醒

没有发现需要推翻3.4.2结构的新问题。

只保留三个执行提醒：

1. **感官型产品不要为了“剧情化”伪造客观Proof。** 香水/护肤/舒适度优先代理表达或缩短广告。
2. **30秒默认不等于所有商品30秒。** 单卖点SA02商品继续主动建议15秒，避免重现AirPods 30s平台期。
3. **高级产品生活化不能变成Lifestyle Film。** LUXURY_NORMALIZATION仍必须通过Product-Centered Gate；生活氛围托举产品，不取代Product Proof。

这些都已被现有3.4.2规则覆盖，因此本轮不新增Hotfix。

---

# 5. 最终结果

- `20 / 20` Case完成有效路由；
- `15 / 20` 直接PASS；
- `5 / 20` PASS_WITH_GUARD，均来自不可直接视觉证明的感官/健康/行为/主观体验边界，而非Story Router失效；
- `0` Architecture Collapse；
- `0` Forced R2；
- `0` 明显TV SHORT DRIFT；
- `0` 因30秒默认导致的强行填时长。

本轮结论：

> **TEXT STRESS BENCHMARK V1 = PASS**

下一阶段：
1. 更新真实视频 `results-registry.md`，补入服装/羽毛裙/7-Eleven/容器TEST B及对应Hotfix证据；
2. 然后做一次“普通用户一句话输入”的冷启动测试；
3. 若无新结构性问题，进入上架候选收口。