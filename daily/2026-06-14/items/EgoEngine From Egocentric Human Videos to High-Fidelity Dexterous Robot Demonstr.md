---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12604v1"
published: "2026-06-10T19:01:40Z"
age_days: 3
score: 27
created: 2026-06-14
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations

> [!summary] 一句话结论（基于摘要）
> We propose EgoEngine, a scalable framework for transforming egocentric human manipulation videos into high-fidelity robot data.

## 关键点

- **问题**：Dexterous manipulation is limited by the cost of collecting large-scale robot demonstrations.
- **创新点 / 方法**：We propose EgoEngine, a scalable framework for transforming egocentric human manipulation videos into high-fidelity robot data.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Dexterous manipulation is limited by the cost of collecting large-scale robot
demonstrations. Egocentric human videos offer a scalable source of diverse manipulation
behaviors, but directly using them for robot learning requires bridging two gaps: the
visual gap between human and robot observations, and the action gap between human motion
and robot-executable action. We propose EgoEngine, a scalable framework for transforming
egocentric human manipulation videos into high-fidelity robot data. Given an egocentric
RGB video, EgoEngine produces: (i) a high-fidelity robot observation video replacing
human with robot while preserving scene context and temporal alignment, and (ii) a task-
aligned, executable robot action trajectory under feasibility constraints. Experiments
in simulation and on real robots show that EgoEngine enables scalable conversion of
human videos into robot data and, to our knowledge, demonstrates the first zero-shot
visuomotor dexterous policy learning from egocentric human videos without real-robot
demonstrations. Project website: https://egoengine.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12604v1
- Authors: Yangcen Liu, Shuo Cheng, Xinchen Yin, Woo Chul Shin, Alfred Cueva, Yiran Yang, Zhenyang Chen, Chuye Zhang, Danfei Xu
- Published: 2026-06-10T19:01:40Z
- Age days: 3

</details>
