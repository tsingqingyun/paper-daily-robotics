---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09337v1"
published: "2026-06-08T11:05:05Z"
age_days: 1
score: 34
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation

> [!summary] 一句话结论（基于摘要）
> Real-robot experiments on long-horizon contact-rich tasks, including latch manipulation, coffee-cup placement, and egg handling, show that TORL-VLA improves success rates at both subtask and full-task levels, as well as time-bounded execution efficiency over…

## 关键点

- **问题**：However, these models are typically deployed as offline policies.
- **创新点 / 方法**：Therefore, we propose TORL-VLA, a tactile-guided online reinforcement learning framework that couples tactile feedback with policy refinement for contact-rich manipulation.
- **证据**：Real-robot experiments on long-horizon contact-rich tasks, including latch manipulation, coffee-cup placement, and egg handling, show that TORL-VLA improves success rates at both subtask and full-task levels, as well as time-bounded execution efficiency over strong baselines.
- **局限**：When contact conditions shift from the training distribution, the policy cannot perform online adaptation, leading to problems such as inappropriate contact forces and inefficient retries.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have become a powerful framework for robotic
manipulation, and recent studies have introduced tactile or force feedback into VLAs to
address contact-rich tasks. However, these models are typically deployed as offline
policies. When contact conditions shift from the training distribution, the policy
cannot perform online adaptation, leading to problems such as inappropriate contact
forces and inefficient retries. Therefore, we propose TORL-VLA, a tactile-guided online
reinforcement learning framework that couples tactile feedback with policy refinement
for contact-rich manipulation. Our method introduces a tactile-derived wrench-aware VLA
to predict reference actions and future wrench sequences, while a lightweight online RL
module is used to refine the reference actions. To stabilize learning from mixed
exploratory policy-generated and human-intervention data, we introduce an intervention-
censored critic that prevents post-intervention success from being wrongly credited to
policy-generated actions preceding intervention. Real-robot experiments on long-horizon
contact-rich tasks, including latch manipulation, coffee-cup placement, and egg
handling, show that TORL-VLA improves success rates at both subtask and full-task
levels, as well as time-bounded execution efficiency over strong baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09337v1
- Authors: Huaihang Zheng, Yi Yang, Kai Ma, Shenglin Xu, Tian Xie, Guozheng Li, Xiangyu Wang, Yiren Ma, Si Liu, Yinian Mao, Baoxu Liu
- Published: 2026-06-08T11:05:05Z
- Age days: 1

</details>
