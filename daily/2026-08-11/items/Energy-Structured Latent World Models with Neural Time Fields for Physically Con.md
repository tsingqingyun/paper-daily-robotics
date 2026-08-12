---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09876v1"
published: "2026-08-10T17:31:18Z"
age_days: 0
score: 28
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Energy-Structured Latent World Models with Neural Time Fields for Physically Constistent Open-World Motion Planning

> [!summary] 一句话结论（基于摘要）
> Against Active Neural Time Fields, it improves navigation success from 81.3% to 89.7% and SPL from 0.64 to 0.73, while cutting the physical collision rate from 12.1% to 5.8% and the Eikonal residual from 0.083 to 0.031.

## 关键点

- **问题**：Physically consistent motion planning remains a fundamental challenge in embodied AI, as generated trajectories must strictly conform to real-world execution dynamics.
- **创新点 / 方法**：To address this, we propose a novel Energy-Structured Latent World Model (ELWM).
- **证据**：Against Active Neural Time Fields, it improves navigation success from 81.3% to 89.7% and SPL from 0.64 to 0.73, while cutting the physical collision rate from 12.1% to 5.8% and the Eikonal residual from 0.083 to 0.031.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physically consistent motion planning remains a fundamental challenge in embodied AI, as
generated trajectories must strictly conform to real-world execution dynamics. While
latent world models offer a promising approach by predicting these dynamics, existing
methods learn unconstrained future representations where absorbed physics remains
implicit. Therefore, they fail to form reusable physical knowledge, which compromises
reliability in unpredictable open-world navigation. To address this, we propose a novel
Energy-Structured Latent World Model (ELWM). Our key idea is to structure the ELWM
latent state to explicitly carry energy and momentum, ensuring strictly causal
transitions via dissipation and control ports. Trained on multimodal RGB-D and inertial
interaction histories, our model guarantees physically consistent predictions. We
further implement this for motion planning by constructing Physics-Conditioned Neural
Time Fields (PC-NTF), a key technical cornerstone that integrates ELWM into an arrival
time field via the Eikonal equation to yield a physically-informed navigation policy.
Across held-out scenes, our evaluation reveals significant improvements. Compared to
generic latent models, PC-NTF reduces 0.8-s motion-prediction NRMSE from 0.36 to 0.29.
Against Active Neural Time Fields, it improves navigation success from 81.3% to 89.7%
and SPL from 0.64 to 0.73, while cutting the physical collision rate from 12.1% to 5.8%
and the Eikonal residual from 0.083 to 0.031. Beyond these targeted gains, our results
demonstrate that embedding explicit physical structures into latent spaces intrinsically
bridges the gap between predictive world models and safe, dynamically feasible motion
planning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09876v1
- Authors: Yapeng Liu, Yuanzhao Zhai, Bo Ding, Huaimin Wang, Lin Wang
- Published: 2026-08-10T17:31:18Z
- Age days: 0

</details>
