---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-16
---

# 2026-08-16 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](items/DreamX-Phi%201.0%20Action-Conditioned%20Video%20World%20Model%20for%20Robotic%20Manipulation.md) — At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge.

- **规模**：2241 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、智能体 Agent 10、世界模型 9、多模态基础模型 9、机器人学习 5、视觉语言动作模型 VLA 5、Sim2Real 2
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](items/DreamX-Phi%201.0%20Action-Conditioned%20Video%20World%20Model%20for%20Robotic%20Manipulation.md)

- **创新点 / 方法**：We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations.
- **证据**：At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge.

### 2. [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](items/MLLM-Routed%20Heterogeneous%20Ensembles%20for%20Robust%20Cross-Dataset%20Image%20Classificatio.md)

- **创新点 / 方法**：We propose ARMDIL, an Adaptive Router for Multi-Domain Image classification with LLMs.
- **证据**：Crucially, we show that ARMDIL effectively navigates these trade-offs, performing competitively with specialized training-based routers.

### 3. [FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving](items/FIRE-VLA%20Failure-Informed%20Self-Evolution%20for%20Vision-Language-Action%20Models%20in%20Au.md)

- **创新点 / 方法**：We introduce FIRE-VLA, a failure-informed self-evolution framework that converts such unresolved failures into privileged supervision for the next policy.
- **证据**：Reinforcement learning improves autonomous-driving vision-language-action (VLA) models by evaluating trajectories sampled from the current policy.

### 4. [NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation](items/NestDex%20Nested%20Policy%20Learning%20with%20Copilot%20Assisted%20Teleoperation%20for%20Dexterous.md)

- **创新点 / 方法**：We introduce NestDex, a nested policy-learning framework that reduces this burden by using learned hand skills to assist demonstration collection.
- **证据**：Across real-world dexterous manipulation experiments, NestDex improves demonstration reliability and efficiency, and the resulting empirical evaluations support effective autonomous policy learning.

### 5. [Adaptation of Generalist Robot Policies with Minimal Data](items/Adaptation%20of%20Generalist%20Robot%20Policies%20with%20Minimal%20Data.md)

- **创新点 / 方法**：We build MiDAS, a simple offline-to-online RL recipe that first anchors a pre-trained VLA to the target task with behavior cloning on single/few demonstrations, then improves it through value-based online RL on a residual policy parameterization.
- **证据**：Starting from a fragile low-success policy obtained from a single demonstration, MiDAS improves its robustness and learns new successful behaviors over ~6 hours of online interaction.

## 扫读 7 篇

- [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](items/XCoT-VLA%20Executable%20Chain-of-Thought%20for%20Vision-Language-Action%20Driving.md) — We propose XCoT-VLA, which replaces descriptive rationales with compact executable CoT tokens learned from automatically constructed Reason-Action supervision.
- [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](items/PlayWorld%20Benchmarking%20World%20Models%20with%20Agent%20Players%20over%20Long-Horizon%20Objecti.md) — Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective.
- [Deliberate Practice: Learning Robot Skills under a Budget](items/Deliberate%20Practice%20Learning%20Robot%20Skills%20under%20a%20Budget.md) — Through simulated and real-world experiments on long-horizon manipulation tasks, we show that our approach allows robots to optimally use limited practice time to acquire useful policies and improve long-horizon planning.
- [Reasoning for Social Audio-Visual Question Answering: Where Do We Stand?](items/Reasoning%20for%20Social%20Audio-Visual%20Question%20Answering%20Where%20Do%20We%20Stand.md) — A simple Vanilla SFT baseline matches or outperforms existing reasoning methods across three benchmarks at a fraction of the cost, establishing it as an essential baseline for evaluating novel fine-tuning techniques.
- [Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes](items/Semantic%20Radiance%20Fields%20as%20Simulators%20for%20Spatial%20Reasoning%20in%20Real-World%20Scene.md) — We propose using Semantic Radiance Fields (SRF) as simulators for spatial reasoning agents.
- [Learning Unified Video and Image Representation for Video Face Forgery Detection](items/Learning%20Unified%20Video%20and%20Image%20Representation%20for%20Video%20Face%20Forgery%20Detection.md) — Extensive experiments on benchmark datasets demonstrate the effectiveness of our framework, which outperforms state-of-theart methods in detecting partially forged videos while introducing no additional computational overhead.
- [RGB-D Video Generation for Improving Human-to-Robot Object Handover Prediction](items/RGB-D%20Video%20Generation%20for%20Improving%20Human-to-Robot%20Object%20Handover%20Prediction.md) — Experimental evaluations demonstrate that our framework achieves high intention identification accuracy and low false trigger rates in both ablation studies and real-world deployment on a physical robot platform.

## 其余存档 12 篇

- [Redistribution-based Cost Inference Improves Sparse Safe Offline RL](items/Redistribution-based%20Cost%20Inference%20Improves%20Sparse%20Safe%20Offline%20RL.md) · [[具身智能评测与基准]]
- [Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs](items/Map-Det3D%20Metric%20Feed-Forward%203D%20Reconstruction%20Prior%20for%20Multi-view%203D%20Object%20D.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Attention from Action, for Action: Emergent Visual Bottlenecks for Policy Learning](items/Attention%20from%20Action%2C%20for%20Action%20Emergent%20Visual%20Bottlenecks%20for%20Policy%20Learnin.md) · [[世界模型]] [[具身智能评测与基准]]
- [FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving](items/FlashDrive%20Flash%20Vision-Language-Action%20Inference%20for%20Autonomous%20Driving.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation](items/HounsWorld%20A%20Multimodal%20World%20Model%20for%20Hidden%20Patient-State%20Readout%2C%20Reconstruc.md) · [[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- [Error-Aware Reverse Auction Mechanism for Large Language Model Routing](items/Error-Aware%20Reverse%20Auction%20Mechanism%20for%20Large%20Language%20Model%20Routing.md) · [[世界模型]] [[具身智能评测与基准]]
- [FUSE: Active Functional Affordance Grounding through Adaptive Semantic-Geometric Evidence Acquisition](items/FUSE%20Active%20Functional%20Affordance%20Grounding%20through%20Adaptive%20Semantic-Geometric.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?](items/Can%20Vision-Language%20Models%20Assess%20Proxemic%20Risk%20from%20Egocentric%20Robot%20Images.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning](items/Surgical%20WAM%20A%20World-Action%20Model%20for%20Data-Efficient%20Surgical%20Robot%20Learning.md) · [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [EgoPHI: Estimating Contact and Force from Egocentric Vision](items/EgoPHI%20Estimating%20Contact%20and%20Force%20from%20Egocentric%20Vision.md) · [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [Towards Socially Compliant Navigation in Deep Reinforcement Learning via Proxemics-Based Reward Modeling](items/Towards%20Socially%20Compliant%20Navigation%20in%20Deep%20Reinforcement%20Learning%20via%20Proxemi.md) · [[世界模型]] [[机器人学习]]
- [Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents](items/Convergent%20Detour%20Hijacking%20Task-Preserving%20Resource%20Amplification%20in%20Skill-Base.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2241
- 入选条目：24
- 回填已见条目：0
- 最高分论文：DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation
- 最高分论文发布时间：2026-08-13T17:18:09Z
- 主要技术对象分类：具身智能评测与基准 18、智能体 Agent 10、世界模型 9、多模态基础模型 9、机器人学习 5、视觉语言动作模型 VLA 5、Sim2Real 2
- 信息源错误：0

</details>
