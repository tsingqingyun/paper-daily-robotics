---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21571v1"
published: "2026-07-23T17:50:45Z"
age_days: 0
score: 28
created: 2026-07-24
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering

> [!summary] 一句话结论（基于摘要）
> Extensive experiments in simulated environments reveal that this form of memory breaks the accuracy-efficiency tradeoff in sequential settings, simultaneously achieving higher answer accuracy and lower navigation costs.

## 关键点

- **问题**：However, real-world robots operate continuously and must accumulate, retain, and selectively reuse information acquired from prior interactions.
- **创新点 / 方法**：Embodied question answering (EQA) is traditionally evaluated under an episodic formulation, where agents solve each task independently and reset internal state between episodes.
- **证据**：Extensive experiments in simulated environments reveal that this form of memory breaks the accuracy-efficiency tradeoff in sequential settings, simultaneously achieving higher answer accuracy and lower navigation costs.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-24/Beyond Episodic Evaluation Memory Architectural Bottlenecks in Sequential Embodi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied question answering (EQA) is traditionally evaluated under an episodic
formulation, where agents solve each task independently and reset internal state between
episodes. However, real-world robots operate continuously and must accumulate, retain,
and selectively reuse information acquired from prior interactions. Despite this
practical requirement, the architectural mechanisms needed to support sequential memory
in EQA remain underexplored. In this work, we investigate how different memory
architectures behave when EQA agents are evaluated sequentially, with multiple questions
answered in the same scene while memory is carried forward across queries. We find that
simply preserving existing memory is often insufficient. Agents that retain only
traversability information, such as 2D occupancy maps, remember where the robot has
explored but not the visual-semantic evidence needed for later questions. Agents trained
on short-horizon episodic data face a different challenge: when exposed to continuous,
multi-query histories, their inherited context suffers from severe temporal mismatch,
rather than forming a reusable scene representation. To overcome this architectural
bottleneck, we highlight the necessity of structured, spatially grounded memory:
architectures that map persistent visual observations onto metric 3D geometry preserve
visual-semantic evidence in a coherent scene representation. Extensive experiments in
simulated environments reveal that this form of memory breaks the accuracy-efficiency
tradeoff in sequential settings, simultaneously achieving higher answer accuracy and
lower navigation costs. We further validate these findings on a real-world mobile robot,
demonstrating that spatially grounded visual memory is critical for enabling continuous,
intelligent operation in physical environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21571v1
- Authors: Zikui Cai, Kaushal Janga, Tan Dat Dao, Seungjae Lee, Shivin Dass, Mingyo Seo, Kaiyu Yue, Mintong Kang, Nandhu Pillai, Monte Hoover, Aadi Palnitkar, Ruchit Rawal, Ruijie Zheng, Bo Li, Yuke Zhu, Roberto Martín-Martín, Tom Goldstein, Furong Huang
- Published: 2026-07-23T17:50:45Z
- Age days: 0

</details>
