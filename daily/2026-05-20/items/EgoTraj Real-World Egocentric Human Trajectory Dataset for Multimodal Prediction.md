---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19004v1"
published: "2026-05-18T18:26:51Z"
age_days: 1
score: 38
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# EgoTraj: Real-World Egocentric Human Trajectory Dataset for Multimodal Prediction

> [!summary] 一句话结论（基于摘要）
> Addressing this need, we introduce EgoTraj, an egocentric multimodal open dataset recorded using Meta Quest Pro (MQPro).

## 关键点

- **问题**：However, progress in this direction remains limited due to the scarcity of egocentric trajectory datasets collected in real-world environments.
- **创新点 / 方法**：Addressing this need, we introduce EgoTraj, an egocentric multimodal open dataset recorded using Meta Quest Pro (MQPro).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-20/EgoTraj Real-World Egocentric Human Trajectory Dataset for Multimodal Prediction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Accurately forecasting human trajectories from an egocentric perspective plays a central
role in applications such as humanoid robotics, wearable sensing systems, and assistive
navigation. However, progress in this direction remains limited due to the scarcity of
egocentric trajectory datasets collected in real-world environments. Addressing this
need, we introduce EgoTraj, an egocentric multimodal open dataset recorded using Meta
Quest Pro (MQPro). EgoTraj contains 75 sequences of human navigation collected from
multiple MQPro wearers in real-world urban environments. Each recording provides
synchronized RGB video along with ground-truth data, including continuous time-
synchronized 6-degree-of-freedom head poses, per-frame 3D eye gaze vectors, scene
annotations. To the best of our knowledge, EgoTraj differs from typical egocentric
trajectory datasets by capturing long-horizon, self-directed navigation across diverse
urban routes with broad participant diversity. To demonstrate the potential of the
dataset, we benchmark several state-of-the-art methods for egocentric trajectory
prediction and conduct ablation studies to analyze the contributions of gaze, scene, and
motion cues. The results highlight the utility of EgoTraj for AR-based perception,
navigation, and assistive systems. The EgoTraj dataset, code, and EgoViz Dashboard are
publicly available at https://github.com/yehiahmad/EgoTraj.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19004v1
- Authors: Ahmad Yehia, Abduallah Mohamed, Tianyi Wang, Jiseop Byeon, Kun Qian, Junfeng Jiao, Christian Claudel
- Published: 2026-05-18T18:26:51Z
- Age days: 1

</details>
