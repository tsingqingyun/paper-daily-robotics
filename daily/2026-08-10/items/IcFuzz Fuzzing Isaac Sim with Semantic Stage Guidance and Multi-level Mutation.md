---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06088v1"
published: "2026-08-06T14:29:05Z"
age_days: 3
score: 27
created: 2026-08-10
concepts: ["世界模型"]
---

# IcFuzz: Fuzzing Isaac Sim with Semantic Stage Guidance and Multi-level Mutation

## 为什么重要

自动筛选分数：27

连接概念：[[世界模型]]

## 摘要

Robotics simulators serve as a foundational infrastructure for embodied AI, facilitating
safe and scalable robotic system development. NVIDIA Isaac Sim has emerged as one of the
most popular simulators, distinguished by its GPU-accelerated physics engine and
photorealistic rendering, which enable high-fidelity modeling of complex environments.
However, its inherent complexity inevitably introduces software bugs that can compromise
simulation reliability. Existing fuzzing approaches struggle to test Isaac Sim
effectively due to challenges of context-aware object semantics, hierarchical simulation
control, and a vast simulation state space. In this paper, we propose IcFuzz, the first
fuzzing approach for Isaac Sim. IcFuzz first performs an LLM-based semantic stage
segmentation, decomposing simulation programs into structured stages that capture
context-aware object semantics. Guided by this information, IcFuzz designs multi-level
mutation operators to systematically exercise the simulator across hierarchical
granularities. To efficiently navigate the vast simulation state space, IcFuzz employs a
multi-armed bandit algorithm to adaptively schedule mutation operators. Experimental
results show that IcFuzz outperforms the baselines in terms of both code coverage and
bug detection. Specifically, IcFuzz achieves approximately 190\%--205\% of the code
coverage of the baselines and detects an average of 3.7 unique crashes over three rounds
of 12-hour tests, while no crashes are detected by the baselines. Moreover, IcFuzz has
uncovered 11 bugs over approximately four months, 9 of which have been confirmed or
fixed by the developers.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06088v1
- Authors: Zhixiang Chen, Zhuangbin Chen, Ruoxi Jia, Zeqin Liao, Wei Li, Jinyang Liu, Zibin Zheng
- Published: 2026-08-06T14:29:05Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
