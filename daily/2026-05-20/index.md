---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-05-20
---

# 2026-05-20 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Dexora: Open-source VLA for High-DoF Bimanual Dexterity](items/Dexora%20Open-source%20VLA%20for%20High-DoF%20Bimanual%20Dexterity.md) — Empirically, Dexora outperforms competitive VLA baselines on both basic and dexterous benchmarks (e.g., average dexterous success 66.7% vs.

- **规模**：2019 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 19、多模态基础模型 18、智能体 Agent 15、世界模型 11、机器人学习 7、视觉语言动作模型 VLA 6、Sim2Real 2
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Dexora: Open-source VLA for High-DoF Bimanual Dexterity](items/Dexora%20Open-source%20VLA%20for%20High-DoF%20Bimanual%20Dexterity.md)

- **创新点 / 方法**：In this work, we introduce Dexora, the first open-source VLA system that natively targets dual-arm, dual-hand high-DoF manipulation.
- **证据**：Empirically, Dexora outperforms competitive VLA baselines on both basic and dexterous benchmarks (e.g., average dexterous success 66.7% vs.

### 2. [RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models](items/RoVLA%20Multi-Consistency%20Constraints%20for%20Robust%20Vision-Language-Action%20Models.md)

- **创新点 / 方法**：To address this issue, we propose RoVLA, a robust vision-language-action framework with multi-consistency constraints.
- **证据**：Experiments on LIBERO-Plus, RoboTwin 2.0, and real-world manipulation tasks show that RoVLA consistently outperforms strong baseline methods and exhibits superior robustness under diverse task and observation shifts.

### 3. [RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents](items/RoboJailBench%20Benchmarking%20Adversarial%20Attacks%20and%20Defenses%20in%20Embodied%20Robotic.md)

- **创新点 / 方法**：We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [EgoTraj: Real-World Egocentric Human Trajectory Dataset for Multimodal Prediction](items/EgoTraj%20Real-World%20Egocentric%20Human%20Trajectory%20Dataset%20for%20Multimodal%20Prediction.md)

- **创新点 / 方法**：Addressing this need, we introduce EgoTraj, an egocentric multimodal open dataset recorded using Meta Quest Pro (MQPro).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [Not What You Asked For: Typographic Attacks in Household Robot Manipulation](items/Not%20What%20You%20Asked%20For%20Typographic%20Attacks%20in%20Household%20Robot%20Manipulation.md)

- **创新点 / 方法**：We introduce a decoupled perception architecture that exposes a frozen CLIP encoder to adversarial stickers while maintaining geometric grounding via DETIC.
- **证据**：In a controlled evaluation pool of 59 attributable episodes, the attack achieves an overall Attack Success Rate (ASR) of 67.8%, rising to 70.0% among fully successful episodes, under uncontrolled viewing angles and occlusion with no perceptual optimization.

## 扫读 7 篇

- [PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models](items/PAPO-VLA%20Planning-Aware%20Policy%20Optimization%20for%20Vision-Language-Action%20Models.md) — To address this issue, we propose Planning-Aware Policy Optimization for VLA models (PAPO-VLA).
- [Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction](items/Robo-Cortex%20A%20Self-Evolving%20Embodied%20Agent%20via%20Dual-Grain%20Cognitive%20Memory%20and%20A.md) — Extensive evaluations on IGNav, AR, and AEQA show that Robo-Cortex consistently outperforms strong baselines in both task success and exploration efficiency, with gains of up to +4.16% SPL over the strongest prior method and up to +15.30% SPL under heuristic…
- [ManiSoft: Towards Vision-Language Manipulation for Soft Continuum Robotics](items/ManiSoft%20Towards%20Vision-Language%20Manipulation%20for%20Soft%20Continuum%20Robotics.md) — To investigate these challenges, we introduce \ManiSoft, a benchmark for vision-language manipulation with soft arms.
- [Seeing Together: Multi-Robot Cooperative Egocentric Spatial Reasoning with Multimodal Large Language Models](items/Seeing%20Together%20Multi-Robot%20Cooperative%20Egocentric%20Spatial%20Reasoning%20with%20Multim.md) — Across 22 MLLM baselines, SP-CoR consistently improves cooperative reasoning, outperforming the strongest fine-tuned baseline by +3.87% on Habitat and +7.12% on iGibson.
- [ARC-RL: A Reinforcement Learning Playground Inspired by ARC Raiders](items/ARC-RL%20A%20Reinforcement%20Learning%20Playground%20Inspired%20by%20ARC%20Raiders.md) — We introduce ARC-RL, a suite of four MuJoCo continuous-control environments featuring robotic morphologies inspired by the bestiary of ARC Raiders: the 18-DoF tall hexapod Queen, the 12-DoF armoured hexapod Bastion, the 18-DoF compact hexapod Tick, and the 12…
- [Key-Gram: Extensible World Knowledge for Embodied Manipulation](items/Key-Gram%20Extensible%20World%20Knowledge%20for%20Embodied%20Manipulation.md) — Across RoboTwin2.0, LIBERO/LIBERO-Plus, and real-world dual-arm manipulation, Key-Gram consistently improves both $π_{0}$ and $π_{0.5}$ backbones, with average relative gains of $29.5\%/9.9\%$ on RoboTwin2.0, $35.8\%/4.5\%$ on LIBERO-Plus transfer without tar…
- [DexHoldem: Playing Texas Hold'em with Dexterous Embodied System](items/DexHoldem%20Playing%20Texas%20Hold%27em%20with%20Dexterous%20Embodied%20System.md) — On primitive execution, $π_{0.5}$ obtains the highest task completion rate ($61.2\%$), while $π_{0.5}$ and $π_0$ tie on scene-preserving success rate ($47.5\%$).

## 其余存档 12 篇

- [Qumus: Realization of An Embodied AI Quantum Material Experimentalist](items/Qumus%20Realization%20of%20An%20Embodied%20AI%20Quantum%20Material%20Experimentalist.md) · [[多模态基础模型]] [[智能体 Agent]]
- [On Improving Multimodal Pedestrian Trajectory Prediction with CVAE: A Study on Benchmark and Robot Data](items/On%20Improving%20Multimodal%20Pedestrian%20Trajectory%20Prediction%20with%20CVAE%20A%20Study%20on%20Be.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning](items/Non-Colliding%20Biometric%20Identities%20for%20Digital%20Entities%20Geometry%2C%20Capacity%2C%20and.md) · [[智能体 Agent]]
- [SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects](items/SceneCode%20Executable%20World%20Programs%20for%20Editable%20Indoor%20Scenes%20with%20Articulated.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Sampling-Based Safe Reinforcement Learning](items/Sampling-Based%20Safe%20Reinforcement%20Learning.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution](items/SWEET%20Sparse%20World%20Modeling%20with%20Image%20Editing%20for%20Embodied%20Task%20Execution.md) · [[智能体 Agent]] [[世界模型]]
- [Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR](items/Rethinking%20Muon%20Beyond%20Pretraining%20Spectral%20Failures%20and%20High-Pass%20Remedies%20for.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [EgoBabyVLM: Benchmarking Cross-Modal Learning from Naturalistic Egocentric Video Data](items/EgoBabyVLM%20Benchmarking%20Cross-Modal%20Learning%20from%20Naturalistic%20Egocentric%20Video.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Code as Agent Harness](items/Code%20as%20Agent%20Harness.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](items/StableVLA%20Towards%20Robust%20Vision-Language-Action%20Models%20without%20Extra%20Data.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Beyond Waypoints: Dual-Heatmap Grounding for Cross-Embodiment Semantic Navigation](items/Beyond%20Waypoints%20Dual-Heatmap%20Grounding%20for%20Cross-Embodiment%20Semantic%20Navigation.md) · [[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- [Domain-Adaptive Communication-Rate Optimization for Sim-to-Real Humanoid-Robot Wireless XR Teleoperation](items/Domain-Adaptive%20Communication-Rate%20Optimization%20for%20Sim-to-Real%20Humanoid-Robot%20W.md) · [[机器人学习]] [[Sim2Real]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2019
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Dexora: Open-source VLA for High-DoF Bimanual Dexterity
- 最高分论文发布时间：2026-05-18T17:50:32Z
- 主要技术对象分类：具身智能评测与基准 19、多模态基础模型 18、智能体 Agent 15、世界模型 11、机器人学习 7、视觉语言动作模型 VLA 6、Sim2Real 2
- 信息源错误：0

</details>
