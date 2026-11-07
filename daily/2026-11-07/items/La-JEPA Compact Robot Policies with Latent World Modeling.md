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
url: "https://arxiv.org/abs/2611.08156v1"
published: "2026-11-05T15:16:38Z"
age_days: 1
score: 40
created: 2026-11-07
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# La-JEPA: Compact Robot Policies with Latent World Modeling

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> La-JEPA 保留预训练视觉编码器，把负责控制的策略重新做小：训练时同时学习未来特征和动作，执行时只生成动作。关键是让预测未来的训练信号改善策略，而不让机器人每次行动前都生成未来。

## 问题

任务是根据多相机图像、机器人状态和指令输出一段动作。现有 WAM、VLA 能借用生成模型的知识，也继承其庞大骨干；即便不生成未来，部署仍要承担骨干成本。本文追问：控制是否必须连同生成架构一起继承？

### 用一个例子理解

理解用例（非论文实验）：输入两路桌面图像、机械臂状态和“把杯子放到托盘里”；编码器提取特征，策略输出接近、抓取、移动的一段动作。执行部分动作后重新观察，不必先画出杯子未来的位置。

## 创新点或方法

旧做法沿用视频或语言生成骨干；本文只借用编码器知识，World DiT 和 Action DiT 从头训练。前者处理观察与未来特征，后者生成动作。注意力屏蔽使动作只能读取观察和动作，不能偷看未来；未来预测仍通过共享的 World DiT 参数塑造观察表示。因此训练可以联合学习，推理可以省去未来生成。[S13](https://arxiv.org/html/2611.08156v1#S3.SS1.SSS0.Px1.p1.1) [S14](https://arxiv.org/html/2611.08156v1#S3.SS1.SSS0.Px3.p1.1) [S15](https://arxiv.org/html/2611.08156v1#S3.SS2.SSS0.Px1.p1.1) [S16](https://arxiv.org/html/2611.08156v1#S3.SS2.SSS0.Px1.p1.2)

### 方法如何工作

1. 把近期多相机画面编码为特征，并把未来画面编码为监督目标，避免学习重建像素。[S13](https://arxiv.org/html/2611.08156v1#S3.SS1.SSS0.Px1.p1.1)
2. 训练时分别扰动未来特征和动作，让两个 DiT 学习恢复它们所需的流匹配速度。[S15](https://arxiv.org/html/2611.08156v1#S3.SS2.SSS0.Px1.p1.1) [S16](https://arxiv.org/html/2611.08156v1#S3.SS2.SSS0.Px1.p1.2)
3. 限制动作读取观察特征，使未来监督经参数更新帮助控制，同时避免训练依赖不可用的未来。[S14](https://arxiv.org/html/2611.08156v1#S3.SS1.SSS0.Px3.p1.1)
4. 推理只生成动作块，执行一部分后重新观察；未来预测分支不再承担生成成本。[S12](https://arxiv.org/html/2611.08156v1#S3.p1.1) [S27](https://arxiv.org/html/2611.08156v1#A2.T9.2)

### 必要术语

- JEPA 特征：通过预测输入的表示而学习的特征；本文用它代替偏重像素保真的视觉潜变量。
- 流匹配：学习如何把噪声逐步变成目标；本文分别用于未来特征和动作。
- 具身预训练：先从广泛机器人经验学习；本文策略主要从目标示范学习，但仍使用预训练编码器。

## 证据

仿真覆盖 LIBERO-Plus、RoboTwin 2.0；[S6](https://arxiv.org/html/2611.08156v1#S1.p4.1) 报告在无具身预训练组领先，部署参数约为次优策略的四分之一，相对 Fast-WAM 最多快 5 倍，但节选未给仿真成功率全表。真机四项任务中，La-JEPA 平均成功次数为 17.50/20，π0.5 为 17.25/20，Fast-WAM 为 16.00/20；策略调用延迟分别为 25.16、71.89、88.09 毫秒。[S18](https://arxiv.org/html/2611.08156v1#S5.T5) [S19](https://arxiv.org/html/2611.08156v1#S5.T5.2) [S20](https://arxiv.org/html/2611.08156v1#S5.SS5.p1.1) 这支持有限任务上的竞争力，延迟也不是控制闭环周期。

## 局限

作者明确指出：随机化 RoboTwin 上仍落后于最强具身预训练方法，单一机器人设置的四项真机任务也不足以证明普遍追平 π0.5。[S22](https://arxiv.org/html/2611.08156v1#S6.SS0.SSS0.Px2.p1.1) 我的待核查问题是：表示替换、未来预测和编码器适配各贡献多少？诊断中有效秩与成功率同时提高，不能据此认定有效秩就是原因。[S32](https://arxiv.org/html/2611.08156v1#A5.SS4.p1.1)

- **判断**：值得读到注意力掩码和消融：它最有用的贡献是解释为何训练时预测未来，可以帮助一个执行时不预测未来的小策略。

## 研究关联

值得借鉴的是把“借用预训练表示”和“继承预训练策略架构”拆开。如果任务需要紧凑控制器，可以先比较好的视觉特征加小策略，再判断是否值得承担大生成骨干的成本。

### 下一步读哪里

先看 [S14](https://arxiv.org/html/2611.08156v1#S3.SS1.SSS0.Px3.p1.1) 的信息流，再核查联合损失和推理采样设置；[S27](https://arxiv.org/html/2611.08156v1#A2.T9.2) 已给动作分块与重规划配置。比较 LIBERO-Plus 前须核对指令修正协议；[S7](https://arxiv.org/html/2611.08156v1#S1.p5.1) 指出原评测器会污染指令，不能混用成绩。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.08156v1
- 获取时间：2026-11-07T03:39:39.171981+00:00
- [S1] [La-JEPA: Compact Robot Policies with Latent World Modeling · 正文段落 1](https://arxiv.org/html/2611.08156v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.08156v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.08156v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.08156v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.08156v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.08156v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.08156v1#S1.p5.1)
- [S8] [Vision-language-action policies. · 正文段落 8](https://arxiv.org/html/2611.08156v1#S2.SS0.SSS0.Px1.p1.1)
- [S9] [World-action models. · 正文段落 9](https://arxiv.org/html/2611.08156v1#S2.SS0.SSS0.Px2.p1.1)
- [S10] [Joint-embedding predictive architectures. · 正文段落 10](https://arxiv.org/html/2611.08156v1#S2.SS0.SSS0.Px3.p1.1)
- [S11] [Compact policies. · 正文段落 11](https://arxiv.org/html/2611.08156v1#S2.SS0.SSS0.Px4.p1.1)
- [S12] [3 La-JEPA · 正文段落 12](https://arxiv.org/html/2611.08156v1#S3.p1.1)
- [S13] [Visual representations. · 正文段落 14](https://arxiv.org/html/2611.08156v1#S3.SS1.SSS0.Px1.p1.1)
- [S14] [World–action architecture. · 正文段落 16](https://arxiv.org/html/2611.08156v1#S3.SS1.SSS0.Px3.p1.1)
- [S15] [Joint flow matching. · 正文段落 17](https://arxiv.org/html/2611.08156v1#S3.SS2.SSS0.Px1.p1.1)
- [S16] [Joint flow matching. · 正文段落 19](https://arxiv.org/html/2611.08156v1#S3.SS2.SSS0.Px1.p1.2)
- [S17] [Experimental setup. · 正文段落 24](https://arxiv.org/html/2611.08156v1#S4.SS0.SSS0.Px1.p1.1)
- [S18] [5.5 Real-Robot Experiments · 正文段落 50](https://arxiv.org/html/2611.08156v1#S5.T5)
- [S19] [5.5 Real-Robot Experiments · 正文段落 51](https://arxiv.org/html/2611.08156v1#S5.T5.2)
- [S20] [5.5 Real-Robot Experiments · 正文段落 52](https://arxiv.org/html/2611.08156v1#S5.SS5.p1.1)
- [S21] [5.5 Real-Robot Experiments · 正文段落 53](https://arxiv.org/html/2611.08156v1#S5.SS5.p2.1)
- [S22] [Large-scale pretraining. · 正文段落 55](https://arxiv.org/html/2611.08156v1#S6.SS0.SSS0.Px2.p1.1)
- [S23] [7 Conclusion · 正文段落 56](https://arxiv.org/html/2611.08156v1#S7.p1.1)
- [S24] [Appendix B Training and Evaluation Protocols · 正文段落 80](https://arxiv.org/html/2611.08156v1#A2.p1.1)
- [S25] [Architecture and optimization. · 正文段落 81](https://arxiv.org/html/2611.08156v1#A2.SS0.SSS0.Px1.p1.1)
- [S26] [Architecture and optimization. · 正文段落 82](https://arxiv.org/html/2611.08156v1#A2.T9)
- [S27] [Architecture and optimization. · 正文段落 83](https://arxiv.org/html/2611.08156v1#A2.T9.2)
- [S28] [Training data and checkpoint selection. · 正文段落 89](https://arxiv.org/html/2611.08156v1#A2.SS0.SSS0.Px4.p1.1)
- [S29] [Data and evaluation pipelines: · 正文段落 98](https://arxiv.org/html/2611.08156v1#A2.SS0.SSS0.Px7.p1.1)
- [S30] [Data and evaluation pipelines: · 正文段落 100](https://arxiv.org/html/2611.08156v1#A2.I2.i1)
- [S31] [Data and evaluation pipelines: · 正文段落 104](https://arxiv.org/html/2611.08156v1#A2.I2.i5)
- [S32] [E.4 Representation Diagnostics · 正文段落 159](https://arxiv.org/html/2611.08156v1#A5.SS4.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/La-JEPA Compact Robot Policies with Latent World Modeling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Latent Action JEPA (La-JEPA), a compact world-action model whose policy transformer is trained from scratch in the feature space of a pretrained V-JEPA 2.1 encoder. Following Fast-WAM, La-JEPA learns to predict future features jointly with actions during training and generates only actions at inference. Among policies without embodied pretraining, La-JEPA achieves state-of-the-art performance in clean and randomized RoboTwin 2.0 scenes and on LIBERO-Plus with correct instructions, while using far fewer parameters than the strongest competing policies. It runs substantially faster than Fast-WAM at comparable performance and outperforms the closest JEPA-based methods, LeapBot-WA and JEPA-WAM, on LIBERO-Plus and RoboTwin 2.0 without their pretrained policy backbones. On four real-robot tasks, its average success is comparable to pi0.5 and above non-embodied-pretrained baselines. Through a design study of the choices behind La-JEPA, we show that JEPA features outperform video VAE latents, most clearly out of distribution, and that training-time future prediction choices significantly impact the policy even when future prediction is skipped at inference. We correct the LIBERO-Plus instructions, as the officially released evaluator corrupts them for most variants, and re-evaluate several strong open baselines. Without a generative pretrained policy backbone, La-JEPA is better and faster than far larger policies, suggesting that robot foundation models may benefit from architectures designed for control rather than inherited from generation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08156v1
- Authors: Mateo Clémente, George Z. Xue, Amin Abyaneh, Liheng Ma, Rui Heng Yang, Tongtong Cao, Zhanguang Zhang, Yingxue Zhang
- Published: 2026-11-05T15:16:38Z
- Age days: 1

</details>
