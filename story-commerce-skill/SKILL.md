---
name: story-commerce-skill
description: 面向短视频剧情带货广告的全品类商用导演Skill。先锁商品事实、受众购买问题与Best Proof，再选择一个主Hook和Primary Story Architecture；随后把商业判断编译成产品中心的剧情、可见状态变化、合理场面调度、真实物理状态、人物表演、情绪驱动运镜、光影、声音与Seedance高权重精简提示词。默认30秒首推，15秒在单一Proof已足够时主动建议。核心不是“拍一个短剧再塞产品”，而是让剧情为产品服务、Proof推动剧情、产品在中后段接管注意力。
---

# 剧情带货 Skill 4.0｜Router Architecture

主文件只负责：**Truth Lock → Single Core Decision → Hook → Story/Proof → Scene/Performance → Prompt Compile → Independent Judge**。

原有商业决策、Story Architecture、Scene DNA、FACS、物理、运镜、节奏、光影与Prompt专业知识继续保留在 references 中；只有命中任务时才读取，不再把所有规则重复写进总控。

## 固定链路

`Truth Lock → Single Core Decision → Hook Router → Story / Proof Router → Scene / Performance / Visual → Prompt Compiler → Independent Judge`

下游不得越权改写上游事实与商业核心。

## 1. Truth Lock

先读取 `references/commerce-decision-routing.md`，锁定：
- Product / SKU / Reference Asset
- Audience / Job
- Why Buy / Why Hesitate
- Conversion Goal
- 已确认卖点、价格、CTA、平台/合规边界
- Best Proof / Proofability
- 用户本轮必须出现与禁止出现的内容

优先级：
`用户明确要求 > 产品事实/参考资产 > 合规/平台 > Core Decision > Best Proof > Product Centrality > Story > Scene/Performance/Camera > 风格炫技`

固定裁决：
`PRODUCT TRUTH > STORY TRICK`
`PROOF > REVERSAL`
`EVENT MEANING > ELEMENT PRESENCE`
`BLOCKING BEFORE CAMERA`
`CLARITY > PROMPT VOLUME`

不因历史案例多就自动带入账单、价格震惊、朋友核价、旧人物、旧CTA、某个Scene或R2。

## 2. Single Core Decision

每条广告先静默回答：
1. 观众这一条广告只需要改变哪一个主要购买判断？
2. 最强的一个Proof是什么？
3. 最后希望得到什么情绪释放、欲望或行动？

如果同时存在多个并列核心，先收敛，不进入剧情。其他卖点只能作为Proof Ladder或支撑信息，不能和主判断抢注意力。

继续读取 `references/product-centered-narrative-gate.md`：决定 `DIRECT PRODUCT ROUTE` 或 `NEED-LED STORY ROUTE`。如果删除产品后故事仍完整成立，判定剧情漂移，返回重写。

## 3. Hook Router

读取 `references/hook-router.md`。

先判断当前最强注意力资产，只选**一个主Hook**，最多一个辅助Hook。Hook可以来自利益/价格、事件中冲突、视觉异常、错误预判、结果前置或人物反应，但必须由本条广告事实和正片内容兑现。

Hook生成后先做Hook Judge；如果素材本身没有抓力，回到Commercial Core或Proof补内容，不靠同时堆多个Hook技巧硬救。

## 4. Story / Proof Router

### 4.1 Story Architecture
读取 `references/story-architecture-router.md`，只选一个Primary Architecture或安全EXIT。

允许的主结构继续由原模块管理；Tie Break保持：
`商业匹配 > Proof自然 > 产品因果 > 简单 > 生成稳定`

禁止塌成万能模板：
`两个人聊天 → 一个人不信 → 举产品 → 震惊 → CTA`

### 4.2 Proof First
Proof先于反转。核心Proof写成：
`初始状态 → 人物操作 → 接触/作用 → 可见过程 → 可见结果 → Reaction / Decision Change`

感官、长期效果、精确测试或高风险声明不能靠人物Reaction伪造客观证据。

30秒后半需要多层证据时，再形成 `Proof Ladder`；每一层必须增加新信息，不重复同一个“很好用”。

### 4.3 Reversal
形成Proof Plan后再读取 `references/reversal-router.md`。从R0开始判断，R1/R2只有在真的增加商业价值和剧情可读性时使用；不能为了“必须反转”牺牲Best Proof、产品事实或生成稳定。

## 5. Scene / Performance / Visual

### 5.1 Scene选择
用户未指定特殊Scene时，普通真实生活场景与Scene DNA共同竞争。只有特殊Scene确实增加因果、冲突、Proof或视觉记忆时，读取：
- `references/scene-router.md`
- `references/scene-dna-library.md`

不为了展示场景库而强行套Scene。

### 5.2 时长与节奏
默认首推约30秒。30秒及以上读取：
- `references/30s-narrative-engine.md`
- `references/paid-social-rhythm-dna.md`

如果单一卖点/单一Proof在12–18秒已经自然完成，主动建议15秒，不为30秒填剧情。

产品出现后，剧情逐步让位给产品：
`Hook earns attention → Product takes over attention → Proof escalates desire → CTA converts desire`

### 5.3 Scene Staging
只要涉及进出门、上下车、接近/离开、跨空间、品牌场所或同镜多个关键元素，读取 `references/scene-staging-compiler.md`。

先确定：
`EVENT MEANING → START/END → FROM/THROUGH/TO → BLOCKING → DEPTH → CAMERA → BRAND`

元素都出现但关系错误，仍判失败。

### 5.4 Physical State
关键人物/商品/道具状态变化读取 `references/physical-logic-dna.md`：
`BUILD STATE FIRST → CHANGE STATE WITH CAUSE → THEN WRITE SHOT`

真实摄影再读取 `references/physical-reality-lock.md`，它只做物理与摄影可信底座，不覆盖商业决策和Story。

### 5.5 Performance / FACS
所有关键情绪、Reaction、冲突、Reveal读取 `references/performance-facs.md`。FACS只负责把当前关键情绪编译成可见动作，不把眉眼鼻嘴清单塞满每一镜。

抽象词如“荒诞升级、震惊、紧张、压迫、崩溃”必须变成：
`刺激 → 感知 → 可见动作/接触 → 状态变化 → 反应 → 决定/行动`

升级必须出现新Evidence、新动作、新阻力或新状态，不能只是把“更震惊”重复三遍。

### 5.6 Camera / Light
关键产品操作和情绪Beat读取 `references/camera-action-compiler.md`。Camera先服从Blocking、真实操作面和轴线，再服从情绪强度。

光影/真实摄影沿用现有摄影底座与用户参考：主光必须有世界来源，产品证据和人物关键反应可读；设备名只在能带来可见结果时保留，不堆质量词。

## 6. Prompt Compiler

输出Seedance Prompt前读取 `references/prompt-attention-compiler.md`。

内部可以复杂，最终Prompt必须压缩。优先保留：
1. 商品/人物/参考事实
2. 核心事件与Best Proof
3. 关键动作、接触和状态变化
4. 关键Reaction / 表演
5. 场面与运镜
6. 光影/声音节点
7. 少量高风险反向限制

完整Prompt默认结构继续保持：
1. 【开场总控】只写风格、调性、观感、平台感，不写具体事件。
2. 【主体、空间与参考锁定】
3. 【表演与状态】
4. 【光影与成像基线】
5. 【分镜描述】按观看顺序写可执行动作和结果。
6. 【声音】对白/环境声/SFX/BGM只写真正有作用的节点。
7. 【反向限制】只处理当前严重误读，不做长禁词墙。

模型收到画面，不收到“荒诞升级、高级一点、情绪加强、一次成功”等管理语言；这些必须先在导演层转成可见结果。

## 7. Independent Judge

交付前读取 `references/independent-judge.md`。

Judge只检查：Truth、Single Core Decision、Hook、Product Centrality、Proof、State Change、Scene/Performance、Camera/Light、Prompt Attention。

FAIL时指出最早或影响最大的失败点，返回对应模块修正；不因局部问题整条推倒重来。Truth与Commercial Core一旦锁定，下游不能为了剧情更好看擅自改写。

真实成片出问题时优先定位最小问题片段：定位异常 → 判断问题层 → 局部修复 → 检查前后承接 → 再替换。Prompt文字PASS不等于成片PASS。

## 专项路由

| 条件 | 读取模块 |
|---|---|
| 商品决策/受众/Why Buy/Why Hesitate/Best Proof | `references/commerce-decision-routing.md` |
| 产品是否真正驱动剧情 | `references/product-centered-narrative-gate.md` |
| Story结构 | `references/story-architecture-router.md` |
| Reversal R0/R1/R2 | `references/reversal-router.md` |
| 陌生品类/跨品类先验 | `references/category-priors.md` |
| 感知价值反差 | `references/perceived-value-contrast-routing.md`，不能抢Core Decision/Best Proof |
| 特殊Scene | `references/scene-router.md`、`references/scene-dna-library.md` |
| 30秒剧情与买量节奏 | `references/30s-narrative-engine.md`、`references/paid-social-rhythm-dna.md` |
| 复杂场面调度 | `references/scene-staging-compiler.md` |
| 商品/人物/道具状态 | `references/physical-logic-dna.md` |
| 真实摄影底座 | `references/physical-reality-lock.md` |
| 表演/FACS | `references/performance-facs.md` |
| Camera × Action | `references/camera-action-compiler.md` |
| Prompt注意力压缩 | `references/prompt-attention-compiler.md` |
| Hook选型/检查 | `references/hook-router.md` |
| 最终独立QC | `references/independent-judge.md` |

## 经验维护

不要因为一次生成就继续往母版塞规则。

- 单次失败先记录为案例/观察。
- 反复出现且因果清楚，或用户明确批准后，才晋升为长期规则。
- 新规则优先写入对应专业reference，不继续把主 `SKILL.md` 变回百科全书。
- 保留现有 validation / regression 体系做回归检查；没有真实生成证据时，不把文字推演说成模型能力结论。
