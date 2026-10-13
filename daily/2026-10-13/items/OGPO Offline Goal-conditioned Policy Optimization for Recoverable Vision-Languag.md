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
url: "https://arxiv.org/abs/2610.12914v1"
published: "2026-10-09T03:04:50Z"
age_days: 3
score: 35
created: 2026-10-13
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> OGPO 想让机器人偏离示范路线后还能接着完成任务：它把离线示范改成“需要到达哪些关键状态”的训练材料，用到达这些状态的奖励优化 VLA，而不只是要求逐步复现专家动作。

## 问题

任务是给已有 VLA 做操作技能后训练。逐步模仿能教会机器人一条可行路线，但执行时物体被挪动、抓取位置变化，机器人就可能处于示范没经过的状态；这时，原来的动作标签很少告诉它怎样重新推进任务。瓶颈是恢复方向的监督不足，而不只是动作预测不够准确。

### 用一个例子理解

理解用例（非论文实验）：输入是“把杯子放到托盘上”和杯子被碰偏后的画面；策略以杯子最终进入托盘等关键状态为方向，输出适合当前位置的抓取、搬运动作，而非继续照原示范位置伸手。具体目标如何输入策略仍需核查。

## 创新点或方法

旧做法把示范中每一步动作当标准答案；OGPO 自适应地给轨迹标注语义关键状态，再构造以目标状态为条件的过程奖励，让策略学习“怎样到达下一处任务进展”。巧处是把同一批示范从动作答案变成进展目标，容许到达目标的动作路线不同。训练完全离线，不需要新增在线交互；推理时由优化后的策略执行。关键状态怎么选、奖励怎么算、推理时目标怎么提供，摘要未说明。

### 方法如何工作

1. 从离线示范轨迹中自适应标注语义关键状态，把完整动作路线转成可追求的任务进展目标。
2. 依据目标状态构造过程奖励，让训练获得“执行是否朝目标推进”的信号；具体奖励公式摘要未提供。
3. 用这些奖励离线优化 VLA，使监督重点从复现动作转向到达关键状态，不新增在线交互。
4. 在正常任务和中途扰动条件下测试策略，检查偏离后是否仍能完成目标；恢复动作如何得到离线支持，摘要只说明到此。

### 必要术语

- 目标条件策略：动作选择取决于要到达的状态；本文用它组织关键状态的到达学习。
- 语义关键状态：能表达任务取得某种进展的状态；本文将其作为轨迹重标注的目标。
- 过程奖励：评价执行过程中进展的信号；本文用它补充逐步动作标签。

## 证据

摘要报告在 LIBERO、MetaWorld 上优于标准监督微调，并在 LIBERO-Plus 和新建的执行中途扰动基准 LIBERO-ReAct 上表现出更强恢复能力。这些属于仿真评测，支持它在所测任务和可恢复偏离条件下更稳健。摘要没有成功率、提升幅度、扰动强度、重复试验或具体基座模型，尚不能判断优势有多大，也没有真机恢复证据。

## 局限

论文强调的是可恢复的偏离状态，不能据此推断它能处理物体损坏、目标不可达等失败。我会核查离线数据如何覆盖或约束这些偏离状态，以及恢复收益是否来自关键状态奖励本身；摘要不足以回答这些问题，也不能据此断言全文没有相应实验。

- **判断**：值得读到关键状态重标注、奖励定义和扰动评测细节，因为它是否真正教会恢复，取决于这三者怎样衔接。

## 研究关联

这里值得借鉴的是训练目标的改写：当任务允许多条成功路线时，不必把某条专家路线当作唯一答案，可以监督必须实现的中间结果。尝试这个方向的前提是，关键状态确实代表任务进展，而且能从离线数据中可靠识别。

### 下一步读哪里

先检查关键状态的识别规则与目标采样方式，再看奖励和离线优化如何避免选择数据不支持的动作；最后核查 LIBERO-ReAct 的扰动时机、可恢复性判定，以及与标准微调的公平对比。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/OGPO Offline Goal-conditioned Policy Optimization for Recoverable Vision-Languag.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations. While effective for learning feasible actions, this paradigm supervises policies to reproduce expert actions at each step, biasing them toward demonstration-specific action paths and providing limited guidance for recovering toward task-progress states once execution deviates from demonstrated trajectories. To address this limitation, we propose OGPO, an Offline Goal-conditioned Policy Optimization framework for recoverable VLA post-training. Instead of treating offline demonstrations merely as step-wise action labels, OGPO adaptively relabels trajectories with semantic key states and constructs goal-conditioned process rewards to optimize the policy for reaching these task-progress states. In this way, OGPO shifts VLA post-training from trajectory-level action imitation to key-state reachability learning, enabling policies to acquire a more robust ability to complete goal states from feasible off-demonstration states without requiring additional online interaction. Experiments on LIBERO and MetaWorld show that OGPO consistently improves VLA policy performance over standard supervised fine-tuning. Moreover, evaluations on LIBERO-Plus and our proposed LIBERO-ReAct, a mid-execution perturbation benchmark, further demonstrate that OGPO achieves stronger robustness and goal-directed recoverability under distribution shifts and recoverable off-demonstration states.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12914v1
- Authors: Xule Gao, Xi Wang, Zehua Zang, Rui Wang, Changwen Zheng, Chuxiong Sun
- Published: 2026-10-09T03:04:50Z
- Age days: 3

</details>
