---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01088v1"
published: "2026-07-01T15:45:08Z"
age_days: 4
score: 28
created: 2026-07-06
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ROSA: A Robotics Foundation Model Serving System for Robot Factories

> [!summary] 一句话结论（基于摘要）
> The results show that ROSA improves factory productivity by up to 12.06x over conventional dedicated serving systems.

## 关键点

- **问题**：While RFM serving systems are central to this vision, existing systems are largely shaped by a single-robot, single-model assumption: inference is treated as an edge-computing problem handled by an on-robot or dedicated nearby GPU, and the serving objective is to minimize the latency of a single action model.
- **创新点 / 方法**：In this paper, we propose ROSA, an RFM serving system for robot factories designed around three key principles.
- **证据**：The results show that ROSA improves factory productivity by up to 12.06x over conventional dedicated serving systems.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-06/ROSA A Robotics Foundation Model Serving System for Robot Factories.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotics foundation models (RFMs) are making general-purpose robots increasingly
practical for factory deployments. While RFM serving systems are central to this vision,
existing systems are largely shaped by a single-robot, single-model assumption:
inference is treated as an edge-computing problem handled by an on-robot or dedicated
nearby GPU, and the serving objective is to minimize the latency of a single action
model. In this paper, we propose ROSA, an RFM serving system for robot factories
designed around three key principles. First, ROSA adopts shared GPU-pool serving,
allowing a fleet of robots to access powerful server-class GPUs over the network in
order to improve inference performance, battery duration, and GPU utilization. Second,
ROSA provides a robotics-aware programming abstraction and system design that supports
multi-model pipelines, per-task performance requirements, and failure handling. Third,
ROSA uses factory-objective-driven scheduling to maximize SLO-qualified factory
productivity rather than minimizing individual request latency. We implement ROSA on top
of Ray Serve for distributed orchestration, with vLLM, PyTorch, and JAX as model-serving
backends, and evaluate it on both real robots and synthetic large-scale workloads. The
results show that ROSA improves factory productivity by up to 12.06x over conventional
dedicated serving systems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01088v1
- Authors: Wenqi Jiang, Jason Clemons, Rowland O'Flaherty, Hugo Hadfield, Alperen Degirmenci, Shuran Song, Yashraj Narang, Christos Kozyrakis
- Published: 2026-07-01T15:45:08Z
- Age days: 4

</details>
