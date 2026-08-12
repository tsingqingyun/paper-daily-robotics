---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10614v1"
published: "2026-06-09T09:13:36Z"
age_days: 0
score: 35
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Robotic foundation models pre-trained on human demonstration videos have shown promise,
but a significant embodiment gap remains when the resulting policies are deployed on
real robots. A common remedy is to fine-tune these models on robot-specific
demonstrations. However, robot data collection can be prohibitively expensive and time-
consuming, which is particularly acute in dexterous manipulation, e.g., teleoperating a
multi-fingered hand for even a single atomic task can take days. To address this, we
introduce Dexterous Point Policy, a framework that learns dexterous manipulation
policies directly from human videos and requires no robot demonstrations. Our core
insight is that a unified 3D keypoint representation can bridge human and robot
embodiments when used for both observations and actions. Specifically, we extract 3D
keypoints of task-relevant objects and human hands from raw videos, and train an
autoregressive transformer over these keypoints. We observe that at the keypoint level,
specifically the wrist and fingertips, human and robot behaviors closely align, enabling
direct policy transfer. On a suite of real-robot tasks spanning pick-and-place and tool
use, Dexterous Point Policy attains 75.0% success, whereas a state-of-the-art VLA
baseline reaches only 1.0%. Furthermore, our method generalizes strongly to unseen
scenarios, including multi-object environments and novel object categories.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10614v1
- Authors: Beomjun Kim, Seong Hyeon Park, Seunghoon Sim, Seungjun Moon, Sanghyeok Lee, Jinwoo Shin
- Published: 2026-06-09T09:13:36Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
