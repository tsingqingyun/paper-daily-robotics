---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07107v1"
published: "2026-06-05T10:01:37Z"
age_days: 2
score: 31
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]]

## 摘要

Most vision-language-action (VLA) models map observations directly to actions without
explicit intermediate planning, which limits performance on long-horizon tasks where
early mistakes compound. We propose Coarse-to-Control, a plan-execute VLA that
introduces planning natively in the action-token space. The key idea is to let the
policy first predict a compact sequence of coarse action tokens that summarize the
intended future trajectory, and then generate executable action tokens conditioned on
this plan. Because both planning and execution share a unified discrete action
vocabulary, the plan stays close to the control manifold and provides directly
actionable guidance rather than an abstract hint that must be translated back to motor
commands. Experiments on LIBERO, SimplerEnv-WidowX, and real-world manipulation tasks
show that action-token planning consistently improves over direct action generation,
with the largest gains on long-horizon multi-stage tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07107v1
- Authors: Jinhao Wu, Shiduo Zhang, Yicheng Liu, Xiaopeng Yu, Sixian Li, Siyin Wang, Hang Zhao, Jing Huo, Yang Gao, Jingjing Gong, Xipeng Qiu, Yu-Gang Jiang
- Published: 2026-06-05T10:01:37Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
