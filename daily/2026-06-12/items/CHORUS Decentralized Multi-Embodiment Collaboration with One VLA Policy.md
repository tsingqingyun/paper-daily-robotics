---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12352v1"
published: "2026-06-10T17:26:08Z"
age_days: 1
score: 31
created: 2026-06-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

> [!summary] 一句话结论（基于摘要）
> In real-world experiments including mobile tape measurement, library book handovers, and laundry basket lifting, CHORUS achieves a 64% point improvement over decentralized, from-scratch models, improves reactivity to teammate behavior by 40% points, and outpe…

## 关键点

- **问题**：However, achieving such coordination in mobile multi-robot settings remains challenging: centralized methods conditioned on the combined observations of a team scale poorly with team size, and decentralized methods that train one policy per robot often require explicit alignment procedures or information sharing at in…
- **创新点 / 方法**：We propose CHORUS, a framework that adapts a single VLA backbone to control diverse, multi- robot teams.
- **证据**：In real-world experiments including mobile tape measurement, library book handovers, and laundry basket lifting, CHORUS achieves a 64% point improvement over decentralized, from-scratch models, improves reactivity to teammate behavior by 40% points, and outperforms centralized baselines.
- **局限**：However, achieving such coordination in mobile multi-robot settings remains challenging: centralized methods conditioned on the combined observations of a team scale poorly with team size, and decentralized methods that train one policy per robot often require explicit alignment procedures or information sharing at in…

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multi-robot collaboration allows robots to efficiently take on a wide range of tasks,
from moving a couch through a doorway to assembling structures on a construction site.
However, achieving such coordination in mobile multi-robot settings remains challenging:
centralized methods conditioned on the combined observations of a team scale poorly with
team size, and decentralized methods that train one policy per robot often require
explicit alignment procedures or information sharing at inference time to overcome
partial observability. Our key insight is that the visuomotor priors of pretrained
vision-language-action (VLA) models should enable reactive, decentralized collaboration
from each robot's local observations alone, without these inference-time assumptions. We
propose CHORUS, a framework that adapts a single VLA backbone to control diverse, multi-
robot teams. At inference time, each robot runs an independent copy of CHORUS,
conditioned only on its own observations and a robot-identifying prompt. In real-world
experiments including mobile tape measurement, library book handovers, and laundry
basket lifting, CHORUS achieves a 64% point improvement over decentralized, from-scratch
models, improves reactivity to teammate behavior by 40% points, and outperforms
centralized baselines. Together, these results show that a shared VLA backbone is
capable of achieving decentralized multi-robot collaboration, without per-robot policies
or inter-robot communication at inference.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12352v1
- Authors: Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg
- Published: 2026-06-10T17:26:08Z
- Age days: 1

</details>
