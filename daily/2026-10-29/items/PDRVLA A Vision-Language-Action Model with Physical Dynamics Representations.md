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
url: "https://arxiv.org/abs/2610.37381v1"
published: "2026-10-27T15:09:10Z"
age_days: 1
score: 39
created: 2026-10-29
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PDRVLA 把预测未来所需的信息压进少量 physical tokens，让动作模型利用这些信息，却不用在控制时生成视频。它同时学习未来外观、深度和光流，并在预训练中借助冻结的视频模型提供监督。

## 问题

任务是从观察和指令生成机器人操作动作。仅识别当前物体，还不足以判断搬动后的位置关系如何变化；在线生成未来视频又会拖慢控制。因此，瓶颈是如何给动作模型补充变化信息，同时控制推理开销。[S3](https://arxiv.org/html/2610.37381v1#S1.p1.1) [S4](https://arxiv.org/html/2610.37381v1#S1.p2.1) [S5](https://arxiv.org/html/2610.37381v1#S1.p3.1) 作者也承认已有工作采用训练时视频监督，本文沿此方向具体设计多种预测目标。

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放进盒子”和当前图像、机器人状态；physical tokens 编码与后续外观、空间和运动相关的信息，动作专家据此生成八步控制，执行完再观察。运行中无需先渲染积木移动的视频。

## 创新点或方法

原本只靠视觉语言特征出动作，现在从中间层提取固定数量的 physical tokens，与最后一层特征一起交给动作专家。预训练时，token 预测未来 RGB、深度、光流的压缩特征；深度和光流由模型生成伪标签。[S27](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px1.p1.1) 冻结的视频模型还接收 token，通过未来预测损失教它们提供有用条件。联合策略训练移除视频模型，保留直接预测，并加入动作和语言监督。推理只保留学好的 token 路径，每次输出八步动作，全部执行后才重新观察规划。[S20](https://arxiv.org/html/2610.37381v1#S3.SS3.p1.1) [S24](https://arxiv.org/html/2610.37381v1#S4.p1.1)

### 方法如何工作

1. 从视觉语言中间特征提取紧凑 token，为动作模型增加独立的信息入口。
2. 用记录视频的未来外观、深度和光流特征监督 token，使它们包含场景变化信息。
3. 借冻结视频模型的预测损失辅助预训练，随后移除它，继续联合学习动作、语言和直接预测。
4. 推理时把 token、最终视觉语言特征和自身状态交给动作专家，输出并执行一段控制。

### 必要术语

- Physical tokens：紧凑的学习表示；本文用未来预测目标训练它们，再用于动作生成。
- 光流：图像位置随时间移动的估计；本文作为未来运动的监督目标。
- 伪标签：由其他模型估计的训练目标；本文的深度和光流监督来自这种估计。

## 证据

四项测试均为仿真。LIBERO、LIBERO-Plus、RoboTwin 2.0、SimplerEnv成功率分别为99.3%、89.9%、93.6%、81.5%；对照Qwen-RobotManip前三项为99.1%、89.0%、93.0%，InternVLA-A1.5四项为98.9%、84.8%、93.2%、80.8%。[S42](https://arxiv.org/html/2610.37381v1#S5.T5.2) LIBERO共2000回合，Plus有10030个案例。[S36](https://arxiv.org/html/2610.37381v1#S5.SS1.p1.1) [S37](https://arxiv.org/html/2610.37381v1#S5.SS1.p2.1) 总体领先，但LIBERO长任务97.6%，低于LingBot-VA的98.5%。[S43](https://arxiv.org/html/2610.37381v1#S5.SS2.SSS0.Px1.p1.1) 基线来自各自论文和协议，不能把差距全归因于物理模块。[S40](https://arxiv.org/html/2610.37381v1#S5.SS2.p1.1)

## 局限

作者把接触、材料属性等列为未来预测目标，当前结果不等于已学会这些性质。[S50](https://arxiv.org/html/2610.37381v1#S6.p2.1) 我的待核查问题是：物理模块在同数据、同训练预算下带来多少动作增益，以及实际延迟是多少。节选说视频监督改善预测，却未给相应消融数值；也没有真机评测结果。

- **判断**：值得细读训练目标和同条件消融；四项仿真成绩支持方法可用，但尚不足以说明优势主要来自物理表示。

## 研究关联

可以借鉴的是把昂贵预测器当训练工具，把执行时真正需要的信息压进小表示。若已有视频训练数据又受控制延迟限制，联合预测外观、空间和运动，比只要求重建画面更值得检查。

### 下一步读哪里

沿[S27](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px1.p1.1) [S28](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px2.p1.1) [S29](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px2.p2.1) [S30](https://arxiv.org/html/2610.37381v1#S4.E4) [S31](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px2.p2.2) [S32](https://arxiv.org/html/2610.37381v1#S4.E5) [S33](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px3.p1.1)检查伪标签质量、预测时间范围及视频模型监督怎样回传到模块；核查未来预测改善是否对应动作改善，并查八步开环执行的延迟和扰动代价。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.37381v1
- 获取时间：2026-10-29T00:42:04.889781+00:00
- [S1] [PDRVLA: A Vision–Language–Action Model with Physical Dynamics Representations · 正文段落 1](https://arxiv.org/html/2610.37381v1#abstract1.1)
- [S2] [PDRVLA: A Vision–Language–Action Model with Physical Dynamics Representations · 正文段落 2](https://arxiv.org/html/2610.37381v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.37381v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.37381v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.37381v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.37381v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.37381v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.37381v1#S1.I1.i1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.37381v1#S1.I1.i2)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.37381v1#S1.I1.i3)
- [S11] [2.1 Corpus Overview · 正文段落 12](https://arxiv.org/html/2610.37381v1#S2.SS1.p1.1)
- [S12] [2.1 Corpus Overview · 正文段落 13](https://arxiv.org/html/2610.37381v1#S2.SS1.p2.1)
- [S13] [2.1 Corpus Overview · 正文段落 14](https://arxiv.org/html/2610.37381v1#S2.T1)
- [S14] [2.1 Corpus Overview · 正文段落 15](https://arxiv.org/html/2610.37381v1#S2.T1.2)
- [S15] [2.1 Corpus Overview · 正文段落 16](https://arxiv.org/html/2610.37381v1#S2.SS1.p3.1)
- [S16] [2.1 Corpus Overview · 正文段落 17](https://arxiv.org/html/2610.37381v1#S2.T2)
- [S17] [2.2.1 Real-Robot Data · 正文段落 19](https://arxiv.org/html/2610.37381v1#S2.SS2.SSS1.p1.1)
- [S18] [2.2.2 UMI Data · 正文段落 24](https://arxiv.org/html/2610.37381v1#S2.SS2.SSS2.p1.1)
- [S19] [2.2.2 UMI Data · 正文段落 25](https://arxiv.org/html/2610.37381v1#S2.SS2.SSS2.p2.1)
- [S20] [3.3 Action Generation · 正文段落 71](https://arxiv.org/html/2610.37381v1#S3.SS3.p1.1)
- [S21] [3.3 Action Generation · 正文段落 72](https://arxiv.org/html/2610.37381v1#S3.SS3.SSS0.Px1.p1.1)
- [S22] [3.3 Action Generation · 正文段落 77](https://arxiv.org/html/2610.37381v1#S3.SS3.SSS0.Px1.p1.2)
- [S23] [3.3 Action Generation · 正文段落 81](https://arxiv.org/html/2610.37381v1#S3.SS3.SSS0.Px2.p1.1)
- [S24] [4 Training · 正文段落 84](https://arxiv.org/html/2610.37381v1#S4.p1.1)
- [S25] [4 Training · 正文段落 85](https://arxiv.org/html/2610.37381v1#S4.F4)
- [S26] [4.1 Physical Dynamics Pretraining · 正文段落 86](https://arxiv.org/html/2610.37381v1#S4.SS1.p1.1)
- [S27] [4.1 Physical Dynamics Pretraining · 正文段落 87](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px1.p1.1)
- [S28] [4.1 Physical Dynamics Pretraining · 正文段落 88](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px2.p1.1)
- [S29] [4.1 Physical Dynamics Pretraining · 正文段落 89](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px2.p2.1)
- [S30] [4.1 Physical Dynamics Pretraining · 正文段落 90](https://arxiv.org/html/2610.37381v1#S4.E4)
- [S31] [4.1 Physical Dynamics Pretraining · 正文段落 91](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px2.p2.2)
- [S32] [4.1 Physical Dynamics Pretraining · 正文段落 92](https://arxiv.org/html/2610.37381v1#S4.E5)
- [S33] [4.1 Physical Dynamics Pretraining · 正文段落 93](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px3.p1.1)
- [S34] [4.1 Physical Dynamics Pretraining · 正文段落 94](https://arxiv.org/html/2610.37381v1#S4.SS1.SSS0.Px3.p2.1)
- [S35] [5 Experiments · 正文段落 115](https://arxiv.org/html/2610.37381v1#S5.p1.1)
- [S36] [5.1 Experimental Setup · 正文段落 116](https://arxiv.org/html/2610.37381v1#S5.SS1.p1.1)
- [S37] [5.1 Experimental Setup · 正文段落 117](https://arxiv.org/html/2610.37381v1#S5.SS1.p2.1)
- [S38] [5.1 Experimental Setup · 正文段落 118](https://arxiv.org/html/2610.37381v1#S5.SS1.p3.1)
- [S39] [5.1 Experimental Setup · 正文段落 119](https://arxiv.org/html/2610.37381v1#S5.SS1.p4.1)
- [S40] [5.2 Main Results · 正文段落 120](https://arxiv.org/html/2610.37381v1#S5.SS2.p1.1)
- [S41] [5.2 Main Results · 正文段落 121](https://arxiv.org/html/2610.37381v1#S5.T5)
- [S42] [5.2 Main Results · 正文段落 122](https://arxiv.org/html/2610.37381v1#S5.T5.2)
- [S43] [5.2 Main Results · 正文段落 123](https://arxiv.org/html/2610.37381v1#S5.SS2.SSS0.Px1.p1.1)
- [S44] [5.2 Main Results · 正文段落 124](https://arxiv.org/html/2610.37381v1#S5.T6)
- [S45] [5.2 Main Results · 正文段落 125](https://arxiv.org/html/2610.37381v1#S5.T6.2)
- [S46] [5.2 Main Results · 正文段落 126](https://arxiv.org/html/2610.37381v1#S5.SS2.SSS0.Px2.p1.1)
- [S47] [5.2 Main Results · 正文段落 127](https://arxiv.org/html/2610.37381v1#S5.T7)
- [S48] [5.2 Main Results · 正文段落 128](https://arxiv.org/html/2610.37381v1#S5.T7.2)
- [S49] [5.2 Main Results · 正文段落 129](https://arxiv.org/html/2610.37381v1#S5.SS2.SSS0.Px3.p1.1)
- [S50] [6 Conclusion · 正文段落 159](https://arxiv.org/html/2610.37381v1#S6.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/PDRVLA A Vision-Language-Action Model with Physical Dynamics Representations.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We introduce PDRVLA, whose lightweight Physical Dynamics Module extracts physical tokens from vision--language features to condition action generation without online video generation. The module learns through direct prediction of future RGB, depth, and optical-flow features, with auxiliary supervision through a frozen pretrained video world model. Training relies entirely on publicly available data, expanded through human-to-robot synthesis, subtask annotation, and embodied chain-of-thought (ECoT) annotation. Across four simulation benchmarks, PDRVLA achieves success rates of 99.3% on LIBERO, 89.9% on LIBERO-Plus, 93.6% on RoboTwin~2.0, and 81.5% on SimplerEnv. Ablations show improved future prediction with world-model supervision and evaluate how subtask conditioning, future object-pose supervision, and ECoT training affect action success.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37381v1
- Authors: Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu
- Published: 2026-10-27T15:09:10Z
- Age days: 1

</details>
