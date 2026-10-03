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
url: "https://arxiv.org/abs/2610.00317"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-10-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# DriftOPD: Sequence-Level Reverse-KL Distillation for One-Step VLA Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> DriftOPD 用离线示范学习“这个动作对后续完成任务有多大帮助”，再把这种依据加入一步动作生成的训练。它无需在线试跑或独立教师，目标是让生成便宜的动作专家也顾及长期后果。

## 问题

VLA 常一次生成一小段动作、执行后重新规划，但按动作块训练主要优化局部动作似然，没有显式考虑整个任务成功。序列级强化学习可以考虑后果，却通常需要策略试跑和闭环交互，在真机上成本高。

### 用一个例子理解

理解用例（非论文实验）：机器人要取出挡板后的物体。输入画面与任务；训练中的 Q 评价帮助偏好先移开挡板的动作；推理时专家一步输出该动作块，执行后再根据新画面继续。

## 创新点或方法

旧做法只匹配局部动作，本文将序列级反向 KL 分解为动作块项和反映后续影响的未来势能项。训练时用一步 drifting 目标优化前者，用离线示范学出的 Q 函数评价后者，从而在不在线交互的条件下加入长期依据。推理时动作专家一步生成动作，摘要未说明是否需要调用 Q 函数；drifting 目标的具体构造也未给出。

### 方法如何工作

1. 从离线示范学习 Q 函数，估计当前动作与后续任务结果的关系，为长期评价提供依据。
2. 将序列级反向 KL 拆成局部动作项和未来势能项，使长期目标能够分项处理。
3. 用一步 drifting 目标及 Q 评价共同训练动作专家，同时约束局部生成和后续效果；摘要只说明到此。
4. 部署时一步生成短动作块并按滚动方式继续执行，避免多轮动作生成带来的成本。

### 必要术语

- 动作块：一次生成的一小段连续动作；本文优化的基本动作单位。
- 反向 KL：衡量分布差异的一种方向；本文从序列层面将它拆成局部与未来两项。
- Q 函数：估计在当前状态采取某动作的后续价值；本文从离线示范学习它。
- 一步生成：一次生成过程得到动作；不表示整个任务只执行一个动作。

## 证据

摘要报告，在多种 VLA 架构、仿真及真实操作中，DriftOPD 通常优于现有一步蒸馏基线，任务成功表现与多步教师策略相当。这里教师策略是比较对象，不等于训练需要教师。未给架构名称、任务数量、成功率、生成延迟和例外结果，因此只能判断它展示了可行性，不能量化速度与成功率的取舍。

## 局限

摘要未列出明确局限。我的主要待核查问题是离线 Q 函数如何评价示范之外的动作，以及误差是否会引导策略偏离可靠区域。真机实验支持所测任务的效果，但不证明任意离线数据都足以学准长期后果。

- **判断**：值得细读目标推导和 Q 函数训练；真正决定可信度的是未来价值估计，而不只是一步生成速度。

## 研究关联

可借鉴的是将计算成本与决策时间跨度分开：动作只生成一步，训练仍可以考虑后续收益。离线数据能覆盖关键决策、价值估计可信时，这条路径值得尝试。

### 下一步读哪里

核查序列级分解成立的条件、drifting 目标需要哪些样本，以及离线 Q 的训练目标和覆盖范围。重点看去掉未来势能项的消融、一步基线与多步策略的公平比较，以及真机任务上的例外。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/DriftOPD Sequence-Level Reverse-KL Distillation for One-Step VLA Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.00317v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models increasingly rely on action experts that generate short action chunks under receding-horizon control. While chunk-level training is convenient across robot embodiments, it optimizes local action likelihood without explicitly accounting for long-horizon task success. Sequence-level reinforcement learning can address this limitation, but typically requires policy rollouts and closed-loop interaction, which are costly for real-robot manipulation. We introduce DriftOPD, a teacher-free, rollout-free framework for sequence-level on-policy distillation of continuous VLA action experts. We show that the sequence-level reverse Kullback-Leibler (KL) divergence decomposes into a chunk-level reverse-KL term and a future-potential term that captures the long-horizon effect of the current action. DriftOPD optimizes these two terms using a one-step drifting objective and a Q-function critic learned from offline demonstrations, respectively, enabling sequence-level optimization with only offline data and one-step action generation. Across multiple VLA architectures in simulation and real-world manipulation, DriftOPD generally outperforms existing one-step distillation baselines while achieving task success performance comparable to multi-step teacher policies. These results demonstrate that long-horizon behavior can be effectively distilled into one-step VLA action experts without online interaction or a separate teacher.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.00317
- Authors: Youngjun Jun, Kyumin Choi, Youngmin Kim, Seonghyun Jin, Sunwoo Park, Jangho Park, Jong Chul Ye
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
