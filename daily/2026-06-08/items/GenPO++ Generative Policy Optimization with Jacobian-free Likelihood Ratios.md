---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06967v1"
published: "2026-06-05T06:54:09Z"
age_days: 2
score: 30
created: 2026-06-08
concepts: ["多模态基础模型", "机器人学习"]
---

# GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[机器人学习]]

## 摘要

Generative policies provide expressive and multimodal action distributions, making them
attractive for reinforcement learning (RL) in complex continuous-control tasks. Among
them, flow-based policies are especially appealing because they generate actions through
deterministic transport maps. However, applying such generative policies to likelihood-
based on-policy learning remains limited by the difficulty of evaluating the probability
of executed actions. Existing flow RL methods either replace the true action-density
ratio with approximate surrogates, which can introduce biased updates, or recover exact
likelihoods through dummy-action augmentation, which enlarges the policy space and
increases computation. In this work, we propose GenPO++, a reversible generative policy
optimization framework that uses history states as auxiliary memory in a high-order
reversible ODE solver, yielding exact inversion without changing the original action
dimension. The resulting generative policy map has a log-determinant determined only by
fixed solver coefficients, enabling exact and Jacobian-free likelihood-ratio
computation. This design preserves the expressiveness of generative flow policies while
avoiding both action ratio bias and dummy-action overhead. We evaluate GenPO++ on large-
scale simulated control, fine-tuning, and real-world robotic manipulation tasks, where
it achieves competitive or superior performance over state-of-the-art on-policy RL
methods, while improving training stability and computational efficiency.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06967v1
- Authors: Ke Hu, Shutong Ding, Panxin Tao, Jingya Wang, Ye Shi
- Published: 2026-06-05T06:54:09Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
