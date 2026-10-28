---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.35385v1"
published: "2026-10-26T13:06:33Z"
age_days: 1
score: 36
created: 2026-10-28
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# EmbodiedLab: Benchmarking Embodied Agents That Act to Know

> [!summary] 这篇论文到底做了什么（基于摘要）
> EmbodiedLab 让机器人自己设计并操作实验，从实际读数中找出答案。它评测的不只是机器人有没有改变物体状态，还包括它是否通过操作获得了有证据支持的知识。

## 问题

任务是给定实验目标和仪器，让机器人自行决定操作顺序、观察反馈并得出结论。普通操作评测预先给出目标状态；科学发现评测又常把物理实验简化成符号操作或数值查询。两者都难以检验：机器人能否把实验想法变成可靠操作，再把读数变成答案。

### 用一个例子理解

理解用例（非论文实验）：输入是“测出未知弹簧的刚度”和实验装置；机器人逐次加载已知重量，用相机读取伸长量，再据此计算刚度；输出包括估计值及对应读数，而非只报一个数字。

## 创新点或方法

旧评测把操作或求知单独拿出来；本文把两者放进同一物理仿真实验室。每个实例重新采样系统参数，使答案不能提前记住，又能精确评分。运行时，智能体通过相机读取仪器，自行选择实验程序；评测同时检查结论、当次记录的读数和必要物理状态。作者还比较原生控制、加入感知与运动规划、加入从强智能体蒸馏的操作技能；技能训练细节未说明。

### 方法如何工作

1. 为实例重新采样系统参数，得到一个答案未知但可评分的实验，避免靠记忆直接作答。
2. 智能体接收目标与仪器，自行安排操作，以产生能回答问题的观测。
3. 执行操作并通过相机读取仪表，把物理反馈变成后续决策依据。
4. 提交结论后，对照当次读数和目标物理状态评分，检查求知与执行是否同时成立。

### 必要术语

- 主动求知：为了获得信息而行动；本文以物理实验检验这种能力。
- 原生控制：使用智能体原有的观察与控制方式；本文以此衡量加入辅助能力前的表现。
- 技能蒸馏：把强智能体的操作经验转成可复用技能；具体训练形式摘要未说明。

## 证据

摘要报告覆盖五个学科、14 类仪器平台的 30 个实验，每项均验证可解；测试六个前沿模型及其开发者的编程智能体。原生控制下，最强智能体成功率仍低于一半；每个智能体的大多数失败来自仪器交互，弱智能体从操作技能获得的帮助超过感知与规划。摘要未给逐任务成功率、重复次数和失败分类规则，因此支持的是该仿真实验室中的瓶颈判断。

## 局限

这里验证的是物理仿真中的实验能力，不能直接推到真机。交互失败最多也不等于推理已足够好；我会核查错误实验设计是否被计入操作失败，以及不同辅助工具的接口是否公平。

- **判断**：值得读评测协议和失败案例，尤其适合用来判断实验型智能体究竟缺推理能力还是操作能力。

## 研究关联

可借鉴的是把“答案正确”与“答案来自本次实验”分开检查。当任务需要主动测量未知量时，最终回答正确还不够，必须能追溯到操作和读数。

### 下一步读哪里

先核查知识答案如何绑定当次读数，再看失败分类、辅助技能的训练来源，以及可解性由谁、用什么控制条件验证。提供材料没有正文节选，具体评分容差和实验表格仍需查原文。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/EmbodiedLab Benchmarking Embodied Agents That Act to Know.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied agents are expected to accomplish real-world goals by deciding for themselves how and when to interact with their surroundings. For many such goals, changing the physical state of the world is the means rather than the end: the agent changes the state of a system through interaction, observes the feedback, and explores until it either achieves the goal itself (e.g., discovering physical laws) or learns what the goal requires; it acts to know. Manipulation benchmarks stop at acting to change, with the target state given; scientific discovery benchmarks evaluate knowing but replace physical experimentation with symbolic actions or numerical queries. We introduce EmbodiedLab, a benchmark in which a robot must act to know. Quantitative science experiments make this setting controllable: the parameters of the system are resampled for every instance, so the result cannot be known in advance, yet it can be scored exactly. Across 30 experiments in five disciplines on 14 apparatus platforms, the agent receives an objective and the apparatus, chooses its own procedure, and operates a physics-based simulated laboratory, reading the instruments through its cameras. Evaluation checks what the agent came to know, grounded in readings recorded during the episode, as well as the physical state the task requires; every experiment is verified to be solvable. We evaluate six frontier models in their developers' coding agents with native observation and control, with added perception and motion planning, and with manipulation skills distilled from the strongest agents. With native control, even the strongest agent succeeds less than half the time; for every agent, most failures arise in interacting with the apparatus, and manipulation skills help weaker agents more than perception and planning. The benchmark and its evaluation code are available at https://github.com/HexaFuture/EmbodiedLab.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.35385v1
- Authors: Hongcheng Gao, Zelin Zheng, Alex Zhou, Jay Zhu, Shijia Ge, Yazhe Wang, Xiping Li, Jianshu Zeng, Di Wu, Xuan Shangguan, Yexing Wan, Lingyu He, Yongli Wang, Xiaohan Yu, Zhiqi Jia, Yue Liu, Bryan Hooi, Yinpeng Dong, Wentao Zhang, Sihang Wu, Xiao He
- Published: 2026-10-26T13:06:33Z
- Age days: 1

</details>
