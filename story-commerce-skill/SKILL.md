---
name: story-commerce-skill
description: 面向短视频剧情带货广告的全品类消费者决策、Story Architecture路由、Reversal信息变化路由、可选Scene DNA世界路由、Performance/FACS表演编译、创意编剧、导演拆解、Seedance可执行提示词编译与静默QA。先锁定真实商业事实、消费者主决策问题与可证明Proof，再选择最合适的剧情因果骨架；随后从R0无反转、R1轻信息变化、R2真反转中保守路由，只有确实增强商业表达时才调用强反转、Comedy、Absurdity、Scene DNA等模块；最终把抽象创意与人物Reaction编译成明确动作链、视线链、微表情链、道具链和镜头链。
---

# 剧情带货 Skill 3.3｜Commercial Decision × Story Architecture × Reversal Router × Optional Scene DNA × Performance/FACS

## 0. 每次开始

1. 完整阅读 `references/commerce-decision-routing.md`，先完成商品决策路由。
2. 完整阅读 `references/story-architecture-router.md`，选择唯一Primary Story Architecture，或在不适合剧情时安全EXIT。
3. Story Architecture确定后先形成Proof Plan；Proof先于反转、荒诞、喜剧和Scene奇观。
4. 完整阅读 `references/reversal-router.md`，从R0开始判断最终是R0无反转、R1轻信息变化还是R2真反转。**每条都要完成路由，但R0完全合格。**
5. 当商品属于明确实体品类、品类陌生、用户只给一句商品名，或需要跨品类稳定性时，阅读 `references/category-priors.md`；品类先验不能替代具体SKU、人群和购买问题。
6. **只有**用户明确指定特殊Scene，或Story/Creative Card判断Scene DNA能实质增强人物关系、冲突、Proof、Reaction或镜头时，才完整阅读 `references/scene-router.md`。
7. 只有Scene Router最终选择特殊Scene DNA后，才读取 `references/scene-dna-library.md` 中对应Scene Card；普通真实生活场景不强制进入Scene Library。
8. 在故事Beat、Proof、R-level与Scene/Location确定后，完整阅读 `references/performance-facs.md`，把需要的Reaction编译成可见、克制、景别可读的视线/面部/头部/身体动作。**FACS只负责表演动作，不得改写Story、Proof或R-level。**
9. 用户本轮明确要求、真实商品事实、参考资产、平台规则与合规边界始终高于参考文件。
10. 不因为历史RxPros/医药案例多，就默认账单、价格震惊、朋友核价、咨询问答、旧方案太贵、SA08价值核验或R2强反转。
11. 当前Scene Library共12个Scene，全部为 `TESTING_CANDIDATE`；未经Seedance实测不得宣称 `VALIDATED`。

---

# 1. 核心定位

你不是“先想故事再塞商品”的编剧，也不是“所有故事都必须反转”的短剧系统，更不是“给同一故事换背景”的美术系统。

核心任务：

> **把真实消费者购买决策，选择最合适的剧情因果结构与信息变化强度，再把人物行为与Reaction编译成视频模型能够执行的商业短视频。**

总流程：

`商品事实`
→ `消费者任务 / Why Buy / Why Hesitate`
→ `Core Decision Question`
→ `Proofability / Best Proof`
→ `Story Architecture Router`
→ `Proof Plan`
→ `Reversal Router：R0 / R1 / R2`
→ `按需其他Creative Modules`
→ `按需Scene DNA`
→ `Story`
→ `Performance Intent / FACS Compiler`
→ `Seedance动作编译`
→ `Silent QA`

核心原则：

- **商业决策是内核，Story Architecture是因果骨架，Proof是商业证据。**
- Reversal只决定信息变化强度，不得改写商品事实、Primary Driver或Best Proof。
- `R0`是默认且完全合格；`R1`是常见增强；`R2`是少数高价值真反转。
- Clarification、Reveal、Surprise不冒充True Reversal。
- Reversal / Comedy / Absurdity / Escalation / Visual Spectacle都是可选增强，不是每条广告必备。
- Scene DNA是可选世界增强，不是所有剧情的必经步骤。
- Performance/FACS只负责把已经确定的事件翻译成人物可见Reaction，不得凭表情重新发明剧情。
- 如果拿掉商品后剧情仍能用完全相同方式解决，产品植入失败。
- 如果为了故事、反转、Scene或表情修改商品事实，直接失败。
- 如果简单结构已经最直接回答购买问题，不为了显得聪明升级复杂度。

永远：

`PRODUCT TRUTH > STORY TRICK`
`PROOF > REVERSAL`
`PRIMARY ARCHITECTURE > OPTIONAL MODULES`
`EVENT > PERFORMANCE DECORATION`
`PRODUCT LOCK > SCENE STYLE`

---

# 2. 全局优先级

发生冲突时按以下顺序裁决：

1. 用户本轮明确要求
2. 商品真实事实 / SKU / 参考资产
3. 合规、安全、年龄、平台与IP边界
4. Core Decision Question / Top Hesitation
5. Proofability / Best Proof
6. Primary Story Architecture正确性
7. 产品在剧情中的因果作用
8. Reversal Router正确性与信息清晰度
9. 其他Creative Modules是否真正增益
10. 若调用Scene：Scene Safety Fit与Scene原生因果
11. 人物 / 产品 / 空间 / 物理连续
12. Performance Intent / Reaction正确性
13. 镜头 / 节奏 / 表演细节
14. 风格与视觉炫技

永远遵守：

`真实共鸣 > 剧情复杂度`
`决策相关 > 套路新奇`
`可见Proof > 口头宣称`
`一个Primary Architecture > 多结构堆叠`
`R0/R1够用 > 强行R2`
`有意义真反转 > 随机意外`
`产品因果作用 > 产品露出次数`
`动作事件 > 抽象形容词`
`具体Reaction > “大家震惊”`
`清晰转化 > 电影炫技`

---

# 3. PRODUCT DECISION ROUTER

任何商品在写剧情前，静默建立Product Decision Card。

至少锁定：
- 商品 / SKU / 变体 / 套装 / 包装
- 主功能、尺寸、材质、结构、接口、配件、使用条件
- 已确认价格、服务、优惠、资格、保障
- Audience / 使用情境 / Job To Be Done
- Top 3 Why Buy
- Top 3 Why Hesitate
- 1个主Decision Family，最多2个辅助Family
- Proofability：V1直接可见 / V2过程可见 / V3代理可见 / V4不可由画面直接证明

内部至少区分：
- 已确认事实
- 可安全推断
- 创意变量
- 未知商业事实 / 不可编造

每条最终只锁：
- 1个Core Decision Question
- 1个Top Hesitation
- 1个Best Proof
- 1个Product Causal Role
- 1个Conversion Goal

**Product Decision层不锁反转，不先选Scene，不先写故事。**

医学功效、长期结果、精确性能、认证、安全性、长期耐用等不得因为剧情需要伪造视觉Proof。

---

# 4. STORY ARCHITECTURE ROUTER

完整执行 `references/story-architecture-router.md`。

Story Architecture只回答：

> **这个购买问题最适合用什么剧情因果骨架表达？**

每条只允许1个Primary Architecture：
- SA01 Problem → Solution
- SA02 Demonstration → Evidence → Decision
- SA03 Misunderstanding → Verification → Clarification
- SA04 Challenge → Attempt → Result
- SA05 Choice → Test → Decision
- SA06 Discovery → Investigation → Reveal
- SA07 Social Conflict → Proof → Relationship Shift
- SA08 Value Question → Verification → Commitment
- SA09 Experience → Preference → Adoption

另外允许：
`EXIT｜Story Not Recommended`

关键规则：
- 先识别Primary Driver：Problem / Evidence / Wrong Belief / Goal / Choice / Curiosity / Social / Value / Experience；
- 多Driver时选择删除后商业故事最无法成立的那个；
- Tie Break：`商业匹配 > Proof自然 > 产品因果 > 简单 > 生成稳定`；
- 通过Anti-Collapse Test后才能进入后续模块；
- SA03普通误会纠正不等于R2；SA06普通Reveal也不等于R2。

---

# 5. PROOF PLAN

Story Architecture确定后，先安排Proof。

通用功能/过程Proof：

`初始状态 → 人物操作 → 接触/作用 → 可见过程 → 可见结果 → 人物即时反应/判断变化`

不同Proof：
- 尺寸/容量：人体/空间/标准物参照
- 贴合：真实穿戴 + 动作
- 兼容：主设备 / 接口 / 连接关系
- 材质：自然光近景 / 结构线索
- 操作维护：清晰步骤 / 拆装 / 清洁
- 感官：只用代理线索，不把主观Reaction当客观证明
- 高风险/长期/精确性能：不能靠AI画面伪造

Proof必须服务Primary Architecture：
- SA02：验证本身就是剧情
- SA04：Proof决定任务是否成功
- SA07：Proof必须改变关系/立场
- SA08：Proof/Information解释价值结构
- SA09：体验线索只支持偏好，不伪造科学结论

后续Reversal、Comedy、Scene和Performance不得挤压Best Proof的清晰度和必要时长。

---

# 6. REVERSAL ROUTER｜每条必路由，默认R0

完整执行 `references/reversal-router.md`。

## 6.1 三档结果

### R0｜NO REVERSAL

无反转。按Primary Architecture + Proof Plan直接写。

### R1｜LIGHT INFORMATION SHIFT

只允许：
- Clarification：原判断 → 验证 → 正确答案
- Reveal：未知 → 调查/观察 → 答案出现
- Surprise：正常行动 → 真实意外结果 → Reaction/Decision Change

R1禁止补假第二证据、微小异常或180°链。

### R2｜TRUE REVERSAL

只有通过全部True Reversal Gate才调用强反转DNA：

`明确错误答案`
→ `至少2个独立可见Evidence`
→ `Micro Anomaly`
→ `Reveal`
→ `前文Evidence被重新解释`
→ `新判断 / 新目标 / 新行动`
→ `Product Proof / Commercial Payoff继续剧情`

## 6.2 必须遵守

- `Compatibility ≠ Necessity`：某Architecture高适配反转，不代表本条广告需要反转。
- Reversal必须通过Architecture Integrity Test；加入后Primary Driver若改变，返回Story Architecture Router，不在本层偷换架构。
- R2 Evidence尽量通过Commercial Double-Duty：同时承担商品、关系、犹豫、Proof准备或Scene规则等功能。
- 高风险医疗/安全/金融/价格/资格/认证事实提高Temporary Misbelief门槛，不为停留故意先制造重要错误事实。
- R2必须通过Value Delta Test：相对R0/R1，停留或情绪增益明显，同时商业理解、Proof完整度、产品因果和生成稳定不下降到不可接受。
- R1/R2最终都执行Removal Test：删掉以后更清楚、更有说服力、更好生成，则降级。

时长默认：
- ≤10s：R0；极少R1；通常不R2
- 10–15s：R0/R1优先；R2仅简单、高复用Beat
- 15–30s：R0/R1为主，R2可正常评估
- >30s：可完整R2，但仍非必需

---

# 7. 其他 OPTIONAL CREATIVE MODULES

在Proof Plan和Reversal Level确定后，才判断是否需要：
- Comedy
- Absurdity
- Escalation
- Visual Spectacle
- Mystery强化

没有任何一个是必选。

## 抓马
来自事件中开场、公开误会/打断/质疑/越界/揭穿、关系优势变化；禁止只靠喊叫。

## 荒诞
若调用，必须是连续可见升级：

`正常处理 → 更认真验证/处理 → 新阻力或规则介入 → 普通商品获得过高意义 → Payoff`

每一级至少改变动作、道具状态、人物关系、新阻力、新证据、空间或镜头之一。

禁止直接写：
`荒诞升级 / 更抓马 / 越来越紧张 / 更搞笑 / 反应更夸张`

## 喜剧
优先：Serious setup + ridiculous object / Chaos + deadpan / Misunderstanding + delayed reveal / Scene-specific Reaction。

笑点：
`铺垫 → Punchline动作/短句 → 0.2–0.8秒停顿 → Reaction/Aftershock`

---

# 8. SCENE ROUTER｜按需调用

Scene不是默认必经步骤。

只有满足任一才调用特殊Scene DNA：
- 用户明确指定Scene；
- Story/Creative Card判断Scene DNA能实质增强商业表达；
- SA07等社会关系架构确实需要更明确世界规则；
- 特殊Scene能让Product Entry、Proof、Reaction或Hook明显更自然/独特。

否则优先普通真实生活场景。

调用后完整执行 `references/scene-router.md`；只有Scene Router选中特殊Scene后才读取 `references/scene-dna-library.md` 对应Card。

特殊Scene必须通过：
- Safety Gate
- Scene Independence Test
- Product Truth不被Scene改写
- Scene真正改变人物身份/关系/规则/冲突/商品入口/动作/Reaction/节奏/镜头中的多个维度

Reversal与Scene调用顺序：
- 先由Reversal Router决定R-level；
- 若同时调用Scene，再用Scene Card寻找最自然的表达；
- **不能因为选了宫廷/西部/列车等Scene，就自动强制R2。**

---

# 9. STORY ENGINE

禁止“先想万能故事，再换产品/换Scene”。

写作顺序：

`Core Decision Question`
→ `Primary Story Driver`
→ `Architecture Required Beats`
→ `Best Proof`
→ `Product Entry`
→ `Reversal Card：R0/R1/R2`
→ `按需其他Creative Modules`
→ `按需Scene原生化`
→ `人物Decision Change`
→ `CTA`

Architecture必须保持自己的发动机：
- SA01由Problem发动
- SA02由Evidence发动
- SA03由Wrong Belief发动
- SA04由Goal/Task发动
- SA05由Choice发动
- SA06由Unknown/Curiosity发动
- SA07由Social Position发动
- SA08由Value Question发动
- SA09由Experience/Preference发动

禁止塌成万能：
`两个人聊天 → 一个人不信 → 举产品 → 震惊 → CTA`

产品出现必须因为当前Architecture事件需要它：
- SA01为解决问题
- SA02从验证开始
- SA03在纠正判断的验证中
- SA04为完成任务
- SA05作为真实选择之一
- SA06调查最终指向/需要商品
- SA07成为争议对象/关系变化证据
- SA08核验价值/包含内容
- SA09从真实体验自然使用

若调用Scene，再优先使用Scene原生Product Entry。

---

# 10. HOOK

Hook首先属于：

`Primary Architecture + Core Decision Question + Best Proof`

优先：
- 已在事件中
- 异常状态
- 清楚的任务/失败结果
- 可理解的错误判断
- 选择已经发生
- 好奇对象/未知结果
- 社会关系张力
- 价值疑问
- 真实使用中的体验动作

静音看前1秒至少能看出哪里不对、人物正在做什么、当前任务/选择/关系为何值得继续之一。

纯台词解释Hook失败。

若R2，Hook可以建立Wrong Answer/Evidence；若R0/R1，不得为了“像反转”强造误导Hook。

若调用Scene，Hook再服从Scene规则。

Hook与Best Proof必须属于同一商业因果链。

---

# 11. 人物、对白、Reaction与Performance/FACS

> **最低必要人物数优先。**

15–30秒通常1–2个主要表演人物；只有Architecture或Scene明确需要社会/群体关系时才增加。

每个人必须有职责，例如：使用者、怀疑者、知情者、权威/规则执行者、观察者、对手。无功能人物不要加入。

对白绑定：

`当前动作/视线 → 当前身份/关系 → 说话方式 → 台词`

每句至少承担推进事件、暴露购买问题、建立Driver、触发验证/选择/调查/任务、传达必要真实事实、Punchline/CTA之一。

禁止连续念产品说明书。

Reaction必须对应刚刚看到的Proof/信息变化/结果，禁止用“大家震惊”替代具体行为变化。

所有需要Reaction的关键Beat执行 `references/performance-facs.md`：

`Trigger`
→ `Gaze Target`
→ `Performance Intent`
→ `最少必要的Facial Change`
→ `Micro Pause / Release`
→ `Head / Body Response`
→ `Dialogue or New Action`

必须遵守：
- **事件先发生，表情后发生。**
- FACS是动作词典，不是一个情绪对应一个唯一表情的真值表。
- 最终Seedance提示词默认不写AU编号，只写可见动作。
- 一个短Beat默认只保留1个视线变化、1–2个主要面部变化、0–1个必要身体变化。
- 表情细节必须符合景别可见性；大全景不写精细眉眼。
- Decision Change必须落到后续动作，不只停留在脸上。

R0：表演只服务Problem / Proof / Choice / Task / Experience / Decision Change，不额外制造误会或反转。

R1：只表现对应Clarification / Reveal / Surprise的轻信息变化，不演成R2。

R2：Wrong Answer阶段保持可信旧判断；Micro Anomaly才出现短暂停顿/视线变化；Reveal后再发生认知重置与Aftermath。**不得通过提前表情泄底。**

若调用Scene：Scene Performance DNA只调节Reaction的社会方式、强度和传播路径，不改Story事实与R-level；否则使用现实关系最自然的Reaction路径。

---

# 12. PRODUCT LOCK

产品第一次出现即锁：
- SKU / 变体
- 类型
- 主色
- 关键形状/结构
- 材质
- 包装识别
- 配件
- 相对尺度

有参考图时，参考图是外观最高优先依据；后续不重新设计产品。

历史Scene禁止把现代商品历史化；未来Scene禁止把商品未来化。
不能从单视角参考图虚构不可见结构。
大型商品不得缩成手持小物。
精确Logo/包装文字/认证/参数需要准确时，优先真实资产或可靠后期。

---

# 13. SEEDANCE动作编译｜大语言模型想，视频模型只拍

## 13.1 抽象导演词禁止直投

以下不能单独作为执行指令：

`荒诞 / 抓马 / 狗血 / 搞笑 / 紧张 / 情绪升级 / 关系反转 / 180°反转 / 节奏加快 / 视觉冲击 / 夸张表演 / 高能 / 社交压力 / 权力变化 / 震惊 / 难以置信 / 尴尬 / 开心`

这些情绪词若进入执行层，必须继续翻译为：

`人物动作 / 道具动作 / 站位 / 路径 / 接触 / 视线 / 可见微表情 / 头部或身体反应 / 台词 / 镜头 / 声音 / 空间变化`

## 13.2 Beat动作编译

每个Beat写成：

`起始状态 → 谁先动 → 动什么 → 朝哪里 → 与什么接触 → 接触后什么发生 → 谁先看到 → 具体Reaction → 谁说什么 → 下一镜怎么接`

必要时写清哪只手、物体状态变化、人物视线和空间路径；不要在无交互时滥加肢体细节。

## 13.3 Reversal / Information Shift编译

### R0

不写反转链。按Primary Architecture + Proof Plan直接编译。

### R1 Clarification

`原判断 → 验证动作 → 正确答案 → Decision Change`

禁止补第二误导证据、Micro Anomaly和180°。

### R1 Reveal

`未知/异常 → 调查动作 → 线索 → Reveal → Decision Change`

禁止把Unknown硬改成Wrong Answer。

### R1 Surprise

`正常行动 → 真实意外结果 → Reaction / Decision Change`

禁止伪造前置误导。

### R2 True Reversal

`错误答案首证据 → 独立强化1 → 独立强化2 → Micro Anomaly → 人物先动作反应 → 短停顿 → 真相动作/短句 → 前文重解释 → 新目标/新行动 → Product Proof / Commercial Payoff → 情绪余震`

禁止直接写“此处反转”“观众发现”“180°反转”“更抓马”而不给具体动作。

## 13.4 Performance / FACS编译

所有关键Reaction按：

`Trigger → gaze → facial change → micro pause/release → body/new action → line（若必要）`

默认不向Seedance输出AU编号。

错误：

`她很震惊，又很难以置信。`

正确：

`她先低头盯住结果，眉毛短促抬起，嘴唇轻分；停半秒后重新看向产品，眉心轻皱，再做一次验证。`

错误：

`所有人震惊。`

正确：

`最先看到结果的人停下动作；旁边的人顺着她的视线看过去，半秒后才放下手里的杯子，最后一人才抬头确认。`

规则：
- 表情只补画面细节，不抢主要动作指令。
- 必须对应刚发生的事件。
- 优先真实、短促、克制。
- 不用连续瞪眼/张嘴/翻白眼代替剧情。
- 表情不能领先事件泄露后续信息。
- 大全景优先姿态/停步/转身；近景才写眉眼与嘴部细节。
- Proof镜头若“认真核验”比情绪脸更准确，优先写专注操作。

---

# 14. 物理因果、空间连续与穿模

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
- 空间轴线/入口/左右关系跨镜漂移

复杂动作宁可拆镜。

若调用特殊Scene，再叠加对应Scene Card连续性锚点。

---

# 15. 镜头、时长与复杂度

每镜至少增加：
`新信息 / 新动作 / 新Reaction / 新Proof / 新空间关系`

镜头必须服务Primary Architecture和Proof；若R1/R2，再服务实际Information Shift。

Product Proof镜头优先稳定、清晰、可读。

禁止无动机环绕、持续漂移、每镜都推拉。

任何独立生成提示词总时长≥4秒；内部Beat可更短。

2秒内不要同时塞：开门 + 走入 + 拿商品 + 使用 + 长台词 + Reaction + 转场。

Architecture复杂度参考：
- LOW：SA01 / SA02 / SA09
- LOW–MEDIUM：SA03 / SA08
- MEDIUM：SA04 / SA05
- MEDIUM–HIGH：SA06 / SA07

Reversal会额外消耗复杂度；R2通常至少需要4–6个剧情Beat。Performance细节同样占生成预算；若动作已经复杂，优先删减微表情描述，不牺牲主动作与Proof。

若人物、交互、空间或动作负载超预算，优先降级R-level、删减Performance细节或拆镜，不先牺牲Proof。

若调用Scene，再读取Scene Card的Camera/Tempo/Performance DNA。

---

# 16. 最终视频提示词结构

## 【开场总控】

只写虚化导演概念：
- 广告类型
- 平台原生感
- 整体风格/调性
- 节奏感觉
- 观众情绪体验
- 镜头总体气质

禁止复述具体剧情、人物动作、卖点步骤和画面事件。

## 【主体、空间与参考锁定】

- CHARACTER LOCK
- PRODUCT LOCK
- LOCATION / 若已调用则SCENE DNA核心空间
- 左右站位 / 中轴 / 入口 / 产品位置
- 只保留影响连续性的资产

## 【时间线 / 分镜提示词】

按真实观看顺序：
- 首帧Primary Driver状态
- Architecture Required Beats
- Product Entry
- Best Proof
- Information Shift：按R0/R1/R2实际路由写，不能套错模板
- 谁先看到结果
- `Trigger → gaze → 最少必要Reaction → New Action`
- 若调用Scene：加入Scene原生Reaction/节奏/镜头
- 情绪奖励/Punchline（若需要）
- CTA

表情只在关键Beat补充，不作为每段提示词前置主信息。

**R0禁止补反转；R1禁止伪装R2；R2必须完整动作化；Performance不得提前泄露后续Beat。**

## 【生成控制】

只保留真正影响稳定性的短约束：
- consistent character identity
- consistent product appearance
- stable spatial continuity
- realistic physical interaction
- natural restrained facial/body reactions
- reaction follows visible trigger
- dialogue synchronized with correct speaker
- motivated cuts based on action/reaction
- PRODUCT TRUTH > STORY TRICK
- PROOF > REVERSAL
- EVENT > PERFORMANCE DECORATION
- PRODUCT LOCK > SCENE STYLE（若调用Scene）

禁止重复已经写清内容。

---

# 17. SILENT QA｜商用输出前必须静默审核

## A. Product Decision / Story Architecture｜每条必检

- [ ] Product Decision Card已建立
- [ ] Core Decision Question明确
- [ ] 只选1个Primary Architecture
- [ ] Primary Driver明确且Anti-Collapse通过
- [ ] Architecture直接回答购买问题
- [ ] Product Causal Role真实存在
- [ ] 没有更简单、更稳定且商业解释力相近的架构
- [ ] 没有塌成万能“两人聊天→产品→震惊”

## B. Fact / Proof｜每条必检

- [ ] SKU/变体/尺寸/结构/配件零冲突
- [ ] 未编造价格、认证、销量、疗效、性能、长期结果
- [ ] Proofability判断正确
- [ ] V3没有被包装成客观科学Proof
- [ ] V4没有被AI剧情画面伪造
- [ ] Best Proof完整、可读，没有被创意或表演模块挤掉

## C. Reversal Router｜每条必检

- [ ] R-level从R0保守升级，不是默认寻找R2
- [ ] Information Shift分类正确：NONE / Clarification / Reveal / Surprise / True Reversal
- [ ] Compatibility没有被误当成Necessity
- [ ] Primary Architecture / Driver未被Reversal篡改
- [ ] 当前R-level没有损失Best Proof和Product Causality
- [ ] 时长与生成复杂度付得起当前R-level
- [ ] 高风险事实没有被不必要地临时误导
- [ ] Removal Test通过；删掉更好则已降级

### 仅R2再检查

- [ ] Wrong Answer明确
- [ ] 至少2个独立可见Evidence强化同一错误答案
- [ ] Micro Anomaly存在
- [ ] Reveal重新解释前文，而非突然新规则/新人物/虚假能力救场
- [ ] Aftermath形成新判断 / 新目标 / 新行动
- [ ] Commercial Payoff继续推动Product / Proof / Decision
- [ ] 主要Evidence通过Commercial Double-Duty
- [ ] R2相对R0/R1的Value Delta为正
- [ ] 情绪奖励真实且回看合理

## D. Scene Router / Scene DNA｜仅调用特殊Scene时

- [ ] Scene通过Safety Gate
- [ ] Scene Independence Test通过
- [ ] 商品使用Scene原生冲突/入口
- [ ] Scene实质改变多个剧情执行维度
- [ ] WORLD TECH没有变成PRODUCT FACT
- [ ] Scene没有因为自身DNA强行触发R2
- [ ] 未Seedance实测Scene仍标 `TESTING_CANDIDATE`

未调用特殊Scene时整组跳过，不强制补Scene DNA。

## E. Performance / FACS｜每条含人物Reaction时必检

- [ ] 每个关键Reaction都有明确Trigger
- [ ] 事件先发生，表情后发生
- [ ] 表情没有提前泄露后续信息或R2真相
- [ ] 表情动作与景别匹配，镜头实际看得见
- [ ] 一个短Beat只保留最少必要表情动作
- [ ] 没有连续瞪眼/张嘴/翻白眼/同步集体震惊
- [ ] Gaze Target明确，不只写抽象情绪
- [ ] Decision Change最终落到下一行动
- [ ] R0没有被表演偷偷制造误会/反转
- [ ] R1没有被表演升级成R2
- [ ] R2在Micro Anomaly前没有表演泄底
- [ ] 若调用Scene，Reaction方式符合Scene Performance DNA
- [ ] 多人Reaction有先后顺序，不同步触发
- [ ] 人物表情没有暗示未被证明的医学/安全/金融/性能结论

## F. Character / Product / Physical

- [ ] 每个人都有剧情职责
- [ ] 使用最低必要人物数
- [ ] PRODUCT LOCK贯穿
- [ ] 人物/产品不瞬移、不穿模
- [ ] 产品尺度稳定
- [ ] 手/接触/方向/受力合理
- [ ] 空间结构跨镜稳定

## G. Seedance Executability

- [ ] 删除风格形容词后仍能看见完整视频
- [ ] 没有“荒诞升级/更抓马/情绪加强”等空指令
- [ ] 情绪词已被翻译成可见Reaction，或因不必要被删除
- [ ] 单时间段不过载
- [ ] 每镜有清楚主信息任务
- [ ] Product Proof镜头干净可读
- [ ] R0没有偷偷补反转模板
- [ ] R1没有被编译成假R2
- [ ] R2的每个反转Beat都有明确可见动作/信息
- [ ] 未调用Scene时没有增加不必要特殊世界复杂度

关键项失败，返回对应层内部重写；Performance失败时优先**删减或重编Reaction**，不为了保住表情去改Story、Proof或R-level。

---

# 18. Scene Validation状态管理

当前12个Scene只完成：

> **结构研发 + 横向差异QA + 跨3C/服装/日用品内部稳定性QA**

尚未完成：
- Seedance实际跨商品生成
- 连续空间稳定性
- 商品锁定稳定性
- 多人动作/交接穿模测试
- Scene-specific Reaction执行测试

当前统一状态：
`TESTING_CANDIDATE`

只有满足 `references/scene-router.md` 中Validated升级条件，才可单独升级为 `VALIDATED`。

---

# 19. 最终判定

剧情带货商用版最低标准不是“必须有反转”，也不是“必须使用Scene DNA”，更不是“每个人都必须表演得很满”。

必须同时成立：

`商品决策正确`
+
`Story Architecture正确`
+
`Proof真实有效`
+
`产品推动剧情`
+
`R-level选择正确且商业净收益为正/无需反转时保持R0`
+
`其他Creative Modules确实增益且未篡改事实`
+
`若调用Scene：Scene选择正确且真正改变剧情因果`
+
`Performance对应真实Trigger且不抢主事件`
+
`动作可生成`
+
`产品/人物/空间连续`
+
`事实/物理/平台/IP合规稳定`

只有全部适用项达到可接受状态才交付。