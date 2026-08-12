---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09559v1"
published: "2026-06-08T14:33:40Z"
age_days: 1
score: 32
created: 2026-06-10
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Safe-RULE: Safe Reinforcement UnLEarning

> [!summary] 一句话结论（基于摘要）
> In this work, we propose a new learning paradigm, named safe reinforcement unlearning (Safe-RULE), used as a defense framework to remove the influence of poisoned data without retraining from scratch or requiring access to the original training environment.

## 关键点

- **问题**：However, its reliance on static datasets exposes offline Safe RL to data poisoning attacks, where adversaries inject malicious samples that compromise safety and induce unsafe policy behavior.
- **创新点 / 方法**：In this work, we propose a new learning paradigm, named safe reinforcement unlearning (Safe-RULE), used as a defense framework to remove the influence of poisoned data without retraining from scratch or requiring access to the original training environment.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/Safe-RULE Safe Reinforcement UnLEarning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Offline safe reinforcement learning (Safe RL) enables policy learning without online
interactions, making it suitable for safety-critical systems such as robotics systems.
However, its reliance on static datasets exposes offline Safe RL to data poisoning
attacks, where adversaries inject malicious samples that compromise safety and induce
unsafe policy behavior. In this work, we propose a new learning paradigm, named safe
reinforcement unlearning (Safe-RULE), used as a defense framework to remove the
influence of poisoned data without retraining from scratch or requiring access to the
original training environment. We further extend reinforcement unlearning to offline
Safe RL by explicitly accounting for both task performance and safety constraints during
the unlearning process. Experiments across benchmark Safe RL tasks demonstrate that our
approach effectively enhances safety performance against data poisoning attacks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09559v1
- Authors: Shixiong Jiang, Taozheng Zhu, Fanxin Kong
- Published: 2026-06-08T14:33:40Z
- Age days: 1

</details>
