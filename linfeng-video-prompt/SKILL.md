---
name: linfeng-video-prompt
description: 把产品Brief、脚本、分镜、故事板、参考视频或成片问题转为精炼、一读成像、可直接生成的视频提示词、导演分析或分镜，并校验资产职责、创意幅度、节奏/风格一致、空间物理、声音、时长与模型容量。用于TVC、商业广告、UGC、短剧、产品演示、视觉奇观/超现实、复杂运镜、连续性返修、画质诊断及Seedance等视频模型工作流；用户说“林枫视频提示词skill”或要求写、改、检查视频提示词时使用。
---

# 林枫视频提示词｜Router Architecture

把导演判断编译为一读成像、可执行、不过载的视频提示词。主文件只负责：**锁定 → 路由 → 状态变化 → 光影入口 → 编译 → 独立QC**。专业知识继续保留在现有 references 中，只有命中任务时才加载，不把所有规则一次塞进Prompt。

## 固定链路

`Contract Lock → Route → State Change Compile → Visual Baseline → Prompt Compile → Independent Judge`

下游不得为了风格或创意改写上游事实。

## 1. Contract Lock

先锁定本轮真正会改变结果的信息：
- 交付类型：分析、方案、脚本/分镜、可复制Prompt、实际生成或局部返修；
- 模型/平台、时长、画幅、参考资产；
- 人物/产品/空间已确认事实；
- 必须出现、禁止出现、准确文字/声音/CTA；
- 用户指定的格式、风格、媒介。

用户已经给出的信息不重复询问；只缺少会改变事实或核心结果的信息时才问一个关键问题。

执行优先级：
`用户明确要求 > 已确认事实/参考资产 > 身份/产品/空间/声音一致性 > 核心事件/证据 > 光影成像 > 运镜/特效 > 默认审美`

普通项目只使用当前事实，不自动带入历史品牌、价格、人设、CTA、平台禁区或旧案例。

## 2. Route

先判断本片的**一个主任务**：
- 剧情/关系
- 产品/商业证据
- 人物表演
- 环境/视觉奇观
- 动作/运镜
- 返修/QC

再叠加真正会改变输出的次模块。不要因为“可能有用”就全部读取。

### 路由表

| 任务信号 | 读取模块 |
|---|---|
| 新写/重写Prompt、压缩、前后矛盾 | `references/prompt-compilation-and-consistency.md`、`references/output-contract-and-validation.md` |
| 每次新写、完整重写、光影/质感返修 | `references/camera-light-quality-baseline.md` |
| 抽象词、动作不落地、状态升级 | `references/state-change-compiler.md` |
| 商业任务、产品事实/比例、购买犹豫 | `references/commercial-contract.md`、`references/product-preflight-and-category-routing.md`、`references/decision-driven-ad-creative.md` |
| 首屏停留、强Hook | `references/golden-3s-hook-engine.md` |
| 多镜、连续节拍、参考反推 | `references/director-information-control.md` |
| 剧情对话、关系戏、人物目的/认知变化 | `references/drama-performance-control.md` |
| 已有剧情需细写微表情/FACS | `references/facial-expression-action-library.md` |
| 多人换位、正反打、交接、复杂空间 | `references/spatial-optics-physics-control.md`；跨镜再叠加 `references/continuity.md`，群像叠加 `references/ensemble-continuity.md` |
| 复杂运镜、动作戏、一镜到底 | `references/director-camera-attention.md` |
| 构图主次、关系揭示 | `references/camera-composition-decision-layer.md`、`references/composition-story-engine.md` |
| 摄影媒介/设备身份 | `references/camera-identity-selection-engine.md` |
| 具体摄影光学方案 | `references/cinematography-toolkit.md` |
| IMAX/UE5/Octane/VFX等质感栈 | `references/visual-quality-stack.md`；先过光影入口，再只选有职责的部分 |
| 实拍可信度、塑料感、失重、环境空洞 | `references/physical-reality-lock.md` |
| 模糊、过锐、脏灰、压缩/输出问题 | `references/visual-quality-diagnostics.md` |
| 写实+异常、产品世界化 | `references/grounded-surreal-product-spectacle.md` |
| A→B连续变形 | `references/visual-transformation-spectacle.md` |
| 物体/屏幕接管画面转场 | `references/physical-takeover-transitions.md` |
| 随拍、纪录、家庭录像、延迟追拍 | `references/observational-camera-authenticity.md` |
| UGC/生活分享/原生产品体验 | `references/ugc-ad-rules.md`；美妆社媒再叠 `references/stylized-social-beauty-ugc.md` |
| 食品/味觉/蒸汽 | `references/food-flavor-direction.md` |
| 选角、妆发、美感 | `references/casting-and-beauty-direction.md` |
| 品牌宣言/主题蒙太奇 | `references/brand-manifesto-montage.md` |
| TVC完整创作/生产/长片 | `references/tvc-full-workflow.md`、`references/tvc-production-operations.md`、`references/tvc-runtime-control.md` |
| 长片节奏/补拍/跨单元 | `references/longform-rhythm-and-retake.md` |
| 配音、精确台词、发音返修 | `references/voiceover-control.md` |
| Seedance工作流/能力边界 | `references/seedance-2.5-workflows.md` |
| 常见故障/跨工具交接 | `references/design-rules.md` |

阶段、默认审美和跨技能交接不明时读 `references/user-operating-contract.md`；混合任务主次不明时读 `references/direction-routing.md`；规则冲突/维护读 `references/rule-governance-and-module-routing.md`。

## 3. State Change Compile

新写或重写时读取 `references/state-change-compiler.md`。

关键Beat优先写成：
`起始状态 → 触发 → 可见动作/接触 → 状态变化 → 反应/镜头响应 → 完成态`

“荒诞升级、震惊、紧张、高级、超现实、电影感、压迫、失控”等抽象词不能单独成为执行指令；必须落成主体动作、空间变化、光线、材质、声音或镜头状态。

关键交互保留：`接近 → 接触 → 受力/响应 → 释放 → 完成态`。多镜只继承真正会影响下一镜的状态：人物位置/朝向/认知、手别与道具归属、商品/环境状态、相机/焦点、主光、声音。

## 4. Visual Baseline

每次新写、完整重写或光影/质感返修固定读取 `references/camera-light-quality-baseline.md`。

先定一套主摄影/媒介身份，再定世界中的主光来源、方向、软硬、明暗层次、色彩与材质。设备名必须对应可见结果；不把IMAX、ARRI、UE5、Octane、VFX全部堆成通用“高级套餐”。

主光按世界位置继承，人物转身或机位换侧不让灯跟着脸转。每镜只补变化项或当前证据需要的局部光。

## 5. Prompt Compile

写或重写最终提示词时读取 `references/prompt-compilation-and-consistency.md` 与 `references/output-contract-and-validation.md`。

完整Prompt默认结构：
1. 【开场总控】只写风格、调性、观感、平台感；不写具体事件。
2. 【主体、空间与参考锁定】
3. 【表演与状态】
4. 【光影与成像基线】
5. 【分镜描述】按观看顺序写自然句，动作与结果优先。
6. 【声音】只写本片需要的对白、环境声、SFX/BGM节点。
7. 【反向限制】只保留当前高风险误读，不做长禁词墙。

编译纪律：
- 模型收到画面，不收到“仔细分析、保证一次成功、加强高级感”等管理话。
- 正向优先 `主体 + 准确动作 + 对象/位置 + 完成结果`。
- 每个镜头一个主要任务；复杂不等于同时堆动作、对白、运镜、特效。
- 用户指定手机随拍、粗糙手绘、动画或超现实时保留该媒介；真实感指该世界内部物理可信，不强制都变成干净电影摄影。
- 生成单元与剪辑镜头分开；默认独立生成单元不少于4秒只是工作流默认，不宣称模型硬下限。

## 6. Independent Judge

交付前读取 `references/independent-judge.md`。

Judge只检查失败点：事实、核心事件、可见状态变化、空间/接触/连续性、光影可读、镜头负载、Prompt冲突与冗余。FAIL时只返回对应模块修正，不因局部问题整条推倒重来。

返修成片时优先定位**最早或影响最大的可见问题**，修最小相关片段，再检查前后承接。Prompt文字PASS不等于成片PASS。

## 输出与维护

- 默认给一版最佳结果；用户要求多版才给多版。
- 用户只要Prompt就交成品，不展开内部路由与判断。
- 用户授权更新时才修改规则；单次生成观察不直接晋升长期规则。
- 验证继续使用 `python3 scripts/audit_module_routing.py`、Skill Creator结构检查和现有 evaluation-cases；不把未真实生成的案例说成成片验证。
