---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-18
---

# 2026-08-18 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](items/HAF%20Adapting%20Generalist%20VLAs%20to%20Humanoid%20Whole-Body%20Loco-manipulation%20via%20Hierar.md) — Evaluated on seven real-world humanoid loco-manipulation tasks, HAF surpasses vanilla single-stage VLA baselines and improves whole-body coordination and task performance.

- **规模**：2245 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 22、具身智能评测与基准 17、视觉语言动作模型 VLA 16、智能体 Agent 9、机器人学习 8、世界模型 7、Sim2Real 2
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](items/HAF%20Adapting%20Generalist%20VLAs%20to%20Humanoid%20Whole-Body%20Loco-manipulation%20via%20Hierar.md)

- **创新点 / 方法**：To address these bottlenecks, we introduce HAF (Humanoid Adaptation Framework), a two-part framework consisting of HAF-VLA and HAF-Steer that transfers off-the-shelf generalist VLA foundation models to humanoid whole-body loco-manipulation.
- **证据**：Evaluated on seven real-world humanoid loco-manipulation tasks, HAF surpasses vanilla single-stage VLA baselines and improves whole-body coordination and task performance.

### 2. [$τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](items/%24%CF%84_0%24-VLA%20a%20Hierarchical%20Robot%20Foundation%20Model%20with%20World-Model-Guided%20Test-Tim.md)

- **创新点 / 方法**：We introduce $τ_0$-VLA, a hierarchical robot foundation model that formulates high-level subtask generation as a compute-scalable inference problem through world-model-guided test-time computation.
- **证据**：Across in-domain and distribution-shifted settings, allocating additional test-time computation substantially improves next-subtask prediction accuracy, and these gains translate into higher closed-loop success on long-horizon robot manipulation tasks.

### 3. [NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation](items/NebulaVLA%20A%20Dual-Frequency%20Vision-Language-Action%20Model%20With%20Guide%20Action%20for%20Ro.md)

- **创新点 / 方法**：We present NebulaVLA, an asynchronous dual-frequency architecture that decouples high-level semantic reasoning from low-level action control, optimizing computational resources and modularity.
- **证据**：Comprehensive evaluations demonstrate that NebulaVLA significantly outperforms synchronous baselines, achieving an 85.5\% average success rate on LIBERO-Plus and accelerating action generation by \textasciitilde 2.7$\times$.

### 4. [GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture](items/GigaBrain-0.7%20Scaling%20Embodied%20Foundation%20Models%20to%20Emergent%20Capabilities%20with%20a.md)

- **创新点 / 方法**：To this end, we present GigaBrain-0.7, an embodied foundation model with substantially improved generalization across diverse robot embodiments.
- **证据**：Compared with the preceding GigaBrain-0 series and prior state-of-the-art models including $π_{0.5}$, GigaBrain-0.7 achieves substantial improvements in foundation zero-shot capabilities, language-conditioned instruction following, and post-training task success rates.

### 5. [Robo-Dopamine 2.0: History-Conditioned and OOD-Aware Process Reward Modeling for Robotic Manipulation](items/Robo-Dopamine%202.0%20History-Conditioned%20and%20OOD-Aware%20Process%20Reward%20Modeling%20for.md)

- **创新点 / 方法**：We introduce Robo-Dopamine 2.0, a history- and OOD-aware process reward model with a pairwise prediction interface.
- **证据**：In downstream reinforcement learning, the full model achieves 86.8% mean RoboTwin success and 71/80 successful real-world insertions.

## 扫读 7 篇

- [Vision-Based Tactile Intelligence for Robotics: Sensing, Learning, and Embodied Manipulation](items/Vision-Based%20Tactile%20Intelligence%20for%20Robotics%20Sensing%2C%20Learning%2C%20and%20Embodied%20M.md) — Tactile sensing is essential for robots in contact-rich tasks, yet many tactile sensors still provide sparse, low-dimensional signals that do not capture sufficient information for complex robotic perception and interaction.
- [US-VLA: An Ultrasound Vision-Language-Action Model for Embodied Abdomina](items/US-VLA%20An%20Ultrasound%20Vision-Language-Action%20Model%20for%20Embodied%20Abdomina.md) — Extensive experiments demonstrate that US-VLA achieves competitive performance in ultrasound probe manipulation tasks, indicating its effectiveness and promising generalization within the evaluated abdominal ultrasound setting.
- [StructRL: Structured Action-Space Exploration for Flow-Based VLAs](items/StructRL%20Structured%20Action-Space%20Exploration%20for%20Flow-Based%20VLAs.md) — We show that simply switching the in-chain noise to a structured form does not suffice: noise added at an intermediate flow time can be weakened by the remaining denoising steps before execution, a phenomenon we call \emph{Structured Noise Dilution}.
- [Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory](items/Don%27t%20Drop%20the%20BATON%20Long-Horizon%20Robot%20Manipulation%20via%20Agentic%20Subtask%20Explora.md) — On the long-horizon benchmark RoboMemArena, BATON improves task success by 11.6% and cumulative success by 14.9% over the SoTA.
- [ViTaR: Visuo-Tactile Residual Adaptation for Foundation VLA Manipulation](items/ViTaR%20Visuo-Tactile%20Residual%20Adaptation%20for%20Foundation%20VLA%20Manipulation.md) — On the UniVTAC benchmark spanning seven contact-rich tasks, ViTaR achieves 61.3% average success, a 30.6 percentage-point improvement over its frozen VLA base that also surpasses purpose-built tactile baselines.
- [Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification](items/Algorithm-Architecture%20Co-Design%20for%20Efficient%20VLA%20Inference%20via%20Speculative%20Inf.md) — On the algorithm side, SpecVLA introduces a state-aware VLA inference execution paradigm and a hardware-friendly construction of a smaller verification model (sVLA) using differential residuals and block-wise mixed-precision quantization.
- [PACE: Phase-Progress-Aware Credit for Long-Horizon Embodied Manipulation](items/PACE%20Phase-Progress-Aware%20Credit%20for%20Long-Horizon%20Embodied%20Manipulation.md) — Extensive simulation experiments and diverse real-world robotic-arm experiments demonstrate that PACE consistently achieves significant improvements over the strongest baseline.

## 其余存档 12 篇

- [ForceU-VLA: A Force-Aware Vision-Language-Action Model for Embodied Ultrasound Scanning](items/ForceU-VLA%20A%20Force-Aware%20Vision-Language-Action%20Model%20for%20Embodied%20Ultrasound%20Sc.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability](items/Bit-Flip%20Attacks%20on%20Vision-Language-Action%20Models%20Action-Decoding%20Architecture%20S.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents](items/When%20State%20Becomes%20an%20Attack%20Surface%20State-Semantic%20Injection%20in%20LLM-Driven%20Embo.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- [Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation](items/Security%20of%20Foundation-Model-Powered%20Embodied%20Agents%20Attack%20Surfaces%2C%20Attacks%2C%20D.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [DeepInsight II: One Trace from Benchmark to Robot](items/DeepInsight%20II%20One%20Trace%20from%20Benchmark%20to%20Robot.md) · [[多模态基础模型]] [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- [GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation](items/GaussianDWM%2B%2B%20Language-Grounded%203D%20Gaussian%20Driving%20World%20Model%20for%20Unified%20Scen.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](items/SparkVLA%20Stop-Aware%20Hierarchical%20VLA%20with%20Adaptive%20Action%20Chunking%20for%20Long-Hori.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Revisiting Open-Loop Execution in Robotics: Toward Reactive, Higher-Performing Policies](items/Revisiting%20Open-Loop%20Execution%20in%20Robotics%20Toward%20Reactive%2C%20Higher-Performing%20Po.md) · [[世界模型]] [[机器人学习]]
- [EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints](items/EcoVLA%20Energy-Efficient%20Device-Edge%20Co-Inference%20for%20Vision-Language-Action%20Mode.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning](items/MatchingPolicy%20Correspondence-Aware%20Policy%20Enables%20Cross-Object%20In-Context%20Learn.md) · [[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- [CrossView: Can Vision-Language Models Reason Across Cameras?](items/CrossView%20Can%20Vision-Language%20Models%20Reason%20Across%20Cameras.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [EgoTac: In-the-wild Tactile Prediction from Egocentric Vision](items/EgoTac%20In-the-wild%20Tactile%20Prediction%20from%20Egocentric%20Vision.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2245
- 入选条目：24
- 回填已见条目：0
- 最高分论文：HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL
- 最高分论文发布时间：2026-08-17T17:22:33Z
- 主要技术对象分类：多模态基础模型 22、具身智能评测与基准 17、视觉语言动作模型 VLA 16、智能体 Agent 9、机器人学习 8、世界模型 7、Sim2Real 2
- 信息源错误：0
- 自动恢复信息源：0

</details>
