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
url: "https://arxiv.org/abs/2610.40109v1"
published: "2026-10-29T14:12:07Z"
age_days: 3
score: 28
created: 2026-11-02
concepts: ["具身智能评测与基准"]
---

# Coupled Guidance for Flow Matching

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Coupled Guidance 解决流匹配模型被外加约束引导后容易失稳的问题。它在调整预测结果的同时协调调整噪声端表示，避免采样偏离训练时学过的噪声—数据配对关系。

## 问题

机器人原本会抓方块，途中新添障碍后，需要在采样时改轨迹而不重训策略。直接搬用扩散引导可能把中间状态推到模型不熟悉的位置：约束方向看似正确，模型后续预测却更不可靠。[S3](https://arxiv.org/html/2610.40109v1#S1.p2.1) [S7](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px2.p2.1)

### 用一个例子理解

理解用例（非论文实验）：输入机械臂状态和新障碍的位置；原策略生成抓取轨迹，碰撞代价建议绕行，Coupled Guidance 协调两端修正；输出重新采样的动作序列，仍需执行检测。

## 创新点或方法

训练时，流匹配在配对的噪声与数据之间插值，学习运动方向；本文不改变这个基础训练。推理时，旧方法直接修改采样更新，本文把更新改写成两端的协调修正：保留原有数据引导，修改潜变量端引导，使配对更接近训练结构。[S15](https://arxiv.org/html/2610.40109v1#S3.SS2.p1.1) [S16](https://arxiv.org/html/2610.40109v1#S3.SS2.p2.1) [S17](https://arxiv.org/html/2610.40109v1#S3.Ex3) [S18](https://arxiv.org/html/2610.40109v1#S3.SS2.p2.2) [S19](https://arxiv.org/html/2610.40109v1#S3.SS2.p3.1) [S20](https://arxiv.org/html/2610.40109v1#S3.E1) [S29](https://arxiv.org/html/2610.40109v1#S4.SS1.p1.1) [S30](https://arxiv.org/html/2610.40109v1#S4.SS1.p5.1) 节选未给完整更新式，不能据此写出可复现算法。

### 方法如何工作

1. 基础模型沿训练中的噪声—数据插值学习速度，形成采样所依赖的配对结构。
2. 采样时估计最终结果，并用观测约束或碰撞代价计算数据端修正。
3. 同步设置潜变量端修正，减轻单边引导造成的配对漂移。
4. 继续积分得到图像或动作轨迹；具体离散更新需查完整公式，节选只说明到此。

### 必要术语

- 耦合分布：噪声与目标数据怎样配对的联合分布；是本文分析引导失稳的核心。
- 潜变量端：这里指生成起点的噪声表示；本文对它增加协调修正。
- Jacobian：输出估计对当前状态的变化率；部分引导依赖它，偏离训练配对时可能放大不稳定。

## 证据

ManiSkill3 PickCube 策略在原环境成功率99.8%；添加障碍后，无引导约21%，朴素能量引导最高36%，耦合引导最高81%，表注说明测试256个环境种子。[S33](https://arxiv.org/html/2610.40109v1#S5.T2) [S34](https://arxiv.org/html/2610.40109v1#S5.SS1.p2.1) [S35](https://arxiv.org/html/2610.40109v1#S5.SS1.p3.1) 还测试 Adroit 四任务，以及 ImageNet-128、CelebA-HQ-256 的补全、超分和去模糊。图像节选给出方法间表现，但未提供数值表和具体指标名，无法量化这些收益。

## 局限

作者的理论讨论有假设，独立配对下的密度比分解也只是简化分析。[S25](https://arxiv.org/html/2610.40109v1#S3.SS4.SSS0.Px1.p1.2) [S26](https://arxiv.org/html/2610.40109v1#S3.SS4.SSS0.Px2.p1.1) [S27](https://arxiv.org/html/2610.40109v1#S3.SS4.SSS0.Px2.p2.1) 实验并非所有方法都同样受益：超分中耦合对 ΠGDM+ 几乎无帮助，去模糊中它又优于耦合 ΠGDM。[S41](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px2.p1.1) [S42](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px3.p1.1) 机器人证据来自仿真；“几乎无额外开销”仍需核查计时口径和基线本身的导数成本。

- **判断**：已有流匹配采样器需要加约束时，值得读到更新公式和稳定性分析；收益依赖具体引导算子，不能当作通用替换件。

## 研究关联

可以借鉴的诊断顺序是：引导越强反而越差时，先检查它是否把生成过程带离训练分布，而不只调整约束权重。这里把问题落实到噪声端与数据端的配对，提供了比“梯度太大”更具体的解释。

### 下一步读哪里

优先核查第4.1节完整更新式中两端如何重组、参数如何选；结合[S40](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px1.p1.1) [S41](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px2.p1.1) [S42](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px3.p1.1) [S43](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px4.p1.1)看何时稳定、何时无效。避障比较应按[S48](https://arxiv.org/html/2610.40109v1#A2.SS1.p4.1)理解为能量引导，不能误当成直接使用 ΠGDM。

- **概念**：具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.40109v1
- 获取时间：2026-11-02T01:18:50.050400+00:00
- [S1] [Coupled Guidance for Flow Matching · 正文段落 1](https://arxiv.org/html/2610.40109v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.40109v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.40109v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.40109v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.40109v1#S1.p3.1)
- [S6] [Guidance Methods · 正文段落 9](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px2.p1.1)
- [S7] [Guidance Methods · 正文段落 10](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px2.p2.1)
- [S8] [Base Methods · 正文段落 11](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px3.p1.1)
- [S9] [Base Methods · 正文段落 12](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px3.p2.1)
- [S10] [Base Methods · 正文段落 13](https://arxiv.org/html/2610.40109v1#S2.Ex1)
- [S11] [Base Methods · 正文段落 14](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px3.p2.2)
- [S12] [Base Methods · 正文段落 15](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px3.p3.1)
- [S13] [Base Methods · 正文段落 16](https://arxiv.org/html/2610.40109v1#S2.Ex2)
- [S14] [Base Methods · 正文段落 17](https://arxiv.org/html/2610.40109v1#S2.SS0.SSS0.Px3.p3.2)
- [S15] [3.2 Flow-Matching Training and Inference · 正文段落 19](https://arxiv.org/html/2610.40109v1#S3.SS2.p1.1)
- [S16] [3.2 Flow-Matching Training and Inference · 正文段落 20](https://arxiv.org/html/2610.40109v1#S3.SS2.p2.1)
- [S17] [3.2 Flow-Matching Training and Inference · 正文段落 21](https://arxiv.org/html/2610.40109v1#S3.Ex3)
- [S18] [3.2 Flow-Matching Training and Inference · 正文段落 22](https://arxiv.org/html/2610.40109v1#S3.SS2.p2.2)
- [S19] [3.2 Flow-Matching Training and Inference · 正文段落 23](https://arxiv.org/html/2610.40109v1#S3.SS2.p3.1)
- [S20] [3.2 Flow-Matching Training and Inference · 正文段落 24](https://arxiv.org/html/2610.40109v1#S3.E1)
- [S21] [3.2 Flow-Matching Training and Inference · 正文段落 25](https://arxiv.org/html/2610.40109v1#S3.SS2.p3.2)
- [S22] [3.2 Flow-Matching Training and Inference · 正文段落 26](https://arxiv.org/html/2610.40109v1#S3.E2)
- [S23] [3.3 From Guided Flow to Coupled Guidance · 正文段落 32](https://arxiv.org/html/2610.40109v1#S3.SS3.p2.3)
- [S24] [3.4 Training Coupling versus Guided Coupling · 正文段落 44](https://arxiv.org/html/2610.40109v1#S3.SS4.p1.1)
- [S25] [Assumptions. · 正文段落 50](https://arxiv.org/html/2610.40109v1#S3.SS4.SSS0.Px1.p1.2)
- [S26] [Interpretation. · 正文段落 54](https://arxiv.org/html/2610.40109v1#S3.SS4.SSS0.Px2.p1.1)
- [S27] [Interpretation. · 正文段落 56](https://arxiv.org/html/2610.40109v1#S3.SS4.SSS0.Px2.p2.1)
- [S28] [Conclusion. · 正文段落 60](https://arxiv.org/html/2610.40109v1#S3.SS4.SSS0.Px3.p1.1)
- [S29] [4.1 Coupled Guidance Algorithm · 正文段落 61](https://arxiv.org/html/2610.40109v1#S4.SS1.p1.1)
- [S30] [4.1 Coupled Guidance Algorithm · 正文段落 69](https://arxiv.org/html/2610.40109v1#S4.SS1.p5.1)
- [S31] [4.1 Coupled Guidance Algorithm · 正文段落 72](https://arxiv.org/html/2610.40109v1#S4.T1)
- [S32] [5.1 Collision Avoidance · 正文段落 73](https://arxiv.org/html/2610.40109v1#S5.SS1.p1.1)
- [S33] [5.1 Collision Avoidance · 正文段落 74](https://arxiv.org/html/2610.40109v1#S5.T2)
- [S34] [5.1 Collision Avoidance · 正文段落 76](https://arxiv.org/html/2610.40109v1#S5.SS1.p2.1)
- [S35] [5.1 Collision Avoidance · 正文段落 77](https://arxiv.org/html/2610.40109v1#S5.SS1.p3.1)
- [S36] [5.2 Robotic Control as an Inpainting Task · 正文段落 78](https://arxiv.org/html/2610.40109v1#S5.F2)
- [S37] [5.2 Robotic Control as an Inpainting Task · 正文段落 79](https://arxiv.org/html/2610.40109v1#S5.SS2.p1.1)
- [S38] [5.2 Robotic Control as an Inpainting Task · 正文段落 84](https://arxiv.org/html/2610.40109v1#S5.SS2.p5.1)
- [S39] [5.3 Image Generation · 正文段落 87](https://arxiv.org/html/2610.40109v1#S5.SS3.p2.1)
- [S40] [Inpainting · 正文段落 90](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px1.p1.1)
- [S41] [Super-resolution · 正文段落 91](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px2.p1.1)
- [S42] [Deblurring · 正文段落 92](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px3.p1.1)
- [S43] [Jacobian Influence · 正文段落 94](https://arxiv.org/html/2610.40109v1#S5.SS3.SSS0.Px4.p1.1)
- [S44] [7 Conclusion · 正文段落 97](https://arxiv.org/html/2610.40109v1#S7.p1.1)
- [S45] [B.1 Baseline selection · 正文段落 114](https://arxiv.org/html/2610.40109v1#A2.SS1.p1.1)
- [S46] [B.1 Baseline selection · 正文段落 115](https://arxiv.org/html/2610.40109v1#A2.SS1.p2.1)
- [S47] [B.1 Baseline selection · 正文段落 116](https://arxiv.org/html/2610.40109v1#A2.SS1.p3.1)
- [S48] [B.1 Baseline selection · 正文段落 117](https://arxiv.org/html/2610.40109v1#A2.SS1.p4.1)
- [S49] [B.1 Baseline selection · 正文段落 118](https://arxiv.org/html/2610.40109v1#A2.Ex19)
- [S50] [B.2 Robotics · 正文段落 119](https://arxiv.org/html/2610.40109v1#A2.SS2.p1.1)
- [S51] [C.1 Robotics · 正文段落 123](https://arxiv.org/html/2610.40109v1#A3.SS1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/Coupled Guidance for Flow Matching.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Guidance methods are essential tools for steering the generation process in diffusion models, improving the generalizability of stochastic robotic controllers and enabling high-quality controlled image synthesis. Despite strong parallels between flow-matching and diffusion, integrating guidance into flow-matching models remains quite challenging. Recent work has proposed general guidance frameworks for flow-matching, however, they are direct adaptations of diffusion guidance methods and can prove unstable. In this work, we conduct a theoretical analysis of guidance in flow-matching and show that a naive translation of diffusion-based guidance to flow-matching breaks the coupling distribution used during training, resulting in weaker control over sampling accuracy. Building on this insight, we propose Coupled Guidance, a flow-matching-specific guidance mechanism derived from a geometric perspective that leverages the coupling structure inherent to flow-matching training. To validate the effectiveness of our approach, we conduct extensive experimentation on a custom robotic collision avoidance task using ManiSkill3, four robotic dexterous manipulation tasks from the Adroit benchmark, and three image generation tasks, namely inpainting, super-resolution, and deblurring, using the ImageNet-128 and CelebA-HQ-256 datasets. Our findings show that our framework improves sample quality and guidance stability across all tasks, without imposing any additional overhead.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.40109v1
- Authors: Mateo Clémente, Léo Maxime Brunswic, Rui Heng Yang, Amir Rasouli
- Published: 2026-10-29T14:12:07Z
- Age days: 3

</details>
