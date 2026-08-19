---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17584v1"
published: "2026-08-18T09:49:16Z"
age_days: 0
score: 31
created: 2026-08-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction

> [!summary] 一句话结论（基于摘要）
> In an interactive simulation with 164 cases, HODAgent achieves 84.8% and 91.5% Joint Success under two VLM backbones, outperforming baselines by 9.8 and 18.9 points.

## 关键点

- **问题**：We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification.
- **创新点 / 方法**：We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification.
- **证据**：In an interactive simulation with 164 cases, HODAgent achieves 84.8% and 91.5% Joint Success under two VLM backbones, outperforming baselines by 9.8 and 18.9 points.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/HODAgent Towards On-Demand, Responsive Humanoids for Physical World Human Intera.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor, Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes. This allows handling new requests during motion, retaining progress, revising actions, and grounding closure in execution outcomes. A shared interface connects simulation and physical robots (Unitree G1), isolating platform-specific control. In an interactive simulation with 164 cases, HODAgent achieves 84.8% and 91.5% Joint Success under two VLM backbones, outperforming baselines by 9.8 and 18.9 points. On physical robots, pass rates are 92% (atomic), 72% (composite), and 63.3% (complete tasks). On multiple embodied benchmarks, it improves over baselines by 0.7-9.0 points. Results show a unified System-2 agent enables adaptive humanoid service across simulation and reality.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17584v1
- Authors: Wang Warren Chen, Jiahao Zhang, Zhenjiang Li, Mingxu Wang, Lei Yi, Yuchen Kang, Shuo Sun, Ziping Chen, Jie Chen
- Published: 2026-08-18T09:49:16Z
- Age days: 0

</details>
