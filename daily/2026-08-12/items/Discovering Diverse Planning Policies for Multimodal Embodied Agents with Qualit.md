---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08523v1"
published: "2026-08-09T06:41:53Z"
age_days: 2
score: 27
created: 2026-08-12
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Discovering Diverse Planning Policies for Multimodal Embodied Agents with Quality-Diversity Optimization

> [!summary] 一句话结论（基于摘要）
> Experiments on the ThreeDWorld transport benchmark show that the proposed framework improves both task success and interaction efficiency over representative baseline planners.

## 关键点

- **问题**：However, state-of-the-art large-model-based planners often rely on a single dominant planning style during execution.
- **创新点 / 方法**：Multimodal embodied agents are increasingly required to solve long-horizon tasks by integrating visual observations, textual goals, and interaction history into closed-loop decision making.
- **证据**：Experiments on the ThreeDWorld transport benchmark show that the proposed framework improves both task success and interaction efficiency over representative baseline planners.
- **局限**：We address this limitation by proposing a Quality-Diversity (QD) framework for discovering diverse planning policies for multimodal embodied agents.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multimodal embodied agents are increasingly required to solve long-horizon tasks by
integrating visual observations, textual goals, and interaction history into closed-loop
decision making. However, state-of-the-art large-model-based planners often rely on a
single dominant planning style during execution. Once this execution mode becomes
ineffective, the agent may remain stalled for many steps, repeatedly interacting with
the environment without making meaningful progress. We address this limitation by
proposing a Quality-Diversity (QD) framework for discovering diverse planning policies
for multimodal embodied agents. The proposed method treats planning-policy templates as
evolvable individuals and organizes them into a behavior-indexed archive rather than
collapsing search to a single prompt style. In the offline stage, rollout trajectories
are summarized into structured success and failure experiences, which guide policy
variation through recombination and experience-guided mutation. The resulting policies
are mapped into a behavior space defined by interaction intensity and goal-directedness,
and the highest-quality policy in each niche is retained in the archive. In the online
stage, the agent executes one policy at a time while monitoring task progress. When
persistent stall is detected, the system rolls back to the latest checkpoint and
switches to a behaviorally distinct archive policy to resume execution. Experiments on
the ThreeDWorld transport benchmark show that the proposed framework improves both task
success and interaction efficiency over representative baseline planners. These results
suggest that discovering diverse policy repertoires is an effective way to support
adaptive multimodal planning and online failure recovery.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08523v1
- Authors: Pengfei Xu, Yong Liu, Xiaoya Nan, Qiang Yang, Peilan Xu
- Published: 2026-08-09T06:41:53Z
- Age days: 2

</details>
