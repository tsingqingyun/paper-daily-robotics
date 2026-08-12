---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-25
---

# 2026-06-25 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[World Value Models for Robotic Manipulation](items/World%20Value%20Models%20for%20Robotic%20Manipulation.md) — When deployed for policy learning, WVM improves manipulation performance across various policy extraction approaches in both simulated and real-world deployment, providing robust guidance for learning from mixed-quality data.

- **规模**：2100 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 15、智能体 Agent 13、具身智能评测与基准 12、世界模型 11、机器人学习 10、视觉语言动作模型 VLA 8、AI 核心知识地图 1
- **源异常**：0

## 必读 5 篇

### 1. [World Value Models for Robotic Manipulation](items/World%20Value%20Models%20for%20Robotic%20Manipulation.md)

- **创新点 / 方法**：Generalist value models play a pivotal role in scaling robotic policy learning from large-scale, mixed-quality data.
- **证据**：When deployed for policy learning, WVM improves manipulation performance across various policy extraction approaches in both simulated and real-world deployment, providing robust guidance for learning from mixed-quality data.

### 2. [RoBoSR: Structured Scene Representations for Embodied Robotic Reasoning](items/RoBoSR%20Structured%20Scene%20Representations%20for%20Embodied%20Robotic%20Reasoning.md)

- **创新点 / 方法**：We introduce RoBoSR, an intermediate structural representation that formulates manipulation as step-wise state transitions over semantically grounded, object-centric scene graphs.
- **证据**：Across several benchmarks and real-world demonstrations, our method consistently outperforms prompting-based methods and classical TAMP baselines in zero-shot generalization and long-horizon tasks.

### 3. [G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models](items/G%24%203%24VLA%20Geometric%20inductive%20bias%20for%20Vision-Language-Action%20Models.md)

- **创新点 / 方法**：We propose G$^3$VLA, a camera-aware geometric module that injects calibrated structure into the visual-token stream of a pretrained VLA without altering its action space or imitation objective, combining intrinsic-conditioned ray embeddings, projective positional encoding (PRoPE), and bidirectional cross-view fusion.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation](items/NoContactNoWorries%20Estimating%20Contact%20through%20Vision%20and%20Proprioception%20for%20In-H.md)

- **创新点 / 方法**：We present NoContactNoWorries, a transformer-based multimodal framework that fuses RGB-D vision with the robot's proprioception to infer binary contact states as a pseudo-tactile signal for hand-object interactions.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation](items/Flow%20as%20Flow%20Modeling%20Robot%20Velocity%20Fields%20as%20Probability%20Velocity%20Fields%20for%20F.md)

- **创新点 / 方法**：We propose Flow as Flow, a framework that models robot flows as probability flows based on a flow matching formulation.
- **证据**：Across standard benchmarks, our method outperforms representative baseline methods on standard metrics, while achieving approximately 33$\times$ faster generation.

## 扫读 7 篇

- [NavWM: A Unified Navigation World Model for Foresight-Driven Planning](items/NavWM%20A%20Unified%20Navigation%20World%20Model%20for%20Foresight-Driven%20Planning.md) — In this paper, we propose NavWM, a unified navigation world model that seamlessly integrates latent world reasoning, multimodal action prediction, and controllable visual generation.
- [Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos](items/Supervise%20What%20Survives%20Geometry-Guided%20VLA%20Adaptation%20from%20Synthetic%20Robot%20Vide.md) — On real-robot tasks, GRA outperforms pseudo-action baselines under matched data budgets and narrows the gap to policies trained with substantially more real demonstrations, suggesting that correctly routed geometry bridges generated videos to robot policies m…
- [REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs](items/REALM%20A%20Unified%20Red-Teaming%20Benchmark%20for%20Physical-World%20VLMs.md) — Our evaluation shows that text and typographic injection attacks induce the most failures, multimodal co-optimization yields the strongest visual-perturbation transfer, single- pass attacks approach iterative methods at much lower cost, and model scale alone…
- [TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU](items/TurboMPC%20Fast%2C%20Scalable%2C%20and%20Differentiable%20Model%20Predictive%20Control%20on%20the%20GPU.md) — We present TurboMPC, a differentiable MPC solver that runs entirely on the GPU and supports state and control inequality constraints, implicit integrators, cross-time-coupled costs, and slack variables.
- [InSight: Self-Guided Skill Acquisition via Steerable VLAs](items/InSight%20Self-Guided%20Skill%20Acquisition%20via%20Steerable%20VLAs.md) — We present InSight, a framework that unlocks autonomous skill acquisition by rendering VLAs steerable at the primitive-action level (e.g., "move gripper to the bowl", "lift upward", "pour the bottle").
- [RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models](items/RECALL%20Recovery%20Experience%20Collection%20for%20Active%20Lifelong%20Learning%20in%20Vision-Lan.md) — We demonstrate that active, uncertainty-guided data collection leads to more efficient fine-tuning than when using passively-collected demonstrations.
- [KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies](items/KEMO%20Event-Driven%20Keyframe%20Memory%20for%20Long-Horizon%20Robot%20Manipulation%20with%20VLA%20P.md) — Compared with the memory-free baseline (e.g., $π_{0.5}$), KEMO improves aggregate Task Success Rate by 23.6\% and Stage Completion Rate by 34.1\%.

## 其余存档 12 篇

- [TSD: A Physics-Inspired Trajectory Saliency Detector for Efficient Imitation Learning](items/TSD%20A%20Physics-Inspired%20Trajectory%20Saliency%20Detector%20for%20Efficient%20Imitation%20Lear.md) · [[世界模型]] [[机器人学习]]
- [TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation](items/TEXEDO%20Test%20Time%20Scaling%20for%20Controller-aware%20Language-conditioned%20Humanoid%20Moti.md) · [[世界模型]]
- [ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection](items/ReMMD%20Realistic%20Multilingual%20Multi-Image%20Agentic%20Verification%20for%20Multimodal%20Mis.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model](items/DriveStack-VLA%20Render-Teacher%20Alignment%20for%20BEV-Based%20DeepStack%20Vision-Language-.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [AIR: Adaptive Interleaved Reasoning with Code in MLLMs](items/AIR%20Adaptive%20Interleaved%20Reasoning%20with%20Code%20in%20MLLMs.md) · [[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models](items/Attacking%20the%20Trusted%20Imagination%20Oracle-Level%20Integrity%20Attacks%20on%20Imagine-then.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving](items/Intend%2C%20Reflect%2C%20Refine%20An%20Adaptive%20Multimodal%20Reflection%20Framework%20for%20Autonomo.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](items/ArtiTwinSplat%20Interactable%20Digital%20Twin%20Reconstruction%20via%20Gaussian%20Splatting%20fr.md) · [[智能体 Agent]] [[世界模型]]
- [DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy](items/DexTeleop-0%20Force-Aware%20Bimanual%20Dexterous%20Teleoperation%20with%20Ego-Centric%20Percep.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation](items/Flow6D%20Discrete-to-Continuous%20Flow%20Matching%20for%20Efficient%20and%20Accurate%20Category-.md) · [[AI 核心知识地图]]
- [AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control](items/AdaReP%20Adaptive%20Re-Planning%20under%20Model%20Mismatch%20for%20Neural%20World-Model%20Predicti.md) · [[智能体 Agent]] [[世界模型]]
- [Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization](items/Compact%20Object-Level%20Representations%20with%20Open-Vocabulary%20Understanding%20for%20Indo.md) · [[多模态基础模型]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2100
- 入选条目：24
- 回填已见条目：0
- 最高分论文：World Value Models for Robotic Manipulation
- 最高分论文发布时间：2026-06-23T16:07:48Z
- 主要技术对象分类：多模态基础模型 15、智能体 Agent 13、具身智能评测与基准 12、世界模型 11、机器人学习 10、视觉语言动作模型 VLA 8、AI 核心知识地图 1
- 信息源错误：0

</details>
