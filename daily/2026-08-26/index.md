---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-26
---

# 2026-08-26 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation](items/Pointing-VLA%20Typed%20Spatial%20Grounding%20Interfaces%20for%20Vision-Language-Action%20Manip.md) — Pointing-VLA achieves SOTA performance on Bridge/WidowX, averaging 72.9\% across the evaluated four-task set without Bridge-specific finetuning under collision-enabled CuRobo execution.

- **规模**：1110 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、多模态基础模型 14、视觉语言动作模型 VLA 13、机器人学习 11、智能体 Agent 10、世界模型 9、Sim2Real 1
- **源异常**：2
- **需要更高精度**：从“必读”选择论文，进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation](items/Pointing-VLA%20Typed%20Spatial%20Grounding%20Interfaces%20for%20Vision-Language-Action%20Manip.md)

- **创新点 / 方法**：We present Pointing-VLA, a typed hidden-state spatial readout built on Embodied-R1.
- **证据**：Pointing-VLA achieves SOTA performance on Bridge/WidowX, averaging 72.9\% across the evaluated four-task set without Bridge-specific finetuning under collision-enabled CuRobo execution.

### 2. [InstructMove: A Text-Indispensable Benchmark for Instruction-Following Manipulation](items/InstructMove%20A%20Text-Indispensable%20Benchmark%20for%20Instruction-Following%20Manipulati.md)

- **创新点 / 方法**：We introduce InstructMove, a text-indispensable benchmark for instruction-following manipulation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 3. [TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks](items/TrAct%20Bridging%20Robot%20Control%20and%20Visual%20Prediction%20with%20Visual%20Tracks.md)

- **创新点 / 方法**：Building on this observation, we propose TrAct, a world-model-based robot decision-making framework that uses visual tracks as an intermediate interface between control and prediction.
- **证据**：Experiments on the proposed LIBERO-INTEGRAL benchmark and real-world Franka manipulation show that TrAct improves success rates from 27% to 55% in simulation and from 49% to 76% on real-world tasks compared with the strong VLA baseline $π_{0.5}$.

### 4. [Hierarchical Skill Retrieval for Data-Efficient Adaptation of Vision-Language-Action Models](items/Hierarchical%20Skill%20Retrieval%20for%20Data-Efficient%20Adaptation%20of%20Vision-Language-Ac.md)

- **创新点 / 方法**：To address this challenge, we propose Hierarchical Skill Retrieval (HSR), a retrieval framework for data-efficient VLA adaptation.
- **证据**：Experiments on the LIBERO benchmark and several real-world robot manipulation tasks show that HSR improves the average success rate by 10.3% and 21.3% over the strongest baseline, respectively.

### 5. [Act with Intent: Distilling Behavior Intent for Vision-Language-Action Models](items/Act%20with%20Intent%20Distilling%20Behavior%20Intent%20for%20Vision-Language-Action%20Models.md)

- **创新点 / 方法**：We propose Intention Distillation (INDI), which distills behavior-level intent into the action decoder.
- **证据**：On SimplerEnv-Bridge, INDI improves GR00T-N1.7 from 64.3% to 84.7%, and on RoboCasa Kitchen it improves the controlled GR00T-N1.7 baseline from 64.1% to 70.3%, with consistent gains on $π_{0.5}$ across both benchmarks.

## 扫读 7 篇

- [Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency](items/Learning%20to%20Act%20While%20Waiting%20RL%20Finetuning%20of%20Generalist%20Robot%20Policies%20Under%20I.md) — In this work, we introduce a latency-aware framework, Asynchronous RL with Intermediate Information (ARLI), that enables RL-based improvement of generalist policies under inference delays.
- [Enhancing Sim2Real Transfer for Torque-Controlled Robots through Real2Sim Dynamics Estimation and Reinforcement Learning](items/Enhancing%20Sim2Real%20Transfer%20for%20Torque-Controlled%20Robots%20through%20Real2Sim%20Dynami.md) — Our results demonstrate a significant improvement in tracking accuracy and policy robustness after parameter tuning, with smooth policy transfer from simulation to the Real-World across multiple target-reaching tasks.
- [SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation](items/SuperMap%20A%20Spatio-Temporal%20SLAM%20System%20for%20Visual-Language%20Navigation.md) — SuperMap produces a queryable 4D scene-graph representation that interfaces naturally with Vision-Language Models by supporting compositional queries over object semantics, relations, We demonstrate SuperMap on benchmarks and real robots, including dynamic sc…
- [Gripper-aware Vision Language Action Models](items/Gripper-aware%20Vision%20Language%20Action%20Models.md) — Intensive experiments in both simulation and real-world robots show that our GVLA outperforms the current baselines across evaluated settings.
- [Triplet2Track: A Hierarchical System with Object-Centric Representations for Reliable Long-Horizon Manipulation](items/Triplet2Track%20A%20Hierarchical%20System%20with%20Object-Centric%20Representations%20for%20Reli.md) — Across diverse real-world long-horizon tasks, TTS achieves a 74.8\% average success rate and supports object-level and compositional generalization.
- [Fiber Optic Sensing Glove for High Performance Dexterous Manipulation Capture](items/Fiber%20Optic%20Sensing%20Glove%20for%20High%20Performance%20Dexterous%20Manipulation%20Capture.md) — Benchmarked on a 2-hour dataset of dexterous object manipulation tasks across 5 subjects, the glove achieves 7.2 mm mean fingertip position error against motion capture ground truth, reduced to 4.9 mm by a one-time factory calibration of the fiber routing hub…
- [PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control](items/PonderPounce%20A%20Pretrained%20MLLM%20as%20an%20Episode%20Context%20Engine%20for%20Robot%20Control.md) — Optimized serving achieves p50 latencies of 78ms for cognition refresh and 25ms for action-model invocation, supporting 20Hz action playback.

## 其余存档 12 篇

- [OmniCAD: A Large-Scale Benchmark for 3D Spatial Reasoning in Robotics Assemblies](items/OmniCAD%20A%20Large-Scale%20Benchmark%20for%203D%20Spatial%20Reasoning%20in%20Robotics%20Assemblies.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms](items/From%20Seeing%20to%20Acting%20Smart%20Glasses%20as%20First-Person%20Intelligence%20Platforms.md) · 多模态基础模型 具身智能评测与基准
- [ROS2SmolVLA: Enabling Small Vision-Language-Action Models for Integration into Industrial-Grade Lightweight Robots](items/ROS2SmolVLA%20Enabling%20Small%20Vision-Language-Action%20Models%20for%20Integration%20into%20In.md) · 多模态基础模型 视觉语言动作模型 VLA
- [Budget-Constrained Embodied Perception: Four Resource Walls and a Pre-Registered Evaluation of Access-Structured Perception on Open Models at less than 31B](items/Budget-Constrained%20Embodied%20Perception%20Four%20Resource%20Walls%20and%20a%20Pre-Registered.md) · 多模态基础模型 智能体 Agent 具身智能评测与基准
- [MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks](items/MobilePA-Bench%20Benchmarking%20Mobile%20Planner%20Agents%20on%20Complex%20Real-World%20Tasks.md) · 智能体 Agent 机器人学习 具身智能评测与基准
- [GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](items/GaussianWAM%20Distilling%20Geometry%20and%20Semantics%20from%203D%20Gaussian%20Fields%20into%20World.md) · 多模态基础模型 世界模型 视觉语言动作模型 VLA
- [DreamLedger: Execution-Settled Credit Files for World-Model Imagination in Robot Decision Loops](items/DreamLedger%20Execution-Settled%20Credit%20Files%20for%20World-Model%20Imagination%20in%20Robot.md) · 智能体 Agent 具身智能评测与基准
- [Reward-Free Continual Adaptation for Resilient Space Robots](items/Reward-Free%20Continual%20Adaptation%20for%20Resilient%20Space%20Robots.md) · 智能体 Agent 世界模型 机器人学习
- [Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation](items/Think%20Only%20When%20Needed%20Prompt-Authority%20Control%20for%20Selective%20Slow-Path%20Interven.md) · 多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- [Macro-Action Topological Navigation under Noisy Localization using Reinforcement Learning](items/Macro-Action%20Topological%20Navigation%20under%20Noisy%20Localization%20using%20Reinforcement.md) · 智能体 Agent 机器人学习 具身智能评测与基准
- [UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models](items/UniMem%20Unifying%20Multimodal%20Memory%20and%20Control%20for%20Vision-Language-Action%20Models.md) · 多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [Physics Filtering Favors the Generalization of Robot Learning](items/Physics%20Filtering%20Favors%20the%20Generalization%20of%20Robot%20Learning.md) · 世界模型 机器人学习

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：1110
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation
- 最高分论文发布时间：2026-08-24T11:43:49Z
- 主要技术对象分类：具身智能评测与基准 16、多模态基础模型 14、视觉语言动作模型 VLA 13、机器人学习 11、智能体 Agent 10、世界模型 9、Sim2Real 1
- 信息源错误：2
- 自动恢复信息源：0

### 信息源错误

- OpenAI News: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)
- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
