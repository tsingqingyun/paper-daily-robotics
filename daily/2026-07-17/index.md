---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-17
---

# 2026-07-17 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](items/Exploratory%2C%20Communicative%2C%20and%20Deployable%20Vision-Driven%20Embodied%20Agents%20for%20Ope.md) — Experimental results demonstrate that our trained agent outperforms leading commercial closed-source VLMs on interactive tasks with a 56.9% success rate.

- **规模**：270 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 20、多模态基础模型 15、智能体 Agent 14、机器人学习 13、世界模型 11、视觉语言动作模型 VLA 8、Sim2Real 1
- **源异常**：2

## 必读 5 篇

### 1. [Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](items/Exploratory%2C%20Communicative%2C%20and%20Deployable%20Vision-Driven%20Embodied%20Agents%20for%20Ope.md)

- **创新点 / 方法**：To bridge this gap, we present REAL, an agentic framework for open-world mobile manipulation.
- **证据**：Experimental results demonstrate that our trained agent outperforms leading commercial closed-source VLMs on interactive tasks with a 56.9% success rate.

### 2. [Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning](items/Learning%20Robust%20Execution%20in%20Robotic%20Manipulation%20with%20Agentic%20Reinforcement%20Lea.md)

- **创新点 / 方法**：In this paper, we propose: (1) two complementary metrics to assess execution quality at runtime, and (2) an agentic reinforcement learning framework that learns to restore effective execution through high-level decision-making rather than directly learning low-level actions.
- **证据**：We evaluate the proposed method on the LIBERO benchmark, achieving up to a 13.7% improvement in success rate under standard settings and up to a 39.2% improvement under disturbance settings, demonstrating substantially enhanced execution robustness.

### 3. [ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning](items/ExToken%20Structured%20Exploration%20for%20Efficient%20Vision-Language-Action%20Reinforcemen.md)

- **创新点 / 方法**：Motivated by these insights, we introduce RL Exploration Token (ExToken), a simple yet general framework that condition VLA policies on discrete behavioral priors derived from offline demonstrations for structured exploration.
- **证据**：Extensive experiments across simulated and real-world robotic manipulation tasks demonstrate that ExToken consistently accelerates convergence, improves task performance, and exhibits strong robustness under highly constrained interaction budgets.

### 4. [Industrial Dexterity Benchmark: A Hardware-Software Benchmarking Platform for Industrial Dexterous Manipulation](items/Industrial%20Dexterity%20Benchmark%20A%20Hardware-Software%20Benchmarking%20Platform%20for%20Ind.md)

- **创新点 / 方法**：As a part of this work, we introduce three key contributions: a set of Industrial Dexterity Benchmark (IDB) boards aimed to mimic datacenter cable management, automotive cable harnesses, and gearbox assembly tasks; a scalable imitation learning framework (DAG-ROS); and a multimodal diffusion- based policy framework (A…
- **证据**：The best performing configuration, a multimodal expansion Diffusion Policy (DP), includes a multi-view RGB image source passed through an R3M encoder and reaches a 78% grasp and insert combined task success rate.

### 5. [Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](items/Jetson-PI%20Towards%20Onboard%20Real-Time%20Robot%20Control%20via%20Foresight-Aligned%20Asynchro.md)

- **创新点 / 方法**：In this paper, we propose Jetson-PI, a method for efficient VLA deployment on onboard devices via Foresight-Aligned Asynchronous Correction.
- **证据**：Extensive experiments demonstrate that Jetson-PI achieves 8.66x and 5.41x improvements in control frequency compared with naive PyTorch and vla.cpp on NVIDIA Jetson Orin, while outperforming VLASH by 14.8\% in average success rate on the LIBERO benchmark.

## 扫读 7 篇

- [Semantic Anchoring for Robotic Action Representations](items/Semantic%20Anchoring%20for%20Robotic%20Action%20Representations.md) — Validated on different VLA backbones across simulation and real-world benchmarks, our method yields up to +18.7% on real-world in-distribution tasks and +21.5% on out-of-distribution generalization.
- [Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](items/Generalizable%20VLA%20Finetuning%20via%20Representation%20Anchoring%20and%20Language-Action%20Al.md) — On a physical xArm7 robot, across two widely used VLA architectures, Anchor-Align improves real-robot success on both (28% to 54% and 37% to 60%).
- [FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](items/FlowWAM%20Optical%20Flow%20as%20a%20Unified%20Action%20Representation%20for%20World%20Action%20Models.md) — On RoboTwin manipulation, FlowWAM raises the success rate to 92.94% on the Clean setting and 92.14% on Random, outperforming both VLA and WAM baselines.
- [VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](items/VistaVLA%20Geometry-%20and%20Semantic-Aware%203D%20Gaussian-Grounded%20VLA%20for%20Robotic%20Manip.md) — Notably, in real-world scenarios, VistaVLA improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA- Adapter baseline on challenging out-of-distribution tasks.
- [UESF-Bench: Benchmarking and Probing for Unified Embodied Seeking and Following](items/UESF-Bench%20Benchmarking%20and%20Probing%20for%20Unified%20Embodied%20Seeking%20and%20Following.md) — Experimental results show that SeekFollow-VLA achieves clear improvements over both single-head and dual-head baselines across single-person and multi-person environments, establishing a baseline for unified embodied seek-and-follow.
- [EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal](items/EgoHTR%20Egocentric%204D%20Demonstrations%20of%20Human%20Terrain%20Traversal.md) — The resulting dataset comprises over 150k frames, which we evaluate against motion-capture ground truth, demonstrating state-of-the-art accuracy and establishing a rigorous benchmark for human motion analysis and synthesis.
- [DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation](items/DenseReward%20Dense%20Reward%20Learning%20via%20Failure%20Synthesis%20for%20Robotic%20Manipulation.md) — Experiments show that DenseReward outperforms general-purpose VLMs and existing robotic reward models in dense reward prediction across both simulated and real-world manipulation.

## 其余存档 12 篇

- [Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning](items/Breaking%20D%C3%A9j%C3%A0%20Vu%20Independent%20Auditing%20of%20Visual%20Place%20Recognition%20through%20Vision.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [Joint On-and-Off Policy Learning for Vision-and-Language Navigation](items/Joint%20On-and-Off%20Policy%20Learning%20for%20Vision-and-Language%20Navigation.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning](items/Vision-Based%20Dribbling%20for%20Humanoid%20Soccer%20via%20Privileged%20Representation%20Learnin.md) · [[机器人学习]]
- [Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models](items/Learning%20Safe%20Agent%20Behaviour%20from%20Human%20Preferences%20and%20Justifications%20via%20Worl.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Hy-Embodied-VLM-1.0: Efficient Physical-World Agents](items/Hy-Embodied-VLM-1.0%20Efficient%20Physical-World%20Agents.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Towards Spatial Supersensing in the Wild](items/Towards%20Spatial%20Supersensing%20in%20the%20Wild.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Flow-aware Optimal Navigation in Unsteady Flows through Reinforcement Learning](items/Flow-aware%20Optimal%20Navigation%20in%20Unsteady%20Flows%20through%20Reinforcement%20Learning.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation](items/Worlds%20in%20One%20Demo%20A%20Synthetic%20Data%20Engine%20for%20Learning%20Open-World%20Mobile%20Manipu.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence](items/Self%20in%20Space%20Benchmarking%20Self-Awareness%20and%20Spatial%20Cognition%20in%20UAV%20Embodied.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets](items/UniPhysGen%20Unified%20Physical%20Grounding%20for%20Simulation-Ready%203D%20Assets.md) · [[世界模型]] [[具身智能评测与基准]]
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](items/Learning%20Physics-Guided%20Residual%20Dynamics%20for%20Deformable%20Object%20Simulation.md) · [[智能体 Agent]] [[世界模型]]
- [Just-In-Time Scene Graph Growth: Combating Perceptual Saturation in Long-Horizon Robotics](items/Just-In-Time%20Scene%20Graph%20Growth%20Combating%20Perceptual%20Saturation%20in%20Long-Horizon.md) · [[智能体 Agent]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：270
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation
- 最高分论文发布时间：2026-07-15T09:55:45Z
- 主要技术对象分类：具身智能评测与基准 20、多模态基础模型 15、智能体 Agent 14、机器人学习 13、世界模型 11、视觉语言动作模型 VLA 8、Sim2Real 1
- 信息源错误：2

### 信息源错误

- OpenAI News: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>
- Hugging Face Blog: The read operation timed out

</details>
