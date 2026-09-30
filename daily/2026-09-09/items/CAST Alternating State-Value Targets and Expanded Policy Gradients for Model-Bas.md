---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08853v1"
published: "2026-09-08T15:05:16Z"
age_days: 0
score: 27
created: 2026-09-09
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# CAST: Alternating State-Value Targets and Expanded Policy Gradients for Model-Based Reinforcement Learning

> [!summary] 先说人话（基于摘要）
> CAST让模型强化学习的价值函数同时吸收规划器的较强行为和当前策略的行为。它用真实规划转移与模型想象转移构造交替目标，缓解价值学习只盯着较弱策略的问题。

## 这篇到底在做什么

- **卡在哪里**：在线规划可选出比学习策略更好的动作，但已有组合方法通常仍估计策略自身的价值，难以充分利用规划引导行为。
- **关键解法**：以状态价值critic替代动作价值critic，训练目标结合一段真实的规划引导转移和一段当前策略的想象转移，使价值对应规划器与策略交替作用的过程，并由当前策略起正则作用。
- **拿什么证明**：摘要报告在DeepMind Control和HumanoidBench上与多种先进方法比较，并成功迁移到实体Unitree Go2完成动态倒立；摘要未给出可核查的结果数字或明确的基准胜幅。

## 值不值得读

- **和你的研究有什么关系**：对世界模型与机器人强化学习研究者，这是关于规划行为如何进入价值学习的具体修改，适合已有在线规划系统进一步检验。
- **先别急着信**：需核查交替目标的理论含义及对模型误差的敏感性；标题中的扩展策略梯度在摘要中没有得到具体说明。
- **判断**：模型强化学习方向值得精读公式与消融，实体倒立结果本身不能替代基准收益归因。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/CAST Alternating State-Value Targets and Expanded Policy Gradients for Model-Bas.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Model-based reinforcement learning (MBRL) is a family of RL methods that learn a model of the environment and use it for action selection, making it well suited to robotics due to its sample efficiency. Combining learned models with online planning can further improve action selection, as the planner can exploit the model to find better actions than the learned policy alone. Recent methods combining learned policies with online planning typically learn the value of the policy rather than the stronger planner-guided behavior. We present CAST (Critic with Alternating State-value Target), which uses planner-guided behavior to improve value learning while regularizing the value estimate with the current policy. CAST replaces the action-value critic with a state-value critic, trained using a target that combines a real planner-guided transition and an imagined transition under the current policy. The resulting value function corresponds to an alternating process between planner-guided behavior and the current policy, allowing it to benefit from the stronger planner behavior while being regularised by the policy being learned. We evaluate CAST on the DeepMind Control and HumanoidBench Suites against several state-of-the-art methods, and demonstrate successful transfer to a physical Unitree Go2 quadruped performing a dynamic handstand.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08853v1
- Authors: Pietro Noah Crestaz, Mohamed Yassine Kabouri, Nicolas Mansard, Andrea Del Prete
- Published: 2026-09-08T15:05:16Z
- Age days: 0

</details>
