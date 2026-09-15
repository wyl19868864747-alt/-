---
name: skill-engineering-governance
description: Use when creating, editing, distilling, syncing, refactoring, evaluating, or declaring completion of any Skill in this repository, especially when changes come from external Skills, failure cases, user feedback, or GitHub SSOT synchronization.
---

# Skill 工程治理｜Evidence-Driven Evolution

把 Skill 当成需要持续验证的行为系统，而不是不断追加规则的文档。

核心原则：**先找失败与根因，再做最小修改；任何“已完成 / 已同步 / 已修复”都必须有新鲜证据。**

## 1. Layer Separation

先判断问题属于哪一层，禁止跨层打补丁：

- **Interaction Layer**：回答方式、状态表达、下一步呈现。
- **Governance Layer**：Skill 创建、修改、蒸馏、同步、测试、版本治理。
- **Domain Layer**：视频、广告、UGC、TVC 等专业判断。
- **Prompt Layer**：最终下发给生图 / 生视频模型的可执行提示词。
- **Runtime Layer**：平台上下文、工具调用、Agent 编排、连接器或运行代码。

若问题属于 Runtime，不得靠给业务 Skill 继续加字来掩盖。

## 2. Distill Before Import

外部 Skill 只能先蒸馏，再使用：

1. 提取可跨项目复用的**机制**，不是复制原项目流程。
2. 删除与原领域绑定的命令、框架、角色设定和无关规则。
3. 判断机制应落在哪一层；治理规则优先留在 Governance，不污染专业 Skill。
4. 只把会改变当前系统行为的最小规则写入。
5. 长段原文不直接搬运；使用自己的结构和语言重写。

当前已确认可吸收的两类机制：

- `obra/superpowers`：失败先行、根因定位、最小修复、回归验证、完成前证据校验。
- `ayghri/i-have-adhd`：答案前置、步骤有界、状态可见、错误直说、减少跑题与无效开场。

后者只作为**操作沟通协议**使用，不把 ADHD 身份框架写入业务 Skill，也不把交互措辞写进生成模型 Prompt。

## 3. Failure-First Skill Evolution

新增或修改一条行为规则前，先定义至少一个失败案例或压力案例。

优先顺序：

`真实失败案例 > 历史用户反馈 > 可复现压力案例 > 纯理论假设`

执行：

`Baseline → Failure → Root Cause → Minimal Rule → Re-run → Regression`

如果当前环境无法真正运行旧版本与新版本对比，可以继续做结构性修改，但必须标记为：

`UPDATED — RUNTIME UNVERIFIED`

不得把“文档写进去了”说成“行为已经验证通过”。

## 4. Root Cause Before Patch

遇到错误时先回答：**最早在哪一层开始错？**

常见分类：

- 用户信息已经给过，却重复询问 → Interaction / Runtime
- 大纲逻辑错误 → Domain / Orchestration
- 提示词太啰嗦、抽象词污染 → Prompt Compile
- 产品数量或状态漂移 → Domain continuity / Prompt state lock
- 平台下一轮忘记用户回答 → Runtime
- 模型本身无法稳定理解精确数值 → Model capability / Prompt strategy

修最早拥有问题的那一层，不在下游堆补丁。

同一问题连续修三次仍反复出现时，停止追加规则，重新检查架构归属。

## 5. Minimal Change Contract

一次 Skill 迭代尽量只解决一个根因：

- 不做“顺手一起改”。
- 不因局部失败重写无关模块。
- 已经成功的规则默认保护。
- 同一机制会影响多个 Skill 时，优先放到共享治理层或可复用 reference，而不是多处重复长文。
- 可由脚本、schema、lint、结构校验稳定检查的机械规则，优先自动化；Skill 文本保留判断型规则。

## 6. Regression Gate

行为修改至少检查三类案例：

1. **Original Failure**：原问题是否被修复。
2. **Neighbor Case**：正常相邻场景是否被误伤。
3. **Counterexample**：新规则不该触发时，是否能够保持沉默。

对提示词类 Skill 额外检查：

- 是否增加无意义 Prompt 长度；
- 是否把内部管理词直接下发给生成模型；
- 是否重复已有全局规则；
- 是否因为修一个问题降低主体、事件、产品或动作的信息权重。

## 7. Verification Before Completion

任何完成状态都必须先有新鲜证据。

### GitHub 修改

声明“GitHub 已更新”前：

1. 写入目标分支；
2. 重新读取目标文件；
3. 检查新增引用路径真实存在；
4. 检查关键规则确实出现在目标文件；
5. 再报告状态。

### 同步

声明“已同步”前，必须同时可验证源与目标。

- GitHub 已更新但本账号 Skill 无法直接读取 → 只能说 `GITHUB VERIFIED / ACCOUNT SYNC UNVERIFIED`。
- 只看到旧对话、记忆或执行者口头报告 → 不算同步证据。
- GitHub `main` 为 SSOT；不得根据旧记忆反向覆盖 GitHub。

## 8. Operator Output Contract

这是给用户看的**交互层规则**，不是创作 Prompt 模板：

- 明确状态问题：第一句直接回答“是 / 否 / 当前到哪一步”。
- 多步骤任务：用有界编号步骤，避免一个步骤塞多个动作。
- 执行中的任务：明确当前状态和已经完成的具体结果。
- 出错：直接给 `现象 / 原因 / 影响 / 修法`，不加情绪化铺垫。
- 不插入与当前目标无关的旁支建议。
- 工作已经结束时，不用冗余总结和客套收尾。
- 只有仍有未完成工作时，结尾给**一个**最具体的下一步。

**禁止把“下一步、当前进度、验证状态、不要跑题”等治理语言写进 Seedance、生图或其他生成模型提示词。**

## 9. Status Vocabulary

优先使用清晰状态，不使用模糊完成感：

- `VERIFIED`：目标文件/行为已有对应验证证据。
- `UPDATED — RUNTIME UNVERIFIED`：规则已写入，但尚未完成真实行为回归。
- `GITHUB VERIFIED / ACCOUNT SYNC UNVERIFIED`：GitHub 已核验，本账号 Skill 尚无直接同步证据。
- `NOT SYNCED`：源目标明确不一致。
- `BLOCKED`：缺少权限、工具、输入或关键事实，无法继续。

## 10. Repository Maintenance Contract

- GitHub `main` 是 Skill 唯一母版 SSOT。
- 新规则必须有明确归属文件；不要把所有内容继续塞进主 `SKILL.md`。
- 能放 reference 的重内容放 reference，主 Skill 保持路由与强约束。
- 重要行为变化应新增或更新 evaluation / validation case。
- 用户本轮明确要求高于默认规则，但不能篡改已确认事实。
- 外部 Skill 是研究来源，不是上游 SSOT。

最终目标：**让 Skill 越改越稳定、越精炼、越可验证，而不是越改越长。**
