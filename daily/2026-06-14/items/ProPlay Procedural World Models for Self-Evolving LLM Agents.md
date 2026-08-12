---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12780v1"
published: "2026-06-11T00:47:37Z"
age_days: 3
score: 25
created: 2026-06-14
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ProPlay: Procedural World Models for Self-Evolving LLM Agents

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Self-evolving agents are expected to improve through interaction without external
supervision, but this remains difficult in partially observable environments where
agents must explore actively, learn from limited feedback, and decide when to trust
prior experience. Existing LLM-agent methods often rely on memory or planning modules,
yet they rarely close the loop between them to continually refine an internal
understanding of environment dynamics. We introduce ProPlay, a procedural world model
that supports procedure-level preplay, where agents can rehearse future procedural paths
using the learned world knowledge. Rather than representing experience as isolated rules
or low-level action constraints, ProPlay abstracts successful trajectories into
procedures and organizes them in a procedure graph that captures causal transitions
among task stages. Each transition is associated with a reliability record embedding to
estimate its task-specific contribution from past outcomes. Before each episode, ProPlay
simulates future procedural trajectories over known graph structures as structured soft
guidance; after execution, it refines the graph using environment feedback. Experiments
on public benchmarks show that ProPlay consistently improves environment understanding
and self-evolution capability over strong baselines. Our code has been released in
https://github.com/antman9914/proplay.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12780v1
- Authors: Yijun Ma, Zehong Wang, Yiyang Li, Ziming Li, Xiaoguang Guo, Weixiang Sun, Chuxu Zhang, Yanfang Ye
- Published: 2026-06-11T00:47:37Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
