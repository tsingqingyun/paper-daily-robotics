---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10464v1"
published: "2026-09-09T17:08:13Z"
age_days: 1
score: 26
created: 2026-09-11
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization

> [!summary] 先说人话（基于摘要）
> In contrast to DINO-WM, SG-JEPA reduces open-loop prediction error by up to 2 times on two-dimensional datasets, and increases control success rate up to 2.5 times for three-dimensional robotic datasets, for which we train independent diffusion policies.

## 问题

Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate physically realistic dynamics remains hitherto untested.

## 创新点或方法

In this work, we introduce SemiGroup-JEPA (SG-JEPA), which extends the LeWorldModel framework by supplying the parameter governing the physics to the temporal model via action-conditioning and jointly training an encoder and predictor through an autoregressive latent rollout.

## 证据

In contrast to DINO-WM, SG-JEPA reduces open-loop prediction error by up to 2 times on two-dimensional datasets, and increases control success rate up to 2.5 times for three-dimensional robotic datasets, for which we train independent diffusion policies.


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Semigroup-JEPA Latent Dynamics Consistency for Zero-Shot Physics Generalization.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate physically realistic dynamics remains hitherto untested. In this work, we introduce SemiGroup-JEPA (SG-JEPA), which extends the LeWorldModel framework by supplying the parameter governing the physics to the temporal model via action-conditioning and jointly training an encoder and predictor through an autoregressive latent rollout. To evaluate the model's ability to generalize out of distribution, we design dynamical tasks under different gravitational fields that, despite obeying the same physical law, exhibit qualitatively different dynamics, ranging from floating motion in weak gravitational fields to rapid bouncing in strong ones. In contrast to DINO-WM, SG-JEPA reduces open-loop prediction error by up to 2 times on two-dimensional datasets, and increases control success rate up to 2.5 times for three-dimensional robotic datasets, for which we train independent diffusion policies. To explain this advantage, we develop a linear feature model that separates local law-conditioned error from its recursive amplification under rollout. Guided by this model, we find that back-propagating the multi-step rollout loss into the representation trains the encoder to keep the features that the predictor can carry forward, and that those are the features the dynamics depend on, so most of the gain comes from the encoder learning better features rather than from the predictor learning better dynamics. See project page at https://sg-jepa.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10464v1
- Authors: Andy Zeyi Liu, Haoran Sun, Lucas Baker, Randall Balestriero, John Sous
- Published: 2026-09-09T17:08:13Z
- Age days: 1

</details>
