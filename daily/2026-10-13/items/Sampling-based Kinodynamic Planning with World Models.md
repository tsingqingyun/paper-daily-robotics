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
url: "https://arxiv.org/abs/2610.12910v1"
published: "2026-10-09T03:01:00Z"
age_days: 3
score: 30
created: 2026-10-13
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Sampling-based Kinodynamic Planning with World Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> 机器人有时必须先绕路，才能把物体推到目标；只优化眼前目标距离的规划器容易卡住。本文让世界模型预测动作后果，再用 RRT 和 KPIECE 在预测状态中长出搜索树，探索暂时没有收益的中间动作。

## 问题

任务是从图像出发，规划满足机器人运动约束的动作序列。瓶颈不是能否预测下一帧，而是能否找到长程必要的绕行动作：摘要指出，CEM、MPPI 在目标函数不奖励这类动作时会停滞。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和推块目标；模型预测机器人绕到块后方的结果，搜索树保留这条暂时不缩短目标距离的分支；随后找到向目标推动的路径，输出动作序列。

## 创新点或方法

旧做法反复优化动作序列；本文把学到的世界模型当作状态推进器，让树搜索保留并扩展中间状态。RRT 用最近邻引导探索，KPIECE 借助投影组织探索，并在 GPU 上批量扩展。实验直接使用现成 DINO-WM；摘要未说明额外训练，核心改动发生在规划阶段。

### 方法如何工作

1. 把当前图像转成模型使用的潜在状态，作为搜索起点。
2. 用最近邻或投影策略选择扩展位置，让探索覆盖不同中间状态。
3. 批量提出动作并由世界模型预测后继状态，形成新的树分支。
4. 继续扩展通向目标的分支，得到候选动作路径；执行与重规划细节摘要未说明。

### 必要术语

- 潜在空间：图像压缩后的状态表示；本文在其中搜索动作后果。
- 传播器：给定状态和动作，计算下一状态；本文由世界模型承担。
- RRT / KPIECE：两类采样式运动规划方法；本文用它们组织中间状态探索。

## 证据

摘要报告四个仿真领域和一个真机推块任务，对比 CEM、MPPI。仿真成功率持平或更高，规划耗时最多降低至对应基线的约 1/13.8；真机成功率提高 20%。摘要未给各任务数值、试验次数，也未说明 20% 是相对增幅还是百分点；不能把最佳加速视为所有任务的收益。

## 局限

树搜索仍依赖世界模型预测；长路径上的误差会不会产生现实中不可执行的方案，是我的待核查问题。摘要没有交代预测误差、潜在空间距离和真机重规划如何处理，仿真加速也不能直接外推到真机。

- **判断**：值得读到搜索策略和计算预算对比的细节，因为它提供了一个明确诊断：规划失败可能来自探索不足。

## 研究关联

遇到需要先退后进的任务，可以先检查搜索方式是否排斥必要中间状态，而不急着更换预测模型。这里值得借鉴的是保留探索分支，让短期目标分数低的状态也有继续发展的机会。

### 下一步读哪里

我会先核查潜在状态如何定义距离、KPIECE 投影如何选择，再看相同时间预算下的成功率，以及长程预测错误如何影响真机执行。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/Sampling-based Kinodynamic Planning with World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual world models predict the consequences of actions from images, but planning with them is typically done by optimizers such as CEM and MPPI. However, these optimizers stall on long-horizon tasks where progress requires motion the objective does not reward, such as moving around a block before pushing it. This paper revisits kinodynamic sampling-based motion planning for world models, using the learned model as the propagator of a tree search in latent space. Our key insight is that the sampling strategies devised for high-dimensional search in configuration space apply directly to the latent space of a world model, where they rapidly expand through intermediate states that myopic optimizers never sample. We present two exploration strategies for the high-dimensional latent space, nearest-neighbor-guided RRT and projection-based KPIECE, with GPU-native batched expansion for efficient device utilization. We evaluate with an off-the-shelf DINO-WM on four simulated domains and a real-world block-pushing task. Our approaches match or exceed the success rate of CEM and MPPI at up to 13.8x lower planning time in simulation, and improve the success rate by 20% on the real robot.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12910v1
- Authors: Yitian Gao, Hanlan Yang, Zachary Kingston
- Published: 2026-10-09T03:01:00Z
- Age days: 3

</details>
