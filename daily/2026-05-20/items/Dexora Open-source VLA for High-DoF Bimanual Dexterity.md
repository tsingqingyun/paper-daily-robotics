---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18722v1"
published: "2026-05-18T17:50:32Z"
age_days: 1
score: 48
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Dexora: Open-source VLA for High-DoF Bimanual Dexterity

> [!summary] 一句话结论（基于摘要）
> Empirically, Dexora outperforms competitive VLA baselines on both basic and dexterous benchmarks (e.g., average dexterous success 66.7% vs.

## 关键点

- **问题**：Vision-Language-Action (VLA) models have recently become a central direction in embodied AI, but current systems are restricted to either dual-gripper control or single-arm dexterous hand manipulation.
- **创新点 / 方法**：In this work, we introduce Dexora, the first open-source VLA system that natively targets dual-arm, dual-hand high-DoF manipulation.
- **证据**：Empirically, Dexora outperforms competitive VLA baselines on both basic and dexterous benchmarks (e.g., average dexterous success 66.7% vs.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：48
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have recently become a central direction in embodied
AI, but current systems are restricted to either dual-gripper control or single-arm
dexterous hand manipulation. While low-dimensional gripper control can often be handled
with simpler methods, high-dimensional dexterous hand control benefits greatly from full
end-to-end VLA learning. In this work, we introduce Dexora, the first open-source VLA
system that natively targets dual-arm, dual-hand high-DoF manipulation. We design a
hybrid teleoperation pipeline that decouples gross arm kinematics (captured with a
custom exoskeleton backpack) from fine finger motion (markerless hand tracking via Apple
Vision Pro), and that drives both a physical dual-arm dual-hand platform and an
identical MuJoCo digital twin. Using that interface, we assemble a large training
corpus: an embodiment-matched synthetic corpus (100K simulated trajectories, 6.5M
frames) and a real-world dataset of 10K teleoperated episodes (2.92M frames). To
mitigate noisy teleoperation demonstrations, we propose a data-quality-aware training
recipe: an offline discriminator provides clip-level weights for diffusion-transformer
policy training, down-weighting low-quality demonstrations. Empirically, Dexora
outperforms competitive VLA baselines on both basic and dexterous benchmarks (e.g.,
average dexterous success 66.7% vs. 51.7%), attains 90% success on basic tasks, and
shows robust out-of-distribution and cross-embodiment generalization. Ablations confirm
the importance of real data and the discriminator for dexterity.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18722v1
- Authors: Zongzheng Zhang, Jingrui Pang, Zhuo Yang, Kun Li, Minwen Liao, Saining Zhang, Guoxuan Chi, Jinbang Guo, Huan-ang Gao, Modi Shi, Dongyun Ge, Yao Mu, Jiayuan Gu, Rui Chen, Hao Dong, Huazhe Xu, Li Yi, Yixin Zhu, Hang Zhao, Pengwei Wang, Shanghang Zhang, Guocai Yao, Jianyu Chen, Hongyang Li, Hao Zhao
- Published: 2026-05-18T17:50:32Z
- Age days: 1

</details>
