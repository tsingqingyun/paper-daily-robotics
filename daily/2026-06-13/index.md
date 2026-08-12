---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-13
---

# 2026-06-13 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](items/%24%20texttt%7BWEAVER%7D%24%2C%20Better%2C%20Faster%2C%20Longer%20An%20Effective%20World%20Model%20for%20Robotic%20M.md) — We apply $\texttt{WEAVER}$ in robotic hardware, demonstrating its effectiveness at policy evaluation ($ρ$=0.870 correlation with real- world success rate), policy improvement (real-world success rate improvement of $38\%$ on top of the $π_{0.5}$ robot foundat…

- **规模**：2063 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、智能体 Agent 16、世界模型 15、多模态基础模型 15、视觉语言动作模型 VLA 12、机器人学习 9、Sim2Real 2
- **源异常**：1
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](items/%24%20texttt%7BWEAVER%7D%24%2C%20Better%2C%20Faster%2C%20Longer%20An%20Effective%20World%20Model%20for%20Robotic%20M.md)

- **创新点 / 方法**：We propose $\texttt{WEAVER}$ (World Estimation Across Views for Embodied Reasoning): a WM architecture that simultaneously achieves all three desiderata, providing state-of-the- art results on robotic manipulation tasks.
- **证据**：We apply $\texttt{WEAVER}$ in robotic hardware, demonstrating its effectiveness at policy evaluation ($ρ$=0.870 correlation with real- world success rate), policy improvement (real-world success rate improvement of $38\%$ on top of the $π_{0.5}$ robot foundation model), and test-time planning (real-world success rate…

### 2. [An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics](items/An%20Embodied%20Simulation%20Platform%2C%20Benchmark%2C%20and%20Data-Efficient%20Augmentation%20Fram.md)

- **创新点 / 方法**：We present Pipette, an embodied simulation platform, benchmark, and data-efficient augmentation framework for wet-lab robot learning.
- **证据**：We further introduce an 11-task wet-lab embodied benchmark covering sample handling, culture-ware manipulation, device operation, and precision placement.

### 3. [SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale](items/SPARC%20Reliable%20Spatial%20Annotations%20from%20Robot%20Demonstrations%20at%20Scale.md)

- **创新点 / 方法**：This work introduces Spatial Annotations from Robot Demonstrations with Reliability Calibration (SPARC), a risk-aware framework that automatically labels robot demonstrations with structured spatial annotations and assigns each annotation a reliability score.
- **证据**：On 1.7k human- annotated demonstrations spanning diverse embodiments and scenarios, SPARC significantly outperforms detection-only baselines in localization accuracy while retaining three times more samples at high-precision operating points.

### 4. [RepWAM: World Action Modeling with Representation Visual-Action Tokenizers](items/RepWAM%20World%20Action%20Modeling%20with%20Representation%20Visual-Action%20Tokenizers.md)

- **创新点 / 方法**：This work presents RepWAM, a representation-centric world action model (WAM) built on representation visual-action tokenizers.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [GIVE: Grounding Human Gestures in Vision-Language-Action Models](items/GIVE%20Grounding%20Human%20Gestures%20in%20Vision-Language-Action%20Models.md)

- **创新点 / 方法**：To address this challenge, we propose GIVE (Gesture Intent via Visual-Semantic Enhancement), an effective approach that enhances pre-trained VLA models with human gesture understanding without architectural modifications.
- **证据**：In real-world HRI experiments, GIVE substantially outperforms the baseline, improving target object recognition accuracy by 40% and overall task success rate by 80%, while demonstrating strong robustness and generalization to unseen spatial layouts and diverse participants.

## 扫读 7 篇

- [See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation](items/See%20Selectively%2C%20Act%20Adaptively%20Dual-Level%20Structural%20Decomposition%20for%20Bimanual.md) — Our model improves the overall average success rate over a monolithic baseline by 27.7% in simulation and 43.3% in real-world evaluation, while consistently outperforming single-module variants across both settings.
- [SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation](items/SERF%20Spatiotemporal%20Environment%20and%20Robot%20Feature%20Map%20for%20Long-Horizon%20Mobile%20Ma.md) — We demonstrate SERF on BEHAVIOR-1K, a benchmark for long-horizon mobile manipulation in household environments.
- [Bounding Boxes as Goals: Language-Conditioned Grasping via Neuro-Symbolic Planning](items/Bounding%20Boxes%20as%20Goals%20Language-Conditioned%20Grasping%20via%20Neuro-Symbolic%20Plannin.md) — We achieve 73.3% overall success across 90 real-robot trials at three difficulty levels, requiring no task- specific training.
- [InterleaveThinker: Reinforcing Agentic Interleaved Generation](items/InterleaveThinker%20Reinforcing%20Agentic%20Interleaved%20Generation.md) — On interleaved generation benchmarks, it achieves performance comparable to Nano Banana and GPT-5.
- [A Tutorial on World Models and Physical AI](items/A%20Tutorial%20on%20World%20Models%20and%20Physical%20AI.md) — World modeling is emerging as a central principle for building intelligent systems capable of prediction, reasoning, and decision making.
- [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](items/Trajectory-Level%20Redirection%20Attacks%20on%20Vision-Language-Action%20Models.md) — To find such prompts, we introduce an on-policy prompt search method that uses rollouts to discover perturbations whose closed-loop behavior tracks a target task while satisfying the command-preserving constraints.
- [G-MAPP: GPU-accelerated Multi-Agent Planning and Perception for Reactive Motion Generation](items/G-MAPP%20GPU-accelerated%20Multi-Agent%20Planning%20and%20Perception%20for%20Reactive%20Motion%20G.md) — We quantitatively evaluate the computation-time and success rate differences for the CPU and GPU versions of our planner, and perform qualitative evaluations of our coupled framework using real-world experiments on a 7-DoF Franka Emika robot.

## 其余存档 12 篇

- [LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories](items/LabVLA%20Grounding%20Vision-Language-Action%20Models%20in%20Scientific%20Laboratories.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation](items/FTP-1%20A%20Generalist%20Foundation%20Tactile%20Policy%20Across%20Tactile%20Sensors%20for%20Contact-.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants](items/Y-BotFrame%20An%20Extensible%20Embodied%20Agent%20Framework%20for%20Quadruped%20Robot%20Assistants.md) · [[多模态基础模型]] [[智能体 Agent]]
- [AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots](items/AIR-VLA%2B%20Decoupling%20Movement%20and%20Manipulation%20via%20Cascaded%20Dual-Action%20Decoders.md) · [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [M*: A Modular, Extensible, Serving System for Multimodal Models](items/M%20A%20Modular%2C%20Extensible%2C%20Serving%20System%20for%20Multimodal%20Models.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation](items/PersonaDrive%20Human-Style%20Retrieval-Augmented%20VLA%20Agents%20for%20Closed-Loop%20Driving.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [Improving Robotic Generalist Policies via Flow Reversal Steering](items/Improving%20Robotic%20Generalist%20Policies%20via%20Flow%20Reversal%20Steering.md) · [[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- [UniIntervene: Agentic Intervention for Efficient Real-World Reinforcement Learning](items/UniIntervene%20Agentic%20Intervention%20for%20Efficient%20Real-World%20Reinforcement%20Learnin.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Making Foresight Actionable: Repurposing Representation Alignment in World Action Models](items/Making%20Foresight%20Actionable%20Repurposing%20Representation%20Alignment%20in%20World%20Action.md) · [[世界模型]] [[视觉语言动作模型 VLA]]
- [Sparse2Act: Learning Action-Aligned Sparse 3D Representations for Cross-Domain Robot Manipulation](items/Sparse2Act%20Learning%20Action-Aligned%20Sparse%203D%20Representations%20for%20Cross-Domain%20Ro.md) · [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [Mana: Dexterous Manipulation of Articulated Tools](items/Mana%20Dexterous%20Manipulation%20of%20Articulated%20Tools.md) · [[智能体 Agent]] [[机器人学习]] [[Sim2Real]]
- [GeoHAT: Geometry-Adaptive Hybrid Action Transformer for Mobile Manipulation](items/GeoHAT%20Geometry-Adaptive%20Hybrid%20Action%20Transformer%20for%20Mobile%20Manipulation.md) · [[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2063
- 入选条目：24
- 回填已见条目：0
- 最高分论文：$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation
- 最高分论文发布时间：2026-06-11T17:59:15Z
- 主要技术对象分类：具身智能评测与基准 16、智能体 Agent 16、世界模型 15、多模态基础模型 15、视觉语言动作模型 VLA 12、机器人学习 9、Sim2Real 2
- 信息源错误：1

### 信息源错误

- MIT Technology Review AI: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>

</details>
