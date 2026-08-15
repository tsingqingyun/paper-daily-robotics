---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12707v1"
published: "2026-08-13T01:43:18Z"
age_days: 2
score: 28
created: 2026-08-15
concepts: ["智能体 Agent"]
---

# SAP-Nav: Spatial Semantic Representation Meets Active Perception for Hierarchical Open-Vocabulary Object Navigation

> [!summary] 一句话结论（基于摘要）
> Experiments on LangMap and HM3D-OVON show that SAP-Nav achieves the overall best performance, including a 12.2% improvement in SR over training-based methods on region-level navigation.

## 关键点

- **问题**：Although recent work LangMap has formalized this setting, reliably solving it under partial observations remains challenging: spatial grounding requires persistent environment-level evidence, whereas target verification requires clear and discriminative candidate views.
- **创新点 / 方法**：We present SAP-Nav, a fully online, zero-shot framework that addresses both requirements through active perception.
- **证据**：Experiments on LangMap and HM3D-OVON show that SAP-Nav achieves the overall best performance, including a 12.2% improvement in SR over training-based methods on region-level navigation.
- **局限**：Although recent work LangMap has formalized this setting, reliably solving it under partial observations remains challenging: spatial grounding requires persistent environment-level evidence, whereas target verification requires clear and discriminative candidate views.

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/SAP-Nav Spatial Semantic Representation Meets Active Perception for Hierarchical.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Hierarchical open-vocabulary object navigation (OVON) requires agents to follow free-form instructions that may specify targets through scene-, room-, region-, and instance-level cues in unseen environments. Although recent work LangMap has formalized this setting, reliably solving it under partial observations remains challenging: spatial grounding requires persistent environment-level evidence, whereas target verification requires clear and discriminative candidate views. We present SAP-Nav, a fully online, zero-shot framework that addresses both requirements through active perception. SAP-Nav incrementally constructs a Queryable Spatial-Semantic Representation from actively acquired room views, enabling spatial semantic queries from any explored location. It further employs Active Viewpoint Verification to assess whether the current observation provides sufficient evidence and, when necessary, reposition the agent to a more informative viewpoint before verifying candidates against category and attribute constraints. Although designed for hierarchical OVON, SAP-Nav supports both hierarchical and standard category-level OVON without task-specific training or precomputed scene maps. Experiments on LangMap and HM3D-OVON show that SAP-Nav achieves the overall best performance, including a 12.2% improvement in SR over training-based methods on region-level navigation. Real-world robot experiments further demonstrate its practical feasibility. Code will be made publicly available upon acceptance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12707v1
- Authors: Xuetong Pei, Jian Liu, Vidura Munasinghe, Bo Miao, U-Xuan Tan, Wenrui Ding, Na Zhao
- Published: 2026-08-13T01:43:18Z
- Age days: 2

</details>
