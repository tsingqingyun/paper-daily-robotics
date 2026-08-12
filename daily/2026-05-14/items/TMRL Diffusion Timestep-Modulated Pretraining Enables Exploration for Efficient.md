---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12236v1"
published: "2026-05-12T15:07:04Z"
age_days: 1
score: 36
created: 2026-05-14
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

## 为什么重要

自动筛选分数：36

连接概念：[[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Fine-tuning pre-trained robot policies with reinforcement learning (RL) often inherits
the bottlenecks introduced by pre-training with behavioral cloning (BC), which produces
narrow action distributions that lack the coverage necessary for downstream exploration.
We present a unified framework that enables the exploration necessary to enable
efficient robot policy finetuning by bridging BC pre-training and RL fine-tuning. Our
pre-training method, Context-Smoothed Pre-training (CSP), injects forward-diffusion
noise into policy inputs, creating a continuum between precise imitation and broad
action coverage. We then fine-tune pre-trained policies via Timestep-Modulated
Reinforcement Learning (TMRL), which trains the agent to dynamically adjust this
conditioning during fine-tuning by modulating the diffusion timestep, granting explicit
control over exploration. Integrating seamlessly with arbitrary policy inputs, e.g.,
states, 3D point clouds, or image-based VLA policies, we show that TMRL improves RL
fine-tuning sample efficiency. Notably, TMRL enables successful real-world fine-tuning
on complex manipulation tasks in under one hour. Videos and code available at
https://weirdlabuw.github.io/tmrl/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12236v1
- Authors: Matthew M. Hong, Jesse Zhang, Anusha Nagabandi, Abhishek Gupta
- Published: 2026-05-12T15:07:04Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
