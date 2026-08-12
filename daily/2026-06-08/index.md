---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-08
---

# 2026-06-08 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Robots Need More than VLA and World Models](items/Robots%20Need%20More%20than%20VLA%20and%20World%20Models.md) — In this position paper, we argue that this framing is incomplete.

- **规模**：2056 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 20、世界模型 14、视觉语言动作模型 VLA 14、智能体 Agent 13、具身智能评测与基准 11、机器人学习 9、Sim2Real 3
- **源异常**：0

## 必读 5 篇

### 1. [Robots Need More than VLA and World Models](items/Robots%20Need%20More%20than%20VLA%20and%20World%20Models.md)

- **创新点 / 方法**：In this position paper, we argue that this framing is incomplete.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](items/World-Language-Action%20Model%20for%20Unified%20World%20Modeling%2C%20Language%20Reasoning%2C%20and.md)

- **创新点 / 方法**：We propose world-language-action (WLA) models as a new class of embodied foundation models.
- **证据**：Our WLA-0 prototype, with 2B active parameters, achieves 40 ms per inference on an NVIDIA RTX 5090.

### 3. [PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](items/PiL-World%20A%20Chunk-Wise%20World%20Model%20for%20VLA%20Policy-in-the-Loop%20Evaluation.md)

- **创新点 / 方法**：To address this gap, we propose PiL-World, a chunk-wise world model designed for policy- in-the-loop VLA evaluation.
- **证据**：More importantly, compared with the baseline, it reduces the error between VLA success rates measured in real-world rollouts and those estimated through closed-loop world-model evaluation from 63.2% to 12.0%.

### 4. [AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](items/AffordanceVLA%20A%20Vision-Language-Action%20Model%20Empowering%20Action%20Generation%20throug.md)

- **创新点 / 方法**：To address this challenge, we propose \textbf{AffordanceVLA}, a unified framework that introduces structured affordance forecasting as a task-oriented intermediate representation to establish a more precise and robust perception--action mapping.
- **证据**：Extensive experiments on simulation and real-world demonstrate that AffordanceVLA achieves strong performance across diverse manipulation scenarios.

### 5. [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](items/LARA%20Latent%20Action%20Representation%20Alignment%20for%20Vision-Language-Action%20Models.md)

- **创新点 / 方法**：To address these issues, we propose Latent Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation alignment.
- **证据**：We demonstrate LARA versatility and effectiveness for pre-training, post- training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real- world robotic manipulation benchmarks.

## 扫读 7 篇

- [TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](items/TempoVLA%20Learning%20Speed-Controllable%20Vision-Language-Action%20Policies.md) — Experiments in simulation and on real-world tasks demonstrate that TempoVLA achieves flexible speed control in both directions, while VSTA additionally boosts the default $1\times$ performance via better data utilization.
- [Safe Embodied AI for Long-horizon Tasks: A Cross-layer Analysis of Robotic Manipulation](items/Safe%20Embodied%20AI%20for%20Long-horizon%20Tasks%20A%20Cross-layer%20Analysis%20of%20Robotic%20Manipu.md) — Embodied AI systems are increasingly expected to reason and act over extended horizons in physical environments.
- [WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation](items/WorldFly%20A%20World-Model-Based%20Vision-Language-Action%20Model%20for%20UAV%20Navigation.md) — Extensive evaluations on our benchmark demonstrate that WorldFly outperforms other baselines, particularly in unseen environments, validating the effectiveness of integrating world models into embodied aerial agents.
- [RhinoVLA Technical Report](items/RhinoVLA%20Technical%20Report.md) — Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target.
- [ActionMap: Robot Policy Learning via Voxel Action Heatmap](items/ActionMap%20Robot%20Policy%20Learning%20via%20Voxel%20Action%20Heatmap.md) — To advance this, we introduce ActionMap, a voxel heatmap action head that drops into an existing VLA in place of its native action decoder.
- [Towards a Data Flywheel for Embodied Intelligence in Logistics](items/Towards%20a%20Data%20Flywheel%20for%20Embodied%20Intelligence%20in%20Logistics.md) — Learning- based policies offer a promising path beyond traditional perception-planning-control pipelines, but their scalability depends on how embodied data can be collected, organized, and reused.
- [LadderMan: Learning Humanoid Perceptive Ladder Climbing](items/LadderMan%20Learning%20Humanoid%20Perceptive%20Ladder%20Climbing.md) — Experiments demonstrate that LadderMan achieves robust ladder climbing across a wide range of geometries, successfully transfers to real-world hardware in a zero-shot manner, and supports various manipulation tasks under challenging ladder constraints.

## 其余存档 12 篇

- [Robotic Policy Adaptation via Weight-Space Meta-Learning](items/Robotic%20Policy%20Adaptation%20via%20Weight-Space%20Meta-Learning.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective](items/The%20Sim-to-Real%20Gap%20of%20Foundation%20Model%20Agents%20A%20Unified%20MDP%20Perspective.md) · [[多模态基础模型]] [[智能体 Agent]] [[Sim2Real]] [[具身智能评测与基准]]
- [Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation](items/Think%20Like%20a%20Pilot%20Fine-Grained%20Long-Horizon%20UAV%20Navigation.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models](items/Coarse-to-Control%20Action-Token%20Planning%20for%20Vision-Language-Action%20Models.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- [PhyRoGen: Synthetic Generation of Physical Robot Manipulation Puzzles Using Procedural Content Generation](items/PhyRoGen%20Synthetic%20Generation%20of%20Physical%20Robot%20Manipulation%20Puzzles%20Using%20Proce.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthetic Grasping](items/Simulation-Driven%20Imitation%20Learning%20for%20Biosignals-Free%20Shared-Autonomy%20Prosthe.md) · [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- [GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios](items/GenPO%2B%2B%20Generative%20Policy%20Optimization%20with%20Jacobian-free%20Likelihood%20Ratios.md) · [[多模态基础模型]] [[机器人学习]]
- [HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](items/HANDOFF%20Humanoid%20Agentic%20Task-Space%20Whole-Body%20Control%20via%20Distilled%20Complementa.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning](items/CAPE%20Contrastive%20Action-conditioned%20Parallel%20Encoding%20for%20Embodied%20Planning.md) · [[智能体 Agent]] [[世界模型]]
- [Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning](items/Dreaming%20when%20Necessary%20Advancing%20World%20Action%20Models%20with%20Adaptive%20Multi-Modal.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- [Spline Policy: A Structured Representation for Robot Policies](items/Spline%20Policy%20A%20Structured%20Representation%20for%20Robot%20Policies.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [SCOUT: Semantic scene COverage via Uncertainty-guided Traversal](items/SCOUT%20Semantic%20scene%20COverage%20via%20Uncertainty-guided%20Traversal.md) · [[智能体 Agent]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2056
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Robots Need More than VLA and World Models
- 最高分论文发布时间：2026-06-04T10:43:14Z
- 主要技术对象分类：多模态基础模型 20、世界模型 14、视觉语言动作模型 VLA 14、智能体 Agent 13、具身智能评测与基准 11、机器人学习 9、Sim2Real 3
- 信息源错误：0

</details>
