---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19293v1"
published: "2026-05-19T03:13:09Z"
age_days: 0
score: 29
created: 2026-05-20
concepts: ["机器人学习", "Sim2Real"]
---

# Domain-Adaptive Communication-Rate Optimization for Sim-to-Real Humanoid-Robot Wireless XR Teleoperation

> [!summary] 一句话结论（基于摘要）
> This paper develops a system framework that integrates sampling, transmission, interpolation, and reconstruction and formulates a communication-rate optimization that aims to minimize the communication energy while maintaining the reconstruction accuracy of r…

## 关键点

- **问题**：Since acquiring real-time feedback from physical robots is limited by hardware costs, it is necessary to solve the problem through simulator interaction with offline real-domain data correction.
- **创新点 / 方法**：Building on this analysis, we propose a proximal policy optimization (PPO) method with density-ratio weighting and trust-region regularization.
- **证据**：This paper develops a system framework that integrates sampling, transmission, interpolation, and reconstruction and formulates a communication-rate optimization that aims to minimize the communication energy while maintaining the reconstruction accuracy of robot motion trajectories through dimension-wise sampling-rat…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[Sim2Real]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Wireless extended reality (XR) teleoperation provides embodied interaction capability
for collecting humanoid robot demonstrations, but the large-scale adoption is restricted
by the overhead of high-frequency motion transmission. This paper develops a system
framework that integrates sampling, transmission, interpolation, and reconstruction and
formulates a communication-rate optimization that aims to minimize the communication
energy while maintaining the reconstruction accuracy of robot motion trajectories
through dimension-wise sampling-rate control. Since acquiring real-time feedback from
physical robots is limited by hardware costs, it is necessary to solve the problem
through simulator interaction with offline real-domain data correction. To guide sim-to-
real adaptation, we provide a PAC-Bayes generalization characterization that reveals the
effects of latent density-ratio estimation, finite-sample deviation, and encoder bias.
Building on this analysis, we propose a proximal policy optimization (PPO) method with
density-ratio weighting and trust-region regularization. Experiments on public humanoid
teleoperation dataset show that the proposed method improves the tradeoff between
reconstruction error and communication energy consumption under sim-to-real distribution
shift. We further analyze the effectiveness of the proposed algorithm across various
wireless channels and dynamic motion trajectories.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19293v1
- Authors: Caolu Xu, Zhiyong Chen, Meixia Tao, Li Song, Feng Yang, Wenjun Zhang
- Published: 2026-05-19T03:13:09Z
- Age days: 0

</details>
