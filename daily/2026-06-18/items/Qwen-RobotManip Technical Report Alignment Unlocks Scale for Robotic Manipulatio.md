---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17846v1"
published: "2026-06-16T12:14:39Z"
age_days: 1
score: 46
created: 2026-06-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models

## 为什么重要

自动筛选分数：46

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Foundation models in language and multimodality achieve strong generalization by
aligning heterogeneous data under a unified formulation and training at scale. In this
report, we investigate whether this scaling recipe can be applied to robotic
manipulation to achieve genuine generalization. This is challenging because, unlike
text, manipulation data is heterogeneous by nature, expensive to collect, and narrow in
diversity, making alignment and scale simultaneously difficult. We present Qwen-
RobotManip, a generalizable Vision-Language-Action foundation model built on Qwen-VL.
Qwen-RobotManip introduces a unified alignment framework across the representation,
motion, and behavioral dimensions of manipulation, making large-scale multi-source
training coherent rather than conflicting. This alignment capability in turn enables
Qwen-RobotManip to absorb manipulation data at a scale that prior training regimes could
not sustain. A human-to-robot synthesis pipeline converts egocentric hand demonstrations
into robot trajectories across 15 platforms, and a rigorous curation pipeline harmonizes
heterogeneous datasets. Using only open-source datasets and human videos without
proprietary data collection, Qwen-RobotManip constructs a ~38,100-hour pretraining
corpus and exhibits emergent generalization capabilities, including zero-shot
instruction following, robustness to perturbations, reactive error recovery, and cross-
embodiment transfer. We find that standard benchmarks fail to capture pretraining
quality and instead adopt OOD settings including RoboCasa365, LIBERO-Plus, EBench,
RoboTwin-Clean2Rand, RoboTwin-IF, and RoboTwin-XE. Qwen-RobotManip substantially
outperforms prior state-of-the-art models, including $π$0.5, across all OOD settings,
ranks 1st in RoboChallenge with a 20% relative improvement, and is validated on real-
robot platforms including AgileX ALOHA, Franka, UR, and ARX.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17846v1
- Authors: Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li, Pei Lin, Yiyang Huang, Zixing Lei, Tong Zhang, Jiazhao Zhang, Jie Zhang, Jingyang Fan, Gengze Zhou, Qihang Peng, Chenxu Lv, Xiaoyue Chen, An Yang, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou, Chenfei Wu, Xiong-Hui Chen
- Published: 2026-06-16T12:14:39Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
