---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20556v1"
published: "2026-08-20T20:35:07Z"
age_days: 3
score: 30
created: 2026-08-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Logic-VLA: A Temporal Logic Conditioned Vision-Language-Action Model

> [!summary] 一句话结论（基于摘要）
> Across the evaluation benchmarks, Logic-VLA improves STL satisfaction rate over an STL-blind base policy by 24.8 to 40.7 percentage points (pp) while reducing nominal NL task success by at most 1.8 pp, showing that a single VLA can adapt its behavior to varyi…

## 问题

Vision-language-action (VLA) models can follow natural-language (NL) task instructions, but such instructions may not precisely specify safety-critical or spatiotemporal requirements on the resulting behavior.

## 创新点或方法

We introduce Logic-VLA, a formal-requirement-aware VLA that conditions on Signal Temporal Logic (STL) specifications supplied at inference time.

## 证据

Across the evaluation benchmarks, Logic-VLA improves STL satisfaction rate over an STL-blind base policy by 24.8 to 40.7 percentage points (pp) while reducing nominal NL task success by at most 1.8 pp, showing that a single VLA can adapt its behavior to varying formal requirements without requiring a separate policy f…

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/Logic-VLA A Temporal Logic Conditioned Vision-Language-Action Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models can follow natural-language (NL) task instructions, but such instructions may not precisely specify safety-critical or spatiotemporal requirements on the resulting behavior. We introduce Logic-VLA, a formal-requirement-aware VLA that conditions on Signal Temporal Logic (STL) specifications supplied at inference time. Logic-VLA uses a syntax-graph-based STL encoder pre-trained to capture temporal logic semantics. Policy adaptation proceeds in two stages: STL-conditioned supervised fine-tuning on satisfying demonstrations is followed by trajectory-level preference optimization over matched satisfying-violating rollout pairs using a flow-matching surrogate for Identity Preference Optimization. This formulation improves formal requirement satisfaction while preserving the nominal NL task. We evaluate Logic-VLA in closed-loop quadcopter navigation simulation across randomized photorealistic environments and test generalization to STL formulas unseen during training. Across the evaluation benchmarks, Logic-VLA improves STL satisfaction rate over an STL-blind base policy by 24.8 to 40.7 percentage points (pp) while reducing nominal NL task success by at most 1.8 pp, showing that a single VLA can adapt its behavior to varying formal requirements without requiring a separate policy for each specification.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20556v1
- Authors: Celina Shiyu Wang, Yiqi Zhao, Junjie Ye, Yue Wang, Jyotirmoy V. Deshmukh
- Published: 2026-08-20T20:35:07Z
- Age days: 3

</details>
