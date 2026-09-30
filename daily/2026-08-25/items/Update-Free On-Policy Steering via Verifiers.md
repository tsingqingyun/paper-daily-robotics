---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2603.10282"
published: "Mon, 24 Aug 2026 00:00:00 -0400"
age_days: 0
score: 25
created: 2026-08-25
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Update-Free On-Policy Steering via Verifiers

> [!summary] 一句话结论（基于摘要）
> We present results from both simulation and real-world data and achieve an average 49% improvement in success rate over the base policy across 5 real tasks.

## 问题

Despite their successes, BC policies are often brittle and struggle with precise manipulation.

## 创新点或方法

To overcome these issues, we propose UF-OPS, an Update-Free On-Policy Steering method that enables the robot to predict the success likelihood of its actions and adapt its strategy at execution time.

## 证据

We present results from both simulation and real-world data and achieve an average 49% improvement in success rate over the base policy across 5 real tasks.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-25/Update-Free On-Policy Steering via Verifiers.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2603.10282v3 Announce Type: replace Abstract: In recent years, Behavior Cloning (BC) has become one of the most prevalent methods for learning manipulation from human demonstrations. Despite their successes, BC policies are often brittle and struggle with precise manipulation. To overcome these issues, we propose UF-OPS, an Update-Free On-Policy Steering method that enables the robot to predict the success likelihood of its actions and adapt its strategy at execution time. We accomplish this by training verifier functions using policy rollout data obtained during an initial evaluation of the policy. These verifiers are subsequently used to steer the base policy toward actions with a higher likelihood of success. Our method improves the performance of black-box diffusion policies, without changing the base parameters, making it lightweight and flexible. We present results from both simulation and real-world data and achieve an average 49% improvement in success rate over the base policy across 5 real tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2603.10282
- Authors: Maria Attarian, Ian Vyse, Jasper Gerigk, Evgenii Opryshko, Yifan Ruan, Anas Almasri, Sumeet Singh, Yilun Du, Igor Gilitschenski, Claas Voelcker
- Published: Mon, 24 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
