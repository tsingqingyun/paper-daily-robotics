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
url: "https://arxiv.org/abs/2610.39744v1"
published: "2026-10-29T10:05:50Z"
age_days: 3
score: 28
created: 2026-11-02
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# PAPERBENCHX: Can AI Reproduce Science Across Disciplines?

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PaperBenchX 检查智能体能否把跨学科论文中的关键实验变成别人可以重新运行的证据。它把提交物放进干净环境重跑，只给重新生成且符合科学要求的结果计分。

## 问题

难点不是读懂结论或写出能执行的代码，而是补齐物理模型、数值条件和验证方法。原有复现基准多集中于机器学习；跨到电磁、化学等领域，软件配置本身就决定模拟的是什么系统，跑通也可能算错。[S3](https://arxiv.org/html/2610.39744v1#S1.p1.1) [S4](https://arxiv.org/html/2610.39744v1#S1.p2.1) [S5](https://arxiv.org/html/2610.39744v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）：输入一篇光学器件论文、目标透射曲线和仿真环境；智能体建立几何、材料和边界条件，运行并检查收敛，再输出频谱与分析脚本；评测器从零运行，检查曲线及其物理生成过程。

## 创新点或方法

相较于检查报告或代码，本文让领域专家先限定待复现主张，配好原生软件，建立私有参考流程，再制定建模、执行和验证评分。参考流程也须干净重跑，并经校准和独立专家审核。评测时智能体拿到论文、公开任务和环境，提交统一入口的运行包；评测器重建证据后按隐藏标准评分。这是评测流程，不是训练方法。[S13](https://arxiv.org/html/2610.39744v1#S3.SS1.p2.1) [S14](https://arxiv.org/html/2610.39744v1#S3.SS2.SSS0.Px1.p2.1) [S15](https://arxiv.org/html/2610.39744v1#S3.SS3.p2.1) [S16](https://arxiv.org/html/2610.39744v1#S3.SS3.p3.1)

### 方法如何工作

1. 专家把论文主张收缩成可执行任务，明确观测量和交付物，避免目标含糊。
2. 建立参考流程并在干净环境重放，再用有效、部分有效和无效流程校准评分。
3. 智能体独立重建实验、诊断运行并提交代码包，使过程可以被重新执行。
4. 评测器只收集重跑产物，分别评分建模、执行与验证，定位证据链断在哪里。

### 必要术语

- 领域原生环境：该学科实际使用的模拟器和数值软件；决定本文考核的操作与建模要求。
- 干净重放：清除先前运行状态后从提交包重新执行；检验结果是否独立可再生。
- 评分叶节点：可单独核验的细项；让有证据的部分进展获得分数，同时保留科学约束。

## 证据

93项任务覆盖12个研究领域、10种环境，测试10个智能体配置。最佳配置平均部分得分59.08%，但仅13项超过严格大于90%的完整复现阈值，完整率13.98%；71项没有任何配置完成。[S7](https://arxiv.org/html/2610.39744v1#S1.p5.1) [S18](https://arxiv.org/html/2610.39744v1#S4.SS2.SSS0.Px1.p1.1) [S29](https://arxiv.org/html/2610.39744v1#A2.SS1.SSS0.Px1.p1.1) 平均建模、执行、验证得分分别62.73%、61.83%、42.91%，支持验证是突出薄弱环节，但未单独证明低分的因果来源。

## 局限

完整复现是评分阈值定义，不意味着每个细节完全一致。结论针对选定任务、软件环境和资源预算，开发时限为4至72小时、中位7小时；不能外推成所有科研任务的成功率。[S30](https://arxiv.org/html/2610.39744v1#A2.SS1.SSS0.Px2.p1.1) 各配置还使用不同代理工具外壳，模型能力与运行系统贡献需分辨；待核查评分判断及失败修复对排名的影响。

- **判断**：值得读到任务合同、评分叶节点和失败案例：最有用的贡献是规定什么证据才算完成，而非单看排行榜。

## 研究关联

可借鉴的是把“能重新运行”和“支持科学主张”拆开验证。给科研智能体设验收条件时，应同时要求原始输出、收敛记录和从输出推导结论的过程，避免一张像论文的图掩盖错误模型。

### 下一步读哪里

从[S13](https://arxiv.org/html/2610.39744v1#S3.SS1.p2.1) [S26](https://arxiv.org/html/2610.39744v1#A1.SS1.SSS0.Px4.p1.1) [S31](https://arxiv.org/html/2610.39744v1#A2.SS2.p1.1) [S32](https://arxiv.org/html/2610.39744v1#A2.SS2.p2.1)检查证据准入、单位和参考流程审核，再看[S20](https://arxiv.org/html/2610.39744v1#S5.SS0.SSS0.Px4.p1.1) [S33](https://arxiv.org/html/2610.39744v1#A3.SS2.SSS0.Px1.p2.1)中“执行成功但科学验证失败”的实例。公开演示包有12项，不能把演示覆盖等同全部93项。[S27](https://arxiv.org/html/2610.39744v1#A1.SS3.p1.1)

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.39744v1
- 获取时间：2026-11-02T01:18:50.867158+00:00
- [S1] [PaperBenchX: Can AI Reproduce Science Across Disciplines? · 正文段落 1](https://arxiv.org/html/2610.39744v1#abstract1.1)
- [S2] [PaperBenchX: Can AI Reproduce Science Across Disciplines? · 正文段落 2](https://arxiv.org/html/2610.39744v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.39744v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.39744v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.39744v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.39744v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.39744v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.39744v1#S1.I1.i2)
- [S9] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.39744v1#S2.T1.4.1)
- [S10] [2.1 Machine-Learning Research and Paper Reproduction · 正文段落 15](https://arxiv.org/html/2610.39744v1#S2.SS1.p1.1)
- [S11] [2.2 Cross-Domain Scientific Benchmarks · 正文段落 16](https://arxiv.org/html/2610.39744v1#S2.SS2.p1.1)
- [S12] [2.2 Cross-Domain Scientific Benchmarks · 正文段落 17](https://arxiv.org/html/2610.39744v1#S2.SS2.p2.1)
- [S13] [3.1 Task Definition · 正文段落 21](https://arxiv.org/html/2610.39744v1#S3.SS1.p2.1)
- [S14] [Benchmark composition. · 正文段落 24](https://arxiv.org/html/2610.39744v1#S3.SS2.SSS0.Px1.p2.1)
- [S15] [3.3 Task Construction Pipeline · 正文段落 27](https://arxiv.org/html/2610.39744v1#S3.SS3.p2.1)
- [S16] [3.3 Task Construction Pipeline · 正文段落 28](https://arxiv.org/html/2610.39744v1#S3.SS3.p3.1)
- [S17] [3.4 Evaluation · 正文段落 39](https://arxiv.org/html/2610.39744v1#S3.SS4.p5.3)
- [S18] [Overall performance. · 正文段落 44](https://arxiv.org/html/2610.39744v1#S4.SS2.SSS0.Px1.p1.1)
- [S19] [Partial Progress Rarely Composes into Full Reproduction. · 正文段落 47](https://arxiv.org/html/2610.39744v1#S5.SS0.SSS0.Px1.p1.1)
- [S20] [Final Outputs Alone Cannot Distinguish Scientific Failure Modes. · 正文段落 52](https://arxiv.org/html/2610.39744v1#S5.SS0.SSS0.Px4.p1.1)
- [S21] [Final Outputs Alone Cannot Distinguish Scientific Failure Modes. · 正文段落 54](https://arxiv.org/html/2610.39744v1#S5.SS0.SSS0.Px4.p3.1)
- [S22] [6 Conclusion · 正文段落 55](https://arxiv.org/html/2610.39744v1#S6.p1.1)
- [S23] [Components and evaluation-time visibility. · 正文段落 61](https://arxiv.org/html/2610.39744v1#A1.SS1.SSS0.Px1.p1.1)
- [S24] [Components and evaluation-time visibility. · 正文段落 63](https://arxiv.org/html/2610.39744v1#A1.T1)
- [S25] [Worked scientific contract. · 正文段落 66](https://arxiv.org/html/2610.39744v1#A1.T2)
- [S26] [Evaluator policy. · 正文段落 68](https://arxiv.org/html/2610.39744v1#A1.SS1.SSS0.Px4.p1.1)
- [S27] [A.3 Public Demonstration Tasks · 正文段落 73](https://arxiv.org/html/2610.39744v1#A1.SS3.p1.1)
- [S28] [A.3 Public Demonstration Tasks · 正文段落 74](https://arxiv.org/html/2610.39744v1#A1.T4)
- [S29] [Evaluation scope. · 正文段落 81](https://arxiv.org/html/2610.39744v1#A2.SS1.SSS0.Px1.p1.1)
- [S30] [Resource envelopes. · 正文段落 82](https://arxiv.org/html/2610.39744v1#A2.SS1.SSS0.Px2.p1.1)
- [S31] [B.2 Expert Annotation and Release Review · 正文段落 84](https://arxiv.org/html/2610.39744v1#A2.SS2.p1.1)
- [S32] [B.2 Expert Annotation and Release Review · 正文段落 85](https://arxiv.org/html/2610.39744v1#A2.SS2.p2.1)
- [S33] [Eight-element smartphone MIMO (Task 1-1). · 正文段落 99](https://arxiv.org/html/2610.39744v1#A3.SS2.SSS0.Px1.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/PAPERBENCHX Can AI Reproduce Science Across Disciplines.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Before AI can be trusted to discover new science, it should be able to reproduce what science already knows. Reproduction provides a rigorous checkpoint for an AI scientist: the target claim is known, yet recovering it still requires translating an incomplete scientific description into an executable experiment and producing evidence that can be independently verified. Existing research-reproduction benchmarks largely focus on AI and machine learning, where experiments share relatively homogeneous software stacks. Extending this capability across scientific disciplines introduces a different challenge: agents must operate domain-specific scientific software, make physical and numerical choices, diagnose long-running computations, and distinguish valid evidence from merely plausible outputs. We introduce PAPERBENCHX, a benchmark of 93 expert-constructed paper-reproduction tasks spanning 12 research areas across electromagnetics, photonics, chemistry, materials science, biology, and robotics. Each task provides the source paper, a public task specification, and a domain-native scientific environment involving specialized scientific software. Agents must reconstruct a key experiment, execute and diagnose it, and deliver a runnable workflow that supports the target scientific claim. To evaluate scientific validity rather than surface-level agreement, we replay every submission from scratch and score only regenerated evidence against expert-validated criteria. Across 10 frontier agent configurations, the best configuration fully reproduces only 14% tasks under the 90% threshold. Meanwhile, mean rubric scores range from 27.53% to 59.08%, indicating that substantial partial progress rarely translates into complete scientific reproduction. These results reveal a large gap between paper understanding and reliably producing reproducible scientific evidence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39744v1
- Authors: Ruoyu Wu, Zengji Tu, Aolong Sun, Tianyi Ma, Junren Li, Xinbo Xu, Li Fu, Ziyan Zhang, Pinrui Huang, Xiaochen Wang, Chengda Wu, Yutao Zhou, Jianjun Wu, Lin Chang, Baobao Chang, Liang Chen, Kuan Li
- Published: 2026-10-29T10:05:50Z
- Age days: 3

</details>
