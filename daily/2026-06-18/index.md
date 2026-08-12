---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-18
---

# 2026-06-18 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Geometric Action Model for Robot Policy Learning](items/Geometric%20Action%20Model%20for%20Robot%20Policy%20Learning.md) — We propose the Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action decoding.

- **规模**：2069 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 18、具身智能评测与基准 16、智能体 Agent 12、机器人学习 12、视觉语言动作模型 VLA 12、世界模型 11、AI 核心知识地图 1、Sim2Real 1
- **源异常**：1

## 必读 5 篇

### 1. [Geometric Action Model for Robot Policy Learning](items/Geometric%20Action%20Model%20for%20Robot%20Policy%20Learning.md)

- **创新点 / 方法**：We propose the Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action decoding.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](items/Qwen-RobotManip%20Technical%20Report%20Alignment%20Unlocks%20Scale%20for%20Robotic%20Manipulatio.md)

- **创新点 / 方法**：We present Qwen- RobotManip, a generalizable Vision-Language-Action foundation model built on Qwen-VL.
- **证据**：Qwen-RobotManip substantially outperforms prior state-of-the-art models, including $π$0.5, across all OOD settings, ranks 1st in RoboChallenge with a 20% relative improvement, and is validated on real- robot platforms including AgileX ALOHA, Franka, UR, and ARX.

### 3. [MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation](items/MuseVLA%20An%20Adaptive%20Multimodal%20Sensing%20Vision-Language-Action%20Model%20for%20Robotic.md)

- **创新点 / 方法**：We present MuseVLA, an adaptive multimodal sensing VLA model that integrates novel sensors as on-demand tools for robotic manipulation.
- **证据**：MuseVLA achieves 80.6% success rate on average, outperforming RGB-only and multisensory VLA baselines significantly, and exhibits strong zero-shot capabilities on unseen tasks.

### 4. [WireCraft: A Simulation Benchmark for Industrial DLO Manipulation](items/WireCraft%20A%20Simulation%20Benchmark%20for%20Industrial%20DLO%20Manipulation.md)

- **创新点 / 方法**：To bridge this gap, we introduce WireCraft, a simulation benchmark for industrial DLO manipulation with configurable difficulty and assets, spanning three task families: connector insertion, clip routing, and channel seating.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [Uncertainty Quantification for Flow-Based Vision-Language-Action Models](items/Uncertainty%20Quantification%20for%20Flow-Based%20Vision-Language-Action%20Models.md)

- **创新点 / 方法**：To this end, we propose SAVE, a framework for uncertainty- guided active multitask fine-tuning that reduces the number of costly expert demonstrations required to adapt VLAs to new tasks.
- **证据**：Through extensive experiments on the LIBERO benchmark, we demonstrate that VFD yields better-calibrated uncertainty estimates predictive of downstream performance, that VFD achieves strong performance in detecting failures, and that uncertainty-guided data acquisition with SAVE requires at least 22% fewer samples than…

## 扫读 7 篇

- [ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning](items/ROVE%20Unlocking%20Human%20Interventions%20for%20Humanoid%20Manipulation%20via%20Reinforcement%20L.md) — On challenging real-world contact-rich and fine- grained humanoid manipulation tasks, ROVE outperforms experience-learning baselines and consistently improves across multiple rollout-intervention iterations.
- [ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining](items/ACE-Ego-0%20Unifying%20Egocentric%20Human%20and%20Robotic%20Data%20for%20VLA%20Pretraining.md) — ACE-EGO-0 achieves state-of-the- art performance on RoboCasa GR1 TableTop and RoboTwin 2.0, while demonstrating strong transfer to real-world bimanual manipulation.
- [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](items/Qwen-RobotWorld%20Technical%20Report%20Unifying%20Embodied%20World%20Modeling%20through%20Langua.md) — Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open- source models on WorldModelBench and PBench.
- [ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation](items/ThinkingVLA%20Interleaved%20Vision%20and%20Language%20Reasoning%20for%20Robotic%20Manipulation.md) — Extensive experiments on simulation and real-world benchmarks demonstrate that ThinkingVLA consistently outperforms state-of-the-art baselines, with particularly large gains on long-horizon manipulation tasks.
- [Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning](items/Video-Based%20Optimal%20Transport%20for%20Feedback-Efficient%20Offline%20Preference-Based%20Re.md) — Extensive experiments across locomotion and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms state-of-the-art offline PbRL methods under limited feedback budgets.
- [EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning](items/EgoInfinity%20A%20Web-Scale%204D%20Hand-Object%20Interaction%20Data%20Engine%20for%20Any-View%20Robo.md) — Instead of proposing a static dataset, we introduce EgoInfinity, a universal 4D hand-object interaction data engine that enables web-scale data generation for robot retargeting and learning.
- [Kairos: A Native World Model Stack for Physical AI](items/Kairos%20A%20Native%20World%20Model%20Stack%20for%20Physical%20AI.md) — Experiments on embodied world-model, long-horizon, and action-policy benchmarks show that Kairos achieves top level performance while offering a strong efficiency-capability trade-off.

## 其余存档 12 篇

- [PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space](items/PearlVLA%20Progressive%20Embodied%20Action-Plan%20Refinement%20in%20Latent%20Space.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [T-Rex: Tactile-Reactive Dexterous Manipulation](items/T-Rex%20Tactile-Reactive%20Dexterous%20Manipulation.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [EgoCS-400K: An Egocentric Gameplay Dataset for World Models](items/EgoCS-400K%20An%20Egocentric%20Gameplay%20Dataset%20for%20World%20Models.md) · [[智能体 Agent]] [[世界模型]]
- [VENOM: Versatile Embodied Network for Omni-bodied Motion tracking](items/VENOM%20Versatile%20Embodied%20Network%20for%20Omni-bodied%20Motion%20tracking.md) · [[多模态基础模型]] [[世界模型]] [[机器人学习]]
- [Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So](items/Memory%20as%20a%20Wasting%20Asset%20Pricing%20Flash%20Endurance%20for%20Embodied%20Agents%2C%20and%20the%20L.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments](items/GASE%20Gaussian%20Splatting-Based%20Automated%20System%20for%20Reconstructing%20Embodied-Simul.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]]
- [GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning](items/GeneralVLA-2%20Geometry-Aware%20Reconstruction%20and%20Governed%20Memory%20for%20Robot%20Plannin.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- [Contrastive Action-Image Pre-training for Visuomotor Control](items/Contrastive%20Action-Image%20Pre-training%20for%20Visuomotor%20Control.md) · [[AI 核心知识地图]]
- [WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation](items/WeaveLA%20Event%20Driven%20Cross-Subtask%20Latent%20Memory%20Weaving%20for%20Repetitive%20Robot%20Ma.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [SoK: Security and Privacy of Foundation-Model-Powered Robots](items/SoK%20Security%20and%20Privacy%20of%20Foundation-Model-Powered%20Robots.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI](items/ERQA-Plus%20A%20Diagnostic%20Benchmark%20for%20Reasoning%20in%20Embodied%20AI.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [MagicSim: A Unified Infrastructure for Executable Embodied Interaction](items/MagicSim%20A%20Unified%20Infrastructure%20for%20Executable%20Embodied%20Interaction.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2069
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Geometric Action Model for Robot Policy Learning
- 最高分论文发布时间：2026-06-15T17:58:03Z
- 主要技术对象分类：多模态基础模型 18、具身智能评测与基准 16、智能体 Agent 12、机器人学习 12、视觉语言动作模型 VLA 12、世界模型 11、AI 核心知识地图 1、Sim2Real 1
- 信息源错误：1

### 信息源错误

- Berkeley BAIR Blog: The read operation timed out

</details>
