---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20209v1"
published: "2026-06-18T13:21:40Z"
age_days: 1
score: 28
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# FlowMaps: Modeling Long-Term Multimodal Object Dynamics with Flow Matching

> [!summary] 一句话结论（基于摘要）
> Across more than 600 episodes, FlowMaps outperforms state-of-the-art approaches, showing that modeling object dynamics through continuous, multimodal spatio-temporal distributions improves robotic search and navigation in changing household environments.

## 关键点

- **问题**：In particular, humans interact with objects daily, causing them to change position throughout the environment and making it difficult for robots to reliably associate current observations with previously seen objects.
- **创新点 / 方法**：To this end, we introduce FlowMaps, a latent flow matching model for estimating multimodal distributions over the future locations of dynamic objects in a continuous 3D space.
- **证据**：Across more than 600 episodes, FlowMaps outperforms state-of-the-art approaches, showing that modeling object dynamics through continuous, multimodal spatio-temporal distributions improves robotic search and navigation in changing household environments.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

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

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20209v1
- Authors: Francesco Argenziano, Miguel Saavedra-Ruiz, Sacha Morin, Charlie Gauthier, Daniele Nardi, Liam Paull
- Published: 2026-06-18T13:21:40Z
- Age days: 1

</details>
