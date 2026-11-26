---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.34287v1"
published: "2026-11-25T12:41:23Z"
age_days: 0
score: 38
created: 2026-11-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> DataForgeVLA 用已有遥操作数据打底：先摆出新的机器人与物体起始姿态，再生成操作视频，从画面反推关节动作，给机器人策略提供新的训练示范。

## 问题

训练抓放策略需要不同物体、抓取姿态和摆放位置，靠遥操作收集，每扩一种布置都可能要重新录制。只改示范的外观会保留原动作，遇到需要换抓法的新摆位就不够用。仿真重定向可以改动作，但要为任务准备资产和定义，还可能遇到视觉和接触动力学的仿真到现实差距。[S3](https://arxiv.org/html/2611.34287v1#S1.p1.1)[S9](https://arxiv.org/html/2611.34287v1#S2.p1.1)

### 用一个例子理解

理解用例（非论文实验）——输入一张桌面种子图、一件可以重摆的包装和抓放指令。先把包装旋转并移到桌角，再从新首帧生成抓放过程，逐帧恢复右臂和手的关节姿态。输出是画面和下一帧关节目标对齐的一段训练样本。

## 创新点或方法

关键是把初始几何、后续运动和动作标注分开处理。先利用标定相机和真实关节记录，把 MuJoCo 渲染的手与原图对齐，用轮廓图和原图配对训练 Cosmos-3 图像转换模型。造数据时，在清空的实拍桌面上换手姿和物体位姿，由转换模型生成逼真的首帧，再让另一套微调过的 Cosmos-3 根据指令续写操作视频。RoboHaMeR 从视频恢复运动，经过逆运动学得到关节轨迹。策略用筛过的片段学习右臂与右手的下一帧绝对关节目标；真机推理时由 GR00T 输出目标，造视频和还原动作都发生在训练前。[S14](https://arxiv.org/html/2611.34287v1#S3.SS1.p1.1) [S15](https://arxiv.org/html/2611.34287v1#S3.I1.i1) [S16](https://arxiv.org/html/2611.34287v1#S3.I1.i2) [S17](https://arxiv.org/html/2611.34287v1#S3.I1.i3) [S18](https://arxiv.org/html/2611.34287v1#S3.I1.i4) [S19](https://arxiv.org/html/2611.34287v1#S3.SS1.p3.1) [S20](https://arxiv.org/html/2611.34287v1#S3.SS2.p1.1) [S21](https://arxiv.org/html/2611.34287v1#S3.I2.i1) [S22](https://arxiv.org/html/2611.34287v1#S3.I2.i2) [S23](https://arxiv.org/html/2611.34287v1#S3.I2.i3) [S24](https://arxiv.org/html/2611.34287v1#S3.I2.i4) [S25](https://arxiv.org/html/2611.34287v1#S3.I2.i5)[S29](https://arxiv.org/html/2611.34287v1#S3.SS3.p1.1)[S34](https://arxiv.org/html/2611.34287v1#S4.p3.1) [S35](https://arxiv.org/html/2611.34287v1#S5.p1.1)

### 方法如何工作

1. 用真实位姿渲染机械手并与实拍原图对齐，构造轮廓到真实画面的训练对。
2. 在清空的桌面上重摆手和物体，将新轮廓转成真实风格首帧，固定想覆盖的起始几何。
3. 把首帧和指令交给视频模型，生成完整操作，再从 RGB 恢复运动并映射到机器人关节。
4. 筛掉不一致的片段，把相邻帧转换成当前状态与下一帧控制目标，用于微调 GR00T。

### 必要术语

- 轮廓图：用边缘保留物体和手的几何，去掉渲染纹理；在本文中用来控制生成首帧的摆位。
- 逆运动学：从手腕或手部目标姿态反求关节配置；在本文中把视觉恢复的运动映射回机器人。
- 绝对关节目标：直接指定关节要到的位置；本文的策略训练用下一帧位置作为目标。

## 证据

数据有 340 段，覆盖八类物体，300 段通过筛选。[S27](https://arxiv.org/html/2611.34287v1#S3.SS2.p3.1) 两个预训练 GR00T N1.6 策略各微调 20,000 步，在同一真机奥利奥抓放协议下，合成组成功 16/20，105 段真实遥操作组成功 18/20。成功要求在 30 秒内抓起包装并放进目标盘，途中无重试或人工干预。这说明恢复出的标签能支持这一任务的真机执行。[S35](https://arxiv.org/html/2611.34287v1#S5.p1.1)

## 局限

作者指出，失真的生成动作会把误差传给轨迹恢复，而且真机证据来自一种物体和一套机器人相机配置。两组训练集的大小与任务组成不同，真机成绩相差两次成功只适合描述这次试验。作者也明确缺少匹配的未筛选对照。我会另查预训练策略直接上机能做到多少，以判断合成微调增加了什么。[S39](https://arxiv.org/html/2611.34287v1#S6.p1.1) [S40](https://arxiv.org/html/2611.34287v1#S6.p2.1)

- **判断**：值得读到动作导出和真机协议，尤其要看从视频恢复的姿态怎样变成控制目标。

## 研究关联

如果已有少量标定好的示范，而缺的是新起始摆位，可以先控制首帧几何，再让视频模型生成后续运动。这样能主动指定要补采的场景，同时把实测问题落到关节标签是否足以训练策略。

### 下一步读哪里

对照 [S25](https://arxiv.org/html/2611.34287v1#S3.I2.i5)[S33](https://arxiv.org/html/2611.34287v1#S4.p2.1) [S34](https://arxiv.org/html/2611.34287v1#S4.p3.1) [S35](https://arxiv.org/html/2611.34287v1#S5.p1.1) 核查完整运动学记录与策略导出之间的时间对齐，再查质量筛选能否识别穿模、滑移和关节跳变，以及这些错误是否有不同的拒绝规则。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34287v1
- 获取时间：2026-11-26T03:57:01.821413+00:00
- [S1] [DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training · 正文段落 1](https://arxiv.org/html/2611.34287v1#S0.F1)
- [S2] [DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training · 正文段落 2](https://arxiv.org/html/2611.34287v1#abstract1.1)
- [S3] [1. Introduction · 正文段落 3](https://arxiv.org/html/2611.34287v1#S1.p1.1)
- [S4] [1. Introduction · 正文段落 4](https://arxiv.org/html/2611.34287v1#S1.p2.1)
- [S5] [1. Introduction · 正文段落 6](https://arxiv.org/html/2611.34287v1#S1.p4.1)
- [S6] [1. Introduction · 正文段落 7](https://arxiv.org/html/2611.34287v1#S1.I1.i1)
- [S7] [1. Introduction · 正文段落 8](https://arxiv.org/html/2611.34287v1#S1.I1.i2)
- [S8] [1. Introduction · 正文段落 9](https://arxiv.org/html/2611.34287v1#S1.I1.i3)
- [S9] [2. Related Work · 正文段落 10](https://arxiv.org/html/2611.34287v1#S2.p1.1)
- [S10] [2. Related Work · 正文段落 11](https://arxiv.org/html/2611.34287v1#S2.p2.1)
- [S11] [2. Related Work · 正文段落 12](https://arxiv.org/html/2611.34287v1#S2.p3.1)
- [S12] [2. Related Work · 正文段落 13](https://arxiv.org/html/2611.34287v1#S2.p4.1)
- [S13] [3. Dataset Construction · 正文段落 14](https://arxiv.org/html/2611.34287v1#S3.p1.1)
- [S14] [3.1. Training an Edge-Consistent RGB Transfer Model · 正文段落 15](https://arxiv.org/html/2611.34287v1#S3.SS1.p1.1)
- [S15] [3.1. Training an Edge-Consistent RGB Transfer Model · 正文段落 16](https://arxiv.org/html/2611.34287v1#S3.I1.i1)
- [S16] [3.1. Training an Edge-Consistent RGB Transfer Model · 正文段落 17](https://arxiv.org/html/2611.34287v1#S3.I1.i2)
- [S17] [3.1. Training an Edge-Consistent RGB Transfer Model · 正文段落 18](https://arxiv.org/html/2611.34287v1#S3.I1.i3)
- [S18] [3.1. Training an Edge-Consistent RGB Transfer Model · 正文段落 19](https://arxiv.org/html/2611.34287v1#S3.I1.i4)
- [S19] [3.1. Training an Edge-Consistent RGB Transfer Model · 正文段落 20](https://arxiv.org/html/2611.34287v1#S3.SS1.p3.1)
- [S20] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 21](https://arxiv.org/html/2611.34287v1#S3.SS2.p1.1)
- [S21] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 22](https://arxiv.org/html/2611.34287v1#S3.I2.i1)
- [S22] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 23](https://arxiv.org/html/2611.34287v1#S3.I2.i2)
- [S23] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 24](https://arxiv.org/html/2611.34287v1#S3.I2.i3)
- [S24] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 25](https://arxiv.org/html/2611.34287v1#S3.I2.i4)
- [S25] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 26](https://arxiv.org/html/2611.34287v1#S3.I2.i5)
- [S26] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 27](https://arxiv.org/html/2611.34287v1#S3.I2.i6)
- [S27] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 28](https://arxiv.org/html/2611.34287v1#S3.SS2.p3.1)
- [S28] [3.2. Synthetic Scene Recomposition and Dataset Generation · 正文段落 29](https://arxiv.org/html/2611.34287v1#S3.SS2.p4.1)
- [S29] [3.3. RoboHaMeR Label Generation · 正文段落 30](https://arxiv.org/html/2611.34287v1#S3.SS3.p1.1)
- [S30] [4. Dataset Description and Usage · 正文段落 36](https://arxiv.org/html/2611.34287v1#S4.p1.1)
- [S31] [4. Dataset Description and Usage · 正文段落 37](https://arxiv.org/html/2611.34287v1#S4.T1)
- [S32] [4. Dataset Description and Usage · 正文段落 38](https://arxiv.org/html/2611.34287v1#S4.T1.2)
- [S33] [4. Dataset Description and Usage · 正文段落 39](https://arxiv.org/html/2611.34287v1#S4.p2.1)
- [S34] [4. Dataset Description and Usage · 正文段落 40](https://arxiv.org/html/2611.34287v1#S4.p3.1)
- [S35] [5. Preliminary Results · 正文段落 41](https://arxiv.org/html/2611.34287v1#S5.p1.1)
- [S36] [5. Preliminary Results · 正文段落 42](https://arxiv.org/html/2611.34287v1#S5.p2.1)
- [S37] [5. Preliminary Results · 正文段落 43](https://arxiv.org/html/2611.34287v1#S5.F2.g1)
- [S38] [5. Preliminary Results · 正文段落 44](https://arxiv.org/html/2611.34287v1#S5.F2)
- [S39] [6. Discussion and Limitations · 正文段落 45](https://arxiv.org/html/2611.34287v1#S6.p1.1)
- [S40] [6. Discussion and Limitations · 正文段落 46](https://arxiv.org/html/2611.34287v1#S6.p2.1)
- [S41] [6. Discussion and Limitations · 正文段落 47](https://arxiv.org/html/2611.34287v1#S6.p3.1)
- [S42] [6. Discussion and Limitations · 正文段落 48](https://arxiv.org/html/2611.34287v1#S6.p4.1)
- [S43] [7. Conclusion · 正文段落 49](https://arxiv.org/html/2611.34287v1#S7.p1.1)
- [S44] [Ethics and Privacy Statement · 正文段落 50](https://arxiv.org/html/2611.34287v1#Sx1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/DataForgeVLA Fully Synthetic Manipulation Demonstrations for Vision-Language-Act.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present a dataset of 340 fully synthetic manipulation demonstrations generated from real seed data for Vision-Language-Action (VLA) training. The corpus contains 32,340 frames with synchronized RGB and actions across eight object categories, represented as LeRobot v2.1 episodes with H.264 video, per-frame robot states and pose-valued action labels, language task annotations, summary statistics and quality decisions. Each synthetic demonstration is produced without additional teleoperation: a LoRA-fine-tuned Cosmos-3 model generates a manipulation video, and RoboHaMeR recovers the corresponding robot trajectory from RGB. Quality screening accepted 300 of 340 episodes for policy fine-tuning. As preliminary evidence of feasibility, a pretrained GR00T N1.6 policy fine-tuned exclusively on the 300 accepted episodes reaches 16/20 (80%) real-world pick-and-place success on the Oreo-package task. A policy fine-tuned on 105 real teleoperated episodes achieved 18/20 (90%) under the same protocol. These results are based on one object and 20 trials per policy and are therefore reported as preliminary evidence rather than a general performance claim.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34287v1
- Authors: Sergei Kurchev, Iaroslav Kolomiets, Filipp Maksimov, Elizaveta Semenyakina, Miguel Altamirano Cabrera, Artem Lykov, Dzmitry Tsetserukou
- Published: 2026-11-25T12:41:23Z
- Age days: 0

</details>
