---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21302v1"
published: "2026-07-23T13:26:57Z"
age_days: 0
score: 30
created: 2026-07-24
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Expert Behavior Prior Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Extensive experiments conducted on robotic control (Gym, PyBullet) and industrial control (DMControl) benchmarks demonstrate that EBP significantly outperforms state-of-the-art online RL algorithms, achieving higher sample efficiency and more stable convergen…

## 关键点

- **问题**：However, most existing BPRL methods rely on static offline datasets, which often suffer from low data diversity and suboptimal trajectory quality.
- **创新点 / 方法**：Specifically, we introduce a Q-guided conditional variational autoencoder (Q-CVAE) that learns to generate expert policy priors directly from the online replay buffer.
- **证据**：Extensive experiments conducted on robotic control (Gym, PyBullet) and industrial control (DMControl) benchmarks demonstrate that EBP significantly outperforms state-of-the-art online RL algorithms, achieving higher sample efficiency and more stable convergence.
- **局限**：To address these limitations, we deviate from existing offline pre-training methods and propose an Expert Behavior Prior (EBP) algorithm.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Behavior prior reinforcement learning (BPRL) has emerged as a promising paradigm to
improve sample efficiency in online reinforcement learning (RL) by leveraging policy
priors derived from offline demonstrations. However, most existing BPRL methods rely on
static offline datasets, which often suffer from low data diversity and suboptimal
trajectory quality. This reliance restricts the effectiveness of policy priors,
hindering both policy exploitation and stability during online training. Consequently,
agents are prone to inefficient exploration and unstable learning dynamics. To address
these limitations, we deviate from existing offline pre-training methods and propose an
Expert Behavior Prior (EBP) algorithm. Specifically, we introduce a Q-guided conditional
variational autoencoder (Q-CVAE) that learns to generate expert policy priors directly
from the online replay buffer. This enables the generation of high-value actions for
guiding policy updates without relying on pre-collected expert trajectories. To further
enhance policy exploitation, we propose an expert policy guidance (EPG) mechanism that
selects expert actions from a generative support set, and we integrate a policy gradient
correction (PGC) module to harmonize Q-guidance with expert supervision, promoting
stable and consistent policy improvement. Extensive experiments conducted on robotic
control (Gym, PyBullet) and industrial control (DMControl) benchmarks demonstrate that
EBP significantly outperforms state-of-the-art online RL algorithms, achieving higher
sample efficiency and more stable convergence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21302v1
- Authors: Gong Gao, Weidong Zhao, Xianhui Liu, Ning Jia
- Published: 2026-07-23T13:26:57Z
- Age days: 0

</details>
