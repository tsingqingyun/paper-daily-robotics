---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29774v1"
published: "2026-06-29T04:33:04Z"
age_days: 1
score: 28
created: 2026-06-30
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Analytic Concept-Centric Memory for Agentic Embodied Manipulation

> [!summary] 一句话结论（基于摘要）
> Experiments on memory-dependent manipulation, articulated-object generalization, real- world memory evaluation, and ablations show that our approach improves task completion, retrieval accuracy, object re-identification, and cross-object skill generalization…

## 关键点

- **问题**：However, existing agent memories are often stored as unstructured histories or embedding-based records, making it difficult to retrieve manipulation-relevant object parts, physical states, action effects, and executable skills.
- **创新点 / 方法**：We propose an analytic concept-centric memory framework for agentic embodied manipulation.
- **证据**：Experiments on memory-dependent manipulation, articulated-object generalization, real- world memory evaluation, and ablations show that our approach improves task completion, retrieval accuracy, object re-identification, and cross-object skill generalization over unstructured and embedding-based memory baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon embodied manipulation requires agents to remember persistent objects, track
changing scene states, and reuse prior interaction knowledge. However, existing agent
memories are often stored as unstructured histories or embedding-based records, making
it difficult to retrieve manipulation-relevant object parts, physical states, action
effects, and executable skills. We propose an analytic concept-centric memory framework
for agentic embodied manipulation. Our memory organizes experience around structured
analytic concepts, where objects are represented by semantic parts, parametric
templates, grounded poses, affordances, and manipulation states. It further connects
object and scene memories with transition memory for action-induced state changes and
skill memory for template-grounded and policy-grounded execution. At runtime, the agent
performs structured coarse-to-fine retrieval to identify relevant objects, states,
transitions, and skills, supporting state-consistent reasoning and skill reuse.
Experiments on memory-dependent manipulation, articulated-object generalization, real-
world memory evaluation, and ablations show that our approach improves task completion,
retrieval accuracy, object re-identification, and cross-object skill generalization over
unstructured and embedding-based memory baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29774v1
- Authors: Mingyang Sun, Xiujian Liang, Jiude Wei, Qichen He, Donglin Wang, Cewu Lu, Jianhua Sun
- Published: 2026-06-29T04:33:04Z
- Age days: 1

</details>
