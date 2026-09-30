---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03906v1"
published: "2026-09-03T14:24:29Z"
age_days: 3
score: 25
created: 2026-09-07
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Revisiting Topological Graphs for Macro Action based Closed-loop Reinforcement Learning of Vision Language Navigation in Continuous Environment

> [!summary] 先说人话（基于摘要）
> 论文把连续环境VLN改写为分层MDP：高层策略在拓扑图的前沿节点间选宏动作，免训练低层控制器负责执行，再用action-aware value head驱动图上的PPO。

## 问题

VLN-CE需要在未见环境中闭环遵循指令；行为克隆有分布偏移，偏航后DAgger专家动作可能不唯一，而直接在微动作空间做RL又因奖励稀疏、决策链过长而样本低效。

## 创新点或方法

输入是语言指令与环境观测，高层输出拓扑前沿节点；低层控制器把节点选择变成连续运动。动态图上的动作感知价值头估计状态价值，使PPO能处理随探索变化的候选前沿集合。

## 证据

摘要称广泛实验验证架构有效，并在R2R-CE和RxR-CE达到先进水平；未给SPL、成功率、样本效率或相对提升数字。


## 局限

需核查拓扑图构建和免训练控制器是否使用额外先验，以及最终收益来自宏动作、价值头还是其他训练细节。

- **判断**：VLN-CE研究者值得精读MDP定义和训练细节；缺乏摘要数字，SOTA声明需看完整表格再判断。

## 研究关联

它为具身导航智能体提供一个实用的闭环RL抽象：用拓扑宏动作压缩规划时域，同时保留连续环境执行。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Revisiting Topological Graphs for Macro Action based Closed-loop Reinforcement L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language Navigation in Continuous Environments (VLN-CE) requires an agent to follow natural language instructions through unseen environments. Existing imitation learning (IL) pipelines struggle in this closed-loop setting: behavior cloning suffers from distribution shift, and DAgger's expert actions become ambiguous upon trajectory deviation. While Reinforcement Learning (RL) offers a natural paradigm to address this, directly applying RL to micro action spaces is sample-inefficient due to reward sparsity. To overcome this bottleneck, we reformulate VLN-CE as a Hierarchical Markov Decision Process (MDP), explicitly decoupling high-level planning from low-level control. By abstracting the environment into a topological graph, our high-level policy operates on a macro action space of frontier nodes, with a training-free low-level controller acting as its state transition, which significantly compresses the decision horizon and makes closed-loop RL tractable. To support RL optimization on the macro MDP, we propose an action-aware value head to effectively evaluate state values under the dynamic frontier action space, powering a graph-based PPO. Extensive experiments demonstrate the effectiveness of our architecture. Finally, our model achieves state-of-the-art performance on the R2R-CE and RxR-CE benchmarks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03906v1
- Authors: Shuhao Ye, Sitong Mao, Yuxiang Cui, Yufei Wei, Xuan Yu, Shichao Zhai, Wen Chen, Shunbo Zhou, Rong Xiong, Yue Wang
- Published: 2026-09-03T14:24:29Z
- Age days: 3

</details>
