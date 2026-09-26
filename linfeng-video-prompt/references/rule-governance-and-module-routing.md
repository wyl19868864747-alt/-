# 规则归属与模块路由

本文件用于混合任务冲突、路由诊断和技能维护；普通任务先按 SKILL.md 的入口完成，不要求每次加载整个知识库。

## 1. 主次与叠加

第一轴判断商业记忆/剧情关系，第二轴判断表演/环境产品体验。两轴只决定篇幅主次，不封闭其他能力。路由表是并列勾选项，不得命中第一项后停止；只读取语义命中的文件，只把当前镜头需要的规则编译进成品。

标签含 `grounded-surreal`、`transformation-spectacle`、`observational-camera` 与 `attention-first-hook` 等；标签是后台索引，不是给视频模型的口令。专用玩法不变成所有片型的通用默认。

## 2. 单一归属

| 问题 | 详细规则唯一归属 |
|---|---|
| 阶段、默认交付与用户稳定偏好 | `user-operating-contract.md` |
| 商业/剧情与表演/体验主次 | `direction-routing.md` |
| 输出块、开场边界、声音放置、负面项和终检 | `output-contract-and-validation.md` |
| 逐镜空间状态编译、最小空间信号、创意幅度、信息压缩、容量、情绪转译和状态矛盾 | `prompt-compilation-and-consistency.md` |
| 切镜密度、相隔景别、30°同侧机位、动静组接 | `director-information-control.md` |
| 声线预算、逐窗台词容量、声音桥、BGM节点 | `voiceover-control.md` |
| 常驻摄影机/视觉成像底盘（真实透视、运动模糊、材质差异、光×材质局部反馈、亮暗结构、颜色层级、景深信息层级及基础构图空间层次）及条件灯光/设备/光学可见结果 | `camera-light-quality-baseline.md` |
| AIGC原生虚实结合、现实底盘中的单一不可能机制 | `aigc-native-visual-event-design.md`；连续形变细节由 `visual-transformation-spectacle.md`，写实超现实合同由 `grounded-surreal-product-spectacle.md` |
| 空间坐标、关键接触与复杂物理动作 | `spatial-optics-physics-control.md` |
| 多镜空间接力锁：运动所有权、固定观察走廊、到达锚点、光影辅助坐标 | `spatial-handoff-lock.md` |
| 完成态字段、人物/道具/目标/相机继承与变化因果 | `continuity.md` |
| 逐对空间A–J验收及失败回写 | `independent-judge.md` |
| 产品事实与尺度预检；商业身份交接 | `product-preflight-and-category-routing.md`；`commercial-contract.md` |
| 模型入口、参考/编辑/延长、能力证据 | `seedance-2.5-workflows.md` |

其余领域在 SKILL.md 直接列出触发与文件。主文件保留短的不可漏原则，参考文件负责详细方法与必要示例；其他模块用一句引用，不复制整套输出模板、灯光表或检查表。

## 3. 规则冲突

优先级唯一采用 SKILL.md 的执行顺序；较低层必须在用户媒介、事实与因果边界内调整。专项文件能收窄本场景的写法，不能把“用户要手机随拍”改成无噪电影片，不能把局部修正扩大为整片重做，也不能把某行业禁区变成所有项目的限制。

**约束默认是 Validator / Repair Layer，不是 Creative Selector。** 已经成立的 Hero Idea 先保留，空间、物理、容量、画质和模型规则用于指出哪里会失败，并优先修实现路径；不得因为某方案更复杂就自动选择更普通的替代方案。只有事实/合规、用户明确要求、已知模型能力、真实时长容量、素材证据或物理因果构成硬边界时，才允许最小幅度降低创意幅度。反过来，Hero Idea 也不能成为绕过事实和执行边界的理由。

同一事实放在最高有效层一次：资产管身份，空间管固定关系，表演管情绪轨迹，`camera-light-quality-baseline.md` 管常驻 Capture Baseline / Visual Surface Pass 与条件灯光，分镜管当下变化。**Visual Surface Pass 属于所有新写／重写视频 Prompt 的常驻读取能力：每次必须检查材质、受光、颜色、景深、构图，但最终不得拆成五个输出层；只有改变当前画面的结果才压缩进总控或对应镜头。复杂布光、设备和高级光学仍是条件层。** 需要跨镜提醒时只重申关键状态，不完整复述。硬事实、明确排除项仍保留，不能因偏好正向语言而删掉必要边界。

## 4. 更新与证据

1. 先定位已有归属；能合并就改原规则，不另增同义章节。
2. 新领域确需新文件时，同时在主文件添加语义入口。正文的旧模板、示例和评估预期一并更新，不能留下两个权威版本。
3. 主文件只收稳定的工作顺序与必要底线；专业例子进专项；项目品牌、价格、人物、坐标与一次性数值留在项目层。
4. 区分用户批准的工作约定、官方能力说明、实际测试记录与待验证假设。一次失败不能推出永久禁令；没有成片测试不能声称提高成功率或完全避免穿模。
5. 结构检查跑 `scripts/audit_module_routing.py` 与 Skill Creator 验证；审计必须保证 `camera-light-quality-baseline.md` 位于写／重写 Prompt 的强制读取链，并保证主 Skill 明确保留 Visual Surface Pass 的“每次必判断、融合输出、不拆五层”规则，以及“先保护 Hero Idea，再修执行”的上位约束。行为用例覆盖主要触发、混合任务、创意保护与不应误触发的简单场景，按改变范围选测。

维护时可在后台列“已命中模块—具体使用位置—排除原因”，普通生成不交付路由审计表。将复杂知识保留为可读取的参考，不为追求字数删除有效的专业能力。
