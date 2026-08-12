---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01651v1"
published: "2026-07-02T03:23:40Z"
age_days: 1
score: 33
created: 2026-07-03
concepts: ["机器人学习", "具身智能评测与基准"]
---

# One Demonstration Is Enough for Real-World Robotic Reinforcement Learning

## 为什么重要

自动筛选分数：33

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Learning effective robot control policies on physical hardware is challenging due to
costly data collection and the difficulty of reward specification. Prior work has
incorporated demonstrations into reinforcement learning (RL), yet existing approaches
either require large numbers of demonstrations or depend on continuous human
intervention during training. To address these limitations, we present AutoSERL, a
framework that leverages a single demonstration to fully automate the intervention
process in real-world robot RL. The framework includes three complementary mechanisms to
accomplish certain tasks: a sliding window intervention mechanism that continuously
guides exploration to prevent local optima and unsafe deviations, a safety recovery
mechanism that detects and corrects failure states via predefined trajectory recovery
points, and an intervention termination criterion that automatically disables guidance
once the policy can independently complete the task, preserving its exploration
advantage. We evaluate AutoSERL on six contact-intensive manipulation tasks across two
robot platforms, spanning insertion, hanging, and hinge-based tasks. AutoSERL
consistently outperforms SERL initialized with 20 demonstrations, behavior cloning, and
MILES -- a dedicated one-shot imitation learning baseline -- across all tasks while
matching HIL-SERL, achieves 100% success rate on insertion tasks, and demonstrates
improved robustness to positional variations, all from a single demonstration. Code and
videos are available on our project website: https://autoserl.github.io/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01651v1
- Authors: Yuwan Liu, Hongze Yu, Song Liu, Yuhan Wang, Junge Zhang, Yaodong Yang, Yuanpei Chen, Ceyao Zhang
- Published: 2026-07-02T03:23:40Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
