# TEST B｜30秒日用品 / 容器 × 3.4.2 最终回归

STATUS: `PASS / ACCEPTED`

DATE: 2026-09-05
MODEL: Seedance 2.5
DURATION: 30s
ASSET MODE: TEXT_ONLY BENCHMARK

## 1. Benchmark SKU
透明玻璃沙拉酱摇摇瓶：直筒透明玻璃瓶身，哑光黑色旋拧主盖，主盖顶部带一个小型翻盖倒液口。全片只允许1个瓶体、1个主盖、1个翻盖。

测试链：
`液体在瓶内 → 人手摇动 → 停止 → 打开倒液口 → 倾斜倒出 → 回正 → 主液流停止 → 关闭倒液口`

不宣称：绝对防漏、精确刻度、耐热、材质认证、长期耐用、固定容量。

## 2. Commercial Focus
Core Decision Question：一个容器能否在同一瓶内完成摇匀并直接完成上桌倒取？
Architecture：SA02 Demonstration → Evidence → Decision。
R-level：R1 Surprise / Proof Payoff，不强造R2。
Route：DIRECT PRODUCT。

## 3. 实际结果

### 30秒买量节奏：PASS
0–6秒冲突清楚；约8秒后产品开始接管；后半主要由摇匀、开盖、倒液、结果与Reaction组成，没有重新掉回电视短片。

### Dialogue / Performance：PASS
对白负载明显降低，Speaker稳定；开场压力与21–24秒Reaction都可读。

### FACS：PASS
关键Reaction实际呈现出：
`Visible Result → Shock → Verify → Accept`。
强Reaction已经从“概念规则”变成真实可生成动作链。

### Camera × Emotion：PASS
冲突段更有轻手持与收紧感；Delay段明显稳定；倒液Proof后重新释放；Payoff趋于稳定。

### Audio Event Map：PASS
Hook、对白让位、Delay降能、倒液Reveal与后半Proof节奏存在明显分段，不是一条BGM平铺到底。

### Physical Logic：PASS
- 摇动动力来自人物双手；
- 翻盖先打开，液体再流出；
- 液体通过真实开口进入沙拉；
- 未见明显穿壁；
- 倾斜与重力方向一致；
- 回正后主液流停止；
- 瓶内保留剩余液体；
- 瓶体/主盖/翻盖没有结构性复制或消失。

### Product Takeover：PASS
产品在中后段成为视觉与剧情主角，人物只负责触发、验证和Reaction。

### CTA：PASS
结尾为干净Product Hero，无生成CTA文字。

## 4. 唯一非阻断缺口｜Mixing Proof可视化不足

原计划希望：
`明显分层 → 摇动 → 明显混合`

成片中的液体从开场就偏均匀、不透明，因此“摇匀前后差异”不够可读。

判定：
- ACTION：PASS
- PHYSICS：PASS
- MIXING BEFORE/AFTER PROOF：PARTIAL

根因不是导演引擎失效，而是Proof Fixture本身不够视觉化：不透明奶油型沙拉酱不适合证明明显“分层→混合”。

未来若测试Shake→Mix，优先使用：
`透明金黄色油层 + 深色醋/香料液体层`的vinaigrette，使Before/After状态天然可读。

抽象经验：
> **在设计Proof之前，先确认被证明的状态在画面里真的可见。**

`VISIBLE STATE DIFFERENCE > THEORETICAL PROOF`

## 5. 最终结论

TEST B整体通过，不需要为了Mixing可视化缺口重新生成。

本条提供真实证据：
- 30s Product-Centered Narrative可执行；
- Prompt Attention压缩有效；
- FACS强Reaction可执行；
- Camera × Emotion可执行；
- Audio Event Map可执行；
- 容器/开合/液体/重力/Containment/State Conservation可执行；
- Product Takeover稳定；
- CTA无文字Hero稳定。

FINAL STATUS: `PASS / ACCEPTED`

NEXT ACTION:
- 不再追加容器视频测试；
- 进入Registry收口与最终冷启动测试。