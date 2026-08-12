---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.12702v1"
published: "2026-07-14T12:27:58Z"
age_days: 2
score: 32
created: 2026-07-17
concepts: ["机器人学习"]
---

# Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning

## 为什么重要

自动筛选分数：32

连接概念：[[机器人学习]]

## 摘要

Recent advances in humanoid robotics have highlighted the importance of deployable loco-
manipulation skills. Dribbling a soccer ball while evading active opponents requires
simultaneous balance, precise ball control, and awareness of a dynamic adversary under
onboard sensing and real-time constraints. Existing approaches typically separate
perception and motion, which can be effective in controlled settings but may fail under
occlusions, fast ball movements, and complex opponent interactions, since perception is
not directly optimized for control. We propose an integrated approach in which a
temporal depth encoder is embedded into a reinforcement learning policy through a task-
specific projection layer. We apply this framework to a simulated Booster T1 humanoid
robot and show that it is possible to learn vision-based, opponent-aware dribbling
directly from depth observations, without explicit state estimation or privileged scene
information. The learned policy achieves 100% success in nominal target-driven dribbling
and 96% success with a single static obstacle, while reaching 46% success against an
actively moving ball-attacker opponent. These results demonstrate that the proposed
framework supports robust vision-based dribbling in nominal and moderately dynamic
settings, and provides a strong foundation for handling more challenging moving-
adversary scenarios.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.12702v1
- Authors: Flavio Maiorana, Valerio Spagnoli, Eugenio Bugli, Flavio Volpi, Daniele Affinita, Vincenzo Suriani, Daniele Nardi, Luca Iocchi
- Published: 2026-07-14T12:27:58Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
