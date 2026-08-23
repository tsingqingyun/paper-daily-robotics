---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-23
---

# 2026-08-23 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrained Space](items/Learning%20Highly%20Dynamic%20Skills%20Transition%20for%20Quadruped%20Jumping%20Through%20Constrai.md) — Here, we propose a hierarchical reinforcement learning pipeline that empowers the robots to perform aggressive locomotion through constrained obstacles--a narrow gate.

- **规模**：2259 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 13、世界模型 10、智能体 Agent 8、机器人学习 8、多模态基础模型 4、Sim2Real 2、AI 核心知识地图 1、视觉语言动作模型 VLA 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrained Space](items/Learning%20Highly%20Dynamic%20Skills%20Transition%20for%20Quadruped%20Jumping%20Through%20Constrai.md)

- **创新点 / 方法**：Here, we propose a hierarchical reinforcement learning pipeline that empowers the robots to perform aggressive locomotion through constrained obstacles--a narrow gate.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [SafeBranch: Branch-Pair Safety Alignment for Embodied Agents](items/SafeBranch%20Branch-Pair%20Safety%20Alignment%20for%20Embodied%20Agents.md)

- **创新点 / 方法**：We propose SafeBranch, a framework that aligns an embodied actor on safety through branch pairs constructed from the actor's own unsafe rollouts via environment rollback.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 3. [Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning](items/Learning%20Hierarchical%20Skill%20Policies%20with%20Offline%20Quality-Diversity%20Reinforcemen.md)

- **创新点 / 方法**：To address this issue, we introduce QDOS (Quality-Diversity Offline Skill learning), a unified pipeline for robust offline-to-online learning.
- **证据**：By providing robust and task-relevant skill representations, QDOS significantly improves the quality of the embedded skill space used by the low-level policy.

### 4. [Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine Learning](items/Catching%20the%20Rug%20Early%20Prediction%20of%20Fraudulent%20Memecoins%20on%20Solana%20via%20Machine.md)

- **创新点 / 方法**：While previous studies have focused on Ethereum-based tokens, this paper shifts the spotlight to Solana, the leading blockchain for memecoins by trading volume and token count.
- **证据**：Despite the absence of code-level features, we demonstrate that classic machine learning models, particularly Gradient Boosting (XGBoost), achieve robust performance in detecting potential rug pulls using only the first 5 minutes of trading data.

### 5. [Evidence-Gated Task and Motion Planning with Vision-Language Models](items/Evidence-Gated%20Task%20and%20Motion%20Planning%20with%20Vision-Language%20Models.md)

- **创新点 / 方法**：We propose Evidence Acquisition and Feasibility Gating (EAFG), a framework that acquires visual evidence through VLM-generated exploratory subgoals and TAMP-based execution.
- **证据**：Our experiments show that, in cooking tasks with ambiguous object use, EAFG improves recipe completion by discovering task-relevant objects before planning.

## 扫读 7 篇

- [CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning](items/CoToGrasp%20Contact-Topology-Conditioned%20Dexterous%20Grasp%20Synthesis%20via%20Canonical%20W.md) — By learning the intrinsic contact manifold of the gripper within this workspace, our model achieves zero-shot generalization to unseen objects at inference.
- [HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation](items/HiTac-WAM%20A%20Hierarchical%20Tactile%20World%20Action%20Model%20for%20Contact-Rich%20Robot%20Manip.md) — HiTac-WAM achieves a mean contact F1 of 0.921; under matched training budgets, the directed hierarchy reduces 3D displacement L2 error by 17.6% relative to the deformation-only predictor and improves slip AUPRC by 60.4% relative to the slip-only predictor.
- [ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents](items/ComponentBench%20Diagnosing%20Component-Level%20Failures%20in%20Computer-Use%20Agents.md) — Evaluating seven models -- GPT-5.4, Gemini 3 Flash, GPT-5.4 mini, GPT-5 mini, Gemini 3.1 Flash-Lite, Qwen3-VL-235B, and UI-TARS-1.5-7B -- across four observation and action spaces, we show that these design choices critically impact performance.
- [Growth Without Us: Machine Consumers, Corporate Circularity, and the Decoupling of GDP from Humanity after AGI](items/Growth%20Without%20Us%20Machine%20Consumers%2C%20Corporate%20Circularity%2C%20and%20the%20Decoupling%20o.md) — The standard objection to full automation is demand-side: if humans earn nothing, who buys the output?
- [Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution](items/Beyond%20Multimodal%20Alignment%20Certifying%20Physical%20Language%20through%20Response%20Substi.md) — At a converged budget, the same rank-three chart executes those programs (oracle NMSE 0.18), fusion improves on both modalities, and 14 of 16 registered checks pass; the two failures arise because a diagonal restriction of the fused information matrix perform…
- [Measuring What a Specification Determines: A Formal Semantic-Block Model and an Execution-Judged Benchmark](items/Measuring%20What%20a%20Specification%20Determines%20A%20Formal%20Semantic-Block%20Model%20and%20an%20E.md) — A specification is represented as a structure comprising semantic blocks, dependency relations, block-owned rules, decision points, and explicitly open questions, subject to four machine-checkable well-formedness conditions: acyclicity, single ownership, cons…
- [SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation](items/SCAPE%20Scenario-Conditioned%20Simulation-Augmented%20Policy%20Evaluation.md) — SCAPE also improves testing sample efficiency, produces narrower calibrated prediction intervals, generalizes better to out-of-distribution scenarios, and enables fine-grained deployment strategies.

## 其余存档 12 篇

- [PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views](items/PartialBiGrasp%20Inferring%20Hidden%20Local%20Geometry%20for%20Bimanual%20Grasping%20from%20Partia.md) · [[世界模型]] [[具身智能评测与基准]]
- [DA-WAM: Decision-Aligned Future Latents for Driving World Models](items/DA-WAM%20Decision-Aligned%20Future%20Latents%20for%20Driving%20World%20Models.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding](items/LT-Mem%20Volatility-Aware%20Spatio-Temporal%20Memory%20for%20Lifelong%20Scene%20Understanding.md) · [[世界模型]] [[具身智能评测与基准]]
- [MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces](items/MILD%20Tractable%20Terrain%20Modeling%20for%20Learning%20Improved%20Bipedal%20Locomotion%20on%20Defo.md) · [[机器人学习]]
- [ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control](items/ADAPT%20Physics-Aware%20Diffusion-based%20World%20Models%20for%20Adaptive%20Predictive%20Transfe.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](items/ADEPT%20Accelerating%20Dexterity%20via%20Pre-Training%20and%20Post-Training%20using%20Reinforcem.md) · [[智能体 Agent]] [[机器人学习]] [[Sim2Real]]
- [Dynamic SpectraFormer for Ultra-High-Definition Underwater Image Enhancement](items/Dynamic%20SpectraFormer%20for%20Ultra-High-Definition%20Underwater%20Image%20Enhancement.md) · [[世界模型]] [[具身智能评测与基准]]
- [HarvestPoint-ACT: Explicit Target Selection and Harvest-Point Conditioning for Robotic Fruit Harvesting under Occlusion](items/HarvestPoint-ACT%20Explicit%20Target%20Selection%20and%20Harvest-Point%20Conditioning%20for%20Ro.md) · [[机器人学习]] [[具身智能评测与基准]]
- [VERAGMIL: Virtual Environment for Scooping Granular Foods with Imitation Learning Models](items/VERAGMIL%20Virtual%20Environment%20for%20Scooping%20Granular%20Foods%20with%20Imitation%20Learning.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Orthogonal JEPA: Factorized Predictive States for Latent World Models](items/Orthogonal%20JEPA%20Factorized%20Predictive%20States%20for%20Latent%20World%20Models.md) · [[智能体 Agent]] [[世界模型]]
- [The Missing Touch: Spatially Distributed Tactile Feedback Brings Teleoperation Closer to Human Dexterity](items/The%20Missing%20Touch%20Spatially%20Distributed%20Tactile%20Feedback%20Brings%20Teleoperation%20Cl.md) · [[机器人学习]]
- [Graphical Design of Interpretable Architectures](items/Graphical%20Design%20of%20Interpretable%20Architectures.md) · [[AI 核心知识地图]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2259
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrained Space
- 最高分论文发布时间：2026-08-20T12:50:18Z
- 主要技术对象分类：具身智能评测与基准 13、世界模型 10、智能体 Agent 8、机器人学习 8、多模态基础模型 4、Sim2Real 2、AI 核心知识地图 1、视觉语言动作模型 VLA 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
