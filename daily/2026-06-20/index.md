---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-20
---

# 2026-06-20 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems](items/Co-VLA%20Coordination-Aware%20Structured%20Action%20Modeling%20for%20Dual-Arm%20Vision-Languag.md) — Experiments across simulation and real-world benchmarks show Co-VLA significantly outperforms monolithic baselines, achieving a 27% success rate gain in tight- coordination tasks, more than doubling performance in OOD real-world scenarios (from 13% to 27%), a…

- **规模**：2085 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、多模态基础模型 14、世界模型 12、智能体 Agent 10、机器人学习 10、视觉语言动作模型 VLA 10、AI 核心知识地图 1、Sim2Real 1
- **源异常**：0

## 必读 5 篇

### 1. [Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems](items/Co-VLA%20Coordination-Aware%20Structured%20Action%20Modeling%20for%20Dual-Arm%20Vision-Languag.md)

- **创新点 / 方法**：In this work, we propose Co-VLA, a coordination- aware bimanual manipulation framework introducing explicit structural priors into VLA models.
- **证据**：Experiments across simulation and real-world benchmarks show Co-VLA significantly outperforms monolithic baselines, achieving a 27% success rate gain in tight- coordination tasks, more than doubling performance in OOD real-world scenarios (from 13% to 27%), and reducing task completion time by up to 25%.

### 2. [Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think](items/Finetuning%20Vision-Language-Action%20Models%20Requires%20Fewer%20Layers%20Than%20You%20Think.md)

- **创新点 / 方法**：To exploit this, we introduce a structural compression pipeline that is entirely training-free, bypassing the need of existing methods to load full-scale models to learn optimized token reductions or dynamic layer selectors.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 3. [Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI](items/Data%20Standards%20for%20Humanoid%20Robotics%20The%20Missing%20Infrastructure%20for%20Physical%20AI.md)

- **创新点 / 方法**：We develop three insights.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](items/EventVLA%20Event-Driven%20Visual%20Evidence%20Memory%20for%20Long-Horizon%20Vision-Language-Ac.md)

- **创新点 / 方法**：To address these limitations, we introduce EventVLA, an end-to-end framework founded on the concept of sparse visual evidence memory that comprises two core components: foundational visual anchors to retain initial and short-term contexts, and a dynamic Keyframe Evidence Memory (KEM) module.
- **证据**：Extensive evaluations show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks, EventVLA achieves an average success rate improvement of +40% over state-of-the-art memory-augmented VLAs.

### 5. [EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models](items/EquiVLA%20A%20General%20Framework%20for%20Rotationally%20Equivariant%20Vision-Language-Action.md)

- **创新点 / 方法**：We present \textsc{EquiVLA}, the first general framework for end-to-end $\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a frozen vision-language backbone with a flow-matching Diffusion Transformer action head.
- **证据**：Instantiated on GR00T~N1.5 and evaluated across four LIBERO suites, CALVIN ABCD$\to$D, and five real- robot tasks on Mobile ALOHA, \textsc{EquiVLA} achieves $92.6\%$ average success on LIBERO (vs.

## 扫读 7 篇

- [CRAX: Fast Safe Reinforcement Learning Benchmarking](items/CRAX%20Fast%20Safe%20Reinforcement%20Learning%20Benchmarking.md) — To address this gap, we propose CRAX (Constrained RL Accelerated with JAX).
- [Bidirectional Tutoring for Developmental Motor Learning in Robots: Co-Developed Interaction Dynamics Support Stable Learning](items/Bidirectional%20Tutoring%20for%20Developmental%20Motor%20Learning%20in%20Robots%20Co-Developed%20I.md) — Although such social interaction is crucial for human development, motor- skill learning in robots is often treated as a unidirectional process in which robots passively receive demonstrations from tutors.
- [Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification](items/Fail-RAG%20A%20Retrieval%20Augmented%20Generation%20Informed%20Framework%20for%20Robot%20Failure%20I.md) — Fail-RAG achieved 25 percentage point higher failure detection accuracy on average across five types of robot operations compared to using off-the- shelf VLMs, indicating its effectiveness for real-world failure detection.
- [CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation](items/CoLI%20A%20Reproducible%20Platform%20for%20Continuum%20Robot%20Learning%20via%20Monolithic%203D%20Prin.md) — To address these challenges, we present a novel open-source continuum robot design.
- [Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation](items/Pose6DAug%20Physically%20Plausible%20Multi-view%20Object%20Swapping%20for%20Robot%20Data%20Augment.md) — Fine-tuning a VLA on data augmented by our method improves success rates by 16.5% relative to the state-of-the-art baseline on novel objects, while preserving in- distribution performance.
- [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](items/ENPIRE%20Agentic%20Robot%20Policy%20Self-Improvement%20in%20the%20Real%20World.md) — Powered by ENPIRE, frontier coding agents can autonomously train a policy to achieve a 99% success rate on challenging, dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and tool use, a process that further accelerates when we d…
- [Playful Agentic Robot Learning](items/Playful%20Agentic%20Robot%20Learning.md) — We introduce RATs, Robotics Agent Teams designed for play-time skill acquisition.

## 其余存档 12 篇

- [MemoryWAM: Efficient World Action Modeling with Persistent Memory](items/MemoryWAM%20Efficient%20World%20Action%20Modeling%20with%20Persistent%20Memory.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation](items/Frequency-Aware%20Flow%20Matching%20for%20Continuous%20and%20Consistent%20Robotic%20Action%20Gener.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation](items/TaCauchy%20An%20Extensible%20FEM%20Framework%20for%20Vision-Based%20Tactile%20Simulation.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving](items/Lagrange%20An%20Open-Vocabulary%2C%20Energy-Based%20Sparse%20Framework%20for%20Generalized%20End-t.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Start Right, Arrive Right: Asynchronous Execution via Initial Noise Selection](items/Start%20Right%2C%20Arrive%20Right%20Asynchronous%20Execution%20via%20Initial%20Noise%20Selection.md) · [[具身智能评测与基准]]
- [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](items/ImageWAM%20Do%20World%20Action%20Models%20Really%20Need%20Video%20Generation%2C%20or%20Just%20Image%20Edit.md) · [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory](items/Tri-Info%20Generalizable%2C%20Interpretable%20Failure%20Prediction%20for%20VLA%20Models%20via%20Info.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[Sim2Real]] [[具身智能评测与基准]]
- [DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning](items/DF-ExpEnse%20Diffusion%20Filtered%20Exploration%20for%20Sample%20Efficient%20Finetuning.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- [3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning](items/3D-DLP%20Self-Supervised%203D%20Object-Centric%20Scene%20Representation%20Learning.md) · [[AI 核心知识地图]]
- [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](items/Mem-World%20Memory-Augmented%20Action-Conditioned%20World%20Models%20for%20Persistent%20Robot.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [FlowMaps: Modeling Long-Term Multimodal Object Dynamics with Flow Matching](items/FlowMaps%20Modeling%20Long-Term%20Multimodal%20Object%20Dynamics%20with%20Flow%20Matching.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]]
- [See-and-Reach: Precise Vision-Language Navigation for UAVs within the Field of View](items/See-and-Reach%20Precise%20Vision-Language%20Navigation%20for%20UAVs%20within%20the%20Field%20of%20Vi.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2085
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems
- 最高分论文发布时间：2026-06-18T14:28:37Z
- 主要技术对象分类：具身智能评测与基准 16、多模态基础模型 14、世界模型 12、智能体 Agent 10、机器人学习 10、视觉语言动作模型 VLA 10、AI 核心知识地图 1、Sim2Real 1
- 信息源错误：0

</details>
