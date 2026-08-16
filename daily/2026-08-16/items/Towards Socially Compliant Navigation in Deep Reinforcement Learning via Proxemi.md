---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12917v1"
published: "2026-08-13T07:59:23Z"
age_days: 3
score: 23
created: 2026-08-16
concepts: ["世界模型", "机器人学习"]
---

# Towards Socially Compliant Navigation in Deep Reinforcement Learning via Proxemics-Based Reward Modeling

> [!summary] 一句话结论（基于摘要）
> Results show that the proposed reward consistently improves social metrics in simulation while maintaining competitive navigation performance relative to the compared reward models.

## 关键点

- **问题**：Developing effective robot navigation methods in crowded environments is essential for real-world applications.
- **创新点 / 方法**：In this paper, we introduce a novel proxemics-based reward formulation for DRL social navigation that provides a dense, interpretable social learning signal while maintaining navigation efficiency.
- **证据**：Results show that the proposed reward consistently improves social metrics in simulation while maintaining competitive navigation performance relative to the compared reward models.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Towards Socially Compliant Navigation in Deep Reinforcement Learning via Proxemi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Developing effective robot navigation methods in crowded environments is essential for real-world applications. Although recent deep reinforcement learning (DRL) methods have improved navigation performance in crowded environments, they often focus primarily on task-centric objectives and underrepresent social compliance objectives. In this paper, we introduce a novel proxemics-based reward formulation for DRL social navigation that provides a dense, interpretable social learning signal while maintaining navigation efficiency. Our approach models each human's personal space as a radial Gaussian-mixture field derived from Hall's proxemics theory and computes a robot-centric local cost over the robot's field of view. We integrate the proposed reward into established DRL navigation methods and evaluate it in simulation across multiple crowd scenarios, reward baselines, and crowd densities using both navigation metrics and social metrics. Results show that the proposed reward consistently improves social metrics in simulation while maintaining competitive navigation performance relative to the compared reward models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12917v1
- Authors: Takieddine Soualhi, Jacques Saraydaryan, Laetitia Matignon
- Published: 2026-08-13T07:59:23Z
- Age days: 3

</details>
