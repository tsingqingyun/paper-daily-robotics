---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2605.02757v1"
published: "2026-05-04T15:57:07Z"
age_days: 
score: 30
created: 2026-05-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation

> [!summary] 一句话结论（基于摘要）
> For example, our method improves RDT-1B by 8% on Robotwin 2.0, and boosts $π_0$ by 5.1% on the more challenging LIBERO-Plus benchmark.

## 关键点

- **问题**：Vision-language-action (VLA) models typically rely on large-scale real-world videos, whereas simulated data, despite being inexpensive and highly parallelizable to collect, often suffers from a substantial visual domain gap and limited environmental diversity, resulting in weak real-world generalization.
- **创新点 / 方法**：We present an efficient video augmentation framework that converts simulated VLA videos into realistic training videos while preserving task semantics and action trajectories.
- **证据**：For example, our method improves RDT-1B by 8% on Robotwin 2.0, and boosts $π_0$ by 5.1% on the more challenging LIBERO-Plus benchmark.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-10/Seeing Realism from Simulation Efficient Video Transfer for Vision-Language-Acti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models typically rely on large-scale real-world videos,
whereas simulated data, despite being inexpensive and highly parallelizable to collect,
often suffers from a substantial visual domain gap and limited environmental diversity,
resulting in weak real-world generalization. We present an efficient video augmentation
framework that converts simulated VLA videos into realistic training videos while
preserving task semantics and action trajectories. Our pipeline extracts structured
conditions from simulation via video semantic segmentation and video captioning,
rewrites captions to diversify environments, and uses a conditional video transfer model
to synthesize realistic videos. To make augmentation practical at scale, we introduce a
diffusion feature-reuse mechanism that reuses video tokens across adjacent timesteps to
accelerate generation, and a coreset sampling strategy that identifies a compact, non-
redundant subset for augmentation under limited computation. Extensive experiments on
Robotwin 2.0, LIBERO, LIBERO-Plus, and a real robotic platform demonstrate consistent
improvements. For example, our method improves RDT-1B by 8% on Robotwin 2.0, and boosts
$π_0$ by 5.1% on the more challenging LIBERO-Plus benchmark. Code is available at:
https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation.

### 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2605.02757v1
- Authors: Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You, Fei Wang, Tao Huang, Chang Xu
- Published: 2026-05-04T15:57:07Z
- Age days: 

</details>
