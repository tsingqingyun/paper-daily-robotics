---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20710v1"
published: "2026-07-22T20:26:07Z"
age_days: 2
score: 23
created: 2026-07-25
concepts: ["具身智能评测与基准"]
---

# Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments

> [!summary] 一句话结论（基于摘要）
> To address these limitations, we propose a pipeline for ground-target protection against UAV attacks that employs autonomous swarms of UAVs.

## 关键点

- **问题**：However, such resources may not be available in modern warfare scenarios.
- **创新点 / 方法**：To address these limitations, we propose a pipeline for ground-target protection against UAV attacks that employs autonomous swarms of UAVs.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The presence of UAVs in military operations has recently increased, also increasing the
demand for defense systems against UAV attacks. UAVs can also be used as
countermeasures. Most available methods rely on UAV-to-UAV communication and global
positioning. However, such resources may not be available in modern warfare scenarios.
To address these limitations, we propose a pipeline for ground-target protection against
UAV attacks that employs autonomous swarms of UAVs. We assume a communication- and GPS-
denied environment in which the UAVs use onboard sensors to track the target and
coordinate as a swarm. We developed Kalman filters to estimate the states of unknown
targets and the positions of UAVs in the swarm using only relative measurements. Also,
our strategy is to encircle the target of interest to maximize coverage. To achieve
that, we propose a decentralized swarm encirclement technique that adapts to the
target's motion. Our approach was extensively validated using real robots, demonstrating
its effectiveness in detecting, encircling, and intercepting hostile UAVs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20710v1
- Authors: Dimitria Silveria, Paulo Ricardo Marques de Araujo, Tiago Nascimento, Sidney Givigi
- Published: 2026-07-22T20:26:07Z
- Age days: 2

</details>
