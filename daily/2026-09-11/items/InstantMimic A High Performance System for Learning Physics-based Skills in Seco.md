---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09821v1"
published: "2026-09-09T07:23:51Z"
age_days: 1
score: 28
created: 2026-09-11
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# InstantMimic: A High Performance System for Learning Physics-based Skills in Seconds

> [!summary] 先说人话（基于摘要）
> We present InstantMimic, a system that addresses these inefficiencies by making the entire training loop GPU-native.

## 问题

Physics-based character control is a long-standing challenge in computer graphics and robotics, requiring policies that satisfy complex dynamics while producing realistic motion.

## 创新点或方法

We present InstantMimic, a system that addresses these inefficiencies by making the entire training loop GPU-native.

## 证据

摘要未报告明确实验结论；需阅读全文核查。


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：智能体 Agent 世界模型 机器人学习
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/InstantMimic A High Performance System for Learning Physics-based Skills in Seco.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physics-based character control is a long-standing challenge in computer graphics and robotics, requiring policies that satisfy complex dynamics while producing realistic motion. Recent Deep RL approaches, particularly imitation learning methods such as DeepMimic, have had broad impact beyond animation, influencing robotics by enabling agile and expressive behaviors. While these approaches achieve impressive results, they remain computationally inefficient to train in practice. Despite GPU-accelerated simulation, we find that end-to-end pipelines often underutilize hardware due to overheads outside the physics solver, caused by fragmented GPU kernels and CPU memory access in the critical path. We present InstantMimic, a system that addresses these inefficiencies by making the entire training loop GPU-native. Built on a GPU-native physics backend, our unified pipeline integrates simulation, environment computation, policy inference, and policy updates within a single execution flow. As a result, InstantMimic reduces training time for diverse physics-based skills to a few seconds and makes LLM-agent-driven hyperparameter search practical.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09821v1
- Authors: Ikjun Choi, Geonho Leem, Jungdam Won
- Published: 2026-09-09T07:23:51Z
- Age days: 1

</details>
