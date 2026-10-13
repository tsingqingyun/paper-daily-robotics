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
url: "https://arxiv.org/abs/2610.13732v1"
published: "2026-10-09T15:29:20Z"
age_days: 3
score: 39
created: 2026-10-13
concepts: ["世界模型", "视觉语言动作模型 VLA"]
---

# LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> LAPT-Scale先从人类视频的前后画面学出连续的“隐含动作”，用它预训练机器人策略，再用真实机器人数据把输出转成可执行动作。关键是让隐含动作同时解释视觉结构和运动，减少静态背景对训练的干扰。

## 问题

机器人动作数据昂贵，人类第一视角视频虽然多，却没有机器人控制标签。显式估计手部运动可能产生噪声；离散动作码又可能压缩掉细微变化，单纯像素重建容易被静态区域主导[S4](https://arxiv.org/html/2610.13732v1#S1.p2.1) [S5](https://arxiv.org/html/2610.13732v1#S1.p3.1)。因此瓶颈不只是视频数量，而是能否从视频提取对控制有用的监督。

### 用一个例子理解

理解用例（非论文实验）：输入人手把抽屉拉开的前后帧；LAM生成解释开合变化的连续标签，策略先学习按场景预测这种变化，再用机器人拉抽屉数据校准；最终输入机器人图像和指令，输出机械臂动作。

## 创新点或方法

旧方法估计伪动作或用离散码解释画面；LAPT-Scale-LAM用连续变量解释前后帧变化，通过像素、感知、语义和光流约束保留手物交互。冻结LAM后，它给视频生成标签。策略始终沿用同一动作专家：先预测人类潜动作，再改学机器人动作，最后适配目标任务；不另加头或重新初始化[S17](https://arxiv.org/html/2610.13732v1#S3.SS2.p2.1) [S18](https://arxiv.org/html/2610.13732v1#S3.SS2.p4.1) [S19](https://arxiv.org/html/2610.13732v1#S3.SS2.p4.2) [S20](https://arxiv.org/html/2610.13732v1#S3.SS3.p1.1) [S21](https://arxiv.org/html/2610.13732v1#S3.SS3.p2.1) [S22](https://arxiv.org/html/2610.13732v1#S3.E5) [S23](https://arxiv.org/html/2610.13732v1#S3.SS3.p3.1)。部署直接输出机器人动作，无需LAM或未来视频。

### 方法如何工作

1. 从前后帧推断连续潜动作，并训练它帮助预测下一帧，让变量承载交互变化[S16](https://arxiv.org/html/2610.13732v1#S3.F3) [S17](https://arxiv.org/html/2610.13732v1#S3.SS2.p2.1)。
2. 加入感知、语义和光流约束，使预测兼顾物体结构与运动，而不只复制静态外观[S17](https://arxiv.org/html/2610.13732v1#S3.SS2.p2.1)。
3. 冻结LAM并标注清洗视频，训练策略预测潜动作序列，获得大量无需机器人标签的监督[S15](https://arxiv.org/html/2610.13732v1#S3.SS1.SSS0.Px2.p1.1) [S19](https://arxiv.org/html/2610.13732v1#S3.SS2.p4.2) [S20](https://arxiv.org/html/2610.13732v1#S3.SS3.p1.1)。
4. 用目标机器人数据把同一动作专家的目标改为可执行动作，再用任务数据后训练，建立形态与任务对应[S20](https://arxiv.org/html/2610.13732v1#S3.SS3.p1.1) [S49](https://arxiv.org/html/2610.13732v1#A2.SS1.p4.1)。
5. 部署时根据当前上下文生成机器人动作，潜动作仅承担预训练监督角色[S23](https://arxiv.org/html/2610.13732v1#S3.SS3.p3.1)。

### 必要术语

- 潜动作：从画面变化学出的隐含变量；不是现成关节命令。
- 连续潜空间：允许标签平滑变化而不局限于有限代码；用于保存细微交互变化。
- 形态对齐：用目标机器人的数据建立控制对应；把视频经验接到真实动作。
- 光流：画面中位置的位移信号；帮助LAM关注实际运动。

## 证据

LAM训练用23.3K小时视频，策略主实验用5.1K小时清洗子集，随后用250小时目标机器人数据对齐[S25](https://arxiv.org/html/2610.13732v1#S4.SS1.p1.1) [S26](https://arxiv.org/html/2610.13732v1#S4.SS1.p2.1)。固定机器人数据、架构与评测，视频从1K增至5K小时，真机成功率63.3%升至85.0%[S7](https://arxiv.org/html/2610.13732v1#S1.p5.1) [S37](https://arxiv.org/html/2610.13732v1#S4.SS3.p1.1)。同架构去掉视频预训练为55.0%，增加机器人训练以匹配计算量为53.3%，完整方案85.0%[S42](https://arxiv.org/html/2610.13732v1#S4.T4.2) [S50](https://arxiv.org/html/2610.13732v1#A5.SS1.p1.1)。三项原始真机任务各20次，JoyAI-RA平均80.0%，本文85.0%[S34](https://arxiv.org/html/2610.13732v1#S4.T3) [S35](https://arxiv.org/html/2610.13732v1#S4.T3.2)。这些对照支持视频监督的作用，但小样本不足以精确估计部署可靠性。

## 局限

作者明确说潜动作不保证对应机器人可独立控制的自由度，目标机器人对齐仍必需；遮挡、相机运动、弱操作信号和大形态差异都可能导致失败。真机仅一个平台、七个任务、每条件20次[S45](https://arxiv.org/html/2610.13732v1#S5.p2.1)。我的待核查问题是不同种类视频的收益与筛选成本，不能将观察到的扩量趋势外推为普遍规模定律。

- **判断**：值得深入读到同架构对照和数据筛选，因为它较清楚地回答了“多看人类视频是否真能帮助机器人”，同时保留了必要的机器人对齐环节。

## 研究关联

可借鉴的是把“视频里发生了什么变化”和“机器人该怎样驱动关节”分阶段学习。视频能先提供交互规律，机器人数据再建立控制对应；固定机器人数据的扩量实验比单纯跨模型排名更能检验视频是否有用。

### 下一步读哪里

先看[S17](https://arxiv.org/html/2610.13732v1#S3.SS2.p2.1) [S18](https://arxiv.org/html/2610.13732v1#S3.SS2.p4.1) [S19](https://arxiv.org/html/2610.13732v1#S3.SS2.p4.2) [S20](https://arxiv.org/html/2610.13732v1#S3.SS3.p1.1) [S21](https://arxiv.org/html/2610.13732v1#S3.SS3.p2.1) [S22](https://arxiv.org/html/2610.13732v1#S3.E5) [S23](https://arxiv.org/html/2610.13732v1#S3.SS3.p3.1)如何把潜动作监督切换为机器人动作，再看[S37](https://arxiv.org/html/2610.13732v1#S4.SS3.p1.1) [S38](https://arxiv.org/html/2610.13732v1#S4.F4) [S39](https://arxiv.org/html/2610.13732v1#S4.SS3.p2.1) [S40](https://arxiv.org/html/2610.13732v1#S4.SS4.p1.1) [S41](https://arxiv.org/html/2610.13732v1#S4.T4) [S42](https://arxiv.org/html/2610.13732v1#S4.T4.2)扩量与计算量对照。核查各对齐项的消融结果、任务后训练数据量，并注意[S46](https://arxiv.org/html/2610.13732v1#A2.SS1.p1.1)的官方DreamDojo基线与自训练重建对照不是同一模型。

- **概念**：世界模型 视觉语言动作模型 VLA
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.13732v1
- 获取时间：2026-10-13T00:21:45.817588+00:00
- [S1] [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos · 正文段落 1](https://arxiv.org/html/2610.13732v1#abstract1.1)
- [S2] [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos · 正文段落 2](https://arxiv.org/html/2610.13732v1#p2.1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.13732v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.13732v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.13732v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.13732v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.13732v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.13732v1#S1.I1.i2)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.13732v1#S1.I1.i3)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.13732v1#S1.F1)
- [S11] [Vision-language-action policy learning. · 正文段落 13](https://arxiv.org/html/2610.13732v1#S2.SS0.SSS0.Px1.p1.1)
- [S12] [Human video data for embodied learning. · 正文段落 14](https://arxiv.org/html/2610.13732v1#S2.SS0.SSS0.Px2.p1.1)
- [S13] [Latent action models from videos. · 正文段落 15](https://arxiv.org/html/2610.13732v1#S2.SS0.SSS0.Px3.p1.1)
- [S14] [Pipeline. · 正文段落 16](https://arxiv.org/html/2610.13732v1#S3.SS1.SSS0.Px1.p1.1)
- [S15] [Human-video data and filtering. · 正文段落 17](https://arxiv.org/html/2610.13732v1#S3.SS1.SSS0.Px2.p1.1)
- [S16] [3.2 LAPT-Scale-LAM: Constructing Human Latent-Action Supervision · 正文段落 19](https://arxiv.org/html/2610.13732v1#S3.F3)
- [S17] [3.2 LAPT-Scale-LAM: Constructing Human Latent-Action Supervision · 正文段落 21](https://arxiv.org/html/2610.13732v1#S3.SS2.p2.1)
- [S18] [3.2 LAPT-Scale-LAM: Constructing Human Latent-Action Supervision · 正文段落 25](https://arxiv.org/html/2610.13732v1#S3.SS2.p4.1)
- [S19] [3.2 LAPT-Scale-LAM: Constructing Human Latent-Action Supervision · 正文段落 27](https://arxiv.org/html/2610.13732v1#S3.SS2.p4.2)
- [S20] [3.3 LAPT-Scale-Policy: Three-Stage VLA Policy Training · 正文段落 28](https://arxiv.org/html/2610.13732v1#S3.SS3.p1.1)
- [S21] [3.3 LAPT-Scale-Policy: Three-Stage VLA Policy Training · 正文段落 29](https://arxiv.org/html/2610.13732v1#S3.SS3.p2.1)
- [S22] [3.3 LAPT-Scale-Policy: Three-Stage VLA Policy Training · 正文段落 30](https://arxiv.org/html/2610.13732v1#S3.E5)
- [S23] [3.3 LAPT-Scale-Policy: Three-Stage VLA Policy Training · 正文段落 31](https://arxiv.org/html/2610.13732v1#S3.SS3.p3.1)
- [S24] [4 Experiments · 正文段落 32](https://arxiv.org/html/2610.13732v1#S4.p1.1)
- [S25] [4.1 Experimental Setup · 正文段落 33](https://arxiv.org/html/2610.13732v1#S4.SS1.p1.1)
- [S26] [4.1 Experimental Setup · 正文段落 34](https://arxiv.org/html/2610.13732v1#S4.SS1.p2.1)
- [S27] [4.2 Main Results · 正文段落 35](https://arxiv.org/html/2610.13732v1#S4.SS2.p1.1)
- [S28] [4.2 Main Results · 正文段落 36](https://arxiv.org/html/2610.13732v1#S4.T1)
- [S29] [4.2 Main Results · 正文段落 37](https://arxiv.org/html/2610.13732v1#S4.T1.2)
- [S30] [4.2 Main Results · 正文段落 38](https://arxiv.org/html/2610.13732v1#S4.SS2.p2.1)
- [S31] [4.2 Main Results · 正文段落 39](https://arxiv.org/html/2610.13732v1#S4.T2)
- [S32] [4.2 Main Results · 正文段落 40](https://arxiv.org/html/2610.13732v1#S4.T2.2)
- [S33] [4.2 Main Results · 正文段落 41](https://arxiv.org/html/2610.13732v1#S4.SS2.p3.1)
- [S34] [4.2 Main Results · 正文段落 42](https://arxiv.org/html/2610.13732v1#S4.T3)
- [S35] [4.2 Main Results · 正文段落 43](https://arxiv.org/html/2610.13732v1#S4.T3.2)
- [S36] [4.2 Main Results · 正文段落 44](https://arxiv.org/html/2610.13732v1#S4.SS2.p4.1)
- [S37] [4.3 Scaling with Annotated Human Video · 正文段落 45](https://arxiv.org/html/2610.13732v1#S4.SS3.p1.1)
- [S38] [4.3 Scaling with Annotated Human Video · 正文段落 46](https://arxiv.org/html/2610.13732v1#S4.F4)
- [S39] [4.3 Scaling with Annotated Human Video · 正文段落 47](https://arxiv.org/html/2610.13732v1#S4.SS3.p2.1)
- [S40] [4.4 Controlled Stage-1 and Alignment Ablations · 正文段落 51](https://arxiv.org/html/2610.13732v1#S4.SS4.p1.1)
- [S41] [4.4 Controlled Stage-1 and Alignment Ablations · 正文段落 52](https://arxiv.org/html/2610.13732v1#S4.T4)
- [S42] [4.4 Controlled Stage-1 and Alignment Ablations · 正文段落 53](https://arxiv.org/html/2610.13732v1#S4.T4.2)
- [S43] [4.4 Controlled Stage-1 and Alignment Ablations · 正文段落 54](https://arxiv.org/html/2610.13732v1#S4.SS4.p2.1)
- [S44] [4.4 Controlled Stage-1 and Alignment Ablations · 正文段落 55](https://arxiv.org/html/2610.13732v1#S4.T5)
- [S45] [5 Conclusion and Limitations · 正文段落 74](https://arxiv.org/html/2610.13732v1#S5.p2.1)
- [S46] [B.1 LAM and Policy Training · 正文段落 85](https://arxiv.org/html/2610.13732v1#A2.SS1.p1.1)
- [S47] [B.1 LAM and Policy Training · 正文段落 86](https://arxiv.org/html/2610.13732v1#A2.SS1.p2.1)
- [S48] [B.1 LAM and Policy Training · 正文段落 87](https://arxiv.org/html/2610.13732v1#A2.SS1.p3.1)
- [S49] [B.1 LAM and Policy Training · 正文段落 88](https://arxiv.org/html/2610.13732v1#A2.SS1.p4.1)
- [S50] [E.1 Stage-1 Removal Control · 正文段落 113](https://arxiv.org/html/2610.13732v1#A5.SS1.p1.1)
- [S51] [E.1 Stage-1 Removal Control · 正文段落 115](https://arxiv.org/html/2610.13732v1#A5.T16.2)
- [S52] [F.1 Reconstruction Protocols · 正文段落 117](https://arxiv.org/html/2610.13732v1#A6.SS1.p2.1)
- [S53] [F.1 Reconstruction Protocols · 正文段落 118](https://arxiv.org/html/2610.13732v1#A6.SS1.p3.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/LAPT-Scale Scaling Embodied Policies with Latent Action Pre-Training on Human Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data. Large-scale egocentric human videos offer a rich alternative, but they lack robot action labels, and existing action annotation methods are often noisy under real-world visual complexity and diverse manipulation dynamics. We introduce LAPT-Scale, a scalable latent action pre-training paradigm with two components: LAPT-Scale-LAM learns continuous latent actions by explaining frame-to-frame visual transitions in human videos and uses them as human-derived supervision, while LAPT-Scale-Policy trains a VLA policy through human-video latent-action pre-training, target-robot embodiment alignment, and task-specific post-training. Unlike prior vector-quantized LAMs, LAPT-Scale-LAM uses a continuous latent space to preserve fine-grained motion and interaction dynamics. We further combine perceptual, semantic, and optical-flow alignment signals to improve transition-level supervision beyond pixel reconstruction. Trained on 23.3K hours of egocentric video, LAPT-Scale-LAM provides implicit action supervision for policy pre-training, yielding consistent scaling gains and improving real-robot success from 63.3% to 85.0% as annotated human video scales from 1K to 5K hours. The learned policy also generalizes to unseen visual conditions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.13732v1
- Authors: Zhiyuan Xiang, Peidong Liu, Mingyang Li, Jiawei Li, Wenhow Li, Wenbo Ding, Xiang Deng
- Published: 2026-10-09T15:29:20Z
- Age days: 3

</details>
