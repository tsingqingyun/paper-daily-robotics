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
url: "https://arxiv.org/abs/2610.09943v1"
published: "2026-10-07T12:26:21Z"
age_days: 0
score: 30
created: 2026-10-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization

> [!summary] 这篇论文到底做了什么（基于摘要）
> DRIVE 不只奖励机器人完成任务，还奖励它在相同条件下用不同的有效方式完成任务。它只从成功轨迹计算多样性奖励，并对齐时间，尽量避免把失败乱动或速度差异当成新策略。

## 问题

任务是通过闭环强化学习微调 VLA，使它在微调分布之外仍能成功。普通强化学习虽改善训练条件下的表现，分布外泛化仍有限。作者分析发现，强化学习会收缩整体行为范围，却能增加成功轨迹的多样性；因此关键可能不是探索得多，而是覆盖更多有效解法。

### 用一个例子理解

理解用例（非论文实验）：输入相同桌面场景和搬运指令，采样多次尝试；两条都成功、但分别从障碍两侧搬运的轨迹可获得多样性激励，掉落物体的轨迹不因此受奖。训练后策略直接输出动作。

## 创新点或方法

旧做法主要按任务成败给奖励；DRIVE 把成功行为的相对多样性加入强化学习目标。训练时将匹配任务条件的多次 rollout 分组，对轨迹做时间对齐，再根据成功轨迹之间的行为差异生成内在奖励。这样，同一任务的替代解法获得额外激励，而失败行为和单纯快慢不同不应获得同样奖励。推理时使用微调后的策略；摘要没有说明需要保留分组比较。轨迹距离、对齐算法和奖励权重均未给出。

### 方法如何工作

1. 在匹配的任务条件下采样多条轨迹，使行为差异尽量来自策略选择。
2. 对轨迹进行时间对齐，减少执行速度差异对多样性判断的干扰。
3. 依据成功条件计算相对行为多样性，给有效替代解法内在奖励。
4. 将该奖励用于强化学习微调，得到部署策略；具体奖励合成与优化细节，摘要只说明到此。

### 必要术语

- Rollout：策略与环境交互的一次完整尝试；用于比较不同解法。
- 内在奖励：训练系统额外计算的奖励；本文用于鼓励成功行为多样性。
- 分布外测试：测试条件偏离微调条件；检验替代策略是否带来适应收益。

## 证据

摘要报告 LIBERO-Plus、ManiSkill3、RoboTwin 2.0 三个仿真评估：相对普通强化学习微调，π₀ 的平均分布外表现提高 5.3 个点，π₀.₅ 提高 2.0 个点。双臂 AgileX PiPER-X 真机上，平均分布外成功率从 64.1% 到 73.3%，提高 9.2 个百分点。数字均来自摘要。它们支持所测设置下的收益，但未给各项分布变化、方差和采样预算；也不能单凭这些结果证明多样性是全部收益的原因。

## 局限

作者对成功覆盖与泛化的解释包含可能性判断，不能直接当成因果结论。我会核查相同 rollout 预算下的消融，以及轨迹差异是否对应有效策略差异；时间对齐能减少速度干扰，但摘要不足以证明消除了所有表面差异。

- **判断**：值得读奖励定义和预算公平的消融：这是一个可操作的训练目标，关键在于它是否准确奖励了不同的成功解法。

## 研究关联

值得借鉴的是把探索目标收窄到“多种成功方式”。当一个任务确实允许替代路径时，保留这些路径可能让策略遇到环境变化时还有可用选择；任务只有唯一可行解时，这种奖励是否有益需要另查。

### 下一步读哪里

检查任务条件如何匹配、轨迹比较空间、时间对齐与成功条件奖励公式，再看等采样预算消融和真机分布外变化的定义。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/Many Ways to Succeed Diversity-Driven RL Fine-Tuning for VLA Generalization.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts, and covers more of the latent task-valid solution space than supervised fine-tuning. Broader successful-mode coverage may provide alternative strategies under distribution shifts. Inspired by this, we introduce DRIVE (Diversity-driven RL fIne-tuning for VLA gEneralization), which turns successful-behavior diversity into an explicit RL objective. DRIVE groups rollouts under matched task conditions, compares their trajectories with temporal alignment, and derives a success-conditioned intrinsic reward from relative behavioral diversity. This design encourages broader coverage of feasible solutions without rewarding diverse failures or superficial timing differences. Across LIBERO-Plus, ManiSkill3, and RoboTwin 2.0, DRIVE improves the average out-of-domain (OOD) performance over vanilla RL fine-tuning by 5.3 points on $π_0$ and 2.0 points on $π_{0.5}$. On a dual-arm AgileX PiPER-X platform, DRIVE further increases average OOD success from 64.1% to 73.3% (+9.2 points), demonstrating gains that persist under physical deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09943v1
- Authors: Haoru Li, Jinmei Liu, Zhiyong Wang, Xiaoming Li, Zhenhong Sun, Daoyi Dong, Chunlin Chen, Zhi Wang
- Published: 2026-10-07T12:26:21Z
- Age days: 0

</details>
