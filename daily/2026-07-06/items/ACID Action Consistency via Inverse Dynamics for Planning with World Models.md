---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02403v1"
published: "2026-07-02T16:38:10Z"
age_days: 3
score: 26
created: 2026-07-06
concepts: ["智能体 Agent", "世界模型"]
---

# ACID: Action Consistency via Inverse Dynamics for Planning with World Models

> [!summary] 一句话结论（基于摘要）
> Across four action-conditioned world models and six tasks spanning rigid and deformable manipulation, articulated control, and visual navigation, ACID consistently improves planning and matches the baseline's accuracy with substantially less planning compute.

## 关键点

- **问题**：However, the standard planning cost judges a candidate solely by how close its predicted terminal state lies to the goal, leaving the realizability of the intermediate transitions unchecked -- a predicted trajectory can look convincing while the environment rollout drifts away from it.
- **创新点 / 方法**：In this paper, we propose ACID, a decision-time planning framework that introduces cycle action consistency: the action inferred backward from a predicted transition by an inverse dynamics model should recover the one that was conditioned on.
- **证据**：Across four action-conditioned world models and six tasks spanning rigid and deformable manipulation, articulated control, and visual navigation, ACID consistently improves planning and matches the baseline's accuracy with substantially less planning compute.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Decision-time planning with action-conditioned world models has become a popular
paradigm for embodied control. However, the standard planning cost judges a candidate
solely by how close its predicted terminal state lies to the goal, leaving the
realizability of the intermediate transitions unchecked -- a predicted trajectory can
look convincing while the environment rollout drifts away from it. In this paper, we
propose ACID, a decision-time planning framework that introduces cycle action
consistency: the action inferred backward from a predicted transition by an inverse
dynamics model should recover the one that was conditioned on. We fold this per-step
residual into the planning cost via a scale-invariant adaptive weight. Across four
action-conditioned world models and six tasks spanning rigid and deformable
manipulation, articulated control, and visual navigation, ACID consistently improves
planning and matches the baseline's accuracy with substantially less planning compute.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02403v1
- Authors: Gawon Seo, Dongwon Kim, Suha Kwak
- Published: 2026-07-02T16:38:10Z
- Age days: 3

</details>
