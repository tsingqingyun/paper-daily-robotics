---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11525v1"
published: "2026-06-10T00:06:24Z"
age_days: 2
score: 34
created: 2026-06-12
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real"]
---

# Learning Object Manipulation from Scratch via Contrastive Interaction

> [!summary] 一句话结论（基于摘要）
> Across interaction-centric environments, including 2D dynamic control, robotic manipulation, and robot air hockey, IWR improves both sample efficiency and overall performance over prior CRL methods, with 19.8% average improvement in simulation.

## 关键点

- **问题**：However, despite its success in locomotion and simpler control domains, CRL often struggles in interaction-rich manipulation.
- **创新点 / 方法**：Based on this analysis, we introduce Interaction-weighted Resampling (IWR).
- **证据**：Across interaction-centric environments, including 2D dynamic control, robotic manipulation, and robot air hockey, IWR improves both sample efficiency and overall performance over prior CRL methods, with 19.8% average improvement in simulation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/Learning Object Manipulation from Scratch via Contrastive Interaction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contrastive Reinforcement Learning (CRL) has seen recent success in a wide variety of
goal-conditioned robotics tasks by learning structured representations of the dynamics.
However, despite its success in locomotion and simpler control domains, CRL often
struggles in interaction-rich manipulation. We argue that a key source of this
difficulty is object-centric interaction, such as contact or grasping, that induces
distinct changes in the underlying dynamic modes. In this work, we formulate
manipulation dynamics as a piecewise-smooth Markov process and show that interaction-
induced mode changes create piecewise nonlinear reachability structures that are
difficult for standard CRL energy functions to represent and plan over. Based on this
analysis, we introduce Interaction-weighted Resampling (IWR). IWR performs interaction-
aware resampling around phases before, during, and after interactions, encouraging the
learned representation to preserve the mode boundaries that determine future
reachability to capture multi-modal and piecewise nonlinear reachability. Across
interaction-centric environments, including 2D dynamic control, robotic manipulation,
and robot air hockey, IWR improves both sample efficiency and overall performance over
prior CRL methods, with 19.8% average improvement in simulation. Finally, using a sim-
to-real pipeline with policies trained by IWR, we demonstrate the first real-world goal-
conditioned robot air hockey agent capable of hitting goals, improving success from 25%
to 60%. Project Page: IWR-arxiv.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11525v1
- Authors: Tongle Shen, Caleb Chuck, Fan Feng, Biwei Huang
- Published: 2026-06-10T00:06:24Z
- Age days: 2

</details>
