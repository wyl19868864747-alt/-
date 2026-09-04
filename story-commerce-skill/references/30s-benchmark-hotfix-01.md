# 30S BENCHMARK HOTFIX 01｜长剧情证据、Reaction与交互负载修正

> 来源：30秒服装双人剧情首轮真实Seedance测试。
>
> 目标：修正“Beat齐全但证据不够硬、Reaction早于可见Trigger、连续Proof物理过载、R2证据重复”等问题。

---

# 1. INDEPENDENT EVIDENCE GATE｜R2证据必须真正独立

R2中的Evidence 1 / Evidence 2不能只是同一事实换句话说。

错误：
- 没有包；
- 两手空；
- 什么都没拿。

它们本质都在重复“没带东西”。

正确要求：
每个Evidence必须新增不同信息来源，并独立强化同一Wrong Answer。

例如：
- Evidence 1：人物没有任何包；
- Evidence 2：夹克轮廓平整且看不到明显口袋。

若删除其中一个后，另一个仍然独立成立，则更接近真正独立Evidence。

---

# 2. TRIGGER VISIBILITY GATE｜Reaction前结果必须真的被看见

任何关键Reaction必须服从：

`VISIBLE TRIGGER → GAZE LOCK → REACTION → NEW ACTION`

如果剧情写“从口袋拿出护照”，必须让护照完整离开口袋并进入可读画面后，才切第二人物Reaction。

禁止：
`手伸进口袋 → CUT → 对方震惊`

因为观众看不到对方究竟看见了什么。

---

# 3. ACCESS PATH GATE｜进入容器前必须先有合法入口

服装口袋、包、盒子、抽屉等都必须先建立真实Access Path。

统一链：

`外层状态 → 暴露入口 → 打开入口 → 物品对准入口 → 通过入口进入/离开 → 关闭（若需要）`

例如内袋：
`前襟打开 → 内侧面可见 → 内袋拉链打开 → 钱包进入 → 拉链关闭`

禁止：
- 外套仍关闭，物品直接进入内袋；
- 拉链未打开，手机穿过布料；
- 容器入口位置在切镜后自动改变。

若完整Access Path会导致复杂度过高，优先改用更简单的外侧口袋、动作匹配切或减少Proof次数。

---

# 4. INTERACTION LOAD BUDGET｜连续交互负载

“一镜一项高风险接触”仍然有效，但30秒还必须控制一个连续Burst段的总交互负载。

默认：
> 一个约4–6秒的Proof Burst，最多2次高风险实体交互。

高风险交互包括：
- 拉链开合 + 物品进出；
- 插拔；
- 精细穿戴；
- 多人递物；
- 液体倾倒；
- 多容器切换。

第三个Proof优先改成：
- 外观结果；
- 轮廓对比；
- Reaction；
- 声音/状态结果；
- Decision Change。

不要为了“证明更多”让模型连续处理三个以上小物体身份、入口和状态。

---

# 5. PROP IDENTITY LEDGER｜长视频道具身份守恒

30秒中不仅记录“物体在哪里”，还必须记录“它到底是什么”。

内部：
```text
PROP A: passport | state | location
PROP B: phone | state | location
PROP C: wallet | state | location
```

不同道具必须有明显外形区分；不需要的第三、第四道具应删除。

禁止：
- 移动电源跨镜变成手机；
- 钱包变成另一台电子设备；
- 同一手机复制成两台。

---

# 6. HOOK ESCALATION GATE｜持续冲突必须新增事件，不重复台词

30秒Hook后不能只用不同台词重复同一信息。

每约2–4秒至少新增一个：
- 新Evidence；
- 新Obstacle；
- 新Rule Pressure；
- 新Object State；
- 新Relationship Shift。

错误：
`没包？ → 你忘了 → 你什么都没有`

正确：
`没包 → 视觉确认周围确实没有包 → 夹克轮廓又平整无明显口袋 → Micro Anomaly`

---

# 7. 30S R2执行优先级

当30秒选择R2时，优先保证：

1. Wrong Answer清楚；
2. Evidence 1 / 2真正独立；
3. Micro Anomaly可见；
4. Reveal完整可见；
5. Reaction晚于Reveal；
6. 前文被重新解释；
7. Proof不超过模型交互负载；
8. Decision Change形成关系/购买行为变化。

如果必须在“更多Proof”和“完整Reveal”之间选择：

> **优先完整Reveal。**

如果必须在“第三个复杂交互”和“Reaction / Payoff”之间选择：

> **优先Reaction / Payoff。**
