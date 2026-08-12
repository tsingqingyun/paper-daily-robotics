---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-22
---

# 2026-07-22 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](items/Agentic%20Real2Sim%20Physics-based%20World%20Modeling%20with%20Vision-Language%20Agents.md) — The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate.

- **规模**：150 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、智能体 Agent 16、多模态基础模型 13、视觉语言动作模型 VLA 8、机器人学习 6、世界模型 4、AI 核心知识地图 1
- **源异常**：5
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](items/Agentic%20Real2Sim%20Physics-based%20World%20Modeling%20with%20Vision-Language%20Agents.md)

- **创新点 / 方法**：We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states.
- **证据**：The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate.

### 2. [RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation](items/RoboInter1.5%20A%20Holistic%20Intermediate%20Representation%20Suite%20for%20Embodied%20World%20Mod.md)

- **创新点 / 方法**：Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 3. [RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model](items/RynnBrain%201.1%20Towards%20More%20Capable%20and%20Generalizable%20Embodied%20Foundation%20Model.md)

- **创新点 / 方法**：We present RynnBrain 1.1, a family of embodied foundation models spanning 2B, 9B, and 122B-A10B scales.
- **证据**：RynnBrain 1.1 achieves strong results on embodied cognition, localization, and 3D grounding, with the 122B-A10B model outperforming all evaluated proprietary and open- source models on VSI-Bench, MMSI, and RefSpatial-Bench.

### 4. [WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory](items/WorldScape%20Policy%202.0%20Empowering%20Steerable%20World%20Action%20Modeling%20with%20Reasoning-.md)

- **创新点 / 方法**：In this paper, we introduce WorldScape Policy 2.0, a controllable WAM with reasoning-augmented long short-term memory.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [Patch Policy: Efficient Embodied Control via Dense Visual Representations](items/Patch%20Policy%20Efficient%20Embodied%20Control%20via%20Dense%20Visual%20Representations.md)

- **创新点 / 方法**：Across four simulated and three real- world environment suites, our method achieves a 40% relative improvement over policies using state-of-the-art global-pooled representations.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](items/Closing%20the%20Loop%20in%20Humanoid%20VLA%20Persistent%203D%20Object%20Tokens%20for%20Verifiable%20Loco.md) — On a Unitree G1, POT-VLA improves a matched direct GR00T-N1.7 baseline from 39/80 to 71/80 successes over eight real-world task families.
- [STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models](items/STeP%20Signal%20Temporal%20Logic%20for%20Precise%20Specifications%20for%20Action%20Generation%20with.md) — We evaluate the approach on a real- world tabletop domain, demonstrating how formal specifications can improve the precision, reliability, and interpretability of language-conditioned robot planning.
- [FARO: Feasibility-Aware Robot Motion Optimization](items/FARO%20Feasibility-Aware%20Robot%20Motion%20Optimization.md) — By integrating this module with a feasibility-guided tree search and a Large Language Model (LLM)-based contact plan sampling strategy, we demonstrate that the proposed framework can substantially improve the search process.
- [FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](items/FM-VLA%20Force-based%20Memory%20for%20Vision-Language-Action%20Models%20in%20Contact-Rich%20Mani.md) — Our lightweight force memory achieves over 80% success rate with minimal inference overhead, significantly outperforming baseline approaches.
- [Generalize and Guide: Decomposing Rewards for Few-Shot Inverse Reinforcement Learning](items/Generalize%20and%20Guide%20Decomposing%20Rewards%20for%20Few-Shot%20Inverse%20Reinforcement%20Lear.md) — We demonstrate the effectiveness of our method on multiple challenging navigation and manipulation tasks under significant variations (e.g., object configurations, table layouts, and initial robot poses), achieving an average success rate of 81.2%, outperform…
- [CDIS: Cross-Dimensional Class-Agnostic 3D Instance Segmentation via 2D Mask Tracking and 3D-2D Projection Merging](items/CDIS%20Cross-Dimensional%20Class-Agnostic%203D%20Instance%20Segmentation%20via%202D%20Mask%20Track.md) — Experiments on benchmark datasets demonstrate that CDIS achieves higher accuracy and consistency than state-of-the-art zero-shot methods, while remaining efficient and scalable to diverse real-world environments.
- [DA-Fusion: Deformable Attention-Based RGB-D Fusion Transformer for Unseen Object Instance Segmentation](items/DA-Fusion%20Deformable%20Attention-Based%20RGB-D%20Fusion%20Transformer%20for%20Unseen%20Object.md) — DA-Fusion effectively combines the strengths of both RGB and depth data, enhancing segmentation accuracy in cluttered and multi-layered object environments.

## 其余存档 12 篇

- [Athena-Brain Technical Report: An Efficient Robot Brain for General Intelligence and Embodied Interactio](items/Athena-Brain%20Technical%20Report%20An%20Efficient%20Robot%20Brain%20for%20General%20Intelligence.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [Engineering Trustworthy Agentic AI for Critical Systems](items/Engineering%20Trustworthy%20Agentic%20AI%20for%20Critical%20Systems.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation](items/MEVION%20Low-Cost%20Open-Source%20Data%20Collection%20System%20for%20Powerful%20and%20High-Speed%20D.md) · [[多模态基础模型]] [[机器人学习]]
- [COLIP-2: Olfaction-Vision-Language Embeddings](items/COLIP-2%20Olfaction-Vision-Language%20Embeddings.md) · [[多模态基础模型]]
- [Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security](items/Adaptive%20Adversaries%20A%20Multi-Turn%2C%20Multi-LLM%20Benchmark%20for%20LLM%20Agent%20Security.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](items/RoboHarness%20Memory-Driven%20Orchestration%20of%20Heterogeneous%20Robot%20Policies%20for%20Long.md) · [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Data Leakage Prevention in Agentic Applications via Preemptive Hardening](items/Data%20Leakage%20Prevention%20in%20Agentic%20Applications%20via%20Preemptive%20Hardening.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development](items/Do%20AI-Native%20Biotechs%20Need%20Departments%20Benchmarking%20Company%20World%20Models%20for%20AI-.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Two-Stage Extrinsic Calibration of a Static Line-Scanning Lidar with a Rotary Platform](items/Two-Stage%20Extrinsic%20Calibration%20of%20a%20Static%20Line-Scanning%20Lidar%20with%20a%20Rotary%20Pl.md) · [[AI 核心知识地图]]
- [UniETP: Unifying Environments for Generalizable Embodied Task Planning](items/UniETP%20Unifying%20Environments%20for%20Generalizable%20Embodied%20Task%20Planning.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model](items/PGN%20Design%20and%20Implementation%20of%20a%20Vision-Language%20Navigation%20System%20Based%20on%20Pa.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [SLAM in Low-Light Environments: Project Report](items/SLAM%20in%20Low-Light%20Environments%20Project%20Report.md) · [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：150
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents
- 最高分论文发布时间：2026-07-21T15:23:38Z
- 主要技术对象分类：具身智能评测与基准 16、智能体 Agent 16、多模态基础模型 13、视觉语言动作模型 VLA 8、机器人学习 6、世界模型 4、AI 核心知识地图 1
- 信息源错误：5

### 信息源错误

- OpenAI News: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>
- Google DeepMind Blog: The read operation timed out
- Hugging Face Blog: <urlopen error _ssl.c:1112: The handshake operation timed out>
- Microsoft Research Blog: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>
- MIT Technology Review AI: <urlopen error _ssl.c:1112: The handshake operation timed out>

</details>
