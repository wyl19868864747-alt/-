# 电影摄影、光学、灯光、运动、渲染与 VFX 工具库

## 目录

1. 使用原则
2. 按需技术选型
3. 摄影机系统
4. 镜头、焦段、光圈与滤镜
5. 摄影机运动系统
6. 灯具与控光工具
7. 帧率、快门、曝光与色温
8. 色彩管理与成像纹理
9. 渲染、模拟与合成工具
10. 任务选型速查
11. 提示词转译方法
12. 官方资料

## 1. 使用原则

此文件是后台选型库，不是需要整段复制进提示词的器材清单。

1. 先确定情绪、主体、空间、动作和产品证据，再选择技术。
2. 一个器材、镜头、灯具、滤镜、渲染器或合成工具只承担一个可见职责。
3. 实拍人物或生活场景优先写真实摄影系统、镜头、灯光和运动工具；没有 CG 时不加入渲染器名称。
4. CG 产品、虚拟场景或数字特效只选一个主渲染路径，再用模拟与合成补足具体职责。
5. 仅为需要的画面效果进行技术选型；成品放入【光影与成像基线】，写法与放置唯一按 `camera-light-quality-baseline.md`，分镜只补局部变化。
6. 生成式视频模型不会真实调用这些设备或软件。专业名词必须继续转译为透视、景深、高光、肤色、反射、视差、运动模糊、接触阴影和颗粒等可见结果。

## 2. 按需技术选型

本文件的型号、镜头、光圈、滤镜与运动系统供专业选型查阅，不能作为普通任务的必填表。只选择会改变当前画面的项目：成像媒介、光学透视/景深、焦点和运动、光源与色彩、材质或必要渲染合成。

生成模型接收可见结果；实际拍摄或API参数必须由对应工具设置。光影信息结构和数值取舍唯一按 `camera-light-quality-baseline.md`；本文件不再复制一套全片基线模板。

## 3. 摄影机系统

| 系统 | 已核实技术特征 | 适合的可见结果 | 常用后台起点 |
| --- | --- | --- | --- |
| ARRI ALEXA 35 | 4.6K Super 35、17 挡动态范围、EI 160–6400、LogC4/AWG4/REVEAL | 平滑高光、稳定肤色、强日光与阴影同时保留、真实人物和服装 | 日景 EI 800、24fps、180°；按景别选 T2.8–T4 |
| Sony VENICE 2 8K | 8.6K 全画幅、16 挡、双基础 ISO 800/3200、S-Log3、内置 ND | 全画幅空间层次、自然肤色、低照度城市与室内、浅景深动态跟拍 | 日景 ISO 800；低照度 ISO 3200；24fps、180° |
| 现代旗舰手机主摄 | 约 24–28mm 等效、自动曝光/自动对焦、轻微计算摄影 | TikTok/YouTube UGC、可信近距离口播、轻微手持与对焦呼吸 | 30fps、1/60s；窗光；曝光锁定后保留轻微手持 |

选择逻辑：

- 强逆光、窗边护肤、黑色服装和亮部保护优先 ALEXA 35。
- 全画幅城市跟拍、夜景或电梯低照度优先 VENICE 2。
- UGC 段主动切换到手机观感；不要让同一镜头既是大画幅电影机又是手机自拍。

## 4. 镜头、焦段、光圈与滤镜

### 镜头系列

| 镜头 | 官方特征 | 适用画面 |
| --- | --- | --- |
| ARRI Master Prime | 12–150mm、全系列 T1.3，高解析与高对比 | 清晰、现代、受控的商业摄影；结构、标签、建筑边缘 |
| ARRI Signature Prime | 12–280mm；温暖肤色、开放阴影、清晰黑位 | 高定人物、服饰、自然肤色与柔和空间层次 |
| Cooke S8/i FF | 全画幅，核心焦段 T1.4，控制景深与耀斑 | 有机温暖的人物、时装、低照度、较柔和的高端质感 |
| Angénieux Optimo Ultra Compact | 全画幅紧凑变焦，T2.9 | 连续推拉、活动跟拍、需要真实连续变焦的镜头 |
| Leitz THALIA 65 MAKRO | 24/55/120mm，1:2 微距；自然焦点衰减 | 护肤、珠宝、液滴、面料与产品极近细节 |

### 焦段与景别起点

- 18–25mm：大空间与快速接近；人物近距离会产生明显透视，不用于高定面部主特写。
- 32–40mm：街头跟拍、环境人物、动态视差；适合服装与空间同时成立。
- 50mm：自然透视、产品与人物关系、标准中景。
- 65–85mm：美妆、肤质、时装肩线、克制背景压缩。
- 100–120mm 微距：产品标签、液滴、玻璃、面料；以 T4 左右保持关键平面。

焦段必须结合传感器格式判断。全画幅 40mm 的视角比 Super 35 40mm 更宽；不要跨镜头无解释更换格式和视角。

### T 值

- T1.3–T2：极浅景深、低照度、情绪特写；产品标签和多人物动作容易脱焦。
- T2.8：高定人物和单主体商业镜头的常用平衡。
- T4：产品、微距、服装结构与动作连续的安全起点。
- T5.6 及以上：群像、复杂动作、空间关系需要更深景深时使用。

### 光学滤镜

- Tiffen Black Pro-Mist 1/8：轻微柔化数字锐度和高光，保留产品文字与皮肤细节。
- Black Pro-Mist 1/4：更明显的高光扩散与低对比；高端美妆可用，文字、珠宝和强点光需谨慎。
- ND：保持目标快门与光圈，不作为风格词。
- CPL：控制玻璃、汽车和石材反射；使用后仍需保留表现材质所需的渐变反射。

## 5. 摄影机运动系统

| 工具 | 运动特征 | 适用任务 | 需要写进镜头的内容 |
| --- | --- | --- | --- |
| 三脚架/固定云台 | 构图稳定、观察性强 | 口播、对话、产品英雄镜 | 机位高度、角度、是否微推 |
| J.L. Fisher Dolly/轨道 | 精确直线或曲线，重量感稳定 | 人物侧跟、走廊、产品与人物关系 | 轨道方向、距离、速度、缓入缓出 |
| Slider/微距滑轨 | 短距离精确视差 | 瓶体、液滴、珠宝、布料 | 起止点、滑动距离、焦点接力 |
| Steadicam | 有人体呼吸但连续流畅 | 走廊、人物跟随、生活方式 | 与人物的相对方位、跟随延迟、步速 |
| ARRI TRINITY 2 | 五轴混合稳定，可连续高低机位转换 | 高定时装、街道至大厅、一镜式高低变化 | 同一侧运动路径、高度变化、弧度、地平线 |
| DJI Ronin 2 | 三轴稳定、紧凑灵活 | 近距离环行、汽车、狭窄室内 | 运动半径、操作者路径、摇移速度 |
| Technocrane | 伸缩升降并保持精确取景 | 大空间揭示、从产品升到人物/建筑 | 臂长变化、升降高度、镜头是否后退 |
| MRMC Bolt/Bolt X | 高速、精准、可重复的运动控制 | 产品高速掠过、液滴、可重复 VFX 板 | 预设轨迹、速度峰值、同步动作、缓冲区 |

运动设计顺序：主体事件 → 相机动机 → 工具 → 路径 → 速度 → 焦点 → 画面结果。最终提示词不解释这套顺序，只呈现已选好的摄影运动。

## 6. 灯具与控光工具

### 灯具

- ARRI M18/M40/M90 HMI：约 6000K 日光型硬光，适合从窗外制造有方向的日光、远距离建筑反射和清晰阴影；M40 约 18°–52°可调，M90 约 15°–49°可调。
- ARRI SkyPanel X：1500K–20000K 全光谱，可作硬光、柔光或反弹光；适合可控室内、肤色补光、背景色温和低亮度无闪烁调光。
- 实景窗光/天空光：先确定窗户和太阳世界方向，再用反弹与负补控制；机位改变时世界光源不随画面左右重置。

### 控光与塑形

- Ultrabounce/白色反光布：把硬日光变成大面积自然反弹，适合窗边人物和开放阴影。
- Bleached/Unbleached Muslin：更柔和、略暖的反弹；护肤与肤色可用。
- 1/2 Grid Cloth、Full Grid、Magic Cloth：扩大光源并控制阴影边缘；距离和面积比“柔光”一词更有意义。
- 4×4/8×8 Solid、黑旗、黑布：负补、切光、压低环境反射，塑造面部和黑色服装轮廓。
- Cutter/Floppy/Net：精确控制产品标签、高光带和背景亮度。
- Mirror/Reflector：把真实太阳或 HMI 形成窄束反射；必须有来源、方向和落点。
- Haze：只在可见光束、空间分层或特效融合需要时加入；生活护肤和 UGC 默认不使用。

### 光比与曝光

- 柔和商业人物：约 2:1–3:1 主辅关系，开放阴影保留肤质。
- 高定结构与黑色服装：约 3:1–4:1，用斜侧光和负补显示织纹、肩线与轮廓。
- 产品玻璃：侧后轮廓光 + 大面积渐变反射卡 + 可读标签面；焦散必须落在真实承接面。

## 7. 帧率、快门、曝光与色温

### 帧率与快门角

- 24fps、180°：标准电影运动模糊，真人TVC和时装主线起点。
- 25fps、180°：适合 50Hz 灯光与地区制式。
- 30fps、180°或 1/60s：手机 UGC、社媒口播、较直接的现实感。
- 48/60fps：克制慢动作、布料、头发和产品动作；回放速度必须明确。
- 96/120fps：液滴、粉末、飞溅和高速产品运动；只用于短促证据镜头。
- 90°快门：运动更锐利、紧张、碎裂感更强。
- 270°–360°快门：拖影明显；只在明确梦境或失序体验时使用。

### 曝光与色温

- ALEXA 35 常用 EI 800 起步；根据高光/暗部策略调整，合法范围由机身规格决定。
- VENICE 2 8K 的双基础 ISO 为 800/3200；日景和低照度分别从对应基础值起步。
- 日光起点约 5600K，钨丝灯约 3200K；混合光先决定肤色/产品的白平衡归属，再保留环境色差。
- 强窗景保留亮部纹理；黑色服装保留阴影织纹；玻璃标签面保持在可读曝光区。

## 8. 色彩管理与成像纹理

- ARRI：LogC4/AWG4/REVEAL 作为采集与调色先验，强调亮部滚降、肤色色相和边缘稳定。
- Sony：S-Log3 与 VENICE 色彩科学，适合自然肤色与低照度宽容度。
- ACES/ACEScct：统一摄影机、CG 和合成的色彩管理；用于跨镜头、跨引擎或复杂 VFX。
- Rec.709/社媒 SDR：最终观感需保留中间调、肤色和产品色，不把高光推成廉价 HDR 白边。
- 胶片纹理：细颗粒、轻微高光扩散、克制色彩交叉；不加入暗部彩噪、锐化光边或厚重复古滤镜。

## 9. 渲染、模拟与合成工具

| 工具 | 正确职责 | 适用画面 | 可见转译 |
| --- | --- | --- | --- |
| Autodesk Arnold | Monte Carlo 光线追踪、全局光照、SSS、可预测离线渲染 | CG 人物、皮肤、产品、复杂材质 | 真实能量衰减、皮下散射、稳定反射折射 |
| Maxon Redshift | GPU 加速、偏置式高质量快速渲染 | 动态产品、动态图形、广告迭代 | 干净低噪、稳定运动模糊、受控材质层 |
| Unreal Engine Path Tracer | 硬件加速渐进路径追踪、物理全局光/反射/折射 | 虚拟摄影棚、建筑、数字环境、离线电影帧 | 高密度几何、物理全局光、稳定大空间视差 |
| Unreal Engine Lumen/Nanite | 实时动态全局光与高密度几何 | 大型可探索虚拟场景、虚拟制片、动态环境 | 运动时持续的间接光、反射和几何细节 |
| OctaneRender | 光谱物理渲染、透明/半透明与焦散 | 玻璃、液体、珠宝、金属产品英雄镜 | 清楚材质分离、折射、焦散与光谱色彩 |
| Houdini FX | 流体、烟火、破坏、粒子、布料等物理模拟 | 液体飞溅、烟雾、碎裂、复杂特效 | 明确的产生、受力、碰撞、消散与尺度 |
| Foundry Nuke/NukeX | 节点合成、3D 跟踪、镜头求解、深度合成 | 时间冻结、环境扩展、抠像、实拍与CG整合 | 一致透视、畸变、景深、颗粒、接触阴影与互动光 |

组合规则：

- 纯实拍护肤/服装：摄影机 + 镜头 + 灯光 + 运动系统 + 色彩管理；不加入渲染引擎。
- CG 产品英雄镜：Arnold、Redshift 或 Octane 三选一为主，不并列负责同一材质。
- 大型虚拟环境：Unreal Path Tracer 或 Lumen/Nanite 按离线/实时需求选择。
- 流体、烟火、破坏：Houdini负责模拟；Arnold/Redshift/Octane负责渲染；Nuke负责合成。
- 时间冻结：真实场景板、冻结表演和 Nuke 级跟踪/合成；不需要 Houdini 粒子或无来源悬浮物。

## 10. 任务选型速查

| 任务 | 摄影/镜头 | 运动 | 灯光 | 渲染/VFX |
| --- | --- | --- | --- | --- |
| 高奢护肤窗边人物 | ALEXA 35；65–85mm；产品用 100–120mm 微距；T2.8/T4 | 精密 Dolly、Slider 或 Bolt；UGC切手机 | 反射日光 + Muslin/Ultrabounce + 负补 | 实拍物理成像；必要时 Nuke 清理/合成 |
| 高奢服装城市跟拍 | ALEXA 35 或 VENICE 2；32–50mm；T2.8–T4 | TRINITY 2/Steadicam；遮挡转场 | 斜侧日光 + 大反弹 + 负补显示织纹 | 时间冻结用 Nuke 级跟踪与冻结板 |
| 产品高速英雄镜 | ALEXA 35/高速机观感；100mm 微距；T4；96/120fps | MRMC Bolt/Bolt X | 轮廓光、渐变反射卡、精确触发 | CG产品时选 Arnold/Redshift/Octane 之一 |
| 手机 UGC | 现代手机 24–28mm 等效；30fps、1/60s | 轻微手持或固定小支架 | 窗光/实用灯 + 小面积反弹 | 手机实拍质感；轻量清理，不套CG引擎 |
| 大型奇幻/科幻环境 | 大画幅观感；24–40mm | Technocrane/虚拟摄影机 | 方向性主光 + 体积层次 | Unreal + Houdini + Nuke，按职责拆分 |

## 11. 提示词转译方法

后台：`运镜服务产品，不能乱转。`

前台：`MRMC Bolt 从瓶身标签前方低位起步，沿桌面完成 35°弧形滑移并抬升 20cm；标签持续位于焦平面，背景视差依次露出窗光和人物受光侧脸。`

后台：`人物动作不要 AI 感。`

前台：`她保持面向窗户的四分之三侧身，只把视线从窗外落到产品，右手一次拿起瓶身，肩颈和左手保持自然放松。`

后台：`时间冻结要真实。`

前台：`响指发生前，行人、鸟和车辆保持正常运动；响指的同一帧，行人停在完整步态、鸟停在上方远景、车轮停止转动，相机继续侧向移动并产生清楚视差。Nuke 级冻结合成保持透视、畸变、景深、颗粒和接触阴影一致。`

## 12. 官方资料

资料核验日期：2026-08-10。后续涉及具体新机型、软件版本或时效性参数时重新查证。

- ARRI ALEXA 35：<https://www.arri.com/en/cine-systems/cine-cameras/legacy-cine-cameras/alexa-35>
- Sony VENICE 2：<https://sony-cinematography.com/venice2/>
- ARRI Master Prime：<https://www.arri.com/en/cine-lenses/arri-zeiss-fujinon-lenses/master-primes/master-primes>
- ARRI Signature Prime：<https://www.arri.com/en/cine-lenses/signature-lenses/signature-primes-zooms/signature-primes>
- Cooke S8/i FF：<https://cookeoptics.com/lens/s8-i-ff/>
- Angénieux Optimo Ultra Compact：<https://www.angenieux.com/lenses/optimo-ultra-compact/>
- Leitz THALIA 65 MAKRO：<https://www.leitz-cine.com/product/thalia-makro>
- ARRI TRINITY 2：<https://www.arri.com/en/cine-systems/camera-stabilizer-systems/trinity-2-and-artemis-2/trinity-2>
- MRMC Bolt：<https://www.mrmoco.com/motion-control/bolt/>
- Technocrane：<https://www.supertechno.com/>
- J.L. Fisher Dollies：<https://www.jlfisher.com/dollies>
- ARRI SkyPanel X：<https://www.arri.com/en/lighting/led-panel-lights/skypanel-x>
- ARRI M-Series：<https://www.arri.com/en/lighting/daylight-tungsten/daylight/m-series>
- Tiffen Black Pro-Mist：<https://tiffen.com/products/black-pro-mist-filter>
- Autodesk Arnold：<https://www.autodesk.com/products/arnold/overview>
- Maxon Redshift：<https://help.maxon.net/r3d/maya/en-us/Content/html/Redshift%2BRenderer.html>
- OTOY OctaneRender：<https://home.otoy.com/render/octane-render/>
- Unreal Engine Path Tracer：<https://dev.epicgames.com/documentation/unreal-engine/path-tracer-in-unreal-engine>
- Houdini FX：<https://www.sidefx.com/products/houdini/vfx/>
- Foundry Nuke：<https://www.foundry.com/products/nuke-family/nuke>
- ACES：<https://acescentral.com/>
