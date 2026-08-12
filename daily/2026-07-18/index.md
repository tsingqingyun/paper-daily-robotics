---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-18
---

# 2026-07-18 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning](items/Open-AoE%20An%20Open%20Egocentric%20Manipulation%20Dataset%20and%20Toolchain%20for%20Embodied%20Lear.md) — We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training.

- **规模**：2138 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 20、智能体 Agent 13、具身智能评测与基准 12、视觉语言动作模型 VLA 10、世界模型 8、机器人学习 6、Sim2Real 1
- **源异常**：0

## 必读 5 篇

### 1. [Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning](items/Open-AoE%20An%20Open%20Egocentric%20Manipulation%20Dataset%20and%20Toolchain%20for%20Embodied%20Lear.md)

- **创新点 / 方法**：We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [Reflex: Real-Time VLA Control through Streaming Inference](items/Reflex%20Real-Time%20VLA%20Control%20through%20Streaming%20Inference.md)

- **创新点 / 方法**：We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that perception encoders are functionally independent of the denoising loop.
- **证据**：On LIBERO and Kinetix benchmarks, Reflex achieves a 2.58$\times$ inference speedup and 50Hz stable streaming, reducing reaction latency by up to 54\% and enabling efficient deployment without performance degradation.

### 3. [RoboTTT: Context Scaling for Robot Policies](items/RoboTTT%20Context%20Scaling%20for%20Robot%20Policies.md)

- **创新点 / 方法**：We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency.
- **证据**：On challenging real-robot manipulation tasks, RoboTTT improves overall performance by 87% over the single-step context baseline and fully completes a five-minute, ten-stage assembly task, which no baseline ever does.

### 4. [Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation](items/Towards%20Human-like%20Physical%20Intelligence%20LifelongVision-Language-Action%20Learning.md)

- **创新点 / 方法**：To address this fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the plasticity-stability trade-off with a dual-timescale adaptation mechanism while achieving low-cost robotic deployment with a cache-ef…
- **证据**：However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models.

### 5. [Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color](items/Lights%2C%20Camera%2C%20Malfunction%20When%20Illumination%20Robustness%20Leaves%20VLA%20Models%20Blind.md)

- **创新点 / 方法**：We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals.
- **证据**：We expose this degradation through a diagnostic grayscale evaluation, in which the defended model maintains high success rates on grayscale inputs, while its success rate on benign, color-dependent real-world tasks drops to at most 47.5%, well below the undefended baseline.

## 扫读 7 篇

- [Knowing You at First Glance: Inferring Apparent Personality from Faces](items/Knowing%20You%20at%20First%20Glance%20Inferring%20Apparent%20Personality%20from%20Faces.md) — To this end, we propose \textbf{GlanceFace}, an end-to-end framework for apparent personality inference leveraging vision-language models to introduce semantic priors and a semantic-enhanced facial representation module to capture subtle personality-related c…
- [Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation](items/Representation-Aligned%20Tactile%20Grounding%20for%20Contact-Rich%20Robotic%20Manipulation.md) — Experiments on real-world contact-rich manipulation tasks show that representation-aligned tactile grounding outperforms less aligned or multi-interface tactile prediction, highlighting the importance of where tactile supervision is applied.
- [RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination](items/RxBrain%20Embodied%20Cognition%20Foundation%20Model%20with%20Joint%20Language-Visual%20Reasoning.md) — Experiments show that RxBrain maintains embodied understanding and generation abilities, and produces plans with coupled textual reasoning, world state prediction, and joint subgoal planning.
- [Scaling Behavior Foundation Model for Humanoid Robots](items/Scaling%20Behavior%20Foundation%20Model%20for%20Humanoid%20Robots.md) — Through extensive experiments in both simulation and real-world deployment, we demonstrate that our approach yields significant improvements in control fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on the test set by over…
- [Active Real-World Factor-Based Evaluation for Generalist Robot Policies](items/Active%20Real-World%20Factor-Based%20Evaluation%20for%20Generalist%20Robot%20Policies.md) — We propose an active evaluation framework that addresses this challenge by treating policy evaluation as a sequential experimental design problem.
- [DiMaS: Distribution Matching for Steering Vision-Language-Action Models](items/DiMaS%20Distribution%20Matching%20for%20Steering%20Vision-Language-Action%20Models.md) — Representation steering is a well- established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs.
- [Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection](items/Never%20Too%20Late%20for%20Force%20Accelerating%20VLA%20Post-Training%20with%20Reactive%20Force%20Inje.md) — We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post- training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge.

## 其余存档 12 篇

- [DriftWorld: Fast World Modeling through Drifting](items/DriftWorld%20Fast%20World%20Modeling%20through%20Drifting.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment](items/SUFLECA%20Scaling%20Up%20Feature%20Learning%20for%20CAD-to-image%20Alignment.md) · [[多模态基础模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [Hierarchical Denoising For Multi-Step Visual Reasoning](items/Hierarchical%20Denoising%20For%20Multi-Step%20Visual%20Reasoning.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents](items/SafeRelBench%20A%20Spatial-Relation-Aware%20Benchmark%20for%20Process-Level%20Safety%20in%20VLM-.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [VTM-Nav: Hierarchical Visual-Topological Memory for Cross-Episode Object-Goal Navigation](items/VTM-Nav%20Hierarchical%20Visual-Topological%20Memory%20for%20Cross-Episode%20Object-Goal%20Nav.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments](items/Safe%20Execution%20of%20RL%20Policies%20Via%20Acceleration-Based%20CBF-QP%20Constraint%20Enforceme.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [SoftNav: Injecting 3D Scene Tokens into VLMs for Embodied Navigation](items/SoftNav%20Injecting%203D%20Scene%20Tokens%20into%20VLMs%20for%20Embodied%20Navigation.md) · [[多模态基础模型]] [[智能体 Agent]]
- [HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents](items/HyMobileAgent%20Data-Environment%20Co-Scaling%20for%20Efficient%20GUI%20Agents.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- [Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](items/Zero2Skill%20Bootstrapping%20Robot%20Skills%20through%20Autonomous%20Data%20Collection%2C%20Traini.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](items/S-squared-VLA%20Decoupling%20Semantic%20and%20Spatial%20Streams%20in%20Vision-Language-Action.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](items/AeroAct%20Action-Centered%20World-Action%20Models%20for%20Language-Conditioned%20Quadrotor%20F.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [Multimodality as Supervision: Self-Supervised Specialization to the Test Environment via Multimodality](items/Multimodality%20as%20Supervision%20Self-Supervised%20Specialization%20to%20the%20Test%20Environm.md) · [[多模态基础模型]] [[智能体 Agent]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2138
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning
- 最高分论文发布时间：2026-07-15T14:49:49Z
- 主要技术对象分类：多模态基础模型 20、智能体 Agent 13、具身智能评测与基准 12、视觉语言动作模型 VLA 10、世界模型 8、机器人学习 6、Sim2Real 1
- 信息源错误：0

</details>
