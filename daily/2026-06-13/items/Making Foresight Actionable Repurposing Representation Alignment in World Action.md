---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12217v1"
published: "2026-06-10T15:31:25Z"
age_days: 2
score: 30
created: 2026-06-13
concepts: ["世界模型", "视觉语言动作模型 VLA"]
---

# Making Foresight Actionable: Repurposing Representation Alignment in World Action Models

## 为什么重要

自动筛选分数：30

连接概念：[[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

World Action Models (WAMs) offer a promising route for robot manipulation by using video
generation models to model future scene evolution before producing control actions.
However, our empirical observations reveal a phenomenon: generating plausible visual
futures does not always guarantee the extraction of accurate actions. To diagnose this
failure, we conduct action-head attention analysis and causal interventions. We find
that the action decoder fails to focus on task-relevant interaction regions and remains
sensitive to perturbations in task-irrelevant areas. This reveals a representation
mismatch: hidden states optimized for visual reconstruction are not inherently organized
in a form useful for low-level action control. In this paper, we propose AGRA, an
Action-Grounded Representation Alignment objective that regularizes the world-action
interface by aligning intermediate video diffusion features with spatially coherent
semantic representations from a foundation visual encoder. We evaluate AGRA on real-
world manipulation tasks. Experiments show that AGRA makes world model representations
more action-grounded: by focusing the action decoder on the correct interaction regions,
it improves object localization accuracy and affordance understanding, and makes the
policy more robust to perturbations in task-irrelevant regions. As a result, AGRA
consistently improves both in-distribution performance and out-of-distribution
generalization over the baseline world action model.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12217v1
- Authors: Lu Qiu, Yizhuo Li, Yi Chen, Yuying Ge, Yixiao Ge, Xihui Liu
- Published: 2026-06-10T15:31:25Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
