---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.26490v1"
published: "2026-09-22T14:28:44Z"
age_days: 1
score: 30
created: 2026-09-24
concepts: ["具身智能评测与基准"]
---

# Benchmarking Robots for Everyday Environments: From Lab Experiments to Real-World Operations

> [!summary] 先说人话（基于摘要）
> 这项研究把公共环境机器人的评价扩展到任务完成、交互、安全和经济可行性，尝试回答实验室能运行的机器人能否承担日常运营。

## 问题

传统实验室指标与公共场所运营需求存在脱节，单看技术性能不足以描述非结构化、人本环境中的实际部署表现。

## 创新点或方法

机器人、人机交互、安全和经济领域的专家共同制定并迭代评测概念，在公园清洁、地下通道清洁和图书馆交互辅助三个用例中开展现场评价。

## 证据

研究持续于 2023—2025 年，覆盖三种机器人、七次基准活动，包括一次共识研讨和六次现场评测，每用例两次。摘要归纳了部署关键因素，但未提供量化性能或经济结果。

## 局限

三种机器人对应三个不同用例，摘要没有说明如何形成可复用、可比较的评分尺度；需核查定性共识如何转化为操作化指标。

- **判断**：做真实部署评测值得读评价框架；若重点是 VLA 或世界模型算法，阅读优先级较低。

## 研究关联

对具身评测研究者，它提醒基准需要覆盖运营中的多方目标，适合补充只测任务成功率的研究评估。

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/Benchmarking Robots for Everyday Environments From Lab Experiments to Real-World.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This study introduces an interdisciplinary framework for benchmarking robots deployed in public environments, addressing the gap between traditional laboratory metrics and real-world benchmarking requirements. We evaluate three distinct robots across diverse use cases - outdoor park cleaning, pedestrian underpass cleaning, and interactive library assistance - each representing unique challenges in public daily life. Over a three-year benchmarking process (2023-2025) comprising seven benchmarking events, a consensus workshop and six on-site evaluations (two per use case), we utilized realistic indoor and outdoor test environments to assess not only technical performance but also the broader implications of deploying robots in unstructured, human-centric settings. An expert panel, spanning robotics, human-robot interaction, safety, and economics, systematically developed and refined an evaluation concept to analyze the transition from laboratory prototypes to operational systems. Our findings highlight critical factors for successful deployment, including task fulfillment, interaction quality, safety, and economic feasibility. This work provides actionable insights for researchers and practitioners aiming to bridge the gap between robotic innovation and real-world applicability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.26490v1
- Authors: Raphael Memmesheimer, Martina Overbeck, Dominik Beyer, Björn Kral, Sabine Bellmann, Sven Schneider, Jan Zimmermann, Anna-Maria Meer, Medina Klicic, Simone Roth, Carolin Straßmann, Alexander Arntz, Marlene Wessels, Johannes Kraus, Paul Schweidler, Tristan Schnell, Christoph Zimmermann, Benedikt Pulver, Wilhelm Stork, Martin Gersch, Sven Behnke, Arne Rönnau
- Published: 2026-09-22T14:28:44Z
- Age days: 1

</details>
