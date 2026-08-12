---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.16533v2"
published: "2026-06-15T10:37:42Z"
age_days: 2
score: 37
created: 2026-06-18
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Kairos: A Native World Model Stack for Physical AI

> [!summary] 一句话结论（基于摘要）
> Experiments on embodied world-model, long-horizon, and action-policy benchmarks show that Kairos achieves top level performance while offering a strong efficiency-capability trade-off.

## 关键点

- **问题**：World models are transitioning from passive visual generators to foundational, operational infrastructure for Physical AI: they must natively acquire world knowledge from heterogeneous experience, maintain persistent states over long horizons, and execute efficiently within real deployment constraints.
- **创新点 / 方法**：We introduce Kairos, a native world model stack designed around these requirements.
- **证据**：Experiments on embodied world-model, long-horizon, and action-policy benchmarks show that Kairos achieves top level performance while offering a strong efficiency-capability trade-off.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models are transitioning from passive visual generators to foundational,
operational infrastructure for Physical AI: they must natively acquire world knowledge
from heterogeneous experience, maintain persistent states over long horizons, and
execute efficiently within real deployment constraints. We introduce Kairos, a native
world model stack designed around these requirements. (1) Kairos learns the world by
pioneering a Native Pre-training Paradigm governed by a Cross-Embodiment Data
Curriculum, which organizes open-world videos, human behavioral data, and robot
interactions into a progressive developmental pathway. (2) Kairos maintains the world by
unified world understanding, generation, and prediction within a Native Unified
Architecture equipped with Hybrid Linear Temporal Attention, where sliding-window
attention captures local dynamics, dilated sliding windows capture mid-range
dependencies, and gated linear attention maintains persistent global memory. We
establish formal theoretical bounds demonstrating that this temporal factorization
strictly limits error accumulation, mathematically guaranteeing state propagation across
extended horizons. (3) Kairos runs the world by incorporating a Deployment-Aware System
Co-Design to support low-latency rollout generation on server and consumer-grade
hardware for real-world observation-action-feedback loops. Experiments on embodied
world-model, long-horizon, and action-policy benchmarks show that Kairos achieves top
level performance while offering a strong efficiency-capability trade-off. Together,
these results position Kairos as a cohesive operational foundation for future self-
evolving physical intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.16533v2
- Authors: Kairos Team, Fei Wang, Shan You, Qiming Zhang, Tao Huang, Zuoyi Fu, Zhisheng Zheng, Yunlong Xi, Feng Lv, Xiaoming Wu, Zeyu Liu, Cong Wan, Pu Li, Ruiqing Yang, Xiaoou Li, Wei Wang, Kangkang Zhu, Yuwei Zhang, Shi Fu, Zheng Zhang, Xiaoning Wu, Xuzeng Fan, Dacheng Tao, Xiaogang Wang
- Published: 2026-06-15T10:37:42Z
- Age days: 2

</details>
