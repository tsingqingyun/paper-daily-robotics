---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
created: 2026-09-11
---

# 2026-09-11 AI Embodied Intelligence Update

> [!summary] 今日判断
> On the LIBERO benchmark, HaWMPO achieves the best average success rate, with gains of 15.0% over the base model and 2.8% over the strongest baseline; real-world experiments on a G1 robot further validate its effectiveness, raising the average success rate on…
> **趋势**：暂无可判断趋势。

- **规模**：2310 个候选 → 24 篇入选；回填 0 篇
- **主题**：世界模型 14、具身智能评测与基准 14、智能体 Agent 12、视觉语言动作模型 VLA 10、机器人学习 9、多模态基础模型 8、Sim2Real 4、AI 核心知识地图 1
- **源异常**：1
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy](items/HaWMPO%20Hallucination-Aware%20World%20Model-based%20Policy%20Optimization%20for%20Generalist.md)

> On the LIBERO benchmark, HaWMPO achieves the best average success rate, with gains of 15.0% over the base model and 2.8% over the strongest baseline; real-world experiments on a G1 robot further validate its effectiveness, raising the average success rate on…

- **为什么值得读**：需结合研究方向判断；规则式回退未做语义评审。
- **证据**：On the LIBERO benchmark, HaWMPO achieves the best average success rate, with gains of 15.0% over the base model and 2.8% over the strongest baseline; real-world experiments on a G1 robot further validate its effectiveness, raising the average success rate on two manipulation tasks from 67.5% to 80.0%.
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

### 2. [FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects](items/FolDeX%20A%20Physical-World%20Benchmark%20for%20Long-Horizon%20Robotic%20Manipulation%20of%20Defor.md)

> We introduce FolDeX, a physical-world benchmark built entirely from real-robot data, with garment folding as its primary task.

- **为什么值得读**：需结合研究方向判断；规则式回退未做语义评审。
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

### 3. [Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G](items/Modality-Decoupled%20Federated%20Learning%20for%20Privacy-Preserving%20Embodied%20Intelligen.md)

> A case study on federated robotic manipulation over the Third Generation Partnership Project (3GPP)-based wireless substrate, covering fading, co-channel interference, and malicious jamming, shows that FedMVLA achieves an 84.8% task success rate, exceeds FedA…

- **为什么值得读**：需结合研究方向判断；规则式回退未做语义评审。
- **证据**：A case study on federated robotic manipulation over the Third Generation Partnership Project (3GPP)-based wireless substrate, covering fading, co-channel interference, and malicious jamming, shows that FedMVLA achieves an 84.8% task success rate, exceeds FedAvg by 22.2 percentage points, sustains a widening margin whe…
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

### 4. [Show-Harness: Just a VLM Agent Can Play Robots](items/Show-Harness%20Just%20a%20VLM%20Agent%20Can%20Play%20Robots.md)

> Extensive experiments show that Show-Harness-equipped VLM agents generalize robustly across tasks, embodiments, and environments, outperforming representative agentic and VLA paradigms.

- **为什么值得读**：需结合研究方向判断；规则式回退未做语义评审。
- **证据**：Extensive experiments show that Show-Harness-equipped VLM agents generalize robustly across tasks, embodiments, and environments, outperforming representative agentic and VLA paradigms.
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

### 5. [Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration](items/Valerant%20An%20Automatic%20Navigable%20Game%20Map%20Generator%20via%20Action-Conditioned%20World.md)

> We present \textsc{Valerant}, a training-free framework that transforms a pretrained action-conditioned world model into a WAM for exploring and constructing 3D game maps.

- **为什么值得读**：需结合研究方向判断；规则式回退未做语义评审。
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 扫读 7 篇

- [DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation](items/DUET-DINO%20Simultaneous%20Cross-View%20World%20Modeling%20for%20Latent%20Planning%20in%20Robot%20Ma.md) — Across spatially diverse reach, orientation-intensive angled-reach, and multi-goal grasp-and-lift tasks, DUET-DINO consistently outperforms single-view and independent dual-view baselines, achieving 92% success on reach, 72.5% on angled-reach, and 60.0% on li…
- [GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](items/GTA-2%20A%20Multi-VLM%20Framework%20for%20Synthesizing%20Robot%20Manipulation%20Skills%20via%20Groun.md) — GTA-2 achieves an average zero-shot success rate of 73.9%, exceeding the strongest baseline by 31.4 percentage points, while targeted refinement raises GTA-2's average success rate to 90.7%.
- [Proxy Policy Steering](items/Proxy%20Policy%20Steering.md) — On 8 real-world and 4 simulation manipulation tasks, PPS lifts the state-of-the-art pi 0.5 base policy by 53% absolute success rate on average, with zero-to-one gains on tasks the base never solves, while preserving the base's broad capabilities.
- [Frequency-Conditioned Flow Matching for Vision-Language-Action Models](items/Frequency-Conditioned%20Flow%20Matching%20for%20Vision-Language-Action%20Models.md) — Across LIBERO, LIBERO-Plus, and VLA-Arena, FreqFM consistently improves performance, including a 9.3-point gain on LIBERO-Plus, and further demonstrates its effectiveness on six real-robot tasks.
- [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](items/Time-Frequency%20Geometric%20Cross-Attention%20for%20Chunked%20Vision-Language-Action%20Mode.md) — Relative to the same-source base, TFGCA improves in-distribution LIBERO by +1.5 on average, the OOD LIBERO-Plus by +6.3, the randomized average under RoboTwin domain randomization by +28.5, and the overall success rate on three real-robot AgiBot A2 tasks by +…
- [InstantMimic: A High Performance System for Learning Physics-based Skills in Seconds](items/InstantMimic%20A%20High%20Performance%20System%20for%20Learning%20Physics-based%20Skills%20in%20Seco.md) — We present InstantMimic, a system that addresses these inefficiencies by making the entire training loop GPU-native.
- [No Free Checker: A Survey of Verifiers for Robot Policies](items/No%20Free%20Checker%20A%20Survey%20of%20Verifiers%20for%20Robot%20Policies.md) — Verifiers range from success detectors and reward models to runtime monitors, safety filters, and temporal-logic specifications.

## 其余存档 12 篇

- [A Decade of Bayesian Optimization for Controller Tuning and Robot Learning: Tutorial, Review, and Future Prospects](items/A%20Decade%20of%20Bayesian%20Optimization%20for%20Controller%20Tuning%20and%20Robot%20Learning%20Tutor.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](items/Semigroup-JEPA%20Latent%20Dynamics%20Consistency%20for%20Zero-Shot%20Physics%20Generalization.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility](items/RoboDrop%20Curating%20VLA%20Post-Training%20Data%20via%20Local%20Gradient%20Compatibility.md) · [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [Compact Visuotactile World Models for Lifting: Prediction, Reward Alignment, and Force Constraints](items/Compact%20Visuotactile%20World%20Models%20for%20Lifting%20Prediction%2C%20Reward%20Alignment%2C%20and.md) · [[世界模型]]
- [Automatic Reproducible Camera Intrinsic Calibration](items/Automatic%20Reproducible%20Camera%20Intrinsic%20Calibration.md) · [[AI 核心知识地图]]
- [ViBe: Visual Behavior Adaptation for Perceptive Humanoid Whole-Body Control](items/ViBe%20Visual%20Behavior%20Adaptation%20for%20Perceptive%20Humanoid%20Whole-Body%20Control.md) · [[Sim2Real]]
- [PccDiffuser: Multi-solution Motion Planning for Continuum Robots](items/PccDiffuser%20Multi-solution%20Motion%20Planning%20for%20Continuum%20Robots.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [MuJoCable: Reduced-Order Surface-Routed Cable Transmission for Tendon-Driven Robots](items/MuJoCable%20Reduced-Order%20Surface-Routed%20Cable%20Transmission%20for%20Tendon-Driven%20Robo.md) · [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [PGMT: Perceptive General Motion Tracking for Humanoid Robots](items/PGMT%20Perceptive%20General%20Motion%20Tracking%20for%20Humanoid%20Robots.md) · [[机器人学习]]
- [Programmable World Model](items/Programmable%20World%20Model.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Adaptive Shared Control with Online Bounded-Rational Human Behavior Estimation](items/Adaptive%20Shared%20Control%20with%20Online%20Bounded-Rational%20Human%20Behavior%20Estimation.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Assembling Two Parts in One Hand](items/Assembling%20Two%20Parts%20in%20One%20Hand.md) · [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2310
- 入选条目：24
- 回填已见条目：0
- 最高分论文：HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy
- 最高分论文发布时间：2026-09-09T09:33:25Z
- 主要技术对象分类：世界模型 14、具身智能评测与基准 14、智能体 Agent 12、视觉语言动作模型 VLA 10、机器人学习 9、多模态基础模型 8、Sim2Real 4、AI 核心知识地图 1
- 信息源错误：1
- 自动恢复信息源：0

### 信息源错误

- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
