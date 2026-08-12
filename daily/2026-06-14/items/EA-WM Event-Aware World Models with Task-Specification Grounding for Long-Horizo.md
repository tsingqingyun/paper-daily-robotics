---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13053v1"
published: "2026-06-11T08:35:37Z"
age_days: 2
score: 27
created: 2026-06-14
concepts: ["智能体 Agent", "世界模型"]
---

# EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation

## 为什么重要

自动筛选分数：27

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Pretrained-feature world models provide a useful substrate for robot imagination, but
visual or latent prediction alone does not determine whether an imagined future
satisfies task-relevant events. Long-horizon manipulation requires progress signals that
are relational, predicate-level, and physically grounded: whether an object has moved,
whether a drawer or contact state has changed, whether a placement predicate is
satisfied, and whether a candidate future is reliable enough for execution. We introduce
EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics
with task-specification-grounded event prediction and verification. EA-WM rolls out
candidate futures in pretrained visual-feature space, decodes them into structured event
states, and scores them using task-progress, semantic-consistency, physical-feasibility,
and uncertainty terms. The verifier guides sampling-based planning, gates candidate
actions, and, in the contact-sensitive LIBERO wine-rack setting, selects among
PPOgenerated proposals. Across navigation, deformable-object, wall-constrained, and
languagedescribed manipulation studies, EA-WM shows that event-aware verification can
make featurespace world models more interpretable and better aligned with task progress.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13053v1
- Authors: Kailin Wang, Haoxiang Jie, Yaoyuan Yan, Jiacheng Zhou, Zhiyou Heng
- Published: 2026-06-11T08:35:37Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
