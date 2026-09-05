# PROMPT ATTENTION COMPILER｜Seedance提示词权重、对白锁与执行压缩

> 来源：真实30秒服装与7-Eleven剧情广告生成复盘。
>
> 目标：解决“规则都写了，但模型因信息过载自动忽略台词、表情、状态或场面方向”的执行问题。不是继续加规则，而是把内部导演决策压缩成模型真正能执行的少量高权重指令。

---

# 0. 核心原则

Seedance最终提示词不是Skill全文，也不是导演会议纪要。

内部可以复杂，最终输入必须有明确权重：

`P0 HARD TRUTH / STATE`
→ `P1 CURRENT BEAT EVENT`
→ `P2 PERFORMANCE + CAMERA + AUDIO`
→ `P3 STYLE / DECORATION`

发生冲突时，必须删P3、压P2，不能牺牲P0/P1。

核心：

`INTERNAL COMPLEXITY > EXTERNAL PROMPT SIMPLICITY`

`ONE BEAT = ONE PRIMARY EVENT`

`FEWER WORDS, HIGHER EXECUTION WEIGHT`

`DO NOT REPEAT RULES TO CREATE IMPORTANCE`

---

# 1. PRIORITY TIERS｜最终提示词只有四档权重

## P0｜绝对锁定
只放会导致广告事实或连续性直接失败的内容：
- SKU / Reference Product Lock
- 谁能穿/用产品
- 产品数量与关键状态
- 精确必须保持的对白
- 关键空间起终点
- 合规事实

P0若超过太多项，先判断故事是否本身过载。

## P1｜当前Beat唯一主事件
每段只回答：
- 谁先动？
- 做什么？
- 结果是什么？
- 下一Beat为什么发生？

不能同时塞多个同级主动作。

## P2｜情绪、镜头、声音
只保留支持P1的：
- 1个情绪状态变化
- 1个主要表情链
- 1个主要镜头动作
- 1个关键SFX/BGM变化

## P3｜风格与装饰
例如：高级、时髦、松弛、电影感、环境小道具等。

P3不得重复进入每个Beat；开场总控统一一次即可。

---

# 2. 五层最终Prompt结构｜默认模板

最终提示词优先压成五层：

## ①【开场总控】
1句，最多2句。
只写广告类型、整体情绪斜率、平台原生感、镜头总体气质。

## ②【人物 / 产品 / 空间硬锁】
只保留跨镜必须持续的身份与状态。
不重复剧情。

## ③【对白锁】
只有台词确实重要时单独列：

```text
0–3s｜EMMA｜“You are NOT wearing that to dinner.”
3–5s｜CLAIRE｜“Watch me.”
```

使用：
`SPEAKER + EXACT LINE + TIME WINDOW`

不提供同义句，不写“类似表达”。

## ④【时间线】
每个Beat只写：
`主事件 + 情绪动作链 + 运镜 + 声音节点`

产品锁、人物身份等已在上层写过的内容不重复全文。

## ⑤【生成控制】
默认约8–12条真正高风险Hard Rules。
不要把几十条负面词作为结尾垃圾桶。

---

# 3. DIALOGUE LOAD BUDGET｜对白负载预算

真实生成暴露：3秒内多人物连续说3–5句，同时还要求切镜、产品特写与Reaction，极易出现说话人错位、台词改写或画面状态漂移。

默认：
- **一个镜头只有一个明确说话人。**
- 一个约2–4秒Beat最多1–2句短核心台词。
- 同一Beat若有强Product Action / 强Reaction，优先只留1句。
- 关键短句尽量5–9个英文词；只有事实无法压缩时才更长。
- Punchline / 决策句优先独占镜头或Reaction停顿。

禁止：
`A一句 → B一句 → A一句 → 产品特写 → Reaction` 全塞2–3秒。

若台词精确性比动作更重要：减少镜头任务，不继续添加“must say exactly”等重复警告。

---

# 4. SPEAKER LOCK｜对白与画面绑定

每句关键对白内部必须确定：

```text
SPEAKER:
VISIBLE / OFFSCREEN:
CURRENT SHOT SUBJECT:
EXACT LINE:
LISTENER:
TRIGGER:
NEXT ACTION:
```

最终至少保留：
`镜头主体 + Speaker + Exact Line`

原则：
> **谁在镜头里说，就让这一镜只服务这个说话人；Reaction另切。**

这样优先于两个人同一镜里快速抢话。

---

# 5. BEAT LOAD BUDGET｜一个Beat最多四个执行信号

一个普通剧情Beat最终Prompt默认最多：
1. `PRIMARY EVENT`
2. `EMOTION / FACE CHAIN`
3. `CAMERA MOVE`
4. `AUDIO CUE`

必要时加1个Product Detail，但必须与Primary Event同因果。

如果一个Beat同时要求：
- 复杂空间移动
- 多句对白
- 强Reaction
- 产品精细操作
- 品牌露出
- 复杂运镜
- BGM变化

必须拆Beat，不许继续堆文本。

---

# 6. ACTION VERB ENERGY｜用动词传递强度，不用态度说明

高压、冲突、买量广告允许积极使用高能动词：
- 突然停住
- 猛地转头
- 迅速锁定
- 快速扫视
- 突然逼近半步
- 猛地抬眉
- 瞬间睁大眼
- 快速推近
- 突然甩向
- 猛地硬切
- 音乐瞬间抽空

但规则是：
> **一个Beat最多选1个主动作极限词 + 1个表情极限词 + 1个镜头极限词。**

不要写：
`突然猛地迅速快速立刻狠狠地……`

极限词必须绑定具体动作，不能单独写“情绪更强”。

---

# 7. DELETE ATTITUDE, KEEP VISIBLE ACTION｜删除无效态度说明

以下低价值说明若无法直接生成，默认删掉或动作化：
- 她不是恶意的
- 她知道答案但不炫耀
- 她审美很好
- 她很高级
- 她真实地质疑
- 她不想显得刻薄

替换为可见内容：
- 嘴唇压紧 / 不笑
- 身体前逼半步
- 视线从产品扫到人物
- 回答前停0.3秒
- 不解释，直接执行下一动作

只有会改变台词、动作或关系的态度才保留。

---

# 8. STATE REPLACEMENT RULE｜状态替换必须显式，不让旧锁残留

当人物前后状态真的改变，例如换装、摘耳机、拿走商品：

不要同时写：
`服装全片稳定`
+
`后面换装`

应该写：

```text
PRE-REVEAL STATE:
black top + trousers

HIDDEN TRANSITION:
pre-reveal outfit is fully replaced

POST-REVEAL STATE:
reference dress only
```

状态改变时：
`OLD STATE ENDS → TRANSITION → NEW STATE BEGINS`

避免模型为了同时满足两个强锁，把旧裤子和新裙子叠在一起。

---

# 9. NO REDUNDANT NEGATIVE PATCHING｜不靠重复禁词加权

如果内部已经通过：
- Product Lock
- State Ledger
- Scene Staging
- Physical Logic

最终不要再连续重复：
`不要反向 / 不要进门 / 不要转身 / 不要走错 / 不要……`

优先一条正向可执行句：
> `两人从店内穿过自动门走出，面向镜头，店门始终在身后且距离持续增加。`

正向状态链比负面补丁更高效。

---

# 10. PROMPT ATTENTION QA

输出Seedance Prompt前静默检查：

- [ ] P0硬锁是否只有真正会导致广告失败的内容？
- [ ] 每个Beat是否只有一个Primary Event？
- [ ] 一个镜头是否只有一个明确说话人？
- [ ] 2–4秒Beat是否超过2句核心对白？
- [ ] 对白是否使用Speaker + Exact Line绑定？
- [ ] 情绪是否动作化，而不是态度形容？
- [ ] 每个Beat是否最多1个主表情链、1个主运镜、1个主要Audio Cue？
- [ ] 前后状态改变是否明确结束旧State而不是叠加？
- [ ] 同一规则是否在3个地方重复？若是，删除重复。
- [ ] 生成控制是否约8–12条，而不是长负面清单？
- [ ] 删除所有风格形容词后，视频主事件、对白、状态仍然完整吗？

失败时：
> **先删、再拆Beat、再缩对白；最后才考虑新增提示词。**

最终：

`SIMPLIFY BEFORE ADDING`

`EXACT DIALOGUE NEEDS EMPTY SPACE`

`STRONG EMOTION NEEDS CLEAR ACTION`

`PROMPT ATTENTION IS A FINITE BUDGET`
