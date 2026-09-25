---
name: linfeng-video-prompt
description: 把产品Brief、脚本、分镜、故事板、参考视频或成片问题转为精炼、一读成像、可直接生成的视频提示词、导演分析或分镜，并校验资产职责、创意幅度、节奏/风格一致、空间物理、声音、时长与模型容量。用于TVC、商业广告、UGC、短剧、产品演示、视觉奇观/超现实、复杂运镜、连续性返修、画质诊断及Seedance等视频模型工作流；用户说“林枫视频提示词skill”或要求写、改、检查视频提示词时使用。
---

# 林枫视频提示词

把用户意图先设计成事件，再编译成能拍到、能听到的提示词。判断留在后台，成品直接给画面与声音。

## 1. 不可漏的执行约定

- **最终模型指令不出现结果评价词**：包括“极强抓眼、高能、高级感、电影感、有感染力、热门感、突出情绪、信息推进快”。标题、总控、分镜、声音块同样检查；先设计具体事件、动作、切点和声音变化，再删掉评价。可观察的物理完成态必须保留，例如“泡沫被水冲掉、杯底落桌”；不能误删为“结果词”。
- **画面优先**：主体/产品、事件、动作与当镜空间关系占主体；空间是逐镜编译前置变量，不是尾部补充。音色每个说话者默认一句，光影、配乐和真实性描述不淹没主体。声音或摄影为本轮主任务时才展开。
- **每个明确分镜都有简短摄影机描述**，含快切组内每个子镜。以“景别＋机位＋运镜”短语融入动作句，不解释为什么动或不动。摄影机必须和画面事件耦合：动作／视线／遮挡／形变触发镜头，镜头结束时必须新增可见信息；位移、视线转移、空间揭示分别选跟移、摇镜、后拉，形变传播优先让镜头跟随变化前沿。固定机位用于必须让观众连续看清异常过程的画面。
- **摄影机与成像基线是常驻能力**：任何新写／重写视频 Prompt 都必须读取并执行 `references/camera-light-quality-baseline.md` 的 Capture Baseline。默认保证真实摄影透视、与速度相符的自然运动模糊、不过锐的主体细节、真实皮肤／材质受光、亮部与暗部结构及服务信息层级的景深；只用一条最短全局成像句或必要局部结果下发，不机械逐镜复述。复杂布光、设备与高级光学仍按需展开；用户明确的手机、DV、监控、实验失焦等媒介优先。
- **默认多镜视频平均约1–3秒一切**，在动作接点、新信息或反应处切，不等长切。相邻非特写镜头按相隔景别衔接；每次切镜改变观察角度大于30°，留在同一轴线侧。特写只豁免相隔景别要求，不豁免机位与连续性。切镜细则归 `references/director-information-control.md`。
- **剧情对白不是关键词队列**：有角色对话时，大多数台词保持自然口语意群，并承接上一句或上一动作；1–2词反应只作少量节拍，不能连续用“Really? / Fine. / Sure.”这类碎片凑节奏。时长冲突先删重复意思／重复视觉，不把全部句子削成单词。
- **连续与容量是交付条件**：每镜先继承上一镜的人物位置/朝向、道具归属/接触、目标位置、相机轴侧/观察方向和动作完成态，再设计动作及机位；逐段检查动作和台词所需时间，两人对白合并计算，预留交接与结尾约1秒收束。超载先精简或重排，不能靠“高速、流利”强塞。明确的一镜到底、固定镜头、慢片或其他用户约定优先，不强制套默认切镜密度。

## 2. 工作链路

`锁事实 → 设计事件与时间预算 → 逐镜继承空间完成态 → 当前关系与动作 → 可见的观察位置 → 景别/机位/短运镜 → 完成态交接 → 逐对验收`

1. 锁交付类型、模型/平台、时长/画幅、参考职责、人物/产品/空间事实、准确台词/文字及禁项。已给的信息不重复问；只缺真正改变任务的信息才问。
2. 选一个主任务：剧情、产品证据、表演、环境奇观、动作运镜或返修。路由是并列勾选项，不得命中第一项后停止，也不为“可能有用”加载全部模块。
3. 写/重写Prompt必读 `references/prompt-compilation-and-consistency.md`、`references/spatial-handoff-lock.md`、`references/camera-light-quality-baseline.md` 与 `references/output-contract-and-validation.md`；每次先过空间接力锁与 Capture Baseline 判断，简单单镜也不能跳过成像基线，但不因此增加多余逐镜文字；高风险移动自动启用固定观察走廊。抽象目标先编译，不直接传给模型。两镜以上继续读取镜头、节奏与连续性对应模块；有对白必读声音模块。
4. 每镜执行 Per-Shot Spatial State Compile，并先过 Spatial Handoff Lock：继承全员完成态，明确本镜谁移动、谁原地；跨区域／往返／一动一静时固定高风险运动段的观察方向，抵达后近景保留一个同地地标或受光证据，再选景别、机位与短运镜；把镜尾全员状态交给下一镜。切点和时间预算同步校验，台词可跨镜作声音桥，节奏功能留在后台。
5. 交付前读 `references/independent-judge.md`。只修失败部分，随后复核前后接续；文字通过不等于成片通过。

### 路由表

| 任务信号 | 读取模块 |
|---|---|
| 新写/重写Prompt、压缩、前后矛盾 | `references/prompt-compilation-and-consistency.md`、`references/spatial-handoff-lock.md`、`references/output-contract-and-validation.md` |
| 所有新写/重写视频Prompt | `references/camera-light-quality-baseline.md` 的 Capture Baseline；常驻执行，复杂灯光不自动展开 |
| 光影/质感/摄影明确为主任务或返修目标 | 在常驻基线上展开 `references/camera-light-quality-baseline.md` 的 Lighting / Advanced 层；必要时再读 `references/cinematography-toolkit.md`、`references/visual-quality-diagnostics.md` |
| 抽象词、动作不落地、状态升级 | `references/state-change-compiler.md` |
| 商业任务、产品事实/比例、购买犹豫 | `references/commercial-contract.md`、`references/product-preflight-and-category-routing.md`、`references/decision-driven-ad-creative.md` |
| 首屏停留、强Hook | `references/golden-3s-hook-engine.md` |
| 多镜、连续节拍、参考反推、节奏调性/呼吸 | `references/director-information-control.md`、`references/rhythm-function-control.md`、`references/continuity.md` |
| 剧情对话、关系戏、人物目的/认知变化 | `references/drama-performance-control.md` |
| 已有剧情需细写微表情/FACS | `references/facial-expression-action-library.md` |
| 多人换位、正反打、交接、复杂空间 | `references/spatial-handoff-lock.md`、`references/spatial-optics-physics-control.md`；跨镜再叠加 `references/continuity.md` |
| 复杂运镜、动作戏、一镜到底 | `references/director-camera-attention.md` |
| 构图主次、关系揭示 | `references/camera-composition-decision-layer.md`、`references/composition-story-engine.md` |
| 摄影媒介/设备身份 | `references/camera-identity-selection-engine.md` |
| 具体摄影光学方案 | `references/cinematography-toolkit.md` |
| IMAX/UE5/Octane/VFX等质感栈 | `references/visual-quality-stack.md`；只选有职责的一项或少量组合 |
| 实拍可信度、塑料感、失重、景深失控、环境空洞 | `references/physical-reality-lock.md` |
| 模糊、过锐、脏灰、压缩/输出问题 | `references/visual-quality-diagnostics.md` |
| 写实+异常、产品世界化 | `references/grounded-surreal-product-spectacle.md` |
| A→B连续变形 | `references/visual-transformation-spectacle.md` |
| 真实场景＋不可能变化、虚实结合、AI原生视觉事件 | `references/aigc-native-visual-event-design.md`、`references/grounded-surreal-product-spectacle.md` |
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
| 片型/创意主次冲突 | `references/direction-routing.md` |
| 阶段、直接输出、用户操作约定 | `references/user-operating-contract.md` |
| 规则维护、归属冲突 | `references/rule-governance-and-module-routing.md` |
| 群像与多角色连续 | `references/ensemble-continuity.md` |
| 长片节奏与返拍 | `references/longform-rhythm-and-retake.md` |
| 风格化美妆UGC | `references/stylized-social-beauty-ugc.md` |
| 视听语言诊断、广告节拍画面化 | `references/visual-language.md` |

## 3. 最小编译

- 全局只定义一次主体/产品/参考、必要固定拓扑和持续声音；后台每镜运行空间接力锁，动态站位、朝向、运动者／静止者、接触和相机关系只把影响本镜的最小继承信息编入各镜，不另附空间位置锁。没有参考图时不假称已锁定参考；不用旧项目品牌、人物或价格填空。
- 每镜用最短完整句交代“谁在何处做什么、怎样变化、镜头怎样跟进”。关键交互保留接近、接触、响应和完成态，不逐指逐厘米展开。
- 开场总控可省略；保留时只用一句交代片型、媒介和必要成像特征，不堆评价或镜头清单。具体事件直接进时间轴。
- 默认只交规格、必要锁定、逐镜时间轴、简短声音。准确对白放实际时间窗一次；不再附镜头流、产品露出表、情绪曲线和一致性复述。
- 表情用短动作链：“停手—复核—抬头”“缩肩—放松—轻呼气”；细演或特写任务才展开表情库。
- 主体和动作清楚后，只补当前明确风险的一条最短真实性修正；没有风险就不加。必要接触和状态因果不能以“补丁只能一条”为由删掉。
- 每次写/重写Prompt都执行 `references/camera-light-quality-baseline.md` 的常驻 Capture Baseline，并把它压成一条最短全局成像句或必要局部结果；不逐镜重复。复杂光影／设备／光学只有明确影响当前画面时才展开。设备名必须有可见职责，不堆ARRI、IMAX、UE5、8K等词包；主体未写清前不加光学装饰。
- BGM按剧情选择可听的节奏、音色与进入/抽空/收束节点；口播时压低，不替画面制造情绪。无配乐要求优先；无声片不擅自加声音。

## 4. 输出与维护

默认一版最佳成品；用户只要Prompt就不外显分析。指定格式优先，但仍去重并执行容量检查。局部返修保留未失败的事实与设计，不重做整片。

维护先找规则归属，修改旧模板与冲突示例，禁止只追加口号。运行现有结构检查与相关 evaluation-cases；基础空间编译回归见 `evaluation-cases/per-shot-spatial-state-regression.md`，固定观察走廊／运动所有权／到达锚点回归见 `evaluation-cases/spatial-handoff-lock-regression.md`，常驻摄影机／成像基线回归见 `evaluation-cases/lighting-and-format-cases.md`，AIGC原生视觉事件／镜头耦合／自然对白回归见 `evaluation-cases/aigc-dialogue-camera-regression.md`。未实际生成，不宣称成片效果已经验证。
