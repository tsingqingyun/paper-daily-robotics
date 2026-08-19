---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17423v1"
published: "2026-08-18T06:44:16Z"
age_days: 0
score: 35
created: 2026-08-19
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups

> [!summary] 一句话结论（基于摘要）
> Across four RoboTwin tasks spanning different horizons and coordination patterns, Prism-GRPO improves success and quality at matched rollout budgets and reaches target success rates with up to 56% fewer rollouts.

## 关键点

- **问题**：By splitting same-outcome groups into a quality spectrum, Prism-GRPO recovers training signal while ensuring that every success still outranks every failure.
- **创新点 / 方法**：We introduce Prism-GRPO, which augments binary outcome reward with a weighted trajectory-level execution-quality score.
- **证据**：Across four RoboTwin tasks spanning different horizons and coordination patterns, Prism-GRPO improves success and quality at matched rollout budgets and reaches target success rates with up to 56% fewer rollouts.
- **局限**：GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a critic.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Prism-GRPO Faster VLA Policy Optimization via Splitting Same-outcome Groups.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a critic. This simplification comes with a sampling cost: group-relative advantages require multiple rollouts from each scene. Under binary success rewards, groups whose rollouts all succeed or all fail have zero advantage and are discarded by dynamic sampling. These groups are especially common early in training, when most rollouts fail, wasting much of the expensive robotic rollout budget. We introduce Prism-GRPO, which augments binary outcome reward with a weighted trajectory-level execution-quality score. By splitting same-outcome groups into a quality spectrum, Prism-GRPO recovers training signal while ensuring that every success still outranks every failure. Quality scores can be derived from simulator contacts, executed actions, or visual observations, avoiding task-specific progress rewards. We prove that Prism-GRPO never increases the probability that a sampled group is discarded for having zero advantages, and derive a gradient-alignment condition under which its combined update remains a local ascent direction for task success. Across four RoboTwin tasks spanning different horizons and coordination patterns, Prism-GRPO improves success and quality at matched rollout budgets and reaches target success rates with up to 56% fewer rollouts. It also suppresses a reward-hacking shortcut, with the cleaner behavior transferring under direct deployment to a real robot. Through ablations, we show consistent gains across contact-, smoothness-, and VLM-derived quality signals.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17423v1
- Authors: Zeyun Deng, Yuzhe Lu, Yawei Wang, Linbo Liu, Qing Ping, Han Ding, Guande Wu, Panpan Xu, Jun Huan
- Published: 2026-08-18T06:44:16Z
- Age days: 0

</details>
