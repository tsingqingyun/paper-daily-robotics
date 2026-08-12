---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14617v1"
published: "2026-06-12T16:41:20Z"
age_days: 3
score: 21
created: 2026-06-16
concepts: ["世界模型"]
---

# Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms

> [!summary] 一句话结论（基于摘要）
> Existing whole-body control~(WBC) frameworks allocate the full joint space to locomotion or rely on fixed-gain impedance feedback that accumulates steady- state error under sustained physical human--robot interaction~(pHRI) forces.

## 关键点

- **问题**：Floating-base robots must balance under rigid contact constraints while interacting safely with humans.
- **创新点 / 方法**：Existing whole-body control~(WBC) frameworks allocate the full joint space to locomotion or rely on fixed-gain impedance feedback that accumulates steady- state error under sustained physical human--robot interaction~(pHRI) forces.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Floating-base robots must balance under rigid contact constraints while interacting
safely with humans. Existing whole-body control~(WBC) frameworks allocate the full joint
space to locomotion or rely on fixed-gain impedance feedback that accumulates steady-
state error under sustained physical human--robot interaction~(pHRI) forces. This paper
extends the authors' fixed-base two-layer Impedance MPC to floating-base platforms
through a three-level architecture: a centroidal MPC plans contact forces over a 500\,ms
horizon; a priority-driven WBC layer resolves balance into joint torques through
contact-consistent null-space projection; and the residual null space is governed by a
receding-horizon quadratic program~(QP) that predicts and rejects pHRI disturbances
using a Kalman-augmented state. A contact-consistent feedback linearization reduces the
arm end-effector plant to a double integrator with a \emph{constant} state matrix within
each contact mode, enabling offline precomputation of the QP cost and ${\geq}1$\,kHz
operation. A covariance-inflation protocol preserves the disturbance estimate across
contact-mode switches, guaranteeing zero steady-state error under bounded constant pHRI
loads, and an Impedance Equivalence Theorem shows the infinite-horizon limit recovers a
classical task-space impedance law whose effective mass, damping, and stiffness adapt to
posture and contact configuration. Simulations on a 17-DOF biped and the Unitree G1
humanoid validate the design.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14617v1
- Authors: Yongyan Cao
- Published: 2026-06-12T16:41:20Z
- Age days: 3

</details>
