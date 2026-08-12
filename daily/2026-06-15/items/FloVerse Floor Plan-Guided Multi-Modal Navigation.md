---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14267v1"
published: "2026-06-12T08:49:53Z"
age_days: 2
score: 30
created: 2026-06-15
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# FloVerse: Floor Plan-Guided Multi-Modal Navigation

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]]

## 摘要

Floor plans encapsulate compact spatial priors, enabling agents to navigate unseen
scenes more efficiently. While prior work has explored floor plan-guided navigation, it
has focused mainly on PointNav and a limited set of environments. To bridge this gap, we
introduce FloVerse, a new task for floor plan-guided embodied navigation that unifies
PointNav, ObjectNav, and ImageNav. To support FloVerse, we assemble FloVerse-1.6K, a
large-scale dataset of 1.6K scenes from HM3D and Gibson 4+, paired with corresponding
floor plans, comprising 240K expert trajectories and 12M RGBD frames. We further propose
ThreeDiff, a two-stage imitation learning policy comprising a planner, a diffusion-based
multimodal goal-reasoning module trained via masked-modality modeling, and a refiner, a
depth-based trajectory-refinement module for safe execution. Extensive experiments
demonstrate that (1) floor-plan priors improve navigation performance across all goal
modalities, and (2) ThreeDiff implicitly captures spatial information from floor plans.
These results underscore the effectiveness of spatial priors and validate our proposed
unified approach for floor plan-guided embodied navigation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14267v1
- Authors: Weiqi Huang, Shuangyi Dong, Jiaxin Li, Yifei Guo, Zan Wang, Wei Liang
- Published: 2026-06-12T08:49:53Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
