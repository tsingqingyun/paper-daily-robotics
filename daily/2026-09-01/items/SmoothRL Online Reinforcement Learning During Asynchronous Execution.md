---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29768v1"
published: "2026-08-30T12:56:09Z"
age_days: 1
score: 31
created: 2026-09-01
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# SmoothRL: Online Reinforcement Learning During Asynchronous Execution

> [!summary] 先说人话（基于摘要）
> SmoothRL 把在线强化学习嵌入异步动作块执行，并只对机器人真正执行的动作区域回传价值梯度，避免为已承诺或随后丢弃的动作错误优化。

## 问题

大模型推理慢，需要边执行动作块边异步计算下一块；但在线 RL 若忽略这一执行时序，训练的动作分布会和机器人实际轨迹错位，影响精度与稳定性。

## 创新点或方法

每个动作块按帧划分为上轮已承诺区、本轮实际执行区和被下一轮覆盖的丢弃区。框架显式模拟异步推理，以动作价值函数对策略动作的梯度更新预训练策略，但仅让执行区接收梯度；区别于同步 RL 或对整个生成块优化，它对齐真实执行因果链。

## 证据

摘要只称在需要高精度的真实机器人任务和必须异步执行的高动态任务上进行了评估，没有报告成功率、平滑度、延迟或基线比较数字。


## 局限

缺少任何结果结论，尚不能判断只更新执行区能否稳定训练、提升多少，或是否牺牲动作块整体连贯性。

- **判断**：方法问题定义很扎实，值得实时控制研究者读；但在看到真实机器人定量结果前，应视为有潜力的训练修正而非已证实方案。

## 研究关联

对高延迟 VLA 和机器人基础模型，它解决的是在线适应与实时异步控制之间常被忽略的训练一致性问题，具有明确系统价值。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/SmoothRL Online Reinforcement Learning During Asynchronous Execution.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Deploying robot policies in the physical world requires satisfying two fundamental desiderata: reliability and smooth real-time execution. However, deploying state-of-the-art generalist models presents challenges on both fronts. Achieving the precision and robustness required for real-world deployment necessitates sample-efficient online reinforcement learning (RL) to adapt pretrained models. Meanwhile, the increasing scale of robot foundation models has led to higher inference latency. To satisfy real-time constraints under high latency, modern systems adopt asynchronous inference with action chunking, overlapping policy computation with chunk execution to hide latency and enable smooth control. Despite their complementary roles, integrating asynchronous execution with gradient-based online RL remains underexplored. We present SmoothRL, an online RL framework that fine-tunes a pretrained policy within an asynchronous inference loop. SmoothRL follows a value-gradient paradigm, directly updating policy parameters using gradients of the action-value function with respect to policy actions. To enable correct optimization under asynchronous execution, SmoothRL explicitly models the asynchronous inference process during training. Specifically, each generated action chunk is partitioned by frame index into three regions: a committed region, consisting of actions committed by the previous inference cycle; an execution region, containing newly generated actions executed by the robot; and a discarded region, containing actions superseded by the next inference cycle. Gradients are propagated only through the execution region, ensuring policy optimization aligns with the trajectory distribution induced by asynchronous execution. We evaluate SmoothRL on real-world robotic tasks requiring high precision, as well as highly dynamic tasks that necessitate asynchronous execution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29768v1
- Authors: Guang Gao, Yuxuan Nong, Baifu Huang, Jianan Wang
- Published: 2026-08-30T12:56:09Z
- Age days: 1

</details>
