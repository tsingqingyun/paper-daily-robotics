---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16715v1"
published: "2026-08-17T15:29:58Z"
age_days: 0
score: 31
created: 2026-08-18
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning

> [!summary] 一句话结论（基于摘要）
> Extensive evaluations on RLBench and real-world manipulation tasks confirm that MatchingPolicy achieves superior few-shot performance, generalizing reliably across unseen object instances and semantic categories.

## 关键点

- **问题**：In-context imitation learning enables few-shot policy generalization but struggles to maintain performance on unseen objects and novel scenarios.
- **创新点 / 方法**：To address this, we introduce MatchingPolicy, a correspondence-driven framework that explicitly decouples demonstration-to-scene matching from policy learning.
- **证据**：Extensive evaluations on RLBench and real-world manipulation tasks confirm that MatchingPolicy achieves superior few-shot performance, generalizing reliably across unseen object instances and semantic categories.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/MatchingPolicy Correspondence-Aware Policy Enables Cross-Object In-Context Learn.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In-context imitation learning enables few-shot policy generalization but struggles to maintain performance on unseen objects and novel scenarios. To address this, we introduce MatchingPolicy, a correspondence-driven framework that explicitly decouples demonstration-to-scene matching from policy learning. Central to our method is a correspondence-aware diffusion policy that conditions robotic actions directly on dense semantic correspondences. This architectural separation resolves the inherent conflict between correspondence identification and action adaptation, enabling robust out-of-distribution transfer. Our framework integrates vision foundation models with a novel two-stage matching algorithm to dynamically establish reliable correspondences. Extensive evaluations on RLBench and real-world manipulation tasks confirm that MatchingPolicy achieves superior few-shot performance, generalizing reliably across unseen object instances and semantic categories.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16715v1
- Authors: Qijin She, Hanyang Yu, Zeming Li, Ping Tan
- Published: 2026-08-17T15:29:58Z
- Age days: 0

</details>
