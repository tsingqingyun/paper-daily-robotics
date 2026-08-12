---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07389v1"
published: "2026-06-05T15:26:26Z"
age_days: 2
score: 30
created: 2026-06-08
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthetic Grasping

> [!summary] 一句话结论（基于摘要）
> In three realistic settings, the learned sim- to-real policy achieves over 90\% grasp success, surpasses baseline methods, and exhibits stronger generalization, highlighting the promise of simulation-driven training for biosignals-free shared-autonomy prosthe…

## 关键点

- **问题**：Recent imitation-learning-based approaches have shown promising results, but their scalability is limited by the cost and variability of collecting large amounts of real-world human demonstration data.
- **创新点 / 方法**：In this work, we present a scalable simulation framework that automatically generates diverse reach-to-grasp demonstrations from a wrist-mounted virtual camera.
- **证据**：In three realistic settings, the learned sim- to-real policy achieves over 90\% grasp success, surpasses baseline methods, and exhibits stronger generalization, highlighting the promise of simulation-driven training for biosignals-free shared-autonomy prosthetic grasping.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthe.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Biosignals-free shared-autonomy control of upper-limb prosthetic hands aims to enable
natural and low-effort manipulation without relying on EMG or other physiological
signals. Recent imitation-learning-based approaches have shown promising results, but
their scalability is limited by the cost and variability of collecting large amounts of
real-world human demonstration data. In this work, we present a scalable simulation
framework that automatically generates diverse reach-to-grasp demonstrations from a
wrist-mounted virtual camera. The framework combines physically feasible grasp
synthesis, natural reaching trajectories retargeting, and reach--grasp--lift execution
in procedurally generated indoor environments. It records wrist-view observations,
proprioception, and actions to build a large-scale demonstration dataset for imitation
learning. Through extensive simulation benchmarks, we evaluate object and scene
generalization and compare several representative state-of-the-art imitation learning
methods. Results show that the simulated demonstrations are sufficiently rich and
consistent for effective policy learning. In three realistic settings, the learned sim-
to-real policy achieves over 90\% grasp success, surpasses baseline methods, and
exhibits stronger generalization, highlighting the promise of simulation-driven training
for biosignals-free shared-autonomy prosthetic grasping. The demonstrations are
available at \href{https://sites.google.com/view/sim-prosthetic-
grasp/home}{https://sites.google.com/view/sim-prosthetic-grasp/home}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07389v1
- Authors: Kaijie Shi, Wanglong Lu, Huiling Chen, Vinicius Prado da Fonseca, Ting Zou, Hanli Zhao, Xianta Jiang
- Published: 2026-06-05T15:26:26Z
- Age days: 2

</details>
