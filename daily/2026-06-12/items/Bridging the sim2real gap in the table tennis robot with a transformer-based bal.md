---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11464v1"
published: "2026-06-09T21:35:59Z"
age_days: 2
score: 31
created: 2026-06-12
concepts: ["智能体 Agent", "世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Bridging the sim2real gap in the table tennis robot with a transformer-based ball states predictor

> [!summary] 一句话结论（基于摘要）
> We demonstrate that this simple substitution effectively narrows the sim-to-real gap while preserving the efficiency and scalability of simulation-based training.

## 关键点

- **问题**：Physics-based approaches rely heavily on accurate parameter identification and precise initial state, while learning-based methods often struggle to capture long-range temporal dependencies and are typically trained on limited or simulated data.
- **创新点 / 方法**：We propose a transformer-based framework for table tennis ball state prediction that leverages attention mechanisms to model long-range temporal correlations directly from historical observations, without relying on explicit flight or bounce models.
- **证据**：We demonstrate that this simple substitution effectively narrows the sim-to-real gap while preserving the efficiency and scalability of simulation-based training.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/Bridging the sim2real gap in the table tennis robot with a transformer-based bal.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic table tennis is a representative benchmark for high-speed, closed-loop robotic
control in dynamic environments, where accurate and fast prediction of ball states is
critical for reliable planning and control. Physics-based approaches rely heavily on
accurate parameter identification and precise initial state, while learning-based
methods often struggle to capture long-range temporal dependencies and are typically
trained on limited or simulated data. We propose a transformer-based framework for table
tennis ball state prediction that leverages attention mechanisms to model long-range
temporal correlations directly from historical observations, without relying on explicit
flight or bounce models. To support robust learning and generalization, we collected a
large-scale real-world dataset from players of varying skill levels and diverse ball
cannon configurations. The combination of a high-capacity transformer architecture and
extensive real-world data enables accurate long-horizon forecasting. Building on this
capability, we introduce a plug-and-play sim-to-real transfer strategy, Swap Predictor
at Deployment (SPAD), which replaces the physics-based simulator used during training
with the proposed real-world-trained predictor at deployment, improving the sim-to-real
transferability of the policy without requiring retraining. We demonstrate that this
simple substitution effectively narrows the sim-to-real gap while preserving the
efficiency and scalability of simulation-based training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11464v1
- Authors: Yin Bi, Christian Conti, Bilan Yang, Alexander Sigrist, Peter Dürr, Naoya Takahashi
- Published: 2026-06-09T21:35:59Z
- Age days: 2

</details>
