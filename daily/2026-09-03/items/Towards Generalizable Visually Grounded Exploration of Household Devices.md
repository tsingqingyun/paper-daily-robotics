---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00845v1"
published: "2026-09-01T07:42:45Z"
age_days: 1
score: 30
created: 2026-09-03
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Towards Generalizable Visually Grounded Exploration of Household Devices

> [!summary] 先说人话（基于摘要）
> VGEBench 不再让模型照说明书或标注轨迹操作设备，而是要求其通过“提出假设—交互—依据反馈修正”探索陌生家用装置。逻辑驱动状态机提供多轮动态测试。

## 这篇到底在做什么

- **卡在哪里**：现有具身探索依赖人工轨迹，或在基准中直接提供文档，无法测量模型能否把抽象常识主动落到细粒度视觉可供性上；静态识别也覆盖不了操作中的状态更新。
- **关键解法**：基准以 Logic-Driven State Machine 模拟设备状态和多轮交互，迫使 VLM 主动观察、尝试并根据反馈纠错；区别于静态问答或轨迹模仿，它直接评估无手册、无专项训练的新设备探索。
- **拿什么证明**：摘要称现有 VLM 在将语义知识转为物理执行以及维持长程状态跟踪方面面临显著困难；未给出模型数量、任务规模或结果数字。

## 值不值得读

- **和你的研究有什么关系**：对具身 Agent 与机器人学习者，它补上了开放式功能探索评测，可区分“知道设备是什么”与“能通过交互弄清怎么用”。
- **先别急着信**：状态机仿真能否覆盖真实设备的连续动力学、感知噪声和不可逆后果，是最需要查全文的外部有效性问题。
- **判断**：值得读任务构造和指标，作为新能力缺口的测量工具很有价值；其对真实机器人探索的代表性仍需谨慎验证。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Towards Generalizable Visually Grounded Exploration of Household Devices.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advancements in Vision-Language Models (VLMs) have demonstrated impressive capabilities in static visual recognition and high-level semantic reasoning. However, current embodied exploration paradigms still heavily rely on imitation learning from human-annotated trajectories, which severely limits agents' generalization ability. The key bottleneck of realizing general autonomous embodied agents lies in Generalizable Visually Grounded Exploration: the ability to operate novel devices without manuals or specific training by actively grounding abstract world knowledge into fine-grained visual affordances. Yet, existing benchmarks fail to evaluate this capability: they generally rely on explicit documents and annotated trajectories, neglecting the dynamic Hypothesis-Interaction-Refinement process essential for functional device operation. To bridge this gap, we introduce VGEBench, a comprehensive benchmark designed to evaluate the generalizable visually grounded exploration capabilities of VLMs. Unlike static datasets, we construct a Logic-Driven State Machine framework. This framework simulates multi-turn interaction loops, compelling agents to achieve goals by active visual perception and feedback-driven correction. Experimental results demonstrate that existing VLMs face significant challenges in translating semantic knowledge into physical execution and maintaining long-horizon state tracking.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00845v1
- Authors: Linhao Zheng, Zeming Liu, Wangke Chen, Li Zeng, Wanxiang Che, Heyan Huang, Yuhang Guo
- Published: 2026-09-01T07:42:45Z
- Age days: 1

</details>
