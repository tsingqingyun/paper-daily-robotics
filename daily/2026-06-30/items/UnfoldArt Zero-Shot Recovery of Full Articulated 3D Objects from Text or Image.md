---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30608v1"
published: "2026-06-29T17:44:53Z"
age_days: 0
score: 29
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent"]
---

# UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image

> [!summary] 一句话结论（基于摘要）
> We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation.

## 关键点

- **问题**：Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging.
- **创新点 / 方法**：We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/UnfoldArt Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Articulated 3D objects are essential for interactive environments in embodied AI,
robotics, and virtual reality, but reconstructing their structure and motion from sparse
observations remains challenging. Existing approaches remain largely constrained by lack
of supervised data or lack the priors needed to reliably recover articulation, hidden
geometry, and internal object structure. We present the first debate-driven agentic
approach to articulated 3D object reconstruction from text or image inputs that both
grounds articulation reasoning in concrete motion and exposes the occluded geometry
revealed under articulation. High-level agents reason about object semantics and motion
using knowledge from vision-language and video models, while low-level agents estimate
articulation parameters and interaction points; together, they engage in a two-round
structured debate that first exploits global--local disagreement and then grounds the
agents in freely generated video. The same video prior, conditioned on the agreed
articulation, then drives each part through its motion to expose occluded interiors and
geometry that cannot be inferred from a single static view. By combining agentic
reasoning with a video generative prior, our approach jointly infers articulation and
reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal
structure, and motion-consistent states beyond directly observed surfaces.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30608v1
- Authors: Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai
- Published: 2026-06-29T17:44:53Z
- Age days: 0

</details>
