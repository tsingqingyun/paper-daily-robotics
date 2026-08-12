---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21113v1"
published: "2026-07-23T09:41:28Z"
age_days: 1
score: 23
created: 2026-07-25
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# RL-MACRO: A Cybernetic Closed-Loop Intelligence Framework for Multimodal Adaptive Robotic Craniotomy

## 为什么重要

自动筛选分数：23

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Autonomous robotic craniotomy requires continuous regulation of tool-tissue interactions
to mitigate mechanical overload and thermal damage while maintaining surgical
efficiency. However, this process is inherently partially observable due to unknown,
time-varying tissue properties and the inability to directly measure cutting
temperatures under physical occlusion. To address these challenges, we propose RL-MACRO,
a cybernetic closed-loop intelligence framework that couples multimodal perception,
adaptive decision-making, and robotic execution. This framework empowers the surgical
robot to autonomously perceive inaccessible states from partial sensory feedback and
dynamically optimize its behaviors under uncertain environment. A CNN-LSTM observer
first fuses force and sound feedback to reconstruct the hidden temperature state
(R^2=0.939, MAE = 1.717 deg C). This reconstructed temperature, alongside multi-sensor
features, forms the belief state for an offline Implicit Q-Learning (IQL) policy. A
novel dual-head Actor dynamically coordinates the feed rate, spindle speed, and cutting
depth to optimize efficiency within strict safety bounds. These decisions are seamlessly
translated into spatial motions via online trajectory re-planning and velocity servoing.
Experiments on bovine ribs and six ex vivo goat skulls validate the system's robust
perception, adaptive recovery from force/temperature excursions, and smooth execution on
irregular surfaces, establishing a data-driven cybernetic paradigm for safe and
efficient autonomous bone cutting.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21113v1
- Authors: Xiao Zhang, Jiaxuan Li, Renzhen Le, Di Wu, Chao Sun, Jiachen Zhu, Haoyuan Zhang, Xiang Li, Jian Liu, Zhenzhi Ying, Pengfei Zhang, Liming Shu
- Published: 2026-07-23T09:41:28Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
