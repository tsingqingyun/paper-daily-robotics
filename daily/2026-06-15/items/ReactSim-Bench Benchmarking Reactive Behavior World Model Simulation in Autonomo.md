---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14058v1"
published: "2026-06-12T03:11:06Z"
age_days: 2
score: 26
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving

> [!summary] 一句话结论（基于摘要）
> In this work, we introduce ReactSim-Bench for evaluating the reactive capability of behavior world model simulation in autonomous driving.

## 关键点

- **问题**：However, existing behavior simulation benchmarks do not directly measure reactive capability.
- **创新点 / 方法**：In this work, we introduce ReactSim-Bench for evaluating the reactive capability of behavior world model simulation in autonomous driving.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reactive capability is a key property of data-driven behavior world model simulators for
autonomous driving simulation systems. With this capability, simulated world agents can
respond feasibly to autonomous vehicle (AV) behaviors that differ from the log. However,
existing behavior simulation benchmarks do not directly measure reactive capability.
They often let the simulator jointly control the AV and surrounding agents and evaluate
realism through log similarity or open-loop prediction metrics. In this work, we
introduce ReactSim-Bench for evaluating the reactive capability of behavior world model
simulation in autonomous driving. We decouple the control of agents and the AV, using AV
behaviors that differ from the log and require agents to respond as independent AV
inputs. To obtain these AV behaviors, we construct a pipeline that uses an AV planner
model to generate candidate behaviors and filters the data using rules and manual
verification. Collision metrics, map-based metrics, and kinematic feasibility metrics
are used to evaluate the safety and rule compliance of reactive responses. We construct
2,636 test scenarios with three categories and conduct a systematic evaluation of state-
of-the-art models across multiple architectures, including Transformer-based, diffusion-
based, and next-token-prediction-based models. We further analyze how replan frequency
affects performance and provide insights for future studies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14058v1
- Authors: Zhiyuan Zhang, Yanlun Peng, Jianing Zhang, Xianda Guo, Zehan Huang, Haoran Liu, Qifeng Li, Shaofeng Zhang, Xiaosong Jia, Junchi Yan
- Published: 2026-06-12T03:11:06Z
- Age days: 2

</details>
