---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01067v1"
published: "2026-07-01T15:26:26Z"
age_days: 1
score: 40
created: 2026-07-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments in simulation and on real robots demonstrate that our model achieves superior performance, exhibiting robust generalization and fine-grained manipulation capabilities.

## 关键点

- **问题**：However, limited by hardware and data collection systems, existing datasets with tactility remain small in scale and narrow in contact coverage.
- **创新点 / 方法**：In this paper, we present H-Tac, a large- scale tactile-action dataset with 160-hour egocentric human videos containing more than 300 tasks and 135k episodes.
- **证据**：Extensive experiments in simulation and on real robots demonstrate that our model achieves superior performance, exhibiting robust generalization and fine-grained manipulation capabilities.
- **局限**：As an essential modality for dexterous and contact-rich tasks, tactile sensing provides precise force feedback that cannot be reliably inferred from vision.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulati.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As an essential modality for dexterous and contact-rich tasks, tactile sensing provides
precise force feedback that cannot be reliably inferred from vision. However, limited by
hardware and data collection systems, existing datasets with tactility remain small in
scale and narrow in contact coverage. Meanwhile, Vision-Language-Action (VLA) models
with tactile modality are constrained on dynamics-agnostic post-training, which limits
the performance ceiling on downstream tasks. In this paper, we present H-Tac, a large-
scale tactile-action dataset with 160-hour egocentric human videos containing more than
300 tasks and 135k episodes. Building upon this, we propose Transferable Tactile Pre-
Training (TTP), a system of tactile-based pre-training on human data for fine-grained
robotic tasks. To bridge the gap between humans and robots, we use unified tactile and
action spaces throughout the pre-training and post-training phases, preserving prior
knowledge during human-to-robot transfer. By leveraging a tactile expert for future
tactile prediction, our framework explicitly models the contact dynamics and precise
physical interactions. Extensive experiments in simulation and on real robots
demonstrate that our model achieves superior performance, exhibiting robust
generalization and fine-grained manipulation capabilities. TTP paves the way for
scalable tactile pre-training via human-to-robot transfer.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01067v1
- Authors: Chi Zhang, Penglin Cai, Ziheng Xi, Haoqi Yuan, Hao Luo, Wanpeng Zhang, Sipeng Zheng, Chaoyi Xu, Zongqing Lu
- Published: 2026-07-01T15:26:26Z
- Age days: 1

</details>
