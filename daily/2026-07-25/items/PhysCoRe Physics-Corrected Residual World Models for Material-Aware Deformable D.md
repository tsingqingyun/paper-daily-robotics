---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20653v1"
published: "2026-07-22T18:25:57Z"
age_days: 2
score: 26
created: 2026-07-25
concepts: ["世界模型"]
---

# PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics

> [!summary] 一句话结论（基于摘要）
> Experiments on real deformable-object manipulation sequences show that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that its predicted confidence forms a reliable distribution across the object's geometry, providing a natural si…

## 关键点

- **问题**：Predicting how deformable objects evolve under robotic manipulation is a longstanding challenge.
- **创新点 / 方法**：We present PhysCoRe, a physics-corrected residual world model that couples a differentiable Material Point Method (MPM) simulator with two feed-forward neural networks.
- **证据**：Experiments on real deformable-object manipulation sequences show that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that its predicted confidence forms a reliable distribution across the object's geometry, providing a natural signal for future confidence-guided exploration.
- **局限**：Existing approaches typically rely on per-object optimization to fit material parameters, which can be slow and cannot generalize, while end-to-end learned alternatives extrapolate poorly and often violate basic physical structure.

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Predicting how deformable objects evolve under robotic manipulation is a longstanding
challenge. Existing approaches typically rely on per-object optimization to fit material
parameters, which can be slow and cannot generalize, while end-to-end learned
alternatives extrapolate poorly and often violate basic physical structure. We present
PhysCoRe, a physics-corrected residual world model that couples a differentiable
Material Point Method (MPM) simulator with two feed-forward neural networks. A material
refinement module, Material from Motion (MfM), infers per-particle elasticity from
visual observations, grounding the simulator in object-specific physics. A residual
correction module, Residual from Dynamics (RfD), learns the discrepancy and predicts
corrections to the simulator's internal dynamics, absorbing systematic biases that the
analytical model cannot capture. This design also supports online material
identification on novel objects. MfM adapts from limited interactions, and its
predictive uncertainty steers further exploration toward the regions where its estimate
is least confident. Experiments on real deformable-object manipulation sequences show
that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that
its predicted confidence forms a reliable distribution across the object's geometry,
providing a natural signal for future confidence-guided exploration.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20653v1
- Authors: Haocheng Yin, Shuohan Tao, Yongsheng Chen, Lu Gan
- Published: 2026-07-22T18:25:57Z
- Age days: 2

</details>
