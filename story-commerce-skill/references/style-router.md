# STYLE ROUTER｜商业上架风格锁定路由 V1.3

> 目标：把前台用户选择的视觉风格稳定传入广告导演链，而不是把风格误解成固定场景；同时让声音设计服从Style，而不是给所有风格统一强塞英文旁白。

核心：
`USER STYLE CHOICE = HARD STYLE LOCK`
`STYLE ≠ LOCATION`
`STYLE ≠ STORY TEMPLATE`
`PRODUCT TRUTH / BEST PROOF > STYLE`
`VOICEOVER IS STYLE-CONDITIONAL`

---

## 1. 输入

优先接收前台 `style_id`：

- ST01 美式原生手机实拍风
- ST02 高端静奢广告风
- ST03 欧美高定时尚大片风
- ST04 好莱坞动作大片风
- ST05 超现实创意广告风
- ST06 未来科幻科技风
- ST07 70年代复古美式胶片风
- ST08 Y2K千禧流行风
- ST09 日系清透生活风
- ST10 地中海阳光假日风
- ST11 美式西部荒野风
- ST12 黑色电影暗黑风

如果用户明确用自然语言指定其中某个风格，也映射到对应 `style_id`。

如果没有提供任何风格选择，不追问内部参数；默认使用 `ST01 美式原生手机实拍风` 作为中性社媒基线，除非用户提供了明确参考图/视觉要求。

---

## 2. 强制规则

### 用户选择永远有效

不得因为：
- 商品品类
- 实体/虚拟产品形态
- 价格带
- 使用场景
- 传统行业习惯

而拒绝、替换或自动改掉用户已选Style。

不存在“该产品不适合这个风格，所以禁用”的前台逻辑。

### 风格通过视觉语言适配产品

如果某个Style中的典型装饰会破坏Product Truth、Proof或合规：

> 保留该Style的色彩、光影、材质、构图、镜头、成像质感；舍弃会造成事实误读的装饰。

例：
- 黑色电影风不要求犯罪剧情；
- 西部荒野风不要求牛仔/马匹；
- 未来科技风不要求虚假UI数据；
- 70年代风不允许把现代产品本体改造成复古型号；
- 超现实风不允许产品复制、变形或改变真实功能。

---

## 3. Style Lock执行顺序

Style在以下内容之后锁定：

`Product Truth → Core Decision → Story Architecture → Proof Plan → Reversal`

然后：

`Style Lock → Location Router → Scene Staging → Performance → Camera/Light → Audio / Voiceover Fit → Prompt Compile`

因此Style可以改变“怎么拍、声音怎么呈现”，不能改变“卖什么、证明什么、发生什么核心事件”。

### 3.1 Voiceover Fit｜旁白不是默认必选

进入声音设计阶段时读取：
- `references/english-promotional-voiceover.md`

规则：
- 用户明确要求无旁白：`OFF`；
- 用户明确要求旁白：`ON`；
- 用户未指定：根据Style和商业信息缺口自动决定。

特别是：
- `ST02 高端静奢广告风` 默认 `VOICEOVER OFF`，优先使用留白、材质声、环境声、极简BGM和产品Hero维持高级感；
- 其他Style不是强制ON，而是 `AUTO`；只有旁白确实提升卖点理解、产品记忆或成片完整度时才加入；
- 若人物对白已经把核心卖点讲清，不再额外叠英文宣传旁白；
- 旁白一旦使用，默认英文，并且只能来自已确认Product Truth与卖点。

固定：
`STYLE FEEL > FORCED NARRATION`
`NO VO IS A VALID DIRECTOR CHOICE`

### ST05 专项路由

当 `STYLE ID = ST05 超现实创意广告风` 时，在进入 Location / Staging / Camera 前必须按顺序额外读取：

1. `references/surreal-spectacle-decision-gate.md`
2. `references/surreal-visual-compiler.md`

先做“为什么是这个奇观”的商业决策，再做“这个奇观怎么拍”的视觉编译。

ST05不得只靠光带、粒子、雾、颜色变化制造“超现实”，也不得只因为奇观元素来自产品，就默认奇观因果正确。

必须先通过决策层完成：

`当前卖点 → 期望观众理解 → 产品相关元素 → 奇观动作/事件 → 错误联想检查 → 因果通过`

再进入视觉层：

`0.1–0.5s真实蓄力 → 真实世界内的不可能现象 → 尺度/空间冲击 → 同一事件多机位覆盖 → 卖点回收 → 产品回收`

固定：
`SPECTACLE CAUSAL MEANING > SPECTACLE BEAUTY`
`PRODUCT SEMANTICS ARE NECESSARY, NOT SUFFICIENT`
`PRODUCT SEMANTICS BEFORE SPECTACLE`
`ONE EVENT, MANY ANGLES`
`REAL + IMPOSSIBLE = SURREAL`
`SURREAL ≠ RANDOM VFX`

---

## 4. Style Card｜内部最小输出

读取 `style-dna-library.md` 后，只建立：

```text
STYLE ID:
STYLE NAME:
VISUAL ANCHORS: 2–3个
LIGHT/COLOR ANCHOR: 1个
CAMERA/TEXTURE ANCHOR: 1个
ENVIRONMENT TENDENCY: 1个非强制方向
VOICEOVER TENDENCY: OFF / AUTO / LOW DENSITY
COMPRESSED STYLE LINE: 1句
```

不要把整张Style DNA继续传给下游。

ST05除上述Style Card外，先由 `surreal-spectacle-decision-gate.md` 形成最小Spectacle Decision Card，再由 `surreal-visual-compiler.md` 生成最小Surreal Card；两者都不能把模块全文复制进最终Prompt。

---

## 5. 跨产品迁移

Style必须可作用于：
- 实体商品
- 服装/穿戴
- 家居/餐厨
- 3C/工具
- 美妆/食品
- App / SaaS / 软件
- 游戏 / 数字内容
- 订阅 / 服务

Style只负责视觉表达；产品进入方式与Proof由原商业链决定。

---

## 6. 禁止事项

- 禁止把Style名字直接当Location。
- 禁止因为用户选ST07就强制进入某个70年代固定建筑。
- 禁止因为用户选ST11就强制出现牛仔、马、枪或沙漠。
- 禁止因为用户选ST12就自动增加犯罪、危险、恐怖剧情。
- 禁止为了风格把产品外观、功能、价格或结果改写。
- 禁止同时自动混入多个一级Style。
- 禁止给所有Style统一强塞英文旁白。
- ST05禁止使用与产品原料、材质、颜色、品类认知或卖点没有关系的随机视觉元素充当主奇观。
- ST05禁止用“产品相关元素 + 与卖点相反的奇观动作”强行制造冲击，例如清爽柔和类卖点默认不用无因爆裂、破坏、震荡来表达。
- ST05禁止把真实场景整体替换成一张完整奇幻背景来冒充超现实；应优先保留真实空间锚点，让不可能现象发生在现实内部。

最终原则：

> **用户锁风格，Skill锁商业正确性，Location负责找到能让两者同时成立的具体空间，声音也必须服从风格。**