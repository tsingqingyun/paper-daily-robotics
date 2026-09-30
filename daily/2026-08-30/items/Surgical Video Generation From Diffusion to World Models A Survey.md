---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26214v1"
published: "2026-08-26T08:27:20Z"
age_days: 3
score: 28
created: 2026-08-30
concepts: ["智能体 Agent", "世界模型"]
---

# Surgical Video Generation From Diffusion to World Models: A Survey

> [!summary] 先说人话（基于摘要）
> 这篇综述把 2024—2026 年手术视频生成分为无条件、条件和世界模型三类，核心观察是领域正在从“画面像真”转向“能表示手术场景因果动态”。

## 这篇到底在做什么

- **卡在哪里**：手术视频受隐私、采集成本和类别不均衡限制，而快速增长的生成研究缺少统一框架；像素保真也不等于临床合理，难直接服务模拟、训练和机器人决策。
- **关键解法**：按生成条件与建模目标组织文献，并汇总代表方法在公开数据集上的实验；重点分析通用性、物理真实性、可控性和可解释性，以及从帧生成到世界动态建模的迁移。
- **拿什么证明**：摘要说明覆盖 2024—2026 文献，并汇总公开数据集上的代表性定量结果；未给出论文数量、数据集数量或元分析数字。

## 值不值得读

- **和你的研究有什么关系**：对手术世界模型和机器人决策研究者，它可用于建立术语、数据与评测地图，并提醒不能用像素质量替代临床和因果合理性。对通用 Agent 的直接价值较有限。
- **先别急着信**：需全文核查检索与纳入标准是否系统，以及不同公开数据集的指标是否真的可横向比较。
- **判断**：进入手术视频生成领域者值得通读；已有经验的研究者重点看分类框架、量化汇总和未解问题。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Surgical Video Generation From Diffusion to World Models A Survey.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Surgical video data provides the primary training resource for models of intraoperative perception, surgical workflow understanding, and robotic decision-making. However, clinical data acquisition remains constrained by privacy, cost, and class imbalance. Surgical video generation has emerged as a transformative approach to addressing data scarcity and as a foundation for surgical simulation, training, and robotic policy learning. The field has developed rapidly without a clear conceptual framework. This survey organizes the 2024-2026 literature into three categories: unconditional generation, conditional generation, and world modeling generation, revealing a fundamental shift in how the task is defined from synthesizing visually plausible frames to modeling the causal dynamics of surgical scenes. We examine the persistent gap between pixel-level fidelity and clinical plausibility, and identify generalization, physical realism, controllability, and interpretability as bottlenecks. We further summarize experimental results of representative methods on public datasets to provide a quantitative reference for the field. This survey provides a structured overview of the current state and open challenges, offering a reference for researchers working at the intersection of intelligent perception, multi-modal fusion, generative AI, and surgical data science.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26214v1
- Authors: Fuxiang Huang, Chenxu Zhang, Liang Han, Lei Zhang
- Published: 2026-08-26T08:27:20Z
- Age days: 3

</details>
