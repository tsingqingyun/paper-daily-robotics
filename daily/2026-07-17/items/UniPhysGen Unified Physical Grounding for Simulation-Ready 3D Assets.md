---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13586v1"
published: "2026-07-15T08:27:07Z"
age_days: 1
score: 29
created: 2026-07-17
concepts: ["世界模型", "具身智能评测与基准"]
---

# UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets

> [!summary] 一句话结论（基于摘要）
> We present UniPhys, a scalable framework for automatically transforming raw 3D assets into simulation-ready assets with unified physical semantics.

## 关键点

- **问题**：However, most existing 3D assets lack unified physical semantics, including articulation semantics and intrinsic physical properties, required for realistic interaction.
- **创新点 / 方法**：We present UniPhys, a scalable framework for automatically transforming raw 3D assets into simulation-ready assets with unified physical semantics.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physically grounded 3D assets are increasingly important for embodied AI and robotic
simulation. However, most existing 3D assets lack unified physical semantics, including
articulation semantics and intrinsic physical properties, required for realistic
interaction. Current approaches either treat these semantics independently or rely on
canonicalized object structures, limiting robustness across heterogeneous 3D assets. We
present UniPhys, a scalable framework for automatically transforming raw 3D assets into
simulation-ready assets with unified physical semantics. Based on UniPhys, we construct
UniPhys-40K, a large-scale physically grounded dataset, together with UniPhys-Bench, a
carefully verified benchmark for unified physical grounding evaluation. We further
introduce UniPhysGen, a unified physical grounding model that jointly reasons over
articulation semantics and intrinsic physical properties. UniPhysGen incorporates
geometry-robust articulation grounding to mitigate geometric shortcut bias under
heterogeneous part decompositions. Extensive experiments demonstrate state-of-the-art
performance across articulation grounding and intrinsic physical property estimation
tasks, while the resulting assets can be directly deployed in robotic simulation
environments for realistic physical interaction. Our code and dataset will be available
at https://github.com/breezexian/UniPhysGen.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13586v1
- Authors: Xian Li, Rong Wei, Lujie Yang, Haolin Huang, Junyuan Fang, Siliang Tang, Jun Xiao, Rui Tang, Juncheng Li
- Published: 2026-07-15T08:27:07Z
- Age days: 1

</details>
