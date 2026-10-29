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
url: "https://arxiv.org/abs/2610.37393v1"
published: "2026-10-27T15:15:14Z"
age_days: 1
score: 28
created: 2026-10-29
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling

> [!summary] 这篇论文到底做了什么（基于摘要）
> QCP 让机器人不仅听懂“完成任务”，还能接受“快一点”“平稳一点”这样的质量要求。它反复执行、测量实际质量、重新标注成功轨迹再训练，让可控制的质量范围逐步超出最初示范。

## 问题

抓取搬运是否完成，不能代表过程是否合用：传送带操作可能需要快，搬酒杯则需要稳。常见二元成功信号区分不了这些要求，而初始示范展示的速度和平滑程度也可能有限；本文要让这些属性及其组合在推理时可调。

### 用一个例子理解

理解用例（非论文实验）：输入搬运杯子的任务和“优先平稳”条件，QCP 输出较符合该条件的运动。训练中若一次成功搬运的实测稳定性优于原示范，就把轨迹按实测值标注后加入后续训练。

## 创新点或方法

旧做法主要围绕完成任务训练，QCP 把执行质量也作为可指定条件。训练循环中，策略先按目标质量标签收集在线轨迹，把成功轨迹加入数据集，再根据实测质量重新标注累积轨迹并微调。关键是按“实际做到了什么”标注，而不是把期望标签当成事实；新成功轨迹还可能探索到示范之外的质量。推理时指定所需属性或组合即可控制执行，不需要把每次部署都理解为在线重训。具体策略结构与质量编码未说明。

### 方法如何工作

1. 让策略以目标质量为条件执行，得到带有明确期望的在线轨迹。
2. 保留成功轨迹加入数据集，使质量探索仍以完成任务为前提。
3. 测量累积轨迹的实际质量并重新标注，纠正期望与结果的偏差。
4. 用更新数据微调再收集，让新增高质量行为进入下一轮可学习范围。

### 必要术语

- 质量条件：对执行方式的要求；本文用它控制速度、平滑或稳定性。
- 事后重标注：执行后按实测结果改标签；本文用它建立可靠的质量与行为对应。
- 在线轨迹：当前策略实际执行所得的观察和动作记录；本文靠它扩充初始示范。

## 证据

摘要称，在 Robomimic 和 RoboEval 上，QCP 随迭代改善执行质量和成功率，并产生质量超过初始示范的成功轨迹。真机操作中，调节速度提高传送带作业吞吐量，调节运输稳定性提高搬运酒杯的成功率。摘要未提供数字、基线名称、任务数量和波动范围，因而只能确认作者报告的方向性结果，无法判断收益幅度及稳定性。

## 局限

需要核查质量指标是否对应真正需求，例如运动平滑是否足以代表杯中液体稳定。仅加入成功轨迹也使质量改善与成功样本筛选同时发生，需要对照实验拆开两者贡献；摘要未交代，不能据此断言全文没有。

- **判断**：值得细读质量定义与迭代消融，因为可复用的核心是如何可靠地测量、重标注并扩大可控范围。

## 研究关联

这里值得借鉴的是把执行结果重新变成条件训练数据：一次没有达到预期速度的成功操作，仍可用于学习它实际达到的速度。对于可以客观测量、又需要随任务调整的行为属性，这比仅保留成功标签提供了更多信息。

### 下一步读哪里

先看速度、平滑和稳定性怎样测量，再核查多个属性能否独立调节、冲突时如何取舍。重点找迭代次数、在线采样成本，以及固定数据重训与新增轨迹之间的对照。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot policy evaluation often relies on a binary success signal for task completion. In real-world deployment, however, desired execution behaviors are also defined by quality attributes such as execution speed and motion smoothness, which need to be dynamically controlled according to task requirements. To address this, we introduce Quality-Controllable Policy (QCP), a robot policy that enables inference-time control over both individual quality attributes and their combinations. To extend the controllable quality range beyond initial demonstrations, we further propose an iterative hindsight relabeling loop: QCP collects online rollouts under target quality labels, adds successful trajectories to the dataset, relabels the accumulated trajectories in hindsight according to their measured quality, and fine-tunes the policy. Experiments on Robomimic and RoboEval demonstrate that QCP consistently improves both task execution quality and success rates across iterations, producing successful rollouts that exceed the quality of the initial demonstrations. Finally, we validate QCP on real-world manipulation tasks, where controlling speed increases throughput in conveyor operations and controlling transport stability improves success when carrying wine glasses, demonstrating that quality-controllable policies yield practical gains in physical deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37393v1
- Authors: Sinjae Kang, Dong Kyu Shin, Jaehong Kim, Kamin Lee, Hyoeun Kim, Kaixin Wang, Li Zhao, Seonghyeon Ye, Kimin Lee
- Published: 2026-10-27T15:15:14Z
- Age days: 1

</details>
