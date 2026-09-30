---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03142v1"
published: "2026-09-02T20:25:21Z"
age_days: 4
score: 35
created: 2026-09-07
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Sensing Which Modality Matters: Evidence-Gated Regularization for Robust VLA Policies

> [!summary] 先说人话（基于摘要）
> EGR 按帧、按传感器估计任务相关证据：低证据模态应对扰动保持不变，高证据单模态则被训练成足以完成任务，从而缓解VLA的 modality entanglement，且推理零额外开销。

## 这篇到底在做什么

- **卡在哪里**：有限且同质的机器人示范会让多模态策略学到传感器间的伪相关；结果是无关传感器被污染时策略过敏，而只剩一个真正有用传感器时又无法工作。
- **关键解法**：EGR生成状态条件的模态相关性门控信号，并控制两项一致性目标：对低证据传感器施加不变性，对高证据传感器施加单传感器充分性。它是模态无关的训练目标，不改变推理路径。
- **拿什么证明**：BEHAVIOR-1K衍生基准含快速诊断套件和47个滚动技能。仿真成功率在全模态下由12.5%升至16.4%，无关传感器污染下由9.4%升至16.5%，单传感器回退由2.8%升至6.1%。真实物体干扰下，双臂系统由30%升至85%，视觉触觉单臂系统由55%升至70%。

## 值不值得读

- **和你的研究有什么关系**：它给多摄像头、视觉—触觉VLA提供了无需增加部署延迟的鲁棒训练办法，同时附带专门暴露模态纠缠的评测设计。
- **先别急着信**：绝对仿真成功率仍较低；需核查证据信号如何获得、是否依赖任务标签，以及门控错误时会不会压制互补模态。
- **判断**：值得精读目标函数、证据估计和真实实验；问题定义清楚，跨两种本体的提升也有实际说服力。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Sensing Which Modality Matters Evidence-Gated Regularization for Robust VLA Poli.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies fuse multimodal sensory inputs, but training on limited and homogeneous robot demonstrations encourages spurious inter-sensor correlations rather than task-relevant signal, a failure we term modality entanglement. Under real-world occlusions and distractors, this manifests as nuisance sensitivity to corruption of uninformative sensors and single-modality insufficiency when only one informative sensor remains intact. We propose Evidence-Gated Regularization (EGR), a modality-agnostic training objective that introduces zero inference-time overhead. EGR derives a per-frame and per-sensor task-relevance signal to gate two state-conditional consistency objectives: invariance on low-evidence sensors, and single-sensor sufficiency on high-evidence ones. We introduce a benchmark based on BEHAVIOR-1K, comprising a fast inference-only diagnostic suite and 47 rollout-based skills targeting modality entanglement. We validate EGR on this benchmark and on two real-robot setups with fundamentally different embodiments: a bi-manual setup with two Kinova arms and three RGB cameras, and a single-arm MELFA ASSISTA setup combining vision and GelSight tactile sensors. EGR improves simulation success rates (SR) from 12.5% to 16.4% under full modalities (+31%), from 9.4% to 16.5% under uninformative-sensor corruption (+75%), and from 2.8% to 6.1% under single-sensor fallback (+120%). Under physical-object distractors, EGR boosts SR from 30% to 85% on the bi-manual setup (+183%) and from 55% to 70% on the tactile setup (+27%).

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03142v1
- Authors: Yue Yang, Diego Romeres, Chiori Hori, Gedas Bertasius, Daniel Szafir, Siddarth Jain
- Published: 2026-09-02T20:25:21Z
- Age days: 4

</details>
