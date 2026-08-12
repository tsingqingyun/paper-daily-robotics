---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-15
---

# 2026-06-15 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation](items/ReactVLA%20Fast%20and%20Lightweight%20Reactive%20Robot%20Manipulation%20via%20Improved%20Mean%20Flow.md) — Experimental results show that \texttt{ReactVLA} consistently outperforms similarly sized VLA baselines, including SmolVLA and $π_0$.

- **规模**：2074 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、多模态基础模型 16、世界模型 13、智能体 Agent 11、机器人学习 10、视觉语言动作模型 VLA 10、Sim2Real 1
- **源异常**：0

## 必读 5 篇

### 1. [ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation](items/ReactVLA%20Fast%20and%20Lightweight%20Reactive%20Robot%20Manipulation%20via%20Improved%20Mean%20Flow.md)

- **创新点 / 方法**：To address this limitation, we propose \texttt{ReactVLA}, a lightweight and low-latency VLA framework for real-time robotic manipulation.
- **证据**：Experimental results show that \texttt{ReactVLA} consistently outperforms similarly sized VLA baselines, including SmolVLA and $π_0$.

### 2. [Self-Improving VLA Policies: Selected Diffusion Noise for Spurious-Robust Action Smoothing](items/Self-Improving%20VLA%20Policies%20Selected%20Diffusion%20Noise%20for%20Spurious-Robust%20Action.md)

- **创新点 / 方法**：We introduce Selected Diffusion Noise (SDN), a simple, training-free test-time method that improves both robustness and success rate by leveraging the diffusion noise space as a controllable degree of freedom.
- **证据**：SDN consistently improves success rates by +8% in simulation and +10% in real-world settings, while producing smoother and more stable actions.

### 3. [PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation](items/PhysVLA%20Towards%20Physically-Grounded%20VLA%20for%20Embodied%20Robotic%20Manipulation.md)

- **创新点 / 方法**：To bridge this gap, we introduce PhysVLA (Physics-VLA), a plug-and-play, inference-time framework designed to wrap any frozen VLA backbone without retraining, fine-tuning, or weight access, with less than 1 ms of overhead per control step.
- **证据**：Evaluated across OpenVLA, OpenVLA-OFT, Force-VLA, and Generalist-VLA on LIBERO-Spatial with a 7-DoF Franka Panda, the framework delivers absolute success rate increases of up to 17% and stability increases of up to 19% with no per-task regressions, improves trajectory efficiency by up to 15% across all four backbones…

### 4. [$μ_0$: A Scalable 3D Interaction-Trace World Model](items/%24%CE%BC_0%24%20A%20Scalable%203D%20Interaction-Trace%20World%20Model.md)

- **创新点 / 方法**：We present $μ_0$, a scalable world model based on 3D traces.
- **证据**：Experiments show that $μ_0$ outperforms baselines in both 2D and 3D trace prediction, including trace prediction models and tokenized VLM methods.

### 5. [Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack](items/Hy-Embodied-0.5-VLA%20From%20Vision-Language-Action%20Models%20to%20a%20Real-World%20Robot%20Lea.md)

- **创新点 / 方法**：In this report, we present Hy-Embodied-0.5-VLA, abbreviated as HyVLA-0.5, an end-to-end system that spans the full robot learning stack: data collection, model design, continued pre-training and supervised fine-tuning, RL post-training, and real-world deployment.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models](items/Elastic%20Queries%20Reinforcement%20Learning%20Self-Aware%20Policy%20Execution%20for%20VLA%20Model.md) — We propose Elastic Queries Reinforcement Learning (EQRL), a framework that makes each VLA policy query elastic.
- [Multi-Agent Embodied Autonomous Driving: From V2X Information Exchange to Shared World Models](items/Multi-Agent%20Embodied%20Autonomous%20Driving%20From%20V2X%20Information%20Exchange%20to%20Shared.md) — Autonomous driving is shifting from isolated vehicle intelligence toward multi-agent embodied systems that share perception, infer intent, and coordinate action under uncertainty.
- [InterleaveThinker: Reinforcing Agentic Interleaved Generation](items/InterleaveThinker%20Reinforcing%20Agentic%20Interleaved%20Generation.md) — On interleaved generation benchmarks, it achieves performance comparable to Nano Banana and GPT-5.
- [An Attention-based Model for Robust Forecasting with Missing Modality](items/An%20Attention-based%20Model%20for%20Robust%20Forecasting%20with%20Missing%20Modality.md) — We show that our proposed model can be trained with missing modalities while approximating a robust representation of all modalities.
- [ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation](items/ContactWorld%20What%20Matters%20in%20Vision-Tactile%20World%20Models%20for%20Contact-Rich%20Manipu.md) — In particular, point-cloud observations improve average planning success rates from 20.7% with wrist-view observations and 22.0% with front-view observations to 32.1%.
- [Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning](items/Output-Level%20Regularization%20Eliminates%20the%20Seed%20Lottery%20in%20Single-GPU%20VLA%20Fine-T.md) — There is a hidden danger.
- [Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions](items/Kine2Go%20Kinematic%20dataset%20for%20the%20Unitree%20Go2%20robot%20with%20diverse%20gaits%20and%20motio.md) — To aid in those kinds of efforts, we present Kine2Go - a dataset with 800 diverse gait kinematics trajectory motion data for the Unitree Go2 robot, derived from 40 distinct policies.

## 其余存档 12 篇

- [FloVerse: Floor Plan-Guided Multi-Modal Navigation](items/FloVerse%20Floor%20Plan-Guided%20Multi-Modal%20Navigation.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- [Improving Robotic Generalist Policies via Flow Reversal Steering](items/Improving%20Robotic%20Generalist%20Policies%20via%20Flow%20Reversal%20Steering.md) · [[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- [ORCA: A Platform for Open-Source Dexterity Research](items/ORCA%20A%20Platform%20for%20Open-Source%20Dexterity%20Research.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift](items/FlowMo-WM%20A%20World%20Model%20with%20Object%20Momentum%20and%20Hidden%20Ambient%20Drift.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [WAM4D: Fast 4D World Action Model via Spatial Register Tokens](items/WAM4D%20Fast%204D%20World%20Action%20Model%20via%20Spatial%20Register%20Tokens.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [TwinBI: An Agentic Digital Twin for Efficient Augmented Interactions with Business Intelligence Dashboards](items/TwinBI%20An%20Agentic%20Digital%20Twin%20for%20Efficient%20Augmented%20Interactions%20with%20Busines.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model](items/SIMMER%20Benchmarking%20Latent%20Failures%20in%20LLM%20Executable%20Planning%20with%20a%20World%20Mode.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [OdysSim: Building Foundation Models for Human Behavior Simulation](items/OdysSim%20Building%20Foundation%20Models%20for%20Human%20Behavior%20Simulation.md) · [[多模态基础模型]] [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs](items/When%20and%20How%20Severely%20Scenario-Specific%20Safety%20Envelopes%20for%20Driving%20VLAs.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving](items/ReactSim-Bench%20Benchmarking%20Reactive%20Behavior%20World%20Model%20Simulation%20in%20Autonomo.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [RT-VLA: Real-Time Vision-Language-Action Models via Knowledge Distillation](items/RT-VLA%20Real-Time%20Vision-Language-Action%20Models%20via%20Knowledge%20Distillation.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation](items/TRACE%20Trajectory-Routed%20Causal%20Memory%20for%20Delayed-Evidence%20Visuomotor%20Imitation.md) · [[智能体 Agent]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2074
- 入选条目：24
- 回填已见条目：0
- 最高分论文：ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation
- 最高分论文发布时间：2026-06-12T08:33:37Z
- 主要技术对象分类：具身智能评测与基准 16、多模态基础模型 16、世界模型 13、智能体 Agent 11、机器人学习 10、视觉语言动作模型 VLA 10、Sim2Real 1
- 信息源错误：0

</details>
