---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13451v1"
published: "2026-07-15T05:15:43Z"
age_days: 1
score: 29
created: 2026-07-17
concepts: ["智能体 Agent", "世界模型"]
---

# Learning Physics-Guided Residual Dynamics for Deformable Object Simulation

> [!summary] 一句话结论（基于摘要）
> We show that PGRD produces more accurate results than both purely physics-based and learning-based methods on a set of diverse real-world deformable objects.

## 关键点

- **问题**：Simulating deformable objects is essential for a wide range of robotic manipulation applications, yet accurately predicting their dynamics remains challenging.
- **创新点 / 方法**：We propose Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the advantages of physics-based and learning-based approaches.
- **证据**：We show that PGRD produces more accurate results than both purely physics-based and learning-based methods on a set of diverse real-world deformable objects.
- **局限**：Simulating deformable objects is essential for a wide range of robotic manipulation applications, yet accurately predicting their dynamics remains challenging.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Simulating deformable objects is essential for a wide range of robotic manipulation
applications, yet accurately predicting their dynamics remains challenging. We propose
Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the
advantages of physics-based and learning-based approaches. Specifically, PGRD combines
an optimizable spring-mass simulator as a backbone with a learned neural network that
predicts residual corrections to the physics-based predictions. We adopt a velocity-
based formulation to ensure stable simulation and a sliding-window transformer
architecture to capture temporal dependencies. We show that PGRD produces more accurate
results than both purely physics-based and learning-based methods on a set of diverse
real-world deformable objects. We further demonstrate the utility of PGRD in two
applications: manipulation planning via Model Predictive Control, including a language-
conditioned setting with a generated goal image; and interactive simulation via action-
conditioned video prediction by 3D Gaussian Splatting.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13451v1
- Authors: Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li
- Published: 2026-07-15T05:15:43Z
- Age days: 1

</details>
