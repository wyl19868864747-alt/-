# PHYSICAL LOGIC DNA｜真实世界物理逻辑与状态转换库

> 来源：真实Seedance Benchmark中反复出现的漂浮、无动力运动、产品朝向重置、开闭状态跳变、数量复制、穿模与隐藏状态变化。
>
> 目标：不再按单条视频追加“禁止XX”，而是在写镜头前先建立真实世界状态，再把每次变化编译成有原因的状态转换。

---

# 0. 模块权限

本模块只负责：
- 重力与支撑；
- 动力来源；
- 实体接触/不穿透；
- 物体数量、位置与开闭状态守恒；
- 产品/道具朝向连续；
- 容器与边界；
- 铰链/轨道/关节运动；
- 人体可达性；
- 运动路径；
- 原因→动作→结果的物理先后。

本模块不负责：
- 180°轴线与机位半区：归Camera Grammar；
- 表情：归Performance/FACS；
- 外观/材质/SKU：归Product Lock；
- 声音距离/遮挡：归Audio Causality；
- “摄影机”被生成进画面：归Meta-Camera Guard。

核心原则：

`BUILD STATE FIRST → CHANGE STATE WITH CAUSE → THEN WRITE SHOT`

---

# 1. 两种物理模式

## REALITY MODE｜默认剧情段

剧情主体默认严格遵守现实世界：
- 重力；
- 支撑；
- 接触；
- 动力；
- 路径；
- 状态；
- 数量；
- 真实机械结构。

如果一个物体的状态无法解释“为什么现在会这样”，先修状态，不靠负面词硬压。

## STYLIZED COMMERCIAL MODE｜明确商业Hero/CTA

只在明确的Hero Shot、CTA、产品奇观镜头中允许：
- 轻微悬浮；
- 非现实环绕；
- 产品拆解展示；
- 空间简化/纯商业背景。

即使进入STYLIZED COMMERCIAL MODE，仍不得破坏：
- SKU；
- 产品结构；
- 配件数量；
- Reference Product Lock。

`CTA可以打破重力，不可以让产品复制或变种。`

---

# 2. SUPPORT DNA｜支撑与重力

LAW：
任何REALITY MODE中的静止物体都必须有合理支撑，且支撑方式符合重心与接触面。

CHECK：
> 受到重力时，什么东西支撑它？

VALID：
桌面 / 地面 / 手掌 / 挂钩 / 固定件 / 容器 / 机械结构。

FAIL：
悬浮、无支撑倾斜、不合理直立、只有一个无法维持重心的微小接触点。

COMPILER：
`物体位置 + 接触面 + 支撑源 + 稳定状态`

例：
`充电盒平放在桌面，底面完整接触桌面，稳定不倾斜。`

---

# 3. MOTIVE FORCE DNA｜动力来源

LAW：
任何显著位移或运动都必须能回答“谁/什么让它动”。

合法动力：
- 人推 / 拉 / 拿 / 放；
- 重力；
- 惯性；
- 风 / 水流；
- 电机 / 车辆动力 / 机器人底盘；
- 弹簧 / 合理机械机构；
- 可见碰撞。

FAIL：
普通手推车、门、椅子、箱子、杯子等无动力自行运动。

内部状态：
```text
MOVING OBJECT:
MOTIVE FORCE:
VISIBLE AGENT / MOTOR:
START:
PATH:
END:
```

---

# 4. SOLID CONTACT DNA｜实体接触与不穿透

LAW：
实体接触必须经历可理解的空间路径；两个实体不能无因互相穿透或融合。

默认动作链：
`接近 → 接触 → 受力/抓取 → 物体响应 → 分离或保持接触`

覆盖：
- 手×产品；
- 人×门/桌；
- 耳机×耳朵；
- 盒盖×盒体；
- 多人递物；
- 产品×容器。

精细接触过载时：
优先动作匹配切、降低一次接触复杂度，不堆负面词。

---

# 5. STATE CONSERVATION DNA｜状态与数量守恒

LAW：
上一镜已经建立的数量、位置、开闭、佩戴/未佩戴、手持/桌面、容器内/外状态，必须被下一镜继承，除非存在动作原因或明确Match Cut。

公式：
`STATE BEFORE → 动作/合法Match Cut → STATE AFTER`

禁止：
- OPEN → CUT → CLOSED，无关盒动作；
- 耳朵已有一对耳机，盒内又出现同一对；
- 手中产品无动作瞬间回到桌面；
- 配件数量凭空增加/减少。

Object State Ledger适用于成对/多件物体。

---

# 6. ORIENTATION DNA｜正反面与朝向连续

LAW：
切镜只改变观察角度，不自动改变物体自身朝向。

若朝向真的变化：
`ORIENTATION BEFORE → 人物/机械作用 → 可见或明确旋转 → ORIENTATION AFTER`

禁止：
`镜头A产品正面朝人物 → CUT → 镜头B产品正面又自动朝镜头`

关键物体内部记录：
```text
FRONT FACES:
BACK / HINGE FACES:
LEFT / RIGHT:
ORIENTATION CHANGE CAUSE:
```

---

# 7. CONTAINMENT DNA｜容器、开口与边界

LAW：
物体进入/离开容器或封闭空间，必须通过真实开口或合法结构。

覆盖：
盒子、包装、包、抽屉、门、杯子、车厢、柜体、瓶子。

禁止：
- 产品穿过关闭包装；
- 人穿过关闭门；
- 内容物穿过密封壁；
- 未打开容器就出现内部物体转移。

---

# 8. ARTICULATION DNA｜铰链、轨道与结构运动

LAW：
机械结构只能沿其真实自由度运动。

例：
- 盒盖围绕铰链旋转；
- 抽屉沿轨道平移；
- 门围绕门轴旋转；
- 笔记本围绕屏幕铰链打开。

禁止：
盒盖整体漂起、抽屉斜穿柜体、门脱离门框移动。

COMPILER：
`固定结构 + 运动关节/轨道 + 受力方向 + 终点状态`

---

# 9. HUMAN REACH DNA｜人体可达性

LAW：
人物必须从当前站位、身体方向和真实手臂范围内到达目标。

CHECK：
- 人离产品多远？
- 身体是否朝向目标？
- 手是否有连续路径？
- 是否需要先靠近/转身？

正确：
`靠近 → 伸手 → 接触 → 产品特写`

错误：
人物上一镜在远处，下一特写突然出现无来源的手。

---

# 10. PATH CONTINUITY DNA｜运动路径连续

LAW：
人物、手、车辆、推车、产品从起点到终点必须存在连续、合理、无穿透的路径。

切镜可以省略路径中间部分，但不能改变：
- 出发方向；
- 所在空间；
- 入口/出口；
- 左右关系；
- 终点的可达性。

复杂移动空间优先建立Path Ledger。

---

# 11. CAUSE → EFFECT DNA｜物理因果先后

LAW：
结果不能领先原因。

统一链：
`原因/Cue → 人物或物体动作 → 接触/作用 → 状态变化 → 可见结果 → Reaction`

禁止：
- 盒子先开，人后伸手；
- 产品效果先发生，产品后介入；
- 人先Reaction，后看到结果；
- 物体先移动，动力源后出现。

这是Physical Logic与Performance/FACS的交界：
**Physical Event先成立，Reaction随后。**

---

# 12. PHYSICAL STATE CARD｜关键互动前静默建立

关键人物×产品/道具互动至少判断：

```text
OBJECT:
POSITION:
SUPPORT:
ORIENTATION:
STATE:
QUANTITY:
CONTAINER / BOUNDARY:
MOTIVE FORCE:
HUMAN REACH:
PATH:
NEXT ACTION:
STATE AFTER:
```

只有高风险/关键互动需要完整Card；普通无关背景不机械展开。

---

# 13. PHYSICAL LOGIC ROUTER｜按动作加载，不全塞Prompt

不同动作调用不同DNA：

- 拿起产品：SUPPORT + HUMAN_REACH + SOLID_CONTACT + STATE_CONSERVATION
- 开盒/开盖：SUPPORT + ORIENTATION + ARTICULATION + SOLID_CONTACT + STATE_CONSERVATION
- 取出/放回：CONTAINMENT + SOLID_CONTACT + STATE_CONSERVATION + HUMAN_REACH
- 推车/车辆：MOTIVE_FORCE + PATH_CONTINUITY + SOLID_CONTACT
- 倒液体：SUPPORT + MOTIVE_FORCE/GRAVITY + CONTAINMENT + PATH
- 穿戴：HUMAN_REACH + SOLID_CONTACT + STATE_CONSERVATION
- 门/抽屉：ARTICULATION + CONTAINMENT + SOLID_CONTACT + STATE_CONSERVATION

最终Seedance提示词只输出当前动作真正需要的可见状态约束，不把整个DNA库背给模型。

---

# 14. PROOF ISOLATION｜控制变量，不让环境替产品作弊

这是商业Proof与物理状态的联合Gate。

LAW：
当广告用Before/After证明某个Benefit时，除产品介入外，其他会解释结果的关键变量应保持不变。

正确：
`同一环境A + 未用产品 → 问题明显`
`同一环境A + 用产品 → 结果改变`

错误：
`环境A + 未用产品`
→ `环境B + 用产品`

如果环境、人物位置、光线、噪音源、任务难度等同时发生有利变化，Proof被污染。

内部检查：
```text
PROOF VARIABLE:
CONTROLLED VARIABLES:
WHAT CHANGED:
CAN RESULT BE EXPLAINED WITHOUT PRODUCT: YES / NO
```

若YES，重新设计Proof。

---

# 15. FAILURE PATTERN映射

- GF16 小物体精细取放穿模 → SOLID_CONTACT / CONTAINMENT
- GF22 成对物体复制/瞬移 → STATE_CONSERVATION
- GF27 普通道具无动力移动 → MOTIVE_FORCE
- 新：无支撑悬浮/不合理直立 → SUPPORT
- 新：切镜产品自动转正 → ORIENTATION
- 新：OPEN/CLOSED隐藏跳变 → STATE_CONSERVATION
- 新：Proof前后环境一起变化 → PROOF_ISOLATION

180°越轴继续归Camera Grammar，不并入Physical DNA。
Meta-camera Literalization继续归Meta-Camera Guard。

---

# 16. PHYSICAL LOGIC QA｜输出前静默检查

- [ ] 所有关键静止物体有合理支撑与重心
- [ ] 所有显著移动有动力来源
- [ ] 接触前有路径，实体不互相穿透
- [ ] 数量、位置、开闭、佩戴/收纳状态跨镜守恒
- [ ] 产品/道具朝向没有因切镜自动重置
- [ ] 容器进出通过真实开口
- [ ] 铰链/轨道/关节沿真实结构运动
- [ ] 人物从当前站位真实够得到目标
- [ ] 起点→路径→终点连续可达
- [ ] 原因先于动作，动作先于结果，结果先于Reaction
- [ ] Before/After没有同时改变会污染Proof的关键变量
- [ ] REALITY MODE与STYLIZED COMMERCIAL MODE边界清楚

失败时先重建状态/路径/动作，不先追加“不要漂浮/不要穿模/不要瞬移”的负面词串。
