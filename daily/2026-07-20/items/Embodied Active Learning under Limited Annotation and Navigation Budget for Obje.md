---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15974v1"
published: "2026-07-17T14:07:46Z"
age_days: 2
score: 30
created: 2026-07-20
concepts: ["智能体 Agent", "世界模型"]
---

# Embodied Active Learning under Limited Annotation and Navigation Budget for Object Detection

> [!summary] 一句话结论（基于摘要）
> Through comparison against several baselines, our experimental results show that spatial inconsistency helps guide the agent and select relevant images without external supervision, achieving the highest detection accuracy at the end of the adaptation process…

## 关键点

- **问题**：Formally, the approach is an embodied variant of batch active learning, where at each round an agent has a limited navigation budget to collect candidate samples and a limited annotation budget for the most relevant images.
- **创新点 / 方法**：Our approach selects informative robot trajectories and image samples to retrain the detector, explicitly targeting its failure cases.
- **证据**：Through comparison against several baselines, our experimental results show that spatial inconsistency helps guide the agent and select relevant images without external supervision, achieving the highest detection accuracy at the end of the adaptation process under the same budget.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This paper studies how to adapt a computer vision object detector to an unknown
environment under both a robot navigation time and annotation budget constraint. Our
approach selects informative robot trajectories and image samples to retrain the
detector, explicitly targeting its failure cases. Formally, the approach is an embodied
variant of batch active learning, where at each round an agent has a limited navigation
budget to collect candidate samples and a limited annotation budget for the most
relevant images. We leverage spatial consistency to identify images with inconsistent
labels, which are likely to provide the greatest improvement to the vision model. We
evaluate the approach using different active learning objectives on large scenes from
the AI2-THOR simulator and on a real-world setup using a Boston Dynamics Spot robot with
the real-time object detector YOLOv5. Through comparison against several baselines, our
experimental results show that spatial inconsistency helps guide the agent and select
relevant images without external supervision, achieving the highest detection accuracy
at the end of the adaptation process under the same budget. The open-source project can
be found at https://mkabouri.github.io/embodied-active-learning-od

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15974v1
- Authors: Hadrien Crassous, Mohamed Yassine Kabouri, Minahil Raza, Joni Pajarinen, Riad Akrour
- Published: 2026-07-17T14:07:46Z
- Age days: 2

</details>
