---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00808v1"
published: "2026-07-01T11:36:27Z"
age_days: 4
score: 26
created: 2026-07-06
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos

> [!summary] 一句话结论（基于摘要）
> Building on this insight, we propose a novel Deconstruct- Recompose Paradigm (DRP) for learning transferable local motion representations.

## 关键点

- **问题**：Pre-training on large-scale videos to improve reinforcement learning efficiency is promising yet remains challenging.
- **创新点 / 方法**：Building on this insight, we propose a novel Deconstruct- Recompose Paradigm (DRP) for learning transferable local motion representations.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Pre-training on large-scale videos to improve reinforcement learning efficiency is promising yet remains challenging.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-06/Local Motion Matters A Deconstruct-Recompose Paradigm for Reinforcement Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pre-training on large-scale videos to improve reinforcement learning efficiency is
promising yet remains challenging. Existing methods typically treat the agent as an
indivisible entity, modeling motion patterns globally. Such global modeling is tightly
coupled with the morphology, hindering transfer across domains. In contrast, despite the
vast disparity in global motions, the local components exhibit similar motion patterns
across different agents. Building on this insight, we propose a novel Deconstruct-
Recompose Paradigm (DRP) for learning transferable local motion representations.
Specifically, in the Deconstruct phase, we identify multiple local points and track
their frame-wise motions, defining each as an Atomic Action. We introduce a Dual-
Attention Encoder (DAE) to learn local motion representations from these Atomic Actions,
capturing their spatiotemporal relationships. In the Recompose phase, we compose local
motion representations with a learnable Motion Aggregation Token [MAT] via latent
dynamics model learning. Additionally, an adapter bridges local motion and downstream
action-specific dynamics to accelerate policy learning. Extensive experiments
demonstrate that our method effectively transfers to diverse robotic control and
manipulation tasks, significantly improving sample efficiency and performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00808v1
- Authors: Jinwen Wang, Youfang Lin, Xiaobo Hu, Shuo Wang, Kai Lv
- Published: 2026-07-01T11:36:27Z
- Age days: 4

</details>
