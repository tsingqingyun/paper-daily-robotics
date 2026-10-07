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
url: "https://arxiv.org/abs/2610.07696v1"
published: "2026-10-06T03:34:46Z"
age_days: 0
score: 38
created: 2026-10-07
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ESP: Energy-Score Policy for One-Step Multimodal Action Generation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> ESP 用一次网络计算，把观察、指令和随机噪声直接变成一段动作。它用 energy score 同时鼓励贴近示范与保留合理差异，让一步生成不必退化成多个动作方案的平均值。

## 问题

同一任务可能有多种有效动作，扩散和流匹配能表达它们，但每段动作需要多次网络计算。普通平方误差回归虽然快，却倾向输出条件均值；给它加噪声也不会自动学到多种行为 [S2](https://arxiv.org/html/2610.07696v1#S1.p1.1) [S3](https://arxiv.org/html/2610.07696v1#S1.p2.1) [S4](https://arxiv.org/html/2610.07696v1#S1.F1)。

### 用一个例子理解

理解用例（非论文实验）：输入画面、机器人状态和“把杯子移到托盘”；若示范包含左右两种绕行，ESP 训练时学习两类动作而非中间路线；推理抽一份噪声，输出其中一种动作块，执行后再观察。

## 创新点或方法

ESP 不学噪声逐步变成动作的过程，而直接学终点映射。训练时每个观察—示范对生成八个噪声条件动作：损失第一项把它们拉向示范，第二项抵消全部挤在一起的倾向 [S21](https://arxiv.org/html/2610.07696v1#S3.E5) [S22](https://arxiv.org/html/2610.07696v1#S3.SS3.p1.2)。跨训练数据平衡这两项，才是匹配分布，而非盲目扩大差异。推理只抽一次噪声、生成一个动作块，不筛选候选 [S5](https://arxiv.org/html/2610.07696v1#S1.p3.1) [S23](https://arxiv.org/html/2610.07696v1#S3.SS4.p1.1)。保留视觉语言条件接口，无需教师蒸馏；真机实验冻结骨干、微调已有动作头 [S40](https://arxiv.org/html/2610.07696v1#S4.SS6.p2.1)。

### 方法如何工作

1. 编码图像、语言和机器人状态，得到决定当前可行动作的条件。
2. 训练时为同一条件抽多份噪声，直接生成多个动作块，让网络有机会表达不同方案。
3. 同时计算动作与示范、动作彼此间的距离，避免只学平均值或无约束发散。
4. 推理抽一份噪声并前向一次输出动作块，省掉多步积分和候选筛选。
5. 执行后用新观察重新生成，让一步动作生成嵌入闭环控制。

### 必要术语

- Energy score：用样本到示范及样本之间的距离评价分布；本文的核心训练目标。
- 严格适当评分：理想条件下，真实数据分布唯一使期望评分最优；不等于实际训练保证。
- 动作块：一次预测的连续多个动作；ESP 一次生成整个块。
- NFE：动作生成所需网络计算次数；ESP 推理为一次，不代表整个机器人系统只算一次。

## 证据

TwoBranch 双分支回归中，ESP 命中率 96.2%，十步流匹配 97.1%，MSE 0.7%；这是单种子机制示例 [S19](https://arxiv.org/html/2610.07696v1#S3.F3) [S28](https://arxiv.org/html/2610.07696v1#S4.SS2.p2.1)。LIBERO 固定初始状态的六任务诊断中，ESP、XM、十步 Flow 分别成功 162/192、127/192、155/192 [S32](https://arxiv.org/html/2610.07696v1#S4.SS5.p2.1) [S33](https://arxiv.org/html/2610.07696v1#S4.SS5.p3.1) [S34](https://arxiv.org/html/2610.07696v1#S4.T3) [S35](https://arxiv.org/html/2610.07696v1#S4.T3.4)。Franka 真机关抽屉为 ESP 12/15、四步 Flow 8/15；完整拾放为 7/15、1/15 [S37](https://arxiv.org/html/2610.07696v1#S4.F6.2) [S38](https://arxiv.org/html/2610.07696v1#S4.F6) [S39](https://arxiv.org/html/2610.07696v1#S4.SS6.p1.1) [S40](https://arxiv.org/html/2610.07696v1#S4.SS6.p2.1)。材料未给延迟表数值，因此能确认动作头计算次数减少，不能量化端到端加速。

## 局限

作者明确报告训练代价：八候选和成对距离使 Flow 每步训练约快 3.81 倍 [S42](https://arxiv.org/html/2610.07696v1#S5.p1.1)；某项实验中 ESP 用更少优化步抵消了时间开销，不能普遍化 [S43](https://arxiv.org/html/2610.07696v1#S5.p2.1)。理论唯一最优需要分布可表示并达到总体最优，不保证有限数据训练恢复真实分布。真机试验较少，轨迹分散也不等于覆盖了所有有效策略。

- **判断**：值得读懂损失公式并检查延迟测量，是一个机制清楚的一步动作生成方案；部署收益应结合训练成本和端到端耗时判断。

## 研究关联

可借鉴的是把“生成得快”和“能表达多种动作”拆开：多模态不必依赖反复采样过程，也可以由训练目标约束直接生成器。在动作头延迟占主要成本时，值得尝试这种替换。

### 下一步读哪里

先读 [S21](https://arxiv.org/html/2610.07696v1#S3.E5) [S22](https://arxiv.org/html/2610.07696v1#S3.SS3.p1.2) [S23](https://arxiv.org/html/2610.07696v1#S3.SS4.p1.1) 理解成对项为何必要，再核查动作归一化、候选数对训练和分布的影响。延迟表需确认是否包含视觉骨干、硬件及动作块长度；[S32](https://arxiv.org/html/2610.07696v1#S4.SS5.p2.1) [S33](https://arxiv.org/html/2610.07696v1#S4.SS5.p3.1) [S34](https://arxiv.org/html/2610.07696v1#S4.T3) [S35](https://arxiv.org/html/2610.07696v1#S4.T3.4) 的多样性诊断要与完整 LIBERO 成功率分开看。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.07696v1
- 获取时间：2026-10-07T02:13:54.480619+00:00
- [S1] [ESP: Energy-Score Policy for One-Step Multimodal Action Generation · 正文段落 1](https://arxiv.org/html/2610.07696v1#abstract1.1)
- [S2] [I Introduction · 正文段落 2](https://arxiv.org/html/2610.07696v1#S1.p1.1)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2610.07696v1#S1.p2.1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2610.07696v1#S1.F1)
- [S5] [I Introduction · 正文段落 5](https://arxiv.org/html/2610.07696v1#S1.p3.1)
- [S6] [I Introduction · 正文段落 6](https://arxiv.org/html/2610.07696v1#S1.p4.1)
- [S7] [I Introduction · 正文段落 8](https://arxiv.org/html/2610.07696v1#S1.I1.i1)
- [S8] [I Introduction · 正文段落 9](https://arxiv.org/html/2610.07696v1#S1.I1.i2)
- [S9] [I Introduction · 正文段落 10](https://arxiv.org/html/2610.07696v1#S1.I1.i3)
- [S10] [II Related Work · 正文段落 11](https://arxiv.org/html/2610.07696v1#S2.p1.1)
- [S11] [II Related Work · 正文段落 12](https://arxiv.org/html/2610.07696v1#S2.p2.1)
- [S12] [II Related Work · 正文段落 13](https://arxiv.org/html/2610.07696v1#S2.p3.1)
- [S13] [II Related Work · 正文段落 14](https://arxiv.org/html/2610.07696v1#S2.p4.1)
- [S14] [II Related Work · 正文段落 15](https://arxiv.org/html/2610.07696v1#S2.p5.1)
- [S15] [II Related Work · 正文段落 16](https://arxiv.org/html/2610.07696v1#S2.p6.1)
- [S16] [III Method · 正文段落 17](https://arxiv.org/html/2610.07696v1#S3.p1.1)
- [S17] [III Method · 正文段落 18](https://arxiv.org/html/2610.07696v1#S3.F2)
- [S18] [III-A Problem Setup and Pointwise Regression · 正文段落 19](https://arxiv.org/html/2610.07696v1#S3.SS1.p1.1)
- [S19] [III-A Problem Setup and Pointwise Regression · 正文段落 33](https://arxiv.org/html/2610.07696v1#S3.F3)
- [S20] [III-C Training Loss · 正文段落 40](https://arxiv.org/html/2610.07696v1#S3.SS3.p1.1)
- [S21] [III-C Training Loss · 正文段落 41](https://arxiv.org/html/2610.07696v1#S3.E5)
- [S22] [III-C Training Loss · 正文段落 42](https://arxiv.org/html/2610.07696v1#S3.SS3.p1.2)
- [S23] [III-D Direct One-Step Generation · 正文段落 43](https://arxiv.org/html/2610.07696v1#S3.SS4.p1.1)
- [S24] [III-D Direct One-Step Generation · 正文段落 44](https://arxiv.org/html/2610.07696v1#S3.SS4.p2.1)
- [S25] [IV-A Evaluation Protocol · 正文段落 45](https://arxiv.org/html/2610.07696v1#S4.SS1.p1.1)
- [S26] [IV-A Evaluation Protocol · 正文段落 46](https://arxiv.org/html/2610.07696v1#S4.SS1.p2.1)
- [S27] [IV-B Controlled Multimodal Regression · 正文段落 47](https://arxiv.org/html/2610.07696v1#S4.SS2.p1.1)
- [S28] [IV-B Controlled Multimodal Regression · 正文段落 48](https://arxiv.org/html/2610.07696v1#S4.SS2.p2.1)
- [S29] [IV-B Controlled Multimodal Regression · 正文段落 50](https://arxiv.org/html/2610.07696v1#S4.F4)
- [S30] [IV-C \pi_{0.5} on LIBERO · 正文段落 57](https://arxiv.org/html/2610.07696v1#S4.T1)
- [S31] [IV-E Multimodality Ablation · 正文段落 66](https://arxiv.org/html/2610.07696v1#S4.SS5.p1.1)
- [S32] [IV-E Multimodality Ablation · 正文段落 67](https://arxiv.org/html/2610.07696v1#S4.SS5.p2.1)
- [S33] [IV-E Multimodality Ablation · 正文段落 68](https://arxiv.org/html/2610.07696v1#S4.SS5.p3.1)
- [S34] [IV-E Multimodality Ablation · 正文段落 69](https://arxiv.org/html/2610.07696v1#S4.T3)
- [S35] [IV-E Multimodality Ablation · 正文段落 70](https://arxiv.org/html/2610.07696v1#S4.T3.4)
- [S36] [IV-E Multimodality Ablation · 正文段落 71](https://arxiv.org/html/2610.07696v1#S4.SS5.p4.1)
- [S37] [IV-E Multimodality Ablation · 正文段落 72](https://arxiv.org/html/2610.07696v1#S4.F6.2)
- [S38] [IV-E Multimodality Ablation · 正文段落 73](https://arxiv.org/html/2610.07696v1#S4.F6)
- [S39] [IV-F Real-World Manipulation with GR00T · 正文段落 74](https://arxiv.org/html/2610.07696v1#S4.SS6.p1.1)
- [S40] [IV-F Real-World Manipulation with GR00T · 正文段落 75](https://arxiv.org/html/2610.07696v1#S4.SS6.p2.1)
- [S41] [IV-F Real-World Manipulation with GR00T · 正文段落 77](https://arxiv.org/html/2610.07696v1#S4.SS6.p4.1)
- [S42] [V Limitations · 正文段落 79](https://arxiv.org/html/2610.07696v1#S5.p1.1)
- [S43] [V Limitations · 正文段落 80](https://arxiv.org/html/2610.07696v1#S5.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/ESP Energy-Score Policy for One-Step Multimodal Action Generation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generative action models based on diffusion and flow matching have been increasingly adopted in vision-language-action (VLA) policies for their ability to capture diverse behaviors, including multiple valid action sequences under the same observation and instruction. Their iterative sampling procedures, however, require repeated network evaluations to generate each action chunk, increasing inference latency in closed-loop control. We propose ESP (Energy-Score Policy), a teacher-free approach that maps policy context and noise directly to an action chunk in a single network evaluation. ESP trains the action head with the energy score rather than mean squared error. Whereas squared-error regression targets the conditional mean, the energy score is strictly proper: its expected value is uniquely minimized by the target distribution. This provides a principled objective for learning multimodal action distributions without iterative sampling, with exact recovery at the population optimum when the model can represent the target distribution. Experiments on both simulation and real-world manipulation tasks demonstrate competitive task success with substantially lower action-generation latency than the flow matching baseline. These results support direct distributional learning as an efficient alternative to iterative generative robot policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.07696v1
- Authors: Lilika Makabe, Heecheol Kim, Yasuyuki Matsushita
- Published: 2026-10-06T03:34:46Z
- Age days: 0

</details>
