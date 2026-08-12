---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02501v1"
published: "2026-07-02T17:58:28Z"
age_days: 0
score: 36
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Embodied AI models now span vision-language-action (VLA) models and world-action models
(WAMs), but practical deployment remains fragmented across model-specific Python stacks,
backend assumptions, and robot-side glue code, especially on heterogeneous edge devices.
Existing inference runtimes are designed mainly for request-response serving and
therefore do not satisfy the runtime contract of embodied deployment: multi-rate
execution inside closed-loop control, latency-first batch-1 inference on heterogeneous
hardware, and extensible embodied interfaces beyond fixed token I/O. We present
Embodied.cpp, a portable C++ inference runtime for embodied models. Based on an
architectural analysis of representative VLA models and WAMs, Embodied.cpp captures a
shared execution path and organizes it into five layers: input adapters, sequence
builders, backbone execution, head plugins, and deployment adapters. The runtime
provides modular multi-rate execution, latency-first fused inference, and extensible
operator and I/O support, enabling deployment across heterogeneous devices, robots, and
simulators through one backend abstraction. We evaluate Embodied.cpp on two VLA models,
HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer
block. The VLA deployments achieve successful closed-loop execution with 100.0% and
91.0% task success rates, respectively. The WAM benchmark reduces block memory from
312.2 MiB to 88.1 MiB. These results show that Embodied.cpp improves deployment
efficiency while preserving high accuracy across diverse embodied model architectures.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02501v1
- Authors: Ling Xu, Chuyu Han, Borui Li, Hao Wu, Shiqi Jiang, Ting Cao, Chuanyou Li, Sheng Zhong, Shuai Wang
- Published: 2026-07-02T17:58:28Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
