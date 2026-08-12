---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18729v1"
published: "2026-05-18T17:52:14Z"
age_days: 1
score: 35
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18729v1
- Authors: Nga Teng Chan, Yi Zhang, Yechi Liu, Renwen Cui, Fanhu Zeng, Zeyuan Ding, Xiancong Ren, Zhang Zhang, Qifeng Chen, Jian Liu, Yong Dai, Xiaozhu Ju
- Published: 2026-05-18T17:52:14Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
