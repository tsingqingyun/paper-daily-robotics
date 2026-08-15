---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-15
---

# 2026-08-15 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[G0.5: One Autoregressive Stream for Robot Reasoning and Action](items/G0.5%20One%20Autoregressive%20Stream%20for%20Robot%20Reasoning%20and%20Action.md) — We introduce G0.5, a pretrained autoregressive VLA in which a single transformer decoder emits reasoning and action tokens under a single objective.

- **规模**：2241 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、智能体 Agent 15、多模态基础模型 14、世界模型 11、视觉语言动作模型 VLA 11、机器人学习 8、Sim2Real 2
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [G0.5: One Autoregressive Stream for Robot Reasoning and Action](items/G0.5%20One%20Autoregressive%20Stream%20for%20Robot%20Reasoning%20and%20Action.md)

- **创新点 / 方法**：We introduce G0.5, a pretrained autoregressive VLA in which a single transformer decoder emits reasoning and action tokens under a single objective.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models](items/UniTexture%20Cross-Task%20Universal%20Adversarial%20Textures%20for%20Vision-Language-Action.md)

- **创新点 / 方法**：We introduce UniTexture, a cross-task universal adversarial texture attack that uses a single textured 3D object to induce targeted deviations in VLA action predictions across multiple tasks.
- **证据**：UniTexture reduces the mean task success rate from 90.0% under benign conditions to 48.4% under attack, induces target-aligned action shifts, and further exhibits cross-suite and cross-model transfer without re-optimization.

### 3. [Policy-Induced Hand Priors in Humanoid Dual-Arm Manipulation: Diagnosing and Mitigating Initial-Pose Dependence](items/Policy-Induced%20Hand%20Priors%20in%20Humanoid%20Dual-Arm%20Manipulation%20Diagnosing%20and%20Miti.md)

- **创新点 / 方法**：This work investigates initial-pose dependence in VLA-based humanoid dual-arm manipulation.
- **证据**：Evaluations across multiple policies and 17 initial configurations reveal strong initial-pose--policy interactions: the same pose produces substantially different success rates across policies, while a single policy exhibits large performance variation across poses.

### 4. [RoboSynChallenge: Mastering Real-World Dexterity via Generalizing Synthesized Manipulation Skills](items/RoboSynChallenge%20Mastering%20Real-World%20Dexterity%20via%20Generalizing%20Synthesized%20Man.md)

- **创新点 / 方法**：Despite rapid advances in model architectures and learning algorithms, progress is often limited by the scarcity and narrow diversity of real-world data.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](items/ComBodied%20Agents%20a%20New%20Paradigm%20of%20Human-Centric%20Agentic%20AI.md)

- **创新点 / 方法**：We introduce Combodied Agents, a human-centered paradigm that perceives, models, predicts, and supports individual human-state trajectories over time, using software tools, sensors, wearables, robots, and human services as action channels rather than end goals.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [HandEdit: A Unified Benchmark for Egocentric Human-to-Robot Dexterous Hand Image Editing](items/HandEdit%20A%20Unified%20Benchmark%20for%20Egocentric%20Human-to-Robot%20Dexterous%20Hand%20Image.md) — In this work, we present HandEdit, a unified large-scale embodiment-aware image-editing dataset and benchmark specifically designed to transform human hands and arms into various dexterous robotic embodiments within egocentric frames.
- [Self-Evolving Embodied Agents via Skill-Harness Evolution](items/Self-Evolving%20Embodied%20Agents%20via%20Skill-Harness%20Evolution.md) — We propose SHAPER, a self-evolving framework for train-free embodied adaptation that keeps model parameters frozen and improves the non-parametric agent system by evolving reusable skills and a context-code harness through target-environment rollouts.
- [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](items/H2R-Bench%20Benchmarking%20Human-to-Robot%20Manipulation%20Video%20Generation%20in%20World%20Mod.md) — Therefore, we introduce H2R-Bench, a benchmark for evaluating cross-embodiment human-to-robot manipulation video generation, where models transform egocentric human demonstrations into robot manipulation videos under specified embodiments.
- [Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence](items/Spatial%20Memory%20Agent%20Experience-Grounded%20Procedure%20Memory%20for%20Spatial%20Intelligen.md) — Across five representative spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and the best accuracy among the evaluated methods in most of the 20 evaluations, establishing a practical parameter-update-free…
- [Scaling Automatic Research Agents via World Models](items/Scaling%20Automatic%20Research%20Agents%20via%20World%20Models.md) — Moreover, our post-trained 4B and 9B agents outperform much larger open-weight agents of 48B and 120B on held-out benchmarks.
- [Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL](items/Learning%20Loco-Manipulation%20From%20SMPC%20Demonstrations%20With%20Sparse%20Offline-to-Onlin.md) — To bypass this limitation, we leverage Sample-based Model Predictive Control (SMPC) entirely in simulation as an automated, rapidly tunable expert to generate massive offline datasets.
- [Decoding Task Progress from VLA Representations](items/Decoding%20Task%20Progress%20from%20VLA%20Representations.md) — Leveraging ideas from mechanistic interpretability, we probe the residual stream of $π_{0.5}$ and find that task progress, the normalized time remaining in a trajectory, is linearly readable from the activations.

## 其余存档 12 篇

- [HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation](items/HUI360%20A%20360%C2%B0%20Egocentric%20Dataset%20and%20Baselines%20for%20Human-Robot%20Interaction%20Antic.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](items/StellaVLA%20In-Context%20Structured%20Demonstration%20for%20Generalizable%20Vision-Language-.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning](items/Temporal%20GRPO%20Beyond%20Trajectory-Level%20Credit%20in%20Vision-Language-Action%20Reinforce.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](items/HumanoidVLN%20A%20Physics-Grounded%20Simulator%20and%20Benchmark%20for%20Vision-Language%20Navig.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](items/ContactGuard%20Pre-Contact%20Execution%20Monitoring%20with%20Action-Conditioned%20Latent%20Wor.md) · [[世界模型]]
- [S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation](items/S2-HWM%20Sparse%20Event-Structured%20Hierarchical%20World%20Model%20for%20Long-Horizon%20Surgica.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation](items/DreamFly%20Causal%20Memory%20and%20Receding-Horizon%20Diffusion%20Planning%20for%20Aerial%20Vision.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [D3D-GEN: Robot-Aware Domain-Grounded Interactive 3D World Generation for Social Robotics](items/D3D-GEN%20Robot-Aware%20Domain-Grounded%20Interactive%203D%20World%20Generation%20for%20Social%20R.md) · [[智能体 Agent]] [[世界模型]]
- [BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving](items/BrainWAM%20Action-Space%20Coordination%20of%20Semantic%20Priors%20and%20Predictive%20Dynamics%20fo.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [SAP-Nav: Spatial Semantic Representation Meets Active Perception for Hierarchical Open-Vocabulary Object Navigation](items/SAP-Nav%20Spatial%20Semantic%20Representation%20Meets%20Active%20Perception%20for%20Hierarchical.md) · [[智能体 Agent]]
- [AVA-Encoder: Towards Agent-Native Video Representation Learning](items/AVA-Encoder%20Towards%20Agent-Native%20Video%20Representation%20Learning.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Autonomous Telerehabilitation via Skeletal Motion Prediction and Joint-Level Performance Assessment](items/Autonomous%20Telerehabilitation%20via%20Skeletal%20Motion%20Prediction%20and%20Joint-Level%20Per.md) · [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2241
- 入选条目：24
- 回填已见条目：0
- 最高分论文：G0.5: One Autoregressive Stream for Robot Reasoning and Action
- 最高分论文发布时间：2026-08-12T07:26:47Z
- 主要技术对象分类：具身智能评测与基准 17、智能体 Agent 15、多模态基础模型 14、世界模型 11、视觉语言动作模型 VLA 11、机器人学习 8、Sim2Real 2
- 信息源错误：0

</details>
