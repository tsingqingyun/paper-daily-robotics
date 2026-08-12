---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13817v1"
published: "2026-06-11T18:46:43Z"
age_days: 3
score: 29
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift

> [!summary] 一句话结论（基于摘要）
> In simulated aquatic surface-vehicle environments with diverse hidden flows, disturbances, and randomized vehicle dynamics, FlowMo-WM improves long-horizon rollout accuracy over representative action-conditioned latent world models.

## 关键点

- **问题**：However, many action-conditioned models are evaluated in settings where motion is dominated by immediate control, whereas aquatic surface vehicles and other real-world objects continue moving under inertia and are displaced by hidden ambient drift, such as water currents or wind.
- **创新点 / 方法**：We propose FlowMo-WM, an end-to-end trainable visual world model that infers object-centric motion state and a predictive long-history context associated with hidden drift from image-action histories without direct supervision of flow fields.
- **证据**：In simulated aquatic surface-vehicle environments with diverse hidden flows, disturbances, and randomized vehicle dynamics, FlowMo-WM improves long-horizon rollout accuracy over representative action-conditioned latent world models.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/FlowMo-WM A World Model with Object Momentum and Hidden Ambient Drift.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models in robot learning predict future states from visual observations and
actions, enabling agents to reason about the consequences of their controls. However,
many action-conditioned models are evaluated in settings where motion is dominated by
immediate control, whereas aquatic surface vehicles and other real-world objects
continue moving under inertia and are displaced by hidden ambient drift, such as water
currents or wind. We propose FlowMo-WM, an end-to-end trainable visual world model that
infers object-centric motion state and a predictive long-history context associated with
hidden drift from image-action histories without direct supervision of flow fields.
FlowMo-WM factorizes image-action history into a short-history latent state, trained to
summarize object-centric motion, and a longer-history context, trained to summarize
slowly varying exogenous influences. A zero-context residual transition separates
action-conditioned base dynamics from context-dependent drift effects during latent
rollout. In simulated aquatic surface-vehicle environments with diverse hidden flows,
disturbances, and randomized vehicle dynamics, FlowMo-WM improves long-horizon rollout
accuracy over representative action-conditioned latent world models. Prediction-time
context ablations, in which the inferred context is zeroed or shuffled during rollout,
show that the ambient context is important for stable prediction under hidden drift,
while frozen linear probes characterize information encoded in the learned factors.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13817v1
- Authors: Yitao Jiang, Luyang Zhao, Muhao Chen, Devin Balkcom
- Published: 2026-06-11T18:46:43Z
- Age days: 3

</details>
