---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16843v1"
published: "2026-08-17T17:28:49Z"
age_days: 0
score: 34
created: 2026-08-18
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation

> [!summary] 一句话结论（基于摘要）
> We present a trust-boundary-centric survey of foundation-model-powered embodied-agent security.

## 关键点

- **问题**：Context and long-term memory, middleware and networking, world-state integrity, and multi-agent trust remain comparatively underexplored.
- **创新点 / 方法**：We present a trust-boundary-centric survey of foundation-model-powered embodied-agent security.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/Security of Foundation-Model-Powered Embodied Agents Attack Surfaces, Attacks, D.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Foundation models are increasingly used for perception, reasoning, planning, and action generation in embodied agents, creating security risks that can propagate from digital inputs to physical behavior. Existing surveys often organize threats by mechanisms such as jailbreaks, prompt injection, backdoors, poisoning, or adversarial examples, but these categories do not consistently identify where an adversary first enters the embodied control loop. We present a trust-boundary-centric survey of foundation-model-powered embodied-agent security. Using a first-compromised-trust-boundary principle, we separate attack surface from attack mechanism and organize the system into five layers and twelve attack surfaces spanning the model supply chain, user instructions, context and memory, physical semantic environments, multimodal perception, world state, internal reasoning, task planning, action interfaces, middleware, multi-agent communication, and execution control. Based on 58 attack records and 61 defense records collected through August 15, 2026, we analyze representative attacks, cross-layer propagation, defense placement, and evaluation practices. Our quantitative analysis shows that attack research is concentrated on multimodal perception and action interfaces, while defenses are especially concentrated on action-level and runtime protection. Context and long-term memory, middleware and networking, world-state integrity, and multi-agent trust remain comparatively underexplored. We conclude with open challenges in state provenance, compositional defenses, long-horizon attack propagation, physical realizability, Byzantine multi-robot behavior, and unified closed-loop evaluation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16843v1
- Authors: Jiawei Liu, Jiacheng Guo, Tian Zhang, Yiwei Xu, Juan Wang, Jinlin Fan, Bowen Xiao
- Published: 2026-08-17T17:28:49Z
- Age days: 0

</details>
