---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15727v1"
published: "2026-07-17T08:04:43Z"
age_days: 2
score: 35
created: 2026-07-20
concepts: ["具身智能评测与基准"]
---

# Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on both synthetic and real-world benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally aligned 3D reconstructions, significantly outperforming existing event-based methods.

## 关键点

- **问题**：However, extending such dense 3D reconstruction to event cameras remains challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the lack of large-scale, well-labeled datasets.
- **创新点 / 方法**：In this work, we introduce Event3R, a feed- forward framework that directly maps asynchronous event streams to globally consistent 3D point clouds.
- **证据**：Extensive experiments on both synthetic and real-world benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally aligned 3D reconstructions, significantly outperforming existing event-based methods.
- **局限**：However, extending such dense 3D reconstruction to event cameras remains challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the lack of large-scale, well-labeled datasets.

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/Event3R Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-T.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robust 3D reconstruction is essential for robotics and embodied perception. Recent feed-
forward approaches such as DUSt3R have demonstrated impressive progress in dense 3D
reconstruction from RGB images, achieving global geometric consistency and strong
generalization. However, extending such dense 3D reconstruction to event cameras remains
challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the
lack of large-scale, well-labeled datasets. In this work, we introduce Event3R, a feed-
forward framework that directly maps asynchronous event streams to globally consistent
3D point clouds. Event3R represents incoming events as spatial-temporal voxels, enabling
time-aware feature integration through a temporal attention module that enhances the
module's temporal feature learning. To further strengthen temporal representation
learning and reduce reliance on labeled data, we propose a Masked Bin Modeling (MBM)
strategy for self-supervised pre-training, enabling robust temporal representation
learning with minimal labeled data, and retain it as an auxiliary fine-tuning objective.
In addition, contrastive alignment and consistency regularization losses are
incorporated during fine-tuning to reinforce structural correspondence and temporal
coherence across views. Extensive experiments on both synthetic and real-world
benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally
aligned 3D reconstructions, significantly outperforming existing event-based methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15727v1
- Authors: Jian Huang, Haotian Shen, Xinhao Lou, Chengrui Dong, Wenpu Li, Peidong Liu
- Published: 2026-07-17T08:04:43Z
- Age days: 2

</details>
