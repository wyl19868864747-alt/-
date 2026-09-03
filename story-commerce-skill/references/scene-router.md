# SCENE ROUTER｜剧情带货场景路由 3.2

> 目标：让特殊Scene只在真正增强商业表达时被调用，并严格保持：
>
> `Commercial Decision → Story Architecture → Proof Plan → Reversal Level → Scene Router → Scene DNA原生化 → Story → Seedance Prompt`

Scene Router位于Story Architecture、Proof Plan和Reversal Router之后。

**Scene不得重新选择Primary Architecture，不得重新决定R0/R1/R2，不得为了世界效果篡改商品事实或Best Proof。**

---

# 0. 总原则

Scene不是美术风格标签，而是一套会改变人物身份、社会规则、天然冲突、商品进入方式、动作、对白、Reaction、节奏、镜头与空间连续性的世界规则。

核心测试：

> **如果完全没有商品，这个世界里的人原本会因为什么产生冲突？**

回答不清楚，Scene DNA不成立。

Scene系统当前拆成三层：

- `scene-index.md`：路由索引，回答“哪些Scene值得候选”
- `scene-dna-library.md`：执行DNA，回答“选中后这个世界具体怎么演、怎么拍”
- `scene-validation-registry.md`：验证状态，回答“哪些能力真实测试过”

任何Scene都必须服从：

`用户明确要求 > 商品事实/SKU/参考资产 > 合规与安全 > Core Decision Question > Best Proof > Primary Story Architecture > R0/R1/R2 > Scene增益 > 美术风格`

永远：

`PRODUCT TRUTH > SCENE TRICK`
`PRIMARY ARCHITECTURE > SCENE`
`PROOF > SCENE SPECTACLE`
`PRODUCT LOCK > SCENE STYLE`

现代商品进入历史/未来世界时，外观、颜色、比例、包装、结构和真实能力保持不变；Scene只能改变“这个世界的人为什么注意它、怎样行动、怎样验证、怎样反应、怎样拍”。

---

# 1. Scene是可选模块，不是必经步骤

进入Scene Router前，已经具备：

- Product Decision Card
- Core Decision Question
- Top Hesitation
- Best Proof / Proofability
- Primary Story Architecture / Primary Driver
- Reversal Card：R0 / R1 / R2
- Platform / Duration / Constraints

只有满足以下任一情况才考虑特殊Scene DNA：

1. 用户明确指定特殊Scene；
2. Story Architecture Card判断Scene DNA Value为MEDIUM/HIGH；
3. 世界规则能明显增强人物身份、冲突、Product Entry、Proof、Reaction、Hook或镜头；
4. 相比普通真实生活场景，特殊Scene能产生明确的商业或观看增益。

如果普通真实生活场景已经更直接、更可信、更稳定：

> **不调用特殊Scene DNA。**

特殊Scene不是Skill工作量证明。

---

# 2. 数据读取顺序

## 2.1 先读Index

进入特殊Scene候选阶段时先读取 `scene-index.md`：

- Safety / Audience Constraints
- Decision Fit
- Architecture Fit
- Proof Fit
- Product Entry Modes
- DNA Activation Condition
- Generation Risks
- Creative Compatibility
- Scene Class / Diversity信息

当前过渡期只有S01、S04、S12完成结构化Pilot Index；其他Scene尚未迁移时，不得因为缺少Index分数而自动淘汰，继续结合现有Scene Card与本文件legacy priors判断。

## 2.2 再读选中的DNA Card

只有Scene进入最终候选或已经被用户明确指定后，才读取 `scene-dna-library.md` 对应Scene Card。

不要为了比较12个Scene而每次完整读取12张执行Card。

## 2.3 Validation只提供证据状态

读取 `scene-validation-registry.md` 确认：

- 当前Status
- 哪些生成测试PASS/FAIL/PARTIAL/NOT_TESTED
- 是否可以声称VALIDATED

Validation状态不能代替商业匹配度；但关键生成风险已明确FAIL时，应降权或避免使用。

---

# 3. Scene Status

当前正式候选库共12个Scene，全部为：

`TESTING_CANDIDATE`

尚无任何Scene被证据支持为`VALIDATED`。

状态真值以 `scene-validation-registry.md` 为准。

当前12个：

- S01 架空古装宫廷
- S02 现代美国高中
- S03 架空古代战争军营
- S04 现代美国企业办公室
- S05 架空美国西部边疆贸易小镇
- S06 架空现代豪华上流晚宴
- S07 现代美国大型购物中心
- S08 架空未来都市·星际商业世界
- S09 架空复古美国公路Diner
- S10 架空高压真人竞赛节目
- S11 架空古代地中海公共市集
- S12 架空复古豪华长途列车

---

# 4. Scene Selection｜选择规则

## 4.1 用户明确指定Scene

用户明确选择Scene时优先使用，不擅自换成历史高频模板。

但仍先执行Safety与Truth Gate。

仅在以下情况允许阻断或改路由：

- Scene与商品/受众存在明确合规冲突；
- 商品无法自然进入，必须严重歪曲事实才能成立；
- Scene会迫使不可证明卖点变成伪Proof；
- Scene要求与真实参考资产/物理事实冲突；
- 核心Scene机制必然破坏Primary Architecture或Best Proof。

若用户只是指定“办公室/列车/宫廷”作为空间，但故事没有触发该Scene的 `DNA_ACTIVATION_CONDITION`：

> 可以保留该Location，但不声称正在使用完整Scene DNA。

---

## 4.2 用户未指定Scene

先比较：

`普通真实生活场景`
VS
`特殊Scene DNA`

特殊Scene只有存在明确增益时才能胜出。

### Step A｜Safety先淘汰

任何BLOCKED或Safety Gate失败Scene直接淘汰。

### Step B｜DNA Activation

问：

> 当前故事是否真的会触发该Scene的世界发动机/权力规则/空间逻辑？

如果NO，特殊Scene降级为普通Location，不参与完整Scene DNA排名。

### Step C｜Fit Scoring

结构化Index统一使用：

`BLOCKED / LOW / MEDIUM / HIGH`

运行时可映射：

`LOW=0 / MEDIUM=1 / HIGH=2`

重点比较：

1. **Decision Fit**：是否放大Core Decision Question
2. **Architecture Fit**：是否增强当前Primary Architecture，而非偷换Driver
3. **Proof Fit**：是否能自然承载Best Proof
4. **Native Conflict Fit**：无商品时是否已有真实世界冲突
5. **Product Entry Fit**：商品是否无需硬塞即可进入
6. **Character Fit**：目标人物是否能自然成为该世界角色（运行时动态计算）
7. **Reaction Fit**：Scene原生Reaction是否增强Decision Change
8. **Visual Distinctiveness**：是否带来有效而非纯装饰的视觉差异
9. **Generation Risk**：人物、空间、交接、文字、尺度风险是否在Complexity Budget内
10. **Safety Fit**

### Reversal Fit的条件调用

- R0：不评分Reversal Fit；Scene不得主动添加误判/反转
- R1：只检查Scene是否能自然表达已经确定的Clarification / Reveal / Surprise
- R2：才检查 `REVERSAL_COMPATIBILITY` 与 `SUPPORTED_REVERSAL_TYPES`

**Scene支持R2 ≠ 本条应该升级R2。**

### Step D｜Diversity Penalty

同批多条广告对以下重复项降权：

- Scene ID重复
- PRIMARY_CLASS重复
- SECONDARY_CLASS_TAGS高度重复
- Reaction机制重复
- 空间拓扑重复
- Product Entry机制重复

但Diversity永远不能覆盖商业匹配度。

### Step E｜Special Scene Value Check

最后问：

> 使用这个特殊Scene，相比普通真实生活场景，是否明显增强了商业理解、Primary Architecture、Best Proof、Reaction或视觉记忆中的至少一项，同时没有显著损失生成稳定性？

如果NO：

> 使用普通真实生活场景。

---

# 5. Router Prior｜过渡期Legacy候选先验

> 仅用于尚未完成Index迁移的Scene；不是硬匹配。任务14完成12个迁移后，应逐步让位给结构化Index。

## 身份、穿搭、品味、社交接受
- S06 豪华晚宴
- S02 美国高中（仅安全普通商品）
- S07 现代商场
- S01 古装宫廷

## 效率、工作流、操作步骤、问题解决
- S04 现代办公室
- S08 未来商业世界
- S03 古代战争军营
- S10 真人竞赛（仅可短时验证）

## 耐用、实用、现场结果、机制Proof
- S05 西部小镇
- S11 古代市集
- S10 真人竞赛
- S03 古代战争军营

## 比较、试用、选择、购买决策
- S07 现代商场
- S11 古代市集
- S05 西部小镇

## 归属、旅行、便携、随身使用
- S12 豪华列车
- S09 复古Diner
- S07 现代商场

## 误会、轻喜剧、信息传播
- S09 复古Diner
- S02 美国高中
- S06 豪华晚宴
- S12 豪华列车

## 强时代错位/视觉奇观
- S01 古装宫廷
- S03 古代战争军营
- S05 西部小镇
- S08 未来商业世界
- S11 古代市集
- S12 豪华列车

---

# 6. Scene Safety Gate｜硬阻断

## S02 现代美国高中

默认使用18岁以上成年演员扮演毕业班学生。

禁止路由：
- 成人药品、减重/GLP-1等医疗内容
- 酒精、烟草、尼古丁
- 赌博/博彩
- 成人约会/性产品
- 武器
- 其他明显年龄限制/不适合校园语境商品

无真实学校Logo、吉祥物、球队。

## S03 架空古代战争军营

战争感通过军帐、地图、补给、传令、队列、Deadline建立。

禁止以刀枪、射击、砍杀、伤口、尸体、爆炸杀伤建立Scene；不用于真实武器/军火商品。

## S05 架空美国西部边疆贸易小镇

保留Western Standoff Composition，不保留Gunfight。

枪械、弹药、拔枪、射击、血腥不是商业Scene资产；不使用原住民族刻板印象或真实历史人物。

## S06 架空现代豪华上流晚宴

不复制真实Gala、奢侈品牌、名人、慈善组织。

不把贫穷、出身、族裔、口音当笑点；“高端”只表示社交规则和视觉质感。

## S08 架空未来都市·星际商业世界

严格：

`WORLD TECH ≠ PRODUCT FACT`

环境可未来化，但商品不能自动获得AI、全息、扫描、医疗检测、自动感应等真实SKU不存在能力。

## S09 架空复古美国公路Diner

借mid-century视觉和空间语法，不复制真实种族隔离制度/民权事件，不使用真实餐饮或饮料品牌。

## S10 架空高压真人竞赛节目

Challenge必须：

`Verified Product Fact → Visible Task → Fair Rule → Observable Result`

禁止危险挑战、赌博、彩票、购买即抽奖、虚假比分、未经证实的百分比/#1/best声明。

长期舒适、长期耐用、医学效果、精确续航等不可用短比赛伪证明。

## S11 架空古代地中海公共市集

保持统一架空地中海古典视觉，不混搭无关文明，不使用真实宗教仪式、人口交易或文化刻板印象。

## S12 架空复古豪华长途列车

不复制Orient Express、Pullman等真实高识别品牌/车型/路线。

默认可使用Social/Ownership Mystery，但**不得因为Scene本身自动添加R2，也不自动添加谋杀、侦探、枪械、毒药等犯罪悬疑。**

---

# 7. Product × Scene Compilation｜世界原生化，不重写上游决策

选择特殊Scene后，不得直接套Scene故事模板。

上游已经锁定：

- Core Decision Question
- Primary Driver
- Primary Story Architecture
- Architecture Required Beats
- Best Proof
- Product Causal Role
- R0 / R1 / R2

Scene只负责把这些内容**世界原生化**。

正确顺序：

`Primary Story Architecture`
→ `保留Required Beats`
→ `保留Best Proof`
→ `保留R0/R1/R2`
→ `读取Scene World Engine / Native Conflict / Social Rules`
→ `用Scene身份与规则重新表达同一个Story Driver`
→ `选择Scene原生Product Entry`
→ `选择Scene原生动作 / Dialogue / Reaction / Camera / Pacing`
→ `锁Space Topology / Continuity Anchors`
→ `CTA`

## R0

Scene不得添加：
- 错误答案
- 双误导证据
- Micro Anomaly
- 180°反转

只把原Architecture与Proof变成该世界自然发生的事件。

## R1

保留Reversal Router已经决定的类型：

- Clarification
- Reveal
- Surprise

Scene只改变它在该世界里的呈现方式，不升级成R2。

## R2

只有Reversal Router已经确定R2时：

- 从Scene Index / DNA Card寻找兼容的世界原生Reversal表达
- 不改Wrong Answer的商业功能
- 不增加新的第二套反转
- 不为了Scene奇观挤压Best Proof

核心检查：

> **同一个商品、同一个Primary Architecture换Scene后，人物身份、冲突呈现、Product Entry、动作、Dialogue、Reaction、节奏、镜头应明显改变；但Primary Driver、Best Proof和R-level不得被改写。**

若只是背景从办公室换成宫廷，故事、动作、对白基本一样，Scene DNA调用失败。

---

# 8. DNA Activation Test｜Location ≠ Scene DNA

选定Scene后必须问：

1. 当前故事是否触发该Scene至少一个关键世界规则？
2. 这个规则是否真的改变人物为什么行动？
3. Product Entry是否利用了这个世界，而不是普通桌面露出？
4. Reaction是否来自这个世界的社会/空间规则？

如果主要答案为NO：

> 保留Location可以，但退出完整Scene DNA调用。

例：
- “两个人坐办公室聊天” ≠ S04 Office DNA
- “人物在豪华列车包厢聊天” ≠ S12 Train DNA
- “穿古装站宫殿里介绍产品” ≠ S01 Court DNA

---

# 9. Scene Independence Test

正式故事生成前回答：

1. 删除商品，这个Scene中的人物为什么本来就会产生事件/冲突？
2. 商品加入后，是利用了该世界规则，还是中途插播？
3. 把特殊Scene换成普通客厅后，故事是否几乎不用改？

若第1题答不出，或第3题为“是”：

> 特殊Scene DNA失败；重写或回退普通生活场景。

---

# 10. Generation Complexity Gate

Scene选择不能只看创意价值，还要看生成预算。

重点读取/判断：

- 核心人物数量
- 背景人群复杂度
- Product Handoff
- 狭窄空间/门/玻璃
- Left/Right与Axis连续
- 产品尺度漂移
- 屏幕文字乱码
- 历史/未来Scene重设计商品风险

原则：

> **最低必要人物数优先。**

Scene Card里的旧“2–4主角”“3–6近景人物”等只能作为历史研发参考，不得覆盖3.2主Skill的最低必要人物原则。

如果两个Scene商业增益接近：

> 选择人物更少、交互更简单、空间更稳定的那个。

---

# 11. Cross-Product Stability Test

Scene进入VALIDATED前，至少使用三类差异商品实际测试：

- 3C
- 服装
- 日用品

必须验证：

- 世界发动机保持
- 商品剧情不同但Scene原生
- PRODUCT LOCK
- Best Proof真实
- 不因时代/风格重设计商品
- 物理交互稳定
- 空间连续
- Reaction Chain可执行

测试结果统一写入 `scene-validation-registry.md`。

`scene-dna-library.md`中的“跨商品结构QA”只算 `INTERNAL_PASS`，不等于实际生成PASS。

---

# 12. VALIDATED升级条件

单Scene只有满足 `scene-validation-registry.md` 的全部硬条件，才可从：

`TESTING_CANDIDATE → VALIDATED`

至少包括：

- 三类跨商品实际生成PASS
- Scene Recognition PASS
- PRODUCT LOCK PASS
- Space Continuity PASS
- Physical Interaction PASS
- 适用的多人/交接稳定性PASS
- Scene-specific Reaction PASS
- Safety Gate PASS
- IP Distinctness PASS

关键项FAIL或NOT_TESTED时继续保持TESTING。

不得因为理论结构成熟、Index已迁移或内部QA通过就提前升级。

---

# 13. Router最终输出｜内部

Scene Router只需返回：

```text
SCENE MODE:
NORMAL_LOCATION / SPECIAL_SCENE_DNA

SELECTED SCENE:
<若SPECIAL则填Sxx>

WHY:
<为什么特殊Scene比普通生活场景有明确增益>

DNA ACTIVATION:
<被触发的世界规则>

PRODUCT ENTRY:
<Scene原生入口>

R-LEVEL PRESERVATION:
R0 / R1 Clarification / R1 Reveal / R1 Surprise / R2

CONTINUITY ANCHORS:
<最少必要空间锁定>

GENERATION RISK:
<主要风险>
```

普通用户默认不需要看到这张卡。

---

# 14. 最终原则

- Scene是可选增强，不是必经步骤。
- Story Architecture决定因果骨架；Scene不能偷换Primary Driver。
- Proof已经先锁；Scene不能为了视觉奇观挤压或伪造Proof。
- R0/R1/R2已经先锁；Scene不能自动升级反转。
- Location不等于Scene DNA；必须触发世界规则。
- 特殊Scene必须赢过普通生活场景，才值得增加生成复杂度。
- Scene Index负责检索，DNA Library负责执行，Validation Registry负责证据状态。
- **Scene的价值不是背景有多漂亮，而是换了这个世界以后，人物为什么行动、怎么行动、怎么反应、怎么拍都真正改变。**