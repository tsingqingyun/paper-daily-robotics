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
url: "https://arxiv.org/abs/2610.17709"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 31
created: 2026-10-30
concepts: ["机器人学习"]
---

# Where Small Mistakes Matter: Quantifying State Criticality for Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> SCRIM 给示范中的每个状态评估“这里稍微做错，后面会损失多少”。它训练一个专门制造小动作偏差的策略来找脆弱时刻，再用分数调整模仿训练权重或筛选示范。

## 问题

行为克隆通常均匀拟合示范动作，但同样大小的误差后果不同：空旷处偏一点可能可恢复，关键接触时偏一点可能导致失败。统一权重没有反映这种差异，也可能把有限训练数据和拟合能力用在后果较轻的状态上。

### 用一个例子理解

理解用例（非论文实验）：输入一组插接示范；SCRIM 分别估计搬运途中和插入入口处的小动作误差会造成多大后续损失，再提高高风险状态的训练权重，输出重新训练的模仿策略。

## 创新点或方法

旧做法按统一权重学习所有状态；本文先固定一个模仿策略，再训练对抗扰动策略和价值评估器，估计在受限动作扰动下后续价值最坏会下降多少。SCRIM 将估计转成状态分数，用于加权行为克隆损失，或选择紧凑的示范子集。训练因此多了评分和重新训练环节；摘要未描述部署时需要运行扰动策略或价值评估器，也未说明是否反复更新评分。

### 方法如何工作

1. 固定一个模仿策略，使评分针对明确的后续行为，而不是不断变化的对象。
2. 训练受约束的扰动策略寻找有害动作偏差，同时用价值评估器估计后续损失。
3. 把最坏损失估计转成示范状态分数，区分可恢复误差和后果严重的误差。
4. 用分数加权训练或筛选示范，得到新的模仿策略；摘要未说明是否循环重估分数。

### 必要术语

- 行为克隆：根据示范中的状态学习对应动作；本文调整其训练权重。
- 状态关键性：某状态下小动作误差能造成多大最坏后续损失；本文要估计的量。
- 对抗扰动策略：在限制内寻找有害动作偏差的策略；本文用它探测脆弱时刻。
- 价值评估器：估计后续任务回报的模型；本文用它衡量扰动的长期后果。

## 证据

摘要称在多种仿真和真实机器人操作任务上，加权训练提高整体表现，筛选数据可显著减少训练数据并保持性能，分数还能解释哪些时刻关键。但输入没有具体任务名、基线、成功率、数据保留比例或重复试验统计。由此可以理解作者验证的方向，尚不能判断收益大小、额外计算成本或适用任务范围。

## 局限

我的待核查问题是分数对扰动半径、价值评估误差和固定策略水平有多敏感。它度量的是给定策略及扰动条件下的脆弱性，不能直接当作状态固有的、对任何策略都成立的重要程度。仿真与真机各自提供什么证据也需分别查看。

- **判断**：值得细读关键性定义和评分验证，因为核心问题是它能否可靠识别真正影响结局的误差，而不仅仅找到模型难拟合的动作。

## 研究关联

这里改变了示范价值的判断方式：动作难不难拟合，与动作做错的后果有多大，是两个问题。若训练资源有限，按后果分配权重值得尝试，尤其适合少数精细接触时刻决定任务成败的情况。

### 下一步读哪里

先核查扰动约束和后续价值的定义，再看评分与实际扰动后失败的对应关系；数据筛选实验需比较随机筛选、相同数据量和相同总训练预算，并检查评分成本。

- **概念**：机器人学习
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/Where Small Mistakes Matter Quantifying State Criticality for Imitation Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.17709v2 Announce Type: replace-cross Abstract: Imitation learning typically treats every demonstration state as equally important, optimizing a behavior-cloning objective uniformly across the dataset. Yet not all states are created equal: in a small number of critical states, even a slight deviation from the expert action can lead to a failure, while in many other states such errors are recoverable and inconsequential. We formalize state criticality in imitation learning as the worst-case degradation in downstream value induced by a bounded perturbation of the expert action at a given state. We then propose SCRIM, a practical State CRIticality Measure that estimates this quantity by training an adversarial disturbance policy and a value critic around a fixed imitation policy. SCRIM assigns each demonstration state a score reflecting how vulnerable the task outcome is to small, policy-relevant action errors. We show that these scores can be used to reweight behavior-cloning losses, improving imitation at consequential states and increasing overall task performance. We further show that SCRIM enables data curation by selecting compact, high-value subsets of demonstrations that preserve performance while substantially reducing the amount of training data. We evaluate SCRIM across various simulated and real-world robotic manipulation tasks, and demonstrate that SCRIM improves policy training, enables efficient data selection, and provides interpretable insights into which moments in a demonstration are most critical for task success. Project website: https://sia-lab-git.github.io/SCRIM/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.17709
- Authors: Yusuf Umut Ciftci, Joonwon Kang, Ajay Suresha Sathya, Somil Bansal
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
