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
url: "https://arxiv.org/abs/2611.11854v1"
published: "2026-11-09T04:23:14Z"
age_days: 1
score: 39
created: 2026-11-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> DASH 把慢速理解和快速动作生成拆开并发运行，让大模型算得慢时机器人仍能及时控制。动作头同时接收较旧的语义和自己读取的最新视觉，并在训练中学习应对这种时间差。

## 问题

任务是人形机器人的灵巧操作。同步 VLA 必须等视觉语言骨干算完才能生成后续动作，但机器人在等待时仍在运动，动作依据的观察便越来越旧；增大骨干会直接拖慢闭环反应。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放进托盘”和实时画面；慢模型持续提供任务语义，动作头看到杯子位置变化后结合旧语义更新动作；输出下一段手臂和手部控制。

## 创新点或方法

同步串行计算改成两个并发进程：慢速 System 2 提供语义，快速 System 1 用流匹配生成动作，并通过自己的 ResNet 读取新画面。训练时冻结骨干，用不同步输入模拟部署中的语义滞后；推理时两者经 LCM 通信，动作头独立运行。自适应时间聚合器再对齐重叠动作块，处理推理延迟变化。

### 方法如何工作

1. 慢骨干处理画面与指令，产生语义信息，承担较重的理解计算。
2. 快速动作头读取最新视觉并融合已有语义，避免每次动作都等待骨干。
3. 训练中制造不同步输入，让动作头接触部署时会遇到的旧语义。
4. 并发推理产生重叠动作块，再按时间聚合，使延迟变化下的动作能够衔接。

### 必要术语

- 控制关键路径：执行下一次控制必须等待的计算链；DASH 将慢骨干移出这条链。
- 流匹配动作头：逐步生成动作的模块；本文让它承担快速控制。
- 动作块：一次预测的连续多步动作；不同预测之间可能重叠，需要时间对齐。

## 证据

摘要中的异步 RoboTwin 将推理延迟计入仿真时间：骨干从0.8B扩大到8B时，DASH 保持20 Hz，同步方案从9.7降至4.1 Hz，且 DASH 在各规模成功率更高。真机为带灵巧手的人形机器人，抓放成功率也高于同步方案，但未给具体数字。证据支持所测范围内的控制频率解耦，不能外推为任意硬件上的零延迟。

## 局限

固定20 Hz不等于语义永远及时，也不直接等于端到端反应延迟固定。需要核查严重语义过期时的失败，以及提升分别来自并发、新视觉还是训练方式；摘要未给这些拆分结果。

- **判断**：值得细读训练中的时间错位构造和动作聚合；它直接处理了大骨干部署时可测量的控制瓶颈。

## 研究关联

这里值得借鉴的是按信息更新速度分工：语义可以慢些刷新，接触前的位置变化却需要及时看到。当理解计算成为控制瓶颈时，给快速动作模块独立的新鲜观察入口很有针对性。

### 下一步读哪里

先查语义滞后如何采样、动作头如何融合两路信息，再查聚合器的时间对齐规则；重点核查新视觉、异步训练的消融及真机延迟分布。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-11/Decoupled Asynchronous System for Humanoids (DASH) Latency-Agnostic Scaling of V.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in humanoid dexterous manipulation. We present DASH, a Decoupled Asynchronous System for Humanoids that removes this coupling. DASH splits the policy into a slow vision-language model (System 2) and a fast flow-matching action head (System 1) that run as concurrent processes over the LCM communication protocol, so the control rate is set by the action head alone, independent of backbone size. The action head fuses stale semantics from a frozen backbone with fresh vision from its own ResNet encoder, desynchronized training exposes it to the staleness it meets at deployment, and an adaptive temporal aggregator aligns overlapping action chunks under variable inference latency. On an asynchronous RoboTwin benchmark that charges inference latency in simulated time, DASH holds 20 Hz control rate from 0.8B to 8B backbones while the synchronous rate falls from 9.7 to 4.1 Hz, with higher success at every size. On a real humanoid with dexterous hands, DASH achieves clearly higher pick-and-place success than the synchronous pipeline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.11854v1
- Authors: Bingzhang Wang, Nathan Zhao, Jialeng Ni, Jiajin Zheng, Yin Zhang, Kehua Chen, Jian Yao
- Published: 2026-11-09T04:23:14Z
- Age days: 1

</details>
