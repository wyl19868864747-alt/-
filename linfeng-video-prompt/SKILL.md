---
name: linfeng-video-prompt
description: 把产品Brief、脚本、分镜、故事板、参考视频或成片问题转为精炼、一读成像、可直接生成的视频提示词、导演分析或分镜，并校验资产职责、创意幅度、节奏/风格一致、空间物理、声音、时长与模型容量。用于TVC、商业广告、UGC、短剧、产品演示、视觉奇观/超现实、复杂运镜、连续性返修、画质诊断及Seedance等视频模型工作流；用户说“林枫视频提示词skill”或要求写、改、检查视频提示词时使用。
---


# 林枫视频提示词

把导演判断编译为一读成像、能直接执行的视频提示词。主文件负责入口与优先级；详细规则各有一个归属文件，命中条件才读取，读过且未变更的文件本轮不重复读。

## 工作顺序

1. **确定交付**：分析、方案、脚本/分镜、可复制提示词、实际生成或局部返修。沿用用户已给的语言、格式、模型、时长和资产；只缺少会改变事实或核心结果的信息时才问一个关键问题。只要提示词就交成品，不附内部推理。
2. **确定主次**：第一轴选商业记忆或剧情关系；第二轴选人物表演或环境/产品体验。混合任务确定主导层，同时叠加必要模块。主次不明时读 `references/direction-routing.md`；阶段、默认审美和交接不明时读 `references/user-operating-contract.md`。
3. **锁事实与动作**：后台用 F/I/P/U 区分已确认事实、创作推断、偏好与未知；推断不变成产品事实。先定核心事件、人物目的、关键结果、资产职责和动作因果，再定运镜。多镜只记需要继承的状态；简单片段直接写起点、路径、接触与完成态。
4. **先定光影，再写镜头**：每次新写、完整重写或光影/质感返修，读取 `references/camera-light-quality-baseline.md`。它是固定入口，不等用户提醒“电影感”。编辑继承原片，只有变动的光源、材质或场景重新设计；光影服务主体与叙事，不改变商品本色。
5. **编译**：写或重写视频提示词时读取 `references/prompt-compilation-and-consistency.md` 与 `references/output-contract-and-validation.md`。完整提示词采用“概念开场—资产—表演—空间—光影—分镜—反向”的结构，分镜采用连续自然句；简单动作和局部编辑用对应短格式。
6. **检查并交付**：依输出合同做一次集中检查，失败只回到相应归属文件修正。默认给一版最佳结果；要求多版才给多版。实际生成只有工具可用且用户请求时执行，提示词通过检查不等于成片已验证。

## 执行优先级

`用户明确要求 → 已确认事实与资产 → 身份、产品、空间/动作/声音一致性 → 叙事与关键证据 → 光影、成像与色彩 → 运镜/特效装饰 → 默认偏好`。

- 用户选手机随拍、粗糙手绘、动画或超现实，就保留该媒介与创意。真实感指该世界内的接触、遮挡、重量和因果可信，不把所有片子改成干净电影摄影。
- 正向先写谁在什么位置、做什么、接触哪里、造成什么结果；把“不要乱、不要穿模、要高级”翻译成具体关系。少量负面项只处理当前严重误读。
- 主光按世界位置继承，人物转身或机位换侧不让灯跟着脸转。每镜只补发生变化或决定叙事的局部光影。
- 关键交互保留接近、接触、受力、响应、释放与完成态；人物/道具换位可见可达。产品身份、数量、真实尺度和持有权连续，精确声音/文字只有一个真源。
- 生成单元与剪辑镜头分开：本工作流默认独立生成单元不少于4秒，内部镜头可更短；这是制作默认，不是所有模型的技术下限，用户明确要求且平台支持时按用户要求。
- 普通项目只使用当前事实与资产，不自动带入历史品牌、价格、人设、平台禁区、场景或CTA。完整预算不足时保住核心看点、反应和结果可读性，先减少同时竞争的动作。

## 按需调用表

下表是**并列勾选项**，不得命中第一项后停止；每个命中模块只应用与当前段落有关的内容。这里是路由，不要求全部展开进提示词。

| 任务信号 | 规则归属 |
|---|---|
| 新写/重写提示词、压缩、解决前后矛盾 | `references/prompt-compilation-and-consistency.md`、`references/output-contract-and-validation.md` |
| 光影、设备、材质、色彩；每次新写的固定入口 | `references/camera-light-quality-baseline.md` |
| 阶段、稳定默认、跨技能资产交接 | `references/user-operating-contract.md` |
| 混合任务主次、商业/剧情和表演/体验双轴 | `references/direction-routing.md` |
| 模块冲突、规则归属或维护 | `references/rule-governance-and-module-routing.md` |
| 商业任务、产品事实与比例、购买犹豫 | `references/commercial-contract.md`、`references/product-preflight-and-category-routing.md`、`references/decision-driven-ad-creative.md` |
| 短视频首屏停留、强Hook | `references/golden-3s-hook-engine.md`；按目标区分标准Hook与 `attention-first-hook` |
| 多镜、连续节拍、参考反推、每镜为什么拍 | `references/director-information-control.md` |
| 剧情对话、关系戏、抢话、人物目的与认知变化 | `references/drama-performance-control.md` |
| 已有剧情需细写情绪、微表情、反应 | `references/facial-expression-action-library.md`；全局写情绪轨迹，局部写触发后的动作 |
| 多人换位、交接、正反打、复杂空间或穿模返修 | `references/spatial-optics-physics-control.md`；跨镜叠加 `references/continuity.md`，群像叠加 `references/ensemble-continuity.md` |
| 复杂运镜、动作戏、一镜到底、镜头注意力 | `references/director-camera-attention.md` |
| 构图选择、主次不清、关系或信息揭示 | `references/camera-composition-decision-layer.md`、`references/composition-story-engine.md` |
| 设备家族、摄影者身份、媒介成像差异 | `references/camera-identity-selection-engine.md` |
| 需要具体摄影光学方案 | `references/cinematography-toolkit.md` |
| IMAX、UE5、Octane、VFX、东方奇幻等质感栈 | `references/visual-quality-stack.md`；先读光影入口，再选有实际职责的部分 |
| 实拍可信度、塑料感、失重动作、环境空洞 | `references/physical-reality-lock.md` |
| 模糊、过锐、脏灰、压缩或输出规格问题 | `references/visual-quality-diagnostics.md` |
| 写实与异常结合、物体自行运动、产品世界化 | `references/grounded-surreal-product-spectacle.md`，标签 `grounded-surreal` |
| A→B变形过程是核心看点 | `references/visual-transformation-spectacle.md`，标签 `transformation-spectacle` |
| 物体、门、屏幕等接管画面形成转场 | `references/physical-takeover-transitions.md` |
| 随拍、纪录、家庭录像、延迟追拍 | `references/observational-camera-authenticity.md`，标签 `observational-camera` |
| UGC、生活分享、原生产品体验 | `references/ugc-ad-rules.md`；美妆社媒风格叠加 `references/stylized-social-beauty-ugc.md` |
| 食品、味觉、蒸汽与食欲 | `references/food-flavor-direction.md` |
| 选角、妆发、美感与人物呈现 | `references/casting-and-beauty-direction.md` |
| 品牌宣言、主题蒙太奇 | `references/brand-manifesto-montage.md` |
| TVC完整创作、生产交付、长片运行 | 分别读取 `references/tvc-full-workflow.md`、`references/tvc-production-operations.md`、`references/tvc-runtime-control.md` |
| 长片节奏、局部补拍、跨单元承接 | `references/longform-rhythm-and-retake.md` |
| 配音、精确台词、发音返修、有声/无声转换 | `references/voiceover-control.md` |
| Seedance生成/参考/编辑/延长与能力边界 | `references/seedance-2.5-workflows.md`；以当前入口为准 |
| 常见故障、跨工具交接 | `references/design-rules.md` |
| 视觉语言术语与基础例子 | `references/visual-language.md` |

## 维护

用户授权更新时才修改规则。详细归属与升级条件见治理文件；验证运行 `python3 scripts/audit_module_routing.py` 和 Skill Creator 结构检查，再选受影响行为案例，不把未生成的案例说成成片测试。

案例入口：`evaluation-cases/director-and-quality-cases.md`、`evaluation-cases/portable-behavior-cases.md`、`evaluation-cases/cross-module-routing-cases.md`、`evaluation-cases/grounded-surreal-cases.md`、`evaluation-cases/transformation-spectacle-cases.md`、`evaluation-cases/observational-camera-cases.md`、`evaluation-cases/product-identity-handoff-cases.md`、`evaluation-cases/spatial-prompt-compression-cases.md`、`evaluation-cases/lighting-and-format-cases.md`。
