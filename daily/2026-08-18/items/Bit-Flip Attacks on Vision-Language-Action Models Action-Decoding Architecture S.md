---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15475v1"
published: "2026-08-16T01:44:09Z"
age_days: 2
score: 36
created: 2026-08-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability

> [!summary] 一句话结论（基于摘要）
> We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless.

## 关键点

- **问题**：Quantized Vision-Language-Action (VLA) models expose a weight-fault surface: Rowhammer-style faults can corrupt deployed INT8 bits.
- **创新点 / 方法**：We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/Bit-Flip Attacks on Vision-Language-Action Models Action-Decoding Architecture S.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Quantized Vision-Language-Action (VLA) models expose a weight-fault surface: Rowhammer-style faults can corrupt deployed INT8 bits. We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless. Across four model variants spanning three action-head families, damaging bits concentrate in a few action-generating layers, but the empirical budget depends sharply on the head: direct regression and token policies fall in $1$--$5$ flips, whereas the evaluated flow-matching policies require ${\sim}100$--$300$. Our fixed-direction manifold-escape loss cuts \pizero{}'s budget from ${\sim}1000$ to ${\sim}100$ flips, and a matched five-direction sweep shows that the attack is not specific to an all-positive direction. On a direct head, protecting $3.1\%$ of weights preserves $60\%$ success at $K{=}100$, and protecting $5.3\%$ moves the open-loop break threshold from 3 to 100 flips. Finally, task-calibrated emulated $K{=}100$ flips yield $0/20$ real-robot successes, versus $14/20$ clean and $16/20$ global-random. Weight integrity is therefore a security boundary for embodied foundation models. Code is included as ancillary material.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15475v1
- Authors: Yudong Gao, Linghan Chen, Wenhan Wu, Mia Zhou, Jiyao Wang, Kaiyan Ji, Mingyu Guo, Honglong Chen
- Published: 2026-08-16T01:44:09Z
- Age days: 2

</details>
