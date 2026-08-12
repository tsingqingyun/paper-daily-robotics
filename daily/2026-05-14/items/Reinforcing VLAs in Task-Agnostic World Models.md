---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12334v1"
published: "2026-05-12T16:16:15Z"
age_days: 1
score: 33
created: 2026-05-14
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Reinforcing VLAs in Task-Agnostic World Models

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Post-training Vision-Language-Action (VLA) models via reinforcement learning (RL) in
learned world models has emerged as an effective strategy to adapt to new tasks without
costly real-world interactions. However, while using imagined trajectories reduces the
sample complexity of policy training, existing methods still heavily rely on task-
specific data to fine-tune both the world and reward models, fundamentally limiting
their scalability to unseen tasks. To overcome this, we argue that world and reward
models should capture transferable physical priors that enable zero-shot inference. We
propose RAW-Dream (Reinforcing VLAs in task-Agnostic World Dreams), a new paradigm that
completely disentangles world model learning from downstream task dependencies. RAW-
Dream utilizes a world model pre-trained on diverse task-free behaviors for predicting
future rollouts, and an off-the-shelf Vision-Language Model (VLM) for reward generation.
Because both components are task-agnostic, VLAs can be readily finetuned for any new
task entirely within this zero-shot imagination. Furthermore, to mitigate world model
hallucinations, we introduce a dual-noise verification mechanism to filter out
unreliable rollouts. Extensive experiments across simulation and real-world settings
demonstrate consistent performance gains, proving that generalized physical priors can
effectively substitute for costly task-dependent data, offering a highly scalable
roadmap for VLA adaptation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12334v1
- Authors: Yucen Wang, Rui Yu, Fengming Zhang, Junjie Lu, Xinyao Qin, Tianxiang Zhang, Kaixin Wang, Li Zhao
- Published: 2026-05-12T16:16:15Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
