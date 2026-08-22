---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-22
---

# 2026-08-22 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[EXIMO: VLM Guided Exploration of VLA Policies](items/EXIMO%20VLM%20Guided%20Exploration%20of%20VLA%20Policies.md) — In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.

- **规模**：2259 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、世界模型 9、多模态基础模型 9、智能体 Agent 9、机器人学习 9、视觉语言动作模型 VLA 8、AI 核心知识地图 3、Sim2Real 2
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [EXIMO: VLM Guided Exploration of VLA Policies](items/EXIMO%20VLM%20Guided%20Exploration%20of%20VLA%20Policies.md)

- **创新点 / 方法**：In this work, we propose EXIMO, an efficient algorithm for finetuning of VLA policies.
- **证据**：In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.

### 2. [Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation](items/Fine-Tuning%20VLAs%20with%20Self-Demonstrated%20Generative%20Control%20for%20Multi-Task%20Manipu.md)

- **创新点 / 方法**：In this paper, we propose a self-supervised method that generates online interaction rollouts from the zero-shot VLA as additional training data for finetuning.
- **证据**：Our experiments show this finetuning scheme yields strong multi-task policies that, on the target robot, (1) inherit prior tasks distilled from the zero-shot model, (2) enable generalist instruction following, while (3) learning new skills from expert data with improved sample efficiency.

### 3. [RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation](items/RoMAN-Flow%20Taming%20Autoregressive%20Normalizing%20Flows%20for%20Offline%20Reinforcement%20Lea.md)

- **创新点 / 方法**：We present RoMAN-Flow (Robotic Manipulation with Autoregressive Normalizing Flows), an offline reinforcement learning framework that makes AR-NF policies practical for robotic manipulation by addressing this sampling bottleneck in both stages.
- **证据**：Offline reinforcement learning improves robotic policies using previously collected data without further environment interaction.

### 4. [OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation](items/OrthoSkillVLA%20Continual%20Skill%20Learning%20via%20Gradient-Informed%20Skill%20Subspace%20Adap.md)

- **创新点 / 方法**：To this end, we propose OrthoSkillVLA, a parameter-efficient framework for continual skill learning in pretrained VLA models without demonstration replay.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [DreamHand: Repurposing Video Diffusion Models for Occlusion-Robust Egocentric 3D Hand Motion Recovery](items/DreamHand%20Repurposing%20Video%20Diffusion%20Models%20for%20Occlusion-Robust%20Egocentric%203D.md)

- **创新点 / 方法**：We introduce DreamHand, an offline clip-level framework that extracts features via a Deterministic Clean-Latent Encoder and decodes them with a Bidirectional Spatiotemporal Decoder.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms](items/Planning-Oriented%20End-to-End%20Autonomous%20Driving%20Architectures%2C%20Evaluation%2C%20and%20E.md) — End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols.
- [Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](items/Towards%20Professional%20Tennis%20Styles%20for%20Humanoid%20Robots%20with%20Adaptive%20Motion%20Plan.md) — To address these issues, our adaptation mechanism improves tracking robustness by learning to track randomized execution speeds, while conditioning the planner on a learned motion-speed adapter to mitigate compounding errors.
- [GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation](items/GOAG%20Generative%20and%20Object-Agnostic%20Grasp%20Planner%20for%20Dexterous%20Robotic%20Manipula.md) — Our method delivers state-of-the-art results on the objects from the MultiDex dataset, achieving an average success rate of 86.93%.
- [Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions](items/Robust%20Cross-Modal%20Foundation%20Model%20Perception%20for%20Underwater%20Robots%20under%20Degra.md) — Under extreme combined degradation, the DINOv2 baseline achieves 0.4610 balanced accuracy, while degradation-aware visual-sonar fusion reaches 0.6152, a 33.5% relative improvement.
- [What Matters for Latent Actions in Robot Learning](items/What%20Matters%20for%20Latent%20Actions%20in%20Robot%20Learning.md) — In this work, we present the first comprehensive empirical study of latent action learning for robotic manipulation.
- [Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control](items/Hybrid%20Feedback%20Sampling%20for%20Sample-Efficient%20Model%20Predictive%20Control.md) — Our theoretical analysis shows that our hybrid sampling approach achieves faster convergence than standard MPPI and better optimality than standard feedback sampling.
- [Multi-Tool Robotics Enables In-Situ Sample Manipulation for Time-Resolved Synchrotron Measurements](items/Multi-Tool%20Robotics%20Enables%20In-Situ%20Sample%20Manipulation%20for%20Time-Resolved%20Synchr.md) — Here we present a robotic platform at an X-ray scattering beamline to enable real-time sample handling and processing in the experimental hutch, revealing previously inaccessible transient in-situ dynamics in perovskite thin films.

## 其余存档 12 篇

- [Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents](items/Towards%20general%20embodied%20intelligence%20integrating%20large%20language%20models%2C%20knowled.md) · [[多模态基础模型]] [[智能体 Agent]]
- [When Automata Meet Streams: Temporal Logic Compilation for Stream-Based Robotics Task and Motion Planning](items/When%20Automata%20Meet%20Streams%20Temporal%20Logic%20Compilation%20for%20Stream-Based%20Robotics.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [Video2DoorTraversal: Push Door Traversal via Simulated Door Twins](items/Video2DoorTraversal%20Push%20Door%20Traversal%20via%20Simulated%20Door%20Twins.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- [DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](items/DECOWAM%20Decoupled%20Whole-Body%20World-Action%20Model%20for%20Legged%20Mobile%20Manipulation.md) · [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [PVRA: A Pointwise Key-point Voting Framework for Robotic Assembly](items/PVRA%20A%20Pointwise%20Key-point%20Voting%20Framework%20for%20Robotic%20Assembly.md) · [[AI 核心知识地图]]
- [Keeping the Franka Emika Panda alive: a ROS 2 stack with a reliable position interface](items/Keeping%20the%20Franka%20Emika%20Panda%20alive%20a%20ROS%202%20stack%20with%20a%20reliable%20position%20inte.md) · [[智能体 Agent]] [[机器人学习]]
- [World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms](items/World-Model-Grounded%20LLM%20Planning%20for%20AUV%20and%20ASV%20Navigation%20Near%20Offshore%20Wind.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Effector-Centric NMPC of Tiltable-Multirotors for Offset-Free Omnidirectional Aerial Manipulation](items/Effector-Centric%20NMPC%20of%20Tiltable-Multirotors%20for%20Offset-Free%20Omnidirectional%20Ae.md) · [[AI 核心知识地图]]
- [An Irreducible Quantum Advantage in Aligning World Models with Reality](items/An%20Irreducible%20Quantum%20Advantage%20in%20Aligning%20World%20Models%20with%20Reality.md) · [[智能体 Agent]] [[世界模型]]
- [Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control](items/Learning%20the%20Right%20Abstraction%20Neural%20Reduced%20Dynamics%20for%20Complex%20Robot%20Control.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [DyG$^2$T: Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Graph Transformer](items/DyG%24%202%24T%20Modeling%20Object%20Dynamics%20with%203D%20Gaussian%20Temporal-Spatial%20Particle%20Gra.md) · [[世界模型]] [[视觉语言动作模型 VLA]]
- [Multimodal Rapport Estimation in Real-World HRI](items/Multimodal%20Rapport%20Estimation%20in%20Real-World%20HRI.md) · [[多模态基础模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2259
- 入选条目：24
- 回填已见条目：0
- 最高分论文：EXIMO: VLM Guided Exploration of VLA Policies
- 最高分论文发布时间：2026-08-20T10:58:45Z
- 主要技术对象分类：具身智能评测与基准 16、世界模型 9、多模态基础模型 9、智能体 Agent 9、机器人学习 9、视觉语言动作模型 VLA 8、AI 核心知识地图 3、Sim2Real 2
- 信息源错误：0
- 自动恢复信息源：0

</details>
