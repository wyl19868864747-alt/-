---
name: pet-short-drama-skill
description: 面向欧美社媒的宠物短剧、剧情带货、UGC开箱和身份翻盘短片。总控加载全局核心规则、项目事实及单一主风格；逐镜继承空间完成态、预演物理接触、设计摄影构图和声音，并在最终提示词中落实反应镜头、后果与完整结尾。
---

# Pet Short Drama Director Skill｜总控路由

**本文件只管调用顺序、规则优先级与交付闸门。** 规则母版在 `references/CORE_RULES.md`；各风格只写创意增量，不重写全局规则。

## 1｜加载顺序与优先级

每次调用先读 `references/CORE_RULES.md`，再根据请求载入：

1. **全局母版**：`references/CORE_RULES.md` 明确 G-01～G-08 的归属文件与强制适用阶段。执行分镜／Prompt任务时按母版加载 00～07 公共模块；成片返修还须加载回归案例。
2. **本次项目事实**：当前上传的参考图／视频、已确认的角色与场景，按 `references/PROJECT_CONTRACT.md` 建立项目状态；没有的参考不能虚构。
3. **一个主风格**：从 `references/styles/` 选取。混合时只允许副风格补局部机制；不能用风格规则覆盖全局核心或项目事实。
4. **交付验收**：`evaluation/REGRESSION_CASES.md` 与 `evaluation/CROSS_STYLE_REGRESSION.md`；发现失败回到最早失效镜头，后续逐镜重新继承。

优先处理当前用户明确给出的事实、规格与创意例外；创意例外必须明确描述视觉变化过程，不得以“风格化”为借口省掉空间位移、道具交接或镜头接续。全局核心对所有风格生效，风格文件仅补充独有的故事节拍与表现方式。

## 2｜选择主风格

| 用户任务 | 加载文件 |
|---|---|
| 宠物IP、小事件大叙事、荒诞英雄 | `references/styles/ip-story-superhero-absurd.md` |
| 宠物剧情带货、产品体验 | `references/styles/commerce-story-product.md` |
| 宠物UGC开箱、产品发现 | `references/styles/ugc-unboxing.md` |
| 欧美竖屏豪门、复仇、身份翻盘 | `references/styles/us-vertical-revenge-identity-flip.md` |

没有创意：基于账号与目标构想一版大纲；已有故事：保留核心事件，只修因果与生成风险。使用“之前的金毛”时从 `references/00-project-defaults.md` 读取默认IP；用户新参考明确取代旧身份时以当前参考为准。

## 3｜生产流程：边写边预演，不再事后补锁

`选风格与项目事实 → 大纲 → 逐镜循环〔继承上镜末态 → 设计真实动作／接触 → 预演可达性与容量 → 选观察机位／景别／运镜／【构图】 → 冻结本镜末态〕 → Prompt编译 → 声音／结尾核算 → 验收 → 生成后局部返修`

**逐镜循环不可拆成“先写完所有漂亮分镜，最后再检查连续性”。** 下一镜首态必须等于上一镜末态；角色暂时出画仍保留位置与运动。摄影机换位不能替角色完成位移；构图不能重摆演员。具体执行见 `references/01-spatial-state-chain.md`、`references/02-physical-previsualization.md`。

大纲只写事件和关系；分镜／最终Prompt每镜均有 `时间＋景别＋观察机位／运镜＋【构图】＋当前位置／动作＋必要台词／声音`。角色说话的口型、词数、时间窗及尾部停留必须实际容得下。

## 4｜交付格式与最终闸门

- **只要大纲**：仅给故事结构；不提前堆摄影术语。
- **要导演分镜**：逐镜现状、可见位移、摄影角度／运镜、`【构图】` 和声音；先完成逐镜预演。
- **要视频Prompt**：规格 → 参考职责 → 必要角色／声线／持续环境 → 连续时间轴（每镜含【构图】）→ 一条持续BGM及事件音；按 `references/07-prompt-compiler.md` 去除抽象目标词。不在末尾追加“空间锁”代替逐镜动作。
- **已生成成片**：先核验实际文件，再对照分镜查穿帮；保留成功镜头，优先局部返修。

最终静默检查：`参考与身份 → 每镜状态接力 → 物理接触与动作时间 → 同轴摄影与构图 → 宠物声线与口型 → BGM变化 → Reaction → Consequence → Final State → 约1秒停稳`。

最后一句狠话／产品卖点／Reveal不是终点；结尾要看见反应、后果真的发生、人物或场景进入完成态后再结束。风格可改变结尾呈现，不能删除结尾闸门。

## 5｜维护规则：改一处，所有风格继承

- 发现跨风格问题，先按 `references/CORE_RULES.md` 定位唯一规则拥有者，**只修改公共模块**；风格文件只记录该风格额外案例，不复制核心正文。
- 给修订规则分配／保留 G-ID，补充 `evaluation/REGRESSION_CASES.md` 真实失败案例，按 `evaluation/CROSS_STYLE_REGRESSION.md` 为每个现有风格检查适用结果。
- 新风格只新增 `references/styles/<style>.md` 并登记到本路由及跨风格矩阵，不复制 01～07 模块。
- 修改后运行 `evaluation/validate_structure.py`（静态结构检查），再做跨风格逐镜推演；静态通过不等于视频生成通过。
- GitHub `main` 的 `pet-short-drama-skill/` 为 SSOT，先同步母版，再更新其他平台副本；禁止以旧压缩包反向覆盖。
