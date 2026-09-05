# PERFORMANCE × FACS COMPILER｜剧情带货表演、情绪过渡与微表情动作库

> 来源：连续真实Seedance剧情广告Benchmark。
>
> 目标：把已经确定的Story Beat编译成**可见、可生成、有强弱过渡、能与运镜/声音同步的表演动作**。避免“Skill里有FACS，最终Prompt却只写克制/自然，导致冲突和Reveal反应过平”。

---

# 0. 定位

调用位置：

`Story / Proof / R-level / Scene / Staging`
→ `Performance Intent`
→ `Emotion Intensity`
→ `Gaze / Face / Head / Body`
→ `Camera Emotion Handoff`
→ `Dialogue / Next Action`
→ `Seedance Prompt`

核心原则：

> **先有事件，再有Reaction；先定情绪强度与过渡，再选面部动作。**

FACS是可见面部运动词典，不是“一个情绪=一个唯一表情”的真值表。最终Seedance提示词默认**不输出AU编号**，只写人能看见的动作变化。

`QUIET PERFORMANCE ≠ FLAT EMOTION`

`STRONG REACTION ≠ LONG REACTION`

---

# 1. 表演优先级

每个Reaction按以下顺序编译：

`Trigger`
→ `Gaze Target`
→ `Emotion Intensity`
→ `First Facial Change`
→ `Micro Pause / Release`
→ `Head / Body Response`
→ `Dialogue or New Action`

优先级：

`事件动作 > 视线 > 身体反应 > 关键面部变化 > 台词语气 > 装饰性表情`

一个短Beat默认只保留：
- 1个明确视线变化；
- 1–2个主要面部变化；
- 0–1个必要身体变化；
- 1个情绪方向变化。

只有Reaction特写、Micro Anomaly或高潮Reveal才增加细节。

## 1.1 商业人物吸引力｜压力不等于让主角讨厌

`TENSION SOURCE ≠ PROTAGONIST NEGATIVITY`

普通商用广告中，压力优先来自：
- 时间
- 环境
- 任务
- 选择
- 外部阻力
- 社会关系

主角默认应保持：有能力、有能量、可喜欢/可代入、遇到问题后主动行动。

除非用户明确要求荒诞、黑色、狗血、讽刺或强关系冲突，不用持续不耐烦、丧气抱怨、无原因翻白眼/冷笑承担Hook。

短促压怒、排斥、震惊可以很强，但必须有明确事件Trigger并迅速进入下一动作。

---

# 2. FACS核心动作词典｜内部参考

| AU | 可见动作 |
|---|---|
| AU1 | 内眉抬起 |
| AU2 | 外眉抬起 |
| AU4 | 眉毛下压/眉心收紧 |
| AU5 | 上眼睑抬起，眼裂增大 |
| AU6 | 面颊抬起，眼周收紧 |
| AU7 | 眼睑收紧 |
| AU9 | 鼻部皱起 |
| AU10 | 上唇抬起 |
| AU12 | 嘴角向上拉 |
| AU14 | 嘴角单侧收紧/不对称变化 |
| AU15 | 嘴角向下 |
| AU17 | 下巴/颏部收紧 |
| AU20 | 嘴角水平向外拉 |
| AU23 | 嘴唇收紧 |
| AU24 | 嘴唇压紧 |
| AU25 | 双唇分开 |
| AU26 | 下颌下降 |

常见组合只作内部参考：
- 快乐：`AU6 + AU12`
- 惊讶：`AU1 + AU2 + AU5`，强时可加`AU26`
- 愤怒/压怒：`AU4 + AU5/7 + AU23/24`
- 厌恶：`AU9/10`
- 悲伤：`AU1 + AU4 + AU15`
- 恐惧：`AU1 + AU2 + AU4 + AU5 + AU20`
- 轻蔑：常见单侧`AU14`

不要把组合当成跨人物、跨文化、跨语境的固定情绪指纹。

---

# 3. BEAT-LEVEL EMOTION INTENSITY｜每个Beat单独定强度

旧规则“商业广告默认克制”保留，但不再把全片统一压成SUBTLE。

内部使用1–5级：

- `1/5`：几乎中性，轻微注意变化
- `2/5`：轻怀疑、轻认可、自然生活状态
- `3/5`：明确可读的紧张、挑战、惊讶、决心
- `4/5`：强冲突、强排斥、难以置信、明显压迫
- `5/5`：只给真正高潮Reaction / Burst Reveal / 极强意外，短促使用

规则：
- 强度服务Story Beat，不由“高端/高级”自动压低。
- 高端广告可以表演克制，但冲突节点仍可4/5、Reveal Reaction可5/5。
- 5/5不等于持续尖叫；它可以是`猛地抬眉 + 眼睛瞬间睁大 + 下颌松开 + 身体冻结0.3–0.5s`。
- 同一人物连续Beat应有强度变化，避免全程同一脸。

### 推荐情绪曲线示例

`冲突4 → 复核3 → Delay3 → Reveal Shock5 → Verify4 → Accept3/4`

错误：
`质疑2 → 回答2 → 再质疑2 → Reveal2 → 接受2`

后者逻辑完整但没有情绪斜率。

---

# 4. 商业剧情常用表情链｜动作模板

## 4.1 怀疑 / 不信
`视线锁住证据 → 眉心压下 → 眼睑收紧 → 嘴唇压紧 → 暂不说话`

## 4.2 困惑
`视线在物体与人物间快速切换 → 内眉抬起同时眉心略收 → 嘴唇轻分 → 头微偏`

## 4.3 轻惊讶
`眉毛快速抬起 → 眼睛短暂睁大 → 嘴唇轻分 → 立刻锁回结果`

## 4.4 强惊讶 / 震撼｜Reveal可用4–5/5
`眼神猛地锁住结果 → 双眉突然明显抬高 → 眼睛瞬间睁大 → 下颌突然松开/嘴巴短暂张开 → 身体本能后撤半步或冻结0.3–0.5秒 → 再快速重新扫视结果`

必须短促。高潮之后进入Verify，不能保持同一震惊脸数秒。

## 4.5 难以置信
`盯结果 → 眉毛短促抬起 → 眉心重新收紧复核 → 快速从上到下扫视产品/结果 → 再看对方 → 新验证`

## 4.6 发现异常
`原动作突然停半拍 → 眼睛先移向异常点 → 眉心收紧/单眉抬起 → 身体轻向目标靠近 → 保持观察`

## 4.7 恍然 / 理解
`眉心松开 → 视线从证据移向人物 → 嘴唇轻分后合上 → 呼气/轻点头 → 新行动`

## 4.8 压怒 / 强硬质疑
`眉毛猛地压低 → 眼睑收紧 → 嘴唇压紧 → 下颌收紧 → 身体向前逼近半步 → 视线不离目标`

仅在剧情真的有关系冲突/规则压力时调用，不给普通主角无原因加攻击性。

## 4.9 厌恶 / 排斥
`鼻部短促皱起 → 上唇抬起 → 头后撤一点 → 视线离开刺激物后迅速回看`

## 4.10 担忧 / 紧张
`内眉抬起靠近 → 眼睑略紧 → 嘴唇抿住 → 呼吸变短 → 迅速检查关键对象`

## 4.11 害怕
`眉毛抬起收拢 → 眼睛明显睁大 → 嘴唇分开 → 身体后撤/冻结`
剧情带货低频使用。

## 4.12 失落 / 失望
`内眉抬起收紧 → 嘴角轻下压 → 视线落下 → 肩颈松掉`

## 4.13 尴尬
`快速看左右/旁人 → 视线错开 → 嘴唇压紧 → 短促紧笑/下巴内收 → 身体略缩`

## 4.14 心虚 / 被戳穿
`直视 → 视线猛地短移开 → 嘴唇压紧 → 下巴内收 → 试图恢复正常`

## 4.15 释然
`眉心/眼睑明显松开 → 呼气 → 肩膀下降 → 嘴角抬起 → 回看产品/对方`

## 4.16 满意 / 认可
`看结果 → 眼周放松 → 面颊轻抬 → 嘴角上扬 → 轻点头/继续使用`

## 4.17 开心 / 真正愉悦
`面颊抬起 → 嘴角上扬 → 眼周自然收紧 → 身体打开`

## 4.18 克制好笑 / 憋笑
`嘴角想上扬又压住 → 面颊抬起 → 快速看旁人 → 0.3–0.6秒停顿 → 回到事件`

## 4.19 轻蔑 / 不屑
`单侧嘴角收紧 → 下巴轻抬/头略偏 → 很短 → 回到事件`
只适合明确关系冲突。

## 4.20 专注 / 认真核验
`目光锁定操作点 → 眉心收紧 → 嘴唇闭合 → 头部减少移动 → 手更精确`

## 4.21 下定决心 / 坚定
`视线从证据猛地抬回目标 → 眉眼稳定 → 嘴唇压紧后放松 → 轻点头 → 立刻行动`

---

# 5. EMOTION TRANSITION COMPILER｜不是静态脸，是状态过渡

关键Reaction必须至少写出“前态 → 转折 → 后态”。

例如强Reveal：

`SHOCK → VERIFY → ACCEPT`

可见链：
1. `Shock`：猛抬眉、眼睛瞬间睁大、下颌松开、冻结0.4秒；
2. `Verify`：嘴巴合回去，眉心重新收紧，视线快速从产品上到下扫描；
3. `Accept`：眉心突然松开，呼气，嘴角上扬，做出新决定。

禁止：
`震惊脸 → CUT → 开心脸`

中间没有认知复核，人物会像表情贴纸切换。

---

# 6. Reaction Compiler

内部字段：

```text
TRIGGER:
PERFORMANCE INTENT:
INTENSITY 1–5:
GAZE TARGET:
FIRST FACE CHANGE:
BODY RESPONSE:
NEXT EMOTION STATE:
NEXT ACTION:
```

最终压成：
`Trigger → gaze → face/body change → micro pause → verify/release → new action → line（若必要）`

Reaction若不改变观众理解或下一动作，就不要占时间。

---

# 7. ACTION VERB ENERGY｜高压Beat允许高能动词

普通提示词太多“自然、轻轻、短暂”会把所有情绪压平。

冲突/危机/强Reveal可使用：
- 突然停住
- 猛地转头
- 迅速锁定
- 快速扫视
- 突然逼近半步
- 猛地抬眉
- 瞬间睁大眼
- 身体本能后撤
- 突然冻结

但：
> **一个Beat最多1个主动作极限词 + 1个主要表情极限词。**

不用极限词堆砌代替具体动作。

---

# 8. R0 / R1 / R2 表演边界

## R0
Reaction只服务Problem / Proof / Choice / Task / Experience / Decision Change。
禁止为了情绪起伏偷偷添加反转。

## R1 Clarification
`怀疑/确信 → 验证专注 → 结果 → 理解/认可 → 新行动`

## R1 Reveal
`未知/好奇 → 线索 → 注意力集中 → Reveal后惊讶/恍然 → 新判断`

## R1 Surprise
`正常状态 → 短促强/轻惊讶（按事件定强度） → 快速恢复 → 按结果行动`

## R2 True Reversal
`旧判断可信 → Evidence强化旧判断 → Micro Anomaly停顿/转视线 → Reveal → Shock/Verify → 认知重置 → Aftermath行动`

Micro Anomaly前不得通过表情提前泄底。

---

# 9. CAMERA × EMOTION HANDOFF｜运镜必须跟情绪走

Performance负责给Camera提供情绪意图，但不越权破坏轴线/产品操作。

### TENSION / CONFLICT 3–4/5
优先可用：
- 轻手持呼吸感
- 快速小幅推近
- 短促甩镜反打
- 更近景别
- 事件发生后迅速重构图

目的：制造不稳定、逼近和压力。

### DELAY / WAITING 2–3/5
优先：
- 镜头突然稳定
- Hold 0.3–0.8秒
- 缓慢微推
- 让环境声/BGM退后

目的：让“突然安静”本身成为节奏反差。

### REVEAL / BURST 4–5/5
优先：
- 突然硬切
- 由局部猛地打开到完整全身/完整结果
- Full Reveal后停0.3–0.6秒让结果成立

### STRONG REACTION 4–5/5
优先：
- 硬切近景/特写
- 很短的快速微推近
- 不使用长时间环绕

### RELIEF / PAYOFF 2–4/5
优先：
- 摄影机逐渐稳定
- 构图变宽/变松
- 人物呼气、肩膀下降

核心：
`EMOTION TIGHTENS → CAMERA TIGHTENS`

`DELAY STABILIZES`

`REVEAL OPENS / HITS`

`RESOLUTION STABILIZES`

Camera仍服从180°轴线、Scene Staging与Actor Operability。

---

# 10. Scene Performance Modulation

若调用特殊Scene，强度与社会传播服从Scene DNA：
- S01 宫廷：克制权威、等级链
- S02 高中：同伴快速扩散
- S03 军营：结果→Commander→新命令
- S04 办公室：职业控制，压力来自任务
- S05 西部：身体停顿/长静
- S06 Gala：停杯/侧目/笑容轻僵
- S07 Mall：停步/重新拿起
- S08 Future：系统异常→人工复核
- S09 Diner：手继续、眼睛先偷听
- S10 Competition：Result先于Emotion
- S11 Market：拿/掂/靠近体现改判
- S12 Train：礼貌克制、整理衣服/轻点头

Scene Performance不能改Story事实或R-level。

---

# 11. 镜头与表情匹配

- 大全景：姿态、停步、转身、站位
- 中景：视线、头部、嘴角、肩颈
- 中近景/近景：关键眉眼/嘴部
- 特写：Proof Reaction、Micro Anomaly、Reveal后认知变化

镜头看不清的表情不要写。

关键4–5/5 Reaction若必须被观众读懂，优先主动给近景/特写预算。

---

# 12. 对白与表演同步

默认：
`先看到/听到 → 先Reaction → 再说话`

长台词不能覆盖关键Reaction停顿。

Punchline / 决策句：
`动作/结果 → 0.2–0.8秒停顿 → 短句 → 对方Reaction`

对白本身也要有动作能量。冲突句优先短、犀利、单意图，不用礼貌解释稀释张力。

若台词需要精确锁定，交给 `prompt-attention-compiler.md` 的Speaker + Exact Line规则，不在本文件重复堆提示。

## 12.1 Audio / Hearing Causality｜听见也必须有物理原因

每句关键对白内部锁：

```text
SPEAKER LOCATION:
ON/OFF SCREEN:
DISTANCE:
DIRECTION:
RELATIVE LOUDNESS / ROOM FEEL:
LISTENER HEARING CONDITION:
```

画外音通过较弱直接声、空间反射、方位感表达距离。

人物佩戴耳机、隔着门/玻璃或处于高噪环境时，先问：
> **她为什么能听见这句话？**

合法原因如：摘下一只/两只耳机、靠近合理距离、真实Transparency功能明确开启、视觉手势获得信息。

不能因为后面需要回答，就自动让人物清楚听见。

---

# 13. Seedance最终提示词写法

AU编号只内部使用，最终写自然动作。

错误：
`她越来越紧张，情绪升级。`

正确：
`她猛地看向门口，眉心压紧，嘴唇抿住；第二声门铃响起时立刻转头，身体向门口逼近半步。`

错误：
`她很震撼。`

正确：
`她眼神猛地锁住完整结果，双眉突然抬高，眼睛瞬间睁大，下颌松开，身体冻结0.4秒；随后眉心重新收紧，从上到下快速复核产品。`

错误：
`她用余光看同事，形成干幽默。`

改为可读动作：
`同事刚要开口，她不看他，只突然抬起食指示意“等一下”；同事立即停住。`

**动作关系 > 含混态度词。**

---

# 14. Silent Performance QA

- [ ] 每个关键Reaction都有明确Trigger。
- [ ] 每个关键Beat已设1–5强度，不再全片统一“克制”。
- [ ] 冲突/Reveal需要强度时，是否被“高级/自然”错误压平？
- [ ] 表情没有领先事件泄底。
- [ ] 表情与景别匹配，4–5/5 Reaction有足够近景预算。
- [ ] Reaction有前态→转折→后态，而不是静态表情贴纸。
- [ ] 主动作/Proof没有被表情抢走。
- [ ] Decision Change落到行动。
- [ ] 普通商用张力没有变成主角持续负面人格。
- [ ] 高压Beat是否使用少量明确高能动词，而不是抽象“情绪更强”？
- [ ] Camera Handoff是否与情绪一致：冲突更紧/手持，Delay稳定，Reveal Hit，Payoff稳定？
- [ ] R0没有被偷偷制造反转。
- [ ] R1没有演成R2。
- [ ] R2在Micro Anomaly前没有泄底。
- [ ] Scene表演方式符合Scene DNA。
- [ ] 多人Reaction有先后。
- [ ] 每句关键画外音有位置/距离/方向/空间感。
- [ ] 人物佩戴耳机/隔门时，听见外部对白有合理原因。
- [ ] 高风险内容不靠表情暗示未证明结论。

失败时：
> 先重设Beat强度、Trigger、状态过渡和Camera Handoff；再删无效态度词。不用“更激动/更震惊”这种空补丁。

---

# 15. 最终原则

`事件先发生，表情后发生。`

`QUIET PERFORMANCE ≠ FLAT EMOTION.`

`STRONG REACTION ≠ LONG REACTION.`

`TENSION SOURCE ≠ PROTAGONIST NEGATIVITY.`

`Gaze before generic emotion label.`

`Reaction必须改变下一动作，才值得占时间。`

`EMOTION TIGHTENS → CAMERA TIGHTENS.`

`DELAY STABILIZES → REVEAL HITS.`

`动作关系 > 含混情绪表演。`

`FACS是动作词典，不是情绪真相机器。`
