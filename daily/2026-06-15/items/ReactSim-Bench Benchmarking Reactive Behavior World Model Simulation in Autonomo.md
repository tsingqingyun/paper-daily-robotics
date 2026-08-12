---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14058v1"
published: "2026-06-12T03:11:06Z"
age_days: 2
score: 26
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Reactive capability is a key property of data-driven behavior world model simulators for
autonomous driving simulation systems. With this capability, simulated world agents can
respond feasibly to autonomous vehicle (AV) behaviors that differ from the log. However,
existing behavior simulation benchmarks do not directly measure reactive capability.
They often let the simulator jointly control the AV and surrounding agents and evaluate
realism through log similarity or open-loop prediction metrics. In this work, we
introduce ReactSim-Bench for evaluating the reactive capability of behavior world model
simulation in autonomous driving. We decouple the control of agents and the AV, using AV
behaviors that differ from the log and require agents to respond as independent AV
inputs. To obtain these AV behaviors, we construct a pipeline that uses an AV planner
model to generate candidate behaviors and filters the data using rules and manual
verification. Collision metrics, map-based metrics, and kinematic feasibility metrics
are used to evaluate the safety and rule compliance of reactive responses. We construct
2,636 test scenarios with three categories and conduct a systematic evaluation of state-
of-the-art models across multiple architectures, including Transformer-based, diffusion-
based, and next-token-prediction-based models. We further analyze how replan frequency
affects performance and provide insights for future studies.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14058v1
- Authors: Zhiyuan Zhang, Yanlun Peng, Jianing Zhang, Xianda Guo, Zehan Huang, Haoran Liu, Qifeng Li, Shaofeng Zhang, Xiaosong Jia, Junchi Yan
- Published: 2026-06-12T03:11:06Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
