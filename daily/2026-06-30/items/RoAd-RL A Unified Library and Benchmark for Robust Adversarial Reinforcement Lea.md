---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29867v1"
published: "2026-06-29T07:03:45Z"
age_days: 1
score: 32
created: 2026-06-30
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RoAd-RL: A Unified Library and Benchmark for Robust Adversarial Reinforcement Learning

## 为什么重要

自动筛选分数：32

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Deep Reinforcement Learning (DRL) has achieved significant success in robotics and
autonomous systems, yet remains vulnerable to adversarial perturbations that can
severely degrade performance. Research in adversarial reinforcement learning is often
limited by fragmented implementations, inconsistent evaluation protocols, and poor
reproducibility. To address these challenges, we present \textbf{RoAd-RL}, an open-
source benchmarking framework that provides unified abstractions for policies, attacks,
defenses, and robustness metrics, together with reproducible evaluation pipelines and
seamless integration with Stable-Baselines3 and Gymnasium. We evaluate DQN, PPO, and SAC
agents in LunarLander and Highway-v0 under 192 attack-defense configurations. Results
reveal substantial variations in robustness across environments and show that some
commonly used defenses can be more detrimental than the attacks they aim to mitigate,
while temporal smoothing consistently achieves strong performance. RoAd-RL establishes a
standardized benchmark for adversarial reinforcement learning research and is publicly
available at https://pypi.org/project/road-rl.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29867v1
- Authors: Adithya Mohan, Daniel Kriegl, Torsten Schön
- Published: 2026-06-29T07:03:45Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
