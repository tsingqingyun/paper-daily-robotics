---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29867v1"
published: "2026-06-29T07:03:45Z"
age_days: 1
score: 32
created: 2026-06-30
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RoAd-RL: A Unified Library and Benchmark for Robust Adversarial Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Results reveal substantial variations in robustness across environments and show that some commonly used defenses can be more detrimental than the attacks they aim to mitigate, while temporal smoothing consistently achieves strong performance.

## 关键点

- **问题**：Deep Reinforcement Learning (DRL) has achieved significant success in robotics and autonomous systems, yet remains vulnerable to adversarial perturbations that can severely degrade performance.
- **创新点 / 方法**：To address these challenges, we present \textbf{RoAd-RL}, an open- source benchmarking framework that provides unified abstractions for policies, attacks, defenses, and robustness metrics, together with reproducible evaluation pipelines and seamless integration with Stable-Baselines3 and Gymnasium.
- **证据**：Results reveal substantial variations in robustness across environments and show that some commonly used defenses can be more detrimental than the attacks they aim to mitigate, while temporal smoothing consistently achieves strong performance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Deep Reinforcement Learning (DRL) has achieved significant success in robotics and
autonomous systems, yet remains vulnerable to adversarial perturbations that can
severely degrade performance. Research in adversarial reinforcement learning is often
limited by fragmented implementations, inconsistent evaluation protocols, and poor
reproducibility. To address these challenges, we present \textbf{RoAd-RL}, an open-
source benchmarking framework that provides unified abstractions for policies, attacks,
defenses, and robustness metrics, together with reproducible evaluation pipelines and
seamless integration with Stable-Baselines3 and Gymnasium. We evaluate DQN, PPO, and SAC
agents in LunarLander and Highway-v0 under 192 attack-defense configurations. Results
reveal substantial variations in robustness across environments and show that some
commonly used defenses can be more detrimental than the attacks they aim to mitigate,
while temporal smoothing consistently achieves strong performance. RoAd-RL establishes a
standardized benchmark for adversarial reinforcement learning research and is publicly
available at https://pypi.org/project/road-rl.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29867v1
- Authors: Adithya Mohan, Daniel Kriegl, Torsten Schön
- Published: 2026-06-29T07:03:45Z
- Age days: 1

</details>
