---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21071v1"
published: "2026-07-23T09:04:11Z"
age_days: 0
score: 34
created: 2026-07-24
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Autonomous biomedical laboratories increasingly rely on visual perception to recognize,
localize, and manipulate transparent plasticware, yet high-quality real-world datasets
for this setting remain limited. The scarcity of domain-relevant data is particularly
restrictive in cluttered multi-object scenes, where mutual occlusion and view-dependent
appearance changes remain challenging even for contemporary visual foundation models.
Existing transparent-object datasets have advanced segmentation, depth, and pose
estimation, but they usually do not evaluate the combined setting of multi-object
clutter, occlusion, and calibrated multi-view capture that characterizes real laboratory
manipulation scenes. To address this gap, we present TrainsBiolab, a real-world RGB-D
dataset of cluttered transparent biomedical objects captured as calibrated multi-view
sequences. TrainsBiolab contains 161,315 frames from 98 scenes and 1.03M instance
annotations over 15 laboratory object types, including 6D poses, full and visible masks,
depth, and per-frame camera calibration. The dataset is organized along three axes that
reflect operational difficulty: object category, the total number of objects in a frame,
and camera viewpoint. We further define dataset-centric benchmarks for segmentation,
depth estimation and completion, and 6D pose estimation, and report a system-level robot
manipulation evaluation enabled by the released annotations and calibrations. By
focusing on repeated transparent instances, clutter, and multi-view laboratory capture,
TrainsBiolab provides a resource for segmentation, depth estimation, 6D pose estimation,
and multi-view reasoning in autonomous laboratory manipulation. Project page:
https://dualtransparency.github.io/TransBiolab/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21071v1
- Authors: Ke Ma, Yifei Wang, Meng Wang, Tian Xia
- Published: 2026-07-23T09:04:11Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
