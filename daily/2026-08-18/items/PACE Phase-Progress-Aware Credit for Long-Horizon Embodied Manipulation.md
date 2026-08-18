---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15026v1"
published: "2026-08-15T04:25:16Z"
age_days: 2
score: 39
created: 2026-08-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# PACE: Phase-Progress-Aware Credit for Long-Horizon Embodied Manipulation

> [!summary] 一句话结论（基于摘要）
> Extensive simulation experiments and diverse real-world robotic-arm experiments demonstrate that PACE consistently achieves significant improvements over the strongest baseline.

## 关键点

- **问题**：However, in long-horizon manipulation, a single episode often spans hundreds of control steps and multiple phases, while success or failure is only revealed at episode termination.
- **创新点 / 方法**：We present PACE, a credit-assignment framework for post-training on long-horizon manipulation, centered on a phase-progress-aware critic.
- **证据**：Extensive simulation experiments and diverse real-world robotic-arm experiments demonstrate that PACE consistently achieves significant improvements over the strongest baseline.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/PACE Phase-Progress-Aware Credit for Long-Horizon Embodied Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Post-training of vision-language-action (VLA) models typically relies on expert demonstrations and policy interaction trajectories. However, in long-horizon manipulation, a single episode often spans hundreds of control steps and multiple phases, while success or failure is only revealed at episode termination. Policy improvement therefore requires step-level credit signals to distinguish behaviors that advance the task from those that stall or regress. We present PACE, a credit-assignment framework for post-training on long-horizon manipulation, centered on a phase-progress-aware critic. PACE consists of two key modules: (1) the Global-Local Cooperative Value-Correction Critic (GLC-Critic) aggregates visual and motion-difference features within local temporal windows to infer the phase and intra-phase progress of each step, and applies residual correction to a discretized remaining-cost distribution accordingly, enabling step-level credit assignment; (2) Progressive Policy Distillation (PPD) converts credit into positive and negative conditions via task-wise thresholds and trains a credit-conditioned action generation policy: it first protects the pretrained policy with high-credit positive samples, then incorporates all positive and negative credits to learn the quality boundary, and at inference amplifies high-credit behaviors through the difference between conditional outputs. Extensive simulation experiments and diverse real-world robotic-arm experiments demonstrate that PACE consistently achieves significant improvements over the strongest baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15026v1
- Authors: Chengye Song, Jiawei Zhang, Rui Song, Shengqi Wang, Xiangrong Zhang, Ziyi Wang, Huanbin Zhou, Hongzhou Wang
- Published: 2026-08-15T04:25:16Z
- Age days: 2

</details>
