---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12365v1"
published: "2026-06-10T17:34:12Z"
age_days: 3
score: 28
created: 2026-06-14
concepts: ["机器人学习", "Sim2Real"]
---

# Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics

> [!summary] 一句话结论（基于摘要）
> Notably, it outperforms existing co-training baselines by up to 33% when scaled to Open X-Embodiment - a large dataset with heterogeneous data quality and unstructured distribution shifts.

## 关键点

- **问题**：We propose Ambient Diffusion Policy, a simple and principled method for imitation learning from suboptimal data in robotics.
- **创新点 / 方法**：We propose Ambient Diffusion Policy, a simple and principled method for imitation learning from suboptimal data in robotics.
- **证据**：Notably, it outperforms existing co-training baselines by up to 33% when scaled to Open X-Embodiment - a large dataset with heterogeneous data quality and unstructured distribution shifts.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[Sim2Real]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/Ambient Diffusion Policy Imitation Learning from Suboptimal Data in Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We propose Ambient Diffusion Policy, a simple and principled method for imitation
learning from suboptimal data in robotics. High-quality, task-specific robot data is
expensive and time-consuming to collect, while suboptimal datasets with lower-quality or
out-of-distribution demonstrations are abundant. Existing methods that co-train on both
data sources in robotics often fail to separate the meaningful and the harmful features
in the suboptimal samples. In contrast, our method extracts only the useful features by
introducing a new axis to co-training in robotics: noise-dependent data usage. Ambient
Diffusion Policy restricts the contribution of suboptimal data during training to only
the high and low diffusion times. To rigorously justify our approach, we first observe
that robot action data exhibits a spectral power law. This induces two important
properties on the optimal Diffusion Policy that we exploit: a global-to-local hierarchy
and locality. We theoretically formalize this discussion using a simplified model. Our
experiments validate Ambient Diffusion Policy on four types of suboptimal action data
(noisy trajectories, sim-to-real gap, task mismatch, and large-scale data mixtures)
across six tasks. The results show that it effectively learns from arbitrary sources of
suboptimal data. Notably, it outperforms existing co-training baselines by up to 33%
when scaled to Open X-Embodiment - a large dataset with heterogeneous data quality and
unstructured distribution shifts. Overall, Ambient Diffusion Policy increases the
utility of suboptimal demonstrations and expands the set of usable data sources in
robotics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12365v1
- Authors: Adam Wei, Nicholas Pfaff, Thomas Cohn, Arif Kerem Dayı, Constantinos Daskalakis, Giannis Daras, Russ Tedrake
- Published: 2026-06-10T17:34:12Z
- Age days: 3

</details>
