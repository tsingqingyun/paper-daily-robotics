---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17385v1"
published: "2026-06-16T00:44:16Z"
age_days: 1
score: 37
created: 2026-06-18
concepts: ["智能体 Agent", "机器人学习"]
---

# EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning

> [!summary] 一句话结论（基于摘要）
> Instead of proposing a static dataset, we introduce EgoInfinity, a universal 4D hand-object interaction data engine that enables web-scale data generation for robot retargeting and learning.

## 关键点

- **问题**：Internet videos constitute the largest reservoir of embodied human manipulation knowledge, yet converting arbitrary RGB footage into actionable robot training data remains a major bottleneck.
- **创新点 / 方法**：Instead of proposing a static dataset, we introduce EgoInfinity, a universal 4D hand-object interaction data engine that enables web-scale data generation for robot retargeting and learning.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Internet videos constitute the largest reservoir of embodied human manipulation
knowledge, yet converting arbitrary RGB footage into actionable robot training data
remains a major bottleneck. Existing lab- or factory-collected datasets are narrow in
scale and diversity, limiting open-world robot learning. Instead of proposing a static
dataset, we introduce EgoInfinity, a universal 4D hand-object interaction data engine
that enables web-scale data generation for robot retargeting and learning. EgoInfinity
is a modular engine integrating perception, segmentation, reconstruction, interaction-
aware refinement, and retargeting to automate this traditionally unscalable video-to-
action problem without human-in-the-loop annotation. Its modular design lets the engine
continuously benefit from advances in any incorporated component. With EgoInfinity, in-
the-wild human manipulation videos are lifted into agent-agnostic, metric 4D hand-object
representations, including hand trajectories, 6-DoF object poses, and contact-relevant
states. Rather than naively connecting standalone components, EgoInfinity combines
cross-module metric calibration with interaction-aware refinement to improve physical
reliability, reducing drift and contact inconsistencies common in pure visual
reconstruction. We further propose a novel motion retargeter that compiles the recovered
3D hand motions into executable joint trajectories for diverse robot morphologies,
enabling video-to-action retargeting on any robot from arbitrary viewpoints and shot
sizes (e.g., the human body is only partially visible). We validate EgoInfinity across
perception fidelity, kinematic feasibility, contact consistency, cross-embodiment
generalization, and real-robot skill acquisition (e.g., grasping, cutting, wiping, and
pouring), demonstrating a scalable bridge from internet videos to executable robot
behavior for open-world robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17385v1
- Authors: Gaotian Wang, Kejia Ren, Andrew Morgan, Yiting Chen, Howard H. Qian, Podshara Chanrungmaneekul, Kaiyu Hang
- Published: 2026-06-16T00:44:16Z
- Age days: 1

</details>
