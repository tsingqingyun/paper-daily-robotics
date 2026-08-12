---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23085v1"
published: "2026-06-22T09:32:28Z"
age_days: 1
score: 39
created: 2026-06-24
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents

## 为什么重要

自动筛选分数：39

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Long-horizon tasks are common in real-world robotic deployments, yet failure detection
for such tasks remains underexplored. Detecting failures in long-horizon robotic tasks
is particularly challenging because failure onset is often ambiguous and dense temporal
annotations are typically unavailable. We present Foresight, a failure detection
framework that monitors manipulation trajectories using latent representations from an
action-conditioned world model. Foresight is trained using only final task-level success
or failure labels. By leveraging predictive world-model embeddings, our method provides
a unified framework for failure detection across different policies. We further use
functional conformal prediction (FCP) to calibrate detection thresholds adaptively. We
evaluate Foresight with state-of-the-art vision-language-action policies in simulation
on LIBERO-Long, ManiSkill-Long, and BEHAVIOR-1K, compare it against state-of-the-
artfailure detection methods, and validate it on real robots with three long-horizon
tasks on a ReactorX-200 arm and one task on a Franka arm. Our results suggest that
action-conditioned world-model embeddings provide a scalable representation for reliable
failure monitoring in long-horizon manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23085v1
- Authors: Haoran Zhang, Yifu Lu, Boyang Wang, Xuhui Kang, Yen-Ling Kuo, Zezhou Cheng, Mengdi Wang, Odest Chadwicke Jenkins
- Published: 2026-06-22T09:32:28Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
