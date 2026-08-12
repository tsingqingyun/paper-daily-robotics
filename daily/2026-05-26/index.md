---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-05-26
---

# 2026-05-26 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models](items/EXPO-FT%20Sample-Efficient%20Reinforcement%20Learning%20Finetuning%20for%20Vision-Language-A.md) — Our system achieves perfect task performance (30/30 successes) across all evaluated tasks within an average of 19.1 minutes of online robot data, outperforming both prior RL-from-scratch and VLA finetuning approaches.

- **规模**：250 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、多模态基础模型 15、智能体 Agent 11、世界模型 8、机器人学习 8、视觉语言动作模型 VLA 8、AI 核心知识地图 1、Sim2Real 1
- **源异常**：4
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models](items/EXPO-FT%20Sample-Efficient%20Reinforcement%20Learning%20Finetuning%20for%20Vision-Language-A.md)

- **创新点 / 方法**：We present EXPO-FT, a system for stable, sample-efficient RL finetuning of pretrained VLA policies that closes this gap.
- **证据**：Our system achieves perfect task performance (30/30 successes) across all evaluated tasks within an average of 19.1 minutes of online robot data, outperforming both prior RL-from-scratch and VLA finetuning approaches.

### 2. [X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models](items/X-DiffVLA%20X-Embodied%20Diffusion%20Action%20Heads%20for%20Vision-Language-Action%20Models.md)

- **创新点 / 方法**：Specifically, we introduce Embodiment Forcing, a classifier-free guidance technique to implicitly steer action generation toward embodiment-specific functional components, capturing fine-grained structural nuances without explicit supervision.
- **证据**：Experimental results across RoboCasa and Isaac Gym, covering different embodiments from grippers to dexterous hands, show that X-DiffVLA achieves state-of-the-art performance, with improvements of 15.3% and 12.5%, respectively.

### 3. [Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models](items/Capability%20and%20Robustness%20Cannot%20Both%20Be%20Free%20An%20Information-Theoretic%20Bound%20for.md)

- **创新点 / 方法**：We propose encoder- specific slack as a normalized comparison axis for defense papers, and release all code, manifests, and results.
- **证据**：They reach high success rates on clean inputs but collapse under small adversarial perturbations.

### 4. [OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation](items/OASIS%20Observation-Action%20Space%20Alignment%20via%20SE%283%29%20Trajectory%20Prediction%20for%20Rob.md)

- **创新点 / 方法**：We propose OASIS, a visuomotor policy that aligns the intermediate representation with the action space via $SE(3)$ end-effector trajectory prediction.
- **证据**：Across simulation and real-world experiments, OASIS outperforms VLA and WAM baselines in success rate and out-of-distribution generalization.

### 5. [Grow-Prune-Freeze Networks: Adaptive & Continual Learning Technique for Olfactory Navigation](items/Grow-Prune-Freeze%20Networks%20Adaptive%20%26%20Continual%20Learning%20Technique%20for%20Olfactory.md)

- **创新点 / 方法**：We introduce an adaptive framework called Grow-Prune-Freeze (GPF) networks that enable an agent to continually learn through growing, pruning, and freezing early layers of its policy in response to world complexity.
- **证据**：Grounding GPFs in non-linear random matrix theory, we show that the work of Pennington & Worth (2017) can be extended from single hidden layers to n-layer continual-learning models, and that eigenvalue composition of network weights is preserved as successive layers are added.

## 扫读 7 篇

- [TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation](items/TapSampling%20Inference-Time%20Sampling%20with%20a%20Task-Progress-Understanding%20Verifier.md) — Extensive experiments in both simulated and real-world environments demonstrate that our method substantially improves multiple generalist policies without further policy finetuning.
- [Rethinking VLM Representation for VLA Initialization](items/Rethinking%20VLM%20Representation%20for%20VLA%20Initialization.md) — Our experiments show that the original pretrained VLM representation is a key source of action performance.
- [FOUND-IT: Foundation-model-first Task-driven 3D Scene Graphs with Granularity on Demand](items/FOUND-IT%20Foundation-model-first%20Task-driven%203D%20Scene%20Graphs%20with%20Granularity%20on.md) — In addition to achieving 79% higher accuracy on the ASHiTA SG3D task grounding benchmark, we demonstrate FOUND-IT runs in real-time on a ground robot using a Jetson Thor.
- [QuoVLA: Quotient Space for Vision-Language-Action Models](items/QuoVLA%20Quotient%20Space%20for%20Vision-Language-Action%20Models.md) — Extensive experiments across multiple benchmarks demonstrate that QuoVLA achieves strong performance, with particularly notable improvements in generalization under visual, linguistic, and environmental distribution shifts.
- [Hylos: Operability Contracts for Model-Native Spatial Intelligence](items/Hylos%20Operability%20Contracts%20for%20Model-Native%20Spatial%20Intelligence.md) — Foundation models can increasingly describe, reconstruct, and generate 3D objects, assemblies, scenes, and environments, but visually plausible spatial output is not yet operable 3D.
- [X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](items/X-Foresight%20A%20Joint%20Vision-Action%20Causal%20Forecasting%20Network%20via%20Predictive%20Worl.md) — Comprehensive experiments demonstrate that X-Foresight significantly outperforms VLA baselines in planning performance while maintaining strong generative fidelity, establishing a robust paradigm for world-knowledge-driven autonomous systems.
- [EgoProx: Evaluating MLLMs on Egocentric 3D Proximity Reasoning Across a Cognitive Hierarchy](items/EgoProx%20Evaluating%20MLLMs%20on%20Egocentric%203D%20Proximity%20Reasoning%20Across%20a%20Cognitive.md) — To this end, we introduce EgoProx, a benchmark for egocentric 3D proximity reasoning.

## 其余存档 12 篇

- [Towards Active Real-to-Twin Inspection: A New Paradigm for Zero-Shot Anomaly Detection](items/Towards%20Active%20Real-to-Twin%20Inspection%20A%20New%20Paradigm%20for%20Zero-Shot%20Anomaly%20Dete.md) · [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [Fishbone: From One 3D Asset to a Million Controllable Edits](items/Fishbone%20From%20One%203D%20Asset%20to%20a%20Million%20Controllable%20Edits.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [AgentGrounder: Zero-Shot 3D Visual Pointcloud Grounding using Multimodal Language Models](items/AgentGrounder%20Zero-Shot%203D%20Visual%20Pointcloud%20Grounding%20using%20Multimodal%20Language.md) · [[多模态基础模型]] [[智能体 Agent]]
- [RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation](items/RepSAM%20Bridging%20Foundation%20Models%20to%20Robotic%20Vision%20via%20Representation-Guided%20Ad.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [How to Mitigate the Distribution Shift Problem in Robotics Control: A Robust and Adaptive Approach Based on Offline to Online Imitation Learning](items/How%20to%20Mitigate%20the%20Distribution%20Shift%20Problem%20in%20Robotics%20Control%20A%20Robust%20and.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [InvariantCloud: A Globally Invariant, Uniquely Indexed Point Cloud Framework for Robust 6-DoF Tactile Pose Tracking](items/InvariantCloud%20A%20Globally%20Invariant%2C%20Uniquely%20Indexed%20Point%20Cloud%20Framework%20for.md) · [[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses,Evaluation, and Future Directions](items/Security%20in%20the%20Fine-Tuning%20Lifecycle%20of%20Large%20Language%20Models%20Threats%2C%20Defenses.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Stabilizing Streaming Video Geometry via Dynamic Feature Normalization](items/Stabilizing%20Streaming%20Video%20Geometry%20via%20Dynamic%20Feature%20Normalization.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models](items/Understanding%20the%20Impact%20of%20Geometric%20Foundation%20Models%20on%20Vision-Language-Actio.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [ParkourFormer: Integrating Predictive Supervision and Sequence Modeling into Parkour Locomotion](items/ParkourFormer%20Integrating%20Predictive%20Supervision%20and%20Sequence%20Modeling%20into%20Park.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Security of OpenClaw Agents: Fundamentals, Attacks, and Countermeasures](items/Security%20of%20OpenClaw%20Agents%20Fundamentals%2C%20Attacks%2C%20and%20Countermeasures.md) · [[智能体 Agent]]
- [Prior Policy Guided Dual-Agent Coordinated Manipulation Planning of Spacecraft-Manipulator System](items/Prior%20Policy%20Guided%20Dual-Agent%20Coordinated%20Manipulation%20Planning%20of%20Spacecraft-M.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：250
- 入选条目：24
- 回填已见条目：0
- 最高分论文：EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models
- 最高分论文发布时间：2026-05-25T06:31:03Z
- 主要技术对象分类：具身智能评测与基准 18、多模态基础模型 15、智能体 Agent 11、世界模型 8、机器人学习 8、视觉语言动作模型 VLA 8、AI 核心知识地图 1、Sim2Real 1
- 信息源错误：4

### 信息源错误

- OpenAI News: The read operation timed out
- Hugging Face Blog: The read operation timed out
- Microsoft Research Blog: <urlopen error _ssl.c:1112: The handshake operation timed out>
- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out>

</details>
