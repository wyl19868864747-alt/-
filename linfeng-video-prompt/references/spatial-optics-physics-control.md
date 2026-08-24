# 空间、光学、物理与连续状态控制层

本模块用于解决视频生成中最常见但最致命的执行错误：首帧空镜、人物左右翻转、视线错误、主体离关键地标过远、参考图职责混乱、镜头透视漂移、动作失重、光线变平、跨镜状态重置。

本模块是导演执行层，不负责替代创意判断。先确定“为什么值得拍、观众先看到什么、动作如何触发结果”，再用本模块保证这个创意被正确拍出来。

## 1. 首帧状态与镜尾状态

对需要精确控制的单镜或连续镜头，后台先建立 `First Frame State` 与 `End Frame State`。

首帧至少检查：
- 必须立即可见的主体是谁；
- 主体位于画面左/中/右、前/中/后景中的哪里；
- 身体朝向、头部朝向、视线目标分别是什么；
- 手中道具、车门、产品、家具、武器等关键物体处于什么状态；
- 主体与关键地标的真实距离或接触关系；
- 摄影机位于关系轴线哪一侧；
- 是否真的需要空镜。没有明确叙事价值时，不允许模型用空建立镜头消耗开场。

镜尾至少记录：
- 人物最终世界位置与画面位置；
- 身体、头部、视线、手部状态；
- 道具在哪只手、是否打开/关闭/破损/湿润/变形；
- 门、车辆、产品、环境效果的最终状态；
- 光线方向与主要运动方向；
- 下一镜必须继承的连续状态。

多镜头时，下一镜默认从上一镜 `End Frame State` 合理延续，不重置动作、不瞬移、不无因改变距离、手别或物体状态。

## 2. 空间 Scene Graph

在复杂人物关系、动作交互、产品演示、车辆进出、地标依赖镜头中，后台先把自然语言转成最小空间图：

`Camera → Foreground → Subject A / Subject B → Landmark / Prop → Background → Light Source`

对关键主体分别明确：
- screen position：screen-left / center / screen-right；
- world position：相对门、车、桌、路沿、树、产品或其他人物的真实位置；
- depth：foreground / midground / background；
- distance/contact：能量化时写 within 1 meter、hand on handle、back against wall、feet beside rear door 等可见锚点；
- torso direction：身体朝向；
- head direction：头部朝向；
- gaze target：眼睛看向谁或什么；
- movement vector：从哪里向哪里移动。

身体方向与视线方向分开处理。不得仅用“看着”“靠近”“在旁边”等弱关系替代关键空间关系。

## 3. 参考图职责解耦

参考素材必须先分权，不让一种参考覆盖另一种职责：

- Identity Reference：控制脸、年龄、体型、比例、服装、身份锚点；
- Location Reference：控制建筑、材质、地理关系、地标、环境气氛，除非用户明确要求，否则不自动继承原参考图机位与构图；
- Prop / Product Reference：控制形状、比例、材质、标签、状态与接触位置；
- Vehicle Reference：控制车型、比例、车门、损伤、反射与运动状态；
- Style Reference：只控制视觉语言，不得覆盖身份、空间、物理、产品事实或动作。

最终提示词只描述当前镜头真正需要的参考信息。已由参考图稳定提供的细节不重复长篇覆写。

## 4. 光学结果优先于参数名

焦段、FOV、镜头品牌、光圈等参数只在确有帮助时使用。模型控制优先写“摄影机物理距离 + 透视结果 + 背景行为 + 主体比例 + 景深结果”。

### 广角/近距离空间镜头
适用于环境、身体运动、近距离沉浸和空间关系。优先表达：
- camera physically close to the subject；
- foreground presence becomes stronger；
- environment remains readable around the subject；
- straight lines remain natural / rectilinear；
- deep readable spatial context；
- no telephoto compression。

### 标准自然透视
适用于大多数对话、纪实、产品使用和自然动作。优先表达：
- natural human-eye perspective；
- stable face and body proportions；
- background readable without exaggerated expansion or compression。

### 长焦/远距离观察
适用于肖像、偷窥感、体育、野生动物、远处观察与情绪隔离。优先表达：
- camera physically far from the subject；
- close framing achieved through lens reach；
- background compressed behind the subject；
- subject isolated against soft background；
- foreground occlusion when observation感需要成立。

同一连续镜头内不无因改变镜头性格。不同内容类别需要不同光学效果时，用明确切镜分离，不在一个 beat 里同时要求广阔环境、超浅景深肖像和微距细节。

## 5. Physical Causality Chain

所有复杂动作优先检查：

`Cause → Contact → Force → Movement → Inertia / Weight Transfer → Result`

动作必须由可见原因触发。

例如上下车：
`手接触门把手 → 拉门 → 门绕铰链打开 → 身体转向入口 → 脚进入 → 重心转移 → 身体坐入 → 手再次施力 → 门关闭`。

不得让门自行开启、人物穿过实体、脚无接触滑动、物体瞬移、武器或产品无重量悬浮。

针对常见对象：
- 行走：heel contact → weight transfer → hip shift → toe push-off；
- 跑动：真实地面接触、步幅变化、相反侧摆臂、身体前倾；
- 重物/武器：手腕与肩臂对重量有反应，存在加速、减速和惯性；
- 布料/头发：主体先动，布料与头发存在轻微延迟和回摆；
- 液体：遵循重力、黏性、附着、滴落、飞溅弧线与残留；
- 烟尘雪火：随风和热流运动，并与前中后景及物体表面产生连续关系。

## 6. Lighting Geometry

光线不是装饰词，而是空间约束。后台至少确定：

`Primary Source → Direction → Camera Side → Subject Shadow/Rim State → Background Brightness → Exposure Priority`

不要只写 cinematic lighting、dramatic lighting、beautiful rim light。

例如逆光镜头应优先明确：主体位于摄影机与亮背景之间；摄影机留在主体阴影侧；曝光优先保护亮背景；人物正面允许自然压暗；轮廓光、反射高光和环境反弹光负责塑形。

如果正面补光会破坏设计，则用正向结果锁定：`camera-facing side stays naturally dark, rim light separates the silhouette`，只在重复失败时再补最少量负向约束。

## 7. 局部失败锁，而非巨型负面词库

先写目标状态，再只对高风险错误增加一条局部锁。

优先：
- all required characters are already visible in frame one；
- her torso faces camera-right while her eyes stay on him；
- his hand remains on the door handle until the door visibly opens；
- camera remains on the shadow side；
- the background stays compressed throughout this shot。

避免把大量“不要、禁止、避免”集中成通用负面块。负向规则只用于高概率且会严重破坏结果的错误。

## 8. 执行层与创意层的边界

本模块只保证“拍对”，不能替代“值得拍”。每镜仍必须先通过导演信息判断：
- 观众第一眼获得什么信息；
- 为什么继续看；
- 动作、异常或关系变化如何形成问题；
- 触发如何导致变化；
- 视觉、情绪、产品证据或剧情信息最终兑现什么。

对于高概念广告和视觉蜕变，优先遵循：
`熟悉现实 → 微异常/悬念 → 明确动作触发 → 连续传播 → 超预期视觉兑现 → 产品/信息收束`。

执行层只能强化该链路的空间、镜头、物理、光线和连续性，不能为了摄影技术完整而稀释 Hook、Bridge、Payoff。

## 9. 提示词编译顺序

复杂生成任务后台按以下顺序组织，再压缩成用户需要的最终提示词：

`Scene Context → Active References → Location/Spatial Map → First Frame → Spatial Blocking → Optical Outcome → Camera Behavior → Action Timing → Physical Causality → Lighting Geometry → Audio → End Frame / Continuity Locks`

最终输出不必显示这些标题。只有在结构化 Seedance 提示词确实能提高可读性时才保留分段。

高密度信息优先留给：身份锚点、首帧、空间关系、视线、接触、动作路径、光学结果、光线几何、对白和跨镜状态。通用审美形容词、参考图已明确的服装细节、无关背景装饰优先删除。
