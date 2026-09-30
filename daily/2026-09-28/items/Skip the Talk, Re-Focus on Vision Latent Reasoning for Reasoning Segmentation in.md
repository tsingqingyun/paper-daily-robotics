---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30783v1"
published: "2026-09-25T04:04:55Z"
age_days: 3
score: 28
created: 2026-09-28
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Skip the Talk, Re-Focus on Vision: Latent Reasoning for Reasoning Segmentation in Multimodal Large Language Models

> [!summary] 先说人话（基于摘要）
> LIRSeg 用少量可学习潜在 token 替代冗长文字推理，直接帮助模型根据隐含文本需求分割目标。它试图减少文字推理对视觉定位的干扰。

## 问题

推理分割需要理解隐式文本并输出精细目标区域。已有显式 CoT 会增加冗余文本，摘要认为这会干扰感知 token 的注意力，并拉大视觉 token 间的有效距离。

## 创新点或方法

先通过空间对齐将潜在 token 绑定到对象相关视觉证据，再用分割奖励进行 GRPO。配合极端优势采样、分离探索与稳定性更新、潜在多样性增强，提高训练信号信息量并抑制表示坍缩。

## 证据

相对 VisionReasoner，ReasonSeg、MUSE、MMR 的 gIoU 分别绝对提升 4.9、7.1、4.7 个百分点，推理 token 数减少约 16 倍。

## 局限

token 数下降不等于端到端延迟同比下降；需核查潜在推理、空间对齐和各训练机制对最终收益的独立作用。

- **判断**：推理分割方向值得精读消融，机器人方向可重点看精度与实际推理成本。

## 研究关联

对多模态模型和具身智能体感知研究者，它提供了压缩语言推理、保留视觉定位能力的方案。摘要没有机器人闭环验证，价值首先在感知前端。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/Skip the Talk, Re-Focus on Vision Latent Reasoning for Reasoning Segmentation in.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reasoning segmentation aims to interpret implicit textual queries and enable fine-grained visual perception, which is critical for applications such as human-computer interaction and embodied agents. Existing methods typically generate explicit Chain-of-Thought (CoT) by multimodal large language models (MLLMs) before localizing the target. Although intuitive, such explicit verbal reasoning introduces substantial attention interference: redundant textual tokens disrupt attention during perception-token generation and also increase the effective distance between visual tokens. To address this issue, we propose LIRSeg, which fully replaces explicit CoT with a compact set of learnable latent tokens for reasoning segmentation. LIRSeg is trained in two stages: spatial alignment grounds the latent tokens in object-relevant visual evidence, and GRPO further optimizes them with segmentation rewards. To make these compact latent tokens more informative, we introduce three complementary mechanisms from an information perspective: extreme-advantage sampling for selecting informative training signals, decoupled exploration-stability updates for learning complementary representations, and latent diversity amplification for preventing representational collapse. Extensive experiments on benchmarks demonstrate that LIRSeg consistently improves both segmentation accuracy and reasoning efficiency. Compared with the VisionReasoner baseline, LIRSeg achieves absolute gIoU improvements of 4.9% on ReasonSeg, 7.1% on MUSE, and 4.7% on MMR, while achieving a approximately 16x reduction in reasoning tokens. Code is available in supplementary materials.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30783v1
- Authors: Tianhang Guo, Yulin He, Wei Chen, Wenjuan Zhou, Yuhang Li, Xinbiao Gan
- Published: 2026-09-25T04:04:55Z
- Age days: 3

</details>
