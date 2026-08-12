---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-25
---

# 2026-07-25 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training](items/Unified%20Prediction%20and%20Planning%20via%20Conflict-Aware%20Disjoint%20Parameter%20Training.md) — To resolve this, we propose a novel model-merging- based framework, Disjoint Parameter Training (DPT).

- **规模**：2151 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、世界模型 10、智能体 Agent 9、多模态基础模型 8、机器人学习 5、视觉语言动作模型 VLA 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training](items/Unified%20Prediction%20and%20Planning%20via%20Conflict-Aware%20Disjoint%20Parameter%20Training.md)

- **创新点 / 方法**：To resolve this, we propose a novel model-merging- based framework, Disjoint Parameter Training (DPT).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [Robostral Navigate](items/Robostral%20Navigate.md)

- **创新点 / 方法**：We introduce Robostral Navigate, an 8B vision-language model built around this scalability objective.
- **证据**：On R2R-CE, it achieves a 77.4% success rate, surpassing the best monocular method by 10.5 points and the strongest depth- or multi-camera system by 5.3 points despite using only a single RGB camera.

### 3. [PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics](items/PhysCoRe%20Physics-Corrected%20Residual%20World%20Models%20for%20Material-Aware%20Deformable%20D.md)

- **创新点 / 方法**：We present PhysCoRe, a physics-corrected residual world model that couples a differentiable Material Point Method (MPM) simulator with two feed-forward neural networks.
- **证据**：Experiments on real deformable-object manipulation sequences show that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that its predicted confidence forms a reliable distribution across the object's geometry, providing a natural signal for future confidence-guided exploration.

### 4. [LAVIFT: Latent-Action-Guided Vision Fine-Tuning for Surgical Interaction Recognition](items/LAVIFT%20Latent-Action-Guided%20Vision%20Fine-Tuning%20for%20Surgical%20Interaction%20Recognit.md)

- **创新点 / 方法**：Understanding instrument-tissue interactions is essential for context-aware surgical AI and autonomous robotic surgery.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs](items/Inference-Time%20Steering%20for%20Cross-Lingual%20Factual%20Consistency%20in%20LLMs.md)

- **创新点 / 方法**：This leads to cross-lingual factual inconsistency, where they shift their empirical answer distributions based solely on the prompt language.
- **证据**：These findings suggest that cross-lingual inconsistency is at least partly a selection problem, and that simple contextual interventions may outperform more invasive methods for robust, transferable alignment.

## 扫读 7 篇

- [Deep learning-based prediction of time-resolved adhesive forces in viscoelastic Hertzian contacts](items/Deep%20learning-based%20prediction%20of%20time-resolved%20adhesive%20forces%20in%20viscoelastic.md) — We found that the best-performing model has an LSTM architecture with concatenated conditioning, which achieves a held-out mean-squared error of $5.0\times10^{-4}$, a median pull-off-force error of $\approx2.2\%$, and a median hysteresis error of $\approx1.1\…
- [Design and stability analysis of an underactuated hand with passively rotating fingers](items/Design%20and%20stability%20analysis%20of%20an%20underactuated%20hand%20with%20passively%20rotating%20f.md) — With only two phalanges per finger, the design simplifies kinematic complexity while supporting precision and enveloping grasps.
- [Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](items/Future%20Rendering%20%24%20neq%24%20Future%20Surface%20A%20Benchmark%20and%20Dataset%20for%20Dynamic%20Surfa.md) — The benchmark also shows that future rendering quality and future-surface accuracy are statistically decoupled, so the novel-view-synthesis metrics the field reports do not track future geometry.
- [VoLN: Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method](items/VoLN%20Vision-Only%20Long-Horizon%20Navigation---Paradigm%2C%20Benchmark%2C%20and%20Method.md) — On the five-environment Test-Unseen split, it obtains success rates of 7.4%, 4.5%, and 1.8% on Easy, Normal, and Hard episodes, respectively.
- [GuidedAttention: Interpretable and Correctable Visual Attention for OOD-Robust Robot Manipulation via Imitation Learning](items/GuidedAttention%20Interpretable%20and%20Correctable%20Visual%20Attention%20for%20OOD-Robust%20Ro.md) — Experiments in simulation and the real world demonstrate that GuidedAttention consistently improves robot manipulation performance, particularly under positional and appearance out-of-distribution (OOD) conditions.
- [SeededGrasp: Language-Guided Grasping in Complex Scenes with Multiple Embodiments](items/SeededGrasp%20Language-Guided%20Grasping%20in%20Complex%20Scenes%20with%20Multiple%20Embodiments.md) — Experimental results demonstrate that our approach outperforms existing baselines, achieving 72% success in simulation and 78% in real- world grasping experiments.
- [EgoRecovery: Acquiring Failure Recovery Ability Through Human Recovery Demonstration](items/EgoRecovery%20Acquiring%20Failure%20Recovery%20Ability%20Through%20Human%20Recovery%20Demonstrat.md) — In this work, we show that egocentric human data capturing failure recovery processes provides a scalable alternative.

## 其余存档 12 篇

- [Bayesian Retraction Optimization for Tissue Attachment Mapping in Surgical Dissection](items/Bayesian%20Retraction%20Optimization%20for%20Tissue%20Attachment%20Mapping%20in%20Surgical%20Disse.md) · [[世界模型]] [[具身智能评测与基准]]
- [Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar](items/Factorized%20Spatio-Temporal%20Convolutions%20for%20Human%20Pose%20Estimation%20from%20Planar%20Li.md) · [[机器人学习]] [[具身智能评测与基准]]
- [ZONDA: Zero-shot Object Navigation with Dynamic Avoidance in Multi-floor Environments](items/ZONDA%20Zero-shot%20Object%20Navigation%20with%20Dynamic%20Avoidance%20in%20Multi-floor%20Environm.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation](items/SOPD-SocialNav%20Selective%20On-Policy%20Distillation%20for%20Vision-Language%20Social%20Navig.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling](items/FilmWorld%20Agentic%20Novel-to-Film%20Generation%20through%20Dynamic%20Cinematic%20World%20Model.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Correct-by-Construction Behavior Tree Synthesis from Signal Temporal Logic Specifications with Application to Robotic Missions](items/Correct-by-Construction%20Behavior%20Tree%20Synthesis%20from%20Signal%20Temporal%20Logic%20Speci.md) · [[世界模型]] [[具身智能评测与基准]]
- [DWM: Separating World Effects from Actions in Latent World Models](items/DWM%20Separating%20World%20Effects%20from%20Actions%20in%20Latent%20World%20Models.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation](items/Same%20Dangerous%20Objective%2C%20Opposite%20Advice%20Direct%20Exposure%20versus%20Multi-Agent%20Med.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [RL-MACRO: A Cybernetic Closed-Loop Intelligence Framework for Multimodal Adaptive Robotic Craniotomy](items/RL-MACRO%20A%20Cybernetic%20Closed-Loop%20Intelligence%20Framework%20for%20Multimodal%20Adaptive.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Human-Inspired Framework for Robotic Craniotomy: Integrating Multimodal Fusion and Adaptive Trajectory Adjustment](items/Human-Inspired%20Framework%20for%20Robotic%20Craniotomy%20Integrating%20Multimodal%20Fusion%20an.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Emergent Compositional Skills in Mixture-of-Experts VLAs](items/Emergent%20Compositional%20Skills%20in%20Mixture-of-Experts%20VLAs.md) · [[视觉语言动作模型 VLA]] [[机器人学习]]
- [Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments](items/Decentralized%20UAV%20Swarms%20for%20Ground%20Target%20Protection%20in%20GPS-%20and%20Communication-.md) · [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2151
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training
- 最高分论文发布时间：2026-07-22T09:54:22Z
- 主要技术对象分类：具身智能评测与基准 18、世界模型 10、智能体 Agent 9、多模态基础模型 8、机器人学习 5、视觉语言动作模型 VLA 1
- 信息源错误：0

</details>
