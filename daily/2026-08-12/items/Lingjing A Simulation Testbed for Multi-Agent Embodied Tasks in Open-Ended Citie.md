---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08045v1"
published: "2026-08-08T10:18:58Z"
age_days: 3
score: 25
created: 2026-08-12
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Lingjing: A Simulation Testbed for Multi-Agent Embodied Tasks in Open-Ended Cities

> [!summary] 一句话结论（基于摘要）
> We present \textbf{Lingjing}, a simulation platform for heterogeneous multi-agent embodied intelligence in open-ended urban environments.

## 关键点

- **问题**：Controlled studies further examine communication, scalability, robustness, and failure provenance.
- **创新点 / 方法**：We present \textbf{Lingjing}, a simulation platform for heterogeneous multi-agent embodied intelligence in open-ended urban environments.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/Lingjing A Simulation Testbed for Multi-Agent Embodied Tasks in Open-Ended Citie.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Urban embodied intelligence requires coordination among heterogeneous agents (e.g.,
UAVs, ground robots, and autonomous vehicles) in dynamic cities. Simulators therefore
provide a scalable foundation for developing and evaluating such coordination. Existing
platforms nevertheless isolate different embodiments and decouple them from task design
and evaluation. We present \textbf{Lingjing}, a simulation platform for heterogeneous
multi-agent embodied intelligence in open-ended urban environments. Lingjing
reconstructs and renders evolving cities from geographic data, synchronizes multiple
physics engines, and exposes shared physical and structured urban state to agents. Its
Gym-like interface supports user-defined ReAct agents and single- or multi-agent
natural-language missions with configurable star or broadcast communication and resource
constraints. Each episode becomes an attribution-ready replay that links agent
trajectories and communication to relation-graph changes, resource consumption, and
engine-based evaluations for systematic diagnosis. We evaluate twelve vision-language
models on nine urban tasks under a shared engine-in-the-loop protocol. Controlled
studies further examine communication, scalability, robustness, and failure provenance.
Results expose persistent bottlenecks in grounding and long-horizon execution. They also
show task-dependent coordination trade-offs and diminishing returns from added capacity,
while heavier workloads further reduce success. Lingjing provides a unified testbed that
enables reproducible end-to-end evaluation and systematic failure diagnosis in urban
multi-agent embodied intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08045v1
- Authors: Xiaohe Li, Yiru Wang, Junhao Fan, Mingyuan Liu, Jie Huang, Kaixin Zhang, Jiahao Li, Chen Qian, Zide Fan
- Published: 2026-08-08T10:18:58Z
- Age days: 3

</details>
