---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19889v1"
published: "2026-07-22T08:20:52Z"
age_days: 2
score: 26
created: 2026-07-25
concepts: ["多模态基础模型", "世界模型"]
---

# LAVIFT: Latent-Action-Guided Vision Fine-Tuning for Surgical Interaction Recognition

> [!summary] 一句话结论（基于摘要）
> Understanding instrument-tissue interactions is essential for context-aware surgical AI and autonomous robotic surgery.

## 关键点

- **问题**：However, adapting them to fine-grained surgical interactions remains challenging: (1) freezing the vision encoder depends entirely on pretrained representations that may retain noise and provide weak spatial localization, while (2) full fine-tuning can improve global semantic alignment without ensuring that the encode…
- **创新点 / 方法**：Understanding instrument-tissue interactions is essential for context-aware surgical AI and autonomous robotic surgery.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：However, adapting them to fine-grained surgical interactions remains challenging: (1) freezing the vision encoder depends entirely on pretrained representations that may retain noise and provide weak spatial localization, while (2) full fine-tuning can improve global semantic alignment without ensuring that the encode…

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Understanding instrument-tissue interactions is essential for context-aware surgical AI
and autonomous robotic surgery. Pretrained vision-language models (VLMs) and vision
encoders offer an alternative to conventional interaction classifiers by transferring
broad visual and semantic knowledge. However, adapting them to fine-grained surgical
interactions remains challenging: (1) freezing the vision encoder depends entirely on
pretrained representations that may retain noise and provide weak spatial localization,
while (2) full fine-tuning can improve global semantic alignment without ensuring that
the encoder learns meaningful features in the correct action region. We address these
limitations by introducing LAViFiT, an end-to-end latent-action-guided framework for
vision-language fine-tuning. An inverse dynamics model captures the visual changes
induced by each action, while a forward world model drives the encoder to represent
action-relevant regions. A patch-level SIG Regularizer further prevents local feature
collapse without additional supervision, such as bounding boxes or pseudo-labels.
Experiments across multiple encoders and datasets improve recognition and image-text
alignment, while representation analyses show stronger grounding over the complete
instrument-tissue interaction region and more spatially coherent features.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19889v1
- Authors: Jiajun Cheng, Subarna Tripathi, Sainan Liu, Xiaofan Yu, Shan Lin
- Published: 2026-07-22T08:20:52Z
- Age days: 2

</details>
