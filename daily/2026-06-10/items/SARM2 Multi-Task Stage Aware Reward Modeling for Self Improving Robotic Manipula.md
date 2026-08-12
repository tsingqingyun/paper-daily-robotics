---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10305v1"
published: "2026-06-09T01:46:23Z"
age_days: 0
score: 37
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation

## 为什么重要

自动筛选分数：37

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Fine-tuning vision-language-action (VLA) policies for long-horizon manipulation still
relies heavily on behavior cloning, which requires costly high-quality demonstrations
and keeps policies near the demonstration distribution. Reward models can reduce this
dependence by reweighting demonstrations and providing dense supervision for on-robot
reinforcement learning (RL), but they must be dense, accurate, and general. Existing
methods fall short: task-specific stage-aware models are accurate but require per-task
annotations, while general vision-language-model (VLM) reward models are broadly
applicable but too coarse for fine-grained long-horizon progress. We introduce RM, a
multi-task stage-aware reward model that combines an action-primitive-based stage
estimator with a multi-gate Mixture-of-Experts (MMoE) value head to produce dense per-
step rewards across manipulation tasks. Building on RM, we further propose SPIRAL (Self-
Policy Improvement via Reward-Aligned Learning), an on-policy reward-guided framework
that improves VLA policies from cheap autonomous rollouts. On a 10-task benchmark, RM
reduces value-estimation MSE by 80% over the strongest baselines; when used in SPIRAL,
it improves task success from around 50% to near-perfect performance on Folding Shorts
(58% to 100%) and Cleaning Whiteboard (50% to 90%), showing that high-quality dense
rewards are key to a stable robot data flywheel. Project website: https://qianzhong-
chen.github.io/sarm2.github.io/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10305v1
- Authors: Qianzhong Chen, Hau Zheng, Justin Yu, Suning Huang, Jiankai Sun, Ken Goldberg, Chuan Wen, Pieter Abbeel, Yide Shentu, Philipp Wu, Mac Schwager
- Published: 2026-06-09T01:46:23Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
