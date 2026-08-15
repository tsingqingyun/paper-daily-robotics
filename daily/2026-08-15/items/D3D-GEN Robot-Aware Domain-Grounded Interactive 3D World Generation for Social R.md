---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.11876v1"
published: "2026-08-12T10:03:01Z"
age_days: 2
score: 29
created: 2026-08-15
concepts: ["智能体 Agent", "世界模型"]
---

# D3D-GEN: Robot-Aware Domain-Grounded Interactive 3D World Generation for Social Robotics

> [!summary] 一句话结论（基于摘要）
> We propose D3D-GEN, a novel world generation system that combines a domain agent with a retrieval-augmented generation (RAG) pipeline grounded in that domain.

## 关键点

- **问题**：Training and validation of Embodied AI for social navigation critically depends on realistic simulation environments, yet many current approaches fail to find a balance between realism and simulability.
- **创新点 / 方法**：We propose D3D-GEN, a novel world generation system that combines a domain agent with a retrieval-augmented generation (RAG) pipeline grounded in that domain.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/D3D-GEN Robot-Aware Domain-Grounded Interactive 3D World Generation for Social R.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Training and validation of Embodied AI for social navigation critically depends on realistic simulation environments, yet many current approaches fail to find a balance between realism and simulability. We propose D3D-GEN, a novel world generation system that combines a domain agent with a retrieval-augmented generation (RAG) pipeline grounded in that domain. Our system enables users to rapidly generate domain-grounded, fully interactive 3D worlds by automating both the collection of domain knowledge and the synthesis of realistic floorplans and object placements, without dependence on any fixed 3D model database. Given a domain description prompt, the research agent collects publicly accessible domain-specific data and constructs a persistent domain database. Using this database, our RAG pipeline generates plausible floorplans and object placements by dynamically querying a user-provided semantic database, which can be easily extended or modified. The output is a fully interactive 3D world loadable by the popular simulators Isaac Sim and Gazebo. With our approach, we have built databases for several common domains (indoor residential, hospital, office) and generated dozens of distinct, plausible simulation environments for each domain. We present D3D-GEN with a local web frontend that facilitates rapid, interactive world generation for robot simulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.11876v1
- Authors: Anh Duc Do, Volodymyr Scherbyna, Tai Duc Nguyen, Spaarsh Thakkar, Zhengcheng Shen, Teham Buiyan, Archan Misra, Linh Kästner
- Published: 2026-08-12T10:03:01Z
- Age days: 2

</details>
