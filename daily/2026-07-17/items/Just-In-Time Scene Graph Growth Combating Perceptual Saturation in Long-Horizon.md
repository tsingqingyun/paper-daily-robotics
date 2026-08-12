---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13245v1"
published: "2026-07-14T20:14:50Z"
age_days: 2
score: 29
created: 2026-07-17
concepts: ["智能体 Agent"]
---

# Just-In-Time Scene Graph Growth: Combating Perceptual Saturation in Long-Horizon Robotics

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]]

## 摘要

While 3D Scene Graphs (3DSGs) provide crucial structured representations for embodied
agents, conventional Ahead-of-Time, build-everything-then-filter pipelines conflict with
the real-time, low-latency demands of edge platforms, inducing a perceptual saturation
effect via severe observation redundancy. To resolve this, we present JITOMA (Just-In-
Time On-demand Memory Activation), a closed-loop framework that unifies task reasoning,
perception, and memory into a just-in-time growth process. Instead of exhaustively
mapping the entire environment, JITOMA leverages a top-down task heatmap at the frontend
to filter continuous observations, routing minimal streams to maintain a global
foundation of low-cost, dormant anchors. Upon a cognitive query, the backend Large
Language Model (LLM) parses the robotic intent to dynamically awaken task-relevant
anchors, triggering resource-intensive operations -- such as dense node captioning and
functional inference -- exclusively within the activated local subgraph. To evaluate
these dynamic capabilities and study perceptual saturation trade-offs, we introduce
JITOMA-Bench, a comprehensive suite for long-horizon multi-tasking and complex multi-
step reasoning. Extensive experiments demonstrate that JITOMA substantially reduces
active graph size and captioning latency, while maintaining stable processing time under
long-horizon task switching.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13245v1
- Authors: Yue Chang, Rufeng Chen, Yifan Tian, Dazhi Huang, Zhaofan Zhang, Yi Chen, Wenze Zhang, Li Chen, Hui Xiong, Sihong Xie
- Published: 2026-07-14T20:14:50Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
