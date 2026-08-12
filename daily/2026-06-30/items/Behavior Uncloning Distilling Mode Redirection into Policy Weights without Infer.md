---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29201v1"
published: "2026-06-28T05:01:27Z"
age_days: 2
score: 29
created: 2026-06-30
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Behavior Uncloning: Distilling Mode Redirection into Policy Weights without Inference-Time Steering

> [!summary] 一句话结论（基于摘要）
> Across eight simulated and real-world tasks, MoRE improves the average deployment success rate (SR) by 44 percentage points over the original mixed-mode policy.

## 关键点

- **问题**：Behavior-cloned policies often learn multiple behavior modes from demonstration datasets, including modes that are unsafe or otherwise undesired at deployment.
- **创新点 / 方法**：To address this gap, we propose MoRE(Mode Redirection), which redirects policy rollouts toward desired behavior modes through a short "uncloning" step.
- **证据**：Across eight simulated and real-world tasks, MoRE improves the average deployment success rate (SR) by 44 percentage points over the original mixed-mode policy.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Behavior-cloned policies often learn multiple behavior modes from demonstration
datasets, including modes that are unsafe or otherwise undesired at deployment. For
example, a policy trained on diverse handover demonstrations may learn to pass a knife
blade-first. Standard remedies such as data curation and inference-time steering either
require access to the original demonstrations for full retraining or add substantial
inference-time overhead. To address this gap, we propose MoRE(Mode Redirection), which
redirects policy rollouts toward desired behavior modes through a short "uncloning"
step. Specifically, MoRE distills the redirection signal from a temporary mode
classifier into the policy weights to steer behavior. A retain loss balances this edit
by preserving desired-mode competence, allowing the standalone policy to suppress
unwanted modes with zero inference-time overhead. Across eight simulated and real-world
tasks, MoRE improves the average deployment success rate (SR) by 44 percentage points
over the original mixed-mode policy. Among all compared adaptation and steering
baselines, MoRE achieves the strongest SR and approaches the filtered-data retraining
reference, while preserving task competence and inference speed. MoRE also generalizes
across robot policy backbones, including Diffusion Policy and the Pi0.5 VLA, diverse
task categories, and real-world deployments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29201v1
- Authors: Hao Wang, Jiuzhou Lei, Dayou Li, Bangya Liu, Minghui Zheng, Manling Li, Ruohan Zhang, Zhiwen Fan
- Published: 2026-06-28T05:01:27Z
- Age days: 2

</details>
