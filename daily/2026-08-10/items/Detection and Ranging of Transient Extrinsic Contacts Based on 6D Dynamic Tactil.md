---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.07075v1"
published: "2026-08-07T10:27:37Z"
age_days: 3
score: 26
created: 2026-08-10
concepts: ["智能体 Agent"]
---

# Detection and Ranging of Transient Extrinsic Contacts Based on 6D Dynamic Tactile Sensing

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]]

## 摘要

Delicate manipulation often involves transient and subtle collisions between a grasped
object and the environment. While the human hand localizes these contacts effortlessly
thanks to superior tactile sensitivity, robotic systems often lack the requisite
resolution to acquire the information necessary for motion planning, resulting in clumsy
manipulation or even task failure. Here, we propose transient extrinsic contact
detection and ranging (TECDAR), a simple yet fast and efficient method for detecting and
ranging extrinsic contact of grasped objects. Our design of gripper tips employs dynamic
tactile sensing leveraging a single 2.5$\times$3 mm 6D inertial measurement unit. The
sensor captures sub-millisecond tip deformations at a 7 kHz sampling rate, but operating
on a data stream of only 84 KB/s. High bandwidth and compact data size enable the system
to rapidly detect and localize contact between grasped objects and their surroundings.
Specifically, fusing tactile data with robot pose via an extended Kalman filter enables
fast and precise localization of extrinsic contact, reaching millimeter-level accuracy
within 180 ms. Experimental results demonstrate that the system achieves an average
localization accuracy of approximately 7\,mm in both line-contact and point-contact
localization tasks. Furthermore, this near-instantaneous localization enables the robot
to rectify its trajectory on a millisecond scale, facilitating precise tool manipulation
and enhanced perception of complex environments purely through tactile exploration and
mapping. We envision such techniques advancing the future of robotics across domains
requiring delicate manipulation, including precision assembly, surgical assistance, and
autonomous exploration in touch-dominant environments. Project page:
humitlab.github.io/TECDAR/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.07075v1
- Authors: Haowen Zheng, Yinghao Wu, Fuyuan Liu, Yichen Li, Yitian Shao
- Published: 2026-08-07T10:27:37Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
