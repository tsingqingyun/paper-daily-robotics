---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.12931v1"
published: "2026-07-14T16:04:41Z"
age_days: 2
score: 40
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning

> [!summary] 一句话结论（基于摘要）
> Extensive experiments across simulated and real-world robotic manipulation tasks demonstrate that ExToken consistently accelerates convergence, improves task performance, and exhibits strong robustness under highly constrained interaction budgets.

## 关键点

- **问题**：However, its practical scalability remains severely limited by the substantial cost of environmental interactions.
- **创新点 / 方法**：Motivated by these insights, we introduce RL Exploration Token (ExToken), a simple yet general framework that condition VLA policies on discrete behavioral priors derived from offline demonstrations for structured exploration.
- **证据**：Extensive experiments across simulated and real-world robotic manipulation tasks demonstrate that ExToken consistently accelerates convergence, improves task performance, and exhibits strong robustness under highly constrained interaction budgets.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/ExToken Structured Exploration for Efficient Vision-Language-Action Reinforcemen.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-
Language-Action (VLA) models on complex manipulation tasks. However, its practical
scalability remains severely limited by the substantial cost of environmental
interactions. In this work, we first investigate the exploration stagnation bottleneck
in current VLA-RL frameworks and reveal that trajectory diversity is fundamentally more
important to sample efficiency than the sheer quantity of collected rollouts. Motivated
by these insights, we introduce RL Exploration Token (ExToken), a simple yet general
framework that condition VLA policies on discrete behavioral priors derived from offline
demonstrations for structured exploration. By conditioning the policy on different
tokens during rollout collection, ExToken encourages the agent to explore diverse
behavioral modes, substantially improving state-action coverage and exploration
efficiency. To bridge exploration during training with deterministic inference at
deployment, ExToken further incorporates a state-conditioned token selector that
adaptively predicts effective behavioral modes for unseen scenarios. Extensive
experiments across simulated and real-world robotic manipulation tasks demonstrate that
ExToken consistently accelerates convergence, improves task performance, and exhibits
strong robustness under highly constrained interaction budgets.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.12931v1
- Authors: Yilun Kong, Yunpeng Qing, Guozheng Ma, Haoyu Wang, Li Shen, Zhi Hou, Dacheng Tao
- Published: 2026-07-14T16:04:41Z
- Age days: 2

</details>
