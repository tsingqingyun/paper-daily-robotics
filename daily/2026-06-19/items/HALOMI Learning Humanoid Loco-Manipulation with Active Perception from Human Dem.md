---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18772v1"
published: "2026-06-17T07:33:37Z"
age_days: 1
score: 28
created: 2026-06-19
concepts: ["机器人学习", "具身智能评测与基准"]
---

# HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations

> [!summary] 一句话结论（基于摘要）
> Across the three quantitatively evaluated tasks, HALOMI achieves an average success rate of 85\%, while additional qualitative demonstrations show its ability to support dynamic tossing and deep-squat grasping.

## 关键点

- **问题**：However, directly transferring human demonstrations to humanoids requires a precise world-frame tracking controller, which is often brittle under Out-of-Distribution(OOD) targets, while human-to-humanoid gaps persist in both egocentric observation and action execution.
- **创新点 / 方法**：To address these challenges, we present HALOMI, a scalable framework for learning humanoid loco-manipulation with active perception from human demonstrations.
- **证据**：Across the three quantitatively evaluated tasks, HALOMI achieves an average success rate of 85\%, while additional qualitative demonstrations show its ability to support dynamic tossing and deep-squat grasping.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human demonstrations, which can be collected at scale and naturally capture active hand-
eye coordination, are a promising data source for learning humanoid loco-manipulation.
However, directly transferring human demonstrations to humanoids requires a precise
world-frame tracking controller, which is often brittle under Out-of-Distribution(OOD)
targets, while human-to-humanoid gaps persist in both egocentric observation and action
execution. To address these challenges, we present HALOMI, a scalable framework for
learning humanoid loco-manipulation with active perception from human demonstrations.
HALOMI extends Universal Manipulation Interface (UMI) with egocentric sensing to collect
ego-view and wrist-view observations along with head-hand trajectories at scale. We
further propose a manifold-constrained controller that plans in a learned latent
behavior manifold to enable precise and robust head-hand tracking in the world frame. To
bridge the human-to-humanoid gap, we perform ego-view alignment and introduce a
controller-aware reference trajectory adaptation to reduce mismatch in both observation
and action execution. We validate HALOMI on a Unitree G1 humanoid robot with an actuated
neck across five real-world tasks involving navigation, grasping, bimanual manipulation,
whole-body coordination, and dynamic behaviors. Across the three quantitatively
evaluated tasks, HALOMI achieves an average success rate of 85\%, while additional
qualitative demonstrations show its ability to support dynamic tossing and deep-squat
grasping.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18772v1
- Authors: Zehui Zhao, Yuxuan Zhao, Gaojing Zhang, Chenxi Liu, Maolin Zheng, Wenzhao Lian
- Published: 2026-06-17T07:33:37Z
- Age days: 1

</details>
