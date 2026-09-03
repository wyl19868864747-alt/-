# GENERATION FAILURE PATTERNS｜Seedance真实失败模式库

> 目的：把“这条视频坏了”升级成“我们知道为什么坏、以后什么时候应该提前避开”。

只有真实生成中观察到的Failure Pattern才能升级为 `CONFIRMED`。

当前初始条目全部为：`WATCHLIST`。

状态：
- `WATCHLIST`：理论/历史经验高风险，等待Benchmark验证
- `CONFIRMED`：真实Case重复出现或证据明确
- `MITIGATED`：已有稳定规避方法并复测通过
- `MODEL_LIMIT`：当前模型能力边界，Router应主动规避
- `RETIRED`：新模型/新流程下已不再构成稳定风险

---

# GF01｜多人递物 / Handoff穿模

STATUS: WATCHLIST

症状：
- 两只手与产品重叠
- 产品突然跳到另一只手
- 递交中商品尺度变化
- 接手人物的手从不合理位置进入镜头

常见触发：
- 3人以上
- 狭窄空间
- 托盘/盒子/杯子同时参与
- 快速切镜仍要求连续交接

初始规避：
- 最低必要人物
- 拆成“递出 → 独立接手镜”
- 明确产品起点/终点
- 不要求复杂双手交叉

高风险Scene：S01 / S06 / S09 / S12

---

# GF02｜远距离人物的手突然进入近景

STATUS: WATCHLIST

症状：
人物上一镜离产品很远，下一特写出现其手直接拿产品，无空间过渡。

初始规避：
- 先写人物靠近/伸手
- 产品特写前建立接触
- 不用“远处人物 + 独立手部特写”硬接

---

# GF03｜玻璃门 / 门框 / 狭窄空间穿模

STATUS: WATCHLIST

症状：
- 人穿过关闭玻璃门
- 手穿门框
- 开门方向跨镜改变

高风险Scene：S04 / S12

初始规避：
- 锁门侧、人物站位、开门方向
- 门动作单独成为Beat
- 复杂交互时不要同时拿商品

---

# GF04｜产品尺度漂移

STATUS: WATCHLIST

症状：
- 手持时变大/变小
- 从桌面到特写比例改变
- 包装和本体尺寸关系失真

初始规避：
- PRODUCT LOCK含相对尺度
- 用手掌/桌面/人体作稳定参照
- 避免无参照的极端特写后直接切大全景

---

# GF05｜屏幕 / LED / 包装文字乱码

STATUS: WATCHLIST

症状：
生成屏幕、价格、包装、LED出现乱码或错误信息。

高风险Scene：S04 / S08 / S10 / S07

初始规避：
- 非必要文字不成为关键Proof
- Proof用可见动作/物理状态优先
- 精确文字依赖真实资产或后期

---

# GF06｜多人同步转头 / 同步震惊

STATUS: WATCHLIST

症状：
所有人物同一帧同步看向商品、同步瞪眼、同步张嘴。

高风险Scene：S02 / S06 / S07 / S09 / S11

初始规避：
- Reaction Chain明确先后
- 先写First Observer
- 第二人顺着视线发现
- 群体Reaction用传播，不用同时触发

---

# GF07｜R2提前泄底

STATUS: WATCHLIST

症状：
演员在Micro Anomaly前就露出知道真相的表情/动作，导致Wrong Answer不可信。

初始规避：
- Evidence阶段保持旧判断
- Micro Anomaly才允许停顿/视线变化
- Reveal后再做认知重置

---

# GF08｜连续动作顺序错乱

STATUS: WATCHLIST

症状：
- 结果先于原因
- 商品先打开再伸手
- 人物先反应后看见
- 清洁结果先出现再擦

初始规避：
- Beat按`人先动作 → 接触 → 物体响应 → 结果`
- 一段只保留一个主要动作任务
- 复杂操作拆镜

---

# GF09｜狭窄空间左右/方向漂移

STATUS: WATCHLIST

症状：
- 窗侧/门侧互换
- 走廊前后方向反转
- 人物突然从错误车厢/门出现

高风险Scene：S12，次高S04

初始规避：
- Continuity Anchors写入Prompt
- 固定window_side / door_side / corridor_direction
- 减少无动机反打

---

# GF10｜现代商品被古代化 / 未来化

STATUS: WATCHLIST

症状：
- 现代产品获得铜制/木制/复古外观
- 未来Scene自动让商品发光、透明、全息、带AI

高风险Scene：S01 / S03 / S05 / S08 / S11 / S12

初始规避：
- Reference image最高优先
- 明确现代SKU保持原貌
- `WORLD TECH ≠ PRODUCT FACT`
- Scene只改环境与人物，不改产品

---

# GF11｜Proof被剧情/Reaction抢掉

STATUS: WATCHLIST

症状：
观众记得角色闹得很热闹，却没看清产品到底证明了什么。

初始规避：
- Proof先锁时间预算
- Product Proof镜头稳定
- Reaction必须发生在Proof之后
- R2/Comedy/Scene复杂度不足时先降级创意模块

---

# GF12｜Scene只剩背景，没有DNA

STATUS: WATCHLIST

症状：
场景看起来是宫廷/办公室/列车，但人物行动、冲突、商品入口和Reaction换成客厅仍完全一样。

初始规避：
- 强制DNA Activation
- 检查Unique Causal Gain
- 若没有增益，退回NORMAL_LOCATION

---

# GF13｜表情过满导致人物失真

STATUS: WATCHLIST

症状：
连续瞪眼、张嘴、翻白眼、过度眉眼变化，脸部身份稳定性下降。

初始规避：
- 一个短Beat只保留1个视线 + 1–2个主要面部变化
- 动作复杂时优先删表情细节
- 大全景不写精细微表情

---

# GF14｜多人身份/服装漂移

STATUS: WATCHLIST

症状：
- A/B人物互换服装或脸
- 群体角色跨镜身份混乱

初始规避：
- 最低必要人物数
- 主要人物位置/衣着锚点
- 群众弱化，不让背景承担关键剧情

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
是否需要让Router提前降权/阻断？
```

---

# 规则

- 单次偶发失败不自动升级CONFIRMED。
- 同类问题跨2个以上Case复现，优先视为系统性风险。
- 如果简化后仍稳定失败，应考虑MODEL_LIMIT，不继续无限加Prompt。
- CONFIRMED失败若有稳定规避方案并复测通过，可升级MITIGATED。
- Failure Pattern的价值是让未来Router提前避错，不是让Prompt越来越长。
