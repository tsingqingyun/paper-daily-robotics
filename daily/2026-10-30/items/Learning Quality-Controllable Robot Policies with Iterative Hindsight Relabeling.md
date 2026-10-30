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
url: "https://arxiv.org/abs/2610.37393"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-10-30
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling

> [!summary] 这篇论文到底做了什么（基于摘要）
> QCP 让同一个机器人策略在执行时接收速度、运动平滑度等质量要求。它再用“执行、测量、重新标注、继续训练”的循环，尝试学出比初始示范更好的动作。

## 问题

机器人完成搬运只是最低要求：同样成功的两次执行，可能一次快、一次稳。二元成功信号分不清这些差别，也不能直接表达当前想要哪种行为；初始示范还限制了策略见过的质量范围。本文要同时解决执行时可调和训练后突破示范质量范围的问题。

### 用一个例子理解

理解用例（非论文实验）：输入“把装水杯移到托盘，优先平稳”及当前观测；QCP 根据质量条件生成搬运动作，输出一次实际轨迹。若成功但晃动较大，就按测得的稳定性标注，而不保留“很稳”的目标标签。

## 创新点或方法

旧的成功信号之外，QCP 把质量属性及其组合也作为策略条件。推理时，用户给目标质量，策略据此行动；训练时，策略按目标收集轨迹，把成功轨迹加入数据集，再按实际测得的质量重新标注累计数据并微调。巧处是“要求跑得快”不等于“实际跑得快”：训练标签以后者为准，避免把愿望当成结果。摘要未说明质量指标、条件编码和具体训练损失。

### 方法如何工作

1. 给策略观测和目标质量条件，生成一次执行，探索当前能力能达到的行为。
2. 判断任务是否成功，将成功轨迹加入数据集，为下一轮提供可用经验。
3. 测量累计轨迹的实际质量并重新标注，让训练条件对应真实发生的行为。
4. 用更新的数据微调策略，再收集新轨迹，尝试逐轮扩展成功执行的质量范围。

### 必要术语

- 质量条件：对速度、平稳度等执行属性的要求；在本文中用于推理时调节行为。
- 事后重新标注：执行后根据实测结果改写标签；在本文中让条件与轨迹真实质量对应。
- 在线轨迹：当前策略与环境交互产生的完整记录；在本文中补充初始示范之外的经验。

## 证据

摘要称，在 Robomimic 和 RoboEval 上，多轮迭代同时改善执行质量与成功率，并产生超过初始示范质量的成功轨迹。真机验证包括传送带作业和酒杯搬运，分别报告速度控制增加吞吐、运输稳定性控制提高成功率。未给基线名称、数值、试验次数或误差范围，因此能确认报告了这些方向的收益，不能判断收益大小及稳定性。

## 局限

我会核查速度和平稳度冲突时，策略能否可靠达到指定组合，以及超出示范范围的改善能持续多久。摘要没有量化可控范围或目标达成误差；两类真机场景也不足以支持任意质量属性都可控的结论。

- **判断**：值得细读质量标签和迭代数据处理方法，因为这两处决定了策略究竟学会可调行为，还是仅仅平均执行得更好。

## 研究关联

值得借鉴的是把“有没有完成”和“完成得怎样”分开记录。当质量可测、且同一任务确实需要不同执行偏好时，可以尝试按实测质量给成功经验重新标注，让一批轨迹支持多种行为要求。

### 下一步读哪里

先核查质量如何测量和归一化，再看组合控制的目标与实测结果、各轮质量与成功率，以及是否有仅增加数据量的对照，以区分重新标注和数据积累的作用。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.37393v1 Announce Type: cross Abstract: Robot policy evaluation often relies on a binary success signal for task completion. In real-world deployment, however, desired execution behaviors are also defined by quality attributes such as execution speed and motion smoothness, which need to be dynamically controlled according to task requirements. To address this, we introduce Quality-Controllable Policy (QCP), a robot policy that enables inference-time control over both individual quality attributes and their combinations. To extend the controllable quality range beyond initial demonstrations, we further propose an iterative hindsight relabeling loop: QCP collects online rollouts under target quality labels, adds successful trajectories to the dataset, relabels the accumulated trajectories in hindsight according to their measured quality, and fine-tunes the policy. Experiments on Robomimic and RoboEval demonstrate that QCP consistently improves both task execution quality and success rates across iterations, producing successful rollouts that exceed the quality of the initial demonstrations. Finally, we validate QCP on real-world manipulation tasks, where controlling speed increases throughput in conveyor operations and controlling transport stability improves success when carrying wine glasses, demonstrating that quality-controllable policies yield practical gains in physical deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37393
- Authors: Sinjae Kang, Dong Kyu Shin, Jaehong Kim, Kamin Lee, Hyoeun Kim, Kaixin Wang, Li Zhao, Seonghyeon Ye, Kimin Lee
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
