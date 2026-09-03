# GENERATION FAILURE PATTERNS｜Seedance真实失败模式库

> 目的：把“这条视频坏了”升级成“我们知道为什么坏、以后什么时候应该提前避开”。

只有真实生成中观察到的Failure Pattern才能升级为 `CONFIRMED`。

状态：
- `WATCHLIST`：理论/历史经验高风险，等待Benchmark验证
- `CONFIRMED`：真实Case重复出现或证据明确
- `MITIGATED`：已有规避方法且复测解决目标问题
- `MODEL_LIMIT`：当前模型能力边界，Router应主动规避
- `RETIRED`：新模型/新流程下已不再构成稳定风险

---

# GF01｜多人递物 / Handoff穿模
STATUS: WATCHLIST
症状：双手与产品重叠、产品跳手、尺度变化、手从不合理位置进入。
初始规避：最低必要人物；拆“递出→独立接手镜”；锁起点/终点；避免复杂双手交叉。
高风险Scene：S01 / S06 / S09 / S12

---

# GF02｜远距离人物的手突然进入近景
STATUS: WATCHLIST
症状：人物上一镜离产品很远，下一特写出现无来源的手直接拿产品。
初始规避：先写靠近/伸手；产品特写前建立接触；不用“远处人物+独立手部特写”硬接。

---

# GF03｜玻璃门 / 门框 / 狭窄空间穿模
STATUS: WATCHLIST
症状：人穿关闭玻璃门、手穿门框、开门方向跨镜改变。
高风险Scene：S04 / S12
初始规避：锁门侧/站位/方向；门动作单独成Beat；开门时不同时拿复杂商品。

---

# GF04｜产品尺度漂移
STATUS: WATCHLIST
症状：手持变大/变小、桌面到特写比例变化、包装/本体关系失真。
初始规避：PRODUCT LOCK含相对尺度；手掌/桌面/人体作参照；避免无参照极端特写直接切大全景。

---

# GF05｜屏幕 / LED / 包装文字乱码
STATUS: WATCHLIST
症状：屏幕、价格、包装、LED乱码或错误信息。
高风险Scene：S04 / S08 / S10 / S07
初始规避：非必要文字不做关键Proof；物理状态优先；精确文字使用真实资产/后期。

---

# GF06｜多人同步转头 / 同步震惊
STATUS: WATCHLIST
症状：所有人物同一帧同步看商品、同步瞪眼/张嘴。
高风险Scene：S02 / S06 / S07 / S09 / S11
初始规避：锁First Observer；第二人顺视线发现；Reaction用传播，不同时触发。

---

# GF07｜R2提前泄底
STATUS: WATCHLIST
症状：Micro Anomaly前演员已露出知道真相的表情/动作。
初始规避：Evidence阶段保持旧判断；Micro Anomaly后才允许停顿/视线变化；Reveal后再认知重置。

---

# GF08｜连续动作顺序错乱
STATUS: WATCHLIST
症状：结果先于原因、商品先打开再伸手、先反应后看见等。
初始规避：`人先动作→接触→物体响应→结果`；一段一个主要动作；复杂操作拆镜。

---

# GF09｜狭窄空间左右/方向漂移
STATUS: WATCHLIST
症状：窗/门侧互换、走廊方向反转、人物从错误门出现。
高风险Scene：S12，次高S04
初始规避：Continuity Anchors；固定window_side/door_side/corridor_direction；减少无动机反打。

---

# GF10｜现代商品被古代化 / 未来化
STATUS: WATCHLIST
症状：现代产品变铜木复古、未来Scene让商品发光/透明/加AI。
高风险Scene：S01 / S03 / S05 / S08 / S11 / S12
初始规避：Reference最高优先；现代SKU保持原貌；`WORLD TECH ≠ PRODUCT FACT`。

---

# GF11｜Proof被剧情/Reaction抢掉
STATUS: WATCHLIST
症状：观众记得角色热闹，却没看清产品到底证明什么。
初始规避：Proof先锁时间；Proof镜头稳定；Reaction在Proof后；复杂度不足先降创意模块。

---

# GF12｜Scene只剩背景，没有DNA
STATUS: WATCHLIST
症状：背景是宫廷/办公室/列车，但动作、冲突、入口、Reaction换客厅也成立。
初始规避：DNA Activation；Unique Causal Gain；无增益回NORMAL_LOCATION。

---

# GF13｜表情过满导致人物失真
STATUS: WATCHLIST
症状：连续瞪眼、张嘴、翻白眼、过多眉眼变化，脸部身份漂移。
初始规避：短Beat只留1视线+1–2主要面部变化；复杂动作优先删表情；大全景不写细眉眼。

---

# GF14｜多人身份/服装漂移
STATUS: WATCHLIST
症状：A/B互换服装/脸，群体角色跨镜混乱。
初始规避：最低必要人物；主要人物位置/衣着锚点；背景不承担关键剧情。

---

# GF15｜Proof镜头与人物操作面冲突

STATUS: MITIGATED

TRIGGER CASES:
- B1-S04-P1 Attempt 1｜AirPods Pro 2 × Office × Seedance 2.5 × 30s

SYMPTOMS:
- 为让观众正面看清盒内，模型把工作面朝镜头，人物面对盒盖背面。

ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + SKILL_RULE_GAP

MITIGATION:
- 执行 `references/camera-action-compiler.md`；
- 先锁人物操作面，再锁机位；
- 开盒/内部结构优先人物肩后OTS / 操作侧斜后方；
- 当前机位不能兼顾操作与Proof时主动切镜。

RETEST EVIDENCE:
- B1-S04-P1 Attempt 2：开盒已改为人物右肩后OTS，人物与镜头从同一工作面观察；首轮“盒子背对人物”的错误未复现。

ROUTER IMPACT:
Seedance Compiler硬检查；继续跨Case监控，但目标问题已被本次复测修正。

---

# GF16｜小物体 × 手指精细取放穿模

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 1：取出/放回均出现手指/产品穿插
- B1-S04-P1 Attempt 2：25–26s收纳阶段仍出现精细接触/状态错误

SYMPTOMS:
- 手指进入小物体或槽位几何内部；
- 抓取/放回边界模糊；
- 成对小物体在收纳时发生不连续状态。

ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + MODEL_HIGH_RISK_INTERACTION

HIGH-RISK CONDITIONS:
耳机/耳饰/小配件、紧槽取放、手持盒体同时抓取、多项厘米级接触。

MITIGATION:
- 一镜最多1项高风险接触；
- 产品稳定支撑；
- 明确抓取部位和单一运动方向；
- 非核心Proof允许动作匹配切镜；
- 成对物体增加Object State Ledger。

RETEST EVIDENCE:
Attempt 2仍失败，因此**不能标MITIGATED**。

ROUTER IMPACT:
Generation Risk提高；若后续在更简化方案仍复现，考虑标记MODEL_LIMIT。

---

# GF17｜Story Driver存在但没有被有效视觉化，剧情变平

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 1
- B1-S04-P1 Attempt 2

SYMPTOMS:
- 文本有Client/Deadline，但观众仍主要看到坐着工作→拿耳机→戴上→继续工作；
- Hook没有形成强继续观看理由；
- 事件存在，却没有与产品卖点形成强因果推进。

ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + BENCHMARK_DESIGN

MITIGATION:
- `R0 ≠ FLAT`；
- 前1–3秒必须以可见/可听事件建立Driver；
- Driver必须直接连接真实Pain / Selling Point，而不是只制造“有人来催”。

RETEST EVIDENCE:
Attempt 2强化“提前客户”后仍然偏平，说明仅增加Deadline不足；必须回到Commercial Decision重做。

ROUTER IMPACT:
Hook/Story层硬检查，不等于升级R1/R2。

---

# GF18｜伪商业问题：把易生成的操作步骤当成卖点

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 1
- B1-S04-P1 Attempt 2

SYMPTOMS:
- 广告核心围绕“拿起→开盒→佩戴→放回”；
- 观众无法判断是在卖降噪、续航、音质、通话、外观还是收纳；
- 产品操作很多，但没有一个真实Why Buy被清楚表达。

ROOT CAUSE HYPOTHESIS:
BENCHMARK_DESIGN + SKILL_RULE_GAP

MITIGATION:
- 新增Commercial Validity Gate；
- 每条先锁`Why Buy + Pain/Hesitation + Confirmed Selling Point + Emotional Payoff`；
- 产品操作只能是Proof载体，不能因“好拍”自动升级为Core Decision；
- 纯物理稳定性测试改名`TECHNICAL DIAGNOSTIC CLIP`，与剧情带货Benchmark分开。

ROUTER IMPACT:
必须在Story Architecture之前阻断；Gate失败时禁止继续镜头层修补。

---

# GF19｜把外部压力写成主角负面人格

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 2｜开场助理提醒后，主角“不耐烦/嫌烦”式反应

SYMPTOMS:
- 本应是“工作事件紧迫”，却让主角显得对同事不耐烦；
- 正常消费广告的代入感与愉悦感下降；
- 张力来自人物让人不舒服，而不是事件本身。

ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER

MITIGATION:
- `TENSION SOURCE ≠ PROTAGONIST NEGATIVITY`；
- 普通商用广告让压力来自环境、任务、Deadline、选择或外部问题；
- 主角默认保持有能力、积极、可喜欢、值得代入；
- 只有用户明确要荒诞/黑色/抓马/反转时才允许负面人格成为戏剧资产。

ROUTER IMPACT:
Performance/Dialogue QA。

---

# GF20｜简单微动作时间预算过长，产生“老年感”

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 2｜约11–14s佩戴动作持续过久

SYMPTOMS:
- 简单抬手/佩戴被慢慢演满整个时间段；
- 节奏拖沓、缺乏年轻利落与蓄力后的爆发感；
- 观众知道下一步是什么却必须等动作完成。

ROOT CAUSE HYPOTHESIS:
PROMPT_TIMING / COMPILER

MITIGATION:
- 高能广告中简单微动作通常按约0.5–1.2s视觉节拍设计；
- 需要蓄力时，把时间给前置事件/声音Cue/视线锁定，动作本身短促；
- 使用动作匹配硬切，不用慢动作式完整展示换稳定。

ROUTER IMPACT:
Camera×Action / Timeline编译。

---

# GF21｜空间声音与听觉因果不成立

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 2｜23–24s远处/画外助理讲话与佩戴耳机状态

SYMPTOMS:
- 画外人物虽视觉上有距离，声音缺少明确方向/房间空间感，主观上像贴近镜头说话；
- 主角仍佩戴耳机，却自然、清晰地响应外部讲话，没有建立可听原因；
- 声音逻辑和视觉空间脱节。

ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + AUDIO_SPATIAL_RULE_GAP

MITIGATION:
- 每句对白锁speaker位置、on/off-screen、距离、方向、相对音量与房间感；
- 耳机、门、玻璃等改变听觉条件时，先做Hearing Plausibility Gate；
- 若依赖Transparency / Conversation Awareness等产品功能，明确真实功能与触发条件；否则先摘耳机/视觉交流/不响应。

ROUTER IMPACT:
Seedance Audio/Physical QA。

---

# GF22｜成对物体状态瞬移 / Hidden State Teleport

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 2｜25s两只耳机仍处于佩戴/手持连续状态，26s另一只已无动作地出现在充电仓

SYMPTOMS:
- 两件相似物体跨镜状态无法追踪；
- 一只在手、一只在耳/盒的位置突然改变；
- 模型用“看起来像收纳完成”替代真实状态过渡。

ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + CONTINUITY_STATE_GAP

MITIGATION:
- 成对/多件物体使用Object State Ledger；
- 每Beat分别记录L/R或A/B的位置；
- 任一状态改变必须有可见动作或明确动作匹配切；
- 非核心收纳过程可以直接切到“全部收好”的结果镜，但前一镜不得保留矛盾状态。

ROUTER IMPACT:
Physical Continuity硬检查，适用于耳机、鞋、手套、成套配件等。

---

# 新Failure Pattern登记模板

```text
# GFxx｜名称
STATUS: WATCHLIST / CONFIRMED / MITIGATED / MODEL_LIMIT / RETIRED
TRIGGER CASES:
SYMPTOMS:
ROOT CAUSE HYPOTHESIS:
SKILL_RULE / PROMPT_COMPILER / MODEL_LIMIT / RANDOM_GENERATION / PRODUCT_ASSET_LIMIT
HIGH-RISK CONDITIONS:
HIGH-RISK SCENES:
MITIGATION:
RETEST EVIDENCE:
ROUTER IMPACT:
```

---

# 规则

- 单次偶发失败不自动升级CONFIRMED；但Prompt因果明显、同一Case内重复、或状态逻辑可直接验证的问题可以CONFIRMED。
- 同类问题跨2个以上Case复现，优先视为系统性风险。
- 简化后仍稳定失败，应考虑MODEL_LIMIT，不无限加Prompt。
- CONFIRMED问题复测解决目标问题后可升级MITIGATED，但继续跨Case监控。
- Failure Pattern用于未来Router/Compiler提前避错，不是让Prompt越来越长。
