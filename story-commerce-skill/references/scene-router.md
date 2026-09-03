# SCENE ROUTER｜剧情带货场景路由 3.4｜COMMERCIAL FREEZE

> 目标：让特殊Scene只在真正增强商业表达时被调用，并严格保持：
>
> `Commercial Decision → Story Architecture → Proof Plan → Reversal Level → Scene Router → Scene DNA原生化 → Story → Performance → Seedance Prompt`

Scene Router位于Story Architecture、Proof Plan和Reversal Router之后。

**Scene不得重新选择Primary Architecture，不得重新决定R0/R1/R2，不得为了世界效果篡改商品事实或Best Proof。**

---

# 0. 总原则

Scene不是美术风格标签，而是一套会改变人物身份、社会规则、天然冲突、商品进入方式、动作、对白、Reaction、节奏、镜头与空间连续性的世界规则。

核心测试：

> **如果完全没有商品，这个世界里的人原本会因为什么产生冲突？**

回答不清楚，Scene DNA不成立。

Scene系统拆成三层：

- `scene-index.md`：路由索引，回答“哪些Scene值得候选”
- `scene-dna-library.md`：执行DNA，回答“选中后这个世界具体怎么演、怎么拍”
- `scene-validation-registry.md`：验证状态，回答“哪些能力真实测试过”

任何Scene都必须服从：

`用户明确要求 > 商品事实/SKU/参考资产 > 合规与安全 > Core Decision Question > Best Proof > Primary Story Architecture > R0/R1/R2 > Scene增益 > Performance > 美术风格`

永远：

`PRODUCT TRUTH > SCENE TRICK`
`PRIMARY ARCHITECTURE > SCENE`
`PROOF > SCENE SPECTACLE`
`NORMAL LOCATION IS A VALID WINNER`
`PRODUCT LOCK > SCENE STYLE`

现代商品进入历史/未来世界时，外观、颜色、比例、包装、结构和真实能力保持不变；Scene只能改变“这个世界的人为什么注意它、怎样行动、怎样验证、怎样反应、怎样拍”。

---

# 1. Candidate 0｜普通真实生活场景是正式候选

Scene Router不是“先从12个特殊世界里挑一个，再问要不要放弃”。

用户未指定特殊Scene时，候选池从一开始就是：

`CANDIDATE 0 = NORMAL_LOCATION`
+
`S01–S12 SPECIAL_SCENE_DNA`

`NORMAL_LOCATION`完全合格，尤其适合：
- Proof本身已经足够强；
- 真实使用情境比特殊世界更可信；
- 高风险医疗/安全/金融/资格/价格信息；
- 极短时长；
- 特殊Scene只增加美术差异，不增加商业因果；
- 特殊Scene会显著增加人物、空间、交接、文字或产品变形风险。

如果普通生活场景已经更直接、更可信、更稳定：

> **让NORMAL_LOCATION获胜。**

特殊Scene不是Skill工作量证明。

---

# 2. 进入Scene Router前的已锁输入

进入Scene Router前已经具备：

- Product Decision Card
- Core Decision Question
- Top Hesitation
- Best Proof / Proofability
- Primary Story Architecture / Primary Driver
- Product Causal Role
- Reversal Card：R0 / R1 / R2
- Platform / Duration / Constraints

只有满足以下任一情况才认真评估特殊Scene：

1. 用户明确指定特殊Scene；
2. Story Architecture Card判断Scene DNA Value为MEDIUM/HIGH；
3. 世界规则能明显增强人物身份、冲突、Product Entry、Proof、Reaction、Hook或镜头；
4. 相比NORMAL_LOCATION，特殊Scene能产生明确商业或观看净增益。

---

# 3. 数据读取顺序

## 3.1 先读Index

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

当前12个Scene均已完成结构化Index迁移。候选比较优先读取 `scene-index.md`。

## 3.2 再读选中的DNA Card

只有Scene进入最终候选，或用户明确指定后，才读取 `scene-dna-library.md` 对应Scene Card。

不要为了比较12个Scene而完整读取12张执行Card。

## 3.3 Validation只提供证据状态

读取 `scene-validation-registry.md` 确认：

- 当前Status
- PASS / FAIL / PARTIAL / NOT_TESTED
- 是否可以声称VALIDATED

Validation状态不能代替商业匹配度；关键生成风险若已有FAIL证据，应降权或避免使用。

---

# 4. Scene Status

当前正式候选库共12个Scene，全部为：

`TESTING_CANDIDATE`

尚无任何Scene被证据支持为`VALIDATED`。

状态真值以 `scene-validation-registry.md` 为准。

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

# 5. Scene Selection｜冻结后的分层路由

**禁止把所有字段机械等权相加。**

选择必须分层执行：

## Gate A｜HARD GATES

任一失败直接淘汰特殊Scene：

1. **Safety / Audience Gate**
2. **Product Truth Gate**
3. **Proofability Gate**
4. **DNA Activation Gate**

### DNA Activation Gate

问：

> 当前故事是否真的会触发该Scene的世界发动机、社会规则、权力结构或空间逻辑？

如果NO：

> 该空间最多保留为普通Location，不算调用Scene DNA。

---

## Gate B｜PRIMARY COMMERCIAL FIT

只有通过Hard Gates的候选继续比较：

1. **Decision Fit**：是否放大Core Decision Question
2. **Architecture Fit**：是否增强当前Primary Architecture，而非偷换Driver
3. **Proof Fit**：是否自然承载Best Proof
4. **Product Entry Fit**：商品是否无需硬塞即可进入

这四项是Scene选择的主判断。

如果特殊Scene在这里明显弱于NORMAL_LOCATION：

> 直接让NORMAL_LOCATION获胜，不允许靠视觉奇观追回。

---

## Gate C｜UNIQUE CAUSAL GAIN

每个特殊Scene候选必须能用一句话回答：

> **这个Scene提供了什么NORMAL_LOCATION和其他候选无法同样自然提供的因果优势？**

例如：
- S05不是“西部好看”，而是“商品通过社区公开实用测试改变人物信誉”；
- S07不是“商场真实”，而是“消费者可以合法并列试用、比较并改选”；
- S11不是“古代市场热闹”，而是“公开Claim、Rival挑战和群众判断共同改变价值判断”。

写不出明确`UNIQUE_CAUSAL_GAIN`：

> 特殊Scene降级；优先NORMAL_LOCATION。

---

## Gate D｜SECONDARY EXECUTION FIT

商业核心通过后，再比较：

1. **Character Fit**：目标人物是否自然成为该世界角色
2. **Reaction Fit / Reaction Signature**：Scene原生Reaction是否增强Decision Change
3. **Generation Risk**：人物、交接、空间、文字、尺度、产品变形风险是否在Complexity Budget内
4. **Native Conflict Fit**：世界冲突能否自然持续，而不是一次性装饰

若两个候选商业价值接近：

> 选择人物更少、交互更简单、空间更稳定、Proof更清楚的候选。

---

## Gate E｜TIE BREAK ONLY

只有前面接近时才看：

- Visual Distinctiveness
- Batch Diversity
- Camera novelty
- Optional Comedy / Absurdity compatibility

**Visual Distinctiveness不得用来补偿Decision / Architecture / Proof / Product Entry的不匹配。**

---

# 6. Reaction Signature｜12 Scene差异化签名

Reaction Signature用于Scene选择、Performance调制与Batch Diversity，不要求最终提示词原样输出。

| Scene | REACTION_SIGNATURE | 核心传播方式 |
|---|---|---|
| S01 宫廷 | HIERARCHY_CHAIN | 下位者→权威→主位→等级传播 |
| S02 高中 | PEER_SPREAD | 同伴快速扩散→老师/群体判断 |
| S03 军营 | COMMAND_CHAIN | 结果→Commander→新命令→执行链 |
| S04 办公室 | PROFESSIONAL_JUDGMENT | 结果→Manager/Client→职业判断改变 |
| S05 西部 | LONG_SILENCE_PERSONAL_REVISION | 长静→个人先改口→社区跟进 |
| S06 Gala | DISTRIBUTED_SOCIAL_GLANCES | 停杯/侧目/笑容轻僵→分布式认可 |
| S07 Mall | FLOW_STOP_GATHER | 走路减速→停步→重新拿起/改选 |
| S08 Future | SYSTEM_STOP_MANUAL_OVERRIDE | 系统停止→人工复核→Override/恢复 |
| S09 Diner | LATERAL_OVERHEARD_SPREAD | booth→Server→counter横向传播 |
| S10 Competition | HOST_RESULT_AUDIENCE | Result→Host/Judge→选手→Audience |
| S11 Market | BUYER_RIVAL_CROWD | Buyer→Rival→Crowd→购买判断 |
| S12 Train | LINEAR_CARRIAGE_SPREAD | 当前车厢→Attendant→相邻车厢→真主人 |

同批广告即使Scene ID不同，若Reaction Signature、SPACE_TOPOLOGY和Product Entry高度重复，也要施加Diversity Penalty。

---

# 7. Reversal Fit｜严格条件调用

- **R0**：不评分Reversal Fit；Scene不得主动添加误判、双证据、Micro Anomaly或180°
- **R1**：只检查Scene是否能自然表达已经确定的Clarification / Reveal / Surprise
- **R2**：才检查 `REVERSAL_COMPATIBILITY` 与 `SUPPORTED_REVERSAL_TYPES`

永远：

> **Scene支持R2 ≠ 本条应该R2。**

Scene Card里的“反转”字段只视为兼容资产；没有Reversal Router的R2许可，不得调用完整强反转DNA。

---

# 8. Diversity Penalty

同批多条广告对以下重复项降权：

- Scene ID重复
- PRIMARY_CLASS重复
- SECONDARY_CLASS_TAGS高度重复
- REACTION_SIGNATURE重复
- SPACE_TOPOLOGY重复
- Product Entry机制重复

但Diversity永远不能覆盖商业匹配度。

---

# 9. Special Scene Value Check｜最终净收益

最后比较：

`NORMAL_LOCATION`
VS
`最佳SPECIAL_SCENE_DNA`

特殊Scene必须至少明显增强以下一项：

- 商业理解
- Primary Architecture
- Best Proof
- Product Entry因果
- Reaction / Decision Change
- 有效视觉记忆

同时不能造成不可接受的：

- Proof损失
- Product Truth污染
- 人物/空间/交接复杂度
- 产品变形
- 合规/IP风险

如果净收益不明确：

> **NORMAL_LOCATION获胜。**

---

# 10. Router Prior｜人工Sanity Check

> 当前12个Scene均已完成结构化Index迁移。本节只用于快速人工理解与异常复核，不能覆盖结构化路由。

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

---

# 11. Scene Safety Gate｜硬阻断

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
默认可使用Social/Ownership Mystery，但不得因为Scene本身自动添加R2，也不自动添加谋杀、侦探、枪械、毒药等犯罪悬疑。

---

# 12. Product × Scene Compilation｜世界原生化，不重写上游决策

选择特殊Scene后，上游已经锁定：

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
→ `Performance/FACS按Scene调制`
→ `CTA`

### R0
Scene不得添加错误答案、双误导证据、Micro Anomaly或180°。

### R1
只世界原生化已经确定的Clarification / Reveal / Surprise，不升级R2。

### R2
只有Reversal Router已经确定R2时，才从Scene兼容资产中寻找世界原生表达；不增加第二套反转，不挤压Best Proof。

核心检查：

> **同一个商品、同一个Primary Architecture换Scene后，人物身份、冲突呈现、Product Entry、动作、Dialogue、Reaction、节奏、镜头应明显改变；但Primary Driver、Best Proof和R-level不得被改写。**

若只是换背景，Scene DNA调用失败。

---

# 13. DNA Activation Test｜Location ≠ Scene DNA

选定Scene后必须问：

1. 当前故事是否触发该Scene至少一个关键世界规则？
2. 这个规则是否真的改变人物为什么行动？
3. Product Entry是否利用了这个世界，而不是普通桌面露出？
4. Reaction是否来自这个世界的社会/空间规则？

如果主要答案为NO：

> 保留Location可以，但退出完整Scene DNA调用。

例：
- 两个人坐办公室聊天 ≠ S04 Office DNA
- 人物在豪华列车包厢聊天 ≠ S12 Train DNA
- 穿古装站宫殿里介绍产品 ≠ S01 Court DNA

---

# 14. Scene Independence Test

正式故事生成前回答：

1. 删除商品，这个Scene中的人物为什么本来就会产生事件/冲突？
2. 商品加入后，是利用了该世界规则，还是中途插播？
3. 把特殊Scene换成普通客厅后，故事是否几乎不用改？

若第1题答不出，或第3题为“是”：

> 特殊Scene DNA失败；重写或回退NORMAL_LOCATION。

---

# 15. Generation Complexity Gate

Scene选择不能只看创意价值，还要看生成预算。

重点判断：
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

Scene Card中的人物池只是可选角色资源，不是人数要求；任何旧固定人数描述都不得覆盖最低必要人物原则。

如果两个Scene商业增益接近：

> 选择人物更少、交互更简单、空间更稳定的那个。

---

# 16. Cross-Product Stability / Validation

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

测试结果写入 `scene-validation-registry.md`。

`scene-dna-library.md`中的结构QA只算 `INTERNAL_PASS`，不等于实际生成PASS。

VALIDATED升级必须满足Registry全部硬条件；关键项FAIL或NOT_TESTED时继续保持TESTING。

---

# 17. Router最终输出｜内部

```text
SCENE MODE:
NORMAL_LOCATION / SPECIAL_SCENE_DNA

SELECTED SCENE:
<若SPECIAL则填Sxx>

WHY:
<为什么它比其他候选更适合商业问题>

UNIQUE CAUSAL GAIN:
<该Scene不可替代的因果优势；NORMAL_LOCATION可写“无需特殊世界即可更清楚证明”>

DNA ACTIVATION:
<被触发的世界规则>

PRODUCT ENTRY:
<Scene原生入口>

REACTION SIGNATURE:
<若SPECIAL则填对应签名；NORMAL_LOCATION填NATURAL_RELATION_REACTION>

R-LEVEL PRESERVATION:
R0 / R1 Clarification / R1 Reveal / R1 Surprise / R2

CONTINUITY ANCHORS:
<最少必要空间锁定>

GENERATION RISK:
<主要风险>
```

普通用户默认不需要看到这张卡。

---

# 18. 最终原则｜FREEZE

- NORMAL_LOCATION是正式Candidate 0，不是失败方案。
- Scene是可选增强，不是必经步骤。
- Safety / Truth / Proofability / DNA Activation是Hard Gates。
- Decision / Architecture / Proof / Product Entry是Primary Fit，不能被视觉分数抵消。
- 每个特殊Scene必须说得清Unique Causal Gain。
- Reaction Signature参与Scene选择、Performance调制与Batch Diversity。
- Story Architecture决定因果骨架；Scene不能偷换Primary Driver。
- Proof已经先锁；Scene不能为了视觉奇观挤压或伪造Proof。
- R0/R1/R2已经先锁；Scene不能自动升级反转。
- Location不等于Scene DNA；必须触发世界规则。
- 特殊Scene必须赢过NORMAL_LOCATION，才值得增加生成复杂度。
- Scene Index负责检索，DNA Library负责执行，Validation Registry负责证据状态。
- **Scene的价值不是背景有多漂亮，而是换了这个世界以后，人物为什么行动、怎么行动、怎么反应、怎么拍都真正改变。**
