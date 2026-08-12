---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13675v2"
published: "2026-06-11T17:59:45Z"
age_days: 3
score: 30
created: 2026-06-15
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# Improving Robotic Generalist Policies via Flow Reversal Steering

> [!summary] 一句话结论（基于摘要）
> These gains can be distilled with behavioral cloning by training an auxiliary policy to output noises that the generalist maps to good actions -- showing up to 95% absolute task success rate boosts in under a minute of training.

## 关键点

- **问题**：Finally, FRS enables policy improvement by bootstrapping reinforcement learning with semantic knowledge, improving on several tasks that standard RL fails to improve on.
- **创新点 / 方法**：Generalist policies can learn a wide range of skills from diverse robot datasets.
- **证据**：These gains can be distilled with behavioral cloning by training an auxiliary policy to output noises that the generalist maps to good actions -- showing up to 95% absolute task success rate boosts in under a minute of training.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-15/Improving Robotic Generalist Policies via Flow Reversal Steering.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist policies can learn a wide range of skills from diverse robot datasets. In
order to solve or improve on challenging new tasks, we need a way to infer and invoke
the appropriate actions from the policy's rich behavioral prior, especially when
directly commanding the policy fails. We focus on flow matching generalists and propose
Flow Reversal Steering (FRS): a method that takes suboptimal but ``reasonable'' actions,
finds their latent noises by passing them through the flow policy in reverse, and maps
them to nearby generalist action modes. We evaluate FRS across many simulated and real-
world manipulation settings. First, FRS can turn coarse semantic guidance from humans or
vision-language models (VLMs) into corresponding good robot actions, improving zero-shot
control. These gains can be distilled with behavioral cloning by training an auxiliary
policy to output noises that the generalist maps to good actions -- showing up to 95%
absolute task success rate boosts in under a minute of training. Finally, FRS enables
policy improvement by bootstrapping reinforcement learning with semantic knowledge,
improving on several tasks that standard RL fails to improve on.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13675v2
- Authors: Andy Tang, William Chen, Andrew Wagenmaker, Chelsea Finn, Sergey Levine
- Published: 2026-06-11T17:59:45Z
- Age days: 3

</details>
