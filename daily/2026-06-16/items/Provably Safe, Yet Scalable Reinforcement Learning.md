---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14536v1"
published: "2026-06-12T15:13:51Z"
age_days: 3
score: 22
created: 2026-06-16
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Provably Safe, Yet Scalable Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> In this paper, we present the Provably Safe, yet Scalable RL (PS2-RL) framework, a novel two-phase architecture for learning provably safe policies in a scalable manner, designed to overcome the key bottlenecks of prior methods.

## 关键点

- **问题**：We establish theoretical guarantees for the proposed framework and evaluate it on robotic control tasks with state dimensions up to 10, a regime in which prior provably safe RL methods struggle or become impractical.
- **创新点 / 方法**：In this paper, we present the Provably Safe, yet Scalable RL (PS2-RL) framework, a novel two-phase architecture for learning provably safe policies in a scalable manner, designed to overcome the key bottlenecks of prior methods.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Predominant approaches rely on soft-constrained policy optimization, which has achieved empirical success but does not provide formal safety guarantees for the learned policy.

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safe reinforcement learning (RL) aims to learn policies that optimize rewards while
satisfying constraints. Predominant approaches rely on soft-constrained policy
optimization, which has achieved empirical success but does not provide formal safety
guarantees for the learned policy. In contrast, methods with strict guarantees typically
rely on explicit certificate functions, whose construction requires the direct synthesis
and verification of control-invariant sets, a process that scales poorly with state
dimension and often yields overly conservative behavior. In this paper, we present the
Provably Safe, yet Scalable RL (PS2-RL) framework, a novel two-phase architecture for
learning provably safe policies in a scalable manner, designed to overcome the key
bottlenecks of prior methods. Rather than explicitly computing invariant sets, PS2-RL
leverages a learned backup policy to forward-integrate the system dynamics, generating
an implicit control-invariant set online. In the first phase, the backup policy is
trained with our proposed safe-arrival value function, which characterizes the optimal
backup policy for invariant-set construction. In the second phase, an RL policy is
trained end-to-end through a differentiable projection layer that strictly enforces the
safety guarantees induced by the learned backup policy. By maximizing the volume of the
implicit control-invariant set in the first phase, the resulting PS2 policy from the
second phase is performant and scalable, while maintaining provable safety. Crucially,
PS2-RL imposes no restrictions on the underlying RL algorithm and can be plugged into
any existing training pipeline. We establish theoretical guarantees for the proposed
framework and evaluate it on robotic control tasks with state dimensions up to 10, a
regime in which prior provably safe RL methods struggle or become impractical.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14536v1
- Authors: Kai S. Yun, Zeyang Li, Navid Azizan
- Published: 2026-06-12T15:13:51Z
- Age days: 3

</details>
