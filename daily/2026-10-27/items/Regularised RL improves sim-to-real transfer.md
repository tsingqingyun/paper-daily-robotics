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
url: "https://arxiv.org/abs/2610.32855v1"
published: "2026-10-23T16:28:10Z"
age_days: 3
score: 31
created: 2026-10-27
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Regularised RL improves sim-to-real transfer

> [!summary] 这篇论文到底做了什么（基于摘要）
> SMM-AC 想让仿真里学会的机器人策略，在真实环境发生变化时也能继续工作。它以 soft mellowmax 价值函数构造正则化强化学习算法；摘要报告其真机回报和抗扰动表现优于对比基线。

## 问题

任务是先在仿真中训练连续控制策略，再部署到机器人。瓶颈是观测、环境和动力学都会偏离仿真；摘要指出，实际流程仍常用正则化较弱的 PPO，而正则化对迁移究竟有多大帮助，缺少清楚的实践刻画。这不等于 PPO 无法迁移。

### 用一个例子理解

理解用例（非论文实验）：输入机器人关节与物体观测，仿真训练出的 SMM-AC 策略输出抓取动作；当真机摩擦发生变化时，检查它能否继续完成抓取。这里的具体任务和结果均非摘要所报告。

## 创新点或方法

旧做法主要验证策略在训练环境中的回报；本文把带鲁棒性保证的价值计算引入 Actor-Critic，得到 SMM-AC。直观上，希望训练时的优化准则就能减轻策略对环境偏差的敏感性。训练会学习策略与价值估计；部署时由策略产生动作，摘要未说明是否还需额外计算，也未提供正则项公式和系数选择。

### 方法如何工作

1. 在仿真连续控制任务中采集交互数据，为策略和价值学习提供反馈。
2. 用 soft mellowmax 构造价值学习机制，使优化带有论文所述的正则化与鲁棒性性质；摘要只说明到此。
3. 通过 Actor-Critic 更新策略，得到可部署的控制行为。
4. 在真机及不同扰动下测量回报，检验仿真中的训练选择是否转化为部署收益。

### 必要术语

- 正则化：给优化目标增加约束或偏好；本文用它改善策略面对环境偏差时的表现。
- Actor-Critic：策略负责选动作，价值估计负责指导更新；它是 SMM-AC 的算法组织方式。
- sim-to-real：将仿真训练的策略迁移到真实机器人；本文检验的核心场景。

## 证据

摘要给出两层证据：在 MuJoCo 连续控制基准上，SMM-AC 与 SAC 等基线有竞争力；在真机上，回报更高，且对观测、环境、动力学扰动更稳健。没有具体任务、机器人型号、回报数值、误差条或完整真机基线名单，因此支持所测条件下的迁移收益，尚不能量化收益大小。

## 局限

我会核查理论保证允许哪些环境变化，以及真机扰动是否符合这些条件。摘要没有说明是否统一数据量、调参预算和随机化设置，因此还不能把全部优势单独归因于正则化强度。

- **判断**：值得读方法公式和真机对照实验：关键是理解哪一种正则化、在什么扰动下带来了可靠收益。

## 研究关联

值得借鉴的是，把部署可靠性落实到训练目标本身。若策略在仿真中表现很好，却容易被真实环境的小变化打乱，就值得检查正则化形式，而不只继续追求仿真回报。

### 下一步读哪里

先看 soft mellowmax 怎样进入价值目标，再核查鲁棒性定理的假设；实验重点查真机基线、扰动幅度，以及正则化与其他训练设置的消融。

- **概念**：世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/Regularised RL improves sim-to-real transfer.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Regularised reinforcement learning (RL) has provable robustness guarantees that should ease the transfer of policies from simulation to robots, known as sim-to-real. Yet, weakly regularised algorithms like Proximal Policy Optimisation (PPO) remain the de facto choice in sim-to-real pipelines, while the practical benefits of regularisation for transfer remain poorly characterised. In this work, we study the sim-to-real performance of commonly used RL algorithms, with the aim of characterising the effects of regularisation on robotic performance. To that end, we derive Soft MellowMax Actor-Critic (SMM-AC), a novel regularised RL algorithm based on the soft mellowmax value function, which carries strong robustness guarantees. On MuJoCo continuous control benchmarks, SMM-AC is competitive with baselines like Soft Actor-Critic (SAC). On real robots, SMM-AC achieves higher return, while exhibiting greater robustness to perturbations in observations, the environment, and dynamics than baselines. Together, these results demonstrate that regularised RL improves real-world policy deployment through better robustness to the sim-to-real gap, and changing real-world conditions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.32855v1
- Authors: Danilo Vucetic, Mohamad H. Danesh, Florence Clerc, Hsiu-Chin Lin, Jonathan Tremblay
- Published: 2026-10-23T16:28:10Z
- Age days: 3

</details>
