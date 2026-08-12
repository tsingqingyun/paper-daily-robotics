---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14188v1"
published: "2026-06-12T07:10:56Z"
age_days: 3
score: 23
created: 2026-06-16
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Robustness without Wrinkles: Parallel Simulation and Robust MPC for Certified Deformable Manipulation

> [!summary] 一句话结论（基于摘要）
> Across settings, CORD-SLS achieves millisecond-speed planning, exceeding baselines in safety, speed, and task success.

## 关键点

- **问题**：We present CORD-SLS, a real-time control method for safe deformable object manipulation, with a focus on ropes and cloth.
- **创新点 / 方法**：We present CORD-SLS, a real-time control method for safe deformable object manipulation, with a focus on ropes and cloth.
- **证据**：Across settings, CORD-SLS achieves millisecond-speed planning, exceeding baselines in safety, speed, and task success.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-16/Robustness without Wrinkles Parallel Simulation and Robust MPC for Certified Def.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present CORD-SLS, a real-time control method for safe deformable object manipulation,
with a focus on ropes and cloth. At its core is a GPU-parallel differentiable simulator
with contact smoothing which enables efficient gradient-based planning through
intermittent contact. To robustly satisfy constraints under model and sensing
uncertainty, we develop a real-time, GPU-parallel output-feedback robust model
predictive control (MPC) algorithm that plans with this simulator. We further show that
the simulator accelerates model-based RL for training neural manipulation policies. To
improve real-world robustness, we use conformal prediction to calibrate visual-feedback
and perception-error bounds for MPC, producing reachable tubes that enable high-
probability safe control. We evaluate CORD-SLS on high-dimensional, contact-rich rope
and cloth manipulation tasks in simulation and hardware, including obstacle avoidance,
routing, folding, and smoothing. Across settings, CORD-SLS achieves millisecond-speed
planning, exceeding baselines in safety, speed, and task success.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14188v1
- Authors: Wei-Chen Li, Jeffrey Fang, Sasanka Polisetti, Yuexi Song, Glen Chou
- Published: 2026-06-12T07:10:56Z
- Age days: 3

</details>
