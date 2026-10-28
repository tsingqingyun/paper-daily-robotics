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
url: "https://arxiv.org/abs/2610.35010v1"
published: "2026-10-26T08:21:02Z"
age_days: 1
score: 37
created: 2026-10-28
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> JevVLA 冻结原策略，另学一个小模型判断动作好坏：离散动作靠比较分数来选，连续动作靠分数对动作的梯度来修正。巧处是同一种标量函数同时承担“挑选”和“微调方向”两种工作。

## 问题

抓放策略可能要从候选中选一个，运动策略则直接生成连续动作段；两者都可能语义正确却几何上差一点。完整微调成本高，而只会排序的评价器也未必能提供可靠修正方向。[S4](https://arxiv.org/html/2610.35010v1#S1.p1.1) [S15](https://arxiv.org/html/2610.35010v1#S2.SS3.p2.1) 本文要保留原动作生成器，用小规模训练改善决策。

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放到托盘中央”和图像；冻结策略给出几个落点，适配器挑出较优候选；若使用连续接口，则对落点做有幅度限制的梯度修正，输出调整后的动作。

## 创新点或方法

旧做法直接采用原策略输出；JevVLA把观测、任务和动作编码后送进能量函数，由条件二次项和非线性残差共同打分。训练只更新适配器，按数据来源使用执行成败、专家纠正或示范距离监督；连续设置还监督动作附近的修正方向。推理时比较候选能量，或沿负梯度做有限修正、引导生成。[S7](https://arxiv.org/html/2610.35010v1#S1.p5.1) [S18](https://arxiv.org/html/2610.35010v1#S3.F2) [S23](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p4.1) [S24](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p1.1) [S25](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p1.2) [S26](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p2.2) 各基准共享结构，分别训练权重。

### 方法如何工作

1. 冻结原策略和特征编码器，保留原有生成能力，取得动作提案。
2. 把场景、任务与提案编码进小型能量核心，得到可比较的标量。
3. 用成败或纠正训练能量；连续场景额外学习局部方向，避免只会排序。
4. 部署时按能量选候选，或用其动作梯度有限修正，再由原控制接口执行。

### 必要术语

- 能量函数：给场景中的动作一个标量评价；本文用它表达相对偏好。
- 动作梯度：分数随动作改变的方向；本文据此计算连续修正。
- 冻结策略：保留原模型权重；本文只训练旁边的小适配器。

## 证据

在MetaWorld MT50、VIMA、LanguageTable、LIBERO Plus、CLIPort的独立测试集，相对各自冻结基线的成功率分别增加1.28、2.31、1.60、1.52、1.28个百分点。[S8](https://arxiv.org/html/2610.35010v1#S1.p6.1) 基线包括π0.5、VIMA-200M、行为克隆和CLIPort；核心为79,817参数，CLIPort按闭环执行后的完整成功计分。[S28](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px1.p1.1) [S29](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px2.p1.1) [S30](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px2.p2.1) [S31](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px3.p1.1) 证据支持同一结构适配不同接口，但增益较小，不能解释为一套权重跨任务通用。

## 局限

作者指出候选选择受原策略候选覆盖限制，排序正确也不保证梯度可靠。[S15](https://arxiv.org/html/2610.35010v1#S2.SS3.p2.1) 示范距离只是动作接近程度，不等于执行成功。我的待核查问题是小幅增益的统计不确定性、额外推理成本，以及相对等预算微调的收益；节选未提供这些完整比较，不能据此断言全文缺失或真机有效。

- **判断**：值得细读能量监督与推理更新规则；把它当作小型适配器方案评估，别把跨基准结构复用理解成通用控制器。

## 研究关联

若已有可用策略，问题集中在候选取舍或局部偏差，可以先尝试训练评价器；但若要用梯度修动作，训练目标必须教会它邻域方向，不能只要求好动作排名更高。

### 下一步读哪里

从[S23](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p4.1) [S24](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p1.1) [S25](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p1.2) [S26](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p2.2)检查偏好和梯度标签如何构造；再核查动作编码、修正幅度及验证集选参。读消融时注意[S22](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p3.2) [S32](https://arxiv.org/html/2610.35010v1#S4.SS4.p1.1)提醒：部分比较同时改变结构和损失，不能单独归因。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.35010v1
- 获取时间：2026-10-28T01:41:09.425624+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.35010v1#p1.2)
- [S2] [JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies · 正文段落 2](https://arxiv.org/html/2610.35010v1#abstract1.1)
- [S3] [JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies · 正文段落 3](https://arxiv.org/html/2610.35010v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.35010v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.35010v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.35010v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.35010v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.35010v1#S1.p6.1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.35010v1#S1.I1.i1)
- [S10] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.35010v1#S1.I1.i3)
- [S11] [2.1 Vision–language–action models · 正文段落 14](https://arxiv.org/html/2610.35010v1#S2.SS1.p1.1)
- [S12] [2.1 Vision–language–action models · 正文段落 15](https://arxiv.org/html/2610.35010v1#S2.SS1.p2.1)
- [S13] [2.2 Robot preference learning · 正文段落 16](https://arxiv.org/html/2610.35010v1#S2.SS2.p1.1)
- [S14] [2.2 Robot preference learning · 正文段落 17](https://arxiv.org/html/2610.35010v1#S2.SS2.p2.1)
- [S15] [2.3 Energy-based action selection · 正文段落 19](https://arxiv.org/html/2610.35010v1#S2.SS3.p2.1)
- [S16] [2.4 Inference-time action guidance · 正文段落 21](https://arxiv.org/html/2610.35010v1#S2.SS4.p2.1)
- [S17] [3 Method · 正文段落 24](https://arxiv.org/html/2610.35010v1#S3.p1.1)
- [S18] [3 Method · 正文段落 25](https://arxiv.org/html/2610.35010v1#S3.F2)
- [S19] [3.3 Learning action preferences · 正文段落 41](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p1.1)
- [S20] [3.3 Learning action preferences · 正文段落 46](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p2.2)
- [S21] [3.3 Learning action preferences · 正文段落 47](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p3.1)
- [S22] [3.3 Learning action preferences · 正文段落 49](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p3.2)
- [S23] [3.3 Learning action preferences · 正文段落 50](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px1.p4.1)
- [S24] [3.3 Learning action preferences · 正文段落 51](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p1.1)
- [S25] [3.3 Learning action preferences · 正文段落 53](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p1.2)
- [S26] [3.3 Learning action preferences · 正文段落 56](https://arxiv.org/html/2610.35010v1#S3.SS3.SSS0.Px2.p2.2)
- [S27] [4 Experiments · 正文段落 72](https://arxiv.org/html/2610.35010v1#S4.p1.1)
- [S28] [4.1 Experimental setup · 正文段落 73](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px1.p1.1)
- [S29] [4.1 Experimental setup · 正文段落 74](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px2.p1.1)
- [S30] [4.1 Experimental setup · 正文段落 75](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px2.p2.1)
- [S31] [4.1 Experimental setup · 正文段落 76](https://arxiv.org/html/2610.35010v1#S4.SS1.SSS0.Px3.p1.1)
- [S32] [4.4 Ablation studies · 正文段落 96](https://arxiv.org/html/2610.35010v1#S4.SS4.p1.1)
- [S33] [5 Conclusion · 正文段落 128](https://arxiv.org/html/2610.35010v1#S5.p1.1)
- [S34] [5 Conclusion · 正文段落 129](https://arxiv.org/html/2610.35010v1#S5.p2.1)
- [S35] [Appendix C Comparison method results by task · 正文段落 152](https://arxiv.org/html/2610.35010v1#A3.p1.1)
- [S36] [Appendix C Comparison method results by task · 正文段落 153](https://arxiv.org/html/2610.35010v1#A3.T16)
- [S37] [Appendix C Comparison method results by task · 正文段落 155](https://arxiv.org/html/2610.35010v1#A3.p2.1)
- [S38] [Appendix C Comparison method results by task · 正文段落 156](https://arxiv.org/html/2610.35010v1#A3.T17)
- [S39] [Appendix C Comparison method results by task · 正文段落 158](https://arxiv.org/html/2610.35010v1#A3.p3.1)
- [S40] [Appendix C Comparison method results by task · 正文段落 159](https://arxiv.org/html/2610.35010v1#A3.T18)
- [S41] [Appendix C Comparison method results by task · 正文段落 161](https://arxiv.org/html/2610.35010v1#A3.p4.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/JevVLA Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies can select among discrete candidates for pick-and-place manipulation or generate continuous action chunks for motion control. Improving both forms of decision making through a common mechanism while retaining the capabilities of a pretrained policy is an important adaptation problem. Inspired by Jev's structured, probabilistic decision interface, we propose JevVLA, a lightweight energy-based adaptation framework for VLA policies. JevVLA instantiates this inspiration by modeling the relative quality of action proposals: with the base policy frozen, it learns a differentiable scalar energy conditioned on observations, task context, and actions, using execution feedback, expert corrections, or demonstration-derived preferences. JevVLA uses this single learned action preference function in two ways: its values compare discrete candidates, while its action gradients correct continuous actions or guide their generation. Candidate selection and continuous control thus share one trainable decision core. Each benchmark uses independently trained weights and fixed input/output encodings, while retaining the same core network with approximately 80,000 trainable parameters. On the held-out test sets, JevVLA improves task success over the respective matched base-policy controls by 1.28, 2.31, 1.60, 1.52, and 1.28 percentage points on MetaWorld MT50, VIMA, LanguageTable, LIBERO Plus, and CLIPort, respectively. These results support the feasibility of a lightweight, Jev-inspired energy model for adapting both discrete action selection and continuous action guidance. The JevVLA implementation will be open-sourced at https://github.com/ZJU4EmbodiedAI/JevVLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.35010v1
- Authors: Wei Wang, Wenqiao Zhang, Zheqi Lv, Zheng Dong, Yingjie Niu, Jiaqi Zhu, Jun Xiao, Chao Li, Yueting Zhuang
- Published: 2026-10-26T08:21:02Z
- Age days: 1

</details>
