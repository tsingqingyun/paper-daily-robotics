---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06221v1"
published: "2026-08-06T16:12:18Z"
age_days: 3
score: 26
created: 2026-08-10
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Robot Learning from Human Demonstrations: Handwritten Alphabet Trajectories and Human-Likeness Evaluation

## 为什么重要

自动筛选分数：26

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Learning from demonstration (LfD) provides a developmental framework through which
robots can develop motor skills by observing and imitating human dynamics, reducing
reliance on explicit programming to teach a skill to a robot. The resulting human-like
robot motion is recognised as a key factor in building trust and enabling natural
collaboration in human-robot interaction. This paper presents a framework for learning
human-like robot motion from demonstration, including data collection, probabilistic
trajectory learning, and perceptual user evaluation. A dataset of 3,142 handwriting
demonstrations was collected from 22 participants across all 52 Latin alphabet
character-case combinations via a touchscreen teleoperation interface, capturing planar
position, contact force, and timing. Building on the widely used Gaussian Mixture Model
and Gaussian Mixture Regression approach for learning from demonstration, the framework
is extended in this work by incorporating force and normalised time dimensions to enable
richer representation of human dynamics, and adapting it to handle non-continuous,
multi-segment trajectories, enabling generalisation across demonstrations. A user study
with 21 participants evaluated the perceived human-likeness of the generated
trajectories using a continuous scale anchored between robotic and human-like motion,
normalised to 0-100 where 50 represents the neutral midpoint. The generated trajectories
achieved an overall human-likeness score of 71.50 (SD=22.56), indicating that the
majority of trajectories were perceived as more human-like. Participants identified
geometric positioning and trajectory sequence as the most influential perceptual
factors, and reported positive attitudes toward human-like robot behaviour. The datasets
are released as open-source, providing a reproducible benchmark for developing and
evaluating human-like robot motion methods.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06221v1
- Authors: Alperen Kenan, Paul Bremner, Manuel Giuliani
- Published: 2026-08-06T16:12:18Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
