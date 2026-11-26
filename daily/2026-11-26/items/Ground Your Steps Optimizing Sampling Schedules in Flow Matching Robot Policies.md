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
url: "https://arxiv.org/abs/2611.34148v1"
published: "2026-11-25T10:44:48Z"
age_days: 0
score: 33
created: 2026-11-26
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Ground Your Steps: Optimizing Sampling Schedules in Flow Matching Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> Ground Your Steps（GYS）在模型权重和推理计算次数固定时，调整生成动作所用的积分步点。它用示范判断哪套步点能让生成动作的分布更贴近示范，并检验成功率是否随之提高。

## 问题

流匹配机器人策略要对学到的速度场做数值积分，才能生成接下来一小段关节动作。预算只允许查询速度场几次时，同样次数放在不同积分位置上，得到的动作可能不同。均匀网格把查询点等距排开。作者要解决的是，能否用示范找出更合适的排法，让有限次查询生成更接近示范的动作。

### 用一个例子理解

理解用例（非论文实验）｜机械臂看到一个待插入孔中的插头。给定同一观测、参考示范和固定的模型调用次数，GYS 比较不同积分步点生成的关节动作段，选出差值分布最接近的一套步点。上线后，策略用这套步点生成下一段动作。

## 创新点或方法

GYS 在同一观测下拿生成的动作段与示范比较。它先沿每个关节的时间序列做截断分数阶差分，再构造两组差值：生成减示范，以及两条独立生成动作彼此相减。候选步点若只产生内部很一致、却偏离示范的动作，这两类差值分布仍可能不同。作者用能量距离衡量它们的差异，按任务和计算预算优化步点。摘要称，处理后的两类差值分布恰在生成与示范的动作段分布匹配时重合。部署时用选定的步点做积分，无需重新训练策略。

### 方法如何工作

1. 为一个任务和调用预算设定候选积分步点，在相同观测下采样动作段，使比较聚焦在步点位置。
2. 沿各关节的动作序列做截断分数阶差分，将时间变化纳入后续比较。
3. 构造生成与示范的差值，以及两条独立生成动作的差值，用能量距离比较两类差值的分布。
4. 选择使该距离变小的步点，部署时按这些位置积分，并用成功率检验动作分布的改善有无任务收益。

### 必要术语

- 采样步点：数值积分时查询速度场的位置；本文在调用次数固定时优化这些位置。
- 截断分数阶差分：用有限段时间序列计算的变化量变换；本文对每个关节分别应用它，再比较动作段。
- 能量距离：衡量两个分布差异的统计量；本文用它比较两类动作差值分布并选择步点。

## 证据

摘要以均匀网格为对照。RoboTwin 2.0 基准上，GYS 在几乎每个预算下都提高成功率，并分别为 π₀.₅ 和 GR00T N1.7 报告了 2.8 个百分点的提升。3 项真机操作任务中，报告的最大增幅为 3.3 个百分点。摘要没给出 2.8 个百分点的汇总口径、逐预算结果或波动范围。证据覆盖所测模型和任务，无法推出每种任务或预算都有同样收益。

## 局限

仿真覆盖了几乎所有受测预算的改善，真机摘要只给出了最高增幅。值得核查的是，示范分布更接近时，成功率是否也在各任务和预算下同步变好。理论上的分布判据和实测成功率之间，仍需看逐项结果。

- **判断**：值得细读差值分布为什么能用来选步点，以及固定预算的对照，因为这两处决定方法能否复用到别的流匹配策略。

## 研究关联

如果部署限制了模型调用次数，可以把积分步点本身当成可调参数，用已有示范给求解器选步点。这在权重已经固定、手头又有与任务观测相配的示范时尤其值得尝试。

### 下一步读哪里

先看分布判据依赖哪些假设，差分截断后如何处理动作段边界。再查同一观测下需要多少示范和生成样本、步点搜索的代价，以及逐任务的分布距离与成功率是否同向变化。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/Ground Your Steps Optimizing Sampling Schedules in Flow Matching Robot Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow matching robot policies generate action chunks by integrating a learned velocity field at inference. However, under a fixed budget of neural function evaluations (NFEs), the integration result depends on the sampling schedule. This motivates optimizing the schedule to bring the generated action distribution closer to the demonstrations and improve task success. We propose Ground Your Steps (GYS), a training-free method that optimizes the sampling schedule by matching the generated and demonstrated chunk distributions at each observation. GYS applies truncated fractional differencing along each arm joint's action sequence and compares two types of pairwise differences between action chunks at each observation: differences of a generated chunk against a demonstration, and differences of two independent generated chunks against each other. After fractional differencing, these two pairwise-difference distributions coincide exactly when the distributions of generated and demonstrated action chunks match. GYS minimizes the energy distance between these distributions to obtain an improved schedule for each task and NFE budget. Compared with the uniform grid, GYS brings the generated chunk distribution closer to the demonstrated distribution and raises the success rate through the sampling schedule alone. On RoboTwin 2.0 benchmarks, GYS improves success rates at nearly every budget, with gains of 2.8 percentage points for both $π_{0.5}$ and GR00T N1.7. The gains also transfer to three real-world manipulation tasks, reaching up to 3.3 percentage points. Code is available at https://github.com/D-Robotics-AI-Lab/GroundYourSteps.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34148v1
- Authors: Licheng Yang, Yonghao He, Lingfeng Qian, Xin Shi, Wei Sui, Hu Su
- Published: 2026-11-25T10:44:48Z
- Age days: 0

</details>
