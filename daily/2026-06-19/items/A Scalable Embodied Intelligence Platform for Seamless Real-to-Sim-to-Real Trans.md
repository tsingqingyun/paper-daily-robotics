---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18646v1"
published: "2026-06-17T03:31:43Z"
age_days: 1
score: 36
created: 2026-06-19
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks

> [!summary] 一句话结论（基于摘要）
> To address these challenges, we develop BestMan, a scalable and seamless real-to-sim-to-real platform that bridges the gap between the simulation and the real world, enabling effective strategy development, integration, and deployment for household mobile man…

## 关键点

- **问题**：However, achieving a seamless transfer across the real-to-sim-to-real cycle faces three key challenges, including costly high-fidelity simulation scenes reconstruction, the complexity of systematic strategy evaluation in simulation, and incompatible real-world deployments.
- **创新点 / 方法**：To address these challenges, we develop BestMan, a scalable and seamless real-to-sim-to-real platform that bridges the gap between the simulation and the real world, enabling effective strategy development, integration, and deployment for household mobile manipulation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-19/A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Trans.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Mobile manipulation is a fundamental capability in embodied intelligence robotics. The
growing demand for robust and generalizable manipulation in unstructured household
environments has driven rapid progress in embodied intelligence platforms. However,
achieving a seamless transfer across the real-to-sim-to-real cycle faces three key
challenges, including costly high-fidelity simulation scenes reconstruction, the
complexity of systematic strategy evaluation in simulation, and incompatible real-world
deployments. To address these challenges, we develop BestMan, a scalable and seamless
real-to-sim-to-real platform that bridges the gap between the simulation and the real
world, enabling effective strategy development, integration, and deployment for
household mobile manipulation. Specifically, we design a novel Automated Scene
Generation (ASG) module to reconstruct realistic simulations from real observations.
Then, we propose a simulation-guided task formalization and skill learning architecture
that supports the flexible integration and large-scale evaluations of hybrid skill
strategies in simulation. Finally, to enhance the real-world scalability, we develop a
Hardware-agnostic and Unified Middleware (HUM) to ensure seamless and compatible sim-to-
real transfer across heterogeneous mobile manipulators for real deployments.
Experimental results demonstrate the superior performance of our proposed platform in
establishing standardized benchmarks and facilitating promising research in the field of
mobile manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18646v1
- Authors: Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen
- Published: 2026-06-17T03:31:43Z
- Age days: 1

</details>
