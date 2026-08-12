---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12706v1"
published: "2026-06-10T21:53:33Z"
age_days: 3
score: 27
created: 2026-06-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving

> [!summary] 一句话结论（基于摘要）
> We introduce VLADriveBench, a framework that combines observational metrics (mentioning, hallucination, contradiction, action alignment) with a CoT intervention protocol to provide complementary views of the CoT-action relationship.

## 关键点

- **问题**：Vision-language-action (VLA) models generate chain-of-thought (CoT) reasoning alongside driving trajectories, but existing benchmarks evaluate only trajectory quality and do not assess whether the CoT is relevant, consistent, or causally connected to the driving action.
- **创新点 / 方法**：We introduce VLADriveBench, a framework that combines observational metrics (mentioning, hallucination, contradiction, action alignment) with a CoT intervention protocol to provide complementary views of the CoT-action relationship.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/VLADriveBench Evaluating CoT-Action Relationship in VLA for Autonomous Driving.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models generate chain-of-thought (CoT) reasoning alongside
driving trajectories, but existing benchmarks evaluate only trajectory quality and do
not assess whether the CoT is relevant, consistent, or causally connected to the driving
action. We introduce VLADriveBench, a framework that combines observational metrics
(mentioning, hallucination, contradiction, action alignment) with a CoT intervention
protocol to provide complementary views of the CoT-action relationship. Applying
VLADriveBench to three models across two architectures, we find that the two analyses
can diverge sharply: ORION scores highest on observational alignment yet its CoT is
epiphenomenal, while Alpamayo v1.5 scores lower yet its CoT is strongly causal, with
visual salience gating the extent of CoT influence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12706v1
- Authors: Thach Nguyen, Danhua Guo, Tom Lampo, Fei Wu, Burhan Yaman
- Published: 2026-06-10T21:53:33Z
- Age days: 3

</details>
