---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17717v1"
published: "2026-08-18T12:42:26Z"
age_days: 0
score: 35
created: 2026-08-19
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> On a closed-loop ManiSkill3 tabletop-manipulation benchmark, CompCPZ outperforms convex set baselines, multi-peak decoders, and a zero-shot vision-language-action model (1,900/1,918 paired wins, p << 10^(-30)); the same compiler also transfers without retunin…

## 关键点

- **问题**：This silent semantic failure exposes a structural limitation of language-conditioned robot policies: representations that collapse a disjunctive instruction into a single connected set cannot preserve all feasible modes, and planners that commit to one action degrade under run-time mode uncertainty.
- **创新点 / 方法**：A robot asked to "place the cup near the red plate or the blue plate" may reach the centroid between them and appear geometrically successful, while satisfying neither disjunct of the instruction.
- **证据**：On a closed-loop ManiSkill3 tabletop-manipulation benchmark, CompCPZ outperforms convex set baselines, multi-peak decoders, and a zero-shot vision-language-action model (1,900/1,918 paired wins, p << 10^(-30)); the same compiler also transfers without retuning to planar real-robot trials on a Unitree Go2 quadruped und…
- **局限**：This silent semantic failure exposes a structural limitation of language-conditioned robot policies: representations that collapse a disjunctive instruction into a single connected set cannot preserve all feasible modes, and planners that commit to one action degrade under run-time mode uncertainty.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/CompCPZ Preserving Multi-Modal Intent in Language-Guided Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A robot asked to "place the cup near the red plate or the blue plate" may reach the centroid between them and appear geometrically successful, while satisfying neither disjunct of the instruction. This silent semantic failure exposes a structural limitation of language-conditioned robot policies: representations that collapse a disjunctive instruction into a single connected set cannot preserve all feasible modes, and planners that commit to one action degrade under run-time mode uncertainty. We address this limitation with CompCPZ, a sound algebraic layer that language-conditioned learning systems wrap to recover multi-modal disjunctive representation, recursively composing per-primitive constrained polynomial zonotope enclosures along the language parse tree with distribution-free conformal coverage and sub-millisecond runtime. On a closed-loop ManiSkill3 tabletop-manipulation benchmark, CompCPZ outperforms convex set baselines, multi-peak decoders, and a zero-shot vision-language-action model (1,900/1,918 paired wins, p << 10^(-30)); the same compiler also transfers without retuning to planar real-robot trials on a Unitree Go2 quadruped under motion capture. These results suggest that compositional language grounding should be evaluated not only by reaching a decoded target, but by whether the represented feasibility set preserves the connected-component structure of the user's intent.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17717v1
- Authors: Zhen Zhang, Ahmad Hafez, Peng Xie, Yanliang Huang, Wenyuan Wu, Amr Alanwar
- Published: 2026-08-18T12:42:26Z
- Age days: 0

</details>
