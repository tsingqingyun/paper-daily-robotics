---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06650v1"
published: "2026-08-06T23:31:47Z"
age_days: 3
score: 24
created: 2026-08-10
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# SoRoMoX: Fast, Differentiable, and Parallelizable Soft Robot Models

> [!summary] 一句话结论（基于摘要）
> Their implementations, however, do not support the differentiable, GPU-parallel, and control-oriented workflows that underpin advanced rigid-robotics applications.

## 关键点

- **问题**：Reduced-order models based on Cosserat-rod theory are now well established, and modeling theory is no longer the primary bottleneck in soft-robot control.
- **创新点 / 方法**：Their implementations, however, do not support the differentiable, GPU-parallel, and control-oriented workflows that underpin advanced rigid-robotics applications.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/SoRoMoX Fast, Differentiable, and Parallelizable Soft Robot Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reduced-order models based on Cosserat-rod theory are now well established, and modeling
theory is no longer the primary bottleneck in soft-robot control. Their implementations,
however, do not support the differentiable, GPU-parallel, and control-oriented workflows
that underpin advanced rigid-robotics applications. Here, we fill this gap with SoRoMoX
(Soft Robot Models in JAX), a fully numerical, JIT-compilable Python/JAX framework.
SoRoMoX implements articulated, Piecewise Constant Strain, and Variable Strain models
through a unified, control-ready interface that provides inertia matrices, gravitational
and elastic forces, Jacobians, and their derivatives. To our knowledge, it is the first
rod/strain-based soft-robot modeling framework that runs directly on GPUs and is end-to-
end differentiable with respect to states, inputs, and parameters. Sequential CPU
rollouts are up to 18.1x faster than state-of-the-art alternatives, while GPU-parallel
rollouts increase throughput by up to 234.6x. This performance enables workflows that
were previously impractical or impossible: static-equilibrium system identification with
66% lower marker RMSE; residual-force learning with a further 64% reduction; computed-
torque tracking with RMSE reduced by a factor of approximately 500 relative to model-
free PD; control-gain optimization with up to 62% lower loss than untuned gains; safety-
constrained control using high-order control barrier functions to keep the peak contact
force within a prescribed 5 N bound, compared with 33.5 N without the safety constraint;
and reinforcement-learning policy training up to 7x faster than a CPU PyElastica
discrete-rod baseline through massively parallel rollouts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06650v1
- Authors: Maximilian Stölzle, Solange Gribonval, Daniel Feliu-Talegon, Vito Daniele Perfetta, Michele Martini, Chuhan Zhang, Kiwan Wong, Mohammed Tarnini, Anup Teejo Mathew, Federico Renda, Daniela Rus, Cosimo Della Santina
- Published: 2026-08-06T23:31:47Z
- Age days: 3

</details>
