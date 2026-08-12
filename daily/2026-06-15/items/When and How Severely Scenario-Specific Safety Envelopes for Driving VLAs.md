---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14238v1"
published: "2026-06-12T08:20:06Z"
age_days: 2
score: 26
created: 2026-06-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs

> [!summary] 一句话结论（基于摘要）
> Safety certification of Vision-Language-Action (VLA) driving planners under ISO 21448 (SOTIF) rests on an Operational Design Domain (ODD) specification that answers two complementary questions: when does the planner start to fail, and how severely does it fai…

## 关键点

- **问题**：A Gaussian Mixture Model (GMM) on the changed-explanation subset identifies six discrete severity bands (BIC-optimal $k{=}6$), so two perturbation conditions with the same mean error can differ materially in their share of high-severity (C4/C5) failures.
- **创新点 / 方法**：Safety certification of Vision-Language-Action (VLA) driving planners under ISO 21448 (SOTIF) rests on an Operational Design Domain (ODD) specification that answers two complementary questions: when does the planner start to fail, and how severely does it fail once it does?
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/When and How Severely Scenario-Specific Safety Envelopes for Driving VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safety certification of Vision-Language-Action (VLA) driving planners under ISO 21448
(SOTIF) rests on an Operational Design Domain (ODD) specification that answers two
complementary questions: when does the planner start to fail, and how severely does it
fail once it does? We evaluate Alpamayo R1, a 10B-parameter open-weight driving VLA, on
15,968 (clip, attack) pairs. We find a conservative-aggregate gap: an aggregate safe
threshold of $σ\leq 50$ under a 15% average displacement error (ADE) budget masks well-
sampled scenarios that tolerate the top of the tested grid ($σ= 70$). A Gaussian Mixture
Model (GMM) on the changed-explanation subset identifies six discrete severity bands
(BIC-optimal $k{=}6$), so two perturbation conditions with the same mean error can
differ materially in their share of high-severity (C4/C5) failures. Joining the two
analyses on the same corpus surfaces a finding neither yields in isolation: the
scenarios with the loosest noise thresholds are not those with the lowest high-severity
rate: STOP_SIGNAL concentrates roughly $4\times$ the C4/C5 share of LANE_KEEPING despite
tolerating a larger $σ$. A deployable SOTIF ODD specification for driving VLAs therefore
requires a two-dimensional safety envelope, not a single aggregate value per hazard.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14238v1
- Authors: Abhinaw Priyadershi, Jelena Frtunikj
- Published: 2026-06-12T08:20:06Z
- Age days: 2

</details>
