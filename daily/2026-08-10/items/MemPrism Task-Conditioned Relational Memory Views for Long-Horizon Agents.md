---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06745v1"
published: "2026-08-07T03:13:43Z"
age_days: 3
score: 24
created: 2026-08-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents

## 为什么重要

自动筛选分数：24

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Long-horizon agents rely on memory to reuse experiences, yet existing memory systems
often assume that evidence can be directly consumed through a fixed representation. This
leads to representation mismatch, where relevant information is available but not
organized for the current decision. To this end, we propose MemPrism, a task-conditioned
relational memory framework that separates persistent experience storage from decision-
time working memory. MemPrism records interactions as the event stream and dynamically
constructs relational views according to the current task context. A lightweight view
policy selects the relation structure, evidence range, outcome condition, and
granularity, while a deterministic composer and render transform historical facts into a
temporary optical working-memory view for a frozen task policy. Experiments on long-
horizon embodied and web-agent benchmarks show that MemPrism consistently improves the
task performance, especially as trajectories become longer, while reducing memory token
consumption. Furthermore, the learned view policy transfers across different VLMs
without additional adaptation, demonstrating the effectiveness of task-conditioned
relational views as a general memory interface for agents.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06745v1
- Authors: Zhisheng Chen, Bingfan Zeng, Bangde Cao, Zhengwei Xie, Yuxuan Li, Jinhan Li, Zheng Lu, Xiangchen Guan, Zikai Xiao, Rui Qian, Jingwei Song
- Published: 2026-08-07T03:13:43Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
