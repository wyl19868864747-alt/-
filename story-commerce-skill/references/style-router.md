# STYLE ROUTER｜商业上架风格锁定路由 V1.1

> 目标：把前台用户选择的视觉风格稳定传入广告导演链，而不是把风格误解成固定场景。

核心：
`USER STYLE CHOICE = HARD STYLE LOCK`
`STYLE ≠ LOCATION`
`STYLE ≠ STORY TEMPLATE`
`PRODUCT TRUTH / BEST PROOF > STYLE`

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

`Style Lock → Location Router → Scene Staging → Performance → Camera/Light → Prompt Compile`

因此Style可以改变“怎么拍”，不能改变“卖什么、证明什么、发生什么核心事件”。

### ST05 专项路由

当 `STYLE ID = ST05 超现实创意广告风` 时，在进入 Location / Staging / Camera 前必须额外读取：

- `references/surreal-visual-compiler.md`

ST05不得只靠光带、粒子、雾、颜色变化制造“超现实”。必须先通过该模块完成：

`产品语义来源 → 相关原料/材质 → 唯一奇观机制 → 0.1–0.5s真实蓄力 → 不可能尺度/空间变化 → 同一事件多机位覆盖 → 卖点回收 → 产品回收`

固定：
`PRODUCT SEMANTICS BEFORE SPECTACLE`
`ONE EVENT, MANY ANGLES`
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
COMPRESSED STYLE LINE: 1句
```

不要把整张Style DNA继续传给下游。

ST05除上述Style Card外，再由 `surreal-visual-compiler.md` 生成一个最小Surreal Card，但同样不能把模块全文复制进最终Prompt。

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
- ST05禁止使用与产品原料、材质、颜色、品类认知或卖点没有关系的随机视觉元素充当主奇观。

最终原则：

> **用户锁风格，Skill锁商业正确性，Location负责找到能让两者同时成立的具体空间。**