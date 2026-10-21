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
url: "https://arxiv.org/abs/2610.25961v1"
published: "2026-10-19T07:54:13Z"
age_days: 1
score: 44
created: 2026-10-21
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PaceVLA 让机器人自己判断当前能否加快：空旷移动可以合并动作，精细接触则保留小步和较短预测。它同时学习多种时间粒度的动作解码器，并根据当前场景选择使用哪一种。

## 问题

遥操作示范常因操作者谨慎而缓慢，模仿策略会照搬这些细碎动作。统一合并动作虽然快，却可能删掉抓握和接触所需的细节；只看动作复杂度也未必知道场景需要多高精度[S6](https://arxiv.org/html/2610.25961v1#S1.p1.1) [S7](https://arxiv.org/html/2610.25961v1#S1.p2.1) [S8](https://arxiv.org/html/2610.25961v1#S1.p3.1)。问题因此是每次观察后同时选择动作粒度和预测跨度。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子叠好”和当前图像；远离杯口时选粗动作接近，接近杯沿时改为细动作与短跨度；执行后重新观察，输出下一段动作，避免快速模式贯穿整个接触过程。

## 创新点或方法

旧做法固定粒度，或对原策略输出事后加速；本文让共享动作专家配多个专用解码器，直接学习不同粒度与跨度的目标。训练冻结视觉语言骨干，训练动作专家、解码器、判断器和路由器；判断器学习大型视觉语言模型提供的可合并评分，路由器受各模式预测误差监督，并用均衡项避免只选一种[S20](https://arxiv.org/html/2610.25961v1#S3.SS2.p1.1) [S21](https://arxiv.org/html/2610.25961v1#S3.SS4.p1.1) [S22](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px1.p1.2) [S23](https://arxiv.org/html/2610.25961v1#S3.E2) [S24](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px1.p1.3) [S25](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px2.p1.1) [S40](https://arxiv.org/html/2610.25961v1#A3.SS3.SSS0.Px1.p1.1)。推理先判断能否粗执行，再在相应组内选模式生成动作。具体相邻动作怎样聚合，节选未说明。

### 方法如何工作

1. 把同段示范转换成不同粒度和跨度的训练目标，使模型有快慢多种可选输出。
2. 共享动作专家学习共同运动规律，专用解码器分别学习各模式，避免直接压缩旧预测带来的误差。
3. 用场景可合并评分训练判断器，并用模式误差训练路由器，使选择兼顾场景需求与预测能力。
4. 推理时选组、选模式、生成并执行动作，再用新观察重新决定节奏。

### 必要术语

- 时间动作量化：沿时间合并相邻动作；这里不是把动作数值离散成词元。
- 预测跨度：一次预测覆盖多少原始时间步；影响多久能够重新规划。
- 路由器：根据当前上下文选择输出模式；连接场景信息与执行节奏。

## 证据

覆盖 RoboCasa-Kitchen、LIBERO、DexJoCo 仿真及六项真机任务[S9](https://arxiv.org/html/2610.25961v1#S1.p4.1)。DexJoCo 中，相比 GR00T N1.5，成功率从76.3%到77.3%，有效加速指标为1.11[S34](https://arxiv.org/html/2610.25961v1#S4.T4.fig1.7)；真机 ALLEX 输送任务吞吐量从每分钟3.6件到6.3件，成功率从86%到94%[S36](https://arxiv.org/html/2610.25961v1#S4.T4.fig2.7)。固定合并在该任务仅72%成功。结果支持这些任务上的速度与成功率兼顾，不能把最高加速倍数当所有场景的收益。

## 局限

作者明确指出大幅命令需要控制器跟得上，并调整了跟踪与夹爪增益[S27](https://arxiv.org/html/2610.25961v1#S3.SS5.p1.1)，因此效果依赖整个执行系统。我的待核查问题是：可合并评分在陌生接触场景是否可靠，以及各基线是否采用一致控制器设置；不能把加速全部归因于路由网络。

- **判断**：值得细读训练目标与控制器配置；它把加速落实为可测试的场景决策，但复现不能只添加一个模式选择头。

## 研究关联

这里最可借鉴的是把“多久重新看一次、动作走多大步”也交给策略选择。只有当任务中确实同时存在可快速通过的阶段和精细交互阶段时，这种额外学习才有明确动机。

### 下一步读哪里

先读[S18](https://arxiv.org/html/2610.25961v1#S3.SS1.p1.1) [S20](https://arxiv.org/html/2610.25961v1#S3.SS2.p1.1) [S24](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px1.p1.3) [S25](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px2.p1.1)区分动作学习和模式学习，再看[S37](https://arxiv.org/html/2610.25961v1#S4.SS3.SSS0.Px1.p1.1)消融。下一步核查评分提示、阈值敏感性、动作聚合规则，以及[S27](https://arxiv.org/html/2610.25961v1#S3.SS5.p1.1)指向的控制器增益与基线公平性。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.25961v1
- 获取时间：2026-10-21T00:33:49.702750+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.25961v1#p1.3)
- [S2] [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models · 正文段落 2](https://arxiv.org/html/2610.25961v1#abstract1.1)
- [S3] [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models · 正文段落 3](https://arxiv.org/html/2610.25961v1#S0.F1.sf1)
- [S4] [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models · 正文段落 4](https://arxiv.org/html/2610.25961v1#S0.F1.sf2)
- [S5] [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models · 正文段落 5](https://arxiv.org/html/2610.25961v1#S0.F1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.25961v1#S1.p1.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.25961v1#S1.p2.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.25961v1#S1.p3.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.25961v1#S1.p4.1)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.25961v1#S1.I1.i1)
- [S11] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.25961v1#S1.I1.i3)
- [S12] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.25961v1#S2.p1.1)
- [S13] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.25961v1#S2.p2.1)
- [S14] [3 Method · 正文段落 17](https://arxiv.org/html/2610.25961v1#S3.p1.1)
- [S15] [3 Method · 正文段落 18](https://arxiv.org/html/2610.25961v1#S3.p2.1)
- [S16] [3 Method · 正文段落 19](https://arxiv.org/html/2610.25961v1#S3.E1)
- [S17] [3 Method · 正文段落 20](https://arxiv.org/html/2610.25961v1#S3.p2.2)
- [S18] [3.1 Temporal Action Quantization · 正文段落 21](https://arxiv.org/html/2610.25961v1#S3.SS1.p1.1)
- [S19] [3.1 Temporal Action Quantization · 正文段落 23](https://arxiv.org/html/2610.25961v1#S3.F2)
- [S20] [3.2 Shared Action Expert with Mode-Specific Action Decoders · 正文段落 24](https://arxiv.org/html/2610.25961v1#S3.SS2.p1.1)
- [S21] [3.4 Training Objectives · 正文段落 28](https://arxiv.org/html/2610.25961v1#S3.SS4.p1.1)
- [S22] [Action policy learning. · 正文段落 29](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px1.p1.2)
- [S23] [Action policy learning. · 正文段落 30](https://arxiv.org/html/2610.25961v1#S3.E2)
- [S24] [Action policy learning. · 正文段落 31](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px1.p1.3)
- [S25] [Quantizability regression. · 正文段落 32](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px2.p1.1)
- [S26] [Quantizability regression. · 正文段落 35](https://arxiv.org/html/2610.25961v1#S3.SS4.SSS0.Px2.p2.1)
- [S27] [3.5 Controller Configuration for Accelerated Execution · 正文段落 37](https://arxiv.org/html/2610.25961v1#S3.SS5.p1.1)
- [S28] [4 Experiments · 正文段落 38](https://arxiv.org/html/2610.25961v1#S4.p1.1)
- [S29] [4 Experiments · 正文段落 39](https://arxiv.org/html/2610.25961v1#S4.I1.i1)
- [S30] [4 Experiments · 正文段落 40](https://arxiv.org/html/2610.25961v1#S4.I1.i2)
- [S31] [4 Experiments · 正文段落 41](https://arxiv.org/html/2610.25961v1#S4.I1.i3)
- [S32] [Real-World Tasks. · 正文段落 52](https://arxiv.org/html/2610.25961v1#S4.SS2.SSS0.Px2.p1.1)
- [S33] [Real-World Tasks. · 正文段落 53](https://arxiv.org/html/2610.25961v1#S4.T4.fig1)
- [S34] [Real-World Tasks. · 正文段落 54](https://arxiv.org/html/2610.25961v1#S4.T4.fig1.7)
- [S35] [Real-World Tasks. · 正文段落 55](https://arxiv.org/html/2610.25961v1#S4.T4.fig2)
- [S36] [Real-World Tasks. · 正文段落 56](https://arxiv.org/html/2610.25961v1#S4.T4.fig2.7)
- [S37] [Ablation Study. · 正文段落 61](https://arxiv.org/html/2610.25961v1#S4.SS3.SSS0.Px1.p1.1)
- [S38] [5 Conclusion · 正文段落 67](https://arxiv.org/html/2610.25961v1#S5.p1.1)
- [S39] [Appendix B Evaluation Metrics · 正文段落 78](https://arxiv.org/html/2610.25961v1#A2.p1.1)
- [S40] [Training. · 正文段落 98](https://arxiv.org/html/2610.25961v1#A3.SS3.SSS0.Px1.p1.1)
- [S41] [Training. · 正文段落 99](https://arxiv.org/html/2610.25961v1#A3.T8)
- [S42] [Training. · 正文段落 100](https://arxiv.org/html/2610.25961v1#A3.T8.8)
- [S43] [Training. · 正文段落 101](https://arxiv.org/html/2610.25961v1#A3.T8)
- [S44] [Training. · 正文段落 102](https://arxiv.org/html/2610.25961v1#A3.T8.12)
- [S45] [Controller configuration. · 正文段落 106](https://arxiv.org/html/2610.25961v1#A3.T9)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/PaceVLA Adaptive Temporal Action Quantization in Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Fast and reliable manipulation is crucial for practical robot deployment. Although Vision-Language-Action (VLA) models have recently shown remarkable progress as generalist robot policies, their execution often remains temporally inefficient. A key source of this inefficiency is that policies learn fine-grained temporal patterns from teleoperated demonstrations, requiring many low-level action steps. Temporal action quantization offers a simple way to accelerate execution by aggregating consecutive low-level actions into temporally coarser actions. However, applying action quantization without considering when fine-grained control is required introduces a speed-accuracy trade-off: accelerated actions may efficiently reduce redundant steps in some phases, while discarding critical motion details in precision-sensitive interactions. To address this, we propose PaceVLA, a unified framework for adaptive temporal execution in VLAs that integrates two coupled components: (1) mode-specific action decoders built on a shared action expert, supporting multiple temporal granularities and prediction horizons, and (2) a quantizability-guided mode selection scheme which decides whether coarse execution is appropriate, and a context-conditioned router that selects an execution mode at each inference step. Experiments across three multi-task simulation benchmarks and six real-world tasks show that PaceVLA improves execution efficiency while maintaining task success rate across multiple embodiments, including long-horizon and dexterous manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25961v1
- Authors: Hojin Jeon, Jimin Lee, Taekwan Kim, Nayoung Oh, Taeyoung Kim, Myungkyu Koo, Jinmo Koo, Joonwoo Ahn, Jinwoo Shin
- Published: 2026-10-19T07:54:13Z
- Age days: 1

</details>
