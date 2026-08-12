---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23431v1"
published: "2026-06-22T14:48:58Z"
age_days: 2
score: 29
created: 2026-06-25
concepts: ["机器人学习", "具身智能评测与基准"]
---

# DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy

## 为什么重要

自动筛选分数：29

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Fine-grained, bimanual dexterous manipulation remains a foundational challenge in
robotics. Traditional teleoperation systems often fail in contact-rich tasks because
embodiment gaps hinder accurate kinematic mapping, while tactile and force feedback
remain absent. Consequently, data collection efficiency for high-precision tasks remains
prohibitively low. To address these limitations, we propose a tactile-driven adaptation
strategy designed to enable fine-grained manipulation on top of teleoperation pipelines.
Instantiated within our bimanual dexterous framework, DexTeleop-0, this strategy
introduces a real-time optimization loop that bridges the embodiment gap by translating
coarse human tracking intents into precise, force-compliant robotic commands with
tactile sensing. By estimating accurate contact points and leveraging a tactile-enabled
fingertip force-sensing profile, the system dynamically computes localized corrections
using the operational space Jacobian with respect to joint angle updates. We rigorously
evaluate this tactile-driven adaptation strategy across both simulated environments and
real-world hardware. Compared with representative baselines, the proposed method
consistently achieves higher task success rates and improved execution efficiency in
robust grasping, disturbance-resilient manipulation, and complex dexterous tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23431v1
- Authors: Haichao Liu, Yuyao Jiang, Hyunsun Park, Yuanjiang Xue, Ziwei Wang
- Published: 2026-06-22T14:48:58Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
