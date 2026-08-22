---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19443v1"
published: "2026-08-19T20:56:18Z"
age_days: 2
score: 28
created: 2026-08-22
concepts: ["AI 核心知识地图"]
---

# Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control

> [!summary] 一句话结论（基于摘要）
> Our theoretical analysis shows that our hybrid sampling approach achieves faster convergence than standard MPPI and better optimality than standard feedback sampling.

## 关键点

- **问题**：However, for high-dimensional and open-loop unstable dynamical systems, the required number of samples to improve the control sequence will grow exponentially with the horizon, leading to poor sample efficiency and numerical instability.
- **创新点 / 方法**：Finally, we validate our method on humanoid robot locomotion and manipulation tasks in the real world.
- **证据**：Our theoretical analysis shows that our hybrid sampling approach achieves faster convergence than standard MPPI and better optimality than standard feedback sampling.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Thanks to its parallelizability and flexibility, sampling-based Model Predictive Control (MPC) has become widely popular for controlling real-world robotic systems. However, for high-dimensional and open-loop unstable dynamical systems, the required number of samples to improve the control sequence will grow exponentially with the horizon, leading to poor sample efficiency and numerical instability. This paper investigates the instability of shooting methods in sampling-based MPC and shows that the optimal sampling proposal distribution can be realized by sampling with an optimized feedback policy. We refer to this algorithm as Feedback Sampling MPC (FS-MPC). FS-MPC involves a hybrid sampling design which balances local and global search based on the system stability and the available computation budget. Our theoretical analysis shows that our hybrid sampling approach achieves faster convergence than standard MPPI and better optimality than standard feedback sampling. Empirically, in diverse contact-rich control tasks like humanoid loco-manipulation and dexterous manipulation, we show that FS-MPC successfully tackles dynamically unstable tasks where standard sample-based approaches struggle, and strictly outperforms feedback policies alone. Finally, we validate our method on humanoid robot locomotion and manipulation tasks in the real world.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19443v1
- Authors: Chaoyi Pan, Zeji Yi, John Zhang, Zachary Manchester, Guannan Qu, Guanya Shi
- Published: 2026-08-19T20:56:18Z
- Age days: 2

</details>
