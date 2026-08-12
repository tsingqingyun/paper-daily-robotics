---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18729v1"
published: "2026-05-18T17:52:14Z"
age_days: 1
score: 35
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction

> [!summary] 一句话结论（基于摘要）
> Extensive evaluations on IGNav, AR, and AEQA show that Robo-Cortex consistently outperforms strong baselines in both task success and exploration efficiency, with gains of up to +4.16% SPL over the strongest prior method and up to +15.30% SPL under heuristic…

## 关键点

- **问题**：The ability to navigate and interact with complex environments is central to real-world embodied agents, yet navigation in unseen environments remains challenging due to "experiential amnesia," where existing trajectory-driven or reactive policies fail to synthesize generalizable strategies from past interactions.
- **创新点 / 方法**：We propose Robo-Cortex, a self-evolving framework that enables robots to autonomously induce navigation heuristics and refine cognitive strategies through a continuous reflection-adaptation loop.
- **证据**：Extensive evaluations on IGNav, AR, and AEQA show that Robo-Cortex consistently outperforms strong baselines in both task success and exploration efficiency, with gains of up to +4.16% SPL over the strongest prior method and up to +15.30% SPL under heuristic transfer to unseen environments.
- **局限**：The ability to navigate and interact with complex environments is central to real-world embodied agents, yet navigation in unseen environments remains challenging due to "experiential amnesia," where existing trajectory-driven or reactive policies fail to synthesize generalizable strategies from past interactions.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The ability to navigate and interact with complex environments is central to real-world
embodied agents, yet navigation in unseen environments remains challenging due to
"experiential amnesia," where existing trajectory-driven or reactive policies fail to
synthesize generalizable strategies from past interactions. We propose Robo-Cortex, a
self-evolving framework that enables robots to autonomously induce navigation heuristics
and refine cognitive strategies through a continuous reflection-adaptation loop. By
abstracting success patterns and failure pitfalls into natural-language heuristics,
Robo-Cortex enables a transition from passive execution to active strategy evolution.
Our core innovation is an Autonomous Knowledge Induction (AKI) mechanism that distills
multimodal trajectories into a structured Navigation Heuristic Library for knowledge
generalization. The architecture further incorporates a Dual-Grain Cognitive Memory
system, comprising a Short-term Reflective Memory (SRM) for real-time local progress
analysis, and a Long-term Principle Memory (LPM) that abstracts past trajectories into
reusable guiding and cautionary principles. To ensure robust decision-making, we
introduce a multimodal Imagine-then-Verify loop, where a world model simulates potential
outcomes and a VLM-based evaluator validates action plans. Extensive evaluations on
IGNav, AR, and AEQA show that Robo-Cortex consistently outperforms strong baselines in
both task success and exploration efficiency, with gains of up to +4.16% SPL over the
strongest prior method and up to +15.30% SPL under heuristic transfer to unseen
environments. Preliminary real-world robotic experiments further support the
effectiveness of Robo-Cortex in physical settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18729v1
- Authors: Nga Teng Chan, Yi Zhang, Yechi Liu, Renwen Cui, Fanhu Zeng, Zeyuan Ding, Xiancong Ren, Zhang Zhang, Qifeng Chen, Jian Liu, Yong Dai, Xiaozhu Ju
- Published: 2026-05-18T17:52:14Z
- Age days: 1

</details>
