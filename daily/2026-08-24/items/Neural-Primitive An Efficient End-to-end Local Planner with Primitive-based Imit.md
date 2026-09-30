---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20948v1"
published: "2026-08-21T10:13:44Z"
age_days: 3
score: 27
created: 2026-08-24
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight

> [!summary] 一句话结论（基于摘要）
> It achieves ultra-fast computation (below 1ms on a standard desktop and average 3.68ms during onboard flight), while maintaining low onboard memory requirements (less than 1.5MiB).

## 问题

Autonomous flight in unknown cluttered environments is hindered by the computation-quality-memory trilemma of onboard trajectory generation.

## 创新点或方法

In this paper, we propose an efficient end-to-end local planner via imitation learning.

## 证据

It achieves ultra-fast computation (below 1ms on a standard desktop and average 3.68ms during onboard flight), while maintaining low onboard memory requirements (less than 1.5MiB).

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：智能体 Agent 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/Neural-Primitive An Efficient End-to-end Local Planner with Primitive-based Imit.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous flight in unknown cluttered environments is hindered by the computation-quality-memory trilemma of onboard trajectory generation. In this paper, we propose an efficient end-to-end local planner via imitation learning. A lightweight offline-primitive-based dataset collection framework is designed to produce safe and high-quality trajectory primitives in non-convex environments. A compact neural network directly maps sensory inputs to polynomial coefficients that inherently encode higher-order dynamical information. The learned policy generates smooth, empirically collision-free and dynamically feasible trajectories in real time without back-end solving. It achieves ultra-fast computation (below 1ms on a standard desktop and average 3.68ms during onboard flight), while maintaining low onboard memory requirements (less than 1.5MiB). Extensive simulation benchmarks demonstrate superiority in both planning latency and target-reaching progress quality. Zero-shot deployment in real-world experiments further validates the robust sim-to-real transfer capability of the proposed method.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20948v1
- Authors: Zhitao Liu, Guangtong Xu, Zihan Wang, Jialiang Hou, Chao Xu, Fei Gao
- Published: 2026-08-21T10:13:44Z
- Age days: 3

</details>
