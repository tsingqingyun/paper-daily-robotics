---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19190v1"
published: "2026-07-21T15:23:38Z"
age_days: 0
score: 42
created: 2026-07-22
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents

> [!summary] 一句话结论（基于摘要）
> The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate.

## 关键点

- **问题**：Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runna…
- **创新点 / 方法**：We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states.
- **证据**：The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-22/Agentic Real2Sim Physics-based World Modeling with Vision-Language Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-to-sim conversion for robotic interaction with objects remains labor-intensive
because it requires more than visual reconstruction: a streamlined real2sim process must
recover scene geometries and object states, infer physical parameters, and assemble
actors, objects, cameras, poses, and trajectories into a runnable physical simulation.
Today this process still depends on manual tuning of visual foundation models, mesh
cleanup, coordinate-frame alignment, and brittle workflow glue across visual perception
tools and simulators. We introduce \textit{Agentic Real2Sim}, a framework for
generalized physical world modeling with vision-language agents, converting a real-world
recording of object-robot interaction into a simulatable episodic twin which preserves
observations, geometries, robot interactions, and object states. We evaluate Agentic
Real2Sim on rigid-object manipulation, deformable-object interaction, and humanoid
motion scenes, spanning domains that are usually handled by separate Real2Sim pipelines,
marking a first step toward scalable conversion. The framework's agentic decisions can
be driven by an open-weight VLM backend at a small fraction of the cost of frontier
models, while attaining comparable conversion success rate. We aim to use the resulting
real-world-aligned twins for downstream robotics tasks, specifically policy learning and
evaluation. The project site is available at
https://ericchen321.github.io/agentic_real2sim.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19190v1
- Authors: Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen
- Published: 2026-07-21T15:23:38Z
- Age days: 0

</details>
