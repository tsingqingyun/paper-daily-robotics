---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07304v1"
published: "2026-06-05T14:21:44Z"
age_days: 2
score: 29
created: 2026-06-08
concepts: ["智能体 Agent", "世界模型"]
---

# CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning

> [!summary] 一句话结论（基于摘要）
> On real-world DROID and zero-shot transfer to RoboCasa, CAPE substantially outperforms prior baselines on future-state retrieval, offline action matching, and closed-loop planning, while notably reducing planning-time inference cost at long prediction horizon…

## 关键点

- **问题**：Embodied agents need to predict the future consequences of candidate actions in order to plan effectively before execution.
- **创新点 / 方法**：We propose CAPE, a Contrastive Action-conditioned Parallel Encoding framework that learns visual dynamics by distinguishing the future outcomes induced by different action sequences.
- **证据**：On real-world DROID and zero-shot transfer to RoboCasa, CAPE substantially outperforms prior baselines on future-state retrieval, offline action matching, and closed-loop planning, while notably reducing planning-time inference cost at long prediction horizons.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/CAPE Contrastive Action-conditioned Parallel Encoding for Embodied Planning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied agents need to predict the future consequences of candidate actions in order to
plan effectively before execution. Existing visual dynamics models learn by
reconstructing future visual states or rolling out dense latent representations, which
spreads learning capacity across visually salient but planning-irrelevant content rather
than the action-conditioned changes that drive manipulation outcomes. We propose CAPE, a
Contrastive Action-conditioned Parallel Encoding framework that learns visual dynamics
by distinguishing the future outcomes induced by different action sequences. Given an
initial observation and a candidate action sequence, CAPE decodes the full future latent
trajectory in a single forward pass and is trained with a Goal-Convergent Contrastive
Objective that aligns predictions corresponding to the same future outcome while
separating those corresponding to different outcomes. On real-world DROID and zero-shot
transfer to RoboCasa, CAPE substantially outperforms prior baselines on future-state
retrieval, offline action matching, and closed-loop planning, while notably reducing
planning-time inference cost at long prediction horizons.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07304v1
- Authors: Cong Chen, Haowen Wang, Zhixiang Zhang, Pei Ren, Zhengping Che
- Published: 2026-06-05T14:21:44Z
- Age days: 2

</details>
