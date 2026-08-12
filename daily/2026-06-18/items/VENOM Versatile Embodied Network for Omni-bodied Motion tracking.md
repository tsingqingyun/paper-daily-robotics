---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.16696v1"
published: "2026-06-15T13:31:37Z"
age_days: 2
score: 35
created: 2026-06-18
concepts: ["多模态基础模型", "世界模型", "机器人学习"]
---

# VENOM: Versatile Embodied Network for Omni-bodied Motion tracking

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[世界模型]], [[机器人学习]]

## 摘要

Achieving expert-level expressive full-body motion tracking across multiple humanoids
solely from demonstration data remains a challenging and relatively an underexplored
problem in humanoid robot learning. Cross-embodiment motion tracking policies are mostly
trained by decoupling the control problem into upper and lower body control. This work
proposes VENOM, a cross-embodiment full-body motion tracking model for humanoids in
simulation. VENOM is a GPT-based motion tracker trained on multiple humanoid data that
can track the entire body without the requirement to split into upper and lower body
control. We curate a multi-humanoid motion tracking dataset called the VENOM dataset
that contains states, actions, and rewards and train VENOM and the baselines on this
dataset. In this letter, we evaluate VENOM's performance against baselines and show that
we can achieve a stable motion tracker across different humanoids more capable than an
MLP trained on multiple humanoid data with supervised learning alone, and also show that
despite lack of reward feedback, VENOM closely matches the tracking capability of
experts that were trained using asymmetric-actor critic reinforcement learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.16696v1
- Authors: Siddharth Padmanabhan, Kazuki Miyazawa, Takato Horii
- Published: 2026-06-15T13:31:37Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
