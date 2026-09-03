# Story Architecture Router｜剧情架构路由

## 0. 用途

本文件只解决一个问题：

> **已经知道消费者在犹豫什么、广告要证明什么之后，这个商业问题最适合用什么剧情因果骨架表达？**

它位于 `commerce-decision-routing.md` 之后，位于 Reversal / Comedy / Absurdity / Scene DNA 等创意增强模块之前。

禁止在本层重新修改商品事实、重新定义消费者问题、先选Scene再套故事、先想反转再逼商品适配。

核心顺序：

`Commercial Decision → Story Architecture → Proof Plan → Optional Creative Modules → Optional Scene DNA → Story → Video Prompt`

Story Architecture是**因果骨架**，不是Hook、场景、风格、喜剧、荒诞、反转或镜头语言。

每条广告只允许 **1个 Primary Architecture**。其他Architecture最多贡献局部Beat，不得形成多主线。

---

# 1. Router输入

从Commercial Decision Card读取：

1. `PRODUCT`：商品/SKU是什么
2. `AUDIENCE`：谁会买
3. `CORE DECISION QUESTION`：本条最重要的购买问题
4. `TOP HESITATION`：最高权重犹豫
5. `DESIRED OUTCOME`：消费者最终应形成什么判断/行动
6. `BEST PROOF`：最强可用证据
7. `PROOFABILITY`：V1直接可见 / V2过程可见 / V3代理可见 / V4不可由画面直接证明
8. `PRODUCT CAUSAL ROLE`：商品实际上能改变什么
9. `PLATFORM + DURATION`
10. `CONSTRAINTS`：合规、素材、人物、平台、禁止项

最高权重：

`Core Decision Question + Top Hesitation + Best Proof`

品类只提供先验，不能直接决定Architecture。

---

# 2. Gate 0｜Story Eligibility

在选Architecture前先判断剧情是否值得使用。

## 2.1 必须成立

- 有明确购买问题或决策任务；
- 至少有一个可安全表达的真实商品事实/Proof；
- 剧情能让购买问题更清楚，而不是更复杂；
- 商品能在事件中承担因果作用，而不是无意义露出。

## 2.2 EXIT｜Story Not Recommended

以下任一情况成立，可退出剧情路由：

1. 核心卖点只能由V4证据证明，且没有可靠依据；
2. 为了成立剧情必须编造功能、价格、认证、疗效、性能或商品结构；
3. 剧情会明显降低商业信息清晰度；
4. 商品无法参与事件因果，只能在结尾露出；
5. 用户明确要求纯演示、纯品牌或非剧情广告。

返回内部：

`ROUTER RESULT: STORY NOT RECOMMENDED`

并选择安全替代，如事实型、演示型或信息型广告。

EXIT不是SA10，也不是一种Story Architecture。

---

# 3. Story Driver｜先找发动机，再选架构

不要直接在9个名字里凭感觉选。

先判断：

> **什么力量迫使人物必须继续下一步？**

| Driver | 核心问题 | 对应Architecture |
|---|---|---|
| PROBLEM DRIVER | 已发生的现实问题必须解决 | SA01 |
| EVIDENCE DRIVER | 主任务就是验证商品是否成立 | SA02 |
| BELIEF DRIVER | 人物开场已有明确错误判断 | SA03 |
| GOAL DRIVER | 有不可删除的任务/目标/成功条件 | SA04 |
| CHOICE DRIVER | 核心是A还是B/多个真实选择 | SA05 |
| CURIOSITY DRIVER | 不知道异常原因，必须调查 | SA06 |
| SOCIAL DRIVER | 身份/立场/关系冲突推动剧情 | SA07 |
| VALUE DRIVER | 核心是值不值/包含什么/钱花在哪 | SA08 |
| EXPERIENCE DRIVER | 使用体验形成偏好与继续采用 | SA09 |

一个任务可能出现多个Driver候选，但最终只能选1个Primary Driver。

---

# 4. SA01–SA09 Architecture Library

## SA01｜Problem → Solution
**Driver：现实问题**

结构：
`问题已经发生 → 人物尝试处理 → 原方法不足/受阻 → 产品自然介入 → Proof → 问题解除 → Reaction/CTA`

适合：清洁、家居、工具、小家电、收纳、日常痛点。

产品角色：解决问题的必要工具。

硬边界：外部问题本身必须是故事发动机。不能因为任何广告最后都“解决了问题”就归SA01。

Anti-Collapse：删掉现实问题后，故事还能原样启动吗？如果能，SA01是假架构。

复杂度：LOW。

---

## SA02｜Demonstration → Evidence → Decision
**Driver：证据验证**

结构：
`建立验证任务 → 产品操作 → 可见过程 → 可见结果 → 人物验证 → 形成判断`

适合：3C、清洁、厨具、工具、穿戴贴合、收纳、安装类。

产品角色：被验证的对象。

硬边界：**验证行为本身就是剧情**。有Proof不等于SA02。

Anti-Collapse：删掉验证任务后，故事还能原样启动吗？如果能，不是SA02。

复杂度：LOW。

---

## SA03｜Misunderstanding → Verification → Clarification
**Driver：错误判断**

结构：
`明确错误理解 → 根据错误理解行动 → 出现不一致 → 主动验证 → 信息澄清 → 判断改变 → Proof/CTA`

适合：尺寸、容量、兼容、用途、价格理解、套装内容、归属。

硬边界：开场必须已有“明确但错误的答案”。

**SA03 ≠ Reversal Engine。** 普通认知纠正不等于180°反转。

Anti-Collapse：删掉错误判断后，故事还能原样启动吗？如果能，不是SA03。

复杂度：LOW–MEDIUM。

---

## SA04｜Challenge → Attempt → Result
**Driver：任务目标**

结构：
`建立任务/规则 → 明确成功条件 → 开始执行 → 遇到真实阻力 → 产品参与 → 可观察结果 → Outcome`

适合：工具、清洁、安装、3C、大型商品、操作型产品。

硬边界：目标/Deadline/成功条件必须与商业问题相关且不可删除；不能只是给SA01/SA02加一个装饰性计时器。

Anti-Collapse：删掉任务目标后故事仍成立吗？如果能，不是SA04。

复杂度：MEDIUM。

---

## SA05｜Choice → Test → Decision
**Driver：选择**

结构：
`两个或多个真实选择 → 建立判断标准 → 验证关键差异 → Evidence → 排除/保留 → 做出决定`

适合：价格/价值、套装、材质、规格、配件、订阅、功能差异。

硬边界：必须存在真实选择；不得为了让己方商品赢而编造竞品缺点。

Anti-Collapse：删掉选择后故事仍成立吗？如果能，不是SA05。

复杂度：MEDIUM。

---

## SA06｜Discovery → Investigation → Reveal
**Driver：未知/好奇**

结构：
`出现异常结果/对象 → 人物注意 → 调查 → 发现线索 → 找到原因/商品 → Product Proof → 判断改变`

适合：新奇功能、隐藏结构、特殊用途、App/工具、生活便利产品。

硬边界：开场人物**不知道答案**。如果人物已有错误答案，应优先检查SA03。

Anti-Collapse：删掉未知/异常后故事还能启动吗？如果能，不是SA06。

复杂度：MEDIUM–HIGH。

---

## SA07｜Social Conflict → Proof → Relationship Shift
**Driver：社会关系/立场**

结构：
`人物已有身份/观点/权力冲突 → 商品成为争议对象 → 一方质疑/行动 → Proof → 关系/地位/立场变化`

适合：穿搭、礼赠、美妆、生活方式、收藏、审美型消费。

硬边界：Proof之后必须改变人与人的关系/地位/立场，而不只是“大家觉得产品不错”。

Anti-Collapse：删掉社会冲突后只剩普通产品演示吗？如果是，则SA07是假架构。

复杂度：MEDIUM–HIGH。

---

## SA08｜Value Question → Verification → Commitment
**Driver：价值疑虑**

结构：
`怀疑价值/价格/包含内容 → 明确疑点 → 核验真实商业事实 → Proof/Information → 理解价值结构 → 决策`

适合：订阅、服务、套装、补充装、价格优势、Included服务、长期费用结构。

只有核心问题可以改写为 **“我为什么要花这笔钱？”** 时使用。

边界：
- “A还是B？” → SA05
- “这个功能真的假的？” → SA02
- “我之前理解错了” → SA03

不得因为历史RxPros案例多，就泛化到所有商品。

Anti-Collapse：删掉价值疑虑后故事还能原样启动吗？如果能，不是SA08。

复杂度：LOW–MEDIUM。

---

## SA09｜Experience → Preference → Adoption
**Driver：体验偏好**

结构：
`进入真实使用情境 → 自然体验商品 → 动作/环境呈现体验线索 → 形成偏好 → 继续使用/选择/采用`

适合：服装、鞋包、美妆、食品饮料、家居装饰、香氛、生活方式、高颜值商品。

硬边界：可以展示体验，但不得把主观感受伪装成客观科学证明。V3代理线索仍然只是代理线索。

Anti-Collapse：删掉实际体验过程后，人物偏好/购买决定还能自然成立吗？如果能，不是SA09。

复杂度：LOW。

---

# 5. Primary Driver Test｜多个候选时怎么选

不要使用“第一个YES就选”。

当多个Driver同时成立时，问：

> **删掉哪一个驱动力后，故事和商业问题都不能成立？**

优先选择与 `Core Decision Question` 最不可分割的Driver。

例：
“能不能在5分钟内把污渍清干净？”同时有Problem/Evidence/Goal。
- 若5分钟只是装饰，删掉后仍是同一个购买问题 → SA01或SA02；
- 若“短时间完成”本身就是核心卖点/犹豫 → GOAL DRIVER → SA04。

---

# 6. Tie Break｜多Architecture都成立时

按以下顺序裁决：

1. **商业问题匹配度**：谁最直接回答Core Decision Question；
2. **Proof自然度**：谁能让Best Proof自然发生在剧情中；
3. **Product Causality**：谁让商品真正改变事件结果；
4. **Simplicity**：前三项相近时，Beat更少、人物更少、逻辑更短者优先；
5. **Generation Stability**：再相近时，空间/动作/交互更稳定者优先。

公式：

`商业解释力 > Proof自然度 > 产品因果 > 故事简洁 > 生成复杂度`

两个架构商业解释力相近时，不为“更聪明”而选更复杂的那个。

---

# 7. Historical Pattern Penalty｜反模板

历史项目只能提供经验，不能成为默认剧情。

特别禁止：
- Core Decision不是Value/Price时，默认SA08；
- 默认账单、价格震惊、朋友核价、咨询问答；
- 默认“旧方案太贵”；
- 商品有明显强Proof时，仍为了熟悉感强行写社会冲突或价格误会；
- 因RxPros案例多，把所有产品都写成价格型广告。

同批广告还应避免重复相同Primary Architecture、Hook、Reaction路径和道具；但多样性不能覆盖商业匹配度。

---

# 8. Duration与复杂度

时长只调整架构复杂度，不替代商业判断。

## ≤15秒
优先简单清晰：SA01 / SA02 / SA03 / SA09。
SA06 / SA07 / 复杂SA08需压缩或谨慎使用。

## 15–30秒
SA01–SA09均可，根据商业问题选择。

## >30秒
可以允许更完整Investigation、Social Conflict、多级Challenge或创意增强；但不因为时长更长就必须复杂。

复杂度参考：
- LOW：SA01 / SA02 / SA09
- LOW–MEDIUM：SA03 / SA08
- MEDIUM：SA04 / SA05
- MEDIUM–HIGH：SA06 / SA07

---

# 9. Architecture与Creative Modules的关系

Architecture先决定因果骨架，Creative Modules后决定表达增强。

Router只输出兼容度，不自动调用：

`Reversal: LOW / MEDIUM / HIGH`
`Comedy: LOW / MEDIUM / HIGH`
`Escalation: LOW / MEDIUM / HIGH`
`Absurdity: LOW / MEDIUM / HIGH`
`Visual Spectacle: LOW / MEDIUM / HIGH`
`Scene DNA Value: LOW / MEDIUM / HIGH`

重要：
- SA03不是强反转；
- SA06的Reveal不是天然180°反转；
- SA07可以高适配Reversal，但不强制；
- SA02通常低适配Reversal；
- Scene DNA不是任何Architecture的必经步骤。

是否真正调用Reversal/Scene由后续模块根据商业价值、时长、复杂度与生成稳定性决定。

---

# 10. Story Architecture Card｜内部输出

每条只输出一个Primary Architecture Card，不默认展示给普通用户。

模板：

```text
STORY DRIVER:
<Primary Driver>

PRIMARY ARCHITECTURE:
<SAxx｜Name>

CORE DECISION QUESTION:
<本条购买问题>

WHY THIS ARCHITECTURE:
<为什么这条因果骨架最直接>

CORE STORY ENGINE:
<一句话说明什么在推动剧情>

PRODUCT CAUSAL ROLE:
<产品如何改变事件>

PROOF ROLE:
<Proof在故事里承担什么功能>

REQUIRED BEATS:
<最少必要Beat链>

OPTIONAL MODULE COMPATIBILITY:
Reversal: LOW/MEDIUM/HIGH
Comedy: LOW/MEDIUM/HIGH
Escalation: LOW/MEDIUM/HIGH
Absurdity: LOW/MEDIUM/HIGH
Visual Spectacle: LOW/MEDIUM/HIGH
Scene DNA: LOW/MEDIUM/HIGH

COMPLEXITY:
LOW / LOW–MEDIUM / MEDIUM / MEDIUM–HIGH

PRIMARY RISK:
<最可能发生的架构塌缩>

DO NOT:
<禁止偷换成的其他架构/套路>
```

---

# 11. Anti-Collapse Test｜架构防塌缩

Story Architecture Card建立后必须静默检查：

> **把当前核心Driver删除，故事还能原样继续吗？**

如果YES，当前Architecture是假架构，重选。

对应测试：
- SA01：删现实问题
- SA02：删验证任务
- SA03：删错误判断
- SA04：删目标/成功条件
- SA05：删选择
- SA06：删未知/异常
- SA07：删社会立场冲突
- SA08：删价值疑虑
- SA09：删体验过程

同时检查：
- Product Entry是否自然；
- Best Proof是否没有被剧情挤到旁支；
- Proof后是否真的改变人物判断/行动；
- 是否存在更简单的Architecture完成同一商业任务。

---

# 12. Router完整执行流程

```text
STEP 0 读取Commercial Decision Card
↓
STEP 1 Story Eligibility Gate
  失败 → EXIT
↓
STEP 2 识别可能Story Drivers
↓
STEP 3 Primary Driver Test
↓
STEP 4 映射SA01–SA09候选
↓
STEP 5 Tie Break
  商业匹配 → Proof自然 → 产品因果 → 简单 → 生成稳定
↓
STEP 6 只选1个Primary Architecture
↓
STEP 7 Anti-Collapse Test
  失败 → 重选
↓
STEP 8 输出Story Architecture Card
↓
交给Proof Plan / Optional Creative Modules / Optional Scene Router
```

---

# 13. 最终原则

- **简单是合法且经常更优的答案。**
- Architecture由购买问题决定，不由品类名决定。
- Proof先于反转、荒诞、喜剧和Scene奇观。
- Reversal是可选增强，不是默认骨架。
- Scene DNA是可选世界增强，不是所有剧情的必经步骤。
- 如果不适合剧情，允许EXIT，不为了证明Skill“会创意”而硬编。
