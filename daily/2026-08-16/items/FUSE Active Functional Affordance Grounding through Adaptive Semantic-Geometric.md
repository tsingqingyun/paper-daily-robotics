---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12683v1"
published: "2026-08-13T00:51:09Z"
age_days: 3
score: 24
created: 2026-08-16
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# FUSE: Active Functional Affordance Grounding through Adaptive Semantic-Geometric Evidence Acquisition

> [!summary] 一句话结论（基于摘要）
> Experiments show that FUSE achieves the highest observed non-oracle grounding performance while reducing computation by 1.33x relative to fully explicit exploration, and remains effective across multiple affordance knowledge sources.

## 关键点

- **问题**：Existing affordance grounding methods operate from fixed viewpoints and lack mechanisms for deciding where to look when functional cues are occluded or incomplete.
- **创新点 / 方法**：We introduce Active Functional Affordance Grounding, a new task in which an agent sequentially explores a scene to identify and spatially ground an object satisfying a functional query.
- **证据**：Experiments show that FUSE achieves the highest observed non-oracle grounding performance while reducing computation by 1.33x relative to fully explicit exploration, and remains effective across multiple affordance knowledge sources.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/FUSE Active Functional Affordance Grounding through Adaptive Semantic-Geometric.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied agents must often identify and interact with objects based on their function rather than their identity, requiring them to actively acquire observations that reveal discriminative functional evidence. Existing affordance grounding methods operate from fixed viewpoints and lack mechanisms for deciding where to look when functional cues are occluded or incomplete. We introduce Active Functional Affordance Grounding, a new task in which an agent sequentially explores a scene to identify and spatially ground an object satisfying a functional query. To address this problem, we propose FUSE, an adaptive semantic-geometric evidence acquisition framework that combines explicit uncertainty-driven exploration with a learned amortized planner to efficiently select informative viewpoints. We further introduce a Habitat-based benchmark for evaluating active functional grounding. Experiments show that FUSE achieves the highest observed non-oracle grounding performance while reducing computation by 1.33x relative to fully explicit exploration, and remains effective across multiple affordance knowledge sources.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12683v1
- Authors: Zhou Chen, Sathyanarayanan N. Aakur
- Published: 2026-08-13T00:51:09Z
- Age days: 3

</details>
