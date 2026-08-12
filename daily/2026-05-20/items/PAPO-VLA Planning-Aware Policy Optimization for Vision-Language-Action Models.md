---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19580v1"
published: "2026-05-19T09:22:49Z"
age_days: 0
score: 35
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> To address this issue, we propose Planning-Aware Policy Optimization for VLA models (PAPO-VLA).

## 关键点

- **问题**：However, making VLA policies reliable remains challenging, because a manipulation task is completed through closed-loop interaction, where each action affects subsequent execution.
- **创新点 / 方法**：To address this issue, we propose Planning-Aware Policy Optimization for VLA models (PAPO-VLA).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：However, making VLA policies reliable remains challenging, because a manipulation task is completed through closed-loop interaction, where each action affects subsequent execution.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models show promising ability in language-guided robotic
tasks. However, making VLA policies reliable remains challenging, because a manipulation
task is completed through closed-loop interaction, where each action affects subsequent
execution. To analyze this problem, we revisit VLA policy during execution and argue
that a VLA policy acts both as a planner, which makes task-oriented decisions that
change the direction of execution, and as an executor, which realizes these decisions
through dense continuous actions. This view suggests that improving VLA reliability
requires particular attention to planning actions. Existing optimization methods can
imitate actions or improve complete trajectories, but they usually do not explicitly
identify planning actions or measure their importance for task success. To address this
issue, we propose Planning-Aware Policy Optimization for VLA models (PAPO-VLA). PAPO-VLA
first identifies planning actions by jointly considering action variation and trajectory
outcome, then estimates their importance through causal sufficiency and causal
necessity, and finally incorporates this importance into GRPO advantage estimation. In
this way, more important planning actions receive stronger optimization emphasis, while
the whole trajectory is still optimized by trajectory-level feedback. Experiments on
multiple benchmarks demonstrate the effectiveness of PAPO-VLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19580v1
- Authors: Peizheng Guo, Jingyao Wang, Changwen Zheng, Wenwen Qiang
- Published: 2026-05-19T09:22:49Z
- Age days: 0

</details>
