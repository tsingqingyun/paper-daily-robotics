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
url: "https://arxiv.org/abs/2610.26855v1"
published: "2026-10-19T17:59:55Z"
age_days: 1
score: 51
created: 2026-10-21
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Ropedia W0 用“相机怎么移动、手或机械臂骨架怎么移动”作为共同输入，让同一个模型预测人类和不同机器人接下来看到的视频。关键是统一运动的表达方式，同时保留各自身体结构，使大量人类经历能够参与机器人世界模型训练。

## 问题

任务是预测边走边操作时的第一视角未来视频。移动会改变整个画面，操作又涉及手与物体接触；不同机器人的关节命令还无法直接混用。现有方法常聚焦固定底座夹爪，跨身体迁移又需要专用动作接口；人类视频虽多，相机轨迹和手部标注却常缺失或不可靠[S5](https://arxiv.org/html/2610.26855v1#S1.p1.1) [S6](https://arxiv.org/html/2610.26855v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入机器人面前的厨房图像、走向柜子的相机轨迹和伸手的投影骨架；模型据此预测接近柜子、手进入画面的未来视频，供外部规划器检查候选动作的视觉后果。

## 创新点或方法

旧做法把各机器人的动作分别编码；本文改成用具有实际尺度的相机位姿描述移动，用投影到图像里的骨架描述操作。机器人骨架来自正向运动学及人工标注修正，因此统一的是接口，并非强行把身体变成一样。训练先用人类视频，再等概率混合人类与机器人数据，必要时针对目标数据后训练[S7](https://arxiv.org/html/2610.26855v1#S1.p3.1) [S14](https://arxiv.org/html/2610.26855v1#S4.SS3.p1.1) [S15](https://arxiv.org/html/2610.26855v1#S4.SS3.p2.1) [S16](https://arxiv.org/html/2610.26855v1#S4.SS3.p3.1)。推理根据图像、运动条件和文字生成未来视频；蒸馏后改为少步、连续生成，并不直接等于生成机器人控制策略。

### 方法如何工作

1. 整理视频的相机轨迹、骨架和文字，使不同来源的数据能通过同一接口进入模型。
2. 先在人类视频上学习运动与画面变化的关系，为机器人数据较少的情况提供基础。
3. 混入机器人原生骨架和视频，让模型学习机器人外观、几何及交互差异。
4. 推理时给定候选运动条件生成未来视频；需要实时交互时，再使用蒸馏后的流式生成版本。

### 必要术语

- 世界模型：预测动作之后环境会怎样变化；本文主要输出未来第一视角视频。
- 投影骨架：把身体关键点放到图像坐标中；连接运动条件与画面中的位置。
- 正向运动学：由关节状态算出身体部位位置；用于构造机器人骨架。

## 证据

测试覆盖五个机器人基准及未见人类视频。Xp-Teleop 上，A14B midtrain 无后训练的 PSNR/SSIM/LPIPS 为16.42/0.537/0.259，优于 Cosmos3-Nano 全数据后训练的14.98/0.508/0.293[S26](https://arxiv.org/html/2610.26855v1#S6.T4.4)。人类测试含200段未见视频[S19](https://arxiv.org/html/2610.26855v1#S6.SS2.p1.1)。这些支持视频预测与数据迁移能力；不能单凭图像指标证明接触物理准确。下游控制效果在[S8](https://arxiv.org/html/2610.26855v1#S1.p4.1)有定性结论，节选未给具体数值。

## 局限

这里的零样本指未训练过目标数据集，目标机器人身体仍可能出现在其他训练集里[S18](https://arxiv.org/html/2610.26855v1#S6.SS1.SSS0.Px3.p1.1)，不能据此宣称适应全新身体。我的待核查问题是：长视频中物体状态和接触错误如何累积，以及几何标注的人工成本有多高。

- **判断**：值得细读运动接口与数据处理，再核查控制实验；目前最扎实的理由是跨数据集视频预测，而非已经得到通用物理模拟器。

## 研究关联

值得借鉴的是：混合不同身体的数据前，先寻找共同可观测的运动后果，而非直接拼接关节命令。前提是能获得可靠相机轨迹和骨架；这也把标注质量变成方法成立的重要条件。

### 下一步读哪里

先看[S7](https://arxiv.org/html/2610.26855v1#S1.p3.1) [S14](https://arxiv.org/html/2610.26855v1#S4.SS3.p1.1) [S15](https://arxiv.org/html/2610.26855v1#S4.SS3.p2.1) [S16](https://arxiv.org/html/2610.26855v1#S4.SS3.p3.1)的条件与训练衔接，再对照[S18](https://arxiv.org/html/2610.26855v1#S6.SS1.SSS0.Px3.p1.1) [S26](https://arxiv.org/html/2610.26855v1#S6.T4.4)理解迁移范围。下一步核查骨架如何生成、相机与骨架消融是否控制数据量，以及策略排序和规划是否预测真实成功。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：51
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.26855v1
- 获取时间：2026-10-21T00:33:47.568748+00:00
- [S1] [Ropedia W0 · 正文段落 1](https://arxiv.org/html/2610.26855v1#abstract1.1)
- [S2] [Ropedia W0 · 正文段落 2](https://arxiv.org/html/2610.26855v1#p1.1)
- [S3] [Ropedia W0 · 正文段落 3](https://arxiv.org/html/2610.26855v1#p2.1)
- [S4] [Ropedia W0 · 正文段落 4](https://arxiv.org/html/2610.26855v1#p4.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.26855v1#S1.p1.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.26855v1#S1.p2.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.26855v1#S1.p3.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.26855v1#S1.p4.1)
- [S9] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.26855v1#S1.I1.i3)
- [S10] [2 Related Work · 正文段落 13](https://arxiv.org/html/2610.26855v1#S2.p1.1)
- [S11] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.26855v1#S2.p2.1)
- [S12] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.26855v1#S2.p3.1)
- [S13] [4.2 Architecture: Kinematics-Conditioned World Model · 正文段落 44](https://arxiv.org/html/2610.26855v1#S4.SS2.p2.2)
- [S14] [4.3 Training: From Human Experience to Cross-Embodiment · 正文段落 46](https://arxiv.org/html/2610.26855v1#S4.SS3.p1.1)
- [S15] [4.3 Training: From Human Experience to Cross-Embodiment · 正文段落 47](https://arxiv.org/html/2610.26855v1#S4.SS3.p2.1)
- [S16] [4.3 Training: From Human Experience to Cross-Embodiment · 正文段落 48](https://arxiv.org/html/2610.26855v1#S4.SS3.p3.1)
- [S17] [4.4 Distillation: Real-Time Interactive Rollouts · 正文段落 49](https://arxiv.org/html/2610.26855v1#S4.SS4.p1.1)
- [S18] [Post-training protocol. · 正文段落 59](https://arxiv.org/html/2610.26855v1#S6.SS1.SSS0.Px3.p1.1)
- [S19] [6.2 Benchmark Results · 正文段落 61](https://arxiv.org/html/2610.26855v1#S6.SS2.p1.1)
- [S20] [6.2 Benchmark Results · 正文段落 63](https://arxiv.org/html/2610.26855v1#S6.T2.4)
- [S21] [6.2 Benchmark Results · 正文段落 64](https://arxiv.org/html/2610.26855v1#S6.T2.5)
- [S22] [6.2 Benchmark Results · 正文段落 65](https://arxiv.org/html/2610.26855v1#S6.SS2.p2.1)
- [S23] [6.2 Benchmark Results · 正文段落 66](https://arxiv.org/html/2610.26855v1#S6.T3)
- [S24] [6.2 Benchmark Results · 正文段落 68](https://arxiv.org/html/2610.26855v1#S6.SS2.p3.1)
- [S25] [6.2 Benchmark Results · 正文段落 69](https://arxiv.org/html/2610.26855v1#S6.T4)
- [S26] [6.2 Benchmark Results · 正文段落 70](https://arxiv.org/html/2610.26855v1#S6.T4.4)
- [S27] [6.2 Benchmark Results · 正文段落 71](https://arxiv.org/html/2610.26855v1#S6.SS2.p4.1)
- [S28] [6.2 Benchmark Results · 正文段落 72](https://arxiv.org/html/2610.26855v1#S6.SS2.p5.1)
- [S29] [Distillation recipe. · 正文段落 122](https://arxiv.org/html/2610.26855v1#A2.SS2.SSS0.Px1.p2.1)
- [S30] [Distillation recipe. · 正文段落 125](https://arxiv.org/html/2610.26855v1#A2.F5)
- [S31] [Pretrained initialization under limited data. · 正文段落 178](https://arxiv.org/html/2610.26855v1#A5.SS3.SSS0.Px2.p1.1)
- [S32] [Pretrained initialization under limited data. · 正文段落 179](https://arxiv.org/html/2610.26855v1#A5.F16)
- [S33] [Pretrained initialization under limited data. · 正文段落 180](https://arxiv.org/html/2610.26855v1#A5.F17)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/Ropedia W0 Scaling Loco-Manipulation World Models across Embodiments with Human.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotations and systematic quality control. A unified kinematic representation encodes locomotion through camera poses and manipulation through projected skeletons, with robot skeletons combining embodiment-specific forward kinematics with extensive manual keypoint annotation and correction. We also introduce Xp-Teleop, a long-horizon loco-manipulation benchmark based on high-quality dexterous humanoid teleoperation data. Evaluations demonstrate state-of-the-art performance across five cross-embodiment benchmarks (DreamDojo, $Ψ_0$, $ω$-HOME, Xp-Teleop, and AgiBot) and on held-out human egocentric video, from zero-shot inference to few-shot and full-data post-training. Scaling human pre-training data improves performance on both human and robot evaluations. After distillation, our model supports real-time, minute-long rollouts, enabling live VR interaction. Applications in policy evaluation, model-based planning, and world-action modeling further demonstrate the model's utility for embodied decision-making.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.26855v1
- Authors: Tianqi Liu, Hanfei Zhao, Qifeng Liang, Hui En Pang, Jiarui Xu, Sayang Mu, Penghao Qiu, YingSheng Zhang, Jun Wang, Ziang Cao, Mingze Sun, Yukang Cao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- Published: 2026-10-19T17:59:55Z
- Age days: 1

</details>
