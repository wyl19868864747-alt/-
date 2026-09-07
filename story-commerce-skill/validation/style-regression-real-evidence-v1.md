# STYLE REGRESSION REAL EVIDENCE V1

状态：`IN PROGRESS`

目标：记录 Style Lock 的真实 Seedance 生成证据。与 `style-regression-v1.md` 的 Prompt-level 结果分开，只有真实成片才登记在这里。

## TEST 1｜ST01 美式原生手机实拍风

真实生成：PASS / ACCEPTED WITH MINOR PRODUCT-STATE NOTES

结论：
- STYLE RECOGNITION：PASS。第一眼为真实美国社媒/手机实拍感，自然窗光、近距离轻手持、生活化厨房成立。
- VISUAL DISTANCE BASELINE：PASS。可作为后续风格对照基线。
- PROOF：PASS。分层 → 摇动 → 明显趋于均匀 → 真实翻盖倒液的商业因果可读。
- PRODUCT STATE：PARTIAL。摇动中曾短暂出现疑似额外细长内部结构；结尾翻盖状态需要更稳定。

不因单次产品结构漂移改写整个 Style DNA；后续用最小状态锁处理。

## TEST 2｜ST02 高端静奢广告风｜Attempt 1

真实生成：PARTIAL / STYLE PASS, PROOF FAIL

结论：
- STYLE RECOGNITION：PASS。低饱和米白/深木体系、稳定镜头、微距、留白、材质高光明显成立。
- VISUAL DISTANCE VS ST01：STRONG PASS。同产品同厨房条件下，第一眼已经从“真实手机内容”切换为“高端品牌 Campaign”。
- PRODUCT / POUR PHYSICS：PASS。真实翻盖开口与连续倒液基本成立，结尾翻盖回到关闭状态。
- MIXING PROOF：FAIL。摇动后仍保留明显金黄色上层，未真正完成 `清晰分层 → 均匀状态`，因此核心 Best Proof 未闭环。

### Root cause
当前静奢视觉语言把“稳定、克制、慢”传递到了人物产品操作，导致摇动幅度和状态变化不够强；Style 没有错，但 Style 的动作气质抢了 Proof 的执行强度。

### Transferable rule
`STYLE MAY CONTROL CAMERA ENERGY, NOT REQUIRED PRODUCT ACTION AMPLITUDE.`

中文：
> 风格可以控制镜头有多安静，但不能把完成 Proof 所需的产品动作一起弱化。

静奢、日系、Noir 等低能量视觉风格中，只要 Best Proof 需要明确物理动作：
- 镜头可以稳定、慢、克制；
- 人物表情可以克制；
- 但产品操作必须达到完成状态变化所需的真实幅度、速度和持续时间；
- Proof 完成后再恢复风格节奏。

## TEST 2｜ST02 高端静奢广告风｜Attempt 2 最小重测

真实生成：PASS / ACCEPTED

本次只强化产品操作幅度与 Proof 状态闭环，未改 Style、产品、地点、Core Decision 或 Best Proof。

结论：
- STYLE RECOGNITION：PASS。静奢视觉仍稳定成立：低饱和米白体系、整洁厨房、稳定构图、微距材质观察和克制节奏均未因动作强化而丢失。
- VISUAL DISTANCE VS ST01：STRONG PASS。与 ST01 美式原生手机实拍保持显著视觉距离。
- ACTION AMPLITUDE：PASS。摇瓶动作明显加强，连续且有足够幅度，没有被“静奢=轻动作”再次削弱。
- MIXING PROOF：PASS。开场金黄色油层与深色醋汁分界清楚；摇动过程中两层持续卷入并逐渐融合；约 6s 后原水平分层消失，近景中液体整体成为一致棕金色状态。
- POST-POUR STATE：PASS。倒液后瓶内上方出现的是正常液位下降后的空气头部空间，不是油层重新分离。
- POUR PHYSICS：PASS。顶部翻盖开启后从真实开口连续倒液，液流方向自然。
- END STATE：PASS。倒液后瓶身回正并执行翻盖关闭动作；产品 Hero 保持单瓶、结构稳定。

### 回归结论
这次证明：
`QUIET CAMERA / PREMIUM STYLE` 与 `FULL-STRENGTH PRODUCT ACTION` 可以同时成立。

因此保留可迁移规则：
`STYLE MAY CONTROL CAMERA ENERGY, NOT REQUIRED PRODUCT ACTION AMPLITUDE.`

不再继续测试该容器 / ST02 组合。

## 下一步
进入 TEST 3：`用户真实产品 + 用户提供的一个核心卖点 × ST05 超现实创意广告风`。

目的不是再验证容器，而是验证：
1. 强 Style 是否能迁移到真实用户商品；
2. 超现实奇观是否可以围绕真实卖点建立，而不篡改产品事实；
3. Style 强度提高后，Product Truth / Best Proof / Product Lock 是否仍能保持。

输入只需要：
- 用户真实产品图片；
- 一个已确认、最核心的卖点。
