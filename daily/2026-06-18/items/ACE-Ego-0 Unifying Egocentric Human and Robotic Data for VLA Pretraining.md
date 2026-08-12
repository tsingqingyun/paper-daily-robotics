---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17200v1"
published: "2026-06-15T18:40:18Z"
age_days: 2
score: 39
created: 2026-06-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining

> [!summary] 一句话结论（基于摘要）
> ACE-EGO-0 achieves state-of-the- art performance on RoboCasa GR1 TableTop and RoboTwin 2.0, while demonstrating strong transfer to real-world bimanual manipulation.

## 关键点

- **问题**：However, joint training on human and robot data remains challenging due to divergences in action spaces, embodiment structures, temporal dynamics, and supervision quality.
- **创新点 / 方法**：We introduce ACE-EGO-0, a unified VLA pretraining framework jointly leveraging heterogeneous data sources.
- **证据**：ACE-EGO-0 achieves state-of-the- art performance on RoboCasa GR1 TableTop and RoboTwin 2.0, while demonstrating strong transfer to real-world bimanual manipulation.
- **局限**：However, joint training on human and robot data remains challenging due to divergences in action spaces, embodiment structures, temporal dynamics, and supervision quality.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models benefit from large-scale and diverse embodied data,
yet scaling robot trajectory collection is costly and labor-intensive. Recent advances
show that large-scale egocentric human videos provide complementary real-world
supervision in pretraining. However, joint training on human and robot data remains
challenging due to divergences in action spaces, embodiment structures, temporal
dynamics, and supervision quality. We introduce ACE-EGO-0, a unified VLA pretraining
framework jointly leveraging heterogeneous data sources. To extract large-scale
pretraining supervision from egocentric human videos, we build a scalable egocentric
video-to-action pipeline that converts raw human videos into robot-format pseudo-action
trajectories. To make these labels comparable with robot demonstrations, ACE-EGO-0 uses
a unified action representation based on camera-space actions, morphology conditioning,
and time-aligned action chunking. To robustly leverage noisy pseudo-action supervision
from egocentric human videos, we formulate a reliability-aware training objective with a
human auxiliary loss that concentrates supervision on reliable signals. We instantiate
ACE-EGO-0 on 4.53K hours of robot and simulation data, together with 1.48K hours of
pseudo-action-labeled egocentric human data. Experiments show that incorporating large-
scale human supervision under reliability-aware weighting consistently improves both
unified joint pretraining and supervised fine-tuning. ACE-EGO-0 achieves state-of-the-
art performance on RoboCasa GR1 TableTop and RoboTwin 2.0, while demonstrating strong
transfer to real-world bimanual manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17200v1
- Authors: Hao Li, Ganlong Zhao, Yufei Liu, Haotian Hou, Guoquan Ye, Tongyan Fang, Chunxiao Liu, Siyuan Huang, Jianbo Liu, Xiaogang Wang, Hongsheng Li
- Published: 2026-06-15T18:40:18Z
- Age days: 2

</details>
