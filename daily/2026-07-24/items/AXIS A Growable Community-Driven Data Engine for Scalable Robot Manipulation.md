---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21588v1"
published: "2026-07-23T17:58:08Z"
age_days: 0
score: 38
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> Continual pretraining on AXIS substantially improves the overall success rate of $π_{0.5}$ by 5.8%, outperforms the model pretrained on RoboCasa365 by 37.3%, and exhibits consistent scaling with increasing data volume, with the largest gains observed under la…

## 关键点

- **问题**：Learning effective robot manipulation policies requires diverse, high-quality demonstrations, yet existing data pipelines are often difficult to scale because they rely on specialized hardware, centralized operators, or fixed task suites.
- **创新点 / 方法**：We present AXIS, a growable community-driven data engine and benchmark for scalable robot learning, which enables browser-based teleoperation for large-scale demonstration collection, automatically generates and validates new manipulation tasks, and transforms community- collected demonstrations into training-ready da…
- **证据**：Continual pretraining on AXIS substantially improves the overall success rate of $π_{0.5}$ by 5.8%, outperforms the model pretrained on RoboCasa365 by 37.3%, and exhibits consistent scaling with increasing data volume, with the largest gains observed under layout, sensor-noise, and camera perturbations.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-24/AXIS A Growable Community-Driven Data Engine for Scalable Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning effective robot manipulation policies requires diverse, high-quality
demonstrations, yet existing data pipelines are often difficult to scale because they
rely on specialized hardware, centralized operators, or fixed task suites. We present
AXIS, a growable community-driven data engine and benchmark for scalable robot learning,
which enables browser-based teleoperation for large-scale demonstration collection,
automatically generates and validates new manipulation tasks, and transforms community-
collected demonstrations into training-ready data through automated success checking,
quality filtering, trajectory smoothing, and visual and physics-based augmentation. The
AXIS dataset currently contains 207 diverse tasks and 50K+ trajectories. Meanwhile, AXIS
organizes data into task snapshots and evaluates policies with a systematic held-out
protocol. We compare vision-language-action (VLA) policies under a unified AXIS
evaluation suite and analyze scaling behavior across different data volumes. Continual
pretraining on AXIS substantially improves the overall success rate of $π_{0.5}$ by
5.8%, outperforms the model pretrained on RoboCasa365 by 37.3%, and exhibits consistent
scaling with increasing data volume, with the largest gains observed under layout,
sensor-noise, and camera perturbations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21588v1
- Authors: Mengfei Zhao, Dihong Huang, Yikai Tang, Peihao Li, Mingxuan Yan, Ruiqi Zhuang, Yanjia Huang, Jie Wang, Hai Zhai, Tony Zhou, Rui Zhang, Zhexi Luo, Yuchen Huang, Jianfei Yang, Jiachen Li
- Published: 2026-07-23T17:58:08Z
- Age days: 0

</details>
