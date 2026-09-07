# LOCATION ROUTER｜风格与剧情之间的空间翻译层 V1

> 目标：用户锁定Style后，由Skill根据产品、Proof和剧情自动选择最合理的具体地点。

核心：
`STYLE DECIDES HOW IT FEELS`
`LOCATION DECIDES WHERE IT HAPPENS`
`STAGING DECIDES HOW ELEMENTS RELATE`

---

## 1. 输入

Location Router只读取已经锁定的：
- Product Truth / SKU / Reference
- Core Decision
- Best Proof
- Primary Story Architecture
- 关键人物与动作
- Duration / Platform
- Style Card

不得反向改写以上内容。

---

## 2. 选择优先级

具体地点按以下顺序选择：

1. **产品使用/理解是否自然**
2. **Best Proof是否容易看清**
3. **剧情动作是否能真实发生**
4. **人物与道具是否容易稳定调度**
5. **锁定Style是否容易通过光影、材质、服装、构图和环境细节成立**
6. 美术新鲜度

永远：
`PRODUCT / PROOF FIT > STYLE DECORATION`

但用户Style不可被取消；如果典型环境不合适，就在更合理的地点里翻译该Style。

---

## 3. Location不是Style模板

同一个Style可以对应完全不同地点。

例如 `ST02 高端静奢广告风`：
- 厨房
- 住宅
- 车内
- 办公桌
- 酒店
- 店铺
- 极简摄影空间

都可以成立，只要光影、材质、构图和镜头保持Style。

例如 `ST07 70年代复古美式胶片风`：
- 住宅
- 街道
- 餐饮空间
- 工作场所
- 公路生活环境

都可以成立；不等于“必须去70年代Diner”。

---

## 4. 不同产品形态

### 实体商品
优先选择真实可使用、可接触、可证明的空间；产品必须有真实支撑面、操作面和尺度关系。

### 穿戴 / 时尚
地点要支持上身、动作、镜面/全身或细节观察，不让环境抢掉服装归属和Reveal状态。

### 数字产品 / App / SaaS
可以使用：
- 人物 + 真实设备的生活/工作空间；
- 受控的功能可视化空间；
- 用户已提供UI/品牌资产的界面展示。

禁止用乱码或虚构数据冒充产品功能。

### 游戏 / 数字内容
可以让现实人物使用设备，也可在有真实素材支持时进入游戏/内容世界；Style控制摄影与视觉基调，不虚构不存在的玩法结果。

### 服务 / 订阅
优先通过真实任务、人物状态变化、已确认页面/品牌资产或结果情境表达；不要凭空生成实体产品。

---

## 5. Complexity Budget

默认：
- 15秒：优先1个主地点；
- 30秒：优先1个主地点，必要时最多2个有明确因果关系的地点；
- 不为Style展示而频繁跳世界。

如果多地点不能增加新Proof、状态变化或商业理解：
> 删除。

---

## 6. Location Card｜内部最小输出

```text
PRIMARY LOCATION:
WHY THIS LOCATION:
PRODUCT OPERATING SURFACE:
KEY BACKGROUND:
STYLE TRANSLATION: 用哪些环境/材质/光线支持Style
MOVEMENT CONSTRAINTS:
NEXT: Scene Staging
```

`STYLE TRANSLATION`只能说明视觉实现，不得增加剧情。

---

## 7. 与Scene Staging边界

Location Router只决定：
> 在哪里发生。

`scene-staging-compiler.md`继续决定：
> 人在哪、商品在哪、谁从哪里到哪里、前中后景是什么、机位在哪里、品牌如何出现。

Location完成后，只要涉及进出、接近/离开、跨空间或多个关键元素，必须继续进入Scene Staging。

最终：

> **不要为风格找场景；要为产品与Proof找地点，再把风格翻译进去。**