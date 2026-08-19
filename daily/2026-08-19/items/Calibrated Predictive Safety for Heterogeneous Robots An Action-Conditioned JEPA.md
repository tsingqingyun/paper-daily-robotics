---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17496v1"
published: "2026-08-18T08:24:08Z"
age_days: 0
score: 30
created: 2026-08-19
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields

> [!summary] 一句话结论（基于摘要）
> We propose a receding-horizon decision pipeline: (1) a proposer produces K candidate action chunks; (2) an action-conditioned JEPA rolls each candidate forward in a frozen-encoder latent space conditioned on an embodiment embedding; (3) calibrated risk and pr…

## 关键点

- **问题**：Real-robot experiments and an offline reranking significance test remain future work; see the paper for disclosures.
- **创新点 / 方法**：We propose a receding-horizon decision pipeline: (1) a proposer produces K candidate action chunks; (2) an action-conditioned JEPA rolls each candidate forward in a frozen-encoder latent space conditioned on an embodiment embedding; (3) calibrated risk and progress heads score each rollout and report uncertainty; (4)…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Real-robot experiments and an offline reranking significance test remain future work; see the paper for disclosures.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Calibrated Predictive Safety for Heterogeneous Robots An Action-Conditioned JEPA.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action policies generalize broadly but provide no execution-time guarantees; classical model-based planners respect kinematic and geometric constraints but generalize poorly. We study whether an action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model can predict, before execution, both task progress and physical risk for candidate action chunks, and whether coupling these predictions to an embodiment-specific model-based safety shield yields a deployable pipeline for heterogeneous robots. We propose a receding-horizon decision pipeline: (1) a proposer produces K candidate action chunks; (2) an action-conditioned JEPA rolls each candidate forward in a frozen-encoder latent space conditioned on an embodiment embedding; (3) calibrated risk and progress heads score each rollout and report uncertainty; (4) a deterministic per-embodiment safety shield filters inadmissible candidates; (5) a fallback ladder handles empty-admissible-set cases. The learned ranking only reorders admissible candidates; enforcement guarantees come from the deterministic shield and fallback ladder. We evaluate with a pre-registered protocol in simulation (LIBERO-Long). In 600-episode configurations the full framework improved success over a shield-only baseline and reduced collision false negatives at matched recall. Deployment-efficiency measurements on target on-robot and edge accelerators are included. Real-robot experiments and an offline reranking significance test remain future work; see the paper for disclosures.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17496v1
- Authors: Kaiming Zhong, Tianhua Liu, Yue Wang
- Published: 2026-08-18T08:24:08Z
- Age days: 0

</details>
