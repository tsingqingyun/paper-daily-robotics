---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17027v1"
published: "2026-08-17T18:24:41Z"
age_days: 1
score: 34
created: 2026-08-19
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences

> [!summary] 一句话结论（基于摘要）
> Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research.

## 关键点

- **问题**：However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation, and even more so for humanoids that must also walk and balance.
- **创新点 / 方法**：Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Reinforcement learning breaks through it, and refining the cloned policy with Flow-GRPO on a single sparse reward yields performance that synthetic behavior cloning cannot match.

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/FetchMan Learning Visual Humanoid Loco-Manipulation Policies from Simulated Expe.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation, and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring that behavior to the real world, as is commonly done in locomotion, sidesteps this struggle, so we replicate that recipe for loco-manipulation. In doing so, we find that cloning synthetic demonstrations results in a low performance ceiling no matter the amount of training data. Reinforcement learning breaks through it, and refining the cloned policy with Flow-GRPO on a single sparse reward yields performance that synthetic behavior cloning cannot match. Together, these stages form our end-to-end sim-to-real pipeline spanning more than 150,000 scenes, which we use to train FetchMan. We evaluate it on FetchMan-Bench, a simulation benchmark we release, and deploy it zero-shot on a real Unitree G1, where our single-object reach-and-pick policy walks to and grasps a target across unseen scenes at 73.3% success. Finally, we extend this recipe to multi-object training, a first step toward loco-manipulation generalist policies at this data scale.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17027v1
- Authors: Omar Rayyan, Zhi Li, Max Argus, Yuxin Jiang, Chang Yu, Chenfanfu Jiang, Yuchen Cui
- Published: 2026-08-17T18:24:41Z
- Age days: 1

</details>
