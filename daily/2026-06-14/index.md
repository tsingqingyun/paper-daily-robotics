---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-14
---

# 2026-06-14 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems](items/DARRMS%20--%20An%20Efficient%20Algorithm%20for%20Dynamic%20Attention%20Radius%20in%20Resource-Constr.md) — Through both theoretical analysis and empirical validation, we demonstrate the effectiveness of adaptive observation in improving system performance and maintaining robust decision- making strategies in resource-constrained systems.

- **规模**：2073 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、世界模型 13、智能体 Agent 10、机器人学习 9、多模态基础模型 6、视觉语言动作模型 VLA 5、Sim2Real 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems](items/DARRMS%20--%20An%20Efficient%20Algorithm%20for%20Dynamic%20Attention%20Radius%20in%20Resource-Constr.md)

- **创新点 / 方法**：In this paper, we introduce a new algorithm that allows for reduced demand on computational resources without a large cost of other performance metrics.
- **证据**：Through both theoretical analysis and empirical validation, we demonstrate the effectiveness of adaptive observation in improving system performance and maintaining robust decision- making strategies in resource-constrained systems.

### 2. [Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics](items/Ambient%20Diffusion%20Policy%20Imitation%20Learning%20from%20Suboptimal%20Data%20in%20Robotics.md)

- **创新点 / 方法**：We propose Ambient Diffusion Policy, a simple and principled method for imitation learning from suboptimal data in robotics.
- **证据**：Notably, it outperforms existing co-training baselines by up to 33% when scaled to Open X-Embodiment - a large dataset with heterogeneous data quality and unstructured distribution shifts.

### 3. [Fast-SDE: Efficient Single-Microphone Sound Source Distance Estimation in Reverberant Environments](items/Fast-SDE%20Efficient%20Single-Microphone%20Sound%20Source%20Distance%20Estimation%20in%20Reverbe.md)

- **创新点 / 方法**：To alleviate these issues, we propose Fast-SDE, a lightweight single-microphone SDE framework that is suited for deployment on robot platforms with limited computational resources and strict size constraints.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering](items/Learning%20What%20to%20Say%20to%20Your%20VLA%20Mostly%20Harmless%20Vision%20Language%20Action%20Model%20St.md)

- **创新点 / 方法**：In this work, we propose a framework that interactively searches for language sequences that improve closed-loop VLA task performance, distills these sequences into a test-time language feedback policy (LFP), and learns an improvement head that predicts when language steering will improve performance.
- **证据**：On seen environments, our conformalized LFP improves base VLA performance by 24.7% in simulation and 65.0% in hardware.

### 5. [$μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models](items/%24%CE%BC%24VLA%20On%20Recurrent%20Memory%20for%20Partially%20Observable%20Manipulation%20in%20VLA%20Models.md)

- **创新点 / 方法**：We present a controlled isolation study of recurrence in a strong pretrained VLA backbone.
- **证据**：On MIKASA-Robo, $μ$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline.

## 扫读 7 篇

- [Point Cloud Segmentation for Autonomous Clip Positioning in Laparoscopic Cholecystectomy on a Phantom](items/Point%20Cloud%20Segmentation%20for%20Autonomous%20Clip%20Positioning%20in%20Laparoscopic%20Cholecy.md) — In real robot experiments, our system localizes targets with the required precision of 0.75mm at a 95% success rate and executes autonomous clip positioning with a 100% success rate.
- [Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models](items/Scale%20Buys%20Interpolation%2C%20Structure%20Buys%20a%20Horizon%20Certified%20Predictability%20for.md) — Scale buys interpolation; structure buys a certified horizon.
- [EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation](items/EA-WM%20Event-Aware%20World%20Models%20with%20Task-Specification%20Grounding%20for%20Long-Horizo.md) — We introduce EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics with task-specification-grounded event prediction and verification.
- [Topical Phase Transitions in Artificial Intelligence Research: Large-Scale Evidence and an Early-Warning Signature for Emerging Topics](items/Topical%20Phase%20Transitions%20in%20Artificial%20Intelligence%20Research%20Large-Scale%20Eviden.md) — Analyzing 80,814 accepted main-track papers from five premier AI conferences (ACL, CVPR, ICLR, ICML, NeurIPS) spanning 2017 to 2025, we show major AI topics advance through topical phase transitions: remaining marginal for years, then surging across venues wi…
- [VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving](items/VLADriveBench%20Evaluating%20CoT-Action%20Relationship%20in%20VLA%20for%20Autonomous%20Driving.md) — We introduce VLADriveBench, a framework that combines observational metrics (mentioning, hallucination, contradiction, action alignment) with a CoT intervention protocol to provide complementary views of the CoT-action relationship.
- [EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations](items/EgoEngine%20From%20Egocentric%20Human%20Videos%20to%20High-Fidelity%20Dexterous%20Robot%20Demonstr.md) — We propose EgoEngine, a scalable framework for transforming egocentric human manipulation videos into high-fidelity robot data.
- [From Imitation to Alignment: Human-Preference Flow Policies for Long-Horizon Sidewalk Navigation](items/From%20Imitation%20to%20Alignment%20Human-Preference%20Flow%20Policies%20for%20Long-Horizon%20Side.md) — FlowPilot achieves 42% success rate and 66% route completion in simulation, while FlowPilot-HP further improves real-world robustness and social compliance, reducing IR by 40.0% and NIR by 52.1% relative to the base model.

## 其余存档 12 篇

- [Traceable Virtual Sea Trials in the Marine Robotics Unity Simulator for Manoeuvring Assessment of Unmanned Surface Vehicles](items/Traceable%20Virtual%20Sea%20Trials%20in%20the%20Marine%20Robotics%20Unity%20Simulator%20for%20Manoeuvr.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation](items/Critic%20Architecture%20Matters%20Dual%20vs.%20Unified%20Critics%20for%20Humanoid%20Loco-Manipulat.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [EmbodiSteer: Steering Embodiment-Agnostic Visuomotor Policies with Joint-Space Guidance for Zero-Shot Cross-Embodiment Deployment](items/EmbodiSteer%20Steering%20Embodiment-Agnostic%20Visuomotor%20Policies%20with%20Joint-Space%20Gu.md) · [[机器人学习]] [[具身智能评测与基准]]
- [MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems](items/MAStrike%20Shapley-Guided%20Collusive%20Red-Teaming%20on%20Multi-Agent%20Systems.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Action-Effect Memory Pretraining for Robot Manipulation](items/Action-Effect%20Memory%20Pretraining%20for%20Robot%20Manipulation.md) · [[世界模型]] [[机器人学习]]
- [NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation](items/NavWAM%20A%20Navigation%20World%20Action%20Model%20for%20Goal-Conditioned%20Visual%20Navigation.md) · [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning](items/WT-UMI%20Tactile-based%20Whole-Body%20Manipulation%20via%20Force-Supervised%20Contact-Aware.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [RoboProcessBench: Benchmarking Process-Aware Understanding in Vision-Language Robotic Manipulation](items/RoboProcessBench%20Benchmarking%20Process-Aware%20Understanding%20in%20Vision-Language%20Rob.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training](items/GenHOI%20Contact-Aware%20Humanoid-Object%20Interaction%20by%20Imitating%20Generated%20Videos%20w.md) · [[世界模型]] [[机器人学习]]
- [Diffusion Transformer World-Action Model for AV Scene Prediction](items/Diffusion%20Transformer%20World-Action%20Model%20for%20AV%20Scene%20Prediction.md) · [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Towards Reliable Sequential Object Picking in Clutter: The Runner-up Solution to RGMC 2025](items/Towards%20Reliable%20Sequential%20Object%20Picking%20in%20Clutter%20The%20Runner-up%20Solution%20to.md) · [[具身智能评测与基准]]
- [ProPlay: Procedural World Models for Self-Evolving LLM Agents](items/ProPlay%20Procedural%20World%20Models%20for%20Self-Evolving%20LLM%20Agents.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2073
- 入选条目：24
- 回填已见条目：0
- 最高分论文：DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems
- 最高分论文发布时间：2026-06-10T19:14:56Z
- 主要技术对象分类：具身智能评测与基准 16、世界模型 13、智能体 Agent 10、机器人学习 9、多模态基础模型 6、视觉语言动作模型 VLA 5、Sim2Real 1
- 信息源错误：0

</details>
