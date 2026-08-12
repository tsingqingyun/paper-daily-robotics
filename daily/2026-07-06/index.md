---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-06
---

# 2026-07-06 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Seek to Segment: Active Perception for Panoramic Referring Segmentation](items/Seek%20to%20Segment%20Active%20Perception%20for%20Panoramic%20Referring%20Segmentation.md) — Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.

- **规模**：2113 个候选 → 24 篇入选；回填 0 篇
- **主题**：世界模型 13、具身智能评测与基准 12、智能体 Agent 11、多模态基础模型 8、机器人学习 8、视觉语言动作模型 VLA 3、Sim2Real 2、AI 核心知识地图 1
- **源异常**：0

## 必读 5 篇

### 1. [Seek to Segment: Active Perception for Panoramic Referring Segmentation](items/Seek%20to%20Segment%20Active%20Perception%20for%20Panoramic%20Referring%20Segmentation.md)

- **创新点 / 方法**：To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS).
- **证据**：Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.

### 2. [Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning](items/Actuator%20Reality%20Shaping%20for%20Zero-Shot%20Sim-to-Real%20Robot%20Learning.md)

- **创新点 / 方法**：While conventional approaches attempt to bridge this gap by increasing simulator fidelity through system identification, domain randomization, or learned actuator models, we introduce an alternative paradigm: actuator reality shaping.
- **证据**：We validate the approach on a single-joint high- gear-ratio servo under external loads and a 7-DOF robotic arm reaching task, where actuator reality shaping substantially reduces sim-to-real tracking error and improves zero-shot task performance compared with standard servo-control and representative real- to-sim-to-r…

### 3. [Structured 4D Latent Predictive Model for Robot Planning](items/Structured%204D%20Latent%20Predictive%20Model%20for%20Robot%20Planning.md)

- **创新点 / 方法**：We introduce a Structured 4D Latent Predictive Model, which predicts the evolution of a scene's 3D structure in a structured latent space conditioned on observations and textual instructions.
- **证据**：Consequently, our full planning pipeline achieves superior performance on complex manipulation tasks, exhibits robust generalization to novel visual conditions, and proves effective on real- world robotic platforms.

### 4. [ROSA: A Robotics Foundation Model Serving System for Robot Factories](items/ROSA%20A%20Robotics%20Foundation%20Model%20Serving%20System%20for%20Robot%20Factories.md)

- **创新点 / 方法**：In this paper, we propose ROSA, an RFM serving system for robot factories designed around three key principles.
- **证据**：The results show that ROSA improves factory productivity by up to 12.06x over conventional dedicated serving systems.

### 5. [RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](items/RoboWorld%20Fast%20and%20Reliable%20Neural%20Simulators%20for%20Generalist%20Robot%20Policy%20Evalua.md)

- **创新点 / 方法**：We introduce RoboWorld, an automated evaluation pipeline that pairs a fast autoregressive video world model with a task-progress-aware vision-language model scoring.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [From World Models to World Action Models: A Concise Tutorial for Robotics](items/From%20World%20Models%20to%20World%20Action%20Models%20A%20Concise%20Tutorial%20for%20Robotics.md) — This tutorial presents a design- space view of world models as action-conditioned predictive models that estimate the future evolution of task-relevant observations or states.
- [VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning](items/VLM-AR3L%20Vision-Language%20Models%20for%20Absolute%20and%20Relative%20Rewards%20in%20Reinforceme.md) — Experimental results show that VLM-AR3L consistently outperforms prior VLM-based reward learning methods.
- [QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition](items/QFedAgent%20Quantum-Enhanced%20Personalized%20Federated%20Learning%20for%20Multi-Agent%20Activ.md) — Experiments on the OPPORTUNITY dataset under subject-based non-IID partitions demonstrate 97.7% mean test accuracy, confirming that parameter-efficient quantum fusion remains competitive with conventional federated baselines.
- [ACID: Action Consistency via Inverse Dynamics for Planning with World Models](items/ACID%20Action%20Consistency%20via%20Inverse%20Dynamics%20for%20Planning%20with%20World%20Models.md) — Across four action-conditioned world models and six tasks spanning rigid and deformable manipulation, articulated control, and visual navigation, ACID consistently improves planning and matches the baseline's accuracy with substantially less planning compute.
- [Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos](items/Local%20Motion%20Matters%20A%20Deconstruct-Recompose%20Paradigm%20for%20Reinforcement%20Learning.md) — Building on this insight, we propose a novel Deconstruct- Recompose Paradigm (DRP) for learning transferable local motion representations.
- [Task-Relevant Representation Decoupling for Visual Reinforcement Learning Generalization](items/Task-Relevant%20Representation%20Decoupling%20for%20Visual%20Reinforcement%20Learning%20Genera.md) — T2RD achieves State-Of-The-Art (SOTA) generalization performance and sample efficiency in the DeepMind Control Suite and Robotic Manipulation tasks.
- [Partial Skeleton Visibility for Action Recognition: A Constrained Field-of-View Approach](items/Partial%20Skeleton%20Visibility%20for%20Action%20Recognition%20A%20Constrained%20Field-of-View%20A.md) — Extensive experiments demonstrate that PartialVisGraph consistently achieves state-of-the-art accuracy under partial visibility, with gains of up to 68.8\% on subsets with severe FoV restrictions compared to recent strong baselines, while remaining superior o…

## 其余存档 12 篇

- [DL-VINS-Factory: A Modular Framework for Learned Visual Front-Ends in Visual-Inertial SLAM](items/DL-VINS-Factory%20A%20Modular%20Framework%20for%20Learned%20Visual%20Front-Ends%20in%20Visual-Iner.md) · [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](items/CoRe%20Combined%20Rewards%20with%20Vision-Language%20Model%20Feedback%20for%20Preference-Aligned.md) · [[多模态基础模型]] [[世界模型]] [[机器人学习]]
- [BIFROST: Bridging Invariant Feature Representation for Observation-space Sim2Real Transfer](items/BIFROST%20Bridging%20Invariant%20Feature%20Representation%20for%20Observation-space%20Sim2Real.md) · [[世界模型]] [[Sim2Real]]
- [GEAR-Seg: A Grounded Explainable Agent for Reasoning Segmentation and Data Engine](items/GEAR-Seg%20A%20Grounded%20Explainable%20Agent%20for%20Reasoning%20Segmentation%20and%20Data%20Engine.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$](items/EAGLE-360%20Embodied%20Active%20Global-to-Local%20Exploration%20in%20360%24%20circ%24.md) · [[多模态基础模型]]
- [PWM-ArtGen: Part World Model for Articulated Object Generation](items/PWM-ArtGen%20Part%20World%20Model%20for%20Articulated%20Object%20Generation.md) · [[世界模型]]
- [SPLC: Social Preference Learning for Crowd Robot Navigation](items/SPLC%20Social%20Preference%20Learning%20for%20Crowd%20Robot%20Navigation.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Robust Image Processing Techniques for Construction Environment Monitoring Using Underwater Robots](items/Robust%20Image%20Processing%20Techniques%20for%20Construction%20Environment%20Monitoring%20Using.md) · [[具身智能评测与基准]]
- [Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model](items/Safe%20and%20Adaptive%20Cloud%20Healing%20Verifying%20LLM-Generated%20Recovery%20Plans%20with%20a%20Ne.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems](items/Hardware-Enforced%20Semantic%20Coordination%20for%20Safety-Critical%20Real-Time%20Autonomous.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation](items/Real-Time%20Visual%20Intelligence%20on%20Low-Cost%20UAVs%20A%20Modular%20Approach%20for%20Tracking%2C.md) · [[AI 核心知识地图]]
- [SpaceEra++: A Unified Framework Towards 3D Spatial Reasoning in Video](items/SpaceEra%2B%2B%20A%20Unified%20Framework%20Towards%203D%20Spatial%20Reasoning%20in%20Video.md) · [[多模态基础模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2113
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Seek to Segment: Active Perception for Panoramic Referring Segmentation
- 最高分论文发布时间：2026-07-02T17:56:49Z
- 主要技术对象分类：世界模型 13、具身智能评测与基准 12、智能体 Agent 11、多模态基础模型 8、机器人学习 8、视觉语言动作模型 VLA 3、Sim2Real 2、AI 核心知识地图 1
- 信息源错误：0

</details>
