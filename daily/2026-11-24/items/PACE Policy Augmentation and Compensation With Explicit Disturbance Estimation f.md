---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.27061v1"
published: "2026-11-20T03:28:57Z"
age_days: 3
score: 28
created: 2026-11-24
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# PACE: Policy Augmentation and Compensation With Explicit Disturbance Estimation for Robust Locomotion

> [!summary] 这篇论文到底做了什么（基于摘要）
> PACE 让四足机器人边走边估计关节上多出来的扰动，再把估计同时用于力矩补偿和策略决策。背上额外载荷或受到外力时，控制器由此有了可以直接使用的反馈。

## 问题

四足机器人要在负载、重心和执行器状态变化时仍跟上速度指令。常见做法是在仿真训练中随机改变动力学，让策略预先适应多种情况。变化都由同一个策略消化时，很难在整个范围内保持精确跟踪，遇到训练采样范围外的条件也更难应对。

### 用一个例子理解

理解用例（非论文实验）。给正在按指令匀速走的四足机器人加上一个偏向左侧的背包。观测器估计负载造成的关节扰动，控制器据此补一部分力矩，策略也读取该估计来调整动作。输出是一组随状态更新的关节控制命令，目的是继续跟踪给定速度。

## 创新点或方法

PACE 把载荷变化、重心偏移、执行器退化和外力折算为关节空间里的合成扰动。运行时，非线性观测器在线估计这个量，无需测关节加速度。估计一路进入控制器做前馈力矩补偿，一路加入策略的观测，让策略能随扰动调整动作。快速变化的触地效应另外用关节和惯性测量做解析估计，无需力传感器。策略在仿真平地训练，附加载荷最多 3 kg，训练时如何注入估计误差，摘要未说明。

### 方法如何工作

1. 把多种动力学变化统一折算成关节扰动，使控制系统能用同一种量描述它们的影响。
2. 在线估计合成扰动，并用关节和惯性测量另外估计快速变化的触地效应。
3. 把扰动估计同时送入力矩补偿和策略观测，让底层控制与动作决策各自利用这份反馈。

### 必要术语

- 关节空间扰动：折算到各关节上的额外作用；本文用它统一描述负载、外力和模型偏差。
- 观测器：根据可测信号推断无法直接测量的量；本文用它在线估计关节扰动。
- 前馈力矩补偿：依据已估计的扰动直接加上补偿力矩；本文用它在控制器里抵消部分额外作用。

## 证据

摘要报告，在 11 种仿真动力学条件下，相比先进基线，速度跟踪误差降低 18.1% 至 57.0%，分布外速度指令下仍有改善。真机实验中，机器人背负接近自重的 11.5 kg 载荷，走下未见过的 16 cm 台阶，并穿越五种室外地形。仿真提供了定量的基线对照，真机展示了在这些条件下可运行。摘要未给基线名称、真机速度误差或重复次数。

## 局限

作者点出快速变化的触地效应难由策略学习，这也是单独估计接触的原因。我会核查落地冲击或观测噪声较大时补偿是否稳定，并用消融判断真机表现能在多大程度上归因于两条扰动反馈路径。

- **判断**：值得细读观测器、力矩补偿和消融实验，尤其是它们如何在接触突变时配合。

## 研究关联

如果不同变化都能折算成同一类可估计的关节扰动，控制器就可以先补偿它们共通的力矩影响，再让策略决定如何调整动作。对能建立可靠扰动观测器的系统，这给出了减少策略单独承担适应任务的具体做法。

### 下一步读哪里

先查观测器依赖的动力学模型和更新频率，再分别看力矩补偿、策略额外观测和接触估计的消融。真机部分重点查重复次数、速度误差和载荷测试条件。

- **概念**：世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/PACE Policy Augmentation and Compensation With Explicit Disturbance Estimation f.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning has made quadrupedal locomotion remarkably robust. To handle unmodeled dynamics and external disturbances, domain randomization is usually employed to make a policy hedge against every condition it might meet. However, maintaining accurate tracking across varying dynamics and generalizing beyond the sampled range remain challenging. Here we show that explicitly estimating the disturbance and feeding the resulting estimation back into both the policy and the controller can relax this compromise. We introduce Policy Augmentation and Compensation with Explicit disturbance estimation (PACE). The framework lumps payload variations, center-of-mass (CoM) shifts, actuator degradation, and external forces into one joint-space disturbance. A nonlinear observer subsequently recovers this disturbance online without requiring joint acceleration measurements. The disturbance estimation provides feedforward torque compensation as the foundational control pathway and further augments the policy observation to enable disturbance-aware action generation. Considering the learning difficulty of fast-varying contact effects, we further provide an analytical contact estimation approach from joint and inertial measurements, without demanding force sensors. Across eleven simulated dynamics conditions, PACE reduces velocity-tracking error by 18.1% to 57.0% against state-of-the-art baselines, and maintains improved tracking under out-of-distribution (OOD) commands. Notably, in real-world experiments, the deployed real robot carried an 11.5 kg payload, nearly equal to its own mass. It also negotiated unseen 16 cm step-downs and crossed five outdoor terrains. The policy was trained exclusively on flat ground in simulation with at most 3 kg of added mass.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27061v1
- Authors: Shixuan Han, Yuyang Wang, Jingting Jia, Zeshuai Chen, Jindou Jia, Kexin Guo, Xiang Yu
- Published: 2026-11-20T03:28:57Z
- Age days: 3

</details>
