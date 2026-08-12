---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.07045v1"
published: "2026-08-07T09:54:00Z"
age_days: 3
score: 24
created: 2026-08-10
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video

## 为什么重要

自动筛选分数：24

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

High-quality demonstrations for dexterous robot manipulation are costly and difficult to
collect, whereas monocular human videos provide a scalable source of diverse
manipulation behaviors. However, transferring such demonstrations to dexterous robots
remains challenging: monocular hand-object interaction (HOI) reconstruction often
produces temporally unstable contacts and physically implausible interactions, while
conventional retargeting methods struggle to preserve task-relevant contacts and local
interaction geometry across different hand embodiments. We present C2Dex, a video-to-
dexterous-manipulation framework built around a shared interaction representation:
stable object-side contacts recovered by aggregating noisy frame-wise observations in
the canonical object space. These stable contacts serve a dual role: as trajectory-level
constraints that guide reconstruction toward temporally coherent and physically
plausible human HOI trajectories, and as explicit transfer targets for the dexterous
hand, where Laplacian interaction optimization preserves the local hand-object geometry
across embodiments and residual reinforcement learning refines the trajectory in
simulation. Experiments on DexYCB and TACO show that C2Dex achieves end-to-end
trajectory success rates of 57.78% and 26.67%, respectively, substantially outperforming
the strongest baselines (17.78% and 10.00%) under identical evaluation criteria. Real-
robot replay experiments further demonstrate physical feasibility across diverse
contact-rich manipulation tasks. Project page: https://k-jie.github.io/C2Dex/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.07045v1
- Authors: Jie Ren, Zhehao Jiang, Yinhong Yang, Haorui Jia, Han Jiang, Ben Li, Yao Yao, Cheng Lin, Qiu Shen, Zhenshan Bing, Xiao-Xiao Long, Xun Cao
- Published: 2026-08-07T09:54:00Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
