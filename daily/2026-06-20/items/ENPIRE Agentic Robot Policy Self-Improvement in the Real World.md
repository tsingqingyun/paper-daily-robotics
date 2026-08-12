---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19980v1"
published: "2026-06-18T09:21:27Z"
age_days: 1
score: 33
created: 2026-06-20
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

> [!summary] 一句话结论（基于摘要）
> Powered by ENPIRE, frontier coding agents can autonomously train a policy to achieve a 99% success rate on challenging, dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and tool use, a process that further accelerates when we d…

## 关键点

- **问题**：Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence.
- **创新点 / 方法**：To bridge this gap, we introduce ENPIRE, a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate pol…
- **证据**：Powered by ENPIRE, frontier coding agents can autonomously train a policy to achieve a 99% success rate on challenging, dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and tool use, a process that further accelerates when we dispatch an agent team on a robot fleet.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/ENPIRE Agentic Robot Policy Self-Improvement in the Real World.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Achieving dexterous robotic manipulation in the real world heavily relies on human
supervision and algorithm engineering, which becomes a central bottleneck in the pursuit
of general physical intelligence. Although emerging coding agents can generate code to
automate algorithm search, their successes remain largely confined in digital
environments. We conjecture that the missing abstraction to automate robotics research
is a repeatable feedback loop for real-world policy improvement: reset the scene,
execute a policy, verify the outcome, and refine the next iteration. To bridge this gap,
we introduce ENPIRE, a harness framework for coding agents that instantiates this
physical feedback routine with four core modules: an Environment module (EN) for
automatic reset and verification, a Policy Improvement module (PI) that launches policy
refinement, a Rollout module (R) to evaluate policies with one or multiple physical
robots operating in parallel, and an Evolution module (E) in which coding agents analyze
logs, consult literature, improve training infrastructure and algorithm code to address
failure modes. This closed-loop system transforms real-world manipulation learning into
a controllable optimization procedure, minimizing human effort while allowing fair
ablations across training recipe and agent variants. Powered by ENPIRE, frontier coding
agents can autonomously train a policy to achieve a 99% success rate on challenging,
dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and
tool use, a process that further accelerates when we dispatch an agent team on a robot
fleet. Our results suggest a practical and scalable path toward deploying coding agents
to autonomously advancing robotics in the physical world.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19980v1
- Authors: Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi
- Published: 2026-06-18T09:21:27Z
- Age days: 1

</details>
