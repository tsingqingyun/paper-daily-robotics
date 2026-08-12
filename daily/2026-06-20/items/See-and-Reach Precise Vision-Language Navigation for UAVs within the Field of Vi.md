---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20045v1"
published: "2026-06-18T10:21:42Z"
age_days: 1
score: 28
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# See-and-Reach: Precise Vision-Language Navigation for UAVs within the Field of View

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

UAV Vision-Language Navigation (UAV-VLN) is typically formulated as a holistic search-
and-reach problem, where long-range target discovery and final target approach are
optimized and evaluated jointly. This formulation makes it difficult to assess a
critical capability of aerial embodied agents, namely whether a UAV can accurately
ground a visible target and translate vision-language evidence into precise 3D motion
once the target enters its field of view. To address this limitation, we introduce UAV-
VLN-FOV, a target-visible navigation task that isolates the see-and-reach stage and
enables a more diagnostic evaluation of terminal reaching ability. We further propose
3DG-VLN, a vision-language waypoint prediction framework guided by dynamic 3D direction
cues to enhance fine-grained visual grounding and spatial direction alignment for
precise target reaching. Specifically, 3DG-VLN adaptively processes high-resolution
front-view and downward-view observations to preserve fine-grained visual and geometric
details for target grounding. It also updates the target-relative direction online
during closed-loop navigation, allowing the agent to maintain spatial alignment with the
target and reduce accumulated direction drift. To support this task, we construct a
dedicated high-resolution benchmark which contains 2,717 trajectories with target-
oriented high-level instructions, high-resolution front-view and downward-view
egocentric observations, and continuous 3D waypoint annotations. Experiments show that
3DG-VLN outperforms competitive UAV-VLN baselines, achieving a 13.82\% improvement in
success rate. Real-world trials further demonstrate the potential of 3DG-VLN for
practical see-and-reach navigation. The source code and benchmark are available at
https://github.com/xuefanfu/3DG-VLN.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20045v1
- Authors: Fanfu Xue, En Yu, Yantian Shen, Zhikun Hu, Hongjun Wang, Yang Yang, Xindi Wang, Jiande Sun
- Published: 2026-06-18T10:21:42Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
