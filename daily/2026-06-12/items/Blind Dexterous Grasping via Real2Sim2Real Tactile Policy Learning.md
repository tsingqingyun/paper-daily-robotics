---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11767v1"
published: "2026-06-10T07:46:38Z"
age_days: 1
score: 35
created: 2026-06-12
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning

## 为什么重要

自动筛选分数：35

连接概念：[[世界模型]], [[机器人学习]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Blind grasping with a dexterous hand is a crucial manipulation capability. Nevertheless,
learning such tactile-only policies for real robots remains challenging due to the
tactile sim-to-real gap and the limited expressiveness of sparse tactile signals. To
bridge this gap, we propose a framework for tactile-only blind grasping that is
deployable on a physical multi-fingered robotic hand. Our approach combines three key
components. First, we introduce a Real2Sim tactile calibration pipeline that constructs
a contact-calibrated digital-twin simulator capable of reproducing real tactile signals.
Second, we improve the expressiveness of sparse tactile observations using a layout-
aware tactile encoder, which incorporates sensor-geometry priors through self-supervised
pretraining. Third, to improve generalization to unseen objects, we train object-
specific reinforcement-learning experts in the calibrated simulator and aggregate their
successful grasp trajectories into a tactile-conditioned Diffusion Policy. We evaluate
our method on a physical LEAP Hand equipped with distributed tactile sensing across 10
seen and 10 unseen objects. The deployed policy achieves a 27\% real-world grasp success
rate across all 20 objects, without real-world grasping demonstrations or visual input.
Simulation ablations show that layout-aware tactile pretraining improves grasping
performance, while sensing-level evaluations confirm that Real2Sim calibration increases
the consistency of tactile contact events between simulation and hardware. Together,
these results suggest that contact-event calibration, geometry-aware tactile
representation learning, and diffusion-based policy aggregation provide an effective
path toward tactile-only blind grasping on real dexterous robotic hands. Project
page:Dex-Blind-Grasp.github.io.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11767v1
- Authors: Shengcheng Luo, Xiyan Huang, Zhe Xu, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
- Published: 2026-06-10T07:46:38Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
