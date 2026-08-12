---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29936v1"
published: "2026-06-29T08:12:58Z"
age_days: 1
score: 32
created: 2026-06-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action Generation Model

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Open-environment tabletop robotic manipulation requires systems to possess semantic
understanding, precise geometric pose estimation, and high-frequency action generation.
While end-to-end vision-language-action (VLA) models excel at semantic generalization,
they often lack explicit geometric constraints for fine-grained tasks and require costly
training. To bridge the gap between high-level semantics and low-level physical
execution, we propose OpenSPM, an open environment spatial persistent memory framework
consisting of spatial pose memory and flow-matching action generation model. OpenSPM
first leverages semantically conditioned 3D perception and Kalman filtering to track
continuous 6D poses. It then extracts key spatial poses from human demonstrations,
keeping them as transferable, object-centric spatial persistent memory entries. During
inference, OpenSPM retrieves relevant memory entries in terms of natural language
instructions, transfers the spatial poses to new scenes using SE(3) transformations, and
generates high-frequency action chunks via a lightweight conditional flow-matching
model. Combined with real-time proprioceptive state feedback and terminal residual
correction, the system effectively suppresses trajectory error accumulation. Evaluated
on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent
control frequency of 1033.3 Hz, while requiring minimal inference AI computing power.
Extensive ablations illustrate that structured spatial persistent memory and closed-loop
residual correction play a crucial role in reliable, high-frequency robotic
manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29936v1
- Authors: Iok Tong Lei, Qingchen Xie, Yifan Wang, Yap Ying Jie, Zhidong Deng
- Published: 2026-06-29T08:12:58Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
