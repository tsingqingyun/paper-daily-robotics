---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01757v1"
published: "2026-07-02T06:17:33Z"
age_days: 4
score: 25
created: 2026-07-06
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DL-VINS-Factory: A Modular Framework for Learned Visual Front-Ends in Visual-Inertial SLAM

## 为什么重要

自动筛选分数：25

连接概念：[[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Deep-learning features excel in visual matching, yet their practical value in tightly
coupled visual-inertial SLAM (VI-SLAM) remains insufficiently characterized. We present
DL-VINS-Factory, a unified framework that integrates learned feature extractors (ALIKED,
RaCo, SuperPoint, XFeat) with either Lucas--Kanade (LK) optical-flow tracking or
LightGlue (LG) descriptor matching. All front-ends share a sliding-window Ceres back-
end, with optional AnyLoc DINOv2-VLAD loop closure, and 4-DoF pose-graph optimization.
We benchmark the system across the four datasets covering indoor, unstructured outdoor,
aggressive-motion, and visually degraded conditions. Results show that learned front-
ends are viable for real-time embedded VI-SLAM, but are not universally superior to
classical tracking. Relative to the corresponding GFTT+LK baseline, ALIKED+LG reduces
EuRoC ATE by $5\%$ in monocular odometry and by $7\%$ in stereo with loop-closure. On
NTU-VIRAL, where aggressive aerial motion increases inter-frame viewpoint change,
ALIKED+LG stereo reduces loop-closed ATE by $12\%$. In Botanic Garden dataset, optical-
flow tracking remains preferable, but learned keypoints still improve over the baseline
GFTT, in which SuperPoint+LK reduces grayscale camera ATE by $29\%$, while RaCo+LK
reduces RGB camera ATE by $38\%$. On SubT-MRS, learned front-ends display varying degree
of improvement based on individual cases. With TensorRT acceleration on a Jetson AGX
Orin, all valid configurations run in real time between $29$--$47$ FPS in monocular mode
and $18$--$33$ FPS in stereo mode for the EuRoC and NTU-VIRAL datasets. AnyLoc further
confirms roughly $2$--$7\times$ more valid loops than BRIEF+DBoW2. The implementation is
open-sourced at https://github.com/limshoonkit/DL-VINS-Factory-ROS2/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01757v1
- Authors: Shoon Kit Lim, Melissa Jia Ying Chong, Ting Yang Ling
- Published: 2026-07-02T06:17:33Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
