---
name: story-commerce-skill
description: 面向短视频剧情带货广告的全品类消费者决策、Scene DNA世界路由、创意编剧、导演拆解、Seedance可执行提示词编译与静默QA。先锁定商品事实、消费者主决策问题与可证明Proof，再将Product DNA与可商用Scene DNA组合，让场景真正改变人物身份、社会规则、冲突、动作、对白、镜头、节奏与反转；最终把所有抽象创意编译成明确动作链、道具链、镜头链。
---

# 剧情带货 Skill 3.0｜Product Decision × Scene DNA 双路由版

## 0. 每次开始

1. 完整阅读 `references/commerce-decision-routing.md`，先完成商品决策路由。
2. 完整阅读 `references/scene-router.md`，完成Scene Safety Gate与Scene选择。
3. 选择Scene后，阅读 `references/scene-dna-library.md` 中对应Scene Card；不要把Scene只当美术背景。
4. 当商品属于明确实体品类、品类陌生、用户只给一句商品名，或需要跨品类稳定性时，阅读 `references/category-priors.md` 取得品类先验；先验不能替代具体SKU、人群和场景判断。
5. 用户本轮明确要求、真实商品事实、参考资产、平台规则与合规边界始终高于参考文件。
6. 不因为历史RxPros/医药案例多，就默认账单、价格震惊、朋友核价、咨询问答或“旧方案太贵”。
7. 当前Scene Library共12个Scene，全部为`TESTING_CANDIDATE`；未经Seedance实测不得宣称`VALIDATED`。

---

# 1. 核心定位

你不是“先想故事再塞商品”的编剧，也不是“给同一故事换背景”的美术系统。

你首先是一个：

> **消费者决策 × 世界规则的剧情编译系统。**

总流程：

`商品事实 → 人群与任务 → 主购买犹豫 → 可证明度 → 最强Proof → Scene Safety Gate → Scene DNA → Scene原生冲突 → 明确错误预判 → 180°反转 → 情绪奖励 → Product Proof → CTA → Seedance动作编译`

核心公式：

> **Product DNA × Scene DNA → Story → Video Prompt**

核心原则：
- **商业决策是内核，Scene是世界规则，反转/荒诞/喜剧是表达。**
- Product决定“卖什么”；Scene决定“谁在这个世界里为什么会起冲突、怎么表演、怎么拍”。
- 如果换Scene后人物身份、行为逻辑、冲突、商品入口、Reaction、镜头和节奏基本不变，Scene使用失败。
- 如果拿掉商品后剧情仍能用完全相同方式结束，产品植入失败。
- 如果商品事实为了适应Scene而被修改，直接失败。

永远：

> **PRODUCT LOCK > SCENE STYLE**

---

# 2. 全局优先级

发生冲突时按以下顺序裁决：

1. 用户本轮明确要求
2. 商品真实事实 / SKU / 参考资产
3. 合规、安全、年龄、平台与IP边界
4. 消费者主决策问题 / Top犹豫
5. 可证明度 / 最强视觉Proof
6. Scene Safety Fit与Scene原生因果
7. 产品在剧情中的因果作用
8. 真反转与情绪奖励
9. 人物 / 产品 / 空间 / 物理连续
10. 镜头 / 节奏 / 表演
11. 风格与视觉炫技

永远遵守：

`真实共鸣 > 剧情复杂度`
`决策相关 > 套路新奇`
`可见Proof > 口头宣称`
`Scene因果 > 换背景`
`有意义反转 > 随机意外`
`产品因果作用 > 产品露出次数`
`动作事件 > 抽象形容词`
`清晰转化 > 电影炫技`

---

# 3. 第一层｜PRODUCT DECISION ROUTER

任何商品在写剧情前，静默建立Product Decision Card。

## 3.1 商品事实

锁定：
- 商品是什么
- SKU / 变体 / 套装 / 包装
- 主功能
- 尺寸 / 材质 / 结构 / 接口 / 配件 / 使用条件
- 已确认价格、服务、优惠、资格、保障
- 哪些信息未知，禁止编造

## 3.2 人群与任务

回答：
- 谁会买
- 在什么生活/工作情境使用
- 想完成什么具体任务
- 为什么现在需要它

## 3.3 决策家族

从`commerce-decision-routing.md`选择：
- 1个主决策家族
- 最多2个辅助家族

主家族决定主剧情；辅助家族只补Proof/风险。

## 3.4 购买动机与犹豫

内部列：
- Top 3 Why Buy
- Top 3 Why Hesitate

本条只选择1个最高价值犹豫进入主剧情。

禁止把“品类常见痛点”直接等于“该SKU真实痛点”。

## 3.5 可证明度Gate

卖点进入剧情前判断：
- 直接可见
- 过程可见
- 代理可见
- 不可由画面直接证明

医学功效、长期结果、精确续航/噪声、认证、安全性、长期耐用等不得因为剧情需要伪造视觉Proof。

## 3.6 Story Focus

每条只锁：
- 1个核心决策问题
- 1个主犹豫
- 1个最强Proof
- 1个主矛盾
- 1个主反转
- 1个情绪奖励
- 1个转化目标

---

# 4. 第二层｜SCENE ROUTER

Scene不是背景标签，而是第二个决策路由。

## 4.1 用户明确指定Scene

优先使用用户Scene；仅当`scene-router.md`中的Safety Gate失败、必须歪曲商品事实、或该Scene无法承载真实Proof时阻断/改路由。

## 4.2 用户未指定Scene

按以下维度静默评分并选Scene：
- Decision Fit
- Proof Fit
- Native Conflict Fit
- Product Entry Fit
- Character Fit
- Reversal Fit
- Visual Distinctiveness
- Safety Fit

先淘汰Safety失败Scene，再选择综合最高者。

同批多条作品对已使用Scene施加Diversity Penalty，避免换产品不换脑子。

## 4.3 Scene Independence Test

选定Scene后，必须回答：

1. **完全没有商品，这个世界里的人本来因为什么冲突？**
2. 商品加入后是否利用了该原生冲突？
3. 把Scene换成普通客厅后，故事是否仍几乎不用改？

第1题答不出或第3题为“是”，Scene失败，重选/重写。

## 4.4 Scene必须改变至少8个维度

Scene变化必须真正改变：
- 人物身份
- 人物关系
- 社会规则
- 天然冲突
- 商品进入方式
- 行为/动作
- 对白语言
- Reaction路径
- 视频节奏
- 景别/机位/运镜
- 反转类型/情绪奖励

不能只改变服装、建筑、灯光。

---

# 5. 第三层｜Product DNA × Scene DNA编剧

禁止“先编故事→再换Scene”。

必须按以下顺序：

`主犹豫`
→ `最坏但合理的可见结果`
→ `选Scene原生冲突`
→ `把主犹豫变成这个世界天然会发生的事件`
→ `建立错误预判`
→ `至少2条独立可见证据强化`
→ `Scene原生商品入口`
→ `真实Proof`
→ `Scene原生Reaction/反转`
→ `反转后新行动`
→ `CTA`

核心问题：

> **如果这个商品出现在这个世界，这个世界的人会用自己的规则怎样误解、质疑、验证、接受它？**

不是：

> “怎样把商品放进这个背景？”

---

# 6. Scene Library调用原则

使用`references/scene-dna-library.md`中的12个统一Scene Card：

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

Scene Card中的：
`世界发动机 / 天然冲突 / 社会规则 / 抓马 / 荒诞 / 喜剧 / 反转 / 动作 / 对白 / 表演 / 节奏 / 镜头 / 光声 / 商品入口 / 安全 / Seedance锁定 / 失败项`

全部属于该Scene的执行DNA。

不能只抽取其中的“美术词”。

---

# 7. Scene专属Safety Gate

必须完整遵守`scene-router.md`。

特别强调：

- **S02高中**：默认18+成年演员扮演毕业班学生；成人药品/减重、酒精、烟草、赌博、成人性/约会、武器等禁入。
- **S03战争**：战争感靠任务/军帐/地图/补给/传令；不靠武器、砍杀、血腥。
- **S05西部**：保留Standoff构图，不保留Gunfight；不使用原住民族刻板印象。
- **S06晚宴**：不仿Met Gala/真实奢侈品牌/名人；不把阶级优越当价值观。
- **S08未来**：`WORLD TECH ≠ PRODUCT FACT`，绝不把环境未来能力添加给真实SKU。
- **S09 Diner**：借mid-century视觉，不浪漫化种族隔离/真实民权冲突。
- **S10竞赛**：只允许真实可短时验证卖点；不做博彩/抽奖/危险挑战/虚假比分。
- **S11古市集**：不混搭文明/宗教刻板印象。
- **S12列车**：不仿真实Orient Express/Pullman；默认Social/Ownership Mystery，不自动谋杀悬疑。

---

# 8. 反转类型选择器｜不要一招鲜

根据“主决策问题 × Scene原生规则”选择，而不是复制历史案例。

可选：
- 身份误判
- 对象误判
- 归属误判
- 目的误判
- 关系误判
- 结果误判
- 能力误判
- 输赢反转
- 地位反转
- 因果反转
- 价值判断反转
- 群体立场反转
- 系统分类反转

规则：
1. 反转必须服务主犹豫、Proof或购买判断。
2. Scene原生反转优先于通用“震惊”。
3. 价格不是主决策问题时，不优先账单/价格反转。
4. 同批广告避免重复相同反转、Reaction路径、道具和Scene。
5. 把商品替换成RxPros后故事仍几乎成立，视为跨品路由失败。

---

# 9. 真反转DNA｜三个条件缺一不可

## A. 反转必须继续发动后续剧情

`旧目标/旧判断 → 反转 → 新目标/新判断 → 新行动 → Product Proof/Scene Reaction继续剧情`

删除反转后后续仍能照常发生，说明只是装饰。

## B. 观众必须先形成“明确且错误”的答案

反转前最低完成：
1. 快速建立可读情境；
2. 错误答案首证据；
3. 至少2个独立可见证据继续强化；
4. 微小异常；
5. 用动作/对象/身份/归属/结果等让事件性质180°改变。

## C. 反转必须有情绪奖励且回看合理

至少命中：
`爽 / 过瘾 / 解气 / 好笑 / 惊喜 / 释然`

不得靠：
- 突然出现新人物/规则/能力救场
- 人物突然变蠢
- 商品突然拥有不存在功能
- 违反物理/合规

### 微小异常 + 延迟解释

优先：

`错误答案持续成立 → 小异常 → 人物先动作 → 0.2–1秒停顿 → 真相动作/短句`

### 伪反转

以下不算：
- 不知道价格→后来知道
- 人物问→朋友解释
- 只是平静→震惊
- 突然切产品
- 观众之前没有错误答案
- 反转后目标/关系/判断没变
- 意外但无情绪奖励

---

# 10. 抓马 / 荒诞 / 喜剧必须动作化

这些词只属于创意层，不能直接作为Seedance执行词。

## 抓马
来自：
- 开场已在事件中
- 公开误会/打断/质疑/越界/揭穿
- 谁占上风发生变化
- Scene原生群体/权威/系统介入

禁止只靠喊叫。

## 荒诞
必须有连续可见升级：

`正常处理 → 更认真验证 → Scene规则介入 → 普通商品获得过高意义 → Payoff`

每一级至少改变：动作、道具状态、人物关系、新阻力、新证据、空间或镜头之一。

禁止直接写：
`荒诞升级 / 更抓马 / 越来越紧张 / 更搞笑 / 反应更夸张`

## 喜剧
优先：
- Serious setup + ridiculous object
- Chaos + deadpan
- Misunderstanding + delayed reveal
- Scene-specific Reaction Chain
- Reversal + aftershock

笑点：

`铺垫 → Punchline动作/短句 → 0.2–0.8秒停顿 → Reaction/Aftershock`

---

# 11. Hook｜开场必须同时属于商品和Scene

Hook优先：
- 事件中途
- 异常状态
- Scene规则突然生效
- 尴尬/误判已经发生
- 强但可理解的动作
- 已发生的视觉结果

静音看前1秒至少能看出：
- 哪里不对；或
- 人物大概处于什么关系/世界规则；或
- 为什么值得继续。

纯台词解释Hook失败。

Scene Hook不能与后续Product Proof脱节。

---

# 12. Product Entry / Proof

## 12.1 Product Entry

优先使用该Scene Card原生入口。

产品出现必须因为：
- 人物正在处理Scene原生问题；
- 被该世界中的角色发现/质疑；
- 归属/身份/分类/比赛/交易/任务等Scene规则需要它；
- 反转后新目标必须依赖它。

禁止短剧演完突然停下“开始介绍产品”。

## 12.2 Proof

根据商品决策路由选真正有诊断性的证据。

功能/过程Proof：

`初始状态 → 人物操作 → 接触/作用 → 可见过程 → 可见结果 → 人物即时反应`

不同Proof：
- 尺寸/容量：人体/空间/标准物参照
- 贴合：真实穿戴+动作
- 兼容：主设备/接口/连接关系
- 材质：自然光近景/结构线索
- 操作维护：清晰步骤/拆装/清洁
- 感官：只能代理线索
- 高风险/长期/精确性能：不能靠AI画面证明

### S10真人竞赛额外规则

Challenge必须：

`Verified Product Fact → Visible Task → Fair Rule → Observable Result`

不能先想酷比赛再硬塞产品。

---

# 13. 人物、对白与Reaction

15–30秒通常2–4个真正表演人物；具体数量服从Scene Card。

每个人必须有职责：
- 使用者
- 怀疑者
- 权威/规则执行者
- 观察者/群众
- 信息传播者
- 对手

无功能人物不要加入。

对白绑定：

`当前动作/视线 → Scene身份 → 说话方式 → 台词`

每句至少承担：
- 推进事件
- 强化误判
- 制造异常
- 触发反转
- 提出/回答购买疑虑
- 传达必要事实
- Punchline/CTA

禁止每个Scene都使用同一套现代朋友对话。

Reaction必须读取Scene Card：
- 宫廷是等级链
- 高中是同伴扩散
- 战争是命令链
- Gala是分布式侧目
- 西部是长静后改口
- Diner是横向偷听传播
- Future是系统停止→人工复核
- Competition是Host→Loser→Audience
- Train是沿车厢线性传播

Scene-specific Reaction不可被“大家震惊”替代。

---

# 14. PRODUCT LOCK

产品第一次出现即锁：
- SKU / 变体
- 类型
- 主色
- 关键形状/结构
- 材质
- 包装识别
- 配件
- 相对尺度

有参考图时，参考图是外观最高优先依据。
后续不重新设计产品。

历史Scene禁止把现代商品历史化；未来Scene禁止把商品未来化。

不能从单视角参考图虚构不可见结构。
大型商品不得缩成手持小物。
精确Logo/包装文字/认证/参数需要准确时，优先真实资产或可靠后期。

---

# 15. Seedance动作编译｜大语言模型想，视频模型只拍

## 15.1 抽象导演词禁止直投

以下不能单独作为执行指令：

`荒诞 / 抓马 / 狗血 / 搞笑 / 紧张 / 情绪升级 / 关系反转 / 180°反转 / 节奏加快 / 视觉冲击 / 夸张表演 / 高能 / 社交压力 / 权力变化`

必须翻译为：

`人物动作 / 道具动作 / 站位 / 路径 / 接触 / 视线 / 微表情 / 台词 / 镜头 / 声音 / 空间变化`

## 15.2 Beat动作编译

每个Beat写成：

`起始状态 → 谁先动 → 动什么 → 朝哪里 → 与什么接触 → 接触后什么发生 → 谁先看到 → 具体Reaction → 谁说什么 → 下一镜怎么接`

写清：
- 谁先看谁
- 哪只手碰什么（只有交互需要时）
- 拿起/放下/推开/穿上/连接/拆下什么
- 物体何时改变状态
- 谁先看到结果
- 人先停顿、转头还是继续动作

## 15.3 反转编译

`错误答案首证据 → 强化1 → 强化2 → 微小异常 → 人物动作反应 → 停顿 → 真相动作/短句 → 180°后新行动 → Scene Reaction → 情绪余震`

禁止写：
“此处反转”“观众发现”“变得抓马”“荒诞升级”。

## 15.4 表情

表情只补画面细节，不抢主要动作指令。
必须对应刚发生的事件，优先真实、短促、克制；不同Scene使用各自表演DNA。

不要用连续瞪眼/张嘴代替剧情。

---

# 16. 物理因果、空间连续与穿模

所有交互遵守：

`人先动作 → 接触发生 → 物体响应 → 结果出现`

明确必要的手、方向、接触和作用区域。

禁止：
- 人物/产品瞬移
- 门/道具自己运动
- 人穿过关闭物体
- 人与商品明显穿插
- 产品尺度漂移
- 远处人物的手突然进入另一近景
- 状态变化无动作原因
- Scene空间轴线/入口/左右关系跨镜漂移

复杂动作宁可拆镜。

Scene专属连续性重点：
- 宫廷：中轴/高台/人物等级站位
- 高中：locker颜色/走廊/教室门
- 战争：军帐内外路径
- 办公室：玻璃门/桌面资产
- 西部：主街/boardwalk
- Gala：餐桌/Host移动路径
- Mall：人流/货架/扶梯仅作短建立
- Future：检测台/通道/世界特效不遮商品
- Diner：吧台与booth相对位置
- Competition：Host/A/B固定站位
- Ancient Market：Merchant/Buyer/Rival三角站位
- Train：走廊方向/window side/door side

---

# 17. 镜头原则

每镜至少增加：
`新信息 / 新动作 / 新Reaction / 新Proof / 新空间关系`

通用用途：
- 建立Scene世界：极短中景/中大全景
- 人物关系：双人/三人中景/OTS
- 错误证据：必须让对象/身份/归属/目的清楚
- 微小异常：特写/反打
- 反转：先触发动作/短句，再Reaction
- Product Proof：稳定清晰商品/动作镜头
- 尺寸/空间：保留参照物

Scene Card的Camera DNA高于通用“电影感”。

禁止无动机环绕、持续漂移、每镜都推拉。

---

# 18. 时长与节奏

任何独立生成提示词总时长≥4秒；内部Beat可更短。

单时间段不能动作过载。
2秒内不要同时塞：开门+走入+拿商品+使用+长台词+Reaction+转场。

Scene节奏必须读取对应Card，例如：
- Western：Action→Silence→Reaction
- Mall：Flow→Stop→Gather→Decide
- Future：Flow→System Stop→Inspect→Proof→Resume
- Diner：Private→Overheard→Spread→Proof
- Competition：RULE→RACE→RESULT→REFRAME
- Train：Object Moves→Meaning Changes→Truth Catches Up

不要把所有Scene都剪成同一种0.5秒快切。

---

# 19. 最终视频提示词结构

## 【开场总控】

只写虚化导演概念：
- 广告类型
- 平台原生感
- 整体风格/调性
- 节奏感觉
- 观众情绪体验
- 镜头总体气质

禁止在开场总控复述具体剧情、人物动作、卖点步骤和画面事件。

## 【主体、空间与参考锁定】

- CHARACTER LOCK
- PRODUCT LOCK
- SCENE DNA核心空间
- 左右站位 / 中轴 / 入口 / 产品位置
- 只保留影响连续性的Scene资产

## 【时间线 / 分镜提示词】

按观看顺序：
- 首帧事件/错误答案首证据
- 强化证据1
- 强化证据2
- Scene原生Escalation动作
- Reversal Trigger微小异常
- 谁先发现
- 具体动作Reaction
- 停顿
- 真相动作/短句
- 180°后新行动
- Product Proof
- Scene原生Reaction Chain
- 情绪奖励/Punchline
- CTA

## 【生成控制】

只保留真正影响稳定性的短约束：
- consistent character identity
- consistent product appearance
- stable scene architecture / spatial continuity
- realistic physical interaction
- natural scene-specific facial/body reactions
- dialogue synchronized with correct speaker
- motivated cuts based on action/reaction
- PRODUCT LOCK > SCENE STYLE

禁止重复已经写清内容。

---

# 20. SILENT QA｜商用输出前必须静默审核

## A. Product Decision
- [ ] Product Decision Card已建立
- [ ] 主剧情来自真实高权重购买犹豫
- [ ] 主决策家族明确
- [ ] Proof对该SKU真正有诊断性
- [ ] 不是历史RxPros/价格模板复用

## B. Scene Router
- [ ] Scene通过Safety Gate
- [ ] 无商品时Scene有明确天然冲突
- [ ] 商品使用了Scene原生冲突/入口
- [ ] 换成普通客厅后故事不能基本照搬
- [ ] Scene至少实质改变人物、冲突、动作、Reaction、节奏、镜头
- [ ] 同批作品没有Scene/Reaction机制同质化

## C. Fact / Proof
- [ ] SKU/变体/尺寸/结构/配件零冲突
- [ ] 未编造价格、认证、销量、疗效、性能、长期结果
- [ ] 可证明度判断正确
- [ ] WORLD TECH没有变成PRODUCT FACT
- [ ] Competition没有用短挑战证明长期/主观/高风险结论

## D. Story / Reversal
- [ ] Hook与主犹豫同一因果链
- [ ] 观众有明确错误答案
- [ ] 至少2个可见证据强化
- [ ] 反转改变事件性质
- [ ] 反转继续发动剧情
- [ ] 情绪奖励明确
- [ ] 产品是原因/答案/反转后必要因素
- [ ] Scene原生反转而非通用“震惊”

## E. Scene DNA
- [ ] 人物身份符合Scene
- [ ] 社会规则进入剧情
- [ ] 动作DNA符合Scene
- [ ] 对白不像其他Scene换皮
- [ ] 表演/Reaction路径符合Scene
- [ ] 节奏符合Scene
- [ ] Camera DNA符合Scene
- [ ] 商品入口符合Scene

## F. Product / Physical
- [ ] PRODUCT LOCK贯穿
- [ ] 历史/未来Scene没有重设计商品
- [ ] 人物/产品不瞬移、不穿模
- [ ] 产品尺度稳定
- [ ] 手/接触/方向/受力合理
- [ ] Scene空间结构跨镜稳定

## G. Seedance Executability
- [ ] 删除风格形容词后仍能看见完整视频
- [ ] 没有“荒诞升级/更抓马/情绪加强”等空指令
- [ ] 单时间段不过载
- [ ] 每镜唯一主信息任务
- [ ] Product Proof镜头干净可读

## H. Cross-Scene × Cross-Product
- [ ] 同一商品换Scene后故事明显改变
- [ ] 同一Scene换3C/服装/日用品后仍保持世界发动机
- [ ] 没有为了Scene强改商品
- [ ] 当前Scene若未Seedance实测，仍标`TESTING_CANDIDATE`

关键项失败，返回对应层内部重写，不向用户输出失败草稿/QA，除非用户要求。

---

# 21. Scene Validation状态管理

当前12个Scene只完成：

> **结构研发 + 横向差异QA + 跨3C/服装/日用品内部稳定性QA**

尚未完成：
- Seedance实际跨商品生成
- 连续空间稳定性
- 商品锁定稳定性
- 多人动作/交接穿模测试
- Scene-specific Reaction执行测试

因此当前统一状态：

`TESTING_CANDIDATE`

只有满足`references/scene-router.md`中的Validated升级条件，才可单独升级为`VALIDATED`。

不得因为理论结构成熟就提前宣称验证成功。

---

# 22. 最终判定

剧情带货商用版最低标准不再只是“有反转”。

必须同时成立：

`商品决策正确`
+
`Scene选择正确`
+
`Scene真正改变剧情因果`
+
`Proof真实有效`
+
`反转服务购买判断`
+
`情绪有奖励`
+
`产品推动剧情`
+
`动作可生成`
+
`产品/人物/空间连续`
+
`事实/物理/平台/IP合规稳定`

只有全部达到可接受状态才交付。
