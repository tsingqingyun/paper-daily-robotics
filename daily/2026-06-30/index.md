---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-30
---

# 2026-06-30 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision](items/Training%20Vision-Language-Action%20Models%20with%20Dense%20Embodied%20Chain-of-Thought%20Supe.md) — Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment representations within the vision-language model (VLM).

- **规模**：2105 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、多模态基础模型 15、智能体 Agent 12、视觉语言动作模型 VLA 10、机器人学习 9、世界模型 8、Sim2Real 2
- **源异常**：0

## 必读 5 篇

### 1. [Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision](items/Training%20Vision-Language-Action%20Models%20with%20Dense%20Embodied%20Chain-of-Thought%20Supe.md)

- **创新点 / 方法**：Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment representations within the vision-language model (VLM).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [Vision-Language-Action Models: Experimental Insights from a Real-World UR5 Platform](items/Vision-Language-Action%20Models%20Experimental%20Insights%20from%20a%20Real-World%20UR5%20Platfo.md)

- **创新点 / 方法**：This project investigates whether recent Vision-Language-Action (VLA) models can be transferred from controlled research benchmarks to a real-world robotic platform, specifically a UR5e manipulator, in a reproducible and operationally meaningful manner.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 3. [Event-VLA: Action-Conditioned Event Fusion for Robust Vision-Language-Action Model](items/Event-VLA%20Action-Conditioned%20Event%20Fusion%20for%20Robust%20Vision-Language-Action%20Mode.md)

- **创新点 / 方法**：To address this gap, we propose \textbf{Event-VLA}, an event-enhanced VLA framework for generalizable manipulation across varying illumination conditions.
- **证据**：Experiments in simulation and real-world deployment show that Event-VLA maintains strong manipulation performance under normal lighting and improves success rates under low-light degradation and near-dark real-world settings.

### 4. [SurgVLA-Bench: Towards Evaluating Vision-Language-Action Models for Laparoscopic Surgical Robotics](items/SurgVLA-Bench%20Towards%20Evaluating%20Vision-Language-Action%20Models%20for%20Laparoscopic.md)

- **创新点 / 方法**：To address this limitation, we present SurgVLA-Bench, the first comprehensive benchmark for evaluating VLA models in laparoscopic surgical robotics.
- **证据**：Leveraging the SurRoL simulation platform, we construct a hierarchical task taxonomy ranging from atomic actions to complete surgical procedures, complemented by a multi- dimensional evaluation framework assessing action accuracy and semantic consistency.

### 5. [Sequential Planning via Anchored Robotic Keypoints](items/Sequential%20Planning%20via%20Anchored%20Robotic%20Keypoints.md)

- **创新点 / 方法**：We present Sequential Planning via Anchored Robotic Keypoints, SPARK, a training-free neurosymbolic manipulation system that reaches 43.7% on six LIBERO-PRO position \& task cells, more than doubling CaP-Agent0 and Vision-Language-Action (VLA) baselines.
- **证据**：CaP- Agent0, a multi-turn code-generation agent, achieves 18.2% by re-querying an LLM at every turn, but its restart-from-scratch solution proves costly against minor policy failures.

## 扫读 7 篇

- [SA-VLA: State-aware tokenizer for improving Vision-Language-Action Models' performance](items/SA-VLA%20State-aware%20tokenizer%20for%20improving%20Vision-Language-Action%20Models%27%20perfor.md) — On 12 RoboTwin manipulation tasks, SA-VLA improves the average success rate from 0.29 to 0.56 over the strongest tokenizer baseline.
- [Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models](items/Trust%20Your%20Instincts%20Confidence-Driven%20Test-Time%20RL%20for%20Vision-Language-Action%20M.md) — Extensive experiments on the LIBERO and RoboTwin benchmarks show that T^2VLA consistently outperforms supervised baselines and approaches oracle RL performance with ground-truth rewards, achieving effective improvement without external reward feedback.
- [OP3DSG: Open-Vocabulary Part-Aware 3D Scene Graph Generation for Real-World Environments](items/OP3DSG%20Open-Vocabulary%20Part-Aware%203D%20Scene%20Graph%20Generation%20for%20Real-World%20Envir.md) — Experimental results show that OP3DSG achieves state-of-the-art performance and demonstrates its effectiveness as a perception backbone in diverse real- world robotics tasks.
- [RoamFlow: Reinforcement-Aligned One-Step Action MeanFlow Policy for Image-Goal Navigation](items/RoamFlow%20Reinforcement-Aligned%20One-Step%20Action%20MeanFlow%20Policy%20for%20Image-Goal%20Na.md) — Extensive experiments in both Habitat simulation and real-world robotic platforms demonstrate that RoamFlow achieves efficient inference while maintaining strong navigation performance under real- time constraints.
- [Chronos: A Physics-Informed Full-History Framework for Non-Markovian Long-Horizon Manipulation](items/Chronos%20A%20Physics-Informed%20Full-History%20Framework%20for%20Non-Markovian%20Long-Horizon.md) — Across 16 simulated tasks and 4 real-world experiments, Chronos is evaluated on precision insertion, general manipulation, and memory-dependent long- horizon control.
- [OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action Generation Model](items/OpenSPM%20An%20Environment-Transferable%20Robotic%20Key%20Spatial%20Pose%20Memory%20and%20Closed-L.md) — Evaluated on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3 Hz, while requiring minimal inference AI computing power.
- [RoAd-RL: A Unified Library and Benchmark for Robust Adversarial Reinforcement Learning](items/RoAd-RL%20A%20Unified%20Library%20and%20Benchmark%20for%20Robust%20Adversarial%20Reinforcement%20Lea.md) — Results reveal substantial variations in robustness across environments and show that some commonly used defenses can be more detrimental than the attacks they aim to mitigate, while temporal smoothing consistently achieves strong performance.

## 其余存档 12 篇

- [Learning Transferable Dynamics Priors from Action to World Modeling](items/Learning%20Transferable%20Dynamics%20Priors%20from%20Action%20to%20World%20Modeling.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Enhancing Part-Level Point Grounding for Any Open-Source MLLMs](items/Enhancing%20Part-Level%20Point%20Grounding%20for%20Any%20Open-Source%20MLLMs.md) · [[多模态基础模型]]
- [Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing](items/Goku%20A%20Million-Scale%20Universal%20Dataset%20and%20Benchmark%20for%20Instruction-Based%20Video.md) · [[具身智能评测与基准]]
- [UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image](items/UnfoldArt%20Zero-Shot%20Recovery%20of%20Full%20Articulated%203D%20Objects%20from%20Text%20or%20Image.md) · [[多模态基础模型]] [[智能体 Agent]]
- [Grasp-Oriented Non-Prehensile Manipulation via Learning a Graspability Field](items/Grasp-Oriented%20Non-Prehensile%20Manipulation%20via%20Learning%20a%20Graspability%20Field.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [HUMEMBR: Learning Human Routines for Predictive Embodied Navigation](items/HUMEMBR%20Learning%20Human%20Routines%20for%20Predictive%20Embodied%20Navigation.md) · [[智能体 Agent]]
- [Automating the Design of Embodied AgentArchitectures](items/Automating%20the%20Design%20of%20Embodied%20AgentArchitectures.md) · [[多模态基础模型]] [[智能体 Agent]]
- [CORE: Common Outcome Regularities from Action-Free Visual Demonstrations for Robot Manipulation](items/CORE%20Common%20Outcome%20Regularities%20from%20Action-Free%20Visual%20Demonstrations%20for%20Robo.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Behavior Uncloning: Distilling Mode Redirection into Policy Weights without Inference-Time Steering](items/Behavior%20Uncloning%20Distilling%20Mode%20Redirection%20into%20Policy%20Weights%20without%20Infer.md) · [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [Analytic Concept-Centric Memory for Agentic Embodied Manipulation](items/Analytic%20Concept-Centric%20Memory%20for%20Agentic%20Embodied%20Manipulation.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [GROW$^2$: Grounding Which and Where for Robot Tool Use](items/GROW%24%202%24%20Grounding%20Which%20and%20Where%20for%20Robot%20Tool%20Use.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [OmniCoT: A Benchmark for Global and Multi-Step Panoramic Reasoning](items/OmniCoT%20A%20Benchmark%20for%20Global%20and%20Multi-Step%20Panoramic%20Reasoning.md) · [[多模态基础模型]] [[Sim2Real]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2105
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision
- 最高分论文发布时间：2026-06-29T16:48:48Z
- 主要技术对象分类：具身智能评测与基准 17、多模态基础模型 15、智能体 Agent 12、视觉语言动作模型 VLA 10、机器人学习 9、世界模型 8、Sim2Real 2
- 信息源错误：0

</details>
