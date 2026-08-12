---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-16
---

# 2026-06-16 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[EgoGuide: Egocentric Guidance for Efficient Robot-Free Demonstration Collection and Learning](items/EgoGuide%20Egocentric%20Guidance%20for%20Efficient%20Robot-Free%20Demonstration%20Collection%20a.md) — Real-world experiments show that EgoGuide reduces the required number of data episodes and improves data efficiency.

- **规模**：2043 个候选 → 23 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 14、世界模型 11、智能体 Agent 8、机器人学习 8、多模态基础模型 4、AI 核心知识地图 2、视觉语言动作模型 VLA 2
- **源异常**：2
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [EgoGuide: Egocentric Guidance for Efficient Robot-Free Demonstration Collection and Learning](items/EgoGuide%20Egocentric%20Guidance%20for%20Efficient%20Robot-Free%20Demonstration%20Collection%20a.md)

- **创新点 / 方法**：To improve data efficiency, we present EgoGuide, a collection interface that records synchronized wrist and head/egocentric observations and couples them with online visual-geometric data quality guidance.
- **证据**：Real-world experiments show that EgoGuide reduces the required number of data episodes and improves data efficiency.

### 2. [Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera](items/Spatially%20Conditioned%20Diffusion%20Policy%20Learning%20Precise%20and%20Robust%20Manipulation.md)

- **创新点 / 方法**：To address this challenge, we present Spatially Conditioned Diffusion Policy (SCDP), a diffusion-based visuomotor policy that achieves precise and robust manipulation in a single-camera setting.
- **证据**：Extensive simulation experiments show that SCDP consistently outperforms strong single-view baselines and achieves performance comparable to multi- camera baselines.

### 3. [Encoder Winners Do Not Reliably Transfer Across VLA Backbone Scale: A Frozen-Backbone Grafting Diagnostic](items/Encoder%20Winners%20Do%20Not%20Reliably%20Transfer%20Across%20VLA%20Backbone%20Scale%20A%20Frozen-Back.md)

- **创新点 / 方法**：We introduce a frozen-backbone grafting diagnostic: the vision tower of a released VLA is replaced by a candidate encoder under a fixed protocol (adaptive average pooling, LayerNorm, and a single trainable linear projector), with the language model and action expert frozen.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control](items/Instruct-Particulate%20Scaling%20Feed-Forward%203D%20Object%20Articulation%20with%20Kinematic.md)

- **创新点 / 方法**：To address this gap, we introduce Instruct-Particulate, a model that takes a 3D mesh together with a target kinematic specification, including part descriptions, connectivity, joint types, and optional point prompts, and predicts the corresponding kinematic part segmentation and joint motion parameters.
- **证据**：Experiments show that our model generalizes better across categories and to AI-generated meshes, enabling articulated asset reconstruction from real-world images via image-to-3D models.

### 5. [Causal Object-Centric Models for Planning with Monte Carlo Tree Search](items/Causal%20Object-Centric%20Models%20for%20Planning%20with%20Monte%20Carlo%20Tree%20Search.md)

- **创新点 / 方法**：We introduce COMET (Causal Object-centric Model for Efficient Tree search), a model- based reinforcement learning algorithm that performs Monte Carlo Tree Search in a slot- structured latent space.
- **证据**：Across eight visually and dynamically diverse tasks from the Object-Centric Visual RL benchmark, ManiSkill, Robosuite, and VizDoom, COMET achieves a higher mean normalized score during the early stages of training compared to object-centric and monolithic baselines.

## 扫读 7 篇

- [The N2D Haptic Glove: A Multi-Finger Glove for 2D Directional Force Feedback for Contact Rich Manipulation](items/The%20N2D%20Haptic%20Glove%20A%20Multi-Finger%20Glove%20for%202D%20Directional%20Force%20Feedback%20for.md) — Without directional cues, users must infer contact force from vision alone, often leading to over-pressing, inconsistent control, and reduced precision in robotic teleoperation.
- [More with LESS -- Local Scene Representations for Tactile Imaging](items/More%20with%20LESS%20--%20Local%20Scene%20Representations%20for%20Tactile%20Imaging.md) — We propose Local Encoder for Spatial Sensing (LESS), an object-centric tactile representation that exploits the local nature of touch.
- [Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learning](items/Robust%20Fall%20Recovery%20for%20Armless%20Bipedal-Wheeled%20Robots%20Via%20Force-Guided%20Learnin.md) — To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards).
- [Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback](items/Universal%20Manipulation%20Exoskeleton%20Learning%20Compliant%20Whole-body%20Policies%20with%20R.md) — We demonstrate that this combination of capabilities enables learning bimanual, whole-body, and active compliant policies that operate effectively in highly constrained spaces.
- [Robustness without Wrinkles: Parallel Simulation and Robust MPC for Certified Deformable Manipulation](items/Robustness%20without%20Wrinkles%20Parallel%20Simulation%20and%20Robust%20MPC%20for%20Certified%20Def.md) — Across settings, CORD-SLS achieves millisecond-speed planning, exceeding baselines in safety, speed, and task success.
- [Rethinking One-Step Image Editing through ChordEdit: Reproduction, Simplification, and New Insights](items/Rethinking%20One-Step%20Image%20Editing%20through%20ChordEdit%20Reproduction%2C%20Simplification.md) — We revisit ChordEdit through reproduction, ablation, and simplification.
- [SpikF-GO: Spiking Fourier Graph Operators for Multivariate Time Series Forecasting](items/SpikF-GO%20Spiking%20Fourier%20Graph%20Operators%20for%20Multivariate%20Time%20Series%20Forecastin.md) — Evaluated on eight benchmarks under a unified experimental protocol, SpikF-GO achieves the best average rank among all SNN methods and outperforms its ANN counterpart, FourierGNN, at reduced energy cost.

## 其余存档 11 篇

- [Sensitivity Shaping for Latent Modeling](items/Sensitivity%20Shaping%20for%20Latent%20Modeling.md) · [[智能体 Agent]] [[世界模型]]
- [Provably Safe, Yet Scalable Reinforcement Learning](items/Provably%20Safe%2C%20Yet%20Scalable%20Reinforcement%20Learning.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [SyLink Hand: A Synergy-Inspired Linkage-Driven Anthropomorphic Hand for Human-Like Dexterity](items/SyLink%20Hand%20A%20Synergy-Inspired%20Linkage-Driven%20Anthropomorphic%20Hand%20for%20Human-Lik.md) · [[具身智能评测与基准]]
- [AnyGoal: Vision-Language Guided Multi-Agent Exploration for Training-Free Lifelong Navigation](items/AnyGoal%20Vision-Language%20Guided%20Multi-Agent%20Exploration%20for%20Training-Free%20Lifelon.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]]
- [ComAct: Reframing Professional Software Manipulation via COM-as-Action Paradigm](items/ComAct%20Reframing%20Professional%20Software%20Manipulation%20via%20COM-as-Action%20Paradigm.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Proprioceptive-visual correspondence enables self-other distinction in humanoid robots](items/Proprioceptive-visual%20correspondence%20enables%20self-other%20distinction%20in%20humanoid.md) · [[智能体 Agent]]
- [Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents](items/Functional%20Cache%20Grafting%20Robust%20and%20Rapid%20Code-Policy%20Synthesis%20for%20Embodied%20Ag.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms](items/Whole-Body%20Impedance%20Model%20Predictive%20Control%20for%20Safe%20Physical%20Human--Robot%20Int.md) · [[世界模型]]
- [AERMANI-PLACE: Language Guided Object Placement with Aerial Manipulators](items/AERMANI-PLACE%20Language%20Guided%20Object%20Placement%20with%20Aerial%20Manipulators.md) · [[具身智能评测与基准]]
- [Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks](items/Scratched%20Lenses%2C%20Shifted%20Depth%20Passive%20Camera-Side%20Optical%20Attacks.md) · [[具身智能评测与基准]]
- [CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning](items/CSPO%20Constraint-Sensitive%20Policy%20Optimization%20for%20Safe%20Reinforcement%20Learning.md) · [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2043
- 入选条目：23
- 回填已见条目：0
- 最高分论文：EgoGuide: Egocentric Guidance for Efficient Robot-Free Demonstration Collection and Learning
- 最高分论文发布时间：2026-06-12T17:36:23Z
- 主要技术对象分类：具身智能评测与基准 14、世界模型 11、智能体 Agent 8、机器人学习 8、多模态基础模型 4、AI 核心知识地图 2、视觉语言动作模型 VLA 2
- 信息源错误：2

### 信息源错误

- Google AI Blog: <urlopen error _ssl.c:1112: The handshake operation timed out>
- MIT Technology Review AI: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>

</details>
