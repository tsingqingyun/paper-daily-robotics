---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10927v1"
published: "2026-06-09T14:35:53Z"
age_days: 0
score: 34
created: 2026-06-10
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Experiments in both synthetic and real-world environments across cross-room, cross-episode, and cross-task scenarios show that AllDayNav achieves success rates approaching $100\%$ and consistently surpasses strong map-based, VLM, and RL baselines in path effi…

## 关键点

- **问题**：Lifelong embodied navigation in dynamic environments requires robots to form persistent scene understanding from fragmentary observations, which remains difficult for existing methods that rely on explicit maps or scene graphs and struggle to generalize beyond structured settings.
- **创新点 / 方法**：We propose AllDayNav, a lifelong self-learning navigation framework that implicitly encodes scene dynamics into the billion-scale parameters of a large model via reinforcement learning, powered by a self-evolving multimodal memory that maintains and updates visual keyframes, semantic descriptions, and temporal context…
- **证据**：Experiments in both synthetic and real-world environments across cross-room, cross-episode, and cross-task scenarios show that AllDayNav achieves success rates approaching $100\%$ and consistently surpasses strong map-based, VLM, and RL baselines in path efficiency and robustness, demonstrating implicit, memory-driven…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/AllDayNav Lifelong Navigation via Real-World Reinforcement Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Lifelong embodied navigation in dynamic environments requires robots to form persistent
scene understanding from fragmentary observations, which remains difficult for existing
methods that rely on explicit maps or scene graphs and struggle to generalize beyond
structured settings. We propose AllDayNav, a lifelong self-learning navigation framework
that implicitly encodes scene dynamics into the billion-scale parameters of a large
model via reinforcement learning, powered by a self-evolving multimodal memory that
maintains and updates visual keyframes, semantic descriptions, and temporal context
while autonomously generating open-vocabulary instructions, image goals, and structured
rewards. Experiments in both synthetic and real-world environments across cross-room,
cross-episode, and cross-task scenarios show that AllDayNav achieves success rates
approaching $100\%$ and consistently surpasses strong map-based, VLM, and RL baselines
in path efficiency and robustness, demonstrating implicit, memory-driven reinforcement
learning as a scalable alternative to explicit mapping for reliable lifelong navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10927v1
- Authors: Hang Yin, Yinan Liang, Jiazhao Zhang, Jiahang Liu, Minghan Li, Zhizheng Zhang, He Wang
- Published: 2026-06-09T14:35:53Z
- Age days: 0

</details>
