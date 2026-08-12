---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06147v1"
published: "2026-06-04T13:23:05Z"
age_days: 3
score: 38
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation

> [!summary] 一句话结论（基于摘要）
> Extensive evaluations on our benchmark demonstrate that WorldFly outperforms other baselines, particularly in unseen environments, validating the effectiveness of integrating world models into embodied aerial agents.

## 关键点

- **问题**：However, existing approaches typically rely on historical observations to directly predict actions, often struggling in dense urban environments where severe occlusions and sharp turns result in drastic viewpoint transitions.
- **创新点 / 方法**：To this end, we propose WorldFly, a novel world-model-based VLA framework that employs a dual-branch coupled flow matching mechanism to jointly generate future video predictions and navigation actions, thereby explicitly guiding the agent's policy via spatial imagination.
- **证据**：Extensive evaluations on our benchmark demonstrate that WorldFly outperforms other baselines, particularly in unseen environments, validating the effectiveness of integrating world models into embodied aerial agents.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end Vision-Language-Action (VLA) models have shown promise in UAV navigation.
However, existing approaches typically rely on historical observations to directly
predict actions, often struggling in dense urban environments where severe occlusions
and sharp turns result in drastic viewpoint transitions. We argue that the ability to
"imagine" future states -- inherent in World Models -- is critical for robust decision-
making under such partial observability. To address this, we construct a challenging
Urban Canyon Traversal Benchmark, specifically designed to evaluate spatial
understanding in scenarios characterized by severe occlusions and drastic viewpoint
transitions. To this end, we propose WorldFly, a novel world-model-based VLA framework
that employs a dual-branch coupled flow matching mechanism to jointly generate future
video predictions and navigation actions, thereby explicitly guiding the agent's policy
via spatial imagination. Extensive evaluations on our benchmark demonstrate that
WorldFly outperforms other baselines, particularly in unseen environments, validating
the effectiveness of integrating world models into embodied aerial agents.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06147v1
- Authors: Shengtao Zheng, Kai Li, Weichen Zhang, Yu Meng, Chen Gao, Xinlei Chen, Yong Li, Xiao-Ping Zhang
- Published: 2026-06-04T13:23:05Z
- Age days: 3

</details>
