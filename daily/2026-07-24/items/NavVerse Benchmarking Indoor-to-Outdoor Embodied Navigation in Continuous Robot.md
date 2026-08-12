---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19695v1"
published: "2026-07-22T02:53:46Z"
age_days: 2
score: 35
created: 2026-07-24
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation

## 为什么重要

自动筛选分数：35

连接概念：[[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Robots deployed in delivery, campus, and emergency-response settings often need to
navigate from buildings to streets within a single continuous episode. Existing
benchmarks usually evaluate indoor and outdoor navigation separately, and many abstract
away robot execution, leaving exit finding, boundary traversal, adaptation, and
kinodynamic failures underexplored. We introduce NavVerse, a physics-enabled benchmark
for indoor-to-outdoor embodied navigation. NavVerse contains 100 indoor scenes, 50 urban
outdoor scenes, and 50 indoor-to-outdoor scenes, and 10,000 episodes spanning Object
Navigation, Vision-and-Language Navigation, and Place Navigation tasks, where agents
search for semantic points of interest such as restaurants or banks. Agents are
evaluated through executable robot interfaces using task-success, path-efficiency, and
safety metrics. Zero-shot experiments with RL, VLA, and modular baselines show that
current agents remain far from solving cross-context navigation: end-to-end VLAs obtain
the highest zero-shot success, while the modular method provides the strongest safety
profile. PlaceNav further reveals a clear drop from outdoor to indoor-to-outdoor scenes,
indicating that adaptation remains major bottleneck.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19695v1
- Authors: Junzhe Wu, Yue Hu, Zeyu Han, Po-Hsun Chang, Yinan Dong, Behrad Rabiei, Maani Ghaffari
- Published: 2026-07-22T02:53:46Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
