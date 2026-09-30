---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09612v1"
published: "2026-09-09T02:11:29Z"
age_days: 1
score: 25
created: 2026-09-11
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# MuJoCable: Reduced-Order Surface-Routed Cable Transmission for Tendon-Driven Robots

> [!summary] 先说人话（基于摘要）
> We present MuJoCable, which adds a reduced-order, configuration-dependent cable transmission to MuJoCo.

## 这篇到底在做什么

- **卡在哪里**：Tendon transmissions reduce distal inertia and add compliance, yet routing, slack, and friction govern motion and force transfer.
- **关键解法**：We present MuJoCable, which adds a reduced-order, configuration-dependent cable transmission to MuJoCo.
- **拿什么证明**：摘要未报告明确实验结论；需阅读全文核查。

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：On the underactuated 18-joint SpiRobs, MuJoCable reveals friction-driven load growth and proximal redistribution of joint rotation that the native tendon does not represent.
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/MuJoCable Reduced-Order Surface-Routed Cable Transmission for Tendon-Driven Robo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Tendon transmissions reduce distal inertia and add compliance, yet routing, slack, and friction govern motion and force transfer. Mainstream rigid-body robotics simulators such as MuJoCo do not jointly resolve moving noncircular contact, unilateral tension, and segment friction. We present MuJoCable, which adds a reduced-order, configuration-dependent cable transmission to MuJoCo. Its routing algorithm jointly optimizes an ordered path across moving analytic and mesh surfaces. A unilateral axial law, directional Capstan propagation, and nodal virtual work map this path to segment tensions and body forces. The warm-started engine plugin applies these forces during simulation and exposes route and load states for design. Pulley benchmarks recover analytical transmission relations with a Capstan-ratio error below 0.5%. On the underactuated 18-joint SpiRobs, MuJoCable reveals friction-driven load growth and proximal redistribution of joint rotation that the native tendon does not represent. Hardware tests on SpiRobs and a tendon-route-coupled finger reproduce observed motion sequences. By making physical threading executable, MuJoCable brings transmission sources of the simulation-to-reality gap into route, cable, and actuator design before fabrication.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09612v1
- Authors: Yi Zhang, Qi Shao, Yicong Lin, Muyuan Ma, Tao Sun, Yue Xie
- Published: 2026-09-09T02:11:29Z
- Age days: 1

</details>
