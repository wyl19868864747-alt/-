# STYLE REGRESSION｜REAL GENERATION EVIDENCE V1

状态：`ST01 REAL GENERATION = PARTIAL PASS｜ST02/ST05 PENDING`

目的：记录 Style Lock 4.1 的真实 Seedance 成片证据。与 `style-regression-v1.md` 的 Prompt-level 回归分开记录，避免把文字测试误当真实模型能力。

---

## TEST 1｜ST01 美式原生手机实拍风

### Fixture
- 15s
- 透明玻璃沙拉酱摇摇瓶
- 现代住宅厨房
- 同一核心 Proof：清晰分层 → 关闭状态摇匀 → 均匀结果 → 打开顶部小翻盖 → 倒入沙拉 → 收尾
- 目标 Style：ST01 美式原生手机实拍风

### 真实成片判断

**STYLE EXECUTION：PASS**
- 第一眼具有明确竖屏手机实拍/美国生活内容感；
- 自然窗光、真实住宅厨房、自然肤色成立；
- 镜头近距离、轻手持、不过度电影调色；
- 没有漂移成静奢棚拍或电影大片。

**PROOF READABILITY：PASS**
- 开场金黄色油层与深色醋液层边界非常清楚；
- 摇动后变成均匀液体，Before/After明显；
- 后段真实倾斜并向沙拉连续倒液，核心商业 Proof 可读。

**PRODUCT / PHYSICAL STATE：PARTIAL**
- 摇动阶段约2–3s出现疑似额外细长内部杆/管状结构，产品结构发生短暂漂移；
- 后续黑色主盖与顶部翻盖结构恢复正常；
- 收尾时顶部翻盖未可靠回到关闭状态。

### Root Cause 初判
`MODEL / RANDOM PRODUCT-STRUCTURE DRIFT`，不是 Style Router 结构失败。
原因：原Prompt已经明确限制单瓶、单主盖、单翻盖以及关闭后摇动；本轮问题集中于生成阶段的局部结构漂移。

### 本轮不晋升为母版新规则
不因为一次生成继续增加大段负面提示。下一条测试只做最小正向状态强化：
- 摇动阶段明确“瓶内只有液体，无额外内部机构”；
- `CLOSED SHAKE STATE → OPEN POUR STATE → CLOSED END STATE` 三段状态写清楚。

### 结论
ST01 作为前台独立视觉Style已经获得真实视频证据：**视觉风格PASS**。
整条生成登记为 **PARTIAL PASS**，因为产品结构/翻盖最终状态存在局部失败。

下一步：保持同产品、同Proof、同地点与时长，切换 ST02 高端静奢广告风，验证真实成片视觉距离。
