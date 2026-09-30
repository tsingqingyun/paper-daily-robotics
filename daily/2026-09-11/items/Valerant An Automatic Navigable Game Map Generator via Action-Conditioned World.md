---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09418v1"
published: "2026-09-08T20:17:48Z"
age_days: 2
score: 33
created: 2026-09-11
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration

> [!summary] 先说人话（基于摘要）
> We present \textsc{Valerant}, a training-free framework that transforms a pretrained action-conditioned world model into a WAM for exploring and constructing 3D game maps.

## 问题

Although WAMs are rapidly advancing embodied AI, general-purpose counterparts remain largely unexplored in games.

## 创新点或方法

We present \textsc{Valerant}, a training-free framework that transforms a pretrained action-conditioned world model into a WAM for exploring and constructing 3D game maps.

## 证据

摘要未报告明确实验结论；需阅读全文核查。


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Valerant An Automatic Navigable Game Map Generator via Action-Conditioned World.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) couple predictive world modeling with action generation, allowing anticipated future states to guide agent behavior. Although WAMs are rapidly advancing embodied AI, general-purpose counterparts remain largely unexplored in games. Existing game-oriented approaches often combine action-conditioned world models with external policies and reward functions to realize WAM-like decision-making, yet they operate mainly in 2D visual observation space and do not instantiate persistent 3D geometry. Extending this paradigm to 3D games introduces a distinct challenge. In autonomous driving and robotics, the physical environment exists independently of the model, providing a persistent 3D world in which selected actions can be executed. Games have no such external substrate; the virtual world itself must be instantiated. Most playable games require a persistent and navigable space, while 3D games additionally require explicit geometry that supports movement and interaction. Action-conditioned video rollouts provide visual observations but not this spatial representation. We present \textsc{Valerant}, a training-free framework that transforms a pretrained action-conditioned world model into a WAM for exploring and constructing 3D game maps. By coupling predictive visual rollouts with SLAM-based spatial reconstruction and exploration-driven action selection, \textsc{Valerant} progressively transforms a single image into a persistent 3D game map. This framework extends WAM-based interaction beyond 2D visual simulation and offers a new approach to reducing manual effort in 3D game-map creation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09418v1
- Authors: Yiran Qiao, Feng Wang, Jing Ma
- Published: 2026-09-08T20:17:48Z
- Age days: 2

</details>
