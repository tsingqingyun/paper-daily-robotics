---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25802v1"
published: "2026-05-25T12:51:35Z"
age_days: 0
score: 32
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Rethinking VLM Representation for VLA Initialization

> [!summary] 一句话结论（基于摘要）
> Our experiments show that the original pretrained VLM representation is a key source of action performance.

## 关键点

- **问题**：Vision-Language-Action (VLA) models widely adopt pretrained Vision-Language Models (VLMs) as policy backbones, yet it remains unclear what kind of pretrained VLM representation is useful as a VLA initialization.
- **创新点 / 方法**：In this paper, we study VLA initialization as a controlled representation-design problem along three axes: capability-level embodied VQA supervision, parameter-update strategy, and robot-data pretraining.
- **证据**：Our experiments show that the original pretrained VLM representation is a key source of action performance.
- **局限**：However, embodied VQA adaptation does not yield uniform gains: its benefit depends on downstream bottlenecks, and gains from different capability domains are not simply additive.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models widely adopt pretrained Vision-Language Models
(VLMs) as policy backbones, yet it remains unclear what kind of pretrained VLM
representation is useful as a VLA initialization. In this paper, we study VLA
initialization as a controlled representation-design problem along three axes:
capability-level embodied VQA supervision, parameter-update strategy, and robot-data
pretraining. Our experiments show that the original pretrained VLM representation is a
key source of action performance. However, embodied VQA adaptation does not yield
uniform gains: its benefit depends on downstream bottlenecks, and gains from different
capability domains are not simply additive. For update strategy, LoRA provides a more
reliable initialization than Full Finetune, indicating that overly reshaping the
pretrained representation can weaken VLA initialization. Robot-data pretraining further
improves VLA initialization, with the strongest variant obtained by staged LoRA-based
training. Together, these findings suggest that effective VLM-to-VLA adaptation should
inject action-relevant embodied and robot-trajectory signals while preserving the
pretrained VLM representation that remains useful for action learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25802v1
- Authors: Weifeng Lin, Siyuan Huang, Hao Li, Tingwei Chen, Ruichuan An, Xinyu Wei, Jianbo Liu, Hongsheng Li
- Published: 2026-05-25T12:51:35Z
- Age days: 0

</details>
