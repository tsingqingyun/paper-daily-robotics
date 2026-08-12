---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-19
---

# 2026-06-19 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](items/SC3-Eval%20Evaluating%20Robot%20Foundation%20Models%20via%20Self-Consistent%20Video%20Generation.md) — Across seven real-world vision-language-action policies, SC3-Eval attains a closed-loop Pearson correlation of $0.929$ and MMRV of $0.119$, outperforming three strong prior video-model-based baselines, and generalizes to new tasks.

- **规模**：2085 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 20、多模态基础模型 16、世界模型 12、智能体 Agent 11、视觉语言动作模型 VLA 10、机器人学习 6、Sim2Real 3
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](items/SC3-Eval%20Evaluating%20Robot%20Foundation%20Models%20via%20Self-Consistent%20Video%20Generation.md)

- **创新点 / 方法**：Action-conditioned video world models offer a scalable alternative by simulating policy rollouts.
- **证据**：Across seven real-world vision-language-action policies, SC3-Eval attains a closed-loop Pearson correlation of $0.929$ and MMRV of $0.119$, outperforming three strong prior video-model-based baselines, and generalizes to new tasks.

### 2. [Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](items/Qwen-RobotManip%20Technical%20Report%20Alignment%20Unlocks%20Scale%20for%20Robotic%20Manipulatio.md)

- **创新点 / 方法**：We present Qwen- RobotManip, a generalizable Vision-Language-Action foundation model built on Qwen-VL.
- **证据**：Qwen-RobotManip substantially outperforms prior state-of-the-art models, including $π$0.5, across all OOD settings, ranks 1st in RoboChallenge with a 20% relative improvement, and is validated on real- robot platforms including AgileX ALOHA, Franka, UR, and ARX.

### 3. [Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos](items/Motion-Focused%20Latent%20Action%20Enables%20Cross-Embodiment%20VLA%20Training%20from%20Human%20Eg.md)

- **创新点 / 方法**：To address this, we propose a latent-action-based framework designed to extract general action priors from unlabeled human videos.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models](items/Does%20VLA%20Even%20Know%20the%20Basics%20Measuring%20Commonsense%20and%20World%20Knowledge%20Retentio.md)

- **创新点 / 方法**：We introduce Act2Answer, a lightweight protocol that adapts VLM knowledge benchmarks to VLA evaluation by requiring agents to answer through action.
- **证据**：Each question becomes a short tabletop episode where the agent performs a single object-placement action to select among candidate answers, yielding an action-grounded success rate with reduced control confounds.

### 5. [Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](items/Object-Centric%20Residual%20RL%20for%20Zero-Shot%20Sim-to-Real%20VLA%20Enhancement.md)

- **创新点 / 方法**：We propose an object- centric residual RL framework that refines VLA actions using object poses, enabling a compact observation space that transfers consistently between simulation and reality.
- **证据**：Across five manipulation tasks on a real Franka Research 3 (FR3) robot, our method improves the success rate from 42% to 76% zero-shot, and the improved rollouts can be further reused to retrain the base VLA for self-improvement without additional teleoperation.

## 扫读 7 篇

- [Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation](items/Invertible%20Neural%20Network%20Adapter%20for%20One-Step%20Flow%20Matching%20in%20Robot%20Manipulati.md) — Compared with conventional iterative flow- matching policies, the proposed framework substantially reduces inference complexity while maintaining strong action prediction accuracy and stability.
- [ROBOSHACKLES: A Safety Dataset for Human-Injury Prevention in Embodied Foundation Models](items/ROBOSHACKLES%20A%20Safety%20Dataset%20for%20Human-Injury%20Prevention%20in%20Embodied%20Foundation.md) — Results show that all evaluated models produce unsafe actions in the tested safety-critical scenarios, yielding a 100% unsafe action generation rate.
- [DREAM-Chunk: Reactive Action Chunking with Latent World Model](items/DREAM-Chunk%20Reactive%20Action%20Chunking%20with%20Latent%20World%20Model.md) — On the Kinetix benchmark, DREAM-Chunk improves robustness under increasing action noise and benefits from larger candidate sample sizes, especially when demonstrations contain corrective behaviors.
- [Guava: An Effective and Universal Harness for Embodied Manipulation](items/Guava%20An%20Effective%20and%20Universal%20Harness%20for%20Embodied%20Manipulation.md) — In this work, we present Guava, a harness framework for embodied tool use developed through systematic exploration of the design space of agent workflows, action spaces, and observation spaces.
- [A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks](items/A%20Scalable%20Embodied%20Intelligence%20Platform%20for%20Seamless%20Real-to-Sim-to-Real%20Trans.md) — To address these challenges, we develop BestMan, a scalable and seamless real-to-sim-to-real platform that bridges the gap between the simulation and the real world, enabling effective strategy development, integration, and deployment for household mobile man…
- [EffiNav: Fusing Depth and Vision-Language for Efficient Object Goal Navigation](items/EffiNav%20Fusing%20Depth%20and%20Vision-Language%20for%20Efficient%20Object%20Goal%20Navigation.md) — Across two standard metrics--Success Rate (SR) and Success weighted by Path Length (SPL), EffiNav matches or outperforms recent baselines, reflecting its efficiency, robustness, and practical applicability.
- [PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation](items/PAIWorld%20A%203D-Consistent%20World%20Foundation%20Model%20for%20Robotic%20Manipulation.md) — Built upon a DiT-based world foundation model, PAIWorld achieves state-of-the-art multi-view 3D consistency on robotic manipulation benchmarks, ranking 1st on the WorldArena leaderboard and 2nd on the AgiBot-Challenge2026 leaderboard, while enabling downstrea…

## 其余存档 12 篇

- [Benchmarking Action Spaces in Reinforcement Learning for Vision-based Robotic Manipulation](items/Benchmarking%20Action%20Spaces%20in%20Reinforcement%20Learning%20for%20Vision-based%20Robotic%20Ma.md) · [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- [ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI](items/ERQA-Plus%20A%20Diagnostic%20Benchmark%20for%20Reasoning%20in%20Embodied%20AI.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Monocular 3D Occupancy Perception for Robots on Sidewalks via Hybrid 2D-3D Learning](items/Monocular%203D%20Occupancy%20Perception%20for%20Robots%20on%20Sidewalks%20via%20Hybrid%202D-3D%20Learn.md) · [[具身智能评测与基准]]
- [VEGA: Learning Navigation VLAs from In-the-Wild Egocentric Video with Geometric Trajectory Supervision](items/VEGA%20Learning%20Navigation%20VLAs%20from%20In-the-Wild%20Egocentric%20Video%20with%20Geometric%20T.md) · [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [A Mixed-Reality Testbed for Autonomous Vehicles](items/A%20Mixed-Reality%20Testbed%20for%20Autonomous%20Vehicles.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [HT-Bench: Benchmarking and Learning Dexterous Full-Hand Tactile Representations with Egocentric Vision](items/HT-Bench%20Benchmarking%20and%20Learning%20Dexterous%20Full-Hand%20Tactile%20Representations%20w.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [ReSiReg: Towards Spatially Consistent Semantics in Language-Conditioned Robotic Tasks](items/ReSiReg%20Towards%20Spatially%20Consistent%20Semantics%20in%20Language-Conditioned%20Robotic%20T.md) · [[多模态基础模型]]
- [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](items/Mem-World%20Memory-Augmented%20Action-Conditioned%20World%20Models%20for%20Persistent%20Robot.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization](items/MoonSplat%20Monocular%20Online%20Gaussian%20Splatting%20with%20Sim%283%29%20Global%20Optimization.md) · [[具身智能评测与基准]]
- [HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations](items/HALOMI%20Learning%20Humanoid%20Loco-Manipulation%20with%20Active%20Perception%20from%20Human%20Dem.md) · [[机器人学习]] [[具身智能评测与基准]]
- [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](items/MolmoMotion%20Forecasting%20Point%20Trajectories%20in%203D%20with%20Language%20Instruction.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](items/Qwen-RobotNav%20Technical%20Report%20A%20Scalable%20Navigation%20Model%20Designed%20for%20an%20Agent.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2085
- 入选条目：24
- 回填已见条目：0
- 最高分论文：SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation
- 最高分论文发布时间：2026-06-17T02:15:46Z
- 主要技术对象分类：具身智能评测与基准 20、多模态基础模型 16、世界模型 12、智能体 Agent 11、视觉语言动作模型 VLA 10、机器人学习 6、Sim2Real 3
- 信息源错误：0

</details>
