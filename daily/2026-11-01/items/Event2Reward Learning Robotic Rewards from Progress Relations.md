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
url: "https://arxiv.org/abs/2610.39212v1"
published: "2026-10-29T02:34:14Z"
age_days: 2
score: 32
created: 2026-11-01
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Event2Reward: Learning Robotic Rewards from Progress Relations

> [!summary] 这篇论文到底做了什么（基于摘要）
> Event2Reward 要让机器人分清“时间过去了”和“任务推进了”。它用示范时间确定进度尺度，再用停滞、倒退和恢复事件约束局部进度变化，把预测进度转成强化学习奖励。

## 问题

任务是从机器人执行记录中学习稠密奖励，让策略在完成任务前就得到反馈。只把示范的归一化时间当进度标签，会隐含假设任务一直向前；探索时机器人可能把已放好的物体弄掉，模型却仍把后面的状态看成进步。失败记录能纠正这种错误，但很难给其中每一帧标出准确完成百分比。

### 用一个例子理解

理解用例（非论文实验）：输入一段插销先接近孔口、随后滑开的录像；模型结合绝对尺度与“滑开是倒退”的关系，预测进度下降；输出的塑形奖励因此不再鼓励这次滑开。

## 创新点或方法

旧做法主要回答“这一帧处于示范的什么时间”；本文增加“这段执行比刚才更好、相同还是更差”的约束。巧处是无需知道失败状态的绝对进度，也能监督变化方向。训练进度模型时联合使用时间标签和轨迹内部的相对关系；随后训练控制策略时，用预测进度作为奖励塑形的势函数。机器人部署时是否还运行进度模型，摘要未说明。

### 方法如何工作

1. 从不同质量的执行中标出停滞、倒退和恢复，得到不依赖逐帧绝对数值的关系监督。
2. 用归一化时间锚定进度尺度，避免只有局部排序却缺少全局参照。
3. 联合训练进度预测，使全局尺度与局部变化相互约束。
4. 把预测进度用作势函数生成塑形奖励，再训练策略，帮助探索获得更及时的反馈。

### 必要术语

- 相对进度关系：比较状态间是否前进；本文用它监督失败和恢复过程。
- 势函数：给状态赋一个分数；本文以预测进度为基础构造塑形奖励。
- 稀疏奖励：反馈主要集中在任务完成等少数时刻；它是本文策略学习的对照条件。

## 证据

摘要报告：事件数据集来自约 100K 条真实机器人原始执行记录，包含成功、次优和失败过程。相同训练预算下，在四套 LIBERO 的 40 个任务中，策略平均成功率比仅用稀疏奖励高 18.16 个百分点。真机训练 30 分钟后，三项精密插入任务平均成功率为 60.0%，三项物体操作为 90.0%，分别高出基线 36.7 和 23.3 个百分点。消融支持两类监督互补，但摘要未给各自数值、重复次数和误差范围。

## 局限

真机结果支持这些任务及预算下的学习收益，不能直接外推到任意操作。我的待核查问题是：事件如何定义和标注、关系判断有多大噪声，以及进度模型面对未见过的失败方式会怎样；输入不足以判断这些问题是否已在全文验证。

- **判断**：值得读到监督构造和奖励计算细节，因为核心收益来自怎样利用失败过程，而不只是增加执行数据。

## 研究关联

值得借鉴的是改变标注问题：当“完成了多少”难以回答时，可以先标“有没有退步”。若执行记录包含清楚的失败和恢复片段，这种关系可能比强行填写绝对进度更可靠。

### 下一步读哪里

先核查事件如何转成训练约束、时间标签取自哪些执行，再看势函数如何生成奖励，以及消融是否控制数据量和训练预算。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-01/Event2Reward Learning Robotic Rewards from Progress Relations.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning task progress from robot demonstrations provides a practical way to construct dense shaping rewards for robotic reinforcement learning. A common approach uses normalized demonstration time as progress labels, implicitly assuming monotonically increasing task progress. During policy exploration, however, actual task progress can stall or even regress. Such models may mistake regressions for progress, assigning positive shaping rewards to actions that cause progress loss. Real suboptimal and failed executions offer corrective experience, but assigning absolute progress values to their states is difficult. Our key observation is that stalls, regressions, and recoveries establish local relative progress relations even when absolute progress is unknown. We introduce Event2Reward, which uses normalized temporal labels to anchor the progress scale and these within-trajectory relations to constrain local changes, combining absolute and relative progress supervision. Its progress predictions serve as potentials for reward shaping. We curate an event-annotated dataset from approximately 100K raw real-robot execution records, covering successful, suboptimal, and failed executions, without requiring framewise absolute progress labels. Under the same training budgets, Event2Reward improves average policy success by 18.16 percentage points over a baseline using only sparse task rewards across 40 tasks in four LIBERO suites. On real robots, average success after 30 minutes of wall-clock training reaches 60.0% on three precise insertion tasks and 90.0% on three object manipulation tasks, exceeding the sparse-reward baseline under the same budget by 36.7 and 23.3 percentage points, respectively. Ablation studies further show that absolute progress supervision and relative progress relations are complementary, with joint supervision yielding better downstream policy learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39212v1
- Authors: Junnan Nie, Zitian Fan, Jiachen Zhang, Junyi Lao, Likui Zhang, Chenghao Liu, Xiaoyang Lu, Yunbo Wang, Yixue Zhang, Linbo Zhai, Jiayi Li, Mengzhe Wang, Xichang Wu, Bin Wang, Chang Liu, Tianle Zhang, Songfang Huang
- Published: 2026-10-29T02:34:14Z
- Age days: 2

</details>
