---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19880v1"
published: "2026-07-22T08:10:49Z"
age_days: 1
score: 37
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# EA-Nav: Learning Safe Visual Navigation Policies with Embodiment Awareness

> [!summary] 一句话结论（基于摘要）
> Experimental results show that the proposed method effectively improves navigation performance across different embodiment settings, demonstrating the effectiveness of incorporating embodiment geometry into embodied navigation.

## 关键点

- **问题**：Cross-embodiment navigation is a key challenge in embodied intelligence.
- **创新点 / 方法**：To address these challenges, we propose an imitation-learning-based embodiment-aware navigation framework with a modular multi-stage design.
- **证据**：Experimental results show that the proposed method effectively improves navigation performance across different embodiment settings, demonstrating the effectiveness of incorporating embodiment geometry into embodied navigation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Cross-embodiment navigation is a key challenge in embodied intelligence. Due to
differences in embodiment, the same visual observation may imply different actions for
different agents, making prediction ambiguous when relying solely on vision. Existing
studies mainly rely on reinforcement learning, which requires large-scale interaction
and careful reward design, making it difficult to support scalable pretraining and real-
world adaptation. In contrast, imitation-learning-based approaches remain limited. To
address these challenges, we propose an imitation-learning-based embodiment-aware
navigation framework with a modular multi-stage design. In pretraining, we construct a
cross-embodiment navigation dataset from Internet videos and introduce embodiment
geometry as conditional tokens to reduce action ambiguity under the same observation. In
fine-tuning, we design a multimodal information injection mechanism based on a decoupled
architecture. Specifically, we design a trajectory augmentation strategy to generate
high-risk samples, which are used to train spatial perception and risk-aware correction
separately, thereby explicitly incorporating embodiment geometry for safe navigation.
Experimental results show that the proposed method effectively improves navigation
performance across different embodiment settings, demonstrating the effectiveness of
incorporating embodiment geometry into embodied navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19880v1
- Authors: Jialu Zhang, Yong Du, Xianda Guo, Shunwang Sun, Xinqi Liu, Yue Sun, Guodong Lu, Wei Sui, Jituo Li
- Published: 2026-07-22T08:10:49Z
- Age days: 1

</details>
