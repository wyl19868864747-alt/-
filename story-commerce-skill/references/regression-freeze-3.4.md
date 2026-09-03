# REGRESSION FREEZE 3.4｜剧情带货商用重构最终回归基线

> 本文件记录3.4冻结前的**规则层/结构层回归结果**。
>
> 它不是Seedance实际生成验证报告。Scene真实生成稳定性仍以 `scene-validation-registry.md` 为准。

---

# 1. 冻结版本

`story-commerce-skill/SKILL.md = 3.4 COMMERCIAL FREEZE`

核心链：

`Commercial Decision`
→ `Story Architecture`
→ `Proof Plan`
→ `Reversal Router R0/R1/R2`
→ `Optional Creative Modules`
→ `Scene Router: NORMAL_LOCATION vs S01–S12`
→ `Story`
→ `Performance/FACS`
→ `Seedance Compiler`
→ `Silent QA`

冻结原则：下游只能编译/增强上游，不得反向改写商品事实、Primary Driver、Best Proof或已确定R-level。

---

# 2. Story Architecture回归

确认：

- SA01 Problem → Solution
- SA02 Demonstration → Evidence → Decision
- SA03 Misunderstanding → Verification → Clarification
- SA04 Challenge → Attempt → Result
- SA05 Choice → Test → Decision
- SA06 Discovery → Investigation → Reveal
- SA07 Social Conflict → Proof → Relationship Shift
- SA08 Value Question → Verification → Commitment
- SA09 Experience → Preference → Adoption
- EXIT Story Not Recommended

回归结论：

- 每条只允许1个Primary Architecture；
- Primary Driver优先于表面剧情形式；
- SA03不自动等于R2；
- SA06 Reveal不自动等于R2；
- Scene、Comedy、Absurdity、FACS都不能偷换Primary Driver。

结果：`PASS`

---

# 3. Reversal Router回归

冻结：

- R0 = NO REVERSAL，默认且完全合格
- R1 = Clarification / Reveal / Surprise
- R2 = TRUE REVERSAL，仅通过完整Gate时使用

九Architecture压力测试分布符合预期：

- SA01：R0为主
- SA02：R0为主
- SA03：R1为主
- SA04：R0 / 少量R1
- SA05：R0 / R1
- SA06：R1为主
- SA07：R2高潜力但非默认
- SA08：R1为主，R2谨慎
- SA09：R0为主

确认：

- Compatibility ≠ Necessity
- Architecture Integrity Test有效
- Commercial Double-Duty有效
- Temporary Misbelief Risk对医疗/安全/金融/价格/资格等提高门槛
- Value Delta / Removal Test允许R2→R1→R0降级

结果：`PASS`

---

# 4. Scene Router 12+1回归

候选池：

`NORMAL_LOCATION + S01–S12`

## 4.1 12个特殊Scene正向命中

| Scene | 代表性商业问题 | 结果 |
|---|---|---|
| S01 宫廷 | 资格/身份/公开权力判断 | PASS |
| S02 高中 | 安全普通商品的同伴公开判断 | PASS |
| S03 军营 | Deadline + Command + Supply任务 | PASS |
| S04 办公室 | 工作结果/兼容/客户Deadline | PASS |
| S05 西部 | 公开实用测试改变信誉 | PASS |
| S06 Gala | 品味/礼赠/社交认可 | PASS |
| S07 Mall | 并列试用/比较/改选 | PASS |
| S08 Future | 分类/兼容/系统错误/人工Override | PASS |
| S09 Diner | 偷听/插话/信息横向传播 | PASS |
| S10 Competition | 公平、短时、可见结果挑战 | PASS |
| S11 Market | Public Claim/Rival/Crowd价值判断 | PASS |
| S12 Train | 移动/便携/归属/车厢路径 | PASS |

## 4.2 NORMAL_LOCATION负向控制

以下测试均应拒绝特殊Scene：

1. USB-C配件单纯兼容Proof → NORMAL_LOCATION `PASS`
2. 女装日常舒服/百搭体验 → NORMAL_LOCATION `PASS`
3. 小家电拆洗步骤 → NORMAL_LOCATION `PASS`
4. 订阅服务真实包含内容/价格解释 → NORMAL_LOCATION `PASS`
5. 成人医疗服务价格信息 → NORMAL_LOCATION `PASS`
6. 大沙发是否通过家门 → NORMAL_LOCATION `PASS`

结论：高视觉Scene没有在规则层劫持商业匹配。

## 4.3 同商品不同购买问题

测试夹具：同一钛杯。

- 漏不漏 → 普通真实使用/Proof
- 旅行拿取是否方便 → S12可胜
- 作为礼物是否体面 → S06可胜
- 谁有资格获得 → S01可胜
- 两个版本选哪个 → S07可胜

结论：Scene由`本条购买问题 + Architecture + Proof`决定，不由商品类别单独决定。

结果：`PASS`

---

# 5. Scene 选择冻结逻辑

禁止机械等权总分。

顺序：

## HARD GATES
Safety / Product Truth / Proofability / DNA Activation

## PRIMARY COMMERCIAL FIT
Decision / Architecture / Proof / Product Entry

## UNIQUE CAUSAL GAIN
特殊Scene必须说明其不可替代因果优势。

## SECONDARY EXECUTION FIT
Character / Reaction Signature / Generation Risk / Native Conflict

## TIE BREAK ONLY
Visual Distinctiveness / Diversity / Camera novelty

冻结结论：

> Visual不能用来补偿商业不匹配；特殊Scene净收益不明确时NORMAL_LOCATION胜。

---

# 6. Performance / FACS回归

确认表演层权限：

`Story Beat`
→ `Trigger`
→ `Gaze Target`
→ `Performance Intent`
→ `最少必要Facial Change`
→ `Body / New Action`

规则：

- Event > Performance Decoration
- 事件先发生，表情后发生
- FACS只作可见动作词典，不作为唯一情绪真值表
- 最终Seedance默认不输出AU编号
- R0不能被表演偷偷变成反转
- R1不能演成R2
- R2在Micro Anomaly前不能提前泄底
- 大全景不塞精细眉眼
- Decision Change最终必须落到动作
- 多人Reaction必须有先后，不同步“集体震惊”

结果：`PASS`

---

# 7. 全链路跨品类结构回归

以下均为结构测试夹具，不代表真实商品声明。

| 类型 | Core问题 | Architecture | R-level | Scene Mode | 结果 |
|---|---|---|---|---|---|
| 清洁用品 | 能否直接清掉可见污渍 | SA02 | R0 | NORMAL | PASS |
| 女装 | 两件实际试穿选哪件 | SA05 | R0/R1 | S07或NORMAL按任务 | PASS |
| 礼赠珠宝 | 社会关系/赠送对象改变 | SA07 | R2候选 | S01/S06按问题 | PASS |
| 旅行用品 | 移动中是否方便取用 | SA09 | R0 | S12可胜 | PASS |
| 3C配件 | 是否真实兼容 | SA02 | R0 | NORMAL；有Deadline才S04候选 | PASS |
| 新奇厨房工具 | 结果来源是什么 | SA06 | R1 Reveal | NORMAL；信息传播时S09候选 | PASS |
| 订阅/服务 | 为什么值这笔钱 | SA08 | R1 Clarification | NORMAL为主 | PASS |
| 成人医疗价格信息 | 真实价格/包含内容 | SA08 | R0/R1 | NORMAL | PASS |

结论：同一套系统可让简单广告保持简单，也允许真正需要时调用R2与特殊Scene。

---

# 8. 旧规则残留清理

本轮已处理：

- Scene Router不再使用“选Scene→错误预判→双证据→Scene反转”旧链；
- Scene DNA Card里的`反转`改为`反转兼容（仅R2）`语义；
- Scene Card人物池不再代表固定人数要求；
- S01/S02/S10/S11等旧固定人物数量锁定已改为最低必要人物原则；
- Scene节奏DNA中可能出现的误判/反转，仅在上游Architecture/R-level允许时调用；
- NORMAL_LOCATION正式成为Candidate 0；
- Visual Distinctiveness降为Tie Break；
- Reaction Signature正式参与Scene差异化与Performance调制。

结果：`PASS`

---

# 9. 尚未被本次结构回归证明的项目

以下不得因3.4冻结而声称完成：

- Seedance实际跨商品生成稳定性
- Scene Recognition真实生成PASS
- PRODUCT LOCK真实跨镜稳定
- Space Continuity真实生成PASS
- 多人/Handoff真实穿模率
- Scene-specific Reaction真实执行率

因此当前12个Scene继续全部：

`TESTING_CANDIDATE`

不得升级为`VALIDATED`。

---

# 10. Freeze结论

`3.4 COMMERCIAL FREEZE = STRUCTURAL / ROUTING BASELINE PASS`

以后新增：
- 第13/20/50个Scene
- 新Creative Module
- 新品类先验
- Seedance真实验证结果
- 新FACS/Performance模板

都应作为增量更新。

不得重新引入以下旧错误：

- 每条强制反转
- Scene先于Story Architecture
- 视觉奇观覆盖Proof
- RxPros历史套路成为默认
- 两人聊天→举产品→震惊→CTA
- “荒诞升级/更抓马/震惊”等抽象词直接投视频模型
- 人物/商品/空间无物理因果
- Scene漂亮但对购买问题没有独特因果增益
