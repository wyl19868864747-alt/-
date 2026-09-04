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

# GF02｜远距离人物的手突然进入近景
STATUS: WATCHLIST
症状：人物上一镜离产品很远，下一特写出现无来源的手直接拿产品。
初始规避：先写靠近/伸手；产品特写前建立接触。

# GF03｜玻璃门 / 门框 / 狭窄空间穿模
STATUS: WATCHLIST
高风险Scene：S04 / S12
初始规避：锁门侧/站位/方向；门动作单独成Beat。

# GF04｜产品尺度漂移
STATUS: WATCHLIST
初始规避：相对尺度 + 手掌/桌面/人体参照。

# GF05｜屏幕 / LED / 包装文字乱码
STATUS: WATCHLIST
初始规避：非必要文字不做关键Proof；精确文字用真实资产/后期。

# GF06｜多人同步转头 / 同步震惊
STATUS: WATCHLIST
初始规避：锁First Observer；Reaction分先后传播。

# GF07｜R2提前泄底
STATUS: WATCHLIST
初始规避：Micro Anomaly前保持旧判断。

# GF08｜连续动作顺序错乱
STATUS: WATCHLIST
初始规避：`人先动作→接触→物体响应→结果`。

# GF09｜狭窄空间左右/方向漂移
STATUS: WATCHLIST
高风险Scene：S12 / S04
初始规避：Continuity Anchors。

# GF10｜现代商品被古代化 / 未来化
STATUS: WATCHLIST
初始规避：Reference最高优先；`WORLD TECH ≠ PRODUCT FACT`。

# GF11｜Proof被剧情/Reaction抢掉
STATUS: WATCHLIST
初始规避：Proof先锁时间；Reaction在Proof后。

# GF12｜Scene只剩背景，没有DNA
STATUS: WATCHLIST
初始规避：DNA Activation + Unique Causal Gain。

# GF13｜表情过满导致人物失真
STATUS: WATCHLIST
初始规避：短Beat只留1视线+1–2主要面部变化。

# GF14｜多人身份/服装漂移
STATUS: WATCHLIST
初始规避：最低必要人物 + 衣着/位置锚点。

---

# GF15｜Proof镜头与人物操作面冲突
STATUS: MITIGATED
TRIGGER CASES: Attempt 1
MITIGATION:
- 先锁人物操作面，再锁机位；
- 开盒/内部结构优先同侧OTS；
- 机位不能兼顾操作与Proof时主动切镜。
RETEST EVIDENCE:
- Attempt 2–5未再复现“盒内朝镜头、人物面对盒背面”。

# GF16｜小物体 × 手指精细取放穿模
STATUS: CONFIRMED
TRIGGER CASES: Attempt 1 / Attempt 2
MITIGATION:
- 一镜最多1项高风险接触；
- 产品稳定支撑；
- 单一方向；
- 动作匹配切；
- Object State Ledger。
RETEST EVIDENCE:
- Attempt 3–5删除复杂收纳后未明显复现，但尚未专门复测精细放回。

# GF17｜Story Driver存在但没有被有效视觉化
STATUS: MITIGATED
TRIGGER CASES: Attempt 1 / Attempt 2
MITIGATION:
- 前1–3秒以可见/可听事件建立Driver；
- Driver直接连接Pain / Selling Point。

# GF18｜伪商业问题：把易生成操作步骤当卖点
STATUS: MITIGATED
TRIGGER CASES: Attempt 1 / Attempt 2
MITIGATION:
- Commercial Validity Gate；
- 先锁Why Buy + Pain + Selling Point + Emotional Payoff。
NOTE:
Attempt 5暴露的新问题属于GF28：即使Selling Point在Prompt中正确，也可能没有被观众解码。

# GF19｜把外部压力写成主角负面人格
STATUS: MITIGATED
TRIGGER CASES: Attempt 2
MITIGATION:
- `TENSION SOURCE ≠ PROTAGONIST NEGATIVITY`。

# GF20｜简单微动作时间预算过长
STATUS: MITIGATED
TRIGGER CASES: Attempt 2
MITIGATION:
- 简单微动作约0.5–1.2s；
- 蓄力给事件Cue；
- 动作匹配切。

# GF21｜空间声音与听觉因果不成立
STATUS: MITIGATED
TRIGGER CASES: Attempt 2
MITIGATION:
- 锁speaker位置/距离/方向/房间感；
- 耳机/门/玻璃改变听觉条件时做Hearing Plausibility Gate。

# GF22｜成对物体状态瞬移 / 复制
STATUS: CONFIRMED
TRIGGER CASES: Attempt 2 / Attempt 3
MITIGATION:
- Object State Ledger逐只追踪；
- Hero Shot服从Ledger；
- 人物仍佩戴时优先闭合盒体。
RETEST EVIDENCE:
- Attempt 4–5未复现结尾重复一对，但仍需跨Case复测。

# GF23｜Proof过早完成后的中段平台期 / Post-Proof Plateau
STATUS: CONFIRMED
TRIGGER CASES: Attempt 3 / Attempt 4
MITIGATION:
- Proof前40–50%完成时，后续必须有同Benefit的新因果Beat；
- 新Beat必须改变主角/产品/判断/观众理解；
- 没有高价值新Beat则缩短。

# GF24｜亚秒多镜头插值 / False Hard Cut Morph
STATUS: CONFIRMED
TRIGGER CASES: Attempt 4 Run A/B
MITIGATION:
- 快节奏靠信息密度，不靠3–4个亚秒独立物理场景；
- Hook优先一个强主镜头；
- 必须切时独立镜头尽量≥1.0–1.5s。

# GF25｜商业Beat密度塌陷 / TV Drama Drift
STATUS: CONFIRMED
TRIGGER CASES: Attempt 4 Run A/B
MITIGATION:
- 每2–3秒检查新商业Beat；
- 自然主义行为>3秒无新信息则压缩；
- Surprise/Comedy优先Proof后2–4秒；
- `Audio Calm ≠ Visual Slow`；
- 30秒没有足够高价值Beat则缩短。

---

# GF26｜180°越轴 / Camera Hemisphere Drift
STATUS: CONFIRMED
TRIGGER CASES:
- B1-S04-P1 Attempt 5
SYMPTOMS:
- 同一连续办公室空间内，镜头分别落到女主左前、右前/右侧、左后/OTS等不同180°半区；
- 没有中性镜头、可见过轴运动或新轴线建立；
- 人物、电脑、背景关系在观众脑中左右翻转，产生明显越轴和空间断裂。
ROOT CAUSE HYPOTHESIS:
SKILL_RULE_GAP + PROMPT_COMPILER
MITIGATION:
- 每个连续空间先锁Primary Axis；
- 再锁Allowed Camera Half；
- 同一段所有机位在同一180°半区内变化；
- 合法跨轴仅允许：可见移动穿轴 / 中性轴线镜头 / 明确新轴线建立；
- 使用`references/camera-action-compiler.md`中的Axis Ledger。
ROUTER IMPACT:
Camera / Spatial Continuity硬检查。

---

# GF27｜普通道具无动力自行移动 / Missing Motive Force
STATUS: CONFIRMED
TRIGGER CASES:
- B1-S04-P1 Attempt 5｜约22s普通办公手推车无人推动却自行滑过
SYMPTOMS:
- 无电机、无坡度、无人推动的普通物体自行移动；
- 背景“忙碌感”破坏真实世界物理逻辑。
ROOT CAUSE HYPOTHESIS:
PROMPT_COMPILER + PHYSICAL_CAUSALITY_GAP
MITIGATION:
- 所有显著移动道具先回答`谁让它动`；
- 普通推车必须由人物推/拉；
- 若要自动移动，明确写为具有电动底盘/传感器的autonomous robot cart；
- 不为背景热闹让无动力物体自己运动。
ROUTER IMPACT:
Physical Causality硬检查。

---

# GF28｜卖点存在于Prompt但观众无法解码 / Benefit Decodability Failure
STATUS: CONFIRMED
TRIGGER CASES:
- B1-S04-P1 Attempt 5
SYMPTOMS:
- Prompt明确只卖Active Noise Cancellation，但成片观众仍无法清楚回答“到底在卖什么”；
- 开场有办公室噪音，却没有让噪音造成一个清楚的可见任务阻力；
- 戴耳机前后人物状态差异太小，产品Benefit缺少不可错认的因果变化；
- 结果更像“漂亮职场女性戴耳机工作”，而不是“ANC解决噪音问题”。
ROOT CAUSE HYPOTHESIS:
COMMERCIAL_EXPRESSION + PERFORMANCE + PROMPT_COMPILER
MITIGATION:
新增`BENEFIT DECODABILITY GATE`：
1. Product Before前必须看到/听到一个明确Problem Cost；
2. Product介入动作必须是解决这个Problem的因果转折；
3. Product After后必须出现立即、可读的State Change；
4. 不靠结尾旁白才告诉观众卖点；静音看画面/只听声音至少有一条通道能理解Benefit；
5. 情绪Payoff必须来自Problem被解决，而不是人物从头到尾都很平稳。
ROUTER IMPACT:
Commercial Decision → Proof Expression → Performance联合硬检查。

---

# GF29｜时长与商业复杂度不匹配 / Duration-to-Story Misfit
STATUS: CONFIRMED
TRIGGER CASES:
- Attempt 3：约10s核心ANC已完成，后段平台期
- Attempt 4：为填30s加入生活事件，TV Drama Drift
- Attempt 5：仍需用办公蒙太奇/重复状态填充30s，商业清晰与情绪反而再次下降
SYMPTOMS:
- 单一卖点自然在12–18s即可完成；
- 为使用30s规格强行增加背景事件、重复Proof或自然主义工作过程；
- 越修越像电视剧，广告抓力下降。
ROOT CAUSE HYPOTHESIS:
BENCHMARK_DURATION_ASSUMPTION + STORY_PACING
MITIGATION:
新增`DURATION FIT GATE`：
- 时长由商业问题、Proof数量、架构复杂度和R-level共同决定，不由模型“最多能生成多久”决定；
- 单一强Proof + SA01/SA02/R0-R1若12–18s已完成，优先使用短版；
- 30s必须至少有第二个真实高价值商业Beat/Proof/关系变化，不能靠继续使用填满；
- Benchmark允许为了验证正确广告结构改变时长，并在记录里注明。
ROUTER IMPACT:
Story Architecture / Timeline前置决策。

---

# GF30｜元机位指令被字面生成成摄影器材 / Meta-camera Literalization
STATUS: CONFIRMED
TRIGGER CASES:
- B1-S04-P1 Attempt 5｜约5–6s画面中出现非剧情所需DSLR/三脚架
SYMPTOMS:
- Prompt中“摄影机和人物看向同一工作面”等元导演语言被模型当成场景实体；
- 画面凭空出现摄影机、三脚架，直接出戏。
ROOT CAUSE HYPOTHESIS:
PROMPT_WORDING
MITIGATION:
- 机位用`人物右肩后方OTS近景`、`画面从同侧观察`表达；
- 不把“摄影机/camera”写成动作主体；
- 非拍摄剧情加入`no visible filming equipment in scene`；
- 导演元语言与场景实体语言严格分离。
ROUTER IMPACT:
Seedance Prompt Compiler / Camera wording QA。

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

- 单次偶发失败不自动升级CONFIRMED；但Prompt因果明确、画面可直接验证的物理/轴线错误可以CONFIRMED。
- 同类问题跨2个以上Case复现，优先视为系统性风险。
- 同一Prompt连续2次复现相近结构问题，可作为强系统证据，但仍要跨产品/Scene继续监控。
- 简化后仍稳定失败，应考虑MODEL_LIMIT，不无限加Prompt。
- CONFIRMED问题复测解决目标问题后可升级MITIGATED，但继续跨Case监控。
- Failure Pattern用于未来Router/Compiler提前避错，不是让Prompt越来越长。
