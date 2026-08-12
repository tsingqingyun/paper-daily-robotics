---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06569v1"
published: "2026-06-04T17:48:31Z"
age_days: 3
score: 31
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# PhyRoGen: Synthetic Generation of Physical Robot Manipulation Puzzles Using Procedural Content Generation

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Robot manipulation of physical puzzles is important for automatic assembly and
disassembly tasks. However, to enable robots to solve physical puzzles, manipulation
skills need to be learned, which requires large training datasets, the generation of
which is often time consuming and tedious. To overcome this problem, we propose the
Physical Robot Manipulation Puzzle Generation framework (PhyRoGen), which leverages
procedural content generation (PCG) for automated generation of synthetic datasets of
manipulation puzzles. PhyRoGen is a general-purpose puzzle generator, which can generate
physical puzzles with interlocking object dependencies, where one articulated object
must be manipulated before another can be moved. Based upon PhyRoGen, we define six
concrete generators which we use to generate 24 physical puzzles. By using a
benchmarking framework, we are able to solve all puzzles in 1 to 300 seconds using
sampling-based planning algorithms. Finally, we demonstrate that every generated puzzle
is manipulatable by using a KUKA LBR iiwa robot in a physical simulation. This shows
that our framework is able to procedurally generate unique, solvable robot manipulation
puzzles, which is a crucial ingredient to benchmark manipulation algorithms and to
develop robust foundation models.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06569v1
- Authors: Lennart Julian Droß, Andreas Orthey, Marc Toussaint
- Published: 2026-06-04T17:48:31Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
