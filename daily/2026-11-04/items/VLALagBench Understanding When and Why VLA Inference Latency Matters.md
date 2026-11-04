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
url: "https://arxiv.org/abs/2611.03103"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 39
created: 2026-11-04
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLALagBench: Understanding When and Why VLA Inference Latency Matters

> [!summary] 这篇论文到底做了什么（基于摘要）
> VLALagBench 研究机器人“想得慢一点”究竟会损失多少成功率，并发现损失取决于任务、目标速度和策略。它还用少量校准数据拟合成功率，让推理系统可以按实际延迟和吞吐量选择执行配置。

## 问题

VLA 根据观察计算动作时，物理世界仍在变化，因此算完的动作可能已经不适合当前状态。真正缺少的是延迟与任务失败之间可量化的关系：同样的计算时间，对静态操作和追踪移动目标可能有完全不同的影响。

### 用一个例子理解

理解用例（非论文实验）：相机看到传送带上的物体，VLA 计算抓取动作时物体继续移动；给定系统延迟与请求能力，预测模型比较执行配置，输出预计成功率更高的配置。

## 创新点或方法

本文将任务类型、物体速度、同步或异步执行以及 VLA 策略放进共同评估条件，观察延迟敏感性。同步与异步的关键差异是推理能否和动作执行重叠；异步可减少等待，但需要更频繁地请求推理。随后作者用有限校准数据建立经验预测模型，根据系统延迟和每台机器人可用吞吐量选择算法配置。摘要未说明重新训练策略，主要描述的是运行评估和配置选择；预测模型的形式未提供。

### 方法如何工作

1. 选定任务、物体速度和策略，测量不同延迟下的成功率，得到任务对延迟的敏感程度。
2. 比较同步与异步执行，检验推理和动作重叠能挽回多少表现，以及需要多少额外请求。
3. 用有限校准结果拟合成功率预测模型，降低逐一穷举配置的测试成本。
4. 输入系统延迟和每台机器人的吞吐量，比较可行配置并选择预计成功率更高者；具体搜索规则摘要未说明。

### 必要术语

- 推理延迟：模型从输入到给出动作所需的时间；本文研究这段等待如何影响任务。
- 异步执行：动作运行时同时计算后续动作；本文用它缓解等待造成的损失。
- 吞吐量：单位时间内系统能提供的推理次数；本文用它限制可选配置。
- 均方根误差：衡量预测值与实际值差距的指标；本文用它检验成功率预测。

## 证据

摘要报告，移动目标任务中，100 ms 推理延迟就可能使成功率接近减半，但这不是所有任务和策略的统一降幅。异步执行能挽回部分损失，同时增加推理请求频率。成功率预测在多种 VLA 策略上的均方根误差为 5.7–7.8%；摘要未交代策略名称、任务数量、校准样本量、误差表示口径或评估环境，无法据此推断任意真机系统的预测精度。

## 局限

异步收益不能脱离计算预算理解：更频繁的请求可能在多机器人共享系统时不可持续。经验模型是否能跨目标速度、硬件和未见任务使用，需要检查校准与测试如何划分；摘要没有给出这些边界。

- **判断**：部署前值得读方法和延迟曲线，尤其要看预测模型在哪些条件内可靠，而不是只记住 100 ms 这个数字。

## 研究关联

值得借鉴的是按闭环任务表现选择系统配置：更慢但单次预测更好的模型，未必在快速变化的任务上更好。实际比较模型时，应把延迟和可持续请求频率一起纳入实验条件。

### 下一步读哪里

核查延迟如何施加、是否包含通信和动作执行，异步如何处理旧动作，以及校准模型能否预测未参与拟合的任务；同时检查请求量与成功率的共同变化。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/VLALagBench Understanding When and Why VLA Inference Latency Matters.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2611.03103v1 Announce Type: new Abstract: Vision-language-action (VLA) models offer a promising path toward general-purpose robot manipulation. While inference latency can affect task success in a constantly evolving physical world, the relationship between latency and task success rate remains poorly understood. In this paper, we introduce VLALagBench, a comprehensive benchmark for studying VLA inference latency sensitivity across task types, object speeds, execution modes (synchronous and asynchronous), and VLA policies. Using VLALagBench, we find that even a modest inference latency of 100 ms can nearly halve task success on moving targets, with sensitivity varying substantially across tasks and policies. These differences reflect task-specific requirements for precision and continuous motion. By overlapping inference with action execution, asynchronous execution can recover some of the lost success at the cost of more frequent inference requests. Building on these findings, we develop an empirical model that predicts task success from limited calibration data, achieving root-mean-square prediction errors of only 5.7-7.8% across various VLA policies. Given an inference system's latency and per-robot throughput, these predictions guide the selection of system-specific VLA algorithm configurations to maximize task success. We believe VLALagBench and these findings provide a solid foundation for future robotics algorithm-system co-design.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.03103
- Authors: Qi Wen, Borui Xu, Hussein Amro, Hongshi Tan, Hanmin Lin, Chaoyi Ruan, Shanghao Liu, Gang Yang, Yuejiang Liu, Jiafei Duan, Bingsheng He, Jason Clemons, Christos Kozyrakis, Wenqi Jiang
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
