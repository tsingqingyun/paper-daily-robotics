---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19174v1"
published: "2026-07-21T15:12:11Z"
age_days: 3
score: 25
created: 2026-07-25
concepts: ["世界模型", "具身智能评测与基准"]
---

# Bayesian Retraction Optimization for Tissue Attachment Mapping in Surgical Dissection

> [!summary] 一句话结论（基于摘要）
> Our method uses a Sequential Bayesian Hilbert Map (SBHM) to represent the likelihood that each tissue point is attached to the underlying resection surface.

## 关键点

- **问题**：We instead view tissue attachment identification as an inherently probabilistic problem and propose a Bayesian approach that avoids explicit tissue modeling.
- **创新点 / 方法**：Our method uses a Sequential Bayesian Hilbert Map (SBHM) to represent the likelihood that each tissue point is attached to the underlying resection surface.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Prior work has relied on hand-crafted incision policies that cannot quantify uncertainty or has relied on simulation-based methods that require strong modeling assumptions.

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/Bayesian Retraction Optimization for Tissue Attachment Mapping in Surgical Disse.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

With growing surgeon shortages, automating surgical sub-tasks such as tissue dissection
offers a promising step toward reducing workload and expanding patient access. Prior
work has relied on hand-crafted incision policies that cannot quantify uncertainty or
has relied on simulation-based methods that require strong modeling assumptions. We
instead view tissue attachment identification as an inherently probabilistic problem and
propose a Bayesian approach that avoids explicit tissue modeling. Our method uses a
Sequential Bayesian Hilbert Map (SBHM) to represent the likelihood that each tissue
point is attached to the underlying resection surface. An ensemble of learned
classifiers predicts attachment likelihoods from spatial data acquired during robotic
tissue retraction, with each classifier serving as a noisy information source to update
the SBHM. To plan the next retraction, we devise Bayesian Retraction Optimization (BRO)
to select the most informative action under safety constraints. As the SBHM refines over
time, regions with high attachment likelihood are selectively incised. We validate our
method in simulation across diverse tissue geometries and acquisition strategies, and
demonstrate zero-shot transfer to real robotic dissection experiments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19174v1
- Authors: Shing-Hei Ho, Bao Thach, Toan Vo, James M. Ferguson, Alan Kuntz
- Published: 2026-07-21T15:12:11Z
- Age days: 3

</details>
