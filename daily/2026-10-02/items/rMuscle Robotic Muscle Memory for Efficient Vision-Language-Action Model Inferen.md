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
url: "https://arxiv.org/abs/2609.19104"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-02
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference

> [!summary] 这篇论文到底做了什么（基于摘要）
> rMuscle 利用机器人重复做相似任务时的内部计算相似性，减少 VLA 每次推理的重复工作。它分别缓存视觉 token 输出和动作阶段的神经元激活模式，对准计算量与权重读取两种开销。

## 问题

重复性工作台任务需要及时、平滑地执行动作，但 VLA 推理延迟会拖慢响应。摘要认为已有推理系统没有充分利用跨次执行的相似性，也没有分别处理不同推理阶段的瓶颈；只把整个模型当成统一计算负载，会错过可复用的部分。

### 用一个例子理解

理解用例（非论文实验）：输入是连续把相同零件放入托盘的图像与指令；系统检索可复用的视觉输出及激活模式，重新计算需要更新的部分；输出仍是针对当前场景生成的动作，同时减少重复推理开销。

## 创新点或方法

常规推理反复处理相近观察和内部状态；rMuscle 改为用双阶段缓存复用它们。Context Cache 复用视觉 token 输出以减少计算，Action Cache 复用神经元激活模式以减少权重访问，并非简单重放旧动作。它用在线缓存重计算、滑动窗口检索和连续去噪步骤间的掩码共享控制存储及查询成本。这是推理系统改动，摘要未说明是否需要额外训练或校准，也未给出命中规则与误差控制细节。

### 方法如何工作

1. 分析重复执行中的观察、轨迹和内部状态，确认哪些相似性能够用于省计算。
2. 复用视觉 token 输出，减少上下文处理阶段的重复计算。
3. 复用动作阶段的激活模式，减少所需权重访问；具体映射方式摘要未说明。
4. 通过重计算、窗口检索和去噪步骤间共享掩码控制缓存成本，再测量速度与任务成功率。

### 必要术语

- 视觉 token：图像经过模型处理得到的特征单元；本文缓存其输出。
- 激活模式：神经元响应的分布或模式；本文利用它减少动作阶段的权重访问。
- 去噪步骤：逐步修正动作候选的迭代过程；本文在连续步骤间共享掩码以减少开销。

## 证据

摘要报告在 RTX 4090 和 Jetson Thor 上，覆盖 LIBERO、RoboTwin 及实体操纵任务，获得 1.29–1.42 倍加速，并在真实机器人上维持原有成功率。未提供各设备、模型与任务分别对应的数值，也未说明测速边界、基线配置及缓存预热成本。因此支持所测工作负载上的效率收益，尚不能确定整机动作周期能缩短多少。

## 局限

真机成功率保持是有用证据，但摘要没有样本数或统计不确定性。遇到物体突变、遮挡或首次任务时，缓存如何失效和恢复仍需核查；平均加速也不能说明最慢几次推理是否改善。

- **判断**：值得读缓存命中、更新规则和分阶段性能测量；重复工作负载下思路明确，但收益是否成立取决于相似性和检索开销。

## 研究关联

可借鉴的是先分析重复发生在哪里，再选择复用层级。画面不必完全相同，内部表示仍可能相似；如果任务持续重复，就值得测量视觉计算和权重读取各占多少时间，再决定缓存什么，而不必先缩小模型。

### 下一步读哪里

先查两个缓存具体存什么、怎样判断可复用和何时重算，再查缓存容量、预热成本与检索时间。性能部分应核查加速覆盖哪些推理阶段，以及场景突然变化时的延迟和成功率。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/rMuscle Robotic Muscle Memory for Efficient Vision-Language-Action Model Inferen.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.19104v2 Announce Type: replace Abstract: Factory work is a promising early scenario for embodied AI: assigning repetitive manual jobs to robots has clear economic payoff, and a structured station keeps the jobs tractable for current policies. Vision-Language-Action (VLA) models now dominate as the policy paradigm for these robots. The inference latency of VLA models directly affects robot responsiveness and motion smoothness. However, existing VLA inference frameworks do not fully exploit the characteristics of embodied workloads or account for the distinct bottlenecks across different stages of VLA inference. In this paper, we first characterize embodied workloads and identify substantial task similarity across repeated robot executions. We further find that such similarity extends beyond observations and action trajectories to internal model states. Drawing on these observations, we present rMuscle, a real-time VLA inference framework inspired by human muscle memory. It exploits cross-execution similarity through a dual-phase muscle-memory cache. The Context Cache reuses visual-token outputs to reduce computation, while the Action Cache reuses neuron activation patterns to reduce weight accesses. We keep both the cache memory footprint and access overhead low through online cache recomputation, sliding-window cache retrieval, and mask sharing across consecutive denoising steps. rMuscle achieves 1.29-1.42X speedup on RTX 4090 and Jetson Thor across LIBERO, RoboTwin, and physical manipulation tasks, while maintaining the original success rates on real-world robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19104
- Authors: Kaijun Zhou, Zhiyang Li, Le Chen, Jinyu Gu
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
