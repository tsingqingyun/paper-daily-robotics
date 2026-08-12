---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13970v1"
published: "2026-06-11T23:24:38Z"
age_days: 3
score: 32
created: 2026-06-15
concepts: ["多模态基础模型", "机器人学习"]
---

# An Attention-based Model for Robust Forecasting with Missing Modality

> [!summary] 一句话结论（基于摘要）
> We show that our proposed model can be trained with missing modalities while approximating a robust representation of all modalities.

## 关键点

- **问题**：Learning with missing modalities is a fundamental challenge in multimodal robot learning, as real-world robotic systems often operate in environments with incomplete sensor data.
- **创新点 / 方法**：In this paper, we introduce a multimodal model designed to handle missing modalities during both training and inference.
- **证据**：We show that our proposed model can be trained with missing modalities while approximating a robust representation of all modalities.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning with missing modalities is a fundamental challenge in multimodal robot
learning, as real-world robotic systems often operate in environments with incomplete
sensor data. Attention-based models are appealing for processing multimodal data because
they can handle multiple modalities with a single backbone network. However, most
multimodal models assume that all modalities are available during both training and
inference, limiting their applicability in robotic perception and decision-making. In
this paper, we introduce a multimodal model designed to handle missing modalities during
both training and inference. The model is formulated as a conditional variational
autoencoder (CVAE) and incorporates a transformer-based architecture that leverages
attention mechanisms to learn a unified, fixed-dimensional representation, even when
some modalities are missing. We show that our proposed model can be trained with missing
modalities while approximating a robust representation of all modalities. We evaluate
our approach on five multimodal datasets across two robot learning tasks: human
trajectory prediction and robot manipulation forecasting. Experimental results
demonstrate that our model effectively learns from incomplete data and is superior to
prior multimodal fusion approaches.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13970v1
- Authors: Zhitian Zhang, Wenjie Zi, Yunduz Rakhmangulova, Saghar Irandoust, Hossein Hajimirsadeghi, Thibaut Durand
- Published: 2026-06-11T23:24:38Z
- Age days: 3

</details>
