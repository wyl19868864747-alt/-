# STYLE INJECTION BUDGET｜风格压缩注入规则 V1

> 目标：让用户选中的Style在Seedance里真正可见，同时不挤掉产品、Proof、动作、对白和状态。

Style属于Prompt优先级中的 `P3 STYLE / DECORATION`。

核心：
`LOCK STYLE INTERNALLY → COMPRESS STYLE EXTERNALLY`
`STYLE SHOULD BE VISIBLE, NOT VERBOSE`

---

## 1. 最终Prompt只允许保留

从Style Card中最多提取：
- 2–3个核心视觉锚点；
- 1个光影/色彩锚点；
- 1个镜头/成像质感锚点；
- 必要时1个环境材质提示。

通常压成1句，最多2句。

不要把 `style-dna-library.md` 的整张Card复制到最终Prompt。

---

## 2. 注入位置

### 开场总控
必须体现用户锁定Style，但只写稳定的总体视觉结果，不写具体剧情。

### 局部镜头
只有某个镜头必须依赖Style特征才能成立时，再补1个局部提示，例如：
- Y2K硬闪；
- Noir百叶窗影；
- 70s胶片晕光；
- 超现实尺度揭示。

禁止每个Beat重复完整Style描述。

---

## 3. Style不得占用P0/P1

如果Style与以下内容竞争Prompt注意力：
- Product Lock
- Best Proof
- 关键状态变化
- 精确对白
- 动作方向
- 场面调度

先压缩Style，不压缩上述核心。

`P0/P1 > P2 > P3 STYLE`

---

## 4. 风格实现优先顺序

优先通过以下手段让Style“看得出来”：

1. 光线结构
2. 色彩体系
3. 构图/焦段
4. 镜头运动与成像质感
5. 材质/服装/环境细节

最后才依赖大量专属道具或固定场地。

原因：前五项更可迁移，也更不容易破坏产品逻辑。

---

## 5. 禁止

- 禁止多风格自动叠加。
- 禁止长串同义风格词：`高级、电影级、大片感、奢华、高端、顶级……`
- 禁止用设备/引擎名字堆质量感。
- 禁止为了70s/Y2K/未来等风格改变产品本体年代、外形或功能。
- 禁止超现实风导致产品复制、融化、尺寸永久变化或Proof失真。
- 禁止Style把Location写死。

---

## 6. QA

最终Prompt前检查：
- [ ] 不看Style ID，只看最终风格句，仍能感知对应视觉差异？
- [ ] 删除具体地点名后，这个Style仍成立？
- [ ] 换成另一类产品后，这个Style仍可迁移？
- [ ] Style没有改写Product Truth / Best Proof？
- [ ] Style描述是否只出现1次为主，而不是每Beat重复？

最终：

> **风格必须强到看得见，文字必须少到不抢执行权。**