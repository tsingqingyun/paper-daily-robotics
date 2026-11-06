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
url: "https://arxiv.org/abs/2611.06768v1"
published: "2026-11-04T16:46:03Z"
age_days: 1
score: 36
created: 2026-11-06
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PyRUA-REAL 让编程智能体在真机上运行程序、检查失败、改代码，再把经验和能复用的技能留下来。改进发生在程序和经验库里，模型权重固定，成熟程序可以独立执行并根据实时观测闭环控制。

## 问题

让智能体现场完成一次操作，和把这次操作变成下次还能用的技能，是两件事。失败可能源于看错、走错，甚至验收方式有误；只反复调当前程序的参数也可能一直困在不合适的方案里。部署时若每个阶段都等模型决策，还会增加延迟。[S4](https://arxiv.org/html/2611.06768v1#S1.p1.1) [S5](https://arxiv.org/html/2611.06768v1#S1.p2.1) [S6](https://arxiv.org/html/2611.06768v1#S1.p3.1) [S7](https://arxiv.org/html/2611.06768v1#S1.p4.1)[S13](https://arxiv.org/html/2611.06768v1#S2.p2.1)

### 用一个例子理解

理解用例（非论文实验）。输入是“把方块收进盒子”和一段抓取失败的相机记录。工程师发现程序沿用了旧的盒口位置，于是改成落下前重新定位；研究员在不同摆位下复测后，把定位步骤和适用条件存入库。输出是一段能读当前画面、自动修正放置位置的程序。

## 创新点或方法

研究员智能体选技术路线、写实验目标和停止条件，工程师智能体实现程序、跑真机、用画面和日志定位故障。报告回到研究员手里，供它判断继续局部修补还是换路线，并把环境事实、失败条件和可复用代码一起保存。开发阶段可以反复调用智能体；冻结后由程序里的感知、规划、控制和恢复逻辑处理现场变化，也可以调用本地感知模型。[S7](https://arxiv.org/html/2611.06768v1#S1.p4.1)[S22](https://arxiv.org/html/2611.06768v1#S3.SS2.p2.1) [S23](https://arxiv.org/html/2611.06768v1#S3.SS2.p3.1) [S24](https://arxiv.org/html/2611.06768v1#S3.SS3.p1.1) [S25](https://arxiv.org/html/2611.06768v1#S3.SS4.p2.1)

### 方法如何工作

1. 研究员用任务要求与经验库确定当前实验要解决什么，写清何时停止，给工程师划定试验范围。[S22](https://arxiv.org/html/2611.06768v1#S3.SS2.p2.1) [S23](https://arxiv.org/html/2611.06768v1#S3.SS2.p3.1) [S24](https://arxiv.org/html/2611.06768v1#S3.SS3.p1.1)
2. 工程师实现并运行程序，收集现场画面、状态和日志，把笼统的失败变成可以定位的证据。[S23](https://arxiv.org/html/2611.06768v1#S3.SS2.p3.1)
3. 根据证据修代码或换方案，把成功和失败的适用条件都写回库，使下一轮能沿用已有结论。[S24](https://arxiv.org/html/2611.06768v1#S3.SS3.p1.1) [S25](https://arxiv.org/html/2611.06768v1#S3.SS4.p2.1)
4. 冻结通过测试的程序，用实时感知和恢复逻辑独立执行，并单独测量它在部署中的表现。[S7](https://arxiv.org/html/2611.06768v1#S1.p4.1)[S29](https://arxiv.org/html/2611.06768v1#S4.SS3.p1.1) [S30](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS1.p1.1)

### 必要术语

- 具身递归自改进（RSI）：反复让实体执行结果指导下一轮改动；本文迭代的是机器人程序与经验库。
- 冻结程序：部署时固定代码版本的控制程序；本文用它检验技能能否脱离在线语言模型调用独立执行。

## 证据

双臂 Franka 的八项真机任务在开发记录中平均成功率为 91.1%，汇总了不同代码版本的尝试。七项得到可独立运行的程序；网线插接的开发记录里，脚本执行 0/4，带在线协助的流程 10/17。RoboDojo 仿真中，42 项任务的冻结程序按能力组等权平均为 84.42%，PyRUA-Lean 和 GPT-6-Astra 的报告值为 50.35% 和 22.48%。这里采用实验节与附录表一致的 84.42%，引言另写 84.82%。[S8](https://arxiv.org/html/2611.06768v1#S1.p5.1)[S26](https://arxiv.org/html/2611.06768v1#S4.p1.1)[S30](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS1.p1.1) [S31](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS1.p2.1) [S32](https://arxiv.org/html/2611.06768v1#S4.F5) [S33](https://arxiv.org/html/2611.06768v1#S4.F8) [S34](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS3.p1.1) [S35](https://arxiv.org/html/2611.06768v1#S4.SS8.SSS0.Px2.p1.1)[S41](https://arxiv.org/html/2611.06768v1#A4.p1.1) [S42](https://arxiv.org/html/2611.06768v1#A4.T5) [S43](https://arxiv.org/html/2611.06768v1#A4.T5.7)

## 局限

作者指出，超出已编写恢复逻辑的情况仍可能需要在线判断，网线插接就是例子。[S36](https://arxiv.org/html/2611.06768v1#S5.SS0.SSS0.Px3.p1.1) RoboDojo 对照来自不同或未注明种子的独立评测，分差无法归因到某一项设计。我会核查真机冻结程序在独立布局上的成功率与耗时，以及在线协助中人的复核承担了多少判断。[S34](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS3.p1.1) [S35](https://arxiv.org/html/2611.06768v1#S4.SS8.SSS0.Px2.p1.1)[S41](https://arxiv.org/html/2611.06768v1#A4.p1.1) [S42](https://arxiv.org/html/2611.06768v1#A4.T5)

- **判断**：值得读到失败诊断和冻结部署实验，因为这两处最能区分智能体解决了当场问题，还是留下了以后能稳定执行的程序。

## 研究关联

保存技能时，把它依赖的物体姿态、观测条件、恢复逻辑和已知失败一起记下来。下一次改程序时，这些记录可以帮助判断旧技能能否直接调用，以及新实验该改局部实现还是重新选方案。

### 下一步读哪里

先读 [S22](https://arxiv.org/html/2611.06768v1#S3.SS2.p2.1) [S23](https://arxiv.org/html/2611.06768v1#S3.SS2.p3.1) [S24](https://arxiv.org/html/2611.06768v1#S3.SS3.p1.1) [S25](https://arxiv.org/html/2611.06768v1#S3.SS4.p2.1) 的实验交接与经验记录，再对照 [S30](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS1.p1.1) [S31](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS1.p2.1) [S32](https://arxiv.org/html/2611.06768v1#S4.F5) [S33](https://arxiv.org/html/2611.06768v1#S4.F8) [S34](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS3.p1.1) [S35](https://arxiv.org/html/2611.06768v1#S4.SS8.SSS0.Px2.p1.1) 区分首次成功、开发成功率和部署表现。看 RoboDojo 时按 [S41](https://arxiv.org/html/2611.06768v1#A4.p1.1) [S42](https://arxiv.org/html/2611.06768v1#A4.T5) [S43](https://arxiv.org/html/2611.06768v1#A4.T5.7) 核对种子、平均方式和各能力项，避免用总分代替迁移表现。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.06768v1
- 获取时间：2026-11-06T00:08:05.889853+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.06768v1#p1.1)
- [S2] [PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World · 正文段落 2](https://arxiv.org/html/2611.06768v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.06768v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.06768v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.06768v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.06768v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.06768v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.06768v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.06768v1#S1.I1.i1)
- [S10] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.06768v1#S1.I1.i2)
- [S11] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.06768v1#S1.I1.i3)
- [S12] [2 Related Work · 正文段落 12](https://arxiv.org/html/2611.06768v1#S2.p1.1)
- [S13] [2 Related Work · 正文段落 13](https://arxiv.org/html/2611.06768v1#S2.p2.1)
- [S14] [2 Related Work · 正文段落 14](https://arxiv.org/html/2611.06768v1#S2.p3.1)
- [S15] [2 Related Work · 正文段落 15](https://arxiv.org/html/2611.06768v1#S2.p4.1)
- [S16] [3.1 Problem Formulation · 正文段落 18](https://arxiv.org/html/2611.06768v1#S3.SS1.p1.2)
- [S17] [3.1 Problem Formulation · 正文段落 19](https://arxiv.org/html/2611.06768v1#S3.SS1.p2.1)
- [S18] [3.1 Problem Formulation · 正文段落 22](https://arxiv.org/html/2611.06768v1#S3.SS1.p3.1)
- [S19] [3.1 Problem Formulation · 正文段落 24](https://arxiv.org/html/2611.06768v1#S3.SS1.p3.2)
- [S20] [3.1 Problem Formulation · 正文段落 25](https://arxiv.org/html/2611.06768v1#S3.SS1.p4.1)
- [S21] [3.1 Problem Formulation · 正文段落 26](https://arxiv.org/html/2611.06768v1#S3.F2)
- [S22] [3.2 System Overview · 正文段落 28](https://arxiv.org/html/2611.06768v1#S3.SS2.p2.1)
- [S23] [3.2 System Overview · 正文段落 29](https://arxiv.org/html/2611.06768v1#S3.SS2.p3.1)
- [S24] [3.3 Coding Agents Collaboration · 正文段落 30](https://arxiv.org/html/2611.06768v1#S3.SS3.p1.1)
- [S25] [3.4 Persistent Experience and Skill Evolution · 正文段落 37](https://arxiv.org/html/2611.06768v1#S3.SS4.p2.1)
- [S26] [4 Experiments and Empirical Findings · 正文段落 38](https://arxiv.org/html/2611.06768v1#S4.p1.1)
- [S27] [4.1 Research Question and Hypotheses · 正文段落 39](https://arxiv.org/html/2611.06768v1#S4.SS1.p1.1)
- [S28] [4.1 Research Question and Hypotheses · 正文段落 41](https://arxiv.org/html/2611.06768v1#S4.SS1.p3.1)
- [S29] [4.3 Embodied RSI Performance in the Real World and Simulated Environments · 正文段落 54](https://arxiv.org/html/2611.06768v1#S4.SS3.p1.1)
- [S30] [4.3.1 Real-world capability acquisition with agent · 正文段落 55](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS1.p1.1)
- [S31] [4.3.1 Real-world capability acquisition with agent · 正文段落 56](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS1.p2.1)
- [S32] [4.3.1 Real-world capability acquisition with agent · 正文段落 57](https://arxiv.org/html/2611.06768v1#S4.F5)
- [S33] [4.3.3 Additional Evaluation on RoboDojo · 正文段落 65](https://arxiv.org/html/2611.06768v1#S4.F8)
- [S34] [4.3.3 Additional Evaluation on RoboDojo · 正文段落 66](https://arxiv.org/html/2611.06768v1#S4.SS3.SSS3.p1.1)
- [S35] [4.8 Offline Coding: Execution Efficiency and Capability · 正文段落 83](https://arxiv.org/html/2611.06768v1#S4.SS8.SSS0.Px2.p1.1)
- [S36] [5 Discussion · 正文段落 86](https://arxiv.org/html/2611.06768v1#S5.SS0.SSS0.Px3.p1.1)
- [S37] [6 Conclusion · 正文段落 87](https://arxiv.org/html/2611.06768v1#S6.p1.1)
- [S38] [Appendix A Execution Feedback: Protocol, Costs, and Diagnostic Traces · 正文段落 93](https://arxiv.org/html/2611.06768v1#A1.F15)
- [S39] [Appendix B Generalization under Explicit Task Requirements: Per-Task Results · 正文段落 109](https://arxiv.org/html/2611.06768v1#A2.p1.1)
- [S40] [Appendix B Generalization under Explicit Task Requirements: Per-Task Results · 正文段落 110](https://arxiv.org/html/2611.06768v1#A2.T4)
- [S41] [Appendix D Full RoboDojo Results · 正文段落 120](https://arxiv.org/html/2611.06768v1#A4.p1.1)
- [S42] [Appendix D Full RoboDojo Results · 正文段落 121](https://arxiv.org/html/2611.06768v1#A4.T5)
- [S43] [Appendix D Full RoboDojo Results · 正文段落 122](https://arxiv.org/html/2611.06768v1#A4.T5.7)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/PyRUA-REAL Robot Exploration and Adaptive Learning through RSI in the Real World.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Coding agents powered by models such as GPT-6-Astra connect spatial reasoning with executable robot behavior, raising the question of how such agents can produce lasting improvements in robot capabilities from physical interaction. In this work, we study embodied recursive self-improvement (RSI) through real-world exploration, code refinement, and deployment using PyRUA-REAL, a framework in which coding agents retain interaction experience as persistent memory and reusable executable skills that inform subsequent exploration and improvement. Our empirical study places physical manipulation at the center of the improvement process, examining how agents collaborate, what kinds of execution feedback support effective code refinement, and how task specifications and previously acquired skills influence robustness and task transfer. We further investigate the efficiency and capability of the resulting programs when deployed without involving an online agent for decision-making. Across eight real-world tasks, PyRUA-REAL achieves an average success rate of 91.1%. In complementary evaluation on 42 tasks from the RoboDojo benchmark, it achieves an average success rate of 84.4%. This study provides empirical guidance for turning physical exploration into reusable robot skills that support continued improvement and robust, efficient deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.06768v1
- Authors: Qiang Wang, Jianxin Bi, Shulong Jiang, Ruiyang Si, Wenbo Huang, Kaiqi Chen, Jiaxin Li, Liyun Li, Xuanyi Li, Daquan Zhou
- Published: 2026-11-04T16:46:03Z
- Age days: 1

</details>
