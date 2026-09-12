# 林枫创作 Skills｜GitHub 母版

本仓库作为当前 Skill 的 SSOT（Single Source of Truth）。规则优化优先同步到这里，再用于其他运行环境。

## 母版索引

| Skill | 路径 | 作用 |
|---|---|---|
| 林枫生图提示词 Skill | `linfeng-image-prompt/` | 将人物、产品、场景、海报、电商等需求编译为主体优先、低污染的生图提示词 |
| 林枫视频提示词 Skill | `linfeng-video-prompt/` | 将 Brief、脚本、分镜、参考视频或成片问题编译为高信号、可直接生成的视频提示词与导演控制 |
| 剧情带货 Skill | `story-commerce-skill/` | 剧情产品广告的创意、脚本、分镜与生成流程 |

## 当前统一提示词原则

### 1. 主体优先

最终给生成模型的信息权重默认遵循：

`主体/产品 > 动作/事件 > 空间/构图/连续性 > 必要镜头 > 必要真实性补丁 > 光影/设备术语`

灯光、材质、景深、反射等不是固定必填项；只有直接改变当前结果时才加入。

### 2. 抽象目标先转译

`强钩子、高能、高级感、电影感、张力、情绪感、视觉冲击、超现实感` 等抽象判断由 Skill 在内部完成设计，最终转成模型能执行的主体、动作、尺寸反差、空间、构图、运动、材质或光色结果，不直接当作主要生成指令。

### 3. 真实性补丁

先完成主体与核心事件，再判断当前画面最容易出现的一个 AI 错误；只有风险明确时补一条最短可见修正。默认不把接触阴影、反弹光、高光滚降、景深、空气透视、运动模糊等全部打包。

### 4. 光影不抢主体

光影是加分层，不是主体层。普通任务不设置固定大段光影字段；需要时只保留最能解决问题的一句可见结果。

### 5. 最少词、最大控制力

Skill 可以懂很多，但最终 Prompt 只留下会直接改变生成结果的信息。删除重复、解释性、管理性和为了显得专业而加入的术语。

## 入口

- 生图母版：`linfeng-image-prompt/SKILL.md`
- 视频母版：`linfeng-video-prompt/SKILL.md`
- 视频最终格式：`linfeng-video-prompt/references/output-contract-and-validation.md`
- 视频编译规则：`linfeng-video-prompt/references/prompt-compilation-and-consistency.md`
- 视频真实性补丁：`linfeng-video-prompt/references/physical-reality-lock.md`
- 视频按需光影：`linfeng-video-prompt/references/camera-light-quality-baseline.md`

---

**维护规则：** 当前用户明确要求 > 已确认事实/参考资产 > 母版默认规则。