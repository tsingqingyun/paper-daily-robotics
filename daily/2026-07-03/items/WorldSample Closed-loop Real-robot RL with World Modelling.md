---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02431v1"
published: "2026-07-02T17:00:37Z"
age_days: 0
score: 39
created: 2026-07-03
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# WorldSample: Closed-loop Real-robot RL with World Modelling

## 为什么重要

自动筛选分数：39

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Reinforcement learning (RL) can overcome the demonstration-coverage limitation of
imitation learning (IL) by allowing robots to improve through trial-and-error
interaction beyond the states observed in demonstrations. However, deploying RL on real
robots remains constrained by high interaction costs, since each physical rollout is
costly and reflects only one realized action-outcome path. To address this challenge, we
propose WorldSample, a physically grounded data augmentation framework for real-robot RL
that closes a real-synthetic loop between physical rollouts, world-model generation, and
policy improvement. Grounded on real rollouts, WorldSample generates high-fidelity
synthetic transitions through a post-trained world model, which greatly lowers the
visual hallucination. Specifically, rather than simply using these transitions as real-
world experience, WorldSample introduces Policy-Paced Learning (PPL) to regulate the
training process through sample selection and scheduling, balancing useful augmentation
against value overestimation and mitigating the hallucination-induced noise. Experiments
on robot manipulation tasks involving contact-rich and precise tasks show that
WorldSample improves policy success rate by 28% while reducing training steps by 59%
compared with baselines. Furthermore, WorldSample improves world model visual fidelity
by 19.4dB in PSNR and 0.47 in SSIM over demonstration-only post-training, validating the
effectiveness of the real-synthetic loop for both policy and world model performance.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02431v1
- Authors: Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, Bofang Jia, Ziwei Wang
- Published: 2026-07-02T17:00:37Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
