---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24189v1"
published: "2026-09-21T07:01:14Z"
age_days: 1
score: 31
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent"]
---

# A Topological Representation with Object-Path Graphs for Open-Vocabulary Instance Navigation

> [!summary] 先说人话（基于摘要）
> 这项object–path graph方法把“目标是什么”和“怎么走过去”放进同一张拓扑图。机器人通过图上的全局路线和局部视觉伺服导航，不再让语义图与导航表示彼此脱节。

## 问题

已有方法或逐步做语言引导决策，或依赖在线探索；场景图虽然能存语义记忆，下游导航却仍依赖稠密度量地图，语义定位与移动执行没有统一。

## 创新点或方法

物体—路径图同时支持开放词汇目标定位、图上定位和导航；全局规划选取节点路线，局部用轻量节点定位及语义视觉伺服完成节点间移动。

## 证据

HM3D和Replica实验报告开放词汇物体定位具有竞争力、导航有效，真实机器人实验验证可用性；摘要未给出可核查的结果数字。

## 局限

不使用稠密度量重建不等于不需要环境先验，需核查图如何构建，以及节点间执行对环境变化的适应范围。

- **判断**：做语义导航可选读图构造与执行机制，是否优于既有地图方案需看全文成本和成功率。

## 研究关联

对具身Agent和导航研究，提供了让语义记忆直接服务移动执行的表示方案；对操作型VLA的直接价值较弱。

- **概念**：[[多模态基础模型]] [[智能体 Agent]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/A Topological Representation with Object-Path Graphs for Open-Vocabulary Instanc.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language navigation requires embodied agents to navigate environments using natural language instructions and visual observations. Existing approaches typically decompose navigation into sequential language-guided decisions or rely on online exploration without prior environmental knowledge. Scene graph representations offer compact semantic memory but remain decoupled from downstream navigation, which still depends on dense metric maps. To close this gap, we propose an object--path graph that unifies open-vocabulary semantic reasoning with topological navigation. The proposed representation jointly supports semantic grounding, graph-based localization, and navigation within a single lightweight topological framework. Building on this graph, we introduce a navigation strategy that combines global path planning with local inter-node execution through lightweight node localization and semantic visual servoing, enabling navigation directly over the graph without dense metric reconstruction. Experiments on HM3D and Replica demonstrate competitive performance in open-vocabulary object grounding through the proposed hierarchical graph structure, while achieving effective navigation performance. Real-world robot experiments further validate the practicality of the proposed framework.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24189v1
- Authors: Linwei Zheng, Daojie Peng, Bingtao Wang, Haoang Li, Jun Ma
- Published: 2026-09-21T07:01:14Z
- Age days: 1

</details>
