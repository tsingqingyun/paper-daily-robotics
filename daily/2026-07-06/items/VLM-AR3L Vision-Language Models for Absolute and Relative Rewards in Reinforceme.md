---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00483v2"
published: "2026-07-01T06:11:59Z"
age_days: 5
score: 28
created: 2026-07-06
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Experimental results show that VLM-AR3L consistently outperforms prior VLM-based reward learning methods.

## 关键点

- **问题**：Designing effective reward functions remains a major challenge in reinforcement learning (RL), particularly in open-ended environments where task goals are abstract and difficult to quantify.
- **创新点 / 方法**：In this work, we present VLM-AR3L, a framework that leverages Vision-Language Models (VLMs) to provide both absolute and relative rewards for RL.
- **证据**：Experimental results show that VLM-AR3L consistently outperforms prior VLM-based reward learning methods.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Designing effective reward functions remains a major challenge in reinforcement learning
(RL), particularly in open-ended environments where task goals are abstract and
difficult to quantify. In this work, we present VLM-AR3L, a framework that leverages
Vision-Language Models (VLMs) to provide both absolute and relative rewards for RL. VLM-
AR3L interprets an agent's visual observations in the context of a natural language task
goal, and learns both absolute and relative rewards from VLM-generated preference
labels. The absolute reward model predicts scalar evaluations for individual states,
while the relative reward model compares consecutive observations to infer progress or
regression toward the task goal. Their integration combines the stability of state-based
evaluation with the robustness of comparative supervision. We evaluate VLM-AR3L across
benchmarks spanning classic control, manipulation, and open-world embodied tasks, with a
particular focus on Minecraft given its visual complexity and long-horizon decision-
making requirements. Experimental results show that VLM-AR3L consistently outperforms
prior VLM-based reward learning methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00483v2
- Authors: Kuan-Chen Chen, Winston Chen, Wei-Fang Sun, Min-Chun Hu
- Published: 2026-07-01T06:11:59Z
- Age days: 5

</details>
