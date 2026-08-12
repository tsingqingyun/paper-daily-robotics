---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09381v1"
published: "2026-08-10T09:57:54Z"
age_days: 0
score: 39
created: 2026-08-11
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling

> [!summary] 一句话结论（基于摘要）
> On LIBERO-Plus, JEPA-WAM achieves 79.2%, the best result without large- scale robot-policy pretraining, while its pretrained $π_{0.5}$ instantiation reaches 86.3%, achieving the best overall performance.

## 关键点

- **问题**：Robust robot control benefits from explicitly modeling state transitions, but video- generation world action models (WAMs) introduce substantial deployment cost.
- **创新点 / 方法**：We introduce JEPA-WAM, a latent WAM built in a pretrained V-JEPA space, which couples latent transition prediction with continuous action generation through a shared predictor.
- **证据**：On LIBERO-Plus, JEPA-WAM achieves 79.2%, the best result without large- scale robot-policy pretraining, while its pretrained $π_{0.5}$ instantiation reaches 86.3%, achieving the best overall performance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robust robot control benefits from explicitly modeling state transitions, but video-
generation world action models (WAMs) introduce substantial deployment cost. Existing
latent WAMs avoid explicit future generation, but often compress predictive
representations or separate predictive modeling from the representations used for action
generation. We introduce JEPA-WAM, a latent WAM built in a pretrained V-JEPA space,
which couples latent transition prediction with continuous action generation through a
shared predictor. JEPA-WAM predicts a spatially structured joint current-future target
that captures task-shared visual temporal structure between current and future
observations, while preserving dense patch-level correspondence. Through the shared
predictor, transition supervision directly shapes the backbone, from which dedicated
representations are extracted for action prediction. The same design can also be
instantiated in pretrained VLA policies while preserving their original perception and
action pathways. On LIBERO-Plus, JEPA-WAM achieves 79.2%, the best result without large-
scale robot-policy pretraining, while its pretrained $π_{0.5}$ instantiation reaches
86.3%, achieving the best overall performance. Experiments on RoboTwin 2.0 and real-
world bimanual manipulation further demonstrate strong generalization under visual and
spatial shifts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09381v1
- Authors: Yihan Lin, Jiawei He, Shifeng Bao, Chen Zhao, Yang Li, Xiaobo Wang, Yan Wang, Cheng Chi, Jing Zhang
- Published: 2026-08-10T09:57:54Z
- Age days: 0

</details>
