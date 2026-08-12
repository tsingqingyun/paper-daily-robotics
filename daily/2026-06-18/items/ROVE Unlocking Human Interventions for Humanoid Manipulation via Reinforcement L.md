---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17011v1"
published: "2026-06-15T17:45:06Z"
age_days: 2
score: 41
created: 2026-06-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> On challenging real-world contact-rich and fine- grained humanoid manipulation tasks, ROVE outperforms experience-learning baselines and consistently improves across multiple rollout-intervention iterations.

## 关键点

- **问题**：However, enabling seamless humanoid interventions is a formidable systems challenge due to complex whole-body kinematics and dexterous-hand control.
- **创新点 / 方法**：To address both the system and algorithmic challenges, we propose ROVE, a reinforcement learning framework for humanoid VLA post- training with imperfect human interventions.
- **证据**：On challenging real-world contact-rich and fine- grained humanoid manipulation tasks, ROVE outperforms experience-learning baselines and consistently improves across multiple rollout-intervention iterations.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-18/ROVE Unlocking Human Interventions for Humanoid Manipulation via Reinforcement L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human interventions provide crucial corrective signals for post-training Vision-
Language-Action (VLA) models. However, enabling seamless humanoid interventions is a
formidable systems challenge due to complex whole-body kinematics and dexterous-hand
control. Consequently, the collected intervention trajectories are often suboptimal, and
methods that rely on human interventions as expert supervision can absorb hesitant,
inefficient, or even erroneous behaviors. To address both the system and algorithmic
challenges, we propose ROVE, a reinforcement learning framework for humanoid VLA post-
training with imperfect human interventions. First, ROVE introduces a human-in-the-loop
pipeline capable of collecting deployment and intervention data for humanoid
manipulation. Second, it utilizes Optimistic Value Estimation (OVE) to prioritize high-
value behaviors from mixed-quality trajectories. To further robustify value estimation,
we incorporate cross-embodiment human experience videos to provide rich supervision for
long-tailed failure and recovery modes. The resulting critic yields informative
advantage signals, steering the VLA actor to focus on high-value behaviors rather than
indiscriminately imitating all actions. On challenging real-world contact-rich and fine-
grained humanoid manipulation tasks, ROVE outperforms experience-learning baselines and
consistently improves across multiple rollout-intervention iterations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17011v1
- Authors: Wei Xiao, Weiliang Tang, Yuying Ge, Hui Zhou, Yao Mu, Li Zhang, Yixiao Ge
- Published: 2026-06-15T17:45:06Z
- Age days: 2

</details>
