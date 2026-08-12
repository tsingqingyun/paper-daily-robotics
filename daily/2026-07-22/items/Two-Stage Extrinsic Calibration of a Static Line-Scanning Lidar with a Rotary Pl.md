---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18578v1"
published: "2026-07-20T23:19:33Z"
age_days: 1
score: 28
created: 2026-07-22
concepts: ["AI 核心知识地图"]
---

# Two-Stage Extrinsic Calibration of a Static Line-Scanning Lidar with a Rotary Platform

## 为什么重要

自动筛选分数：28

连接概念：[[AI 核心知识地图]]

## 摘要

A line-scanning lidar yields range and azimuth values in a fixed plane. To perceive
surrounding objects in 3D, there must be relative motion between the lidar plane and the
object. Thus, using a rotating base-platform is promising for industrial applications
where objects need to be scanned or inspected precisely, and is the main focus of this
work. In the rotary platform setup, a 3D point cloud of an object can be constructed if
the axis of rotation and the precise motion about that axis are known. However, this
setup gives rise to the following problem: how can the axis of rotation of the platform
be accurately identified with respect to the lidar coordinate system? It is referred to
as the calibration problem in the robotics community. Any inaccuracy in this
transformation directly affects the quality of the reconstructed point cloud, leading to
misrepresentation of the object of interest. In this work, we explore automated
approaches to statically and dynamically estimate the transformation of a rotary
platform's axis of rotation with respect to a static line-scanning lidar. The proposed
algorithms have been validated on real-world datasets obtained from a custom made rotary
platform and an FMCW lidar, and their convergence characteristics are studied for
various initial conditions.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18578v1
- Authors: Vikram Shree, Hike Danakian, Long Nguyen, Rajanish Gokidi, Patrick Nercessian
- Published: 2026-07-20T23:19:33Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
