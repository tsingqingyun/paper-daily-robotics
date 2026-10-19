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
url: "https://arxiv.org/abs/2610.22951v1"
published: "2026-10-16T05:20:45Z"
age_days: 3
score: 44
created: 2026-10-19
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> MambaAct 把 π₀.₅ 中反复生成动作的 Transformer 模块换成更小的 Mamba，并把视觉语言信息压成可重复使用的条件信号。它主要减少每次去噪的计算量，同时保留原有多步动作生成方式。

## 问题

流匹配 VLA 不是一次前向就得到动作：视觉语言前缀每轮只算一次，动作专家却要反复运行，因此会拖慢控制。已有加速方法常减少采样步数、裁剪网络或视觉 token；本文追问的是反复运行的动作模块本身是否过重。[S2](https://arxiv.org/html/2610.22951v1#S1.p1.1) [S3](https://arxiv.org/html/2610.22951v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放进盒子”、腕部与外部相机图像；骨干编码一次，压缩器生成条件，Mamba 反复修正带噪动作块；输出接下来一段关节动作，再根据新图像重规划。

## 创新点或方法

原模块通过 Transformer 处理带噪动作及视觉语言条件；本文用 Mamba 混合动作序列，把前缀压成紧凑表示，再用 gated FiLM 调节各动作块，避免每步重复逐 token 跨注意力。训练时新动作模块、压缩器和预训练视觉语言骨干一起微调，并非冻结骨干，也不靠额外蒸馏。推理时条件表示复用，动作模块仍运行十次，逐步输出去噪动作。[S10](https://arxiv.org/html/2610.22951v1#S2.SS1.p3.1) [S15](https://arxiv.org/html/2610.22951v1#S3.SS1.p4.1) [S16](https://arxiv.org/html/2610.22951v1#S3.F2) [S17](https://arxiv.org/html/2610.22951v1#S3.SS2.p1.1) [S18](https://arxiv.org/html/2610.22951v1#S3.SS3.p1.1) [S19](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px1.p1.1) [S20](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px1.p2.1) [S21](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px2.p1.1)

### 方法如何工作

1. 把图像和指令编码成视觉语言前缀，为动作提供物体与目标信息。
2. 压缩前缀并生成各动作块的调节信号，减少反复读取长上下文的成本。
3. 将带噪动作和流时间送入 Mamba 动作块，预测当前应怎样修正动作。
4. 重复十次更新得到动作块，执行部分动作后重新观察，避免长时间依赖旧画面。

### 必要术语

- 动作专家：专门从条件信息生成连续动作的子网络；是本文替换的部分。
- 流匹配：学习把噪声逐步变成目标动作的变化方向；决定动作模块需要反复执行。
- Mamba：用选择性状态更新处理序列的模型；本文用它关联一段动作中的各位置。
- FiLM：用条件信息缩放、平移特征；本文用它把压缩后的视觉语言信息注入动作块。

## 证据

匹配 π₀.₅ 基线、三个微调种子下，LIBERO 平均成功率从 96.72±0.14% 到 97.80±0.43%；动作专家从 311.5M 缩到 29.7M，总模型只从 3.62B 到 2.96B。[S30](https://arxiv.org/html/2610.22951v1#S4.SS1.SSS1.p1.1) H100 上去噪延迟降 64.8%，端到端降 52.9%。真机两个 UR5 任务每项用 112 条示范，OOD 每项 52 次测试；倒螺母评分从 86.5% 到 95.2%，放管从 76.9% 到 82.7%，端到端约降三分之一。真机指标含半分奖励，不能视为完整成功比例。[S24](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px4.p1.1) [S27](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px4.p3.1) [S36](https://arxiv.org/html/2610.22951v1#S4.SS1.SSS3.p1.1) [S37](https://arxiv.org/html/2610.22951v1#S4.T4) [S38](https://arxiv.org/html/2610.22951v1#S4.T4.2.1) [S39](https://arxiv.org/html/2610.22951v1#S4.T4.3.1)

## 局限

作者明确承认真机只有两项 UR5 任务，主要考察位置变化；与视觉裁剪、减少去噪步数的兼容性仍待测。[S42](https://arxiv.org/html/2610.22951v1#S5.p2.1) 我的待核查问题是架构收益如何分配给 Mamba 和条件接口；已有对应消融设计，但输入未提供结果。[S41](https://arxiv.org/html/2610.22951v1#S4.SS2.p2.1)

- **判断**：值得读到实现与匹配消融：加速证据清楚，但应把适用范围限定在已测动作路径和部署条件。

## 研究关联

若性能瓶颈在重复计算的动作头，值得先测它的耗时，再考虑替换架构。这篇说明可以保留已有视觉语言表征，通过重训较轻动作路径获得收益；“动作专家缩小十倍”则不代表整个模型或系统加速十倍。

### 下一步读哪里

先看 [S16](https://arxiv.org/html/2610.22951v1#S3.F2) [S20](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px1.p2.1) 的压缩与条件注入，再查 [S41](https://arxiv.org/html/2610.22951v1#S4.SS2.p2.1) 的二乘二消融；用 [S29](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px6.p1.1) [S30](https://arxiv.org/html/2610.22951v1#S4.SS1.SSS1.p1.1) [S39](https://arxiv.org/html/2610.22951v1#S4.T4.3.1) 区分前缀、去噪和端到端耗时，核查目标硬件上的实际瓶颈。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.22951v1
- 获取时间：2026-10-19T15:35:14.736202+00:00
- [S1] [MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models · 正文段落 1](https://arxiv.org/html/2610.22951v1#abstract1.1)
- [S2] [I Introduction · 正文段落 2](https://arxiv.org/html/2610.22951v1#S1.p1.1)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2610.22951v1#S1.p2.1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2610.22951v1#S1.p3.1)
- [S5] [I Introduction · 正文段落 6](https://arxiv.org/html/2610.22951v1#S1.I1.i1)
- [S6] [I Introduction · 正文段落 7](https://arxiv.org/html/2610.22951v1#S1.I1.i2)
- [S7] [I Introduction · 正文段落 8](https://arxiv.org/html/2610.22951v1#S1.I1.i3)
- [S8] [II-A Efficient Vision-Language-Action Models · 正文段落 9](https://arxiv.org/html/2610.22951v1#S2.SS1.p1.1)
- [S9] [II-A Efficient Vision-Language-Action Models · 正文段落 10](https://arxiv.org/html/2610.22951v1#S2.SS1.p2.1)
- [S10] [II-A Efficient Vision-Language-Action Models · 正文段落 11](https://arxiv.org/html/2610.22951v1#S2.SS1.p3.1)
- [S11] [II-B Mamba in Vision-Language-Action Models · 正文段落 13](https://arxiv.org/html/2610.22951v1#S2.SS2.p2.1)
- [S12] [II-B Mamba in Vision-Language-Action Models · 正文段落 14](https://arxiv.org/html/2610.22951v1#S2.SS2.p3.1)
- [S13] [III Methodology · 正文段落 15](https://arxiv.org/html/2610.22951v1#S3.p1.1)
- [S14] [III-A Preliminaries · 正文段落 17](https://arxiv.org/html/2610.22951v1#S3.SS1.p2.2)
- [S15] [III-A Preliminaries · 正文段落 22](https://arxiv.org/html/2610.22951v1#S3.SS1.p4.1)
- [S16] [III-A Preliminaries · 正文段落 25](https://arxiv.org/html/2610.22951v1#S3.F2)
- [S17] [III-B MambaAct · 正文段落 27](https://arxiv.org/html/2610.22951v1#S3.SS2.p1.1)
- [S18] [III-C Experimental Setup · 正文段落 47](https://arxiv.org/html/2610.22951v1#S3.SS3.p1.1)
- [S19] [III-C Experimental Setup · 正文段落 48](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px1.p1.1)
- [S20] [III-C Experimental Setup · 正文段落 49](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px1.p2.1)
- [S21] [III-C Experimental Setup · 正文段落 50](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px2.p1.1)
- [S22] [III-C Experimental Setup · 正文段落 51](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px3.p1.1)
- [S23] [III-C Experimental Setup · 正文段落 52](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px3.p2.1)
- [S24] [III-C Experimental Setup · 正文段落 53](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px4.p1.1)
- [S25] [III-C Experimental Setup · 正文段落 54](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px4.p2.1)
- [S26] [III-C Experimental Setup · 正文段落 55](https://arxiv.org/html/2610.22951v1#S3.F3)
- [S27] [III-C Experimental Setup · 正文段落 56](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px4.p3.1)
- [S28] [III-C Experimental Setup · 正文段落 57](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px5.p1.1)
- [S29] [III-C Experimental Setup · 正文段落 58](https://arxiv.org/html/2610.22951v1#S3.SS3.SSS0.Px6.p1.1)
- [S30] [IV-A1 LIBERO · 正文段落 59](https://arxiv.org/html/2610.22951v1#S4.SS1.SSS1.p1.1)
- [S31] [IV-A1 LIBERO · 正文段落 60](https://arxiv.org/html/2610.22951v1#S4.T1)
- [S32] [IV-A1 LIBERO · 正文段落 61](https://arxiv.org/html/2610.22951v1#S4.T1.9.1)
- [S33] [IV-A1 LIBERO · 正文段落 63](https://arxiv.org/html/2610.22951v1#S4.T2)
- [S34] [IV-A1 LIBERO · 正文段落 64](https://arxiv.org/html/2610.22951v1#S4.T2.2.1)
- [S35] [IV-A2 LIBERO-Plus · 正文段落 66](https://arxiv.org/html/2610.22951v1#S4.T3)
- [S36] [IV-A3 Real-world benchmarks · 正文段落 69](https://arxiv.org/html/2610.22951v1#S4.SS1.SSS3.p1.1)
- [S37] [IV-A3 Real-world benchmarks · 正文段落 70](https://arxiv.org/html/2610.22951v1#S4.T4)
- [S38] [IV-A3 Real-world benchmarks · 正文段落 71](https://arxiv.org/html/2610.22951v1#S4.T4.2.1)
- [S39] [IV-A3 Real-world benchmarks · 正文段落 72](https://arxiv.org/html/2610.22951v1#S4.T4.3.1)
- [S40] [IV-B Ablation Studies · 正文段落 73](https://arxiv.org/html/2610.22951v1#S4.SS2.p1.1)
- [S41] [IV-B Ablation Studies · 正文段落 74](https://arxiv.org/html/2610.22951v1#S4.SS2.p2.1)
- [S42] [V Conclusion · 正文段落 95](https://arxiv.org/html/2610.22951v1#S5.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/MambaAct Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have shown strong promise for generalist robotic manipulation, but their inference cost remains a major bottleneck for real-time control. This limitation is especially pronounced in flow-matching VLAs such as $π_{0.5}$, where the action expert is evaluated repeatedly during iterative denoising. We introduce MambaAct, an efficient Mamba action expert for flow-matching VLA policies. MambaAct retains the pretrained visual-language prefix encoder of $π_{0.5}$, while replacing its transformer-based action expert with a compact Mamba-based action expert. Within this expert, Mamba serves as the action mixer that models dependencies across the noisy continuous-action sequence. To preserve visual-language conditioning without repeated token-level cross-attention, MambaAct uses a lightweight Context Compressor to map Vision-language model (VLM) prefix tokens into a compact conditioning signal that gates and modulates each Mamba action block. MambaAct uses a $10\times$ smaller action expert and reduces flow-matching denoising latency by $64.8\%$ on LIBERO and $58.8\%$ in real-world deployment, while improving mean LIBERO success by $1.08$ percentage points across three independent fine-tuning seeds and maintaining gains on LIBERO-Plus and real-world benchmarks. Our code and model weights are publicly available at https://github.com/giakhuyendihoc/MambaAct.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22951v1
- Authors: Khuyen Pham, Tran Nguyen Le, Edoardo Fazzari, Cesare Stefanini
- Published: 2026-10-16T05:20:45Z
- Age days: 3

</details>
