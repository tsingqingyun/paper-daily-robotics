---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26214"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-08-29
concepts: ["智能体 Agent", "世界模型"]
---

# Surgical Video Generation From Diffusion to World Models: A Survey

> [!summary] 先说人话（基于摘要）
> 这篇综述把2024—2026年手术视频生成分成无条件、条件和世界模型三类，主线是领域正从“生成像真的画面”转向“模拟手术场景的因果动态”。

## 问题

手术视频受隐私、采集成本和类别不平衡限制，但快速发展的生成研究缺少统一框架；像素逼真并不等于临床过程合理，泛化、物理真实性、可控性和可解释性仍是瓶颈。

## 创新点或方法

以生成条件和建模目标组织文献，比较无条件生成、条件生成和世界建模，并汇总代表方法在公开数据上的实验结果。输出是领域分类、量化参考与开放问题，而非新生成模型。

## 证据

摘要只说明覆盖2024—2026文献并汇总代表方法的公开数据结果，没有给出论文数量、数据集范围或汇总数字。


## 局限

需全文核查检索与纳入标准、量化结果能否跨数据集公平比较，以及“因果动态”是否有明确评测定义。

- **判断**：初入手术视频生成者值得通读；已有领域经验者重点看分类框架、量化表格与开放问题。

## 研究关联

对手术机器人和世界模型研究者，它可用于建立任务分类、识别临床合理性与像素指标之间的断层；对通用Agent研究价值有限。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/Surgical Video Generation From Diffusion to World Models A Survey.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.26214v1 Announce Type: new Abstract: Surgical video data provides the primary training resource for models of intraoperative perception, surgical workflow understanding, and robotic decision-making. However, clinical data acquisition remains constrained by privacy, cost, and class imbalance. Surgical video generation has emerged as a transformative approach to addressing data scarcity and as a foundation for surgical simulation, training, and robotic policy learning. The field has developed rapidly without a clear conceptual framework. This survey organizes the 2024-2026 literature into three categories: unconditional generation, conditional generation, and world modeling generation, revealing a fundamental shift in how the task is defined from synthesizing visually plausible frames to modeling the causal dynamics of surgical scenes. We examine the persistent gap between pixel-level fidelity and clinical plausibility, and identify generalization, physical realism, controllability, and interpretability as bottlenecks. We further summarize experimental results of representative methods on public datasets to provide a quantitative reference for the field. This survey provides a structured overview of the current state and open challenges, offering a reference for researchers working at the intersection of intelligent perception, multi-modal fusion, generative AI, and surgical data science.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26214
- Authors: Fuxiang Huang, Chenxu Zhang, Liang Han, Lei Zhang
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
