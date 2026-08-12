---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22860v1"
published: "2026-06-22T05:07:08Z"
age_days: 1
score: 45
created: 2026-06-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning

## 为什么重要

自动筛选分数：45

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Recent advancements in generative imitation learning have significantly propelled the
field of robotic manipulation. However, the majority of existing models rely heavily on
Behavior Cloning (BC), a paradigm that suffers from compounding errors and
distributional shift. Consequently, the efficacy of these models in practical industrial
deployments remains limited. To address these challenges, we introduce a novel, plug-
and-play fine-tuning pipeline designed to facilitate the robust deployment of Vision-
Language-Action (VLA) models in real-world environments. In contrast to contemporary
reinforcement learning (RL) fine-tuning strategies, which are often constrained by
specific model architectures, our proposed framework is model-agnostic and adaptable to
a diverse range of VLA models. We conceptualize VLA-generated actions as a unified
interface, upon which we train a residual policy. This policy is designed to rectify
suboptimal actions and address the distributional shift inherent in imitation learning.
Additionally, we incorporate human-in-the-loop guidance to ensure safe exploration and
maximize training efficiency. We conduct experiments directly in real-world robotic
settings. The results demonstrate that within only 1.5 hour of real-world online RL
training, the average success rate exceeds 95% on real robots. Our work presents a
practical solution for deploying behavior cloning models in industrial scenarios.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22860v1
- Authors: Jingyi Liu, Zhaohong Mai, ShunSen He, Hang Ren, Chao Wang, Shunbo Zhou, XiaoDong Wu, Heng Zhang
- Published: 2026-06-22T05:07:08Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
