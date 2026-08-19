---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15917v1"
published: "2026-08-16T20:21:33Z"
age_days: 2
score: 28
created: 2026-08-19
concepts: ["世界模型", "机器人学习"]
---

# Pre-training Visual Dexterity in Simulation

> [!summary] 一句话结论（基于摘要）
> We find that our approach outperforms training behavior cloning policies from scratch, showing that simulation teleoperation is a viable pre-training source for real-world dexterous manipulation.

## 关键点

- **问题**：Dexterous, multi-fingered hands remain comparatively data-starved because real teleoperation is costly to scale, while human hand video is off-embodiment and requires lossy pose estimation and retargeting.
- **创新点 / 方法**：We introduce Simulation Pre-training for Dexterity (SPD), a pre-training framework for dexterous manipulation that uses data entirely collected in simulation.
- **证据**：We find that our approach outperforms training behavior cloning policies from scratch, showing that simulation teleoperation is a viable pre-training source for real-world dexterous manipulation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Pre-training Visual Dexterity in Simulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large-scale pre-training has made robot policy fine-tuning increasingly data-efficient, but this progress has largely been driven by datasets and embodiments built around simple parallel-jaw grippers. Dexterous, multi-fingered hands remain comparatively data-starved because real teleoperation is costly to scale, while human hand video is off-embodiment and requires lossy pose estimation and retargeting. We introduce Simulation Pre-training for Dexterity (SPD), a pre-training framework for dexterous manipulation that uses data entirely collected in simulation. In SPD, humans manipulate virtual objects inside a VR headset, enabling on-embodiment trajectories and robot-free collection. With the help of five operators, we collect 75 hours of multi-task dexterous manipulation over one week, and use it to pre-train a causal transformer on a sequence modeling objective. We study the benefits of simulation pre-training on real-world tasks by fine-tuning on 1-2 hours of physical demonstrations on a 56-DoF bimanual dexterous setup. We find that our approach outperforms training behavior cloning policies from scratch, showing that simulation teleoperation is a viable pre-training source for real-world dexterous manipulation. We perform ablation studies, measuring the benefits of history conditioning and short action chunks for reactive control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15917v1
- Authors: Sarthak Kamat, Adam Rashid, Satvik Sharma, Aseem Doriwala, Chelsea Finn, Phillip Isola, C. Karen Liu
- Published: 2026-08-16T20:21:33Z
- Age days: 2

</details>
