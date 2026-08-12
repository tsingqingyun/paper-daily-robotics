---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17924v1"
published: "2026-06-16T13:38:03Z"
age_days: 1
score: 36
created: 2026-06-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space

> [!summary] 一句话结论（基于摘要）
> Empirical evaluations on the LIBERO benchmark demonstrate that PearlVLA achieves state-of-the-art performance among existing methods.

## 关键点

- **问题**：Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation.
- **创新点 / 方法**：We propose PearlVLA, a VLA framework that moves deliberation into the latent space of a vision-language model (VLM).
- **证据**：Empirical evaluations on the LIBERO benchmark demonstrate that PearlVLA achieves state-of-the-art performance among existing methods.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-18/PearlVLA Progressive Embodied Action-Plan Refinement in Latent Space.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Current Vision-Language-Action (VLA) models face a trade-off between efficient action
generation and explicit deliberation. Directly decoding actions from vision-language
backbone representations enables low-latency control, whereas explicit reasoning through
textual chains, pixel-level subgoals, or action search can improve planning but incurs
substantial latency and computational cost. We propose PearlVLA, a VLA framework that
moves deliberation into the latent space of a vision-language model (VLM). PearlVLA
separates VLM meta-query representations into a fixed visual grounding branch and an
iterative latent plan branch. At each refinement round, a plan-conditioned world query
probes a lightweight frozen latent world model for an action-free future observation
latent, which is fed back to guide plan refinement. A future-guided RefineNet then
applies scheduled residual updates to progressively refine a coarse semantic draft into
a fine-grained latent action plan. The refined plan after K rounds is then decoded in
parallel into an action chunk for low-latency execution. We further introduce Causal
Refinement-Grouped Process-Reward RL to optimize the latent refinement process with
rewards from longer-horizon imagined futures induced by latent plan edits. Empirical
evaluations on the LIBERO benchmark demonstrate that PearlVLA achieves state-of-the-art
performance among existing methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17924v1
- Authors: Bochen Yang, Lianlei Shan
- Published: 2026-06-16T13:38:03Z
- Age days: 1

</details>
