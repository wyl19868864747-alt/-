# ENGLISH PROMOTIONAL VOICEOVER｜英文宣传旁白编译器 V1

> 目标：避免产品广告只有画面和音乐、缺少品牌/卖点表达而显得“干”。在用户没有提供完整旁白时，根据已确认产品特征与卖点，自动生成一条贯穿关键段落的英文宣传旁白。

---

## 0. 核心原则

`VOICEOVER MUST COME FROM CONFIRMED PRODUCT TRUTH`

`ENGLISH BY DEFAULT`

`VOICEOVER THREADS THROUGH THE FILM, IT DOES NOT EXPLAIN EVERY SHOT`

`SELLING POINT > EMPTY POETRY`

`NO NEW CLAIMS`

旁白的任务是：
- 把产品身份和卖点说清；
- 给画面一个商业“主线”；
- 在关键视觉/Proof之间形成连续感；
- 让广告听起来完整，而不是只有BGM与SFX。

---

## 1. 什么时候自动生成

如果用户没有明确要求“无旁白”，且没有提供一套完整可用的Voiceover：

> 默认生成英文宣传旁白。

如果广告本身有角色对白：
- 不取消角色对白；
- Voiceover只进入无关键对白的窗口；
- 不和Punchline、价格、资格、核心事实对白抢权重。

如果用户明确要求纯音乐、无旁白或无口播，则关闭本模块。

---

## 2. 旁白从什么信息生成

只允许使用：
- 产品名称 / 品类；
- 用户确认的产品特征；
- 用户确认的核心卖点；
- 已确认的真实功能/结果；
- 已确认品牌调性；
- 已确认CTA。

禁止自行增加：
- 最好 / 第一 / No.1；
- 医学或健康结论；
- 精确数据；
- 功效时长；
- 竞品比较；
- 保证性表达；
- 未确认成分/材料/产地。

如果产品事实不足，旁白只能使用更保守的感官/体验表达，不能补事实。

---

## 3. 旁白结构｜不是一整段念到底

默认形成一个 `VOICEOVER THREAD`：

`HOOK / PRODUCT IDENTITY`
→ `SELLING-POINT SETUP`
→ `PROOF / SPECTACLE PAYOFF`
→ `BRAND / CTA CLOSE`

15秒广告通常：
- 2–4个短语义段；
- 总英文词数约12–28词；
- 每段尽量3–9个词；
- 留出足够空间给动作、Reaction、SFX和音乐。

30秒广告通常：
- 3–6个短语义段；
- 总英文词数约25–50词；
- 不追求旁白占满每一秒。

“贯穿视频”指在前、中、后关键节点持续出现，而不是无停顿念满全片。

---

## 4. 写法

优先：
- 短句；
- 有广告记忆点；
- 与视觉卖点同方向；
- 可自然拆成多段；
- 英语母语广告语感。

避免：
- 说明书口吻；
- 把画面逐帧描述出来；
- 长句；
- 过度文艺但不知道卖什么；
- 与屏幕文案完全重复；
- 每句都以产品名开头。

旁白可采用：
- `Product truth → sensory payoff`
- `Problem tension → benefit release`
- `Short campaign line → proof phrase → closing slogan`

---

## 5. 旁白与画面关系

旁白必须服务当前Beat，而不是独立存在。

例如视觉正在做产品Proof：
> 旁白说结果/价值，不要重复动作描述。

视觉正在做超现实奇观：
> 旁白要解释卖点含义，不要解释“现在一片巨大的叶子出现了”。

视觉正在做产品Hero：
> 旁白收成品牌句或卖点句，形成商业落点。

固定：
`SHOW THE EVENT, SAY THE VALUE`

---

## 6. ST05超现实广告旁白

当命中ST05时，旁白不能负责“修正一个错误奇观”。

先通过 `surreal-spectacle-decision-gate.md`，保证关掉声音后奇观本身已经能正确指向卖点；旁白只做强化。

例如伯牙绝弦，用户确认卖点：
`清爽不腻，茶底扎实`

可形成类似：

```text
“Tea that comes through.”
“Smooth, light, never heavy.”
“Boya Juexian — tea at the core, freshness in every sip.”
```

这是表达示意，不是固定品牌官方文案；若品牌已有官方英文文案，用户提供后以官方内容为最高优先级。

---

## 7. 与角色对白的冲突处理

优先级：
`用户指定Exact Dialogue > 关键角色对白 > Voiceover > BGM装饰`

若一个2–4秒Beat已有关键人物台词：
- 默认不再叠Voiceover；
- 把旁白移到下一无对白窗口；
- 或压缩为结尾短句。

禁止人物对白和旁白同时抢同一事实。

---

## 8. Voiceover Card｜内部静默建立

```text
PRODUCT:
CONFIRMED SELLING POINT:
VOICEOVER PURPOSE:
VOICE STYLE:
HOOK VO:
MID VO:
PAYOFF VO:
CLOSING VO:
TOTAL WORD BUDGET:
DIALOGUE COLLISION CHECK:
UNVERIFIED CLAIM CHECK:
```

默认VOICE STYLE根据Style DNA调整语气，但不得改事实：
- UGC：自然、口语；
- 静奢：短、克制；
- 高定：锋利、少词；
- 动作：节奏强、短促；
- 超现实：有想象力但必须说清价值；
- 科技：精确、干净；
- 复古/地域风格：可调语气，不伪造历史/地域事实。

---

## 9. QA

- [ ] 用户是否明确禁止旁白？若是关闭。
- [ ] 所有旁白是否为英文？
- [ ] 是否只使用已确认产品事实与卖点？
- [ ] 是否在前/中/后形成连续商业主线，而非只结尾突然说一句？
- [ ] 是否没有把每个镜头逐字解说？
- [ ] 是否避开角色关键对白？
- [ ] 是否给SFX、Reaction和画面留空间？
- [ ] 结尾旁白是否与CTA/音频一起形成明确收束？
- [ ] 删除画面后旁白仍像这个产品，而不是万能广告套话？

最终：

> **画面负责让卖点被看见，英文旁白负责让卖点被记住。**