---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03142"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-09-05
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Sensing Which Modality Matters: Evidence-Gated Regularization for Robust VLA Policies

> [!summary] 先说人话（基于摘要）
> EGR 为每帧、每传感器估计任务证据：低证据模态要求扰动前后保持不变，高证据模态则要求单独也能支撑决策。它只改变训练目标，不增加推理开销。

## 这篇到底在做什么

- **卡在哪里**：有限且同质的机器人示范容易让 VLA 学到传感器之间的伪相关，形成 modality entanglement：无关传感器被遮挡也会干扰策略，而真正有用的单一传感器又无法独立支撑动作。
- **关键解法**：EGR 产生状态条件的模态相关性门控，并据此施加两类一致性约束：对低证据传感器训练不变性，对高证据传感器训练单传感器充分性。方法不限定模态，并在视觉多相机和视觉—触觉两类机器人上验证。
- **拿什么证明**：BEHAVIOR-1K 衍生基准含快速诊断套件和47项 rollout 技能。仿真成功率在全模态下由12.5%升至16.4%，无关模态损坏时由9.4%升至16.5%，单模态回退由2.8%升至6.1%；真实物体干扰下，双臂平台由30%升至85%，视觉—触觉平台由55%升至70%。

## 值不值得读

- **和你的研究有什么关系**：对多相机、视觉—触觉 VLA，这提供了零部署开销的抗遮挡和抗干扰训练策略，也提供了专门诊断模态纠缠的评测设计。
- **先别急着信**：绝对仿真成功率仍低；最需核查相关性信号是否依赖额外标注或特定扰动，以及正常场景提升与鲁棒性之间的权衡。
- **判断**：值得精读训练目标和基准协议；真实平台提升显著，但较低的仿真绝对成绩要求谨慎解读。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/Sensing Which Modality Matters Evidence-Gated Regularization for Robust VLA Poli.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03142v1 Announce Type: new Abstract: Vision-Language-Action (VLA) policies fuse multimodal sensory inputs, but training on limited and homogeneous robot demonstrations encourages spurious inter-sensor correlations rather than task-relevant signal, a failure we term modality entanglement. Under real-world occlusions and distractors, this manifests as nuisance sensitivity to corruption of uninformative sensors and single-modality insufficiency when only one informative sensor remains intact. We propose Evidence-Gated Regularization (EGR), a modality-agnostic training objective that introduces zero inference-time overhead. EGR derives a per-frame and per-sensor task-relevance signal to gate two state-conditional consistency objectives: invariance on low-evidence sensors, and single-sensor sufficiency on high-evidence ones. We introduce a benchmark based on BEHAVIOR-1K, comprising a fast inference-only diagnostic suite and 47 rollout-based skills targeting modality entanglement. We validate EGR on this benchmark and on two real-robot setups with fundamentally different embodiments: a bi-manual setup with two Kinova arms and three RGB cameras, and a single-arm MELFA ASSISTA setup combining vision and GelSight tactile sensors. EGR improves simulation success rates (SR) from 12.5% to 16.4% under full modalities (+31%), from 9.4% to 16.5% under uninformative-sensor corruption (+75%), and from 2.8% to 6.1% under single-sensor fallback (+120%). Under physical-object distractors, EGR boosts SR from 30% to 85% on the bi-manual setup (+183%) and from 55% to 70% on the tactile setup (+27%).

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03142
- Authors: Yue Yang, Diego Romeres, Chiori Hori, Gedas Bertasius, Daniel Szafir, Siddarth Jain
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
