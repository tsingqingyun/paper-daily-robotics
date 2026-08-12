---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30378v1"
published: "2026-06-29T14:38:20Z"
age_days: 0
score: 27
created: 2026-06-30
concepts: ["多模态基础模型", "Sim2Real", "具身智能评测与基准"]
---

# OmniCoT: A Benchmark for Global and Multi-Step Panoramic Reasoning

> [!summary] 一句话结论（基于摘要）
> It includes OmniCoT-B (6.7K data) for evaluation, which measures both answer accuracy and reasoning quality, OmniCoT-Real (1K data) as a manually annotated real-world subset to quantify the Sim-to-Real gap.

## 关键点

- **问题**：Multimodal Large Language Models (MLLMs) have demonstrated promising spatial reasoning capabilities, while these abilities remain underexplored in the emerging visual modality of panoramic imagery.
- **创新点 / 方法**：To address this gap, we introduce OmniCoT, a panoramic spatial reasoning suite designed to enable MLLMs to use global evidence and perform multi-step inference across viewpoints.
- **证据**：It includes OmniCoT-B (6.7K data) for evaluation, which measures both answer accuracy and reasoning quality, OmniCoT-Real (1K data) as a manually annotated real-world subset to quantify the Sim-to-Real gap.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multimodal Large Language Models (MLLMs) have demonstrated promising spatial reasoning
capabilities, while these abilities remain underexplored in the emerging visual modality
of panoramic imagery. The full 360°$\times$180° field of view of panoramas essentially
supports complex global multi-step reasoning, which is also the fundamental advantage of
panoramas in applications such as embodied intelligence. However, existing panoramic
benchmarks largely focus on simplistic queries that rely on local cues or single-/few-
step reasoning, thereby ignoring the fundamental advantage of panoramas and failing to
fully exploit their potential. To address this gap, we introduce OmniCoT, a panoramic
spatial reasoning suite designed to enable MLLMs to use global evidence and perform
multi-step inference across viewpoints. It includes OmniCoT-B (6.7K data) for
evaluation, which measures both answer accuracy and reasoning quality, OmniCoT-Real (1K
data) as a manually annotated real-world subset to quantify the Sim-to-Real gap. For
training, OmniCoT-T (14.3K data) is purpose-built with structured stepwise Chain-of-
Thought annotations that explicitly link intermediate reasoning steps to panoramic
evidence. Based on OmniCoT-T, we introduce OmniCoT-R1 and adopt a two-stage training
strategy tailored to the geometrically complex panoramic space, where Supervised Fine-
tuning (SFT) anchors reasoning to panoramic evidence (e.g., bearings, proximity) and
GRPO penalizes geometrically incoherent paths to consolidate global 360° spatial
consistency. Through OmniCoT, we aim to recalibrate the difficulty of panoramic spatial
reasoning to better align with the intrinsic capabilities of panoramic imagery, thereby
fostering meaningful progress in this research area.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30378v1
- Authors: Haocong He, Chenfei Liao, Zichen Wen, Zihao Dongfang, Xu Zheng, Bin Ren, Chang Su, Zixin Zhang, Harold Haodong Chen, Hongfei Zhang, Weijia Li, Kailun Yang, Conghui He, Xuming Hu, Nicu Sebe, Linfeng Zhang
- Published: 2026-06-29T14:38:20Z
- Age days: 0

</details>
