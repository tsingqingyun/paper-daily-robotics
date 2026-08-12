---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09857v1"
published: "2026-08-10T17:15:55Z"
age_days: 1
score: 27
created: 2026-08-12
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy

## 为什么重要

自动筛选分数：27

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Advances in advanced artificial intelligence tools have sparked research in robot
autonomy, but the development of such systems has largely focused on execution rather
than verifying the feasibility actions planning models propose. Like general-purpose
LLMs, robotics planning models carry risks: biased toward user-specified goals, they may
suggest actions misaligned with scientific ethics, they may be unsafe due to an
inability to "remember" prior safety risks, or they may be vulnerable to adversarial
attacks on the autonomy ecosystem. We propose a LLM-driven verification layer between
planning and execution to evaluate action permissibility. Our LLM-as-a-Judge ensemble
combines chain-of-thought reasoning across models and synthesizes those expert judge
outputs, mirroring a combination of a mixture of experts and self-consistency approach.
This layer serves as middleware, gating plans from the server's planning module before
they reach the MCP server and therefore the robot's low-level controls: plans are
approved, rejected for reformulation, or escalated for human review. With this system,
we achieve near 85% precision across accept/escalate/reject categories 97% containment
of adversarial attacks, with negligible errors between accepting and rejecting tasks,
and errors mostly manifesting at the escalate boundary.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09857v1
- Authors: Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai
- Published: 2026-08-10T17:15:55Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
