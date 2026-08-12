---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30113v1"
published: "2026-06-29T10:45:53Z"
age_days: 1
score: 36
created: 2026-06-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "Sim2Real", "具身智能评测与基准"]
---

# SA-VLA: State-aware tokenizer for improving Vision-Language-Action Models' performance

> [!summary] 一句话结论（基于摘要）
> On 12 RoboTwin manipulation tasks, SA-VLA improves the average success rate from 0.29 to 0.56 over the strongest tokenizer baseline.

## 关键点

- **问题**：Discrete action tokenization provides a compact interface for autoregressive VLA policies, but accurately recovering continuous robot actions from discrete codes remains challenging.
- **创新点 / 方法**：Existing tokenizers typically map each discrete code to a fixed continuous action prototype, ignoring the robot's current proprioceptive state.
- **证据**：On 12 RoboTwin manipulation tasks, SA-VLA improves the average success rate from 0.29 to 0.56 over the strongest tokenizer baseline.
- **局限**：Discrete action tokenization provides a compact interface for autoregressive VLA policies, but accurately recovering continuous robot actions from discrete codes remains challenging.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Discrete action tokenization provides a compact interface for autoregressive VLA
policies, but accurately recovering continuous robot actions from discrete codes remains
challenging. Existing tokenizers typically map each discrete code to a fixed continuous
action prototype, ignoring the robot's current proprioceptive state. This limitation is
particularly pronounced in manipulation, where the same action token may require
different continuous controls under different joint configurations, object poses, and
contact conditions. We therefore propose SA-VLA, a state-aware action tokenizer that
conditions action decoding on robot state. We study two state-injection mechanisms for
VQ-based action tokenization: cross-attention between state and action features, and a
lightweight state adapter that predicts action-wise modulation factors for state-
conditioned action modulation and reconstruction. The adapter formulation expands the
effective support of a finite codebook by allowing each discrete token to represent a
family of state-dependent continuous actions, while preserving the efficiency and
compatibility of discrete action modeling. Integrated into an LLM-based VLA policy, SA-
VLA supports both autoregressive and parallel action-token decoding with minimal changes
to the model interface. On 12 RoboTwin manipulation tasks, SA-VLA improves the average
success rate from 0.29 to 0.56 over the strongest tokenizer baseline. In zero-shot sim-
to-real experiments on three real-world tasks, it further improves average success from
0.15 to 0.33 over the strongest tokenizer baseline. These results demonstrate that
state-conditioned action decoding is a simple and effective mechanism for reducing the
compression gap in discrete VLA policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30113v1
- Authors: Tengyue Jiang, Chunpu Xu, Jiayue Kang, Yao Mu
- Published: 2026-06-29T10:45:53Z
- Age days: 1

</details>
