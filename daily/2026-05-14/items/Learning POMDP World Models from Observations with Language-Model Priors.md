---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13740v1"
published: "2026-05-13T16:18:15Z"
age_days: 0
score: 29
created: 2026-05-14
concepts: ["智能体 Agent", "世界模型"]
---

# Learning POMDP World Models from Observations with Language-Model Priors

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Whether navigating a building, operating a robot, or playing a game, an agent that acts
effectively in an environment must first learn an internal model of how that environment
works. Partially-observable Markov decision processes (POMDPs) provide a flexible
modeling class for such internal world models, but learning them from observation-action
trajectories alone is challenging and typically requires extensive environment
interaction. We ask whether language-model priors can reduce costly interaction by
leveraging prior knowledge, and introduce \emph{Pinductor} (POMDP-inductor): an LLM
proposes candidate POMDP models from a few observation-action trajectories and
iteratively refines them to optimize a belief-based likelihood score. Despite using
strictly less information, \emph{Pinductor} matches the performance and sample
efficiency of LLM-based POMDP learning methods that assume privileged access to the
hidden state, while significantly surpassing the sample efficiency of tabular POMDP
baselines. Further results show that performance scales with LLM capability and degrades
gracefully as semantic information about the environment is withheld. Together, these
results position language-model priors as a practical tool for sample-efficient world-
model learning under partial observability, and a step toward generalist agents in real-
world environments. Code is available at https://github.com/atomresearch/pinductor.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13740v1
- Authors: Valentin Six, Frederik Panse, Mathis Fajeau, Lancelot Da Costa, Mridul Sharma, Alfonso Amayuelas, Tim Z. Xiao, David Hyland, Philipp Hennig, Bernhard Schölkopf
- Published: 2026-05-13T16:18:15Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
