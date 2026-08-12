---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13172v1"
published: "2026-07-14T18:22:14Z"
age_days: 2
score: 31
created: 2026-07-17
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models

> [!summary] 一句话结论（基于摘要）
> In the context of training within a learned simulator, we show that the use of preferences rather than other types of feedback substantially improves the performance during deployment.

## 关键点

- **问题**：We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available.
- **创新点 / 方法**：We introduce DROPJ, a human-centred method for both safe training and deployment.
- **证据**：In the context of training within a learned simulator, we show that the use of preferences rather than other types of feedback substantially improves the performance during deployment.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We address the problem of safely training an agent policy and deploying a good and safe
policy, in settings where the environment dynamics are unknown and no suitable reward
function is available. In the context of safety-critical environments, we consider
traditional reinforcement learning impractical and resort to the resource of human
input. We introduce DROPJ, a human-centred method for both safe training and deployment.
We first learn a world model (a learned simulator) from a dataset of prior real-world
trajectories. A human then plays the game in this learned simulator to extract several
informative simulated trajectories. From these, we sample pairs of simulated trajectory
segments and elicit from a human their preference over these segments, as well as a
reason (justification) for their choice. We then train a reward model from these
justified preferences and use it, together with the world model, to directly deploy the
agent using model predictive control. Running real-user experiments, we find that
generating informative simulated trajectories from a user significantly reduces the
computational cost during training compared to other strategies, and can also improve
the performance during deployment. In the context of training within a learned
simulator, we show that the use of preferences rather than other types of feedback
substantially improves the performance during deployment. We further demonstrate that
safety justifications accompanying preferences can significantly enhance safety or
prioritise user-prescribed aspects of safety associated with them during deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13172v1
- Authors: Ilias Kazantzidis, Timothy J. Norman, Yali Du, Christopher T. Freeman
- Published: 2026-07-14T18:22:14Z
- Age days: 2

</details>
