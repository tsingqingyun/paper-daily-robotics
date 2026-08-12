---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10568v1"
published: "2026-06-09T08:31:59Z"
age_days: 0
score: 38
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Experiments on public benchmarks and real- world robotic manipulation tasks show that VeriSpace consistently improves decision reliability over both underlying VLA policies and prior verification-based methods, yielding substantial gains in both in-distributi…

## 关键点

- **问题**：Vision-language-action (VLA) models have shown strong promise for robotic manipulation, but their reliability at test time remains limited by one-shot action prediction, where even small action errors can cause grasp failure, collision, or incorrect task progression.
- **创新点 / 方法**：We present VeriSpace, a 3D-aware action verifier for test-time action selection in VLA systems.
- **证据**：Experiments on public benchmarks and real- world robotic manipulation tasks show that VeriSpace consistently improves decision reliability over both underlying VLA policies and prior verification-based methods, yielding substantial gains in both in-distribution and out-of-distribution settings.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have shown strong promise for robotic manipulation,
but their reliability at test time remains limited by one-shot action prediction, where
even small action errors can cause grasp failure, collision, or incorrect task
progression. A natural alternative is to equip VLA systems with test-time verification,
allowing multiple candidate actions to be proposed and evaluated before execution.
However, reliable action verification is challenging because it requires not only
distinguishing subtle geometric differences between candidate actions, but also
assessing whether an action makes meaningful progress toward the task goal. We present
VeriSpace, a 3D-aware action verifier for test-time action selection in VLA systems.
VeriSpace evaluates candidate actions through two key components: Dual-Path 3D-Injected
Scene Encoding, which constructs a scene representation that jointly preserves visual
semantics and explicit 3D geometry, and Spatially-Grounded Action Reasoning, which
evaluates each action by reasoning over task-relevant spatial relations, geometric
validity, and expected goal progress. Together, these components enable more reliable
discrimination between subtle yet outcome-critical action candidates while remaining
fully compatible with existing VLA policies. Experiments on public benchmarks and real-
world robotic manipulation tasks show that VeriSpace consistently improves decision
reliability over both underlying VLA policies and prior verification-based methods,
yielding substantial gains in both in-distribution and out-of-distribution settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10568v1
- Authors: Guiyu Zhao, Longteng Guo, Junyou Zhu, Jun Fu, Yanghong Mei, Bin Cao, Jie Jiang, Xingjian He, Jing Liu
- Published: 2026-06-09T08:31:59Z
- Age days: 0

</details>
