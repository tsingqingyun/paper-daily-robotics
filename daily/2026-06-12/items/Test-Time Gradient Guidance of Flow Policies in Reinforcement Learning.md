---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11087v1"
published: "2026-06-09T16:45:57Z"
age_days: 2
score: 31
created: 2026-06-12
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Empirically, QGF outperforms prior test-time RL methods on single-task and goal-conditioned offline RL benchmarks with high-dimensional action spaces, and is competitive with state-of-the-art training-time algorithms while being much cheaper to run.

## 关键点

- **问题**：While they are known to scale stably in the supervised imitation learning setting, incorporating them into reinforcement learning (RL) pipelines for policy improvement has proven more difficult.
- **创新点 / 方法**：To this end, we propose QGF (Q-Guided Flow), an RL algorithm that performs policy optimization entirely at test time.
- **证据**：Empirically, QGF outperforms prior test-time RL methods on single-task and goal-conditioned offline RL benchmarks with high-dimensional action spaces, and is competitive with state-of-the-art training-time algorithms while being much cheaper to run.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Expressive continuous control policies, such as diffusion and flow models, form the
backbone of recent advances in scaling imitation learning for simulated and real robot
control. While they are known to scale stably in the supervised imitation learning
setting, incorporating them into reinforcement learning (RL) pipelines for policy
improvement has proven more difficult. It often requires specialized training objectives
or backpropagating through denoising processes, which cause well-known issues with
stability and affect scalability. In this paper we study the question of whether simple
policy improvement schemes at test time alone, leaving stable supervised policy training
intact, can be a competitive alternative which sidesteps these issues. To this end, we
propose QGF (Q-Guided Flow), an RL algorithm that performs policy optimization entirely
at test time. QGF works by pre-training both a reference flow policy (via a standard
behavioral cloning objective) and a value function critic and, at test time, using the
value gradient to guide the reference policy to generate higher-value actions without
any additional policy learning. Empirically, QGF outperforms prior test-time RL methods
on single-task and goal-conditioned offline RL benchmarks with high-dimensional action
spaces, and is competitive with state-of-the-art training-time algorithms while being
much cheaper to run. Moreover, it exhibits favorable scaling with model size by avoiding
the instability of actor-critic training, offering a practical and effective alternative
RL algorithm with expressive policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11087v1
- Authors: Zhiyuan Zhou, Andy Peng, Charles Xu, Qiyang Li, Tobias Springenberg, Kevin Frans, Sergey Levine
- Published: 2026-06-09T16:45:57Z
- Age days: 2

</details>
