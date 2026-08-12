---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24628v1"
published: "2026-06-23T14:24:07Z"
age_days: 1
score: 29
created: 2026-06-25
concepts: ["智能体 Agent", "世界模型"]
---

# ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Deploying robots in unstructured real-world environments needs accurate, interactive
models of the objects. Constructing these models at scale remains a critical bottleneck
for robotic system integration. We present ArtiTwinSplat, a framework that automatically
constructs articulated, photo-realistic digital twins of objects directly from RGB-D
videos, requiring no CAD models, simulation assets, or manual annotations. Our method is
built on 3D Gaussian Splatting that preserve geometric fidelity and photometric realism,
coupled with an unsupervised articulation discovery pipeline that recovers part
structure and joint kinematics from observed motion alone. With tracking and
optimization stages our method provides stable, queryable digital twins that support
real-time rendering, viewpoint control, and interactive manipulation. Unlike prior
methods confined to simulation, ArtiTwinSplat operates directly on real-world
observations and produces twins that are immediately usable by downstream robot planning
and learning systems. This method offers a practical, scalable pathway toward digital
twin construction, lowering the integration barrier for articulated object manipulation
in embodied AI and human-robot collaboration contexts.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24628v1
- Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum
- Published: 2026-06-23T14:24:07Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
