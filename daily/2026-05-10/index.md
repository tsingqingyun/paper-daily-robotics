---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-05-10
---

# 2026-05-10 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[MolmoAct2: Action Reasoning Models for Real-world Deployment](items/MolmoAct2%20Action%20Reasoning%20Models%20for%20Real-world%20Deployment.md) — In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied- reasoning benc…

- **规模**：历史记录未保存 个候选 → 12 篇入选；回填 0 篇
- **主题**：多模态基础模型 12、视觉语言动作模型 VLA 12、具身智能评测与基准 9、世界模型 7、智能体 Agent 5、机器人学习 3、Sim2Real 1
- **源异常**：0

## 必读 5 篇

### 1. [MolmoAct2: Action Reasoning Models for Real-world Deployment](items/MolmoAct2%20Action%20Reasoning%20Models%20for%20Real-world%20Deployment.md)

- **创新点 / 方法**：We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes.
- **证据**：In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied- reasoning benchmarks.

### 2. [LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning](items/LaST-R1%20Reinforcing%20Robotic%20Manipulation%20via%20Adaptive%20Physical%20Latent%20Reasoning.md)

- **创新点 / 方法**：In this paper, we present LaST-R1, a novel reinforcement learning (RL) post-training framework designed to effectively harness "latent reasoning-before-acting" policies.
- **证据**：Experiments show that LaST-R1 achieves a near-perfect 99.9% average success rate on the LIBERO benchmark with only one-shot supervised warm-up, significantly improving convergence speed and performance over prior state-of-the-art (SOTA) methods.

### 3. [RLDX-1 Technical Report](items/RLDX-1%20Technical%20Report.md)

- **创新点 / 方法**：To address this, we introduce RLDX-1, a general-purpose robotic policy for dexterous manipulation built on the Multi-Stream Action Transformer (MSAT), an architecture that unifies these capabilities by integrating heterogeneous modalities through modality-specific streams with cross-modal joint self-attention.
- **证据**：Through empirical evaluation, we show that RLDX-1 consistently outperforms recent frontier VLAs (e.g.

### 4. [MotuBrain: An Advanced World Action Model for Robot Control](items/MotuBrain%20An%20Advanced%20World%20Action%20Model%20for%20Robot%20Control.md)

- **创新点 / 方法**：We present MotuBrain, a unified World Action Model that jointly models video and action under a UniDiffuser formulation with a three-stream Mixture-of-Transformers architecture.
- **证据**：Experimentally, MotuBrain achieves 95.8% and 96.1% average success on RoboTwin 2.0 under clean and randomized settings, respectively, attains the strongest reported EWMScore in our WorldArena comparison, and adapts to new humanoid embodiments with only 50--100 trajectories.

### 5. [Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies](items/Learning%20while%20Deploying%20Fleet-Scale%20Reinforcement%20Learning%20for%20Generalist%20Robot.md)

- **创新点 / 方法**：We present Learning While Deploying (LWD), a fleet-scale offline-to-online reinforcement learning framework for continual post-training of generalist Vision-Language-Action (VLA) policies.
- **证据**：A single generalist policy improves as fleet experience accumulates, reaching an average success rate of 95%, with the largest gains on long-horizon tasks.

## 扫读 7 篇

- [TriRelVLA: Triadic Relational Structure for Generalizable Embodied Manipulation](items/TriRelVLA%20Triadic%20Relational%20Structure%20for%20Generalizable%20Embodied%20Manipulation.md) — Prior work improves transferability through structured intermediate representations that objectify visual content.
- [PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations](items/PRTS%20A%20Primitive%20Reasoning%20and%20Tasking%20System%20via%20Contrastive%20Representations.md) — Pretrained on 167B tokens of diverse manipulation and embodied- reasoning data, PRTS reaches state-of-the-art performance on LIBERO, LIBERO-Pro, LIBERO- Plus, SimplerEnv, and a real-world suite of 14 complex tasks, with particularly substantial gains on long-…
- [Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](items/Vision-Language-Action%20Safety%20Threats%2C%20Challenges%2C%20Evaluations%2C%20and%20Mechanisms.md) — Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied intelligence.
- [VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts](items/VLA-GSE%20Boosting%20Parameter-Efficient%20Fine-Tuning%20in%20VLA%20with%20Generalized%20and%20Spe.md) — Under a comparable parameter budget, VLA-GSE updates only 2.51% of the full model parameters and consistently outperforms strong FFT and PEFT baselines.
- [Being-H0.7: A Latent World-Action Model from Egocentric Videos](items/Being-H0.7%20A%20Latent%20World-Action%20Model%20from%20Egocentric%20Videos.md) — Experiments across six simulation benchmarks and diverse real-world tasks show that Being-H0.7 achieves state-of-the-art or comparable performance, combining the predictive benefits of world models with the efficiency and deployability of direct VLA policies.
- [Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation](items/Toward%20Visually%20Realistic%20Simulation%20A%20Benchmark%20for%20Evaluating%20Robot%20Manipulati.md) — Our results show that these factors play a critical role in geometric reasoning and spatial grounding, yet are largely overlooked in existing benchmarks.
- [Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation](items/Seeing%20Realism%20from%20Simulation%20Efficient%20Video%20Transfer%20for%20Vision-Language-Acti.md) — For example, our method improves RDT-1B by 8% on Robotwin 2.0, and boosts $π_0$ by 5.1% on the more challenging LIBERO-Plus benchmark.

## 其余存档 0 篇

无。

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：历史记录未保存
- 入选条目：12
- 回填已见条目：0
- 最高分论文：MolmoAct2: Action Reasoning Models for Real-world Deployment
- 最高分论文发布时间：2026-05-04T17:51:21Z
- 主要技术对象分类：多模态基础模型 12、视觉语言动作模型 VLA 12、具身智能评测与基准 9、世界模型 7、智能体 Agent 5、机器人学习 3、Sim2Real 1
- 信息源错误：0

</details>
