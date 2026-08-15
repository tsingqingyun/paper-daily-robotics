---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13026v1"
published: "2026-08-13T09:54:14Z"
age_days: 1
score: 30
created: 2026-08-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> On RoboTwin 2.0, Temporal GRPO improves task success and sample efficiency, with consistent gains across task horizons.

## 关键点

- **问题**：A rollout that completes several valid stages but fails later can therefore penalize the actions that produced its earlier progress.
- **创新点 / 方法**：Outcome-driven reinforcement learning offers a scalable way to post-train vision-language-action (VLA) policies from sparse task-success feedback.
- **证据**：On RoboTwin 2.0, Temporal GRPO improves task success and sample efficiency, with consistent gains across task horizons.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/Temporal GRPO Beyond Trajectory-Level Credit in Vision-Language-Action Reinforce.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Outcome-driven reinforcement learning offers a scalable way to post-train vision-language-action (VLA) policies from sparse task-success feedback. In common GRPO-based VLA post-training, one rollout-level advantage is applied to every action in the trajectory. A rollout that completes several valid stages but fails later can therefore penalize the actions that produced its earlier progress. We call this trajectory-level credit aliasing. Temporal GRPO addresses this problem by constructing detectable task stages, aligning each rollout with stage-specific action intervals, and comparing only rollouts that have entered the same stage. The resulting stage advantages are applied to their corresponding intervals in a single policy update. On RoboTwin 2.0, Temporal GRPO improves task success and sample efficiency, with consistent gains across task horizons. Controlled updates on LIBERO-Long preserve shared prerequisite stages and concentrate improvement at the first stage where rollout outcomes diverge.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13026v1
- Authors: Yao Zhou, Hang Gao, Fengge Wu, Changwen Zheng, Wenwen Qiang
- Published: 2026-08-13T09:54:14Z
- Age days: 1

</details>
