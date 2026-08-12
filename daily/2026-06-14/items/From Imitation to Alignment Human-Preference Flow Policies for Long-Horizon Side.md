---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12603v1"
published: "2026-06-10T19:01:31Z"
age_days: 3
score: 27
created: 2026-06-14
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# From Imitation to Alignment: Human-Preference Flow Policies for Long-Horizon Sidewalk Navigation

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Autonomous long-horizon sidewalk navigation is essential for micro-mobility applications
such as robotic food delivery and assistive electronic wheelchairs. Unlike autonomous
driving on the road, long-horizon sidewalk navigation requires precise maneuvering
through unpredictable sidewalk terrains and pedestrians, with a lightweight perception
stack as minimal as a single monocular RGB camera. While imitation learning (IL) from
demonstrations offers a practical solution, the resulting autopilot policy often suffers
from compounding errors, a lack of social compliance on sidewalks, and deficiencies in
counterfactual reasoning to handle complex situations. To address these challenges, we
introduce FlowPilot, a mapless navigation policy that achieves robust and efficient
long-horizon navigation performance using only a monocular RGB camera. We first propose
to use anchored flow matching as an action representation for policy pre-training on
large-scale robot fleet data and to capture the diverse, complex, multimodal
distribution of sidewalk navigation behaviors. To bridge the gap between imitation and
alignment, we further design a human-in-the-loop preference learning scheme to tune the
policy on a small amount of human intervention data. It strengthens the model's
counterfactual reasoning and social compliance on sidewalks. We evaluate FlowPilot
through extensive simulation and real-world experiments in diverse sidewalk
environments. FlowPilot achieves 42% success rate and 66% route completion in
simulation, while FlowPilot-HP further improves real-world robustness and social
compliance, reducing IR by 40.0% and NIR by 52.1% relative to the base model.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12603v1
- Authors: Honglin He, Zhizheng Liu, Yukai Ma, Bolei Zhou
- Published: 2026-06-10T19:01:31Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
