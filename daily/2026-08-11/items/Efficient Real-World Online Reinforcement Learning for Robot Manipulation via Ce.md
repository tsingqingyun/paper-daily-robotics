---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09762v1"
published: "2026-08-10T15:54:25Z"
age_days: 0
score: 33
created: 2026-08-11
concepts: ["智能体 Agent", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition

> [!summary] 一句话结论（基于摘要）
> Compared with a state-of-the-art baseline, our method improves the success rate from 60% to 80% on tennis ball pick-and-place, from 60% to 90% on banana pick-and-place, and from 25% to 95% on simulated block relocation, while also successfully accomplishing a…

## 关键点

- **问题**：Recent methods have demonstrated sample-efficient learning through human intervention but remain limited to small randomization ranges and encounter challenges with the non- stationarity induced by concurrently training multiple agents.
- **创新点 / 方法**：To address these limitations, we introduce a unified framework that combines centralized training with decentralized execution (CTDE) and a Hybrid Reward Architecture (HRA).
- **证据**：Compared with a state-of-the-art baseline, our method improves the success rate from 60% to 80% on tennis ball pick-and-place, from 60% to 90% on banana pick-and-place, and from 25% to 95% on simulated block relocation, while also successfully accomplishing a task where the baseline consistently fails.
- **局限**：Recent methods have demonstrated sample-efficient learning through human intervention but remain limited to small randomization ranges and encounter challenges with the non- stationarity induced by concurrently training multiple agents.

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world online reinforcement learning (RL) provides a promising approach for training
robotic manipulation policies directly in the physical world, avoiding the sim-to-real
gap and enabling continuous policy refinement through human-in-the-loop interaction.
Recent methods have demonstrated sample-efficient learning through human intervention
but remain limited to small randomization ranges and encounter challenges with the non-
stationarity induced by concurrently training multiple agents. To address these
limitations, we introduce a unified framework that combines centralized training with
decentralized execution (CTDE) and a Hybrid Reward Architecture (HRA). This enables
multiple actors to share a centralized multi-head critic. The critic is decomposed into
task and grasp heads, corresponding to the sparse task reward and a potential-based
grasping reward, respectively. We accordingly reformulate the critic and actor
objectives to exploit the decomposed Q-values while explicitly accounting for the
categorical action distribution of the discrete gripper policy. Experimental results
demonstrate that the proposed framework substantially improves both sample efficiency
and policy performance. We validate our approach on two robotic arms and a simulated
humanoid robot across tennis ball and banana pick-and-place, pot reset, and simulated
block relocation tasks under dimension-wise domain randomization, approximately 5-25x
larger than those considered in prior work. Compared with a state-of-the-art baseline,
our method improves the success rate from 60% to 80% on tennis ball pick-and-place, from
60% to 90% on banana pick-and-place, and from 25% to 95% on simulated block relocation,
while also successfully accomplishing a task where the baseline consistently fails.
Videos and more details are available at our project website: https://hil-
harc.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09762v1
- Authors: Changhao Li, Yifang Zhang, Heng Zhang, Davide Torielli, Damiano Gasperini, Arturo Laurenzi, Luca Muratore, Arash Ajoudani, Nikos Tsagarakis
- Published: 2026-08-10T15:54:25Z
- Age days: 0

</details>
