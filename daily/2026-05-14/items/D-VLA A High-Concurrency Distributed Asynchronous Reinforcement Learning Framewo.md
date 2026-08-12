---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13276v1"
published: "2026-05-13T09:54:31Z"
age_days: 0
score: 42
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models

## 为什么重要

自动筛选分数：42

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

The rapid evolution of Embodied AI has enabled Vision-Language-Action (VLA) models to
excel in multimodal perception and task execution. However, applying Reinforcement
Learning (RL) to these massive models in large-scale distributed environments faces
severe systemic bottlenecks, primarily due to the resource conflict between high-
fidelity physical simulation and the intensive VRAM/bandwidth demands of deep learning.
This conflict often leaves overall throughput constrained by execution-phase
inefficiencies. To address these challenges, we propose D-VLA, a high-concurrency, low-
latency distributed RL framework for large-scale embodied foundation models. D-VLA
introduces "Plane Decoupling," physically isolating high-frequency training data from
low-frequency weight control to eliminate interference between simulation and
optimization. We further design a four-thread asynchronous "Swimlane" pipeline, enabling
full parallel overlap of sampling, inference, gradient computation, and parameter
distribution. Additionally, a dual-pool VRAM management model and topology-aware
replication resolve memory fragmentation and optimize communication efficiency.
Experiments on benchmarks like LIBERO show that D-VLA significantly outperforms
mainstream RL frameworks in throughput and sampling efficiency for billion-parameter VLA
models. In trillion-parameter scalability tests, our framework maintains exceptional
stability and linear speedup, providing a robust system for high-performance general-
purpose embodied agents.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13276v1
- Authors: Yucheng Guo, Yongjian Guo, Zhong Guan, Wen Huang, Haoran Sun, Haodong Yue, Xiaolong Xiang, Shuai Di, Zhen Sun, Luqiao Wang, Junwu Xiong, Yicheng Gong
- Published: 2026-05-13T09:54:31Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
