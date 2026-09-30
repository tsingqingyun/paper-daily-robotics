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
url: "https://arxiv.org/abs/2609.37530v1"
published: "2026-09-29T13:16:37Z"
age_days: 0
score: 39
created: 2026-09-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RawVLA 把“怎么把相机原始信号变成图片”也纳入训练，让画面处理服务于机器人做对动作，原有动作模型保持冻结。真机实验显示，在低光下调整这层处理，就能明显改善同一个动作策略的表现。

## 问题

机器人动作模型通常直接接收相机处理好的 RGB 图像，因此容易把相机处理当成无关紧要的前置步骤。但曝光、色彩、明暗压缩和去噪可能抹掉抓取需要的细节：同一个场景，只换成像设置，机器人就可能做出不同动作。本文固定场景、任务和机器人状态，逐项改变成像因素，检查问题究竟出在哪。[S3](https://arxiv.org/html/2609.37530v1#S1.p1.1) [S4](https://arxiv.org/html/2609.37530v1#S1.p2.1) [S5](https://arxiv.org/html/2609.37530v1#S1.p4.1)

### 用一个例子理解

理解用例（非论文实验）：机器人在暗处拿杯子。相机连续画面先经过 RawVLA，由它结合历史调整亮度、色彩和噪声，再交给已经训练好的抓取策略。比较默认处理与 RawVLA 时，动作策略和任务保持一致，观察到底是不是看清了才抓得更准。

## 创新点或方法

RawVLA 接收连续的线性 RAW 图像，结合历史状态和上一组处理参数，分别调整亮度与色彩；多帧信息还用于去噪，再输出 RGB 给原动作策略。[S11](https://arxiv.org/html/2609.37530v1#S2.F3) [S12](https://arxiv.org/html/2609.37530v1#S3.p1.1) [S13](https://arxiv.org/html/2609.37530v1#S3.SS1.p1.1) [S14](https://arxiv.org/html/2609.37530v1#S3.SS1.p1.2) 训练时冻结动作策略，让动作误差通过图像反传，只更新图像处理模块，并加入亮度和色彩约束。每个策略单独训练一个模块，运行时按视频流持续调整。[S15](https://arxiv.org/html/2609.37530v1#S3.SS4.p1.1) [S16](https://arxiv.org/html/2609.37530v1#S3.SS4.p1.2) [S17](https://arxiv.org/html/2609.37530v1#S3.SS4.p2.1) [S18](https://arxiv.org/html/2609.37530v1#S3.SS4.p2.3) [S31](https://arxiv.org/html/2609.37530v1#A4.SS1.p1.1) [S33](https://arxiv.org/html/2609.37530v1#A4.SS3.p2.1) 训练不使用配对 RGB 重建损失；默认光照下的配对 RGB 仅用于无梯度的检查点选择。[S31](https://arxiv.org/html/2609.37530v1#A4.SS1.p1.1) [S38](https://arxiv.org/html/2609.37530v1#A4.SS3.p5.1)

### 方法如何工作

1. 固定任务和机器人状态，分别改变曝光、噪声、色彩、明暗响应与位深，找出哪些成像变化最影响动作。[S5](https://arxiv.org/html/2609.37530v1#S1.p4.1)
2. 结合当前图像、历史状态和上一组参数调整亮度与色彩，并利用连续帧去噪。[S11](https://arxiv.org/html/2609.37530v1#S2.F3) [S12](https://arxiv.org/html/2609.37530v1#S3.p1.1) [S13](https://arxiv.org/html/2609.37530v1#S3.SS1.p1.1) [S14](https://arxiv.org/html/2609.37530v1#S3.SS1.p1.2) [S33](https://arxiv.org/html/2609.37530v1#A4.SS3.p2.1)
3. 把处理后的 RGB 交给冻结动作策略；训练时按动作误差和光度约束更新图像处理模块。[S15](https://arxiv.org/html/2609.37530v1#S3.SS4.p1.1) [S16](https://arxiv.org/html/2609.37530v1#S3.SS4.p1.2) [S17](https://arxiv.org/html/2609.37530v1#S3.SS4.p2.1) [S18](https://arxiv.org/html/2609.37530v1#S3.SS4.p2.3) [S31](https://arxiv.org/html/2609.37530v1#A4.SS1.p1.1)
4. 在正常与不利光照下比较同一策略的任务成功率，检查改进是否来自输入处理。[S19](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px2.p1.1) [S24](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px6.p1.1)

### 必要术语

- RAW：相机常规成像处理之前的图像信号；本文模块使用线性 RAW 表示，仿真输入则是三通道伪 RAW。
- ISP：把相机信号处理成 RGB 图像的流程，包括曝光、色彩、明暗与去噪等操作。
- 动作驱动训练：按机器人动作误差来优化图像处理，让画面更适合完成任务。

## 证据

最直观的证据来自四项真机双臂任务，动作底座是已经微调的 π₀.₅。正常光照下，RawVLA、默认图像处理和 DarkISP 的平均成功率分别为 75.0%、76.5%、50.0%；低光下分别为 66.5%、0%、11.0%。这说明在这些任务上，改图像处理能恢复暗光下的操作能力，同时大体保持正常光下的表现。[S24](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px6.p1.1) 仿真还覆盖 LIBERO 与 RoboTwin 2.0；LIBERO 的跨底座平均成功率从最强对照的 43.01% 提到 68.82%。[S20](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px4.p1.1) 论文报告的 168 FPS 仅是图像处理模块速度，不能当作整个机器人策略的控制频率。[S24](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px6.p1.1)

## 局限

这些结果还不能回答换一台相机会怎样：仿真使用三通道线性伪 RAW，没有完整模拟真实传感器的光谱响应、去马赛克、镜头和厂商处理差异。[S29](https://arxiv.org/html/2609.37530v1#A1.SS0.SSS0.Px1.p4.2) [S45](https://arxiv.org/html/2609.37530v1#A10.p1.1) 当前还要为每个下游策略单独训练模块，真机测试限于少量室内任务和光照条件；跨相机、户外、运动模糊及多种退化叠加仍需验证。[S46](https://arxiv.org/html/2609.37530v1#A10.p2.1) 雾天扩展实验用的是合成 RGB，不能算真实 RAW 恶劣天气验证。[S42](https://arxiv.org/html/2609.37530v1#A6.SS0.SSS0.Px1.p1.2) [S46](https://arxiv.org/html/2609.37530v1#A10.p2.1)

- **判断**：已有机器人在暗光下表现差，值得优先读。先确认能否拿到相机 RAW 数据；论文需要为每个动作策略单独训练图像处理模块。

## 研究关联

机器人一换光照就失灵时，先检查相机输出丢了什么信息，再决定是否重训动作模型。一个直接可做的对照是固定策略和任务，只换图像处理；这能把感知输入的问题与策略本身的问题分开。

### 下一步读哪里

先看 [S24](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px6.p1.1) 的真机光照对照，再按 [S31](https://arxiv.org/html/2609.37530v1#A4.SS1.p1.1) [S32](https://arxiv.org/html/2609.37530v1#A4.SS3.p1.1) [S33](https://arxiv.org/html/2609.37530v1#A4.SS3.p2.1) [S34](https://arxiv.org/html/2609.37530v1#A4.SS3.p3.1) [S35](https://arxiv.org/html/2609.37530v1#A4.SS3.p4.1) [S36](https://arxiv.org/html/2609.37530v1#A4.T6) [S37](https://arxiv.org/html/2609.37530v1#A4.T6.2) [S38](https://arxiv.org/html/2609.37530v1#A4.SS3.p5.1) 核查冻结策略、损失和历史帧的用法。接入前重点确认相机能否提供模块需要的线性输入，并读 [S45](https://arxiv.org/html/2609.37530v1#A10.p1.1) [S46](https://arxiv.org/html/2609.37530v1#A10.p2.1) 判断自己的场景超出了哪些已验证条件；不要把 [S19](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px2.p1.1) 的一般基准 rollout 设置直接套成真机样本量。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2609.37530v1
- 获取时间：2026-09-30T16:28:12.506316+00:00
- [S1] [RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2609.37530v1#abstract1.1)
- [S2] [RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation · 正文段落 2](https://arxiv.org/html/2609.37530v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2609.37530v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2609.37530v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 6](https://arxiv.org/html/2609.37530v1#S1.p4.1)
- [S6] [1 Introduction · 正文段落 11](https://arxiv.org/html/2609.37530v1#S1.I1.i3)
- [S7] [Exposure. · 正文段落 15](https://arxiv.org/html/2609.37530v1#S2.F2)
- [S8] [Sensor Noise. · 正文段落 16](https://arxiv.org/html/2609.37530v1#S2.SS0.SSS0.Px2.p1.1)
- [S9] [Chromatic Response. · 正文段落 17](https://arxiv.org/html/2609.37530v1#S2.SS0.SSS0.Px3.p1.1)
- [S10] [Tonal Response. · 正文段落 18](https://arxiv.org/html/2609.37530v1#S2.SS0.SSS0.Px4.p1.1)
- [S11] [Bit Depth. · 正文段落 20](https://arxiv.org/html/2609.37530v1#S2.F3)
- [S12] [3 RawVLA · 正文段落 21](https://arxiv.org/html/2609.37530v1#S3.p1.1)
- [S13] [3.1 Causal Streaming Formulation · 正文段落 22](https://arxiv.org/html/2609.37530v1#S3.SS1.p1.1)
- [S14] [3.1 Causal Streaming Formulation · 正文段落 24](https://arxiv.org/html/2609.37530v1#S3.SS1.p1.2)
- [S15] [3.4 Action-Driven Optimization · 正文段落 44](https://arxiv.org/html/2609.37530v1#S3.SS4.p1.1)
- [S16] [3.4 Action-Driven Optimization · 正文段落 46](https://arxiv.org/html/2609.37530v1#S3.SS4.p1.2)
- [S17] [3.4 Action-Driven Optimization · 正文段落 47](https://arxiv.org/html/2609.37530v1#S3.SS4.p2.1)
- [S18] [3.4 Action-Driven Optimization · 正文段落 51](https://arxiv.org/html/2609.37530v1#S3.SS4.p2.3)
- [S19] [Baseline Methods. · 正文段落 57](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px2.p1.1)
- [S20] [Evaluation on LIBERO. · 正文段落 59](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px4.p1.1)
- [S21] [Evaluation on RoboTwin 2.0. · 正文段落 60](https://arxiv.org/html/2609.37530v1#S5.T4.fig1)
- [S22] [Evaluation on RoboTwin 2.0. · 正文段落 62](https://arxiv.org/html/2609.37530v1#S5.T4.fig2)
- [S23] [Evaluation on RoboTwin 2.0. · 正文段落 66](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px5.p1.1)
- [S24] [Evaluation on Real-World Dual-Arm. · 正文段落 67](https://arxiv.org/html/2609.37530v1#S5.SS0.SSS0.Px6.p1.1)
- [S25] [6 Ablation · 正文段落 68](https://arxiv.org/html/2609.37530v1#S6.T5)
- [S26] [6 Ablation · 正文段落 69](https://arxiv.org/html/2609.37530v1#S6.T5.2.1)
- [S27] [6 Ablation · 正文段落 70](https://arxiv.org/html/2609.37530v1#S6.p1.1)
- [S28] [8 Conclusion · 正文段落 75](https://arxiv.org/html/2609.37530v1#S8.p1.1)
- [S29] [RAW Input Representation. · 正文段落 89](https://arxiv.org/html/2609.37530v1#A1.SS0.SSS0.Px1.p4.2)
- [S30] [Appendix D Neural ISP Training Protocol · 正文段落 124](https://arxiv.org/html/2609.37530v1#A4.p1.1)
- [S31] [D.1 Frozen-Policy Training Protocol · 正文段落 125](https://arxiv.org/html/2609.37530v1#A4.SS1.p1.1)
- [S32] [D.3 RawVLA Training and Temporal Sampling · 正文段落 129](https://arxiv.org/html/2609.37530v1#A4.SS3.p1.1)
- [S33] [D.3 RawVLA Training and Temporal Sampling · 正文段落 130](https://arxiv.org/html/2609.37530v1#A4.SS3.p2.1)
- [S34] [D.3 RawVLA Training and Temporal Sampling · 正文段落 131](https://arxiv.org/html/2609.37530v1#A4.SS3.p3.1)
- [S35] [D.3 RawVLA Training and Temporal Sampling · 正文段落 132](https://arxiv.org/html/2609.37530v1#A4.SS3.p4.1)
- [S36] [D.3 RawVLA Training and Temporal Sampling · 正文段落 133](https://arxiv.org/html/2609.37530v1#A4.T6)
- [S37] [D.3 RawVLA Training and Temporal Sampling · 正文段落 134](https://arxiv.org/html/2609.37530v1#A4.T6.2)
- [S38] [D.3 RawVLA Training and Temporal Sampling · 正文段落 135](https://arxiv.org/html/2609.37530v1#A4.SS3.p5.1)
- [S39] [Appendix F Additional Robustness Evaluation under Severe Haze · 正文段落 141](https://arxiv.org/html/2609.37530v1#A6.p1.1)
- [S40] [Experimental Setting. · 正文段落 142](https://arxiv.org/html/2609.37530v1#A6.SS0.SSS0.Px1.p1.1)
- [S41] [Experimental Setting. · 正文段落 143](https://arxiv.org/html/2609.37530v1#A6.E25)
- [S42] [Experimental Setting. · 正文段落 144](https://arxiv.org/html/2609.37530v1#A6.SS0.SSS0.Px1.p1.2)
- [S43] [Training Objectives. · 正文段落 157](https://arxiv.org/html/2609.37530v1#A7.T8)
- [S44] [Temporal Stability. · 正文段落 178](https://arxiv.org/html/2609.37530v1#A7.F14)
- [S45] [Appendix J Limitations and Future Studies · 正文段落 199](https://arxiv.org/html/2609.37530v1#A10.p1.1)
- [S46] [Appendix J Limitations and Future Studies · 正文段落 200](https://arxiv.org/html/2609.37530v1#A10.p2.1)
- [S47] [K.3 RoboTwin 2.0 Perturbation Settings · 正文段落 228](https://arxiv.org/html/2609.37530v1#A11.SS3.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/RawVLA Embodied Neural Image Signal Processor For Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models typically operate on RGB images produced by a fixed camera image signal processor (ISP), leaving the imaging pipeline outside the learning and evaluation loop. We systematically examine the consequences of this overlooked design choice across five fundamental ISP dimensions: gain, sensor noise, chromatic response, tonal response, and bit depth. Our analysis reveals that RAW-to-RGB processing materially shapes both action prediction and manipulation success, with different ISP dimensions exerting substantially different effects. Guided by these findings, we introduce RawVLA, a streaming neural ISP that adaptively renders RAW observations for frozen VLA policies while concentrating its capacity on the imaging factors relevant to embodied behavior. We further present RawVLA-Bench, a RAW-domain manipulation benchmark to expose image processing as an explicit evaluation variable across clean and adverse acquisition conditions. Experiments on RawVLA-Bench show that RawVLA preserves performance under standard conditions while substantially improving robustness under degraded imaging, establishing adaptive RAW processing as an effective interface between physical cameras and embodied policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37530v1
- Authors: Shuhong Liu, Heng Zhou, Lingfeng Qian, Yuhao Fang, Xianbao Hou, Qianyu Zhou, Lin Gu, Wei Sui, Jianfei Yang, Ziteng Cui
- Published: 2026-09-29T13:16:37Z
- Age days: 0

</details>
