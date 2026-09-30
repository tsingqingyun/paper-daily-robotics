---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08512v1"
published: "2026-09-08T09:58:32Z"
age_days: 1
score: 26
created: 2026-09-10
concepts: ["具身智能评测与基准"]
---

# TASG-Explore: Traversability-Aware Sector-Guided Exploration for Ground Robot on Uneven Terrain

> [!summary] 先说人话（基于摘要）
> TASG-Explore 让地面机器人先判断哪里能走，再按区域组织探索，同时保留窄通道和复杂边界的信息，兼顾速度、覆盖和地形安全。

## 问题

不平地形探索中，精细地形推理拖慢大范围搜索，粗粒度区域引导又容易漏掉窄通道与不规则可通行边界。

## 创新点或方法

用可变体素地面拟合和自适应 8 位障碍编码分析通行性，将代价地图划分扇区，增量维护区域簇、地形相关前沿视点及带未知拓扑假设的路网，再结合区域目标与局部视点规划。

## 证据

在洞穴、森林和崎岖山地等环境与六种代表性规划器比较，报告综合表现最佳。通行性分析处理效率提高 6.3 倍；崎岖山地探索效率提高 51%，覆盖最高增至 2.95 倍，并开展大规模实地实验。


## 局限

需核查各倍数的比较基线和指标定义；最高覆盖增益来自特定山地场景，不能直接外推。

- **判断**：做户外探索值得细读规划流程和实地结果，摘要给出了明确的工程收益信号。

## 研究关联

对具身导航评测研究者，它提供了地形安全、探索效率和覆盖完整性的联合比较对象，也可作为学习式探索方法的工程基线。

- **概念**：具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/TASG-Explore Traversability-Aware Sector-Guided Exploration for Ground Robot on.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous exploration on uneven terrain requires ground robots to balance exploration efficiency, coverage completeness, and terrain safety. Detailed tsrrain reasoning improves local reliability but can slow large-scale exploration, whereas coarse region guidance expands quickly in open areas but can miss narrow passages and irregular traversable boundaries. To address this challenge, this paper presents TASG-Explore, a traversability-aware sector-guided exploration framework for ground robots. The framework first performs hierarchical traversability analysis using variable-voxel ground fitting and adaptive 8-bit obstacle encoding. It then splitting cost map into sectors, incrementally updates sector clusters, extracts terrain-coupled frontier viewpoints, and maintains a dynamic topological roadmap with unknown topological hypotheses. Finally, a sector-guided planner selects region targets and inserts local viewpoints to generate efficient exploration routes. Benchmark experiments in diverse challenging environments, including caves, forests, and rugged hills, show that TASG-Explore achieves the best overall performance among six representative state-of-the-art planners. The proposed traversability analysis improves processing efficiency by 6.3 times while maintaining high accuracy, and the exploration planner improves exploration efficiency by 51% and increases coverage by up to 2.95 times in rugged hill scene. Large-scale real-world experiments further demonstrate the practical value of the proposed method.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08512v1
- Authors: Shaocong Wang, Shiliang Shao, Ting Wang, Guangjie Han, Lianqing Liu
- Published: 2026-09-08T09:58:32Z
- Age days: 1

</details>
