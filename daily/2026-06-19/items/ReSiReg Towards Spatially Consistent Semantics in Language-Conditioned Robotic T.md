---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19088v1"
published: "2026-06-17T13:58:06Z"
age_days: 1
score: 29
created: 2026-06-19
concepts: ["多模态基础模型"]
---

# ReSiReg: Towards Spatially Consistent Semantics in Language-Conditioned Robotic Tasks

> [!summary] 一句话结论（基于摘要）
> Quantitative results show improved dense retrieval; manipulation scenes show more spatially consistent target activations.

## 关键点

- **问题**：However, dense VLM embeddings have shown to be noisy and lack spatial consistency.
- **创新点 / 方法**：Vision-Language Models (VLMs) enable robots to follow open-language instructions.
- **证据**：Quantitative results show improved dense retrieval; manipulation scenes show more spatially consistent target activations.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-19/ReSiReg Towards Spatially Consistent Semantics in Language-Conditioned Robotic T.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language Models (VLMs) enable robots to follow open-language instructions.
However, dense VLM embeddings have shown to be noisy and lack spatial consistency. This
is problematic for robotic applications, which require simultaneous reasoning over
semantics and 3D space. We examine spatial structure across recent VLMs and propose
ReSiReg, a feature reconstruction method that uses spatially consistent VLM
intermediates to improve dense language-grounded retrieval. ReSiReg clusters
intermediates into visual prototypes, derives their language descriptors, and
reconstructs each patch as a soft mixture of prototype-level language embeddings. We
evaluate quantitatively on OVSS and 3D mapping across backbones, and qualitatively in
real-world manipulation scenes. Quantitative results show improved dense retrieval;
manipulation scenes show more spatially consistent target activations. We further
provide a compact 25M dense VLM for robotic applications, substantially smaller than and
competitive with ViT-B baselines. Available at https://resireg.github.io

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19088v1
- Authors: Simon Schwaiger, David Seyser, Alessandro Scherl, Wilfried Wöber, Gerald Steinbauer-Wagner
- Published: 2026-06-17T13:58:06Z
- Age days: 1

</details>
