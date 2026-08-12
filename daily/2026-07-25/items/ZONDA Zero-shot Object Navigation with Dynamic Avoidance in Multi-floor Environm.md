---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21025v1"
published: "2026-07-23T08:07:52Z"
age_days: 1
score: 24
created: 2026-07-25
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ZONDA: Zero-shot Object Navigation with Dynamic Avoidance in Multi-floor Environments

> [!summary] 一句话结论（基于摘要）
> Evaluated on a real Direct Drive Tech TITA biped robot and extensive simulations on HM3D and MP3D, ZONDA achieves significantly improved results.

## 关键点

- **问题**：In Object Goal Navigation task, existing methods are typically restricted to static and single-floor environments, ignoring cross-floor topologies and dynamic pedestrian, which limits their real-world deployment.
- **创新点 / 方法**：To address these limitations, we propose ZONDA, a zero-shot object navigation with dynamic avoidance framework.
- **证据**：Evaluated on a real Direct Drive Tech TITA biped robot and extensive simulations on HM3D and MP3D, ZONDA achieves significantly improved results.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In Object Goal Navigation task, existing methods are typically restricted to static and
single-floor environments, ignoring cross-floor topologies and dynamic pedestrian, which
limits their real-world deployment. To address these limitations, we propose ZONDA, a
zero-shot object navigation with dynamic avoidance framework. In particular, ZONDA
integrates three core components: (i) Heuristic multi-floor planning: from height-
difference traversable maps, enables stair traversal and cross-floor exploration without
a platform-specific learned controller; (ii) Multi-view target verification: cross-
checks multi-scale observations with a vision-language model, significantly reducing
false positives; and (iii) Dynamic pedestrian avoidance: explicitly tracks and predicts
moving pedestrians to generate anticipatory behaviors. Evaluated on a real Direct Drive
Tech TITA biped robot and extensive simulations on HM3D and MP3D, ZONDA achieves
significantly improved results. Moreover, ZONDA can maintain robust navigation on the
dynamic benchmark HM3D-DYNA compared to the existing baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21025v1
- Authors: Shaomin Liang, Xuanhong Liao, Shiyao Zhang
- Published: 2026-07-23T08:07:52Z
- Age days: 1

</details>
