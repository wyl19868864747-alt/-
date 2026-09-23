# Pet Short Drama Skill v1.2.0

**一条原则只维护一处，所有风格共同继承。** `SKILL.md` 负责调用；`references/CORE_RULES.md` 是全局规则索引；`references/00～07` 是各规则唯一拥有者；`references/styles/` 只写风格增量；`references/PROJECT_CONTRACT.md` 承载每条视频的实际角色／场景事实；`evaluation/` 管跨风格回归。

## 当前对白基线

默认30秒带对白宠物短剧**至少12句有效英文短对白**，按情绪与信息递进排布；一句算一个真实发声轮次，不把机关音效、吠叫或拆句充数。逐句安排镜头／发声者／自然时长，最后保留Reaction、Consequence、Final State与停稳。规则归属 G-05 的 `references/04-performance-voice-lipsync.md`，所有风格继承；用户明确静音等任务除外。

## 正确打开方式

- 没想法：`调用宠物短剧Skill，主角还是之前的幼年金毛，选欧美豪门身份翻盘风格，先出30秒大纲。`
- 有想法：`调用宠物短剧Skill，保留我的剧情，先输出每镜有【构图】的导演分镜，边写边做空间状态接力。`
- 要预演：`按上一镜末态推演下一镜首态，检查位移、接触、台词和机位，只改失败镜头。`
- 要Prompt：`调用宠物短剧Skill＋林枫视频提示词Skill，按已通过分镜编译Seedance提示词，不要污染词。`
- 成片返修：`按REGRESSION_CASES复盘这条视频，只修最早出错处并向后传递末态。`

## 新内容放哪里

- 所有风格都会受影响的规则：`CORE_RULES.md` 找到 G-ID → 修改对应 `references/00～07` **唯一拥有者** → 更新回归测试，不能只塞进某个风格文件。
- 新片型：新建 `references/styles/<name>.md`，写清 `全局继承：../CORE_RULES.md`，只加该片型独有节拍／道具／镜头案例，并在 `SKILL.md` 路由和 `CROSS_STYLE_REGRESSION.md` 登记。
- 某条视频的角色、位置、产品、参考：只进入项目事实卡和逐镜状态，不污染全局／风格母版。
- 真实成片的新穿帮：`evaluation/REGRESSION_CASES.md` 记录可观察失败与修复，再评估是否要提升至核心规则。

## 验收与同步

先运行 `python3 evaluation/validate_structure.py`，再按跨风格矩阵做文本逐镜推演；静态检查不能证明实际生成视频不会穿帮。GitHub `main` 为 SSOT；压缩包、当前账号和 iMA 都是需要单独同步／导入的副本。
