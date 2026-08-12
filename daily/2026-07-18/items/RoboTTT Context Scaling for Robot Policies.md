---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15275v1"
published: "2026-07-16T17:59:06Z"
age_days: 1
score: 35
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoboTTT: Context Scaling for Robot Policies

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Recent robot foundation models operate with single-step or short-history visuomotor
context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and
training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude
beyond state-of-the-art policies, without growing inference latency. At this context
length, we unlock new robot capabilities: one-shot in-context imitation from human video
demonstrations, on-the-fly policy improvement, robustness to perturbations, and stronger
performance on multi-stage, long-horizon tasks. We also observe, for the first time,
steady gains in closed-loop performance as pretraining context length scales. At its
core, RoboTTT integrates Test-Time Training into robot foundation models such as Vision-
Language-Action policies, yielding a sequence model whose recurrent state consists of
fast weights, parameters updated by gradient descent during both training and inference,
compressing histories into weight space and retrieving contextual information for long-
context conditioning. To scale training context length, the recipe combines sequence
action forcing with truncated backpropagation through time. On challenging real-robot
manipulation tasks, RoboTTT improves overall performance by 87% over the single-step
context baseline and fully completes a five-minute, ten-stage assembly task, which no
baseline ever does. RoboTTT trained with 8K-timestep context outperforms the same model
pretrained with 1K timesteps by 62%, suggesting context length as a new scaling axis for
robot foundation models. Videos are available at
https://research.nvidia.com/labs/gear/robottt/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15275v1
- Authors: Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge, Jimmy Wu, Tianyuan Dai, Scott Reed, Li Fei-Fei, Yuke Zhu, Linxi "Jim" Fan
- Published: 2026-07-16T17:59:06Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
