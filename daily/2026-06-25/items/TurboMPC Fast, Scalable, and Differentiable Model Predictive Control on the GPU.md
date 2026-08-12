---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24039v1"
published: "2026-06-23T00:42:33Z"
age_days: 1
score: 32
created: 2026-06-25
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU

> [!summary] 一句话结论（基于摘要）
> We present TurboMPC, a differentiable MPC solver that runs entirely on the GPU and supports state and control inequality constraints, implicit integrators, cross-time-coupled costs, and slack variables.

## 关键点

- **问题**：For model predictive control (MPC) to scale with this paradigm, solvers must run efficiently on this hardware while remaining fast, differentiable, and compatible with expressive MPC formulations used in robotics.
- **创新点 / 方法**：We present TurboMPC, a differentiable MPC solver that runs entirely on the GPU and supports state and control inequality constraints, implicit integrators, cross-time-coupled costs, and slack variables.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/TurboMPC Fast, Scalable, and Differentiable Model Predictive Control on the GPU.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotics increasingly relies on GPUs for parallel simulation, large-scale learning, and
neural-network inference. For model predictive control (MPC) to scale with this
paradigm, solvers must run efficiently on this hardware while remaining fast,
differentiable, and compatible with expressive MPC formulations used in robotics. We
present TurboMPC, a differentiable MPC solver that runs entirely on the GPU and supports
state and control inequality constraints, implicit integrators, cross-time-coupled
costs, and slack variables. TurboMPC combines sequential quadratic programming (SQP), an
alternating direction method of multipliers (ADMM) inner solver, implicit
differentiation, and a co-designed JAX-CUDA implementation for efficiency and ease of
use. In simulation, we validate TurboMPC on constrained planning, humanoid imitation
learning, and reinforcement learning with neural-network cost function tasks, achieving
up to $15\times$ and $58\times$ speedups over state-of-the-art CPU and GPU
differentiable solvers, respectively. We deploy TurboMPC on a full-scale car for
minimum-time racing and find that batched, GPU-accelerated tuning of MPC parameters via
Bayesian optimization yields significantly faster driving than a hand-tuned baseline.
TurboMPC also scales to planning horizons of over $8000$ knot points while maintaining
control of the vehicle. We open-source TurboMPC at:
https://github.com/ToyotaResearchInstitute/turbompc

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24039v1
- Authors: Gabriel Bravo-Palacios, Jianghan Zhang, Zachary Pestrikov, Brian Plancher, Thomas Lew
- Published: 2026-06-23T00:42:33Z
- Age days: 1

</details>
