---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-20
---

# 2026-07-20 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](items/Xiaomi-Robotics-1%20Scaling%20Vision-Language-Action%20Models%20with%20over%20100K%20Hours%20of.md) — Xiaomi- Robotics-1 consistently improves with increased data scales and model sizes during pre- training.

- **规模**：2138 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、多模态基础模型 12、智能体 Agent 12、机器人学习 11、世界模型 10、视觉语言动作模型 VLA 6、Sim2Real 1
- **源异常**：0

## 必读 5 篇

### 1. [Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](items/Xiaomi-Robotics-1%20Scaling%20Vision-Language-Action%20Models%20with%20over%20100K%20Hours%20of.md)

- **创新点 / 方法**：We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data.
- **证据**：Xiaomi- Robotics-1 consistently improves with increased data scales and model sizes during pre- training.

### 2. [IMBench: A Benchmark for Intuitive Robotic Manipulation](items/IMBench%20A%20Benchmark%20for%20Intuitive%20Robotic%20Manipulation.md)

- **创新点 / 方法**：We introduce IMBENCH, a benchmark designed to evaluate intuitive manipulation as an integrated capability spanning perception, physical reasoning, action generation, and iterative execution.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 3. [Handroid: Bridging Dexterous Hand and Humanoid](items/Handroid%20Bridging%20Dexterous%20Hand%20and%20Humanoid.md)

- **创新点 / 方法**：We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a single reconfigurable platform.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [Exo2EgoPose: Leveraging Exocentric Demonstrations for Vision-Language guided Egocentric 3D Hand Pose Forecasting](items/Exo2EgoPose%20Leveraging%20Exocentric%20Demonstrations%20for%20Vision-Language%20guided%20Egoc.md)

- **创新点 / 方法**：To overcome the limited field-of-view and highly dynamic motions in the Ego view, we propose a framework dubbed Exo2EgoPose, which innovatively leverages holistic and stable exocentric (Exo) demonstrations as guidance to compensate for partial and dynamic Ego-view cues.
- **证据**：Extensive experiments on \textit{AssemblyHands}, \textit{Ego-Exo4D}, and our newly constructed \textit{EgoMe-pose} benchmarks show the superiority of our method, which outperforms state-of-the-art methods by a large margin.

### 5. [Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation](items/Event3R%20Asynchronous-to-Global%203D%20Reconstruction%20from%20Event%20Camera%20via%20Spatial-T.md)

- **创新点 / 方法**：In this work, we introduce Event3R, a feed- forward framework that directly maps asynchronous event streams to globally consistent 3D point clouds.
- **证据**：Extensive experiments on both synthetic and real-world benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally aligned 3D reconstructions, significantly outperforming existing event-based methods.

## 扫读 7 篇

- [AC-VLA: Robust Out-of-Distribution Action Execution via Compositional Learning](items/AC-VLA%20Robust%20Out-of-Distribution%20Action%20Execution%20via%20Compositional%20Learning.md) — Instantiated on $π_{0.5}$ and evaluated on LIBERO and LIBERO-OOD benchmarks, AC-VLA achieves a ~28% absolute improvement on compositional OOD tasks while maintaining near-perfect in- distribution performance.
- [JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models](items/JoyNexus%20Service-Oriented%20Multi-Tenant%20Post-Training%20for%20VLA%20Models.md) — Results show that, compared with isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves service utilization via cross-tenant scheduling on shared resources.
- [Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation](items/Dynamics-Aware%20Meta-Imitation%20for%20Generalization%20to%20Unseen%20Robotic%20Manipulation.md) — Extensive experiments in both simulation and real-world settings demonstrate that our approach outperforms state-of-the-art baselines regarding direct inference on seen tasks and adaptation to unseen tasks via few-shot fine-tuning.
- [ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning](items/ToolVerse%20Unlocking%20Massive%20Environments%20and%20Long-Horizon%20Tasks%20for%20Agentic%20Rein.md) — To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks.
- [PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects](items/PIXIE%20A%20Zero-Shot%20texture-invariant%206D%20pose%20estimation%20framework%20for%20unseen%20obje.md) — We present PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image using only an untextured 3D model.
- [Embodied Active Learning under Limited Annotation and Navigation Budget for Object Detection](items/Embodied%20Active%20Learning%20under%20Limited%20Annotation%20and%20Navigation%20Budget%20for%20Obje.md) — Through comparison against several baselines, our experimental results show that spatial inconsistency helps guide the agent and select relevant images without external supervision, achieving the highest detection accuracy at the end of the adaptation process…
- [Learning Reach-Avoid Task with Reinforcement Learning: Vectorized Simulation and Benchmark](items/Learning%20Reach-Avoid%20Task%20with%20Reinforcement%20Learning%20Vectorized%20Simulation%20and.md) — We achieved state-of- the-art results with success rates of 96.1% (UR5e) and 98.8% (Franka Emika Robot) for the reach task and 86.8% (UR5e) and 95.2% (Franka) for the static reachavoid task.

## 其余存档 12 篇

- [RAVEN: Reinforcement-Adaptive Visibility-Graph Planning for Robust Humanoid Navigation with Collision-Free MPC](items/RAVEN%20Reinforcement-Adaptive%20Visibility-Graph%20Planning%20for%20Robust%20Humanoid%20Navig.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [PACE: Persona Adaptation through Conversational Elicitation in Human-Robot Interaction](items/PACE%20Persona%20Adaptation%20through%20Conversational%20Elicitation%20in%20Human-Robot%20Intera.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds](items/VTLoc%20Learning-based%20Tactile%20Contact%20Localization%20in%20Visual%20Point%20Clouds.md) · [[具身智能评测与基准]]
- [AEGIS: Assay-Aware Protocol Validation and Runtime Monitoring for Open-Source Liquid Handling Robots](items/AEGIS%20Assay-Aware%20Protocol%20Validation%20and%20Runtime%20Monitoring%20for%20Open-Source%20Liq.md) · [[多模态基础模型]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Recursive Harness Self-Improvement](items/Recursive%20Harness%20Self-Improvement.md) · [[多模态基础模型]] [[智能体 Agent]]
- [Robust Silicone Pour Casting and Sensor Embedding Procedures for Soft Robotic Actuators](items/Robust%20Silicone%20Pour%20Casting%20and%20Sensor%20Embedding%20Procedures%20for%20Soft%20Robotic%20Ac.md) · [[世界模型]] [[具身智能评测与基准]]
- [DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction](items/DPNeXt%20A%20Lightweight%20Multi-Scale%20Feature%20Fusion%20Framework%20for%20Efficient%20ViT-Base.md) · [[多模态基础模型]]
- [DSWorld: A Data Science World Model for Efficient Autonomous Agents](items/DSWorld%20A%20Data%20Science%20World%20Model%20for%20Efficient%20Autonomous%20Agents.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [An Intelligent-Cloud Edge Multimodal Interaction System for Robots](items/An%20Intelligent-Cloud%20Edge%20Multimodal%20Interaction%20System%20for%20Robots.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models](items/Action%20QFormer%20Structured%20Representation%20Shaping%20under%20Action%20Supervision%20in%20Vis.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[Sim2Real]]
- [Data and Learning Where it Matters for Contact-Rich Manipulation](items/Data%20and%20Learning%20Where%20it%20Matters%20for%20Contact-Rich%20Manipulation.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [NeuroCommitSSM: Decision-Centric Shared Autonomy for Safe Assistive Manipulation via EEG-EMG-ET Commit Readiness](items/NeuroCommitSSM%20Decision-Centric%20Shared%20Autonomy%20for%20Safe%20Assistive%20Manipulation.md) · [[智能体 Agent]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2138
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories
- 最高分论文发布时间：2026-07-16T16:02:25Z
- 主要技术对象分类：具身智能评测与基准 16、多模态基础模型 12、智能体 Agent 12、机器人学习 11、世界模型 10、视觉语言动作模型 VLA 6、Sim2Real 1
- 信息源错误：0

</details>
