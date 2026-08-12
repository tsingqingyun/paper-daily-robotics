---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20209v1"
published: "2026-06-18T13:21:40Z"
age_days: 1
score: 28
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# FlowMaps: Modeling Long-Term Multimodal Object Dynamics with Flow Matching

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]]

## 摘要

Joint spatial and temporal understanding of 3D scenes is a crucial requirement for
robots deployed in everyday household environments. Such agents must not only comprehend
and navigate spatial layouts, but also reason about how these spaces evolve over time.
In particular, humans interact with objects daily, causing them to change position
throughout the environment and making it difficult for robots to reliably associate
current observations with previously seen objects. However, these interactions are not
random: human habits and routines induce spatio-temporally consistent patterns in object
locations, which robotic agents can potentially learn and then exploit for downstream
tasks such as navigation. To this end, we introduce FlowMaps, a latent flow matching
model for estimating multimodal distributions over the future locations of dynamic
objects in a continuous 3D space. By learning the implicit dependencies among objects
and their temporal evolution, FlowMaps predicts likely changes in object locations
conditioned on past human interactions, while supporting generalization across
previously unseen environments that share similar object routines. To demonstrate the
utility of this method, we deploy FlowMaps in a downstream dynamic Object Navigation
task in both simulated and real-world environments. Across more than 600 episodes,
FlowMaps outperforms state-of-the-art approaches, showing that modeling object dynamics
through continuous, multimodal spatio-temporal distributions improves robotic search and
navigation in changing household environments. Code and additional material is available
at https://fra-tsuna.github.io/flowmaps/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20209v1
- Authors: Francesco Argenziano, Miguel Saavedra-Ruiz, Sacha Morin, Charlie Gauthier, Daniele Nardi, Liam Paull
- Published: 2026-06-18T13:21:40Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
