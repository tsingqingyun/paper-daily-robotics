---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29201v1"
published: "2026-06-28T05:01:27Z"
age_days: 2
score: 29
created: 2026-06-30
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Behavior Uncloning: Distilling Mode Redirection into Policy Weights without Inference-Time Steering

## 为什么重要

自动筛选分数：29

连接概念：[[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Behavior-cloned policies often learn multiple behavior modes from demonstration
datasets, including modes that are unsafe or otherwise undesired at deployment. For
example, a policy trained on diverse handover demonstrations may learn to pass a knife
blade-first. Standard remedies such as data curation and inference-time steering either
require access to the original demonstrations for full retraining or add substantial
inference-time overhead. To address this gap, we propose MoRE(Mode Redirection), which
redirects policy rollouts toward desired behavior modes through a short "uncloning"
step. Specifically, MoRE distills the redirection signal from a temporary mode
classifier into the policy weights to steer behavior. A retain loss balances this edit
by preserving desired-mode competence, allowing the standalone policy to suppress
unwanted modes with zero inference-time overhead. Across eight simulated and real-world
tasks, MoRE improves the average deployment success rate (SR) by 44 percentage points
over the original mixed-mode policy. Among all compared adaptation and steering
baselines, MoRE achieves the strongest SR and approaches the filtered-data retraining
reference, while preserving task competence and inference speed. MoRE also generalizes
across robot policy backbones, including Diffusion Policy and the Pi0.5 VLA, diverse
task categories, and real-world deployments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29201v1
- Authors: Hao Wang, Jiuzhou Lei, Dayou Li, Bangya Liu, Minghui Zheng, Manling Li, Ruohan Zhang, Zhiwen Fan
- Published: 2026-06-28T05:01:27Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
