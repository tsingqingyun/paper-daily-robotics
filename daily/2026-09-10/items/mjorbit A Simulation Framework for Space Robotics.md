---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08010v1"
published: "2026-09-07T21:45:19Z"
age_days: 2
score: 27
created: 2026-09-10
concepts: ["世界模型", "机器人学习"]
---

# mjorbit: A Simulation Framework for Space Robotics

> [!summary] 先说人话（基于摘要）
> mjorbit 把轨道运动与机器人接触仿真接起来，让空间机器人也能用统一接口做控制和强化学习实验。

## 这篇到底在做什么

- **卡在哪里**：在轨服务、装配和制造涉及多体机器人接触，需要同时处理航天器运动与机器人动力学；摘要关注如何将轨道传播接入现有机器人仿真，并兼顾效率与规模。
- **关键解法**：先实证比较轨道传播的耦合方法，再在 MuJoCo 上加入航天器动力学、执行器和传感器，通过 Python API 提供低延迟 C++ CPU 后端与高吞吐 GPU 后端。
- **拿什么证明**：展示了用模型预测控制和强化学习求解多个在轨案例，并提供开源代码与示例。摘要未给出可核查的性能或精度数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习研究者，这是扩展到空间接触任务的仿真基础设施；对世界模型研究者，可作为交互数据和验证环境，但本身并非学习式世界模型。
- **先别急着信**：需核查轨道与接触动力学耦合的误差，以及两个后端的性能和数值一致性。
- **判断**：有空间机器人需求时值得读实现并运行示例；普通操作学习研究者浏览接口与任务范围即可。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/mjorbit A Simulation Framework for Space Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This paper presents a general framework for simulating multi-body space robots with contact. We bring efficient, large-scale robot simulation to in-space servicing, assembly, and manufacturing applications. First, we perform an empirical trade study of methods for coupling orbit propagation with existing robotics simulation frameworks. Next, we present mjorbit, a general, flexible, and performant framework built on the MuJoCo engine widely used in robotics, to which we add key spacecraft dynamics, actuators, and sensors. We provide a low-latency C++ CPU backend and a high-throughput GPU backend behind a simple Python API. We demonstrate mjorbit by solving several realistic on-orbit case studies with both model-predictive control and reinforcement learning. Open-source code and examples are available at: https://johnzhang3.github.io/mjorbit/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08010v1
- Authors: John Z. Zhang, Joris Verhagen, Fausto Vega, Patrick McKeen, Zachary Manchester
- Published: 2026-09-07T21:45:19Z
- Age days: 2

</details>
