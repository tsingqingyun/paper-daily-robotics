---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12920v1"
published: "2026-05-13T02:48:14Z"
age_days: 1
score: 36
created: 2026-05-14
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue

## 为什么重要

自动筛选分数：36

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Effective collaboration between embodied agents requires more than acting in a shared
environment; it demands communication grounded in each agent's evolving understanding of
the world. When agents can only partially observe their surroundings, coordination
without communication is provably hard, but communication can, in principle, bridge this
gap by allowing agents to share observations and align their world models. In this work,
we examine whether LLM-based embodied agents actually realize the ability to
communicate. We extend PARTNR, a benchmark for collaborative household robotics, with a
natural-language dialogue channel that enables two agents with partial observability to
communicate during task execution. To evaluate whether dialogue leads to genuine world-
model alignment rather than superficial coordination, we propose a framework for
measuring world-model alignment defined over per-agent world graphs: observation
convergence (do private world models align over time?), information novelty (do messages
convey what the partner lacks?), and belief-sensitive messaging (do agents model what
their partner knows?). Our experiments across three LLMs reveal that dialogue reduces
action conflicts 40 to 83 percentage points but degrades task success relative to silent
coordination. Using our metrics, we characterize the gap between superficial
coordination and genuine world-model alignment, and identify where current models fall
on this spectrum.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12920v1
- Authors: Vardhan Dongre, Dilek Hakkani-Tür
- Published: 2026-05-13T02:48:14Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
