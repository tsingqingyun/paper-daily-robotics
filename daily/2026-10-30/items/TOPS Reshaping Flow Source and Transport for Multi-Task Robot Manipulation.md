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
url: "https://arxiv.org/abs/2610.36694"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 32
created: 2026-10-30
concepts: ["多模态基础模型"]
---

# TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> TOPS 改变流策略生成动作时“从哪里出发、沿途多快靠近目标”。它为不同任务准备不同的起始分布和变化节奏，让同一个网络用更少生成步骤完成多任务操作。

## 问题

语言条件多任务策略要生成运动要求不同的动作序列，但常见流方法共享一个高斯起点和线性变化路径。这样的统一设置可能让部分任务需要学习更复杂的搬运过程，少步推理尤其难准确完成。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放到托盘上”和场景观测；TOPS 根据语言选择相应动作起始分布，网络按调整后的节奏把起始样本变成搬运动作序列，输出供机器人执行的动作。

## 创新点或方法

旧做法从共同噪声出发，按统一节奏变成动作；TOPS 将专家动作序列反向映射，构造可有多个模式的任务起始分布，再由语言选择起点。它还依据起点与目标的协方差差异，在需要扩展的方向上先慢后快地向专家动作过渡。训练涉及新的起始样本和插值日程，网络结构保持不变；推理从任务对应的分布开始，沿学到的流积分生成动作。反向映射、语言选择和日程计算的具体实现未在摘要展开。

### 方法如何工作

1. 把专家动作反向映射为起始样本，得到更贴近不同任务需求的生成来源。
2. 根据源与目标的协方差差异调整变化节奏，减少某些方向上的学习困难。
3. 使用调整后的起点和路径训练速度预测网络；摘要未给出完整损失及训练顺序。
4. 推理时由语言选起始分布，再用少量积分步骤得到动作序列，以减少生成耗时。

### 必要术语

- 流匹配：学习把起始分布连续变成目标分布的运动规则；本文目标分布是专家动作。
- 多模态分布：存在多个高概率区域的分布；本文允许任务起点保留多种模式。
- 协方差：描述各方向变化幅度及共同变化关系；本文据其差异调整生成节奏。
- 积分步：沿预测变化方向推进一次；步数直接影响推理成本。

## 证据

摘要报告 LIBERO、LIBERO-Plus、CALVIN 上分布内、扰动和跨环境测试的改善，并称数据效率更好。LIBERO-10 上，一步 TOPS 成功率为 69.67%，十步标准 FM 为 53.44%，推理时间约为后者六分之一。迁移到 π₀.₅ 后，四种受测设置均有收益；真机上层抽屉任务从标准 FM 的 20% 提高到 80%。这些是特定设置的结果，不能据此断言所有任务均可用一步替代十步。

## 局限

理论结论限定在高斯端点模型下，且降低的是速度预测风险的一个上界，不直接保证真实操作成功。我的待核查问题是新任务如何获得起始分布，以及反向映射的成本是否计入总体开销；真机成功率还需结合试验次数判断。

- **判断**：值得细读起始分布构造和日程公式，因为它提供了不改网络结构、直接改生成过程的可操作思路。

## 研究关联

这里值得借鉴的是：生成任务困难，可能部分源于起点和路径选得不合适。若不同任务的动作分布差别明显，可以先检查生成过程是否给网络增加了不必要的学习负担，再考虑扩大模型。

### 下一步读哪里

先核查反向映射是否需要预训练策略、起始分布如何保留任务内多种动作方式；再比较相同步数和相同时间预算的结果，并查看先验与日程分别贡献多少。

- **概念**：多模态基础模型
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/TOPS Reshaping Flow Source and Transport for Multi-Task Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.36694v1 Announce Type: cross Abstract: Flow-based policies for language-conditioned multi-task manipulation commonly share a single $\textit{Gaussian}$ source prior and a common linear transport path across tasks. However, reliably executing multiple tasks with distinct motion requirements remains challenging for a shared policy. We introduce $\textbf{TOPS}$ ($\textbf{T}$ask-$\textbf{O}$riented $\textbf{P}$riors and $\textbf{S}$chedules), which adapts the flow source prior and interpolation schedule to each task without modifying the network architecture. TOPS first constructs multimodal task sources from reverse-mapped expert action sequences, allowing language instructions to select where generation begins. Guided by source-target covariance mismatch, it then slows the transition toward expert actions early in denoising and accelerates it later along directions requiring expansion. Under a $\textit{Gaussian}$ endpoint model, our analysis shows that this schedule adjustment can lower an upper bound on velocity-prediction risk. Experiments on LIBERO, LIBERO-Plus, and CALVIN demonstrate improved performance across in-distribution, perturbation and cross-environment settings, alongside better data efficiency. Using one integration step, TOPS raises LIBERO-10 success from $53.44\%$ to $69.67\%$ compared with ten-step Standard Flow Matching (FM), while reducing inference time to approximately one-sixth of the baseline. TOPS also yields consistent gains when transferred to the large-scale flow-based $\pi_{0.5}$ policy across all four evaluated settings. Real-world experiments further demonstrate improved task success, including an increase from $20\%$ with standard FM to $80\%$ with TOPS on the upper-drawer opening task.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36694
- Authors: Tuo An, Chuhao Zhou, Jiahua Dong, Jingliang Li, Jiaqi Bai, Jindou Jia, Jianfei Yang
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
