---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-19
---

# 2026-08-19 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Q-Learning With World Models](items/Q-Learning%20With%20World%20Models.md) — On challenging manipulation benchmarks Robomimic and LIBERO, QWM significantly outperforms strong prior state-of-the-art methods on both sample efficiency and performance.

- **规模**：2252 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 20、多模态基础模型 16、机器人学习 12、视觉语言动作模型 VLA 12、智能体 Agent 9、世界模型 8、Sim2Real 2
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Q-Learning With World Models](items/Q-Learning%20With%20World%20Models.md)

- **创新点 / 方法**：We propose QWM, a framework that leverages world models to perform test-time search over imagined trajectories on top of Q-learning to select high-value actions during both online rollouts and evaluation.
- **证据**：On challenging manipulation benchmarks Robomimic and LIBERO, QWM significantly outperforms strong prior state-of-the-art methods on both sample efficiency and performance.

### 2. [Teach and Grow: An Agent-Centered Architecture for General Robot Learning](items/Teach%20and%20Grow%20An%20Agent-Centered%20Architecture%20for%20General%20Robot%20Learning.md)

- **创新点 / 方法**：We present Teach-and-Grow Learning (TGL), an agent-centered architecture for general robot learning.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 3. [PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing](items/PRISM%20Precision%20and%20contact-rich%20Real-world%20Industrial%20Skill%20dataset%20with%20Multim.md)

- **创新点 / 方法**：To address this gap, we introduce PRISM, a large-scale multimodal dataset for contact-rich industrial operations.
- **证据**：However, most existing datasets emphasize short-horizon, low-contact tasks such as pick-and-place, and therefore do not capture the precision control, force/torque or tactile regulation, and multimodal feedback required for industrial assembly.

### 4. [CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation](items/CompCPZ%20Preserving%20Multi-Modal%20Intent%20in%20Language-Guided%20Robot%20Manipulation.md)

- **创新点 / 方法**：A robot asked to "place the cup near the red plate or the blue plate" may reach the centroid between them and appear geometrically successful, while satisfying neither disjunct of the instruction.
- **证据**：On a closed-loop ManiSkill3 tabletop-manipulation benchmark, CompCPZ outperforms convex set baselines, multi-peak decoders, and a zero-shot vision-language-action model (1,900/1,918 paired wins, p << 10^(-30)); the same compiler also transfers without retuning to planar real-robot trials on a Unitree Go2 quadruped und…

### 5. [Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies](items/Reuse%20Before%20You%20Retrieve%20Diagnosing%20Headroom%20and%20Complementarity%20for%20Test-Time.md)

- **创新点 / 方法**：Frozen vision-language-action (VLA) policies are increasingly improved at test time by sampling additional policy behaviors or introducing external demonstrations.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups](items/Prism-GRPO%20Faster%20VLA%20Policy%20Optimization%20via%20Splitting%20Same-outcome%20Groups.md) — Across four RoboTwin tasks spanning different horizons and coordination patterns, Prism-GRPO improves success and quality at matched rollout budgets and reaches target success rates with up to 56% fewer rollouts.
- [PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents](items/PROBE%20Manipulation-Grounded%20Visual%20Question%20Answering%20with%20VLM%20Agents.md) — We observe consistent trend across all frontier VLMs: agentic tool-based methods outperform their perception-only baselines (8.0% on average) across all task types.
- [Inference-Time Attention Steering for Vision-Language-Action Driving Models](items/Inference-Time%20Attention%20Steering%20for%20Vision-Language-Action%20Driving%20Models.md) — We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone.
- [FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences](items/FetchMan%20Learning%20Visual%20Humanoid%20Loco-Manipulation%20Policies%20from%20Simulated%20Expe.md) — Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research.
- [LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models](items/LIBERO-VIFO%20Benchmarking%20the%20Capability%20and%20Safety%20of%20Visual%20Cue%20Following%20in%20Vi.md) — To address these gaps, we introduce LIBERO-VIFO, a benchmark to evaluate both the capability and safety of visual cue following in VLA models.
- [EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](items/EATR-Stereo%20Embodiment-Aware%20Routing%20of%20Paired%20Stereo%20Evidence%20for%20Humanoid%20Visi.md) — EATR-Stereo achieves 60.0% full-task success, 100.0% grasp success, and 80.0% stage success.
- [MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation](items/MANIGUARD%20A%20Benchmark%20and%20Data%20Suite%20for%20Specification-Grounded%20Safety%20Evaluatio.md) — We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline.

## 其余存档 12 篇

- [Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning](items/Repetition%20as%20Reinforcement%20Enhancing%20Sample%20Efficiency%20via%20Instant%20Episode%20Repe.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction](items/HODAgent%20Towards%20On-Demand%2C%20Responsive%20Humanoids%20for%20Physical%20World%20Human%20Intera.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving](items/Plug-and-Play%20Traffic%20Element%20Awareness%20for%20End-to-End%20Autonomous%20Driving.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields](items/Calibrated%20Predictive%20Safety%20for%20Heterogeneous%20Robots%20An%20Action-Conditioned%20JEPA.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [HiPHI: A Large-Scale Benchmark for High-Precision Human Motion and Object-Interaction](items/HiPHI%20A%20Large-Scale%20Benchmark%20for%20High-Precision%20Human%20Motion%20and%20Object-Interac.md) · [[具身智能评测与基准]]
- [RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing](items/RoboStriker%20Latent-Space%20Strategic%20Games%20for%20Autonomous%20Humanoid%20Boxing.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects](items/OVIP-SG%20Open-Vocabulary%20Instance-Preserving%20Scene%20Graphs%20for%20Mapping%20and%20Retriev.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [Scalix: Uncertainty-Aware Scale-Consistent Monocular SLAM](items/Scalix%20Uncertainty-Aware%20Scale-Consistent%20Monocular%20SLAM.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback](items/ORPA%20Online%20Residual%20Policy%20Adaptation%20for%20Robot%20Manipulation%20Control%20with%20Human.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Exposing the Long-tail in Embodied Urban Navigation via Scalable Learning from In-the-Wild Videos](items/Exposing%20the%20Long-tail%20in%20Embodied%20Urban%20Navigation%20via%20Scalable%20Learning%20from%20I.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS](items/Beyond%20Similarity%20Matching%20Structured%20Reasoning%20for%20Open-Vocabulary%20Referring%20Se.md) · [[具身智能评测与基准]]
- [Pre-training Visual Dexterity in Simulation](items/Pre-training%20Visual%20Dexterity%20in%20Simulation.md) · [[世界模型]] [[机器人学习]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2252
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Q-Learning With World Models
- 最高分论文发布时间：2026-08-17T22:00:42Z
- 主要技术对象分类：具身智能评测与基准 20、多模态基础模型 16、机器人学习 12、视觉语言动作模型 VLA 12、智能体 Agent 9、世界模型 8、Sim2Real 2
- 信息源错误：0
- 自动恢复信息源：0

</details>
