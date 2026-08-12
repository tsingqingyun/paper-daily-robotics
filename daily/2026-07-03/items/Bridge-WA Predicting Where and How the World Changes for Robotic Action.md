---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02195v1"
published: "2026-07-02T14:03:44Z"
age_days: 0
score: 37
created: 2026-07-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Bridge-WA: Predicting Where and How the World Changes for Robotic Action

## 为什么重要

自动筛选分数：37

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

General-purpose vision-language-action models benefit from large vision-language priors,
but effective manipulation also requires anticipating action-relevant scene changes.
Existing world-action models often rely on large generative world models or dense future
rollouts, which are expensive and spend capacity on visual details weakly coupled to
control. We present Bridge-WA, a lightweight world-action framework that distills a
frozen future-change teacher into three compact priors: future tokens for intended
outcomes, change maps for intervention support, and motion-flow maps for local
transition direction. A WorldBridge conditions the action transformer on these priors
through multi-source attention memories and spatial-temporal biases, while the teacher
model is removed at inference. Across VLABench, RoboTwin2.0, LIBERO-Plus and real-robot
evaluations, Bridge-WA improves task success, progress, and robustness, with
particularly clear gains under out-of-distribution visual shifts. By focusing action
generation on where and how the scene will change, Bridge-WA suppresses nuisance
appearance factors such as background, lighting, and distractors, leading to better
generalization without deployment-time dense future-image generation. Code and
visualizations are available at: https://hcplab-sysu.github.io/BRIDGE-WA .

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02195v1
- Authors: Yongjie Bai, Hanting Wang, Mingtong Dai, Qijun Zhong, Yang Liu, Liang Lin
- Published: 2026-07-02T14:03:44Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
