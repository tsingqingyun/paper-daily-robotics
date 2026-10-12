---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.12465v1"
published: "2026-10-08T17:59:50Z"
age_days: 3
score: 24
created: 2026-10-12
concepts: ["世界模型", "机器人学习", "Sim2Real"]
---

# A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Success Guided Sampling（SGS）按策略当前的成功率分配练习次数，多练偶尔能做成的任务配置。它解决的是大量并行环境被过易或过难样本占用的问题，让扩规模更有效。

## 问题

任务覆盖复杂地形四足运动和接触装配。多样重置能让策略接触有用中间状态，但均匀采样持续重复已掌握任务，也把经验花在暂时毫无进展的任务上；因此增加环境数未必增加有效学习信号 [S6](https://arxiv.org/html/2610.12465v1#S1.p3.1) [S7](https://arxiv.org/html/2610.12465v1#S1.p4.1)。

### 用一个例子理解

理解用例（非论文实验）：输入一组插接任务配置与最近成败记录；SGS 降低总能插好和完全插不进配置的频率，多抽偶尔成功的配置，RL 得到更集中的练习后重新更新成功率。

## 创新点或方法

旧做法每次均匀抽配置；SGS 维护固定配置集合上的滚动成功率，用 beta 形权重提高中等成功率配置的概率，同时保留所有配置非零概率。它改变训练采样，不改变部署动作接口。RL 使用领域内共享奖励；真机装配另将点云教师通过 DAgger 蒸馏成 RGB 学生，只部署学生 [S13](https://arxiv.org/html/2610.12465v1#S2.p4.1) [S19](https://arxiv.org/html/2610.12465v1#S3.SS3.p2.1) [S36](https://arxiv.org/html/2610.12465v1#A3.SS3.p1.1)。

### 方法如何工作

1. 准备覆盖多种起始状态与目标的配置集合，给采样器提供可练习范围。
2. 统计各配置近期成功率，估计策略当前掌握程度。
3. 提高中等成功率配置的采样权重，保留其他配置的探索机会。
4. 按新分布收集并行经验并更新 RL，再回写成败记录，随能力变化调整练习。
5. 装配部署时蒸馏为 RGB 学生，使用留出环境检验独立执行能力后运行真机。

### 必要术语

- 任务配置：起始状态、目标和环境条件的组合；是 SGS 分配练习的单位。
- beta 形权重：按成功率赋予平滑权重；用于偏向适中难度。
- DAgger：让学生执行时由教师提供纠正动作；用于训练图像输入的部署策略。

## 证据

扩规模实验比较均匀采样、PLR 和手工课程，运动与螺母装配各使用三个训练种子，新采样测试配置仍来自训练分布 [S24](https://arxiv.org/html/2610.12465v1#S4.SS3.p1.1) [S25](https://arxiv.org/html/2610.12465v1#S4.SS3.p2.1)。一百万环境时，四足成功率 SGS 73%、PLR 54%；Franka 螺母装配 SGS 70%、均匀 6%、PLR 5% [S26](https://arxiv.org/html/2610.12465v1#S4.SS3.p3.1)。较易插杆任务在 256K 环境时各方法约 98%，说明优势依赖难度。真机验证三种 UR5e 装配，但节选未提供成功率表；不能把仿真数字用于真机 [S31](https://arxiv.org/html/2610.12465v1#S6.p1.1) [S39](https://arxiv.org/html/2610.12465v1#A3.SS5.p1.1)。

## 局限

作者承认离散评分不适合无限扩展，SGS 不生成配置，且迁移差距仍在 [S30](https://arxiv.org/html/2610.12465v1#S5.p1.1)。主装配实验还使用重力课程；取消后单种子结果相近，尚不足以普遍证明不需要课程 [S32](https://arxiv.org/html/2610.12465v1#A2.SS4.p1.1) [S33](https://arxiv.org/html/2610.12465v1#A2.T5) [S34](https://arxiv.org/html/2610.12465v1#A2.T5.6)。真机固定装配板，未固定会因接触移动而失败 [S40](https://arxiv.org/html/2610.12465v1#A3.SS5.SSS0.Px1.p1.1)。

- **判断**：值得细读采样权重和公平比较条件：主要价值是解释扩规模为何失效，并给出可操作的修正，而不是发明新的课程原则。

## 研究关联

这里改变的是扩规模的判断顺序：先检查一批经验里有多少来自仍在学习的配置，再决定增加算力。尤其已有广泛重置覆盖、成功判定清楚时，调整练习分配可能比继续细调奖励更直接。

### 下一步读哪里

核查成功率窗口、初始估计、beta 参数和最低概率如何避免遗忘。结合 [S25](https://arxiv.org/html/2610.12465v1#S4.SS3.p2.1) 区分相同迭代数与相同总交互量；部署部分重点看 [S37](https://arxiv.org/html/2610.12465v1#A3.SS3.SSS0.Px1.p1.1) 的留出评估，避免在线蒸馏更新抬高训练成功率。

- **概念**：世界模型 机器人学习 Sim2Real
- **筛选分数**：24
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.12465v1
- 获取时间：2026-10-12T00:17:08.853903+00:00
- [S1] [A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control · 正文段落 1](https://arxiv.org/html/2610.12465v1#abstract1.1)
- [S2] [A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control · 正文段落 2](https://arxiv.org/html/2610.12465v1#S0.F1)
- [S3] [A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control · 正文段落 3](https://arxiv.org/html/2610.12465v1#p2.1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.12465v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.12465v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.12465v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.12465v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.12465v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.12465v1#S1.I1.i1)
- [S10] [2 Related Work · 正文段落 13](https://arxiv.org/html/2610.12465v1#S2.p1.1)
- [S11] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.12465v1#S2.p2.1)
- [S12] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.12465v1#S2.p3.1)
- [S13] [2 Related Work · 正文段落 16](https://arxiv.org/html/2610.12465v1#S2.p4.1)
- [S14] [2 Related Work · 正文段落 17](https://arxiv.org/html/2610.12465v1#S2.p5.1)
- [S15] [3.1 Problem Setup · 正文段落 18](https://arxiv.org/html/2610.12465v1#S3.SS1.p1.1)
- [S16] [3.1 Problem Setup · 正文段落 19](https://arxiv.org/html/2610.12465v1#S3.SS1.p2.1)
- [S17] [3.2 SGS: Success Guided Sampling · 正文段落 23](https://arxiv.org/html/2610.12465v1#S3.F2)
- [S18] [3.3 Algorithmic Decisions for RL Training · 正文段落 33](https://arxiv.org/html/2610.12465v1#S3.SS3.p1.1)
- [S19] [3.3 Algorithmic Decisions for RL Training · 正文段落 34](https://arxiv.org/html/2610.12465v1#S3.SS3.p2.1)
- [S20] [3.3 Algorithmic Decisions for RL Training · 正文段落 35](https://arxiv.org/html/2610.12465v1#S3.E3)
- [S21] [3.3 Algorithmic Decisions for RL Training · 正文段落 36](https://arxiv.org/html/2610.12465v1#S3.SS3.p2.2)
- [S22] [3.3 Algorithmic Decisions for RL Training · 正文段落 37](https://arxiv.org/html/2610.12465v1#S3.SS3.p3.1)
- [S23] [4 Experimental Results · 正文段落 38](https://arxiv.org/html/2610.12465v1#S4.p1.1)
- [S24] [4.3 SGS benefits from increased training scale. · 正文段落 49](https://arxiv.org/html/2610.12465v1#S4.SS3.p1.1)
- [S25] [4.3 SGS benefits from increased training scale. · 正文段落 50](https://arxiv.org/html/2610.12465v1#S4.SS3.p2.1)
- [S26] [4.3 SGS benefits from increased training scale. · 正文段落 51](https://arxiv.org/html/2610.12465v1#S4.SS3.p3.1)
- [S27] [4.3 SGS benefits from increased training scale. · 正文段落 52](https://arxiv.org/html/2610.12465v1#S4.T1)
- [S28] [4.3 SGS benefits from increased training scale. · 正文段落 53](https://arxiv.org/html/2610.12465v1#S4.T1.2)
- [S29] [4.3 SGS benefits from increased training scale. · 正文段落 54](https://arxiv.org/html/2610.12465v1#S4.F7)
- [S30] [5 Limitations · 正文段落 59](https://arxiv.org/html/2610.12465v1#S5.p1.1)
- [S31] [6 Conclusion · 正文段落 60](https://arxiv.org/html/2610.12465v1#S6.p1.1)
- [S32] [B.4 Gravity-Curriculum Ablation · 正文段落 99](https://arxiv.org/html/2610.12465v1#A2.SS4.p1.1)
- [S33] [B.4 Gravity-Curriculum Ablation · 正文段落 100](https://arxiv.org/html/2610.12465v1#A2.T5)
- [S34] [B.4 Gravity-Curriculum Ablation · 正文段落 101](https://arxiv.org/html/2610.12465v1#A2.T5.6)
- [S35] [Appendix C Sim-to-Real Transfer and Evaluation · 正文段落 107](https://arxiv.org/html/2610.12465v1#A3.p1.1)
- [S36] [C.3 Teacher–Student Distillation · 正文段落 116](https://arxiv.org/html/2610.12465v1#A3.SS3.p1.1)
- [S37] [C.3 Teacher–Student Distillation · 正文段落 117](https://arxiv.org/html/2610.12465v1#A3.SS3.SSS0.Px1.p1.1)
- [S38] [C.3 Teacher–Student Distillation · 正文段落 118](https://arxiv.org/html/2610.12465v1#A3.F10)
- [S39] [C.5 Real-World Evaluation Protocol · 正文段落 125](https://arxiv.org/html/2610.12465v1#A3.SS5.p1.1)
- [S40] [C.5 Real-World Evaluation Protocol · 正文段落 126](https://arxiv.org/html/2610.12465v1#A3.SS5.SSS0.Px1.p1.1)
- [S41] [C.5 Real-World Evaluation Protocol · 正文段落 127](https://arxiv.org/html/2610.12465v1#A3.SS5.SSS0.Px2.p1.1)
- [S42] [C.5 Real-World Evaluation Protocol · 正文段落 128](https://arxiv.org/html/2610.12465v1#A3.SS5.SSS0.Px3.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-12/A Balanced Data Diet Addressing the Exploration Bottleneck in Mega-Scale RL for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose robots must perform a wide range of tasks from agile locomotion to dexterous manipulation. While sim-to-real reinforcement learning (RL) has proven to be a useful tool for this goal, current RL pipelines depend on engineering-heavy, per-task structural priors such as shaped rewards and demonstrations. Recent work has shown that diverse simulator resets, combined with massively parallel simulation, can alleviate much of this engineering burden on several manipulation problems. However, we find that naively scaling this paradigm to more precise or dynamic problems remains non-trivial. While simulator resets can help with exploration, uniformly sampling over this distribution wastes a growing fraction of learning experience on task configurations the policy has already mastered or cannot yet attempt. This makes it challenging to see the expected benefits of scaling parallel environments for RL, since much of the learning signal in a batch is wasted during learning. To mitigate this, we introduce Success Guided Sampling (SGS), a simple adaptive sampler that concentrates RL training on task configurations around the frontier of the policy's capabilities. Doing so allows large-scale simulated RL to make the most out of the experience in a batch, enabling much more effective scaling to large-scale parallel simulation. Across experiments using up to $2^{20}$ (over one million) parallel environments, SGS enables RL to solve challenging multi-terrain quadruped locomotion and contact-rich assembly tasks that prior methods fail to solve. Finally, we distill the learned manipulation policies into RGB-based policies and demonstrate zero-shot transfer to several challenging assembly tasks on real hardware. Project website: https://sgs-rl.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12465v1
- Authors: Octi Zhang, Mateo Guaman Castro, Patrick Yin, Ignacio Dagnino, Abhishek Gupta, Rosario Scalise, Byron Boots
- Published: 2026-10-08T17:59:50Z
- Age days: 3

</details>
