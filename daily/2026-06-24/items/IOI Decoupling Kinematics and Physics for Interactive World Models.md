---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23296v1"
published: "2026-06-22T13:09:34Z"
age_days: 1
score: 35
created: 2026-06-24
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# IOI: Decoupling Kinematics and Physics for Interactive World Models

## 为什么重要

自动筛选分数：35

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Developing generalist embodied agents requires interactive environments providing
visually realistic feedback and accurate action-conditioned dynamics. Interactive world
models address this by simulating such complex dynamics. However, purely data-driven
methods struggle to ensure precise control alignment and physically plausible visual
feedback due to a lack of explicit structural constraints. To address this, we propose
IOI, a hybrid interactive world model integrating analytical kinematic priors with
learned physical dynamics. Unlike data-driven approaches prone to spatiotemporal drift,
IOI introduces explicit kinematic guidance, computing forward kinematics from action
sequences for accurate motion trajectories. These trajectories are rendered into
synchronized front, side, and top orthographic projections, eliminating the need for
extrinsic camera calibration. A Multi-view Kinematic Aggregation and Injection module
fuses these geometric cues and injects them into the video generator, providing
geometry-consistent guidance. Conditioning video generation on these deterministic
trajectories establishes a synergy between the analytical simulator and the world model.
Decoupling deterministic motion into the kinematic prior frees the generator to model
stochastic physical interactions. Experiments on the RoboTwin benchmark validate IOI
across kinematic fidelity, out-of-distribution (OOD) generalization, and policy
evaluation. IOI achieves state-of-the-art simulation performance and robust zero-shot
generalization to unseen OOD tasks. Furthermore, IOI serves as a reliable policy
evaluator, yielding success rates closely aligning with ground-truth physics simulators.
On real-world platforms, policies trained on IOI-synthesized data match those trained on
teleoperation demonstrations, solidifying its practical value for embodied policy
learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23296v1
- Authors: Chengyu Bai, Peidong Jia, Tiecheng Guo, Yukai Wang, Rui Ma, Fangyuan Zhao, Chunkai Fan, Xiaobao Wei, Jintao Chen, Hao Wang, Ying Li, Xiaozhu Ju, Jian Tang, Shanghang Zhang
- Published: 2026-06-22T13:09:34Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
