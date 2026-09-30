---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10215v1"
published: "2026-09-09T14:15:11Z"
age_days: 1
score: 24
created: 2026-09-11
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Adaptive Shared Control with Online Bounded-Rational Human Behavior Estimation

> [!summary] 先说人话（基于摘要）
> The reported results show decreasing Kullback-Leibler divergence between the estimated and simulated human behavior distributions, and a lower accumulated running cost for the robot agent over the shared control interaction period, than the maximum-probabilit…

## 这篇到底在做什么

- **卡在哪里**：This work considers adaptive shared human-robot control for nonlinear control-affine systems, where the assumption of a fully rational human is relaxed and the robot adapts its assistance to observed boundedly rational human behavior.
- **关键解法**：We use a level-k bounded-rationality model of the two-player game to construct a finite bank of candidate human and robot policies through alternating best-response computations, with the associated value functions and policies approximated using adaptive dynamic programming.
- **拿什么证明**：The reported results show decreasing Kullback-Leibler divergence between the estimated and simulated human behavior distributions, and a lower accumulated running cost for the robot agent over the shared control interaction period, than the maximum-probability and probability-weighted alternative policies baseline.

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Adaptive Shared Control with Online Bounded-Rational Human Behavior Estimation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This work considers adaptive shared human-robot control for nonlinear control-affine systems, where the assumption of a fully rational human is relaxed and the robot adapts its assistance to observed boundedly rational human behavior. We use a level-k bounded-rationality model of the two-player game to construct a finite bank of candidate human and robot policies through alternating best-response computations, with the associated value functions and policies approximated using adaptive dynamic programming. During the shared-control interaction, state-transition residuals compare the measured system evolution with the trajectories predicted by the candidate human policies. The residuals are accumulated using a forgetting factor and mapped to a probabilistic human-behavior model over the finite candidate bank. Rather than selecting a single candidate or averaging stored robot policies, the robot computes a distribution-aware one-step best response by minimizing an expected cooperative cost over the complete estimated human behavior distribution. For a quadratic terminal-value approximation and Euler state propagation, this response admits a closed-form solution expressed in terms of the expected human input. The proposed methods are evaluated in simulations of a benchmark nonlinear system stabilization task, and of a planar manipulator shared control setup. The reported results show decreasing Kullback-Leibler divergence between the estimated and simulated human behavior distributions, and a lower accumulated running cost for the robot agent over the shared control interaction period, than the maximum-probability and probability-weighted alternative policies baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10215v1
- Authors: Henry Ascencio Trejo, Roel Pieters, Gokhan Alcan
- Published: 2026-09-09T14:15:11Z
- Age days: 1

</details>
