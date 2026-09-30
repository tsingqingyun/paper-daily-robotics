---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.26360v1"
published: "2026-09-22T13:02:54Z"
age_days: 1
score: 31
created: 2026-09-24
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering

> [!summary] 先说人话（基于摘要）
> HFLEX-EQA 让机器人回答环境问题时，结合已经看到的内容和估计的房间结构，主动寻找可能藏有答案但尚未进入的房间。

## 问题

具身问答要求在未知环境中探索取证。现有 VLM 加语义地图或场景图的方法主要依赖局部观测，未充分利用建筑结构来决定下一步去哪里。

## 创新点或方法

从 RGB-D 逐步构建分层场景图与开放词汇占据地图，VLM 综合场景图、相关图像、探索历史和估计拓扑平面图规划。房间发现策略结合平面图与语义前沿，优先探索相关但未见的房间类型。

## 证据

在 OpenEQA 和 ExploreEQA 上评测，并部署到真实室内环境的四足机器人。摘要报告结构先验结合分层规划有益，未给出可核查的结果数字。

## 局限

需核查拓扑平面图如何估计、错误结构先验怎样影响探索，以及问答准确率与探索代价分别改善多少。

- **判断**：做 EQA 或室内探索值得读规划流程，量化收益和对平面图误差的依赖需查全文。

## 研究关联

对具身智能体和多模态规划研究者，它提供了将局部视觉证据与全局结构假设结合的方法，直接服务于目标导向探索。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied Question Answering (EQA) requires an agent to explore a previously unseen environment, gather relevant information, and answer questions about the scene. Recent approaches leverage Vision-Language Models (VLMs) together with semantic maps or scene graphs to guide exploration. However, exploration is typically driven only by local observations, while structural priors about the environment remain largely unused. We propose HFLEX-EQA, a hierarchical EQA framework that combines online scene graph construction, VLM- based planning, semantic frontier exploration, and floorplan priors. The system incrementally builds a hierarchical scene graph and an open-vocabulary occupancy map from RGB-D observations, enabling a VLM to jointly reason over the scene graph, task-relevant visual observations, exploration history, and an estimated topological floorplan. Furthermore, we introduce a room-discovery strategy that leverages the floorplan and open-vocabulary frontier semantics to guide exploration toward semantically relevant yet currently unobserved room types. We evaluate HFLEX-EQA on the OpenEQA and ExploreEQA benchmarks and demonstrate deployment on a quadruped robot in real indoor environments. Our results demonstrate the benefit of combining VLM-based hierarchical planning with structural floorplan priors for the EQA task.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.26360v1
- Authors: Albert Gassol Puigjaner, Kostas Alexis
- Published: 2026-09-22T13:02:54Z
- Age days: 1

</details>
