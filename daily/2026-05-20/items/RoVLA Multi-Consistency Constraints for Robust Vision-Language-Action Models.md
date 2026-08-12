---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19678v1"
published: "2026-05-19T11:10:20Z"
age_days: 0
score: 40
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Experiments on LIBERO-Plus, RoboTwin 2.0, and real-world manipulation tasks show that RoVLA consistently outperforms strong baseline methods and exhibits superior robustness under diverse task and observation shifts.

## 关键点

- **问题**：Vision-Language-Action (VLA) models have shown strong performance on embodied manipulation, yet they remain brittle under visual observation changes, paraphrased language instructions, and compounded perturbations.
- **创新点 / 方法**：To address this issue, we propose RoVLA, a robust vision-language-action framework with multi-consistency constraints.
- **证据**：Experiments on LIBERO-Plus, RoboTwin 2.0, and real-world manipulation tasks show that RoVLA consistently outperforms strong baseline methods and exhibits superior robustness under diverse task and observation shifts.
- **局限**：This limitation suggests that existing methods still rely heavily on shallow correlations in the training distribution, rather than learning stable couplings among task semantics, environment states, and action generation.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have shown strong performance on embodied
manipulation, yet they remain brittle under visual observation changes, paraphrased
language instructions, and compounded perturbations. This limitation suggests that
existing methods still rely heavily on shallow correlations in the training
distribution, rather than learning stable couplings among task semantics, environment
states, and action generation. Although recent efforts improve robustness through
larger-scale training, post-training adaptation, or enhanced predictive modeling, they
rarely enforce invariance-oriented consistency within the end-to-end policy itself. To
address this issue, we propose RoVLA, a robust vision-language-action framework with
multi-consistency constraints. RoVLA enforces consistency under three complementary
transformations: instruction semantics, trajectory evolution, and observation
perturbation. Specifically, Instructional Consistency (IC) promotes stable grounding
under semantically equivalent instruction rewrites, Evolutionary Consistency (EC)
preserves coherent action intent throughout the generation process, and Observational
Consistency (OC) improves robustness to visual and proprioceptive perturbations by
enforcing consistent predictions before and after targeted disturbances. By explicitly
modeling these invariances during training, RoVLA reduces reliance on superficial
correlations and improves robustness and generalization. Experiments on LIBERO-Plus,
RoboTwin 2.0, and real-world manipulation tasks show that RoVLA consistently outperforms
strong baseline methods and exhibits superior robustness under diverse task and
observation shifts. These results demonstrate the effectiveness of multi-consistency
learning for robust embodied control. Codes will be available at
https://github.com/HCPLab-SYSU/RoVLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19678v1
- Authors: Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu, Liang Lin
- Published: 2026-05-19T11:10:20Z
- Age days: 0

</details>
