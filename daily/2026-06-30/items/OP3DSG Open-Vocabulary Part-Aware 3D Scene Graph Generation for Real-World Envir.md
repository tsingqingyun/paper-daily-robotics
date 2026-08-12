---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29786v1"
published: "2026-06-29T05:05:54Z"
age_days: 1
score: 35
created: 2026-06-30
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# OP3DSG: Open-Vocabulary Part-Aware 3D Scene Graph Generation for Real-World Environments

> [!summary] 一句话结论（基于摘要）
> Experimental results show that OP3DSG achieves state-of-the-art performance and demonstrates its effectiveness as a perception backbone in diverse real- world robotics tasks.

## 关键点

- **问题**：Although advances in foundation models have enabled open-vocabulary 3DSG generation, existing approaches remain object-centric and encode limited relational information -- restricting their applicability in real-world scenarios that require fine-grained understanding.
- **创新点 / 方法**：We propose OP3DSG, an open-vocabulary part-aware 3DSG generation framework that constructs unified graphs that jointly model objects, interactive parts, spatial relations, functional relations, and affordances.
- **证据**：Experimental results show that OP3DSG achieves state-of-the-art performance and demonstrates its effectiveness as a perception backbone in diverse real- world robotics tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/OP3DSG Open-Vocabulary Part-Aware 3D Scene Graph Generation for Real-World Envir.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

3D scene graphs (3DSGs) provide a compact and structured abstraction of 3D environments.
Although advances in foundation models have enabled open-vocabulary 3DSG generation,
existing approaches remain object-centric and encode limited relational information --
restricting their applicability in real-world scenarios that require fine-grained
understanding. We propose OP3DSG, an open-vocabulary part-aware 3DSG generation
framework that constructs unified graphs that jointly model objects, interactive parts,
spatial relations, functional relations, and affordances. OP3DSG integrates object-part
knowledge-guided detection with part-aware 3D fusion to preserve small and interaction-
relevant components, and employs a geometry-initialized prior graph with LLM-based
refinement to reduce spurious relational predictions while enabling efficient graph
construction. To systematically evaluate unified 3D scene graph construction, we
introduce UniGraph3D, a benchmark designed for part-aware perception and multi-level
relational reasoning. Experimental results show that OP3DSG achieves state-of-the-art
performance and demonstrates its effectiveness as a perception backbone in diverse real-
world robotics tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29786v1
- Authors: Yirum Kim, Ue-Hwan Kim
- Published: 2026-06-29T05:05:54Z
- Age days: 1

</details>
