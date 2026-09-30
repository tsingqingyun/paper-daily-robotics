---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09745v1"
published: "2026-09-09T05:41:27Z"
age_days: 1
score: 25
created: 2026-09-11
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# PccDiffuser: Multi-solution Motion Planning for Continuum Robots

> [!summary] 先说人话（基于摘要）
> On a mixed test set comprising workspace with zero to four obstacles, PccDiffuser achieved a success rate of 91\%.

## 这篇到底在做什么

- **卡在哪里**：We present the PccDiffuser, a conditional diffusion framework for continuum robots that learns a multimodal distribution over complete configuration-space paths and samples multiple candidate solutions in parallel, which are subsequently converted into an executable trajectory by time allocation considering actuator c…
- **关键解法**：We present the PccDiffuser, a conditional diffusion framework for continuum robots that learns a multimodal distribution over complete configuration-space paths and samples multiple candidate solutions in parallel, which are subsequently converted into an executable trajectory by time allocation considering actuator c…
- **拿什么证明**：On a mixed test set comprising workspace with zero to four obstacles, PccDiffuser achieved a success rate of 91\%.

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/PccDiffuser Multi-solution Motion Planning for Continuum Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present the PccDiffuser, a conditional diffusion framework for continuum robots that learns a multimodal distribution over complete configuration-space paths and samples multiple candidate solutions in parallel, which are subsequently converted into an executable trajectory by time allocation considering actuator constraints. Under the piecewise constant-curvature model, we use exponential co-ordinates to describe the robot kinematics, and use graph neural network to encode a variable number of environment obstacles. Analytical differential kinematics is incorporated in the denoising process to improve terminal accuracy and whole-body clearance. On a mixed test set comprising workspace with zero to four obstacles, PccDiffuser achieved a success rate of 91\%. Compared with existing sampling- and optimisation-based benchmarks, it delivered both a higher success rate and greater computational efficiency, with the latter advantage becoming more substantial when sampling more candidate solutions. Experiments on a three-section tendon-driven continuum robot further demonstrate consecutive planning, multi-solution planning, and whole-body obstacle avoidance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09745v1
- Authors: Ke Qiu, Sifan Chen, Si Wang, Rong Xiong, Yue Wang, Haojian Lu
- Published: 2026-09-09T05:41:27Z
- Age days: 1

</details>
