---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.07005v1"
published: "2026-08-07T09:20:31Z"
age_days: 3
score: 24
created: 2026-08-10
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Real-time Whole-Body Motion Planning for Mobile Manipulators Carrying Arbitrarily Shaped Payloads via Kinematically-Coupled SVSDF

> [!summary] 一句话结论（基于摘要）
> This letter presents a real-time whole-body motion planning framework for mobile manipulators carrying arbitrarily shaped payloads.

## 关键点

- **问题**：Mobile manipulators are increasingly tasked with transporting large, non-convex payloads through cluttered environments, yet existing planners either oversimplify the payload geometry or fail to handle the kinematic coupling between manipulator links, leading to lost feasible space or stalled optimization.
- **创新点 / 方法**：This letter presents a real-time whole-body motion planning framework for mobile manipulators carrying arbitrarily shaped payloads.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/Real-time Whole-Body Motion Planning for Mobile Manipulators Carrying Arbitraril.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Mobile manipulators are increasingly tasked with transporting large, non-convex payloads
through cluttered environments, yet existing planners either oversimplify the payload
geometry or fail to handle the kinematic coupling between manipulator links, leading to
lost feasible space or stalled optimization. This letter presents a real-time whole-body
motion planning framework for mobile manipulators carrying arbitrarily shaped payloads.
The front-end employs a chain-decomposed kernel-based collision check that preserves the
true geometry of the robot and payload, with compact storage and fast bit-level queries.
A mid-end preprocessing stage converts the front-end path into a continuous trajectory
enforcing smoothness and feasibility, and executes it directly when collision-free to
bypass the costly back-end. When refinement is required, the back-end performs
trajectory optimization built on a Kinematically-Coupled SVSDF (KC-SVSDF), which
propagates collision-avoidance gradients along the kinematic chain to produce coherent
whole-body escape directions. Ablation studies, comparative benchmarks against state-of-
the-art baselines, and real-world experiments on a differential-drive mobile manipulator
demonstrate that the proposed framework reliably transports large, non-convex payloads
through tight passages and cluttered environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.07005v1
- Authors: Yisheng Li, Longji Yin, Tingrui Zhang, Ruize Xue, Haoda Zhu, Nan Chen, Siqi Liang, Yuxi Liu, Fu Zhang
- Published: 2026-08-07T09:20:31Z
- Age days: 3

</details>
