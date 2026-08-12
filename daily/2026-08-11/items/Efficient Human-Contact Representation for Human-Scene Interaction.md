---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09388v1"
published: "2026-08-10T10:09:27Z"
age_days: 0
score: 28
created: 2026-08-11
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Efficient Human-Contact Representation for Human-Scene Interaction

> [!summary] 一句话结论（基于摘要）
> The experimental results show that our approach outperforms state-of-the-art models in reconstruction accuracy and achieves a computation speed-up of at least 12 times over recent baselines.

## 关键点

- **问题**：Despite significant progress in network architectures to improve the results or optimize models' parameters for fast inference speed, the efficient representation of contact between humans and their environments remains an open challenge.
- **创新点 / 方法**：In this paper, we propose a new efficient human- contact representation for human-scene interaction.
- **证据**：The experimental results show that our approach outperforms state-of-the-art models in reconstruction accuracy and achieves a computation speed-up of at least 12 times over recent baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-11/Efficient Human-Contact Representation for Human-Scene Interaction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human-scene interaction is an active research topic with several industrial applications
in virtual reality, gaming, robotics, and surveillance. Despite significant progress in
network architectures to improve the results or optimize models' parameters for fast
inference speed, the efficient representation of contact between humans and their
environments remains an open challenge. In this paper, we propose a new efficient human-
contact representation for human-scene interaction. Our primary contribution is the
introduction of sparse contact masks that strategically select essential contact
information, significantly reducing redundant data in high-dimensional inputs.
Leveraging this efficient contact representation, we propose a suite of sparse operators
to replace traditional dense operators within deep network layers for faster
computation. Our approach not only enhances computational speed but also filters out
non-essential contact data, thereby improving the precision of human-scene interaction
models. To validate the effectiveness of our method, we conduct intensive experiments
across three public benchmark datasets, focusing on two critical tasks for human-scene
interaction: contact prediction and scene synthesis. The experimental results show that
our approach outperforms state-of-the-art models in reconstruction accuracy and achieves
a computation speed-up of at least 12 times over recent baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09388v1
- Authors: Nghia Vu, Tuong Do, Binh X. Nguyen, Erman Tjiputra, Anh Nguyen
- Published: 2026-08-10T10:09:27Z
- Age days: 0

</details>
