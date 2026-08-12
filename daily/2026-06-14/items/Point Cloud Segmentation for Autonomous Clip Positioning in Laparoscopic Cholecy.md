---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12048v1"
published: "2026-06-10T13:12:45Z"
age_days: 3
score: 28
created: 2026-06-14
concepts: ["具身智能评测与基准"]
---

# Point Cloud Segmentation for Autonomous Clip Positioning in Laparoscopic Cholecystectomy on a Phantom

## 为什么重要

自动筛选分数：28

连接概念：[[具身智能评测与基准]]

## 摘要

High-risk applications in robotics, such as robot-assisted surgery, present unique
challenges. These systems must be both highly precise and interpretable in order to be
deployed in environments with very low tolerance for error or unsafe exploration. We
present the first robotic system to demonstrate autonomous clip positioning on a
physical phantom in laparoscopic surgery, one of the most common interventions in
general surgery. After segmentation of a colorless point cloud from a single camera,
target positions for the clips are extracted using spline interpolation, and can then be
adjusted by the human operator. The segmentation model is trained on only 60 hand-
labeled real point clouds, reflecting data scarcity in the surgical domain. We overcome
this with a combination of pre-training on 128,000 synthetic point clouds and two novel
data augmentation techniques. The motion of the end-effector to each target is
visualized for the operator, satisfying the unique motion constraints of minimally-
invasive surgery while ensuring that the robot's actions are verifiable and
interpretable. In real robot experiments, our system localizes targets with the required
precision of 0.75mm at a 95% success rate and executes autonomous clip positioning with
a 100% success rate. We provide insights that are applicable to many other surgical and
non-surgical tasks that require identifying and navigating to a precise target. Source
code and project page: https://github.com/balazsgyenes/kirurc

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12048v1
- Authors: Balázs Gyenes, Nikolai Franke, Paul Maria Scheikl, Pit Henrich, Rayan Younis, Gerhard Neumann, Martin Wagner, Franziska Mathis-Ullrich
- Published: 2026-06-10T13:12:45Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
