# REALITY LOGIC GATE｜跨品类真实世界逻辑闸门

> 位置：Story / Proof / Visual Execution 已确定之后，最终 Prompt Compile 之前。
>
> 目标：禁止把“大纲里要表达什么”机械改写成“人物就这么做”。先把创意意图转成现实中成立、产品事实正确、摄影机真实可见、人物身份可区分、跨镜状态与数量连续、卖点可感知的执行关系。

---

## 0. 模块边界

本模块只定义**跨品类通用的现实规律**，不内置耳机、服装、美妆、食品、家电等单品操作模板。

具体产品的：

`开合 / 穿戴 / 操作 / 使用 / 状态变化 / 功能反馈`

必须由当前 Product Truth 动态决定。

固定结构：

`Universal Reality Kernel + Product Reality Profile + Character Differentiation Lock → Reality-Resolved Beat → Prompt Compile`

本模块不负责：
- 重新想商业核心；
- 重写产品事实；
- 重新选择Style / Hook / CTA；
- 重复Physical Logic DNA、Scene Staging或Camera Compiler的细节规则；
- 直接输出冗长分析给用户。

---

## 1. Product Reality Profile｜当前产品现实档案

每次只建立本条广告真正会用到的最小事实集：

```text
CURRENT STATE:
ALLOWED OPERATION:
REAL OPERATION METHOD:
STATE AFTER:
DIRECTLY OBSERVABLE RESULT:
SUBJECTIVE / INDIRECT EXPERIENCE:
SOURCE OF FACT:
```

事实来源优先：

`用户素材 / 参考图 / 已确认信息 / 可靠产品资料`

如果某个结构、按钮、开合、穿戴、配件或操作方式无法确认：

**保持未知，不自行补全；改用不暴露未知结构的保守动作。**

品类变化时，只更新 Product Reality Profile；下面的 Reality Kernel 不变。

---

## 1.1 Character Differentiation Lock｜多人角色区分锁

当同一条广告存在2名及以上持续出现的人物时，必须先建立**最小人物区分**，避免模型把不同角色收敛成同一张脸、同一发型、同一服装，产生“自己和自己对话”。

每个主要人物只保留少量高辨识锚点：

```text
ROLE:
VISUAL ANCHOR 1:
VISUAL ANCHOR 2:
DIALOGUE ROLE:
```

推荐优先使用：
- 发型/发色轮廓；
- 上装颜色或服装轮廓；
- 一个明显但不过度细化的外观差异。

原则：
- 不写长篇五官说明；
- 不让人物描述抢产品和剧情权重；
- 不要求两人“像姐妹/双胞胎”；
- 每个角色保持独立且持续的面部身份；
- 对白Speaker始终绑定对应角色，不允许角色互换或复制。

最终Prompt中必须压缩保留这组人物区分锚点，但只写到“足以区分角色”的程度。

---

# 2. UNIVERSAL REALITY KERNEL｜六项通用检查

## A. Intent ≠ Action｜信息目的不等于人物动作

先拆开：

`观众需要知道什么`
≠
`人物现实中做什么`
≠
`摄影机如何让观众知道`

禁止为了展示信息，让人物、产品、屏幕、包装或道具做出现实中不合理的动作或朝向。

如果信息无法在当前镜头自然成立：

`改机位 / 拆镜 / 反打 / 过肩 / 特写`

---

## B. Reality Chain｜事件必须有现实因果

所有关键事件按：

`触发 → 感知 → 反应 → 动作 → 结果`

人物收到：

`提问 / 质疑 / 递物 / 突发事件 / 产品体验`

后必须出现必要回应。

短视频优先使用最小反应：

`眼神 / 微表情 / 小动作 / 短句`

只保留推进剧情所需的最短承接，不强制增加长对白。

---

## C. Camera Reality｜摄影机只能看到现实中可见的内容

先确定：

`摄影机位置 → 人物朝向 → 人物视线 → 物体朝向 → 摄影机实际可见内容`

如果“人物必须看到的信息”和“观众必须看到的信息”在同一机位无法同时成立：

**拆镜，不旋转现实来服务展示。**

原则：

`CAMERA FOLLOWS REAL SPACE; REAL SPACE DOES NOT BEND FOR INFORMATION DISPLAY.`

---

## D. Product Truth｜产品操作必须服从真实结构

人物与产品发生交互时，必须按：

`当前真实状态 → 已确认操作 → 产品响应 → 新状态`

禁止：
- 猜测产品结构；
- 虚构按钮、接口、配件；
- 虚构开合/穿戴/使用方式；
- 为了让镜头更顺而改变真实操作机制。

具体受力、路径、接触、铰链、容器和状态守恒继续交给 `physical-logic-dna.md` 编译。

---

## E. Entity / Quantity / State Conservation｜身份、数量与状态守恒

### 人物身份
每个持续角色必须保持独立身份，不因切镜、反打或多人同框而复制、融合、换脸或互换角色。

### 产品/道具数量
只要产品或关键道具有固定数量、成对或套装关系，先锁定：

`TOTAL INVENTORY = N`

每一个实体在任一时刻只能有一个位置、一个持有人和一个状态。

必要时内部追踪：

```text
UNIT A:
UNIT B:
...
CURRENT OWNER / LOCATION / STATE:
```

总量必须始终守恒。禁止同一个实体同时：
- 戴在人物身上又出现在手里；
- 戴在人物身上又留在盒内；
- 被A持有又被B同时持有；
- 因切镜凭空增加、复制或消失。

### 跨镜状态
下一镜默认继承上一镜已经建立的：

`人物位置 + 手中物品 + 产品归属 + 开合/佩戴/使用状态 + 道具位置 + 已完成动作 + 当前任务`

### 时间跳转 / 换场景
如果明确发生时间跳转、地点跳转或中间过程被省略，不能机械继承旧状态，也不能让模型自行猜测。

必须显式建立新场景入口状态：

`PREVIOUS STATE ENDS → TIME/SCENE JUMP → NEW ENTRY STATE`

新场景至少明确关键人物与产品此刻的：

`是否佩戴 / 是否手持 / 是否收纳 / 开合状态 / 所在位置`

这样既允许合理的离屏变化，又避免上一场的佩戴、手持或开合状态错误残留到下一场。

同时检查：

> 当前人物行为是否与正在证明的卖点冲突？

如果冲突，优先修改动作，不修改真实卖点。

---

## F. Perceptible Proof｜卖点必须变成可感知证据

卖点不能直接等于生成指令。

必须经过：

`产品能力 → 用户真实体验 → 现实中产生的结果 → 观众如何看到或听到`

可使用：
- 动作结果；
- 产品状态变化；
- 环境变化；
- 声音变化；
- 材质/形变/运动变化；
- 使用效率变化；
- 克制的人物反应。

对于摄影机无法直接拍到的主观体验，例如：

`舒适 / 音质 / 降噪 / 凉感 / 轻薄 / 柔软 / 香味 / 沉浸 / 顺滑`

必须寻找现实可感知证据。

禁止只靠：
- 台词宣称；
- “她觉得很好”；
- 瞪眼、张嘴等夸张Reaction；
- 抽象词直接下发给生成模型。

高风险、长期、医学、认证或精确测量型Claim仍不能由主观视听体验代替客观证据。

---

# 3. REALITY-RESOLVED BEAT｜Gate输出

本模块不输出长篇分析，只把每个关键Story Beat内部解析成：

```text
INFORMATION INTENT:
REAL HUMAN ACTION:
CHARACTER ROLE / IDENTITY:
PRODUCT STATE / OPERATION:
INVENTORY STATE:
CAMERA-SAFE EXPRESSION:
PERCEPTIBLE RESULT:
REACTION / RESPONSE:
NEXT-BEAT STATE:
```

发生时间/场景跳转时，再补：

```text
NEW SCENE ENTRY STATE:
```

然后交给：

`Scene Staging / Physical Logic / Camera Action → Prompt Attention Compiler`

下游模块负责“如何稳定生成”；本Gate负责“这件事首先必须在现实中成立”。

---

# 4. FAIL ROUTING｜失败处理

任一项不成立时：

优先保留：
1. Product Truth；
2. Core Decision；
3. Best Proof / Selling Point；
4. 核心剧情目的。

允许修改：
- 人物动作；
- 机位 / 景别；
- 镜头数量；
- Reaction方式；
- 产品展示方式；
- 声音与环境表达；
- Beat之间的承接；
- 场景入口状态。

禁止为了保留原分镜而破坏真实逻辑、复制角色/产品或虚构产品事实。

---

# 5. GATE CHECK｜进入Prompt前静默检查

- [ ] 已区分“观众要知道什么 / 人物做什么 / 摄影机怎么展示”。
- [ ] 多人物场景已建立最小角色区分，不会出现同脸、同发型、同服装导致的角色坍缩或自己和自己对话。
- [ ] 关键事件满足触发→感知→反应→动作→结果。
- [ ] 当前机位下人物视线、屏幕/包装/产品朝向真实成立。
- [ ] 所有关键产品操作来自已确认事实或保持未知。
- [ ] 固定数量/成对/套装产品已锁TOTAL INVENTORY，任一实体只有一个位置、持有人和状态。
- [ ] 下一镜继承上一镜的手持、佩戴、开合、位置和使用状态。
- [ ] 时间/场景跳转已明确新的入口状态，不让旧佩戴/手持状态错误残留。
- [ ] 人物行为没有抵消当前卖点。
- [ ] 主观体验已转成可感知视听结果，而不是只靠台词/夸张表情。

任一项失败：先修Reality-Resolved Beat，再进入最终Prompt Compile。

---

# 6. 跨品类原则

**Reality Logic Gate只定义共性规律；具体产品事实动态填充。**

因此：
- 数码换成服装，不换Reality Kernel；
- 服装换成美妆，不换Reality Kernel；
- 美妆换成食品/家电/App，也不换Reality Kernel；
- 只更新该产品本次剧情真正需要的 Product Reality Profile；
- 多人物身份区分、固定数量守恒、时间跳转入口状态同样适用于所有品类。

判断的不是“耳机应该怎么开”或“服装应该怎么拍”，而是：

> **当前角色是不是不同的人；当前产品在现实中应该怎么被正确使用；产品/道具数量有没有守恒；当前人物、产品状态和摄影关系是否真的成立；卖点有没有被观众真实感知。**
