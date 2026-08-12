---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14997v1"
published: "2026-07-16T13:46:00Z"
age_days: 1
score: 27
created: 2026-07-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Language-conditioned quadrotor flight requires a policy to ground semantic goals,
anticipate the visual consequences of ego-motion, and output control references that
remain smooth and dynamically executable under rapidly changing first-person views.
Existing aerial vision-language navigation and vision-language-action methods commonly
use discrete actions, high-level waypoints, or instantaneous velocity commands, which
provide limited supervision about how flight actions change future observations. We
present AeroAct, an action-centered world-action model (WAM) for quadrotor navigation.
To the best of our knowledge, AeroAct is the first WAM instantiated and demonstrated for
real-world aerial flight. The model adapts a pretrained video diffusion Transformer to
predict local trajectory-action chunks from egocentric visual history, proprioception,
and language. Future first-person frames are used during training as dense consequence
supervision, while deployment directly decodes actions without generating future video.
To obtain aligned visual, state, language, and dynamically feasible action data, we
build a DiffAero-based pipeline with complementary Isaac Lab and 3D Gaussian splatting
renderers. We further introduce a low-cost handheld collection device that couples
camera observations with motion estimates to recreate flight-like egocentric
trajectories, and a self-guidance procedure that improves temporal consistency across
overlapping trajectory chunks. Closed-loop simulation and real-world experiments show
that temporal visual context improves target tracking and object-search performance, and
that WAM-based policies can be executed on a physical quadrotor.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14997v1
- Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang
- Published: 2026-07-16T13:46:00Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
