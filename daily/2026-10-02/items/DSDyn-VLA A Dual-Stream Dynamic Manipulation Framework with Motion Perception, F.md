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
url: "https://arxiv.org/abs/2609.39198"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-02
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DSDyn-VLA: A Dual-Stream Dynamic Manipulation Framework with Motion Perception, Future Awareness, and Realtime Correction

> [!summary] 这篇论文到底做了什么（基于摘要）
> DSDyn-VLA 让机器人操作移动中的物体：慢速规划器利用运动信息，提前考虑动作执行时的状态；快速策略则在执行过程中不断纠偏。它把“计划得合适”和“来得及修正”分给两个速度不同的处理流。

## 问题

传送带上的物体不会等模型算完。摘要指出三个瓶颈：静态图像看不出运动趋势，推理完成时观测已过时，一整段动作开环执行又无法追踪新变化。因此，单次生成质量不错的动作，也可能在执行时落空。

### 用一个例子理解

理解用例（非论文实验）：输入是连续相机图像和“拿起传送带上的盒子”；慢流据运动趋势规划接近动作，快流在盒子位置变化时持续修正，输出随实时观测调整的机械臂动作。

## 创新点或方法

相对静态视觉输入和开环动作块，慢速 Flow-Planner 加入光流感知运动，并用未来状态感知补偿推理延迟，生成连续动作块。快速 Res-Refiner 根据实时观测，用轻量强化学习策略向动作块加入高频修正。训练方面只明确后者使用强化学习，规划器如何训练、未来状态如何监督均未说明；推理时两者分别负责较长范围的规划和即时闭环调整。

### 方法如何工作

1. 从视觉序列提取光流，为规划器补上单张图像缺少的运动线索。
2. 结合未来状态感知生成动作块，使计划考虑推理结束后的场景；摘要未说明具体预测机制。
3. 执行过程中用最新观测计算快速残差，修正动作块无法预先覆盖的偏差。
4. 以修正后的动作持续控制机器人，让新的观测有机会在整段动作结束前影响执行。

### 必要术语

- 光流：图像中像素随时间移动的估计；本文用它提供运动线索。
- 动作块：一次生成的一段动作序列；本文由慢流规划，再由快流修正。
- 残差修正：在原计划上加一个调整量；本文用它快速应对实时偏差。
- 闭环控制：执行中不断根据新观测调整动作；本文用它补足开环执行的缺陷。

## 证据

摘要报告：在 Kinetix 动态基准的高延迟设置中，相对当前最佳方法，失败率降低超过 76%；真实动态场景成功率约为 PI0.5 的 6 倍，在 DynBench 上约为其 5 倍。DynBench 基于 MuJoCo，包含九项任务。摘要未给绝对成功率、高延迟数值、真机任务构成及重复次数；失败率相对下降和成功率倍数也不能当作百分点提升。

## 局限

我的待核查问题是：收益分别有多少来自光流、提前规划和快速纠偏？真实部署还取决于端到端观测延迟及控制频率。摘要承诺开源代码和权重，只能理解为计划，不能据此认定已经发布。

- **判断**：值得读到双流接口和延迟消融，因为方法能否复用，关键在快慢两路如何协调，而不只在各自模型有多强。

## 研究关联

值得借鉴的是按时间尺度分工：复杂模型可以低频决定一段动作，再由便宜的反馈控制持续修正。物体运动快、模型推理慢时，应同时检查计划是否考虑延迟，以及执行是否能追上变化。

### 下一步读哪里

先核查未来状态感知如何实现、动作块与残差怎样合成，再检查各模块消融及不同延迟下的结果；真机部分需看绝对成功率、物体速度、硬件算力和控制周期。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/DSDyn-VLA A Dual-Stream Dynamic Manipulation Framework with Motion Perception, F.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.39198v1 Announce Type: new Abstract: While Vision-Language-Action (VLA) models excel in static tasks, they struggle in dynamic environments where objects are in motion (e.g., conveyor belt manipulation). We identify three fundamental limitations hindering current VLAs in these scenarios: the \textbf{perception gap}, where static visual inputs lack temporal motion cues; the \textbf{latency gap}, where inference delays render actions obsolete; and the \textbf{control gap}, caused by the open-loop action chunk execution without real-time adjustment. In this work, we propose \textbf{DSDyn-VLA}, a Slow-Fast \textbf{D}ual-\textbf{S}tream \textbf{Dyn}amic manipulation framework that integrates motion-aware foresighted planning with real-time residual correction. The slow \textbf{Flow-Planner} serves as a macro-planner. By enhancing the VLA with optical flow for temporal perception and a future state awareness mechanism to preemptively offset inference latency, it produces globally consistent, motion-aware action chunks. Complementing this, the fast \textbf{Res-Refiner} employs a lightweight RL policy to inject high-frequency, closed-loop corrections into the planned action chunks based on real-time observations. In addition, we introduce \textbf{DynBench}, a MuJoCo-based benchmark for dynamic object manipulation that comprises nine tasks. Extensive experiments demonstrate that DSDyn-VLA reduces the failure rate by over 76\% compared to current SOTA method in high-latency setting on the Kinetix dynamic benchmark, while achieving about 6$\times$ the success rate of PI0.5 in real-world dynamic settings and about 5$\times$ on DynBench. We will open-source all the code and weights.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.39198
- Authors: Wenhao Li, Xiu Su, Yu Han, Yichao Cao, Shan You, Chang Xu
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
