---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14433v1"
published: "2026-06-12T13:13:53Z"
age_days: 2
score: 30
created: 2026-06-15
concepts: ["机器人学习"]
---

# Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions

## 为什么重要

自动筛选分数：30

连接概念：[[机器人学习]]

## 摘要

The recent popularity of robotics, combined with the steadily decreasing cost of robotic
hardware, has lowered the entry barrier to robotics research and enabled rapid
advancements in the field. One of the primary examples is the Unitree Go2 quadruped
robot, which is often used by researchers in the areas of locomotion, navigation,
control, and others. Many researchers use the Go2 robot in combination with techniques
like imitation learning, reinforcement learning, and behavioral cloning to allow machine
learning systems to take full control of the robot. At the same time, many of those
techniques require demonstration data consisting of the robot's kinematics information
and actions applied to the motors. Obtaining such data is difficult, requires building
complex pipelines, and can take significant time. To aid in those kinds of efforts, we
present Kine2Go - a dataset with 800 diverse gait kinematics trajectory motion data for
the Unitree Go2 robot, derived from 40 distinct policies. Our pipeline accepts data from
various quadruped morphologies and translates them to a Go2-compatible format. Then we
use Reinforcement Learning to train policies following a given motion, and finally we
gather data from those policies, which grants robust, perturbed kinematic data with
corresponding motor-level actions.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14433v1
- Authors: Władysław Pałucki, Paweł Siwak, Krzysztof Ciebiera, Marek Cygan
- Published: 2026-06-12T13:13:53Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
