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
TRIGGER CASES: Attempt 1
MITIGATION:
- 先锁人物操作面，再锁机位；
- 开盒/内部结构优先人物肩后OTS / 操作侧斜后方；
- 当前机位不能兼顾操作与Proof时主动切镜。
RETEST EVIDENCE:
- Attempt 2–4同类开盒镜头未再复现“盒内朝镜头、人物面对盒背面”。

---

# GF16｜小物体 × 手指精细取放穿模
STATUS: CONFIRMED
TRIGGER CASES: Attempt 1 / Attempt 2
SYMPTOMS:
- 手指进入小物体或槽位几何内部；
- 抓取/放回边界模糊；
- 成对小物体在收纳时状态不连续。
MITIGATION:
- 一镜最多1项高风险接触；
- 产品稳定支撑；
- 明确抓取部位/单一方向；
- 非核心Proof允许动作匹配切镜；
- 成对物体使用Object State Ledger。
RETEST EVIDENCE:
- Attempt 3–4删除复杂收纳后没有明显槽位穿模，但尚未专门复测精细放回，因此保持CONFIRMED。

---

# GF17｜Story Driver存在但没有被有效视觉化，剧情变平
STATUS: MITIGATED
TRIGGER CASES: Attempt 1 / Attempt 2
MITIGATION:
- 前1–3秒以可见/可听事件建立Driver；
- Driver直接连接真实Pain / Selling Point。
RETEST EVIDENCE:
- Attempt 3之后“办公室噪音→ANC→专注”Driver清楚成立。

---

# GF18｜伪商业问题：把易生成的操作步骤当成卖点
STATUS: MITIGATED
TRIGGER CASES: Attempt 1 / Attempt 2
MITIGATION:
- Commercial Validity Gate；
- 先锁Why Buy + Pain/Hesitation + Confirmed Selling Point + Emotional Payoff；
- 产品操作只能是Proof载体。
RETEST EVIDENCE:
- Attempt 3–4只表达Active Noise Cancellation，商业信息可读。

---

# GF19｜把外部压力写成主角负面人格
STATUS: MITIGATED
TRIGGER CASES: Attempt 2
MITIGATION:
- `TENSION SOURCE ≠ PROTAGONIST NEGATIVITY`；
- 普通商用广告压力来自环境/任务/时间/关系，主角保持可喜欢、可代入。
RETEST EVIDENCE:
- Attempt 3–4未复现不耐烦主角。

---

# GF20｜简单微动作时间预算过长，产生“老年感”
STATUS: MITIGATED
TRIGGER CASES: Attempt 2
MITIGATION:
- 简单微动作约0.5–1.2s视觉节拍；
- 蓄力给事件Cue/视线，动作本身短促；
- 动作匹配硬切。
RETEST EVIDENCE:
- Attempt 3–4佩戴节拍明显改善。

---

# GF21｜空间声音与听觉因果不成立
STATUS: MITIGATED
TRIGGER CASES: Attempt 2
MITIGATION:
- 锁speaker位置、距离、方向、房间感；
- 耳机/门/玻璃改变听觉条件时执行Hearing Plausibility Gate；
- 不需要听见时改视觉手势。
RETEST EVIDENCE:
- Attempt 3–4未复现远处助理贴脸对白/戴耳机仍直接回应。

---

# GF22｜成对物体状态瞬移 / 复制 / Hidden State Teleport
STATUS: CONFIRMED
TRIGGER CASES:
- Attempt 2：一只耳机无动作进入充电仓
- Attempt 3：女主耳朵一对 + 打开盒内又一对
SYMPTOMS:
- 相似物体跨镜状态无法追踪；
- 同一对物体在两个位置同时存在；
- 标准Hero Shot覆盖真实状态。
MITIGATION:
- Object State Ledger逐只追踪；
- Hero Shot同样服从Ledger；
- 人物仍佩戴耳机时，优先闭合盒体，不展示内部。
RETEST EVIDENCE:
- Attempt 4结尾使用闭合盒体，两次生成均未复现“耳朵+盒内重复一对”；但仍需跨Case复测后再考虑MITIGATED。

---

# GF23｜Proof过早完成后的中段平台期 / Post-Proof Plateau
STATUS: CONFIRMED
TRIGGER CASES:
- Attempt 3：约10s卖点已完成，11–23s维持“继续专注”
- Attempt 4 Run A/B：加入更多背景事件后仍在10–21s形成长平台期
SYMPTOMS:
- Hook和卖点成立，但卖点证明后故事像“已经结束却继续播放”；
- 继续工作/继续使用/背景路人事件占据时长；
- 观众知道产品有效，却没有新的高价值商业变化。
ROOT CAUSE HYPOTHESIS:
STORY_PACING / PROMPT_COMPILER
MITIGATION:
- Proof在前40–50%完成时，后续必须有与同一Benefit直接相关的新因果Beat；
- **Attempt 4新增教训：新Beat不能只是背景发生。必须改变主角动作、判断、产品状态或观众对Benefit的理解。**
- 后续优先短促的Outcome / Contrast / Surprise / Comedy / Decision Change；
- 没有高价值新Beat则缩短，不用自然主义场面填时长。
ROUTER IMPACT:
Story Engine / Timeline QA。

---

# GF24｜亚秒多镜头插值 / False Hard Cut Morph
STATUS: CONFIRMED
TRIGGER CASES:
- B1-S04-P1 Attempt 4 Run A
- B1-S04-P1 Attempt 4 Run B
SYMPTOMS:
- 提示词要求0–3s多个0.7s左右独立噪音镜头，但模型没有稳定执行真正Hard Cut；
- Run B约0.5–1.1s最明显，打印机/办公设备/移动物体横向模糊穿过画面，像不同空间被模型连续插值；
- Run A较轻，但打印机→推车→人物/助理的空间重置仍有“突然出现/跳位”感；
- 快节奏被错误表现成物体乱穿，而不是清楚剪辑。
ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + MODEL_TEMPORAL_INTERPOLATION_RISK
HIGH-RISK CONDITIONS:
- 同一个生成片段内连续多个<1s独立物理场景
- 每个微镜头都有大物体移动/空间重置
- 硬切边界缺少稳定首尾状态
- 1–2秒内同时要求门、人物移动、对白、物体运动
MITIGATION:
- **快节奏优先靠信息密度和声音层，不靠3–4个亚秒独立物理场景。**
- Hook优先`1个强主镜头 + 同画面多噪音源/背景动作 + 声音叠加`；
- 若必须切，尽量让独立镜头≥1.0–1.5s，减少空间重置次数；
- 首镜需要人物互动时，让关键人物从首帧已经处于可执行位置，不在1秒内完成走门→靠近→说话；
- 快切可用于稳定特写/Reaction/产品状态，不让大空间和大物体每0.7s重新生成。
ROUTER IMPACT:
Hook Compiler / Seedance Temporal QA。

---

# GF25｜商业Beat密度塌陷 / TV Drama Drift
STATUS: CONFIRMED
TRIGGER CASES:
- B1-S04-P1 Attempt 4 Run A
- B1-S04-P1 Attempt 4 Run B
SYMPTOMS:
- Prompt为了“继续剧情”加入掉文件、打印机、通话、会议结束等完整生活事件；
- 两次生成约10–21s都长时间使用相似女主中近景打字/说话，观感像电视剧办公室戏；
- 背景事件虽多，但没有快速改变主角目标、产品状态、商业判断；
- Surprise/Nope直到20秒以后才到，核心有趣Beat太迟；
- “故事更完整”反而让短视频广告的抓力下降。
ROOT CAUSE HYPOTHESIS:
STORY_CONTINUATION_OVERCORRECTION + PROMPT_COMPILER
MITIGATION:
- 新增`COMMERCIAL BEAT DENSITY GATE`：短视频广告通常每2–3秒至少出现一个新商业Beat：新信息 / 新动作 / 新产品状态 / 新反差 / 新Reaction / 新Payoff；
- Beat不是“每2秒换背景”，而是观众理解或期待发生变化；
- 单一自然主义行为（打字、听、说、走路）若超过约3秒且没有新商业信息，优先压缩；
- Post-Proof Surprise/Comedy优先在Proof后2–4秒内到达，不拖到20秒以后；
- **Audio Calm ≠ Visual Slow**：产品让声音安静，不代表摄影/信息节奏也要慢；
- 背景事件只有在直接支持Contrast时才保留，并压成0.5–1.5s可读视觉证据，不单独演完整小剧情；
- 30秒如果没有足够高价值Beat，缩短优于电视剧式填时长。
ROUTER IMPACT:
Story Engine / Timeline / Ad Pacing QA。

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
- 同一Prompt连续2次复现相近结构问题，可作为强系统证据，但仍要跨产品/Scene继续监控。
- 简化后仍稳定失败，应考虑MODEL_LIMIT，不无限加Prompt。
- CONFIRMED问题复测解决目标问题后可升级MITIGATED，但继续跨Case监控。
- Failure Pattern用于未来Router/Compiler提前避错，不是让Prompt越来越长。
