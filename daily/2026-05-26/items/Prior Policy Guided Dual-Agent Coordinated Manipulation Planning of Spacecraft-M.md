---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25362v1"
published: "2026-05-25T02:32:23Z"
age_days: 1
score: 26
created: 2026-05-26
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Prior Policy Guided Dual-Agent Coordinated Manipulation Planning of Spacecraft-Manipulator System

> [!summary] 一句话结论（基于摘要）
> To enhance learning efficiency, we present a prior policy-guided Deep Reinforcement Learning algorithm incorporating the Timestep-level Expert Switching Guidance (TESG) mechanism, thereby promoting global convergence and improving task success rates.

## 关键点

- **问题**：The strong dynamic coupling between the manipulator and the base poses a significant challenge to maintaining spacecraft attitude stability, potentially compromising mission safety.
- **创新点 / 方法**：In this paper, we propose a Dual-Agent Coordinated Manipulation Planning (DACMP) framework that simultaneously achieves high-precision end-effector pose reaching for a 6-DoF space manipulator and attitude stabilization of the base spacecraft.
- **证据**：To enhance learning efficiency, we present a prior policy-guided Deep Reinforcement Learning algorithm incorporating the Timestep-level Expert Switching Guidance (TESG) mechanism, thereby promoting global convergence and improving task success rates.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The strong dynamic coupling between the manipulator and the base poses a significant
challenge to maintaining spacecraft attitude stability, potentially compromising mission
safety. In this paper, we propose a Dual-Agent Coordinated Manipulation Planning (DACMP)
framework that simultaneously achieves high-precision end-effector pose reaching for a
6-DoF space manipulator and attitude stabilization of the base spacecraft. To enhance
learning efficiency, we present a prior policy-guided Deep Reinforcement Learning
algorithm incorporating the Timestep-level Expert Switching Guidance (TESG) mechanism,
thereby promoting global convergence and improving task success rates. Extensive
experiments demonstrate that DACMP significantly outperforms baseline DRL algorithms in
terms of task success rate and control precision. Furthermore, the robustness of DACMP
is validated under various challenging scenarios, including system constraints,
environmental disturbances, and perception uncertainties. The code and simulation
configurations are available on GitHub: https://github.com/HIT-YuhuiHu/DACMP.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25362v1
- Authors: Yuhui Hu, Dong Zhou, Kaihong Ouyang, Zhongliang Yu, Jianfeng Lv, Xiangyu Shao
- Published: 2026-05-25T02:32:23Z
- Age days: 1

</details>
