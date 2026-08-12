---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01721v1"
published: "2026-07-02T05:20:47Z"
age_days: 4
score: 25
created: 2026-07-06
concepts: ["多模态基础模型", "世界模型", "机器人学习"]
---

# CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning

## 为什么重要

自动筛选分数：25

连接概念：[[多模态基础模型]], [[世界模型]], [[机器人学习]]

## 摘要

Reward design remains a central challenge in reinforcement learning (RL). Hand-crafted
rewards are often difficult to specify and may lead to suboptimal policies, while
learned rewards from preferences can suffer from inefficiency and unstable training.
Inspired by the dual nature of human learning explored in cognitive science, we
decompose rewards into two complementary components: Formal Rewards (FR), explicitly
designed based on task knowledge, and Residual Rewards (RR), learned from observations
to capture implicit and nuanced preferences. Based on this decomposition, we propose
CoRe, a hybrid framework that integrates FR and RR with vision-language models (VLMs)
feedback to achieve preference-aligned policies without human involvement. Our
contributions are twofold: (1) We propose a Formal Reward Module (FRM) that leverages
VLMs to iteratively design and optimize FR based on task knowledge and preference
feedback, enabling the continual improvement of policy during training; (2) We introduce
a Residual Reward Module (RRM) that learns RR from video-level preference by employing
VLMs to generate preference labels and capturing nuanced rewards that complement FR,
ensuring alignment with human intent. Through the synergy of FRM and RRM, CoRe enables
the automatic construction of reliable rewards that are efficient and preference-
aligned. Extensive experiments demonstrate that CoRe outperforms existing approaches in
terms of policy learning effectiveness and efficiency on ten robotic manipulation tasks
in simulation and five real-worlds. Videos can be found on our project website:
https://core-2026.github.io/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01721v1
- Authors: Hexian Ni, Tao Lu, Yinghao Cai
- Published: 2026-07-02T05:20:47Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
