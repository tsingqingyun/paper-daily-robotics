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
url: "https://arxiv.org/abs/2609.37772v1"
published: "2026-09-29T15:13:14Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control

> [!summary] 这篇论文到底做了什么（基于摘要）
> UAD 抓住一个简单事实：机器人现在只急着用第一步动作，后面的动作可以晚一点算完。它先交付近期动作，边执行边细化后续动作，再补偿提前交付造成的误差；摘要报告这能缩短动作等待时间，并保持相当的任务成功率。

## 问题

扩散和流匹配 VLA 通常一起生成一段动作，反复去噪后才能交付，导致机器人等待。摘要指出，现有加速方法把整段动作当成一个计算单元，忽略执行顺序：第一步现在就要用，末尾动作还有计算余裕。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“拿起杯子”；UAD 先交付伸手的近期动作，机器人移动时继续细化靠近杯柄的动作，并补偿早期偏差；输出是陆续可执行、持续调整的一段控制指令。

## 创新点或方法

旧做法是整段一起等；UAD 改成紧急动作少去噪几步就释放，尾部继续在后台细化，与物理执行重叠。但前面提前结束会产生误差，也会破坏整段联合去噪的一致性。Trajectory Reconciliation 重建统一的内部状态演化，无须额外模型求值；Ghost Action Correction 利用不实际执行的延续动作，把早期误差补偿到剩余可执行动作。它是推理时框架；摘要未说明是否需要配套训练，也未给出补偿公式。

### 方法如何工作

1. 按动作的预计执行时刻区分紧急程度，给后面的动作保留更多计算时间。
2. 先释放少量去噪后的紧急动作，使机器人开始执行，同时继续细化尾部。
3. 重建统一内部状态，恢复不同去噪进度之间的协调，避免尾部沿不一致轨迹演化。
4. 利用不执行的 ghost 延续补偿剩余动作中的早期误差；摘要只说明到此，未给出误差映射细节。

### 必要术语

- 动作块：一次预测的一段连续动作；本文利用它们依次被执行的时间差。
- 去噪：逐步把噪声动作变成可执行动作；本文按紧急程度分配迭代次数。
- 滚动时域控制：执行近期动作后持续更新后续计划；它使远期动作拥有更多计算余裕。

## 证据

摘要报告跨多种 VLA 架构、仿真基准和真机操作任务测试：平均动作可用延迟最高加速 1.89 倍，成功率与采用最优去噪预算的原始推理相当，成功率与延迟的权衡优于现有加速基线。未列任务名、基线名、绝对延迟、成功率及重复次数；因此只能支持所测条件下的加速，不能推出所有任务都快 1.89 倍或整项任务同幅度提速。

## 局限

作者明确指出的挑战是提前释放误差和尾部轨迹不一致，摘要未列剩余局限。我会重点核查：快速接触时误差是否仍可补救，硬件并行能力是否影响收益，以及两种机制各自贡献多少。仿真和真机结果未分列，不能假定收益一致。

- **判断**：适合排查实时控制的等待问题。先核对自己的硬件能否同时执行与推理，再看提前动作的误差在接触任务中是否补得回来。

## 研究关联

如果模型推理让机器人一直等，可以检查计算是否非得整段一起完成，尝试把计算顺序对齐动作的实际执行时间。评测时要分别量首动作等待、后续动作是否及时到达和总任务耗时，才能知道用户真正感受到的提速有多少。

### 下一步读哪里

下一步核查紧急度如何设定、内部轨迹如何重建、ghost 延续如何估计误差，以及墙钟延迟是否计入全部协调开销；查看两个机制的独立消融和真机接触任务表现。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Urgent Actions Go First Urgency-Aware Denoising for Real-Time VLA Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Diffusion and flow-matching Vision-Language-Action (VLA) policies generate action chunks through iterative denoising, incurring substantial inference latency that severely limits real-time robotic control. Existing acceleration methods treat an action chunk as a monolithic computational unit, ignoring a crucial physical reality of receding-horizon control: actions are generated jointly but consumed sequentially, resulting in inherently heterogeneous execution urgencies. We exploit this asymmetry to introduce Urgency-Aware Denoising (UAD), a novel inference-time framework that allocates denoising computation according to when each action is physically needed. UAD releases time-critical urgent actions after fewer denoising steps while overlapping the continued background refinement of tail actions with physical execution. However, heterogeneous denoising introduces two key challenges: early-release errors in urgent actions and trajectory inconsistency in tail actions. UAD elegantly resolves both through two core mechanisms: Trajectory Reconciliation, which reconstructs unified internal state evolution to restore joint denoising coherence without additional model evaluations, and Ghost Action Correction, which leverages non-executed ghost continuations to dynamically compensate for early-release errors across remaining executable actions. Extensive evaluations across multiple VLA architectures, simulation benchmarks, and real-world manipulation tasks demonstrate that UAD achieves up to a 1.89x speedup in average action availability latency while maintaining comparable success rates to vanilla inference with optimal denoising budget, offering a more favorable success-latency trade-off than state-of-the-art VLA acceleration baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37772v1
- Authors: Zibo Wang, Haochen Han, Pengzhen Ren, Mingtong Dai, Fangming Liu
- Published: 2026-09-29T15:13:14Z
- Age days: 0

</details>
