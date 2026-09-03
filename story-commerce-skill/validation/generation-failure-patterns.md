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
- Attempt 2：开盒已改为人物右肩后OTS，人物与镜头从同一工作面观察；首轮“盒子背对人物”的错误未复现。
- Attempt 3：同类开盒镜头继续保持合理操作方向。

ROUTER IMPACT:
Seedance Compiler硬检查；继续跨Case监控。

---

# GF16｜小物体 × 手指精细取放穿模

STATUS: CONFIRMED

TRIGGER CASES:
- Attempt 1：取出/放回均出现手指/产品穿插
- Attempt 2：25–26s收纳阶段仍出现精细接触/状态错误

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
- Attempt 3删除了非必要的“取下→放回仓”复杂收纳动作，全片未再出现明显手指/耳机穿插。由于本次没有重新测试槽位精细放回，**GF16仍保持CONFIRMED，不升级MITIGATED**。

ROUTER IMPACT:
Generation Risk提高；后续用Technical Diagnostic Clip专门复测。

---

# GF17｜Story Driver存在但没有被有效视觉化，剧情变平

STATUS: MITIGATED

TRIGGER CASES:
- Attempt 1
- Attempt 2

SYMPTOMS:
- 文本有Client/Deadline，但观众仍主要看到坐着工作→拿耳机→戴上→继续工作；
- Hook没有形成强继续观看理由；
- 事件存在，却没有与产品卖点形成强因果推进。

MITIGATION:
- `R0 ≠ FLAT`；
- 前1–3秒以可见/可听事件建立Driver；
- Driver必须直接连接真实Pain / Selling Point。

RETEST EVIDENCE:
- Attempt 3使用打印机、推车、办公室交谈声 + 客户提前通知，直接绑定“噪音干扰→主动降噪→专注”。开场Driver已明显可读，首轮问题基本解决。
- Attempt 3中段仍变平，但属于新的`GF23 Post-Proof Plateau`，不再归咎于Hook没有发动。

ROUTER IMPACT:
Hook/Story层继续监控。

---

# GF18｜伪商业问题：把易生成的操作步骤当成卖点

STATUS: MITIGATED

TRIGGER CASES:
- Attempt 1
- Attempt 2

SYMPTOMS:
- 广告核心围绕“拿起→开盒→佩戴→放回”；
- 观众无法判断是在卖降噪、续航、音质、通话、外观还是收纳。

MITIGATION:
- Commercial Validity Gate；
- 每条先锁`Why Buy + Pain/Hesitation + Confirmed Selling Point + Emotional Payoff`；
- 产品操作只能是Proof载体。

RETEST EVIDENCE:
- Attempt 3只表达`Active Noise Cancellation`，以“嘈杂办公室→戴上→声音明显减弱→进入专注”为主因果。核心商业信息已可读。

ROUTER IMPACT:
Story Architecture前硬阻断。

---

# GF19｜把外部压力写成主角负面人格

STATUS: MITIGATED

TRIGGER CASES:
- Attempt 2｜开场助理提醒后，主角“不耐烦/嫌烦”式反应

MITIGATION:
- `TENSION SOURCE ≠ PROTAGONIST NEGATIVITY`；
- 普通商用广告让压力来自环境、任务、Deadline、选择或外部问题；
- 主角默认保持有能力、积极、可喜欢、值得代入。

RETEST EVIDENCE:
- Attempt 3主角面对客户提前与办公室噪音时保持高效、平稳，没有明显嫌烦/丧气人格。

ROUTER IMPACT:
Performance/Dialogue QA。

---

# GF20｜简单微动作时间预算过长，产生“老年感”

STATUS: MITIGATED

TRIGGER CASES:
- Attempt 2｜约11–14s佩戴动作持续过久

MITIGATION:
- 高能广告中简单微动作通常约0.5–1.2s视觉节拍；
- 蓄力时间给事件Cue/视线，动作本身短促；
- 动作匹配硬切，不用慢动作式完整展示。

RETEST EVIDENCE:
- Attempt 3约7–8.5s佩戴节拍明显加快，动作不再拖成“慢慢戴”的老年感。

ROUTER IMPACT:
Camera×Action / Timeline编译。

---

# GF21｜空间声音与听觉因果不成立

STATUS: MITIGATED

TRIGGER CASES:
- Attempt 2｜23–24s远处/画外助理讲话与佩戴耳机状态

MITIGATION:
- 锁speaker位置、on/off-screen、距离、方向、相对音量与房间感；
- 耳机、门、玻璃等改变听觉条件时做Hearing Plausibility Gate；
- 不需要外部人物被主角听见时，改用视觉手势。

RETEST EVIDENCE:
- Attempt 3佩戴耳机后不再安排远处助理直接讲话；助理通过玻璃后的视觉手势交流；ANC前后环境声层级也明显区分。

ROUTER IMPACT:
Seedance Audio/Physical QA。

---

# GF22｜成对物体状态瞬移 / 复制 / Hidden State Teleport

STATUS: CONFIRMED

TRIGGER CASES:
- Attempt 2｜25s两只耳机仍处于佩戴/手持连续状态，26s另一只已无动作地出现在充电仓
- Attempt 3｜27–30s女主仍明显佩戴耳机，但前景打开的充电盒又出现两只耳机，形成“耳朵一对 + 盒内一对”的复制状态

SYMPTOMS:
- 两件相似物体跨镜状态无法追踪；
- 一只在手、一只在耳/盒的位置突然改变；
- 同一对物体在两个位置同时存在；
- 模型用“标准产品Hero Shot”覆盖前面已经建立的真实状态。

ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + CONTINUITY_STATE_GAP + HERO_SHOT_PRIOR

MITIGATION:
- 成对/多件物体使用Object State Ledger；
- 每Beat分别记录L/R或A/B的位置；
- 任一状态改变必须有可见动作或明确动作匹配切；
- **Hero Shot也必须服从Object State Ledger**，不能因为“经典产品图”自动把配件补回盒内；
- 若人物佩戴两只耳机，结尾盒内必须明确为空槽；若模型难稳定生成空槽，则改成闭合盒体Hero Shot，不展示内部。

ROUTER IMPACT:
Physical Continuity硬检查，适用于耳机、鞋、手套、成套配件等。

---

# GF23｜Proof过早完成后的中段平台期 / Post-Proof Plateau

STATUS: CONFIRMED

TRIGGER CASES:
- B1-S04-P1 Attempt 3｜约8.5–10s已经完成“噪音明显减弱 + 主角进入专注”的核心ANC Benefit Expression；约11–23s主要持续为打字、记录、通话与背景助理手势，缺少新的剧情因果变化

SYMPTOMS:
- Hook和卖点都成立，但卖点证明完以后故事像“已经结束却还在继续播放”；
- 中段连续多个镜头只是维持同一状态，例如继续工作、继续使用、继续微笑；
- 观众已经知道产品有效，却没有新的期待、关系变化、选择、阻力、笑点或后果；
- 30秒广告在10秒左右完成核心商业信息，后面变成填时长。

ROOT CAUSE HYPOTHESIS:
STORY_PACING / PROMPT_COMPILER

MITIGATION:
- 增加`POST-PROOF CONTINUATION CHECK`：如果Best Proof在总时长前40–50%已经完成，后续必须至少发生一个与该Benefit直接相关的新因果Beat；
- 合法后续可以是：真实后果、关系变化、轻Surprise、Comedy Payoff、新选择、新目标、再次使用Benefit解决更具体事件；
- **不要求强行R2**。R0仍可通过“Proof→后果→情绪Payoff”保持推进，R1 Surprise也可作为轻量增强；
- 如果没有值得发生的新Beat，优先把广告缩短到15–20秒，而不是用“继续工作/继续使用”填满30秒；
- 后续Beat必须继续服务同一个Selling Point，不能为了热闹突然换第二卖点。

ROUTER IMPACT:
Story Engine / Timeline QA。若跨更多Case复现，再升级为核心Skill硬规则。

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
