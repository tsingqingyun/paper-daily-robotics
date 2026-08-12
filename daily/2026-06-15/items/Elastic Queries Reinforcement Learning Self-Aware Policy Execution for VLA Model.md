---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14375v1"
published: "2026-06-12T12:06:41Z"
age_days: 2
score: 34
created: 2026-06-15
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models are powerful action generators for robot
manipulation, but they are typically executed with fixed inference and replanning
schedules. This rigidity ignores the uneven difficulty of robot control: contact-rich or
uncertain states may need more computation and fresher feedback, while easier states can
often be handled with fewer inference steps and longer open-loop execution. We propose
Elastic Queries Reinforcement Learning (EQRL), a framework that makes each VLA policy
query elastic. A lightweight latent-schedule adaptor jointly selects the latent input,
denoising budget, and action chunk length, without fine-tuning the underlying VLA model.
To make scheduling difficulty-aware, EQRL trains a critic over the joint latent-schedule
action and derives a state difficulty signal from critic ensemble disagreement. This
signal guides compute toward difficult states, while a learned residual allows task-
driven correction. We formulate variable chunk execution as query-level macro-action RL
with chunk-dependent discounting and an amortized number-of-function-evaluations (NFE)
budget. Across simulation and real-robot manipulation, EQRL reduces amortized inference
cost while preserving or improving task success.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14375v1
- Authors: Ge Wang, Xinyu Tan, Xiang Li, Man Luo, Chengsi Yao, Shenhao Yan, Jiahao Yang, Fan Feng, Honghao Cai, Xiangyuan Wang, Zhixin Mai, Yiming Zhao, Yatong Han, Zhen Li
- Published: 2026-06-12T12:06:41Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
