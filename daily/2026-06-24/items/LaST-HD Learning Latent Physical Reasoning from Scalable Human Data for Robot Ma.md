---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23685v1"
published: "2026-06-22T17:59:52Z"
age_days: 1
score: 36
created: 2026-06-24
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation

## 为什么重要

自动筛选分数：36

连接概念：[[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Human-hand demonstrations provide a direct and scalable source of physical interaction
data for robot learning. While manual retargeting is indispensable for establishing
kinematic action correspondence across different morphologies, robust transfer requires
going beyond geometry to address the underlying alignment of physical dynamics between
human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-
robot action learning paradigm that extends reasoning-before-acting VLA by aligning
human-hand and robot demonstrations in a shared latent reasoning space. Rather than
mimicking human kinematics, LaST-HD trains an auxiliary action-conditioned world model
on unpaired human-hand and robot trajectories to synthesize unified latent targets.
After aligning cross-embodiment representations in this shared forward-dynamics space,
these targets supervise LaST-HD's latent reasoning process, enabling it to internalize
shared physical dynamics and drive efficient human-hand action learning. Moreover, we
develop Out-of-Lab (OOL) Glove, a low-cost motion-capture glove tailored to LaST-HD for
human-hand data collection. The captured human data provide precise keypoints and serve
as universal action supervision across grippers and dexterous hands. Armed with the
aligned latent space and high-fidelity human-hand data, we develop a progressive mixed-
to-human training recipe comprising mixed human-robot co-training and human-hand online
correction post-training. Through mixed co-training, LaST-HD improves generalization to
novel objects, scenes, and positions using only human-hand demonstrations. With online
correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy
using only 20 minutes of OOL glove data.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23685v1
- Authors: Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang, Yang Yue, Yeqing Yang, Lei Wang, Peng Jia, Hao Tang, Shanghang Zhang
- Published: 2026-06-22T17:59:52Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
