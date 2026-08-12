---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-12
---

# 2026-06-12 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models](items/Embodied-R1.5%20Evolving%20Physical%20Intelligence%20via%20Embodied%20Foundation%20Models.md) — With only 8B parameters, Embodied-R1.5 achieves SOTA on 16 out of 24 embodied VLM benchmarks, surpassing leading models like Gemini-Robotics-ER-1.5 and GPT-5.4.

- **规模**：2070 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、多模态基础模型 14、世界模型 11、智能体 Agent 11、机器人学习 10、视觉语言动作模型 VLA 10、Sim2Real 3
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models](items/Embodied-R1.5%20Evolving%20Physical%20Intelligence%20via%20Embodied%20Foundation%20Models.md)

- **创新点 / 方法**：We introduce Embodied-R1.5, a unified Embodied Foundation Model (EFM) that integrates comprehensive embodied reasoning capabilities, spanning embodied cognition, task planning, correction, and pointing, within a single architecture toward general physical intelligence.
- **证据**：With only 8B parameters, Embodied-R1.5 achieves SOTA on 16 out of 24 embodied VLM benchmarks, surpassing leading models like Gemini-Robotics-ER-1.5 and GPT-5.4.

### 2. [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](items/TacCoRL%20Integrating%20Tactile%20Feedback%20into%20VLA%20via%20Simulation.md)

- **创新点 / 方法**：We present TacCoRL, a scalable framework that injects Tactile feedback into VLA policies and improves them through sim-real Co-training and simulation-based reinforcement learning (RL), without requiring large-scale tactile pretraining or extensive real-world contact exploration.
- **证据**：Across four bimanual contact-rich tasks, the final visuo-tactile policy achieves an average success rate of 72.5%, compared to baseline of 50.0%.

### 3. [Intelligent Automation for Embodied Benchmark Construction: Pipelines, Embodiments, Simulators, and Trends](items/Intelligent%20Automation%20for%20Embodied%20Benchmark%20Construction%20Pipelines%2C%20Embodiment.md)

- **创新点 / 方法**：Embodied intelligence now spans navigation, household assistance, manipulation, autonomous driving, aerial agents, and multimodal large-model control.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [WorldOlympiad: Can Your World Model Survive a Triathlon?](items/WorldOlympiad%20Can%20Your%20World%20Model%20Survive%20a%20Triathlon.md)

- **创新点 / 方法**：We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [World Pilot: Steering Vision-Language-Action Models with World-Action Priors](items/World%20Pilot%20Steering%20Vision-Language-Action%20Models%20with%20World-Action%20Priors.md)

- **创新点 / 方法**：We present World Pilot, a VLA framework that augments the policy with priors from a World- Action Model (WAM), routed into the decision chain through two complementary pathways.
- **证据**：World Pilot attains a state-of-the-art Total success rate of 84.7% on the LIBERO-Plus zero-shot OOD benchmark and the highest success rate on every real-robot setting across four manipulation tasks, with the largest margins under shifts in viewpoint, geometry, deformable state, and pose.

## 扫读 7 篇

- [DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model](items/DAM-VLA%20Decoupled%20Asynchronous%20Multimodal%20Vision%20Language%20Action%20model.md) — Across seven contact-rich real-world manipulation tasks, DAM-VLA more than doubles the average success rate of the strongest synchronous baseline (95.2\% vs.\ 40.95\%) while sustaining smooth, reactive 100\,Hz control.
- [DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?](items/DIRECT%20When%20and%20Where%20Should%20You%20Allocate%20Test-Time%20Compute%20in%20Embodied%20Planners.md) — We validate these insights on a physical Franka arm in a DROID setup spanning zero-shot manipulation and long-horizon chaining, where our router matches or exceeds a stronger model's success rate at up to 65% lower average latency.
- [Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](items/Fourier%20Features%20Let%20Agents%20Learn%20High%20Precision%20Policies%20with%20Imitation%20Learnin.md) — High-precision robotic manipulation requires fine-grained spatial reasoning that is often difficult to achieve with RGB-only policies due to depth ambiguity and perspective scale issues.
- [DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World](items/DuoBench%20A%20Reproducible%20Benchmark%20for%20Bimanual%20Manipulation%20in%20Simulation%20and%20th.md) — Our results show that current policies remain challenged by bimanual manipulation, particularly in early interaction stages, parallel arm execution, and transfer between simulation and real-world settings.
- [Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning](items/Bridging%20the%20Morphology%20Gap%20Adapting%20VLA%20Models%20to%20Dexterous%20Manipulation%20via%20In.md) — Extensive simulation benchmarks across a suite of multi-stage, contact-rich dexterous manipulation tasks demonstrate that InDex effectively masters intricate skills with minimal demonstration data, substantially outperforming monolithic baselines while preser…
- [Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning](items/Blind%20Dexterous%20Grasping%20via%20Real2Sim2Real%20Tactile%20Policy%20Learning.md) — The deployed policy achieves a 27\% real-world grasp success rate across all 20 objects, without real-world grasping demonstrations or visual input.
- [Learning Object Manipulation from Scratch via Contrastive Interaction](items/Learning%20Object%20Manipulation%20from%20Scratch%20via%20Contrastive%20Interaction.md) — Across interaction-centric environments, including 2D dynamic control, robotic manipulation, and robot air hockey, IWR improves both sample efficiency and overall performance over prior CRL methods, with 19.8% average improvement in simulation.

## 其余存档 12 篇

- [APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](items/APT%20Action%20Expert%20Pretraining%20Improves%20Instruction%20Generalization%20of%20Vision-Lang.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [Implicit Neural Representations of Individual Behavior](items/Implicit%20Neural%20Representations%20of%20Individual%20Behavior.md) · [[智能体 Agent]] [[机器人学习]]
- [Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction](items/Embodied-BenchClaw%20An%20Autonomous%20Multi-Agent%20System%20for%20Embodied%20Spatial%20Intelli.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [SG2Loc: Sequential Visual Localization on 3D Scene Graphs](items/SG2Loc%20Sequential%20Visual%20Localization%20on%203D%20Scene%20Graphs.md) · [[智能体 Agent]]
- [Cross-Modal Benchmarking for Robotic Perception in Natural Environments](items/Cross-Modal%20Benchmarking%20for%20Robotic%20Perception%20in%20Natural%20Environments.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation](items/TacForeSight%20Force-Guided%20Tactile%20World%20Model%20for%20Contact-Rich%20Manipulation.md) · [[世界模型]] [[机器人学习]]
- [CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy](items/CHORUS%20Decentralized%20Multi-Embodiment%20Collaboration%20with%20One%20VLA%20Policy.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [World Model Self-Distillation: Training World Models to Solve General Tasks](items/World%20Model%20Self-Distillation%20Training%20World%20Models%20to%20Solve%20General%20Tasks.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [VICX: Generalizable Robot Manipulation via Video Generation and In-Context Operator Network](items/VICX%20Generalizable%20Robot%20Manipulation%20via%20Video%20Generation%20and%20In-Context%20Operat.md) · [[多模态基础模型]]
- [Bridging the sim2real gap in the table tennis robot with a transformer-based ball states predictor](items/Bridging%20the%20sim2real%20gap%20in%20the%20table%20tennis%20robot%20with%20a%20transformer-based%20bal.md) · [[智能体 Agent]] [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning](items/Test-Time%20Gradient%20Guidance%20of%20Flow%20Policies%20in%20Reinforcement%20Learning.md) · [[机器人学习]] [[具身智能评测与基准]]
- [VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving](items/VLGA%20Vision-Language-Geometry-Action%20Models%20for%20Autonomous%20Driving.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2070
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models
- 最高分论文发布时间：2026-06-09T18:07:50Z
- 主要技术对象分类：具身智能评测与基准 17、多模态基础模型 14、世界模型 11、智能体 Agent 11、机器人学习 10、视觉语言动作模型 VLA 10、Sim2Real 3
- 信息源错误：0

</details>
