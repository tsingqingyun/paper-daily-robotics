---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13757v1"
published: "2026-05-13T16:38:05Z"
age_days: 0
score: 35
created: 2026-05-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FrameSkip: Learning from Fewer but More Informative Frames in VLA Training

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) policies are commonly trained from dense robot
demonstration trajectories, often collected through teleoperation, by sampling every
recorded frame as if it provided equally useful supervision. We argue that this
convention creates a temporal supervision imbalance: long low-change segments dominate
the training stream, while manipulation-critical transitions such as alignment, contact,
grasping, and release appear only sparsely. We introduce FrameSkip, a data-layer frame
selection framework that scores trajectory frames using action variation, visual-action
coherence, task-progress priors, and gripper-transition preservation, then remaps
training samples toward high-importance frames under a target retention ratio. Because
FrameSkip operates only in the dataloader, it leaves the VLA architecture, action head,
training objective, and inference procedure unchanged. Across RoboCasa-GR1, SimplerEnv,
and LIBERO, FrameSkip improves the success-retention trade-off over full-frame training
and simpler frame selection variants, achieving a macro-average success rate of 76.15%
across the three benchmarks compared with 66.50% for full-frame training while using a
compressed trajectory view that retains 20% of unique frames in the main setting.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13757v1
- Authors: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Changti Wu, Hang Yuan, Haishan Liu, Bailing Wang, Cong Huang, Kai Chen
- Published: 2026-05-13T16:38:05Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
