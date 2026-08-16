---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.10976v1"
published: "2026-08-11T14:33:21Z"
age_days: 4
score: 26
created: 2026-08-16
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving

> [!summary] 一句话结论（基于摘要）
> We propose XCoT-VLA, which replaces descriptive rationales with compact executable CoT tokens learned from automatically constructed Reason-Action supervision.

## 关键点

- **问题**：However, verbose natural-language Chain-of-Thought (CoT) is poorly suited to real-time control because it is open-ended, costly to decode, and difficult to optimize as an action-facing representation.
- **创新点 / 方法**：We propose XCoT-VLA, which replaces descriptive rationales with compact executable CoT tokens learned from automatically constructed Reason-Action supervision.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/XCoT-VLA Executable Chain-of-Thought for Vision-Language-Action Driving.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models can connect scene understanding, semantic reasoning, and trajectory generation for autonomous driving. However, verbose natural-language Chain-of-Thought (CoT) is poorly suited to real-time control because it is open-ended, costly to decode, and difficult to optimize as an action-facing representation. We propose XCoT-VLA, which replaces descriptive rationales with compact executable CoT tokens learned from automatically constructed Reason-Action supervision. Logged trajectories provide action evidence, while scene context supplies causal semantics. The predicted XCoT sequence remains in context and conditions fixed trajectory queries through shared multimodal self-attention. Deterministic token-function routing applies the Reason FFN to XCoT tokens and the Control FFN to trajectory queries for flow-matching trajectory generation. We further introduce XCoT Policy Optimization (XCPO) as an optional refinement extension in the same executable token space. XCoT-VLA reduces longitudinal ADE from 1.645 to 1.323 on a general-distribution set and lateral FDE from 1.616 to 0.648 in lane-change scenarios. By representing driving-oriented reasoning with only 2-6 executable XCoT tokens, our method substantially reduces autoregressive reasoning overhead and remains within the real-time planning budget. These results demonstrate that driving-oriented reasoning can be compact, executable, and directly connected to trajectory generation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.10976v1
- Authors: Foundation Model Team, XPeng Inc
- Published: 2026-08-11T14:33:21Z
- Age days: 4

</details>
