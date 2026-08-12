---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25414v1"
published: "2026-05-25T04:30:51Z"
age_days: 1
score: 28
created: 2026-05-26
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# How to Mitigate the Distribution Shift Problem in Robotics Control: A Robust and Adaptive Approach Based on Offline to Online Imitation Learning

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Distribution shift in imitation learning refers to the problem that the agent cannot
plan proper actions for a state that has not been visited during the training. This
problem can be largely attributed to the inherently narrow state-action coverage
provided by expert demonstrations over the full environment. In this paper, we propose a
robust offline to adaptive online imitation learning framework that handles the
distribution shift problem in a lifelong, multi-phase scheme. In the offline learning
phase, we leverage supplementary demonstrations to broaden the state-action coverage of
the policy by utilizing a discriminator to effectively train the policy with
supplementary demonstrations, thereby enhancing the robustness of the policy to
distribution shift. In the subsequent online inference phase, our framework detects the
occurrence of distribution shift and conducts self-supervised imitation learning from
online experiences to adapt the policy to the online environments. Through extensive
evaluations in MuJoCo environments, we demonstrate that our method exhibits better
robustness to distribution shift and better adaptation performance to online
environments than the baseline algorithms, which indicates superior performance of our
framework against the distribution shift.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25414v1
- Authors: Hyung-Suk Yoon, Seung-Woo Seo
- Published: 2026-05-25T04:30:51Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
