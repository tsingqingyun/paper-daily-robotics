---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30111v1"
published: "2026-06-29T10:45:37Z"
age_days: 1
score: 29
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent"]
---

# Automating the Design of Embodied AgentArchitectures

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[智能体 Agent]]

## 摘要

Embodied agents are typically built as hand-designed compositions of perception, memory,
planning, and action modules. This modularity exposes a large architectural design
space, but current systems still rely on researcher intuition to choose where
information is stored, how observations are processed, and how model calls are
connected. Agent Architecture Search (AAS) automates such design for text-domain agents,
but has not been systematically evaluated on perceptual embodied agents through
simulator rollouts. We study this transfer. We introduce AgentCanvas, a typed-graph
runtime that hosts embodied executors as editable node-and-wire programs with simulator-
aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that
cycles through proposal, critique, experiment, and distillation, with triggered
reflection after stalls. We evaluate three AAS variants across four embodied executors
spanning vision-language navigation, embodied question answering, and language-
conditioned manipulation. The resulting 3x4 matrix shows that architecture-level search
can produce deployable and directional success-rate gains on embodied tasks, while one
apparent high-scoring candidate is rejected as leak-bearing. At the same time, the
experiments expose constraints that are muted in text-domain AAS: optimization signals
can be masked by rollout noise, search can become trapped in local edit basins, and
episode-level credit assignment only partially emerges even when detailed logs are
available. These results characterize both the promise and the current limits of
automated architecture search for embodied agents.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30111v1
- Authors: Jian Zhou, Sihao Lin, Jin Li, Shuai Fu, Gengze Zhou, Qi Wu
- Published: 2026-06-29T10:45:37Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
