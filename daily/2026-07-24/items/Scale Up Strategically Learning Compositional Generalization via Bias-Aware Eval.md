---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21582v1"
published: "2026-07-23T17:57:09Z"
age_days: 0
score: 27
created: 2026-07-24
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> We further show the diagnosis is actionable: a bias-aware data collection strategy that reallocates a fixed budget toward under-grounded factors outperforms baselines in simulation and on a real robot using half the demonstrations, thereby enabling more sampl…

## 关键点

- **问题**：However, pretrained policies are known to take shortcuts, deferring to salient cues rather than grounding language.
- **创新点 / 方法**：We introduce a diagnostic framework that localizes this failure to individual \textit{instruction factors}, \textit{e.g.,} reusable semantic components such as color, verb, object, size, and spatial attribute.
- **证据**：We further show the diagnosis is actionable: a bias-aware data collection strategy that reallocates a fixed budget toward under-grounded factors outperforms baselines in simulation and on a real robot using half the demonstrations, thereby enabling more sample-efficient and generalizable policy learning.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Compositional generalization is essential for robot to follow diverse instructions.
However, pretrained policies are known to take shortcuts, deferring to salient cues
rather than grounding language. We introduce a diagnostic framework that localizes this
failure to individual \textit{instruction factors}, \textit{e.g.,} reusable semantic
components such as color, verb, object, size, and spatial attribute. Our framework
formalizes instruction factor bias, the tendency of fine-tuned policies to over-rely on
dominant factors as shortcuts, and quantifies it through two metrics: Factor Dominance
Rate (FDR), capturing pairwise bias between factors, and Factor Dominance Hierarchy
(FDH), aggregating these into a global ranking. Evaluation on six foundation policies
reveals broadly consistent ordering, \textit{i.e.}, color $\geq$ object $\geq$ spatial
$\geq$ verb $\geq$ size, with color dominant, and verb and size most under-grounded. We
further show the diagnosis is actionable: a bias-aware data collection strategy that
reallocates a fixed budget toward under-grounded factors outperforms baselines in
simulation and on a real robot using half the demonstrations, thereby enabling more
sample-efficient and generalizable policy learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21582v1
- Authors: Yu Qi, Zhang Ye, Xinyi Xu, Yuxuan Lu, Amitoj Sandhu, Boce Hu, Haojie Huang, Jonathan Tremblay, Lawson L. S. Wong
- Published: 2026-07-23T17:57:09Z
- Age days: 0

</details>
