---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18617v1"
published: "2026-05-18T16:26:22Z"
age_days: 1
score: 35
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# ManiSoft: Towards Vision-Language Manipulation for Soft Continuum Robotics

> [!summary] 一句话结论（基于摘要）
> To investigate these challenges, we introduce \ManiSoft, a benchmark for vision-language manipulation with soft arms.

## 关键点

- **问题**：Soft robotic arms offer an appealing alternative due to their deformability, but confront challenges such as unreliable proprioception and distributed low-level actuation.
- **创新点 / 方法**：To investigate these challenges, we introduce \ManiSoft, a benchmark for vision-language manipulation with soft arms.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-20/ManiSoft Towards Vision-Language Manipulation for Soft Continuum Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Most existing vision-language manipulation research targets rigid robotic arms, whose
fixed morphology limits adaptability in cluttered or confined spaces. Soft robotic arms
offer an appealing alternative due to their deformability, but confront challenges such
as unreliable proprioception and distributed low-level actuation. To investigate these
challenges, we introduce \ManiSoft, a benchmark for vision-language manipulation with
soft arms. ManiSoft features a tailored simulator that couples realistic soft-body
dynamics with contact-rich interactions via an elastic force constraint. On this basis,
ManiSoft defines four tasks, each highlighting distinct aspects of deformable control,
from basic end-effector coordination to obstacle avoidance. To support policy training
and evaluation, \ManiSoft{} includes an automated pipeline that generates $6{,}300$
diverse scenes and corresponding expert trajectories. To produce high-quality
trajectories at scale, we first employ a high-level planner to decompose each task into
a sequence of waypoints, followed by a low-level reinforcement learning policy that
generates torque commands to track waypoints. Benchmarking three representative policy
models shows relatively promising results in clean scenes but substantial performance
drop under randomization. Visualization analysis indicates that failures stem primarily
from inaccurate visual estimation of proprioceptive state and limited exploitation of
deformability for adaptive obstacle avoiding. We anticipate ManiSoft to serve as a
valuable testbed, bridging the gap between rigid and soft arms in the context of vision-
language manipulation. Out codes and datasets are released at https://buaa-
colalab.github.io/ManiSoft.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18617v1
- Authors: Ziyu Wei, Luting Wang, Chen Gao, Li Wen, Si Liu
- Published: 2026-05-18T16:26:22Z
- Age days: 1

</details>
