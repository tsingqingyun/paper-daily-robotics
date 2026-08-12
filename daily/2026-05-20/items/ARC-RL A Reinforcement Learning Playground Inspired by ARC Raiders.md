---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19503v1"
published: "2026-05-19T07:54:40Z"
age_days: 0
score: 34
created: 2026-05-20
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# ARC-RL: A Reinforcement Learning Playground Inspired by ARC Raiders

> [!summary] 一句话结论（基于摘要）
> We introduce ARC-RL, a suite of four MuJoCo continuous-control environments featuring robotic morphologies inspired by the bestiary of ARC Raiders: the 18-DoF tall hexapod Queen, the 12-DoF armoured hexapod Bastion, the 18-DoF compact hexapod Tick, and the 12…

## 关键点

- **问题**：Game NPCs, however, are bound by stylistic constraints absent from sim-to-real robotics and routinely take the form of creatures with no real- robot counterpart.
- **创新点 / 方法**：We introduce ARC-RL, a suite of four MuJoCo continuous-control environments featuring robotic morphologies inspired by the bestiary of ARC Raiders: the 18-DoF tall hexapod Queen, the 12-DoF armoured hexapod Bastion, the 18-DoF compact hexapod Tick, and the 12-DoF quadruped Leaper.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning for legged locomotion has matured into a stack of multi-component
reward functions and physics-engine benchmarks whose morphologies are uniformly derived
from real commercial hardware. Game NPCs, however, are bound by stylistic constraints
absent from sim-to-real robotics and routinely take the form of creatures with no real-
robot counterpart. We introduce ARC-RL, a suite of four MuJoCo continuous-control
environments featuring robotic morphologies inspired by the bestiary of ARC Raiders: the
18-DoF tall hexapod Queen, the 12-DoF armoured hexapod Bastion, the 18-DoF compact
hexapod Tick, and the 12-DoF quadruped Leaper. All four robots share a unified
observation template, action convention, simulation cadence, and a single closed-form
multi-component reward function whose only per-morphology variation lives in a small set
of weights and parameters. The reward fuses a velocity-tracking tent, a healthy survive
bonus, a phase-locked gait-compliance bonus/cost pair, action regularisers, three safety
penalties, and a posture anchor; no motion-capture data enters the reward at any point.
We additionally provide hand-crafted Central Pattern Generator demonstrators per
morphology, which serve both as fixed expert references and as sources of prior data for
offline-to-online training. On this playground, we conduct a controlled empirical study
comparing standard online algorithms (SAC, SPEQ, SOPE-EO) and methods augmented with
prior data (SACfD, SPEQ-O2O, SOPE), and characterise how each paradigm copes with the
playground's morphological diversity and animation-style stylistic constraints.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19503v1
- Authors: Carlo Romeo, Andrew D. Bagdanov
- Published: 2026-05-19T07:54:40Z
- Age days: 0

</details>
