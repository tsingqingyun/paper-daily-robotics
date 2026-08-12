---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12162v1"
published: "2026-05-12T14:13:06Z"
age_days: 1
score: 29
created: 2026-05-14
concepts: ["机器人学习"]
---

# X-Imitator: Spatial-Aware Imitation Learning via Bidirectional Action-Pose Interaction

> [!summary] 一句话结论（基于摘要）
> Extensive experiments across 24 simulated and 3 real-world tasks demonstrate that our framework significantly outperforms both vanilla policies and prior methods utilizing explicit pose guidance.

## 关键点

- **问题**：Effectively handling the interplay between spatial perception and action generation remains a critical bottleneck in robotic manipulation.
- **创新点 / 方法**：To address this, we propose X-Imitator, a versatile dual-path framework that models spatial perception and action execution as a tightly coupled bidirectional loop.
- **证据**：Extensive experiments across 24 simulated and 3 real-world tasks demonstrate that our framework significantly outperforms both vanilla policies and prior methods utilizing explicit pose guidance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Effectively handling the interplay between spatial perception and action generation
remains a critical bottleneck in robotic manipulation. Existing methods typically treat
spatial perception and action execution as decoupled or strictly unidirectional
processes, fundamentally restricting a robot's ability to master complex manipulation
tasks. To address this, we propose X-Imitator, a versatile dual-path framework that
models spatial perception and action execution as a tightly coupled bidirectional loop.
By reciprocally conditioning current pose predictions on past actions and vice versa,
this framework enables continuous mutual refinement between spatial reasoning and action
generation. This joint modeling exactly mimics human internal forward models. Designed
as a modular architecture, the system can be seamlessly integrated into various
visuomotor policies. Extensive experiments across 24 simulated and 3 real-world tasks
demonstrate that our framework significantly outperforms both vanilla policies and prior
methods utilizing explicit pose guidance. The code will be open sourced.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12162v1
- Authors: Kai Xiong, Hongjie Fang, Lixin Yang, Cewu Lu
- Published: 2026-05-12T14:13:06Z
- Age days: 1

</details>
