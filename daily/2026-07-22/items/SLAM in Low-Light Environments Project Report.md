---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17699v1"
published: "2026-07-20T08:47:43Z"
age_days: 1
score: 28
created: 2026-07-22
concepts: ["具身智能评测与基准"]
---

# SLAM in Low-Light Environments: Project Report

## 为什么重要

自动筛选分数：28

连接概念：[[具身智能评测与基准]]

## 摘要

Simultaneous localization and mapping (SLAM) is one of the fundamental problems in
robotics, as it enables autonomous operations in real-world scenarios. Under low
illumination, reduced contrast, sensor noise, and motion blur degrade both feature
extraction and feature matching, while compensating with LiDAR, depth, or thermal
sensors raises cost, power draw, and integration complexity. Existing benchmarks remain
dominated by well-lit indoor or daylight sequences, leaving open how far SLAM with
standard RGB cameras can be pushed in the dark. We benchmark six systems spanning the
feature-based, direct, filter-based, and learning-based paradigms - ORB-SLAM3, DSO,
Kimera-VIO, OpenVINS, DPVO, and DPV-SLAM - on five LaMARia sequences of varying
difficulty and illumination, reporting absolute and relative pose error alongside
control-point recall. Kimera-VIO is the only system to track all five sequences to
completion, combining the lowest relative pose error with steadily growing absolute
error due to the absence of loop closure; DPVO and DPV-SLAM never lose tracking but
incur absolute errors of roughly 100 m under low light; and the classical monocular
pipelines (ORB-SLAM3, DSO) together with the filter-based OpenVINS fail outright or
diverge on most of the harder and low-light sequences. The results suggest that RGB-only
SLAM maintains stable low-light tracking only when both inertial fusion and global
optimization are present. Closing the remaining gap will likely require low-light-
specific learned front-ends or a return to complementary sensing.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17699v1
- Authors: Oleh Basystyi, Anna Stasyshyn, Oleksandr Kosovan, Yaroslav Prytula
- Published: 2026-07-20T08:47:43Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
