---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18589v1"
published: "2026-06-17T01:28:07Z"
age_days: 1
score: 39
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# DREAM-Chunk: Reactive Action Chunking with Latent World Model

## 为什么重要

自动筛选分数：39

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Action chunking has become a common interface for vision-language-action (VLA) models,
enabling low-frequency policy inference to drive high-frequency robot execution.
However, once an action chunk is committed, its open-loop execution can be brittle under
stochastic dynamics, hardware execution errors, and partial observability. We propose
DREAM-Chunk, a test-time scaling method that augments chunking-based policies with a
lightweight latent world model, without requiring additional policy fine-tuning. At test
time, DREAM-Chunk samples multiple candidate action chunks, rolls out their predicted
latent futures, and selects actions from the chunk whose predicted state best matches
the observed rollout. In this way, DREAM-Chunk uses additional test-time computation to
cover multiple plausible stochastic futures and improve reactivity during long-horizon
chunk execution. On the Kinetix benchmark, DREAM-Chunk improves robustness under
increasing action noise and benefits from larger candidate sample sizes, especially when
demonstrations contain corrective behaviors. We further validate DREAM-Chunk on four
manipulation tasks across two robot platforms and two VLA policies under various sources
of stochasticity. Across simulation and hardware experiments, DREAM-Chunk improves the
robustness of action-chunking policies in stochastic dynamics.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18589v1
- Authors: Wenxi Chen, Kaidi Zhang, Chi Lin, Zhiyuan Zhang, Yu She, Yuejiang Liu, Raymond A. Yeh, Shaoshuai Mou, Yan Gu
- Published: 2026-06-17T01:28:07Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
