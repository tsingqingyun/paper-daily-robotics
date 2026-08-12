---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08303v1"
published: "2026-08-08T19:31:19Z"
age_days: 3
score: 24
created: 2026-08-12
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Agentic skills improve large language model (LLM) agents by encoding reusable procedures
for complex tasks. However, manually authored skills often adapt poorly to long-horizon
tasks and changing environments. To address the limitation, self-evolving skill systems
have been developed to automatically construct and update skills from execution
trajectories, shifting skill acquisition from external marketplaces to a trusted
evolution pipeline. By replacing external skill acquisition with trusted internal
construction, self-evolving skill systems reduce exposure to skill injection attacks
that rely on direct skill manipulation. However, this skill evolution pipeline may
introduce a new attack surface in which an attacker can indirectly steer skill evolution
by inducing compromised trajectories through agent interactions. To demonstrate the
threat, we propose Trajectory Backdoor Attack (TBA), a query-only attack that steers a
trusted skill-evolution pipeline toward producing a backdoored skill. Specifically, we
craft attacker-submitted queries to lead the agent to perform the target action and
explicitly state the corresponding activation condition in the trajectory. We repeat the
same condition-action pattern across diverse triggered tasks, while leaving clean
queries unchanged, encouraging the evolver to consolidate the pattern as a reusable
trigger-dependent rule into the evolved skill. Experiments on three benchmarks across
two skill-evolution systems using four open- and closed-source backbone models
demonstrate that TBA reliably implants conditional backdoors while preserving clean-task
utility, matching or even surpassing direct skill injection. The results reveal a
critical vulnerability in trajectory-driven skill evolution.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08303v1
- Authors: Yuyang Luo, Haoran Wang, Kai Shu
- Published: 2026-08-08T19:31:19Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
