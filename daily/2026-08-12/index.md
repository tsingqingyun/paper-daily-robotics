---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-12
---

# 2026-08-12 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](items/Agentic%20Harnesses%20LLM-Driven%20Verification%20Layers%20for%20Robot%20Autonomy.md) — With this system, we achieve near 85% precision across accept/escalate/reject categories 97% containment of adversarial attacks, with negligible errors between accepting and rejecting tasks, and errors mostly manifesting at the escalate boundary.

- **规模**：2233 个候选 → 24 篇入选；回填 0 篇
- **主题**：智能体 Agent 16、具身智能评测与基准 15、多模态基础模型 13、世界模型 11、机器人学习 4、视觉语言动作模型 VLA 4、Sim2Real 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](items/Agentic%20Harnesses%20LLM-Driven%20Verification%20Layers%20for%20Robot%20Autonomy.md)

- **创新点 / 方法**：We propose a LLM-driven verification layer between planning and execution to evaluate action permissibility.
- **证据**：With this system, we achieve near 85% precision across accept/escalate/reject categories 97% containment of adversarial attacks, with negligible errors between accepting and rejecting tasks, and errors mostly manifesting at the escalate boundary.

### 2. [SAFE-CHEM: Uncertainty-Aware Policy Switching for Robust Robotic Chemistry](items/SAFE-CHEM%20Uncertainty-Aware%20Policy%20Switching%20for%20Robust%20Robotic%20Chemistry.md)

- **创新点 / 方法**：To mitigate these safety risks, we propose SAFE-CHEM, an uncertainty-aware framework designed for robust, learning-based robotic chemists.
- **证据**：Finally, we demonstrate the practical viability of the framework through zero-shot sim-to-real transfer onto a physical Franka Production 3 robot manipulator.

### 3. [High Fidelity Capture, Reconstruction, and Transfer of Human Demonstrations for Robot-Assisted Bathing](items/High%20Fidelity%20Capture%2C%20Reconstruction%2C%20and%20Transfer%20of%20Human%20Demonstrations%20for.md)

- **创新点 / 方法**：We present a straightforward, but effective framework for doing so with high fidelity by utilizing contact regions as a key processing primitive.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability](items/From%20Recovery%20to%20Drop-off%20How%20Action%20Post-training%20Reduces%20a%20VLM%27s%20Late-Layer%20De.md)

- **创新点 / 方法**：We probe depth perception, a primitive of spatiogeometric understanding, from every decoder layer of a weight-matched open-source base VLM/VLA pair: Molmo2-ER and MolmoAct2-LIBERO.
- **证据**：Second, the degradation is not uniform: while the base VLM's depth decodability improves through its final layers, the VLA's collapses, an additional late-layer drop we call the cliff.

### 5. [360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents](items/360CityArena%20A%20Realistic%20Virtual%20Urban%20Navigation%20Benchmark%20for%20Embodied%20Agents.md)

- **创新点 / 方法**：We present 360CityArena, a benchmark for evaluating the urban exploration capabilities of embodied agents within a photorealistic environment constructed from 360-degree videos.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [Discovering Diverse Planning Policies for Multimodal Embodied Agents with Quality-Diversity Optimization](items/Discovering%20Diverse%20Planning%20Policies%20for%20Multimodal%20Embodied%20Agents%20with%20Qualit.md) — Experiments on the ThreeDWorld transport benchmark show that the proposed framework improves both task success and interaction efficiency over representative baseline planners.
- [PhysX-CoT: Structured Physical Reasoning from a Single Image to Simulation-Ready 3D Assets](items/PhysX-CoT%20Structured%20Physical%20Reasoning%20from%20a%20Single%20Image%20to%20Simulation-Ready.md) — Under a unified protocol that retrains all learned baselines on the same backbone, data, and frozen decoder, PhysX-CoT outperforms the closest full-task baseline across geometry, scale, and physical- attribute metrics.
- [Consilience for Verifier-Free Test-Time Scaling](items/Consilience%20for%20Verifier-Free%20Test-Time%20Scaling.md) — In this paper, we demonstrate a critical limitation of existing confidence-based VF-TTS methods by showing that such methods catastrophically break down on complex tasks.
- [Rethink Before You Execute: Adaptive Execution for World Action Models](items/Rethink%20Before%20You%20Execute%20Adaptive%20Execution%20for%20World%20Action%20Models.md) — On real robots, it reduces WAM inferences by 26.9% on easy tasks while maintaining success, and improves success by 13.3 points on difficult tasks.
- [RayLift: Lifting Complementary Ray-Wise Evidence with 3D Geometry Priors for Semantic Scene Completion](items/RayLift%20Lifting%20Complementary%20Ray-Wise%20Evidence%20with%203D%20Geometry%20Priors%20for%20Sema.md) — Extensive experiments on SemanticKITTI and SSCBench-KITTI-360 demonstrate that RayLift achieves competitive performance and consistently outperforms existing methods.
- [Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models](items/Model%20Discovery%20Agent%20LLM-assisted%20Bayesian%20experiment%20design%20for%20data-efficient.md) — On three different benchmarks --- covering physics (\DPbench, \citep{wiemann2026discoverphysics}), chemistry (\CHEMbench, \citep{kabra2026autoscilab}) and biology (\HHbench, a new partially observed single-neuron electrophysiology benchmark we create) --- we…
- [MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection](items/MADBench%20A%20Benchmark%20for%20Modality-Aware%20Audio%20Deepfake%20Detection.md) — We introduce MADBench, the first benchmark that treats speech and environmental audio as distinct acoustic components, enabling component-aware evaluation of audio deepfake detection across independently manipulated forgery sources.

## 其余存档 12 篇

- [verdi: retrieval is not transfer for continual world model optimization](items/verdi%20retrieval%20is%20not%20transfer%20for%20continual%20world%20model%20optimization.md) · [[智能体 Agent]] [[世界模型]]
- [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](items/HarnessWAM%20Bridging%20Prediction%20and%20Deliberation%20in%20World%20Action%20Models.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [EsaacSim: A Multimodal Event Camera Add-on for NVIDIA Isaac Sim](items/EsaacSim%20A%20Multimodal%20Event%20Camera%20Add-on%20for%20NVIDIA%20Isaac%20Sim.md) · [[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](items/SkillsMetric%20Mapping%20the%20Detection%20Boundary%20of%20Static%20Analysis%20for%20Malicious%20Age.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Diminishing Returns of Intelligence: The Non-Linear Relationship Between LLM Scale and User Perception in Short-Duration Open-Ended Social Human-Robot Interactions](items/Diminishing%20Returns%20of%20Intelligence%20The%20Non-Linear%20Relationship%20Between%20LLM%20Scal.md) · [[多模态基础模型]] [[智能体 Agent]]
- [Action- and Language-Conditioned Video Assessment for Embodied Control](items/Action-%20and%20Language-Conditioned%20Video%20Assessment%20for%20Embodied%20Control.md) · [[多模态基础模型]] [[智能体 Agent]]
- [Lingjing: A Simulation Testbed for Multi-Agent Embodied Tasks in Open-Ended Cities](items/Lingjing%20A%20Simulation%20Testbed%20for%20Multi-Agent%20Embodied%20Tasks%20in%20Open-Ended%20Citie.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Sekai2: From World Exploration to Interactive World Modeling](items/Sekai2%20From%20World%20Exploration%20to%20Interactive%20World%20Modeling.md) · [[智能体 Agent]] [[世界模型]]
- [Particle-Based Conformal Prediction for Contact-Aware Uncertainty Calibration in Stratified Configuration Spaces](items/Particle-Based%20Conformal%20Prediction%20for%20Contact-Aware%20Uncertainty%20Calibration%20in.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Hierarchical Topology-Aware Planning and Control of Underwater Vehicle-Manipulator Systems in Confined Environments](items/Hierarchical%20Topology-Aware%20Planning%20and%20Control%20of%20Underwater%20Vehicle-Manipulat.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [Vid2WAM: Distilling Video Diffusion Priors into World Action Models](items/Vid2WAM%20Distilling%20Video%20Diffusion%20Priors%20into%20World%20Action%20Models.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning](items/Query-Only%20Backdoor%20Attacks%20on%20Self-Evolving%20Skills%20via%20Trajectory%20Poisoning.md) · [[智能体 Agent]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2233
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy
- 最高分论文发布时间：2026-08-10T17:15:55Z
- 主要技术对象分类：智能体 Agent 16、具身智能评测与基准 15、多模态基础模型 13、世界模型 11、机器人学习 4、视觉语言动作模型 VLA 4、Sim2Real 1
- 信息源错误：0

</details>
