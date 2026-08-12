---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22409v1"
published: "2026-06-21T09:54:39Z"
age_days: 2
score: 35
created: 2026-06-24
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Gold Points Sniper: Self-guided Visual Reasoning in VLM for Fine-grained Action Understanding

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on our curated instruction-tuning dataset based on the CAP benchmark demonstrate that GPS-enhanced lightweight VLMs achieve substantial performance improvements, with some models reaching performance comparable to proprietary GPT-4o whil…

## 关键点

- **问题**：While open-vocabulary action recognition methods remain limited to assigning predefined labels, and vision-language models (VLMs) face an inherent trade-off between informational richness and factual fidelity in their outputs, neither approach achieves the deep semantic interpretation required for reliable human- robo…
- **创新点 / 方法**：We propose Gold Points Sniper (GPS), a novel framework that empowers lightweight VLMs with self-guided multimodal reasoning capabilities for fine-grained human action understanding.
- **证据**：Extensive experiments on our curated instruction-tuning dataset based on the CAP benchmark demonstrate that GPS-enhanced lightweight VLMs achieve substantial performance improvements, with some models reaching performance comparable to proprietary GPT-4o while maintaining superior factual accuracy.
- **局限**：While open-vocabulary action recognition methods remain limited to assigning predefined labels, and vision-language models (VLMs) face an inherent trade-off between informational richness and factual fidelity in their outputs, neither approach achieves the deep semantic interpretation required for reliable human- robo…

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots operating in everyday environments must understand fine-grained human actions,
intentions, and contextual cues from broad views where people occupy only small regions,
a capability unmet by current systems. While open-vocabulary action recognition methods
remain limited to assigning predefined labels, and vision-language models (VLMs) face an
inherent trade-off between informational richness and factual fidelity in their outputs,
neither approach achieves the deep semantic interpretation required for reliable human-
robot interaction. We propose Gold Points Sniper (GPS), a novel framework that empowers
lightweight VLMs with self-guided multimodal reasoning capabilities for fine-grained
human action understanding. Our approach comprises three key modules: Gold Points
Extractor trains VLMs to identify critical action-relevant details, Selective Socratic
Questioner validates and refines these details through selective self-questioning, and
Semantic Entailment Evaluator quantitatively assesses factual consistency using semantic
entailment classification. Extensive experiments on our curated instruction-tuning
dataset based on the CAP benchmark demonstrate that GPS-enhanced lightweight VLMs
achieve substantial performance improvements, with some models reaching performance
comparable to proprietary GPT-4o while maintaining superior factual accuracy. Our work
establishes a reliable foundation for fine-grained action understanding in domestic
robotics, enabling robots to safely interpret human behavior through information-dense
yet factually grounded descriptions. Source code, training configurations, annotation
prompts, and dataset details are released at https://github.com/Haodi-Liu/GPS-Gold-
Point-Sniper.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22409v1
- Authors: Haodi Liu, Xinhang Yang, Kunda Yan, Sen Cui, Zeyu Zhang, Changshui Zhang
- Published: 2026-06-21T09:54:39Z
- Age days: 2

</details>
