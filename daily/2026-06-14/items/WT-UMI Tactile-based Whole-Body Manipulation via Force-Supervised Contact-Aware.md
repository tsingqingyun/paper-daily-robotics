---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13232v1"
published: "2026-06-11T11:45:58Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning

> [!summary] 一句话结论（基于摘要）
> Across five contact-rich tasks spanning deformable objects, bulky rigid objects, and human--humanoid collaboration, WT-UMI improves success rate and reduces contact-position tracking error over four policy baselines.

## 关键点

- **问题**：Whole-body humanoid manipulation of bulky, deformable, and shared-load objects requires distributed contact sensing and explicit force regulation, yet most imitation policies treat contact force only implicitly.
- **创新点 / 方法**：We introduce a force-conditioned target-pose correction module that converts measured human poses into contact-aware robot targets by learning corrections from teleoperation data.
- **证据**：Across five contact-rich tasks spanning deformable objects, bulky rigid objects, and human--humanoid collaboration, WT-UMI improves success rate and reduces contact-position tracking error over four policy baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Whole-body humanoid manipulation of bulky, deformable, and shared-load objects requires
distributed contact sensing and explicit force regulation, yet most imitation policies
treat contact force only implicitly. On the other hand, different demonstration sources
provide complementary modalities with inherent trade-offs: human demonstrations capture
natural contact forces but not robot-executable actions, while teleoperation directly
records robot actions but with less natural force regulation. This paper presents
\textbf{WT-UMI}, a wearable whole-body tactile interface worn by human operators or
mounted on humanoids, providing accurate observations of tactile images, contact forces,
and end-effector poses across both human demonstration and humanoid teleoperation modes.
We introduce a force-conditioned target-pose correction module that converts measured
human poses into contact-aware robot targets by learning corrections from teleoperation
data. To leverage the natural force interaction in human data, we propose a force-
supervised planner that predicts end-effector pose chunks and contact-force
trajectories. The predicted contact force serves as the reference for a tactile-based
admittance controller. Across five contact-rich tasks spanning deformable objects, bulky
rigid objects, and human--humanoid collaboration, WT-UMI improves success rate and
reduces contact-position tracking error over four policy baselines. Our project page is
available at https://wt-umi.github.io/WTUMI/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13232v1
- Authors: Jaehwi Jang, Zhaoyuan Gu, Alfred Cueva, Zimeng Chai, Junjie Sheng, Thong Nguyen, Himank Galundia, Yifan Wu, Huishu Xue, Isaac Legene, Ojas Mediratta, Davin Doan, Andrew Collins, Sarah Sadegh, KyoungMok Kim, Rishita Dhalbisoi, Zun Chen, Ye Zhao
- Published: 2026-06-11T11:45:58Z
- Age days: 2

</details>
