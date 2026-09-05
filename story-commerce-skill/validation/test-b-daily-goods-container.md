# TEST B｜30秒日用品 / 容器 × 3.4.2 最终回归

STATUS: `READY_TO_RUN`

MODEL TARGET: Seedance 2.5
DURATION: 30s
ASSET MODE: TEXT_ONLY BENCHMARK

## 1. Benchmark SKU
透明玻璃沙拉酱摇摇瓶：直筒透明玻璃瓶身，哑光黑色旋拧主盖，主盖顶部带一个小型翻盖倒液口。全片只允许1个瓶体、1个主盖、1个翻盖。

本轮只验证可见流程：
`分层液体已在瓶内 → 密闭摇匀 → 停止 → 打开倒液口 → 倾斜倒出 → 回正 → 关闭倒液口`

不宣称：绝对防漏、精确刻度、耐热、材质认证、长期耐用、固定容量。

## 2. Commercial Focus
Core Decision Question：一个容器能否把已经分层的沙拉酱直接摇匀，并从同一瓶中完成上桌倒取？
Best Proof：透明瓶内分层状态 → 摇匀后的视觉状态变化 → 连续液体流从真实开口进入沙拉 → 瓶内剩余液体继续被容器承载。
Architecture：SA02 Demonstration → Evidence → Decision。
R-level：R1 Surprise / Proof Payoff，默认不强造R2。
Route：DIRECT PRODUCT。

## 3. 3.4.2 本轮重点
- 强Hook但不靠长对白；
- Dialogue Lock；
- 情绪强度与FACS真正进入最终镜头；
- Conflict手持 / Delay稳定 / Pour Burst / Payoff稳定；
- Product Pivot后产品接管；
- Audio Event Map；
- Scene Staging避免元素组合语义错误；
- SUPPORT / CONTAINMENT / ARTICULATION / PATH / STATE CONSERVATION / CAUSE_EFFECT；
- Prompt Attention：一Beat一个主事件，不重复Hard Rules。

## 4. Pass Gate
- 0–6s冲突不平；
- 对白Speaker与台词稳定；
- 关键Reaction强度可读；
- 摇动由人物手提供动力；
- 主盖不自动消失；
- 翻盖先打开，液体才倒出；
- 液体只从真实倒液口流出，不穿壁；
- 倾斜方向与重力一致；
- 瓶回正后主液流停止；
- 剩余液体仍在瓶内；
- 30s后半由产品Proof主导，不回到电视短剧；
- CTA为无文字Product Hero。

若本条总体达到PASS/PARTIAL-ACCEPTED且无结构性新故障，则剧情带货Skill进入上架候选阶段；后续只补文本压力测试、Registry与冷启动测试。