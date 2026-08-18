---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15680v1"
published: "2026-08-16T11:15:55Z"
age_days: 1
score: 43
created: 2026-08-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Robo-Dopamine 2.0: History-Conditioned and OOD-Aware Process Reward Modeling for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> In downstream reinforcement learning, the full model achieves 86.8% mean RoboTwin success and 71/80 successful real-world insertions.

## 关键点

- **问题**：Vision-language-action (VLA) models improve robotic manipulation but remain vulnerable to compounding errors, scene changes, and off-trajectory states.
- **创新点 / 方法**：We introduce Robo-Dopamine 2.0, a history- and OOD-aware process reward model with a pairwise prediction interface.
- **证据**：In downstream reinforcement learning, the full model achieves 86.8% mean RoboTwin success and 71/80 successful real-world insertions.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/Robo-Dopamine 2.0 History-Conditioned and OOD-Aware Process Reward Modeling for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models improve robotic manipulation but remain vulnerable to compounding errors, scene changes, and off-trajectory states. Reinforcement learning can refine pretrained VLA policies, yet sparse success signals hinder exploration, while engineered dense rewards are costly and task-specific. Existing learned visual reward models often rely on static before-after observations, causing temporal ambiguity and weak discrimination between robustness-preserving variations and task-invalid failures under out-of-distribution (OOD) execution. We introduce Robo-Dopamine 2.0, a history- and OOD-aware process reward model with a pairwise prediction interface. It combines (1) history-conditioned pairwise rewards that use source-aligned reference panels for synthetic OOD queries and observed rollout history for online queries, while preserving the queried endpoints, and (2) an OOD-aware signed progress space that represents valid progress, robustness, failure, and recovery. A Signed-Hop Curriculum with transition-aware replay learns coarse execution ordering before fine-grained progress calibration. We also construct an OOD trajectory dataset and a five-family benchmark. Reference panels improve mean visual order consistency (VOC) from 0.967 to 0.986 and OOD-robust VOC from 0.906 to 0.958. With the same 400K pairwise-reward budget, Signed-Hop training with 25% replay reaches 0.9872 mean VOC, compared with 0.9858 for a matched-pool shuffled control. In downstream reinforcement learning, the full model achieves 86.8% mean RoboTwin success and 71/80 successful real-world insertions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15680v1
- Authors: Yijie Xu, Haopeng Jin, Run Zhou, Shengbang Liu, Sixiang Chen, Hongyang Cheng, Sicheng Hu, Peterson Co, Jinwen Luo, Huajie Tan, Shanghang Zhang
- Published: 2026-08-16T11:15:55Z
- Age days: 1

</details>
