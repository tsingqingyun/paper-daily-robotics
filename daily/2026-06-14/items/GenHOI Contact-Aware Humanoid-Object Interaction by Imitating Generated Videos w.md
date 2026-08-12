---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12995v1"
published: "2026-06-11T07:31:05Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["世界模型", "机器人学习"]
---

# GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training

> [!summary] 一句话结论（基于摘要）
> In this work, we present \textit{GenHOI}, a simple yet effective framework that enables humanoid robots to perform diverse object- interaction tasks in a zero-shot manner by directly imitating a single generated video, without task-specific training or physic…

## 关键点

- **问题**：Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to the tight coupling between dynamic balance and stable interaction with diverse objects.
- **创新点 / 方法**：In this work, we present \textit{GenHOI}, a simple yet effective framework that enables humanoid robots to perform diverse object- interaction tasks in a zero-shot manner by directly imitating a single generated video, without task-specific training or physical demonstration data.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to the tight coupling between dynamic balance and stable interaction with diverse objects.

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/GenHOI Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos w.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet
it remains challenging due to the tight coupling between dynamic balance and stable
interaction with diverse objects. Existing methods often require time-consuming task-
specific policy training or rely on rigid trajectory replay, which limits their ability
to accommodate novel interaction scenarios. In this work, we present \textit{GenHOI}, a
simple yet effective framework that enables humanoid robots to perform diverse object-
interaction tasks in a zero-shot manner by directly imitating a single generated video,
without task-specific training or physical demonstration data. GenHOI first reconstructs
the robot-object scene in simulation and renders a first-frame image, which, together
with the language command, conditions the synthesis of a task-oriented interaction
video. The generated video is then analyzed to identify interaction-relevant contact
events and estimate hand-object contact regions, which are encoded as object-centric
geometric constraints that convert visual interaction cues into physically grounded
optimization priors. Guided by these priors, the reference motion recovered from the
video is refined and smoothed to resolve the scale ambiguity inherent in 2D video
generation, while adapting a single reference trajectory to unseen robot-object relative
poses. The optimized trajectory is finally executed by a closed-loop tracking
controller. We validate the proposed framework in extensive simulation and real-world
experiments across diverse object-interaction tasks, including box grasping, asymmetric
bimanual chair carrying, table lifting from below, and cylindrical-object enveloping.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12995v1
- Authors: Zhihai Bi, Qiang Zhang, Guoyang Zhao, Jiahang Cao, Xueyin Luo, Yushan Zhang, Jinglan Xu, Ruoyu Geng, Yulin Li, Andrew F. Luo, Jun Ma
- Published: 2026-06-11T07:31:05Z
- Age days: 2

</details>
