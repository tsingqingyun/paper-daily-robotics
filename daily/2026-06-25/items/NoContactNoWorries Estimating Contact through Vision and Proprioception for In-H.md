---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24450v1"
published: "2026-06-23T11:36:46Z"
age_days: 1
score: 37
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习"]
---

# NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation

## 为什么重要

自动筛选分数：37

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

Perceiving physical contact is fundamental to dexterous manipulation. While robots often
rely on dedicated hardware tactile sensors, humans exhibit a remarkable ability to infer
contact by integrating visual information with an innate sense of their body's pose and
movement. Inspired by this embodied perceptual skill, we investigate whether a robot can
learn to infer contact from vision, an approach that also offers a scalable alternative
to tactile hardware specifically for binary contact estimation, which faces practical
challenges in cost, fragility, and integration. We present NoContactNoWorries, a
transformer-based multimodal framework that fuses RGB-D vision with the robot's
proprioception to infer binary contact states as a pseudo-tactile signal for hand-object
interactions. We validate by training a single contact prediction model on multiple
objects and show that the inferred contact signal supports downstream reinforcement
learning agents for in-hand object reorientation, generalizing to novel objects.
Experiments in both simulation and on a real-world robot validate our approach,
highlighting the feasibility of inferring contact from vision and proprioception.
Project Page: https://soham2560.github.io/no-contact-no-worries/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24450v1
- Authors: Soham Patil, Avirup Das, Sourabh Bhosale, Spandan Roy
- Published: 2026-06-23T11:36:46Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
