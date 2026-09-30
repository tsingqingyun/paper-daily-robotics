---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.31048v1"
published: "2026-09-25T09:42:20Z"
age_days: 3
score: 32
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability

> [!summary] 先说人话（基于摘要）
> Kintsugi-VLA 把失败轨迹变成恢复训练数据：在仿真中回到失败过程的不同状态，多次尝试续做，找出适合学习恢复的位置。它用实际续做成功概率指导采样。

## 问题

仿真示范流水线通常只保留成功轨迹，丢掉了策略最需要学习恢复的偏离状态。瓶颈是失败轨迹中哪些状态值得采样，不能仅凭轨迹时间位置判断。

## 创新点或方法

固定特权专家，通过精确状态恢复和分支续做估计干预式可恢复概率，采用自适应蒙特卡洛与逐点 Wilson 区间。根据观测到的末段低可恢复边界选择恢复起点，再生成合成恢复示范训练 SmolVLA。

## 证据

在一个仿真 Franka 操作任务中，难度匹配和帧预算匹配下恢复成功率分别为 34.6% 和 38.4%，比同一窗口均匀采样高 5.8、6.7 个百分点。扰动执行及杂乱度、物理条件变化下排序一致；干净任务成功率从 76.8% 降至 74.7%。

## 局限

可恢复性相对于固定专家和采样过程定义，并非状态的绝对属性；证据集中于一个仿真任务，方法还依赖精确状态恢复与分支能力。

- **判断**：值得精读估计方法和预算匹配实验，尤其适合已有仿真失败数据、准备补恢复能力的团队。

## 研究关联

对 VLA 和机器人学习研究者，它提供了失败数据筛选的可操作定义，并显式展示恢复能力与正常执行之间可能存在的取舍。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/Kintsugi-VLA Turning Failed Robot Rollouts into Recovery Data through Interventi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Simulation enables scalable training of Vision-Language-Action policies by using privileged experts to generate visual demonstrations without requiring every trajectory to be collected through manual teleoperation. However, such pipelines typically retain successful demonstrations while failed rollouts are discarded, even though they expose precisely the off-nominal states from which recovery must be learned. We introduce Kintsugi-VLA, a framework for converting failed rollouts into targeted synthetic recovery data by exploiting exact state restoration and branching in simulation. For a fixed privileged expert, we define interventional recoverability as the probability of completing the original task after the simulator is restored to a given state, estimate it using adaptive Monte Carlo continuations with pointwise Wilson intervals, and characterize its non-monotonic evolution along failed trajectories. These estimates identify an observed terminal low-recoverability frontier-the point after which measured recoverability remains below a threshold-which is then used to select informative recovery starting states. In a simulated Franka manipulation task, targeted recovery data yield aggregate SmolVLA recovery success of 34.6\% and 38.4\% under difficulty- and frame-budget matching, respectively, 5.8 and 6.7 percentage points above uniform sampling within the same recovery window. The same ordering is observed under disturbed end-to-end execution and shifted clutter and physics conditions, while clean-task success decreases from 76.8\% to 74.7\%. Kintsugi-VLA demonstrates how failed simulator rollouts can be transformed from discarded experience into structured recovery-training data through direct interventional measurement.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.31048v1
- Authors: Ivan Snegirev, Elizaveta Semenyakina, Dmitrii Maliukov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- Published: 2026-09-25T09:42:20Z
- Age days: 3

</details>
