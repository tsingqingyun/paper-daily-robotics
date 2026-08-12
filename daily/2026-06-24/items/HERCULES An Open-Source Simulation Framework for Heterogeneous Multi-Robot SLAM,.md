---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22756v1"
published: "2026-06-22T01:51:40Z"
age_days: 1
score: 34
created: 2026-06-24
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration

## 为什么重要

自动筛选分数：34

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

We present HERCULES, an open-source simulator and data-collection pipeline for
heterogeneous multi-robot autonomy. Built upon the Unreal Engine 5 (UE5)-based
simulators AirSim and Cosys-AirSim, HERCULES resolves key architectural limitations of
prior frameworks to enable concurrent unmanned aerial and ground vehicle (UAV-UGV)
operation in large-scale, photorealistic, dynamic environments. It introduces a new
waypoint-tracking UGV controller that mirrors existing UAV control interfaces, and
provides a shared navigation stack for mapping, traversability analysis, planning, and
control across heterogeneous platforms. Expanding inherited sensor suites, it adds
physics-based long-wave infrared (LWIR) cameras and configurable night-vision modes for
degraded visual environments. HERCULES provides lightweight APIs, ROS 2 wrappers, and
rigorous time synchronization across sensors and platforms, and brings state-of-the-art
game-engine capabilities into robotics simulation, integrating intelligent agents such
as pedestrians, traffic, and wildlife with high-fidelity dynamic phenomena, including
fire, flooding, and crop disease spread. HERCULES runs in two modes: passively,
replaying offline-designed trajectories to generate reproducible multi-modal datasets,
and actively, running an online planner in closed loop from live observations. Our
experiments in heterogeneous multi-robot SLAM, collaborative perception, and
exploration, using both HERCULES-generated data and active closed-loop execution,
demonstrate its utility for advancing heterogeneous multi-robot autonomy. We publicly
release our source code, experiment code, documentation, and datasets, including a
heterogeneous multi-robot SLAM benchmark collected with two UAVs and two UGVs across
kilometer-scale desert, forest, and city environments, at https://lunarlab-
gatech.github.io/HERCULES-website.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22756v1
- Authors: Sandilya Sai Garimella, Daniel Chase Butterfield, Sean Wilson, Lu Gan
- Published: 2026-06-22T01:51:40Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
