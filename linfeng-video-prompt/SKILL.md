---
name: linfeng-video-prompt
description: 把产品Brief、脚本、分镜、故事板、参考视频或成片问题转为精炼、一读成像、可直接生成的视频提示词、导演分析或分镜，并校验资产职责、创意幅度、节奏/风格一致、空间物理、声音、时长与模型容量。用于TVC、商业广告、UGC、短剧、产品演示、视觉奇观/超现实、复杂运镜、连续性返修、画质诊断及Seedance等视频模型工作流；用户说“林枫视频提示词skill”或要求写、改、检查视频提示词时使用。
---

# 林枫视频提示词｜High-Signal Router

把导演判断编译为**高信号、低污染、一读成像**的视频提示词。

默认原则：**主体和事件先说清，动作与承接写够，镜头只写必要响应；光影、材质、景深、设备与物理真实性只在能直接改善当前镜头时加入。**

## 固定链路

`Contract Lock → Route → Event Compile → Signal Budget → Minimal Prompt Compile → Independent Judge`

下游不得为了风格或创意改写上游事实。

## 1. Contract Lock

先锁真正会改变结果的信息：
- 交付类型：分析、脚本/分镜、可复制Prompt、实际生成或局部返修；
- 模型/平台、时长、画幅、参考资产；
- 人物/产品/空间已确认事实；
- 必须出现、禁止出现、准确文字/声音/CTA；
- 用户指定的格式、风格、媒介。

用户已给的信息不重复询问；只缺少会改变事实或核心结果的信息时才问一个关键问题。

默认执行优先级：
`用户明确要求 > 核心主体/产品 > 核心事件 > 动作/状态变化 > 空间连续 > 镜头响应 > 必要真实性补丁 > 光影/成像 > 技术术语`

如果用户本轮任务本身就是灯光、材质、摄影或画质返修，对应层级可临时上调；不要把默认排序当死规则。

普通项目只使用当前事实，不自动带入历史品牌、价格、人设、CTA、平台禁区或旧案例。

## 2. Route

先判断本片的**一个主任务**：
- 剧情/关系
- 产品/商业证据
- 人物表演
- 环境/视觉奇观
- 动作/运镜
- 返修/QC

再叠加真正会改变输出的次模块，不因为“可能有用”全部读取。

### 路由表

| 任务信号 | 读取模块 |
|---|---|
| 新写/重写Prompt、压缩、前后矛盾 | `references/prompt-compilation-and-consistency.md`、`references/output-contract-and-validation.md` |
| 光影/质感明确为主任务或返修目标 | `references/camera-light-quality-baseline.md` |
| 抽象词、动作不落地、状态升级 | `references/state-change-compiler.md` |
| 商业任务、产品事实/比例、购买犹豫 | `references/commercial-contract.md`、`references/product-preflight-and-category-routing.md`、`references/decision-driven-ad-creative.md` |
| 首屏停留、强Hook | `references/golden-3s-hook-engine.md` |
| 多镜、连续节拍、参考反推 | `references/director-information-control.md` |
| 剧情对话、关系戏、人物目的/认知变化 | `references/drama-performance-control.md` |
| 已有剧情需细写微表情/FACS | `references/facial-expression-action-library.md` |
| 多人换位、正反打、交接、复杂空间 | `references/spatial-optics-physics-control.md`；跨镜再叠加 `references/continuity.md` |
| 复杂运镜、动作戏、一镜到底 | `references/director-camera-attention.md` |
| 构图主次、关系揭示 | `references/camera-composition-decision-layer.md`、`references/composition-story-engine.md` |
| 摄影媒介/设备身份 | `references/camera-identity-selection-engine.md` |
| 具体摄影光学方案 | `references/cinematography-toolkit.md` |
| IMAX/UE5/Octane/VFX等质感栈 | `references/visual-quality-stack.md`；只选有职责的一项或少量组合 |
| 实拍可信度、塑料感、失重、环境空洞 | `references/physical-reality-lock.md` |
| 模糊、过锐、脏灰、压缩/输出问题 | `references/visual-quality-diagnostics.md` |
| 写实+异常、产品世界化 | `references/grounded-surreal-product-spectacle.md` |
| A→B连续变形 | `references/visual-transformation-spectacle.md` |
| 物体/屏幕接管画面转场 | `references/physical-takeover-transitions.md` |
| 随拍、纪录、家庭录像、延迟追拍 | `references/observational-camera-authenticity.md` |
| UGC/生活分享/原生产品体验 | `references/ugc-ad-rules.md` |
| 食品/味觉/蒸汽 | `references/food-flavor-direction.md` |
| 选角、妆发、美感 | `references/casting-and-beauty-direction.md` |
| 品牌宣言/主题蒙太奇 | `references/brand-manifesto-montage.md` |
| TVC完整创作/生产/长片 | `references/tvc-full-workflow.md`、`references/tvc-production-operations.md`、`references/tvc-runtime-control.md` |
| 配音、精确台词、发音返修 | `references/voiceover-control.md` |
| Seedance工作流/能力边界 | `references/seedance-2.5-workflows.md` |
| 常见故障/跨工具交接 | `references/design-rules.md` |

## 3. Event Compile

视频的详细度优先给**时间、主体、事件、动作和状态变化**，不是摄影术语。

关键Beat默认压成：
`起始状态 → 触发 → 可见动作/变化 → 结果 → 必要镜头响应`

简单时不用把每一项都写满。例如：
`她看到价格后动作突然停住，低头重新核对，再抬头看朋友；镜头快速推近，在她确认数字的一刻停住。`

抽象情绪优先压成可见动作链：
- 震惊：`停住 → 核对 → 抬头`
- 怀疑：`盯住证据 → 迟疑 → 再确认`
- 松弛：`肩膀放下 → 呼吸变慢 → 轻笑`

只有用户要求细演、面部特写或当前生成确实需要时，才展开FACS/眉眼鼻嘴细节。

关键交互保留必要因果：`接近 → 接触 → 响应/变化 → 完成态`。不为“严谨”自动描述每个手指、每厘米路径或全部中间态。

## 4. Signal Budget｜信息权重

最终Prompt不是知识展示。默认把文字预算优先给：
1. 主体身份、产品结构与当前状态；
2. 当前发生的事件；
3. 动作、表演与交互结果；
4. 跨镜连续和空间关系；
5. 必要镜头响应；
6. 只在有收益时加入的真实性、光影、材质、景深、设备信息。

### 真实性补丁

在主体与事件已经清楚后，后台只问一次：
`这个镜头最可能出现的一个AI错误是什么？`

只有答案明确时，补**最多1条**可见结果；没有明显风险就不补。

常见补丁：
- 漂浮：`鞋底紧贴地面，保留轻微接触阴影。`
- 产品失真：`产品尺寸和包装结构在推进中保持稳定。`
- 玻璃塑料感：`玻璃边缘保持透明折射，高光不过曝成死白。`
- 横移平面感：`近景移动快于远景，形成自然空间视差。`
- 焦点混乱：`眼睛清晰，背景自然退焦。`
- 环境脱节：`火光只轻微影响人物朝向火源的一侧。`

这些属于**按需补丁，不是固定字段，不得机械全加。**

## 5. Global Baseline｜Global Once

全局信息只定义一次，且只保留真正会持续影响后续镜头的内容：
- 片型/媒介/调性
- 人物与产品身份
- 空间基础关系
- 必要的主摄影质感
- 若确实影响结果的一套主光/色彩关系
- 持续声音规则

设备名必须对应可见结果；不把 IMAX、ARRI、UE5、Octane、VFX、8K、HDR 堆成“高级套餐”。

如果光线只是普通场景条件，不必独立写【光影】；人物、产品、服装、空间、主光没有变化时，分镜不得重复介绍。

## 6. Prompt Compile｜Shot Specific

写或重写最终提示词时读取 `references/prompt-compilation-and-consistency.md` 与 `references/output-contract-and-validation.md`。

### 默认格式｜简单/中等视频

1. **规格**：时长、画幅、必要模型/平台信息。
2. **【开场总控】**：1句，只写片型、调性、节奏、媒介观感；不写具体事件，不堆设备。
3. **【主体/锁定】**：只写会漂移的人物、产品、空间、参考事实；没有就省略。
4. **【时间轴】**：按观看顺序写。每段优先 `事件 → 动作/变化 → 结果 → 必要镜头响应`。
5. **按需真实性补丁**：直接并入对应镜头句子，最多1条，不单独堆模块。
6. **【声音/限制】**：只有需要时出现；只写准确对白、关键SFX或2–4个高风险限制。

### 复杂视频才展开

多人复杂换位、严格产品连续、多场景、复杂光线切换、一镜到底、长片生产等任务，才增加独立的表演、空间、光影等块。复杂度增加才增加Prompt长度。

### 编译纪律

- **Global Once, Shot Specific**：全局只说一次，分镜只写当前变化。
- 每镜先问“这镜唯一最重要的事是什么？”只围绕它写。
- 镜头信息默认只写**一个必要响应**：推近、后拉、跟随、固定等待、甩镜、环绕等。没有叙事价值就不写。
- 构图、焦段、景深、灯位只有在它们决定当前结果时才出现。
- 光影属于加分控制，不得占用比主体、事件、动作更高的信息权重，除非本轮任务本身就是灯光/画质。
- 不重复“真实、电影级、专业、高清、高端、自然光学”等同义词。
- 正向先写主体和动作结果；反向限制只处理当前高风险误读。
- 模型收到画面和声音，不收到“仔细分析、保证一次成功、增强高级感”等管理话。

## 7. Prompt Pollution Audit

交付前逐句检查：
1. 是否直接改变主体、事件、动作、表演、空间、镜头、光色、材质、时间、文字或声音？
2. 是否已经在全局块说过？
3. 是否只是把一个有效概念解释得更长？
4. 是否为了显得专业加入设备/摄影术语？
5. 是否把模型本可自由完成的镜头实现锁得过细？
6. 光影/真实感文字是否已经开始抢主体和事件的信息权重？

重复、解释性、低价值信息删除。**视频可以详细，但详细应该花在“发生什么、怎么变化、如何承接”，不是花在术语数量。**

## 8. Independent Judge

交付前读取 `references/independent-judge.md`。

Judge只检查失败点：事实、核心主体、核心事件、可见状态变化、空间/接触/连续性、必要的光影可读、镜头负载、Prompt冲突与冗余。FAIL时只修对应模块，不因局部问题整条推倒重来。

返修成片时优先定位最早或影响最大的可见问题，修最小相关片段，再检查前后承接。Prompt文字PASS不等于成片PASS。

## 输出与维护

- 默认给一版最佳结果；用户要求多版才给多版。
- 用户只要Prompt就交成品，不展开内部路由与判断。
- 用户指定原格式时保留其格式，但仍执行高信号压缩和去重。
- 用户授权更新时才修改规则；单次生成观察不直接晋升长期规则。
- 验证继续使用现有脚本、Skill Creator结构检查和 evaluation-cases；不把未真实生成的案例说成成片验证。