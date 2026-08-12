---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12579v1"
published: "2026-06-10T18:28:24Z"
age_days: 2
score: 32
created: 2026-06-13
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# G-MAPP: GPU-accelerated Multi-Agent Planning and Perception for Reactive Motion Generation

## 为什么重要

自动筛选分数：32

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Reactive motion generation in unstructured environments remains an open challenge in
robotics. Due to the computational complexity of collision-free motion generation,
existing methods either generate global trajectories for static scenarios, or employ
models that make conservative assumptions about the environment. This paper identifies
the primary bottleneck as the runtime performance demand of planning on high-fidelity
environments, and the temporal integration between the perception and planning modules.
Therefore, we propose a framework that does not compromise on runtime performance and
world representations for perception and planning by accelerating world modeling and
vector-field based planning using the GPU. This allows us to achieve faster parallel
state exploration for quasi-global trajectory planning, and tighter coupling of the
perception-action loop in real-time for dynamic cluttered environments with off-the-
shelf depth sensors. We quantitatively evaluate the computation-time and success rate
differences for the CPU and GPU versions of our planner, and perform qualitative
evaluations of our coupled framework using real-world experiments on a 7-DoF Franka
Emika robot. Experimental results demonstrate that our GPU-based framework achieves up
to a 5x speedup over the CPU version and successfully avoids collisions across both
trivial and challenging physical world scenarios.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12579v1
- Authors: Tanmay Bishnoi, Riddhiman Laha, Tobias Löw, Jose Alex Chandy, Luis F. C. Figueredo, Sami Haddadin
- Published: 2026-06-10T18:28:24Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
