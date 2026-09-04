# 30S BENCHMARK HOTFIX 01｜长剧情证据、Reaction与交互负载修正

> 来源：30秒服装双人剧情首轮与真实Reference羽毛裙测试。
>
> 目标：修正“Beat齐全但证据不够硬、Reaction早于可见Trigger、连续Proof物理过载、R2证据重复、穿戴商品角色归属混乱、Reveal前状态泄漏”等问题。

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

---

# 8. WEARABLE OWNERSHIP LOCK｜穿戴商品角色归属锁

真实服装、鞋、珠宝、腕表等穿戴商品，在每一个剧情Beat都必须只有一个明确状态与归属。

内部至少记录：
```text
PRODUCT SKU:
CURRENT LOCATION: rack / hand / fitting room / body
CURRENT WEARER: NONE / Character A / Character B
NON-WEARER WARDROBE:
```

硬规则：
- 同一件真实SKU不能同时挂在衣架上又穿在人物身上；
- 同一件SKU不能同时穿在两个主要人物身上；
- 非产品人物必须有明确的非产品服装状态，不能因为参考图里有人穿产品就被模型自动套上同款；
- 穿戴归属变化必须经过明确剧情状态转换或合法换装Match Cut。

推荐链：
`GARMENT ON RACK / WEARER NONE → Character A takes garment → fitting-room hidden transition → GARMENT ON Character A / rack empty`

---

# 9. REVEAL STATE RESERVATION｜Reveal前禁止泄漏最终状态

如果剧情高潮依赖“第一次完整看到某个状态”，该状态在Reveal之前必须被保留，不能提前泄漏。

例如：
- 挂着看夸张 → 上身后意外高级；
- 盒子打开才揭示内部结构；
- 结果屏幕出现才揭示答案。

若Reveal目标是“Character A第一次完整穿上产品”，则Reveal前：
- 任何主角/配角都不得提前穿同一SKU；
- 镜子、背景人物、衣架旁的Reference泄漏都不得出现完整上身状态；
- 可以展示产品挂着、材质微距、局部下摆、手持等未完成状态。

公式：
`PRE-REVEAL STATES ≠ FINAL REVEAL STATE`

否则即使后面有全身Hero镜头，R2的惊喜也已经被提前花掉。

---

# 10. REFERENCE-WEARER SEPARATION｜参考图中的模特不是剧情角色

当产品参考图包含真人模特时，必须把“产品身份”和“参考图人物”拆开。

参考图只锁：
- 商品结构；
- 尺寸/长度关系；
- 材质；
- 颜色；
- 局部动态与上身比例。

默认不继承：
- 参考图模特身份；
- 发型/脸；
- 配饰；
- 姿势；
- 其他搭配单品；
- 谁应该在剧情里穿产品。

剧情层必须另外明确：
`WHO MAY WEAR PRODUCT = Character X only after Beat N`

如果产品Reveal依赖换装，优先把这句状态约束写入人物/产品锁定，而不是只写“不要让另一个人穿”。

---

# 11. REVEAL-FIRST QA｜30秒服装R2额外检查

- [ ] Reveal前产品没有以最终穿戴状态提前出现
- [ ] 同一SKU任一时刻只有一个Location / Wearer
- [ ] 非产品人物有清楚的Wardrobe Lock
- [ ] 衣架上的产品被拿走后，衣架状态同步为空
- [ ] Full-body Reveal真的第一次完整给出答案
- [ ] Reaction晚于完整Reveal
- [ ] Second Proof验证新的疑问，不重复第一次Reveal
- [ ] 最终Decision Change来自看到产品结果，而不是台词自行宣告
