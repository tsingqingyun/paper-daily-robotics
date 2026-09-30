---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09148v2"
published: "2026-09-08T17:59:03Z"
age_days: 2
score: 30
created: 2026-09-11
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Proxy Policy Steering

> [!summary] 先说人话（基于摘要）
> On 8 real-world and 4 simulation manipulation tasks, PPS lifts the state-of-the-art pi 0.5 base policy by 53% absolute success rate on average, with zero-to-one gains on tasks the base never solves, while preserving the base's broad capabilities.

## 这篇到底在做什么

- **卡在哪里**：Generalist robot policies carry broad manipulation priors from large-scale data, but specializing them to a new task remains the deployment bottleneck.
- **关键解法**：We introduce Proxy Policy Steering (PPS), an inference-time adaptation method that resolves this challenge by training two lightweight proxy policies whose calibrated velocity-space difference steers the frozen base sampler.
- **拿什么证明**：On 8 real-world and 4 simulation manipulation tasks, PPS lifts the state-of-the-art pi 0.5 base policy by 53% absolute success rate on average, with zero-to-one gains on tasks the base never solves, while preserving the base's broad capabilities.

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Proxy Policy Steering.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist robot policies carry broad manipulation priors from large-scale data, but specializing them to a new task remains the deployment bottleneck. This requires eliciting task-specific behavior from limited demonstrations without degrading their broad capabilities. We introduce Proxy Policy Steering (PPS), an inference-time adaptation method that resolves this challenge by training two lightweight proxy policies whose calibrated velocity-space difference steers the frozen base sampler. A reference proxy models the frozen base's behavior on target-task observations, and a task proxy, initialized from the reference, captures how this behavior changes under task supervision. Their difference forms a calibrated velocity-space residual that steers the frozen base sampler at every denoising step. We identify the conditions under which this residual isolates the change induced by task supervision, and validate them empirically. Because the base is never directly modified, its broad capabilities remain available at inference, including behaviors such as recovery from failure that the demonstrations themselves do not exercise. Adaptation requires only forward velocity predictions from the base, making PPS lightweight to train and applicable even without access to the base's parameters. On 8 real-world and 4 simulation manipulation tasks, PPS lifts the state-of-the-art pi 0.5 base policy by 53% absolute success rate on average, with zero-to-one gains on tasks the base never solves, while preserving the base's broad capabilities. PPS outperforms LoRA fine-tuning, from-scratch specialists, residual policies, and prior inference-time steering methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09148v2
- Authors: Chuanruo Ning, Tianrui Wang, Wei-Chiu Ma, Kuan Fang
- Published: 2026-09-08T17:59:03Z
- Age days: 2

</details>
