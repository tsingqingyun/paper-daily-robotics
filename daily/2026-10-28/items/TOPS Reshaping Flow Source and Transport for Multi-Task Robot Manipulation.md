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
url: "https://arxiv.org/abs/2610.36694v1"
published: "2026-10-27T06:11:55Z"
age_days: 0
score: 32
created: 2026-10-28
concepts: ["多模态基础模型"]
---

# TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> TOPS 改变流式动作策略“从哪里开始生成”和“沿途怎样推进”：不同任务使用不同起点分布，并调整向专家动作过渡的节奏。它不改网络架构，希望减少不同运动要求挤在同一生成过程中的困难。

## 问题

语言条件多任务操纵中，不同任务需要不同动作分布，常见流策略却共享高斯起点和线性传输路径。共享策略因而需要从同一种初始分布出发，处理差异很大的运动要求，可能增加学习与少步生成的难度。

### 用一个例子理解

理解用例（非论文实验）：输入是“拉开抽屉”；指令选择与拉动动作相适应的生成起点，再按调整后的节奏逐步得到动作序列，输出供机器人执行的轨迹。这里未假定作者验证了特定轨迹形状。

## 创新点或方法

旧做法从统一高斯分布沿共同线性路径生成动作；TOPS 将专家动作序列反向映射，构造包含多个模式的任务起点，让语言指令选择生成从哪里开始。随后根据起点与目标的协方差差异调整插值进度：对需要扩展的方向，前期放缓、后期加快。训练时改变起点与路径设定，推理时按相应设定积分得到动作；起点构建是否需要额外训练及具体成本，摘要未说明。网络架构保持不变。

### 方法如何工作

1. 反向映射专家动作，构造任务相关起点，使生成初态包含动作结构。
2. 用语言选择对应起点分布，让不同任务从更合适的位置开始。
3. 依据起点与目标的协方差差异调整过渡节奏，改变模型需要学习的速度场。
4. 推理时沿该速度场积分生成动作，并检验减少积分步数后的成功率。

### 必要术语

- 流匹配：学习如何把初始样本连续变成目标动作；是本文修改的生成机制。
- 源先验：生成开始时的分布；TOPS 让它随任务变化。
- 插值日程：从起点向目标推进的节奏；用于重塑学习路径。
- 协方差：分布在不同方向上的变化及关联；本文据其差异调整扩展节奏。

## 证据

摘要报告 LIBERO、LIBERO-Plus、CALVIN 上分布内、扰动和跨环境测试及数据效率收益。LIBERO-10 中，单步 TOPS 为 69.67%，十步标准 FM 为 53.44%，推理耗时约为后者六分之一。迁移到 π₀.₅ 后，在四种评估设置中均有收益，但未给数值。真机上层抽屉打开任务从标准 FM 的 20% 升至 80%。这些是不同条件下的独立结果，不能将单个抽屉任务的增幅视为总体真机收益。

## 局限

理论只在高斯端点模型下说明速度预测风险上界可能下降，不能直接保证复杂动作分布或闭环任务成功。还需核查多模态起点对未见指令是否稳定，以及真实任务试验次数；这些条件摘要没有展开。

- **判断**：值得深入读公式与少步推理消融，因为改动位置清晰，但需要分清起点设计和时间安排各自的贡献。

## 研究关联

这里可借鉴的是：生成难学、推理步数多时，可以检查初始分布与生成路径是否适合任务。对于任务动作形态差异明显的共享策略，调整这两项可能比单纯扩大网络更直接。

### 下一步读哪里

下一步核查专家动作如何反向映射、语言怎样选择多模态起点，以及方向相关进度如何实现；重点看相同步数对比和分别移除两项改动的结果。

- **概念**：多模态基础模型
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/TOPS Reshaping Flow Source and Transport for Multi-Task Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow-based policies for language-conditioned multi-task manipulation commonly share a single $\textit{Gaussian}$ source prior and a common linear transport path across tasks. However, reliably executing multiple tasks with distinct motion requirements remains challenging for a shared policy. We introduce $\textbf{TOPS}$ ($\textbf{T}$ask-$\textbf{O}$riented $\textbf{P}$riors and $\textbf{S}$chedules), which adapts the flow source prior and interpolation schedule to each task without modifying the network architecture. TOPS first constructs multimodal task sources from reverse-mapped expert action sequences, allowing language instructions to select where generation begins. Guided by source-target covariance mismatch, it then slows the transition toward expert actions early in denoising and accelerates it later along directions requiring expansion. Under a $\textit{Gaussian}$ endpoint model, our analysis shows that this schedule adjustment can lower an upper bound on velocity-prediction risk. Experiments on LIBERO, LIBERO-Plus, and CALVIN demonstrate improved performance across in-distribution, perturbation and cross-environment settings, alongside better data efficiency. Using one integration step, TOPS raises LIBERO-10 success from $53.44\%$ to $69.67\%$ compared with ten-step Standard Flow Matching (FM), while reducing inference time to approximately one-sixth of the baseline. TOPS also yields consistent gains when transferred to the large-scale flow-based $π_{0.5}$ policy across all four evaluated settings. Real-world experiments further demonstrate improved task success, including an increase from $20\%$ with standard FM to $80\%$ with TOPS on the upper-drawer opening task.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36694v1
- Authors: Tuo An, Chuhao Zhou, Jiahua Dong, Jingliang Li, Jiaqi Bai, Jindou Jia, Jianfei Yang
- Published: 2026-10-27T06:11:55Z
- Age days: 0

</details>
