---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-24
---

# 2026-06-24 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning](items/HiL-ResRL%20A%20Model-Agnostic%20Finetuning%20Adapter%20via%20Human-in-the-loop%20Residual%20Rei.md) — The results demonstrate that within only 1.5 hour of real-world online RL training, the average success rate exceeds 95% on real robots.

- **规模**：2097 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 19、多模态基础模型 15、视觉语言动作模型 VLA 14、机器人学习 12、世界模型 11、智能体 Agent 7、Sim2Real 3、AI 核心知识地图 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning](items/HiL-ResRL%20A%20Model-Agnostic%20Finetuning%20Adapter%20via%20Human-in-the-loop%20Residual%20Rei.md)

- **创新点 / 方法**：To address these challenges, we introduce a novel, plug- and-play fine-tuning pipeline designed to facilitate the robust deployment of Vision- Language-Action (VLA) models in real-world environments.
- **证据**：The results demonstrate that within only 1.5 hour of real-world online RL training, the average success rate exceeds 95% on real robots.

### 2. [Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data](items/Wh0%20Generative%20World%20Models%20as%20Scalable%20Sources%20of%20Egocentric%20Human%20Hand%20Manipul.md)

- **创新点 / 方法**：We propose Wh0, a framework that uses generative video world models as scalable and controllable sources of egocentric human-hand manipulation data to unlock the manipulation capabilities of pretrained dexterous VLA models.
- **证据**：Across 18 real-world dexterous manipulation tasks, compared with a model post-trained only on robot data, Wh0 improves zero-shot success on unseen tasks from 8.3% to 38.9%.

### 3. [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](items/LIBERO-Safety%20A%20Comprehensive%20Benchmark%20for%20Physical%20and%20Semantic%20Safety%20in%20Visi.md)

- **创新点 / 方法**：To address this, we introduce a parametric safety benchmark to procedurally generate safety- critical scenarios with comprehensive stochasticity.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI](items/Humanoid-OmniOcc%20Stereo-Based%20Full-View%20Occupancy%20Dataset%20for%20Embodied%20AI.md)

- **创新点 / 方法**：We present Humanoid-OmniOcc, a large- scale panoramic stereo-based occupancy dataset tailored for humanoid robots.
- **证据**：Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular baselines and generalizes well to both unseen simulated test scenes and real-world environments, validating the effectiveness of the Real2Sim2Real design.

### 5. [Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA](items/Cloak%20Zero-Shot%20Cross-Embodiment%20Manipulation%20by%20Masking%20the%20End-Effector%20from%20t.md)

- **创新点 / 方法**：We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist camera.
- **证据**：We demonstrate the recipe with Cloak-VLA, a VLA trained with Cloak on a single parallel-jaw gripper dataset.

## 扫读 7 篇

- [PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models](items/PolicyTrim%20Boosting%20Intrinsic%20Policy%20Efficiency%20of%20Vision-Language-Action%20Models.md) — Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3$\times$ and reduces physical execution steps by 51.4\%.
- [dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models](items/dVLA-RL%20Reinforcement%20Learning%20over%20Denoising%20Trajectories%20for%20Discrete%20Diffusio.md) — Extensive evaluations demonstrate that our approach achieves a success rate of \textbf{99.7\%} on LIBERO.
- [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](items/Foresight%20Failure%20Detection%20for%20Long-Horizon%20Robotic%20Manipulation%20with%20Action-Co.md) — We present Foresight, a failure detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model.
- [From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models](items/From%20Pixels%20to%20Concepts%20Growing%20Rich%203D%20Semantic%20Scene%20Graph%20Forests%20utilizing%20F.md) — Evaluations were conducted on the uHumans2 and ScanNet indoor dataset, validating the accuracy and relevance of the generated relationships.
- [OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation](items/OpenHLM%20An%20Empirical%20Recipe%20for%20Whole-Body%20Humanoid%20Loco-Manipulation.md) — In a challenging long-horizon task that spans a wide vertical range of the humanoid, OpenHLM outperforms two state-of-the- art humanoid VLA baselines (GR00T N1.6 and $Ψ_0$) using less than half the total demonstration time.
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](items/HoloAgent-0%20A%20Unified%20Embodied%20Agent%20Framework%20with%203D%20Spatial%20Memory.md) — In this work, we introduce HoloAgent-0, a unified embodied agent framework for real- world robot deployment.
- [LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation](items/LaST-HD%20Learning%20Latent%20Physical%20Reasoning%20from%20Scalable%20Human%20Data%20for%20Robot%20Ma.md) — With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.

## 其余存档 12 篇

- [Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation](items/Flow%20as%20Flow%20Modeling%20Robot%20Velocity%20Fields%20as%20Probability%20Velocity%20Fields%20for%20F.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [Improving Robotic Imitation Learning via Trajectory Standardization](items/Improving%20Robotic%20Imitation%20Learning%20via%20Trajectory%20Standardization.md) · [[机器人学习]] [[具身智能评测与基准]]
- [BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation](items/BiliVLA%20Scene-Aware%20Vision-Language-Action%20Model%20with%20Reinforcement%20Learning%20for.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [IOI: Decoupling Kinematics and Physics for Interactive World Models](items/IOI%20Decoupling%20Kinematics%20and%20Physics%20for%20Interactive%20World%20Models.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Gold Points Sniper: Self-guided Visual Reasoning in VLM for Fine-grained Action Understanding](items/Gold%20Points%20Sniper%20Self-guided%20Visual%20Reasoning%20in%20VLM%20for%20Fine-grained%20Action%20U.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [IMAGIN-4D: Image-Guided Controllable Interaction Generation](items/IMAGIN-4D%20Image-Guided%20Controllable%20Interaction%20Generation.md) · [[AI 核心知识地图]]
- [Flatness Preserves Instruction Following in Vision-Language-Action Models](items/Flatness%20Preserves%20Instruction%20Following%20in%20Vision-Language-Action%20Models.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration](items/HERCULES%20An%20Open-Source%20Simulation%20Framework%20for%20Heterogeneous%20Multi-Robot%20SLAM%2C.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation](items/Flowing%20With%20Purpose%20Latent%20Action%20Guided%20Flow%20Matching%20Policies%20For%20Robotic%20Man.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models](items/UniFS%20Unified%20Fast-to-Slow%20Hierarchical%20Architecture%20for%20Vision-Language-Action.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Pose Anything Anywhere:Model-free Object Poses from Arbitrary References](items/Pose%20Anything%20Anywhere%20Model-free%20Object%20Poses%20from%20Arbitrary%20References.md) · [[世界模型]] [[具身智能评测与基准]]
- [Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models](items/Assistron%20Bayesian%20Shared%20Autonomy%20with%20Off-the-shelf%20Vision-Language-Action%20Mod.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2097
- 入选条目：24
- 回填已见条目：0
- 最高分论文：HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning
- 最高分论文发布时间：2026-06-22T05:07:08Z
- 主要技术对象分类：具身智能评测与基准 19、多模态基础模型 15、视觉语言动作模型 VLA 14、机器人学习 12、世界模型 11、智能体 Agent 7、Sim2Real 3、AI 核心知识地图 1
- 信息源错误：0

</details>
