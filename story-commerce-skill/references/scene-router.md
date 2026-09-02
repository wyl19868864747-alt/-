# SCENE ROUTER｜剧情带货场景路由

> 目标：让剧情不再只是“商品 + 随机故事 + 换背景”，而是严格执行：
>
> `Product DNA × Scene DNA → Story → Seedance Prompt`

## 0. 总原则

Scene 不是美术风格标签，而是一套会改变人物身份、社会规则、天然冲突、动作、对白、表演、镜头、节奏、反转和商品进入方式的世界规则。

核心测试：

> **如果完全没有商品，这个世界里的人原本会因为什么产生冲突？**

回答不清楚，Scene 不成立。

任何 Scene 都必须服从：

`用户明确要求 > 商品事实/SKU/参考资产 > 合规与安全 > 主决策问题 > 可证明Proof > Scene适配 > 剧情与反转 > 美术风格`

Scene 不能改写商品事实。永远：

> **PRODUCT LOCK > SCENE STYLE**

现代商品进入历史/未来世界时，外观、颜色、比例、包装、结构和真实能力保持不变；Scene 只能改变“人物如何理解它、为什么冲突、怎么验证、怎么拍”。

---

# 1. Scene Status

当前正式候选库共12个Scene，全部处于：

`TESTING_CANDIDATE`

尚无任何Scene标记为`VALIDATED`。只有实际通过Seedance跨商品稳定测试、空间连续测试、产品一致性测试、动作物理测试后，才允许升级。

| ID | Scene | 核心发动机 | 状态 | 特殊限制 |
|---|---|---|---|---|
| S01 | 架空古装宫廷 | 身份 / 礼仪 / 权力 | TESTING_CANDIDATE | generic royal court |
| S02 | 现代美国高中 | 同伴 / 社交评价 / 公开尴尬 | TESTING_CANDIDATE | 18+演员；敏感商品禁入 |
| S03 | 架空古代战争军营 | 任务 / 命令 / 时间压力 | TESTING_CANDIDATE | No-Weapon Commercial Rule |
| S04 | 现代美国企业办公室 | Deadline / 结果 / 职业体面 | TESTING_CANDIDATE | generic corporate world |
| S05 | 架空美国西部边疆贸易小镇 | 名声 / 实用价值 / 公开检验 | TESTING_CANDIDATE | No-Weapon Commercial Rule |
| S06 | 架空现代豪华上流晚宴 | 品味 / 身份 / 社会认可 | TESTING_CANDIDATE | 不崇拜阶级、不仿真实Gala |
| S07 | 现代美国大型购物中心 | 比较 / 选择 / 注意力 | TESTING_CANDIDATE | generic stores/无虚构促销 |
| S08 | 架空未来都市·星际商业世界 | 系统分类 / 权限 / 效率 | TESTING_CANDIDATE | WORLD TECH ≠ PRODUCT FACT |
| S09 | 架空复古美国公路Diner | 误听 / 熟客社会 / 横向传播 | TESTING_CANDIDATE | 包容性呈现，不浪漫化隔离历史 |
| S10 | 架空高压真人竞赛节目 | 规则 / 时间 / 公开结果 | TESTING_CANDIDATE | 仅可视Proof；非博彩/抽奖 |
| S11 | 架空古代地中海公共市集 | 公开叫卖 / 商人竞争 / 群众判断 | TESTING_CANDIDATE | 不混搭文明/宗教刻板印象 |
| S12 | 架空复古豪华长途列车 | 封闭移动 / 归属 / 车厢顺序 | TESTING_CANDIDATE | 不仿Orient Express；非谋杀悬疑 |

---

# 2. Scene Selection｜选择规则

## 2.1 用户明确指定Scene

用户明确选择Scene时，优先使用该Scene，不擅自换成历史高频模板。

仅在以下情况允许阻断或改路由：
- Scene与商品/受众存在明显合规冲突；
- 商品无法自然进入且必须严重歪曲事实才能成立；
- Scene会迫使不可证明卖点变成伪Proof；
- 用户Scene要求与真实参考资产/物理事实冲突。

发生阻断时，保留用户想要的核心风格，改用最接近且安全的Scene，不硬塞。

## 2.2 用户未指定Scene

静默完成Scene Fit Scoring，每项0–2分：

1. **Decision Fit**：是否天然放大主决策问题
2. **Proof Fit**：是否能自然形成真实视觉Proof
3. **Native Conflict Fit**：无商品时是否已有天然冲突
4. **Product Entry Fit**：商品是否无需硬塞即可进入
5. **Character Fit**：目标人群是否自然成为该世界角色
6. **Reversal Fit**：Scene原生反转是否服务主犹豫
7. **Visual Distinctiveness**：相较同批内容是否明显不同
8. **Safety Fit**：平台、年龄、IP、敏感品类风险

先淘汰任何Safety Gate失败Scene；从剩余Scene中选择综合最高者。

同批多条广告必须增加“Scene Diversity Penalty”：已使用的Scene、相近空间和相同Reaction机制降权，避免批量作品换商品不换脑子。

---

# 3. Router Prior｜按主决策/Proof倾向推荐

这只是先验，不是硬匹配。

## 身份、穿搭、品味、社交接受
优先候选：
- S06 豪华晚宴
- S02 美国高中（仅适合安全普通商品）
- S07 现代商场
- S01 古装宫廷（适合时代错位/地位反转）

## 效率、工作流、操作步骤、问题解决
优先候选：
- S04 现代办公室
- S08 未来商业世界
- S03 古代战争军营
- S10 真人竞赛（仅可短时验证）

## 耐用、实用、现场结果、机制Proof
优先候选：
- S05 西部小镇
- S11 古代市集
- S10 真人竞赛
- S03 古代战争军营

## 比较、试用、选择、购买决策
优先候选：
- S07 现代商场
- S11 古代市集
- S05 西部小镇

## 归属、旅行、便携、随身使用
优先候选：
- S12 豪华列车
- S09 复古Diner
- S07 现代商场

## 误会、轻喜剧、信息传播
优先候选：
- S09 复古Diner
- S02 美国高中
- S06 豪华晚宴
- S12 豪华列车

## 强时代错位/视觉奇观
优先候选：
- S01 古装宫廷
- S03 古代战争军营
- S05 西部小镇
- S08 未来商业世界
- S11 古代市集
- S12 豪华列车

---

# 4. Scene Safety Gate｜硬阻断

## S02 现代美国高中
默认使用18岁以上成年演员扮演毕业班学生。
禁止把以下商品/主题路由到高中：
- 成人药品、减重/GLP-1等医疗内容
- 酒精、烟草、尼古丁
- 赌博/博彩
- 成人约会/性产品
- 武器
- 其他明显年龄限制/不适合未成年校园语境的商品

## S03 古代战争军营
战争感通过军帐、地图、补给、传令、队列、Deadline建立。
禁止以刀枪、射击、砍杀、伤口、尸体、爆炸杀伤建立Scene。
不用于真实武器/军火商品。

## S05 西部边疆小镇
保留Western Standoff Composition，不保留Gunfight。
枪械、弹药、拔枪、射击、血腥不是商业Scene资产。
不使用原住民族刻板印象或真实历史人物。

## S06 豪华晚宴
不复制Met Gala、真实奢侈品牌、名人、慈善组织。
不把贫穷、出身、族裔、口音当笑点；“高端”只表示社交规则和视觉质感，不表示阶级优越。

## S08 未来商业世界
环境可以有未来技术，但商品不能获得真实SKU不存在的未来功能。
严格分离：
`WORLD TECH ≠ PRODUCT FACT`
禁止自动添加AI、全息、扫描、医疗检测、自动感应等产品能力。

## S09 复古Diner
借mid-century视觉和空间语法，不复制真实种族隔离制度或民权事件，不使用真实餐饮/饮料品牌。

## S10 真人竞赛
Challenge必须由真实可证明属性反推：
`Verified Product Fact → Visible Task → Fair Rule → Observable Result`
禁止危险挑战、赌博、彩票、购买即抽奖、虚假比分、未经证实的百分比/#1/best声明。
长期舒适、长期耐用、医学效果、精确续航等不可用15秒比赛“证明”。

## S11 古代市集
保持统一架空地中海古典视觉，不混搭无关文明，不使用真实宗教仪式、人口交易或文化刻板印象。

## S12 豪华列车
不复制Orient Express、Pullman等真实高识别品牌/车型/路线。
默认Social/Ownership Mystery，不自动添加谋杀、侦探、枪械、毒药等犯罪悬疑。

---

# 5. Product × Scene Compilation

选择Scene后，不得直接套Scene故事模板。

必须依次编译：

`Product Decision Card`
→ `锁1个主犹豫`
→ `锁1个可证明Proof`
→ `选择Scene`
→ `读取Scene原生冲突`
→ `让主犹豫在Scene规则中变成事件`
→ `选择Scene原生错误预判`
→ `至少2个可见证据强化`
→ `商品进入Scene原生入口`
→ `真实Proof`
→ `Scene原生反转/Reaction`
→ `CTA`

核心检查：

> **同一个商品换Scene后，人物身份、冲突原因、商品入口、动作、对白、Reaction、节奏、镜头、反转必须明显不同。**

若只是背景从办公室换成宫廷，但故事、台词、动作基本一样，Scene Router失败，返回重写。

---

# 6. Scene Independence Test

正式故事生成前，内部回答：

1. 如果删除商品，这个Scene中的人物为什么本来就会发生冲突？
2. 商品加入后，是利用了这个冲突，还是中途插播？
3. 把场景替换成普通客厅后，故事是否几乎不用改？

若第1题答不出，或第3题答案为“是”，Scene使用失败。

---

# 7. Cross-Product Stability Test

Scene进入正式VALIDATED前，至少使用三类差异商品实测：
- 3C：如无线耳机
- 服装：如现代女装外套
- 日用品：如便携清洁用品

三类都必须保持：
- 同一世界规则
- 不同但Scene原生的剧情
- PRODUCT LOCK
- 真实Proof
- 不穿模
- 空间一致
- 不因时代/风格重设计商品

不能成立的Scene继续保持TESTING，不强行升Validated。

---

# 8. Validated升级条件

单Scene只有同时通过以下项目才能从`TESTING_CANDIDATE`升级为`VALIDATED`：

- [ ] 三类跨商品生成成功
- [ ] Scene核心世界一眼可识别
- [ ] 不依赖真实IP/Logo
- [ ] PRODUCT LOCK跨镜稳定
- [ ] 关键道具交互无明显穿模
- [ ] 空间轴线/入口/人物位置稳定
- [ ] Scene原生Reaction能准确执行
- [ ] 换商品后仍保持同一栏目感
- [ ] 换Scene后同一商品故事明显改变
- [ ] Safety Gate通过

当前12个Scene全部尚待这一阶段，不得提前标记Validated。
