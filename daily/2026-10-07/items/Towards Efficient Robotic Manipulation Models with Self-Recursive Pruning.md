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
url: "https://arxiv.org/abs/2610.08555v1"
published: "2026-10-06T15:40:35Z"
age_days: 0
score: 30
created: 2026-10-07
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Towards Efficient Robotic Manipulation Models with Self-Recursive Pruning

> [!summary] 这篇论文到底做了什么（基于摘要）
> LCAM 在不做恢复训练的情况下剪掉机器人策略中的部分连接。它把权重、示范中的激活统计和动作损失敏感度一起用于判断重要性，并在每轮粗剪后重新计算，避免一直沿用原模型的排名。

## 问题

任务是压缩已经训练好的操作策略，同时保住动作表现。通用剪枝常以权重大小、局部重建误差或语言模型似然为依据，这些标准不直接反映闭环控制需要保留什么；摘要称直接用于机器人任务时表现不理想。

### 用一个例子理解

理解用例（非论文实验）：输入一个已有抓取策略和一批示范，LCAM 统计连接的使用情况及动作损失敏感度，逐轮删去低重要性连接并重估，输出一个部分权重为零的抓取策略。

## 创新点或方法

旧做法主要维护通用模型指标；LCAM 加入与动作预测有关的信号。它结合按行归一化的权重贡献、校准示范上的激活矩和输出方向对动作损失的敏感度，给连接排序。随后由粗到细递归剪枝，每轮粗剪后重估重要性；达到稀疏度拐点后，用留出数据上的离线动作失真指导更细的预算分配。这是训练后的校准与裁剪，不需要昂贵的恢复训练或剪枝后的模拟器 rollout。推理使用剪后的策略，具体公式和预算分配规则摘要未说明。

### 方法如何工作

1. 用校准示范收集激活统计和动作损失相关信号，让重要性判断贴近机器人输出。
2. 结合归一化权重贡献给连接排序，决定第一轮粗剪对象。
3. 粗剪后重新校准重要性，适应剩余网络已经改变的状态。
4. 在稀疏度拐点后参考留出动作失真细分预算，得到无需恢复训练的稀疏策略。

### 必要术语

- 非结构化剪枝：删除单个权重连接；本文不要求整层或整通道一起删。
- 激活矩：概括激活分布的统计量；参与估计连接的重要性。
- 动作失真：剪枝后动作输出相对参考输出的偏差；用于指导细剪预算。
- 稀疏度拐点：剪枝过程进入需要更细分配预算的转折位置；摘要未给判定公式。

## 证据

摘要报告三个 LIBERO 套件、多个机器人策略及 OpenVLA 评估。明确数字来自 LIBERO-Object 的 OpenVLA：50% 非结构化剪枝时成功率为 84.0%，保留稠密策略超过 90% 的成功率。这说明该设置下删去一半连接仍能保留大部分任务成功表现；不能据此推定其他套件或更高稀疏度的结果。真机乒乓球只有定性描述，摘要未列对照数值、运行延迟或内存收益。

## 局限

我的待核查问题是离线动作失真能多好地预示闭环成功率，以及校准示范覆盖不足时会怎样。另一个实际边界是：非结构化稀疏不自动等于运行更快，是否加速取决于执行实现和硬件；摘要没有给出这方面证据。

- **判断**：值得读到重要性公式和递归消融，尤其适合判断如何压缩已有策略；部署加速收益仍需单独验证。

## 研究关联

值得借鉴的是用动作行为相关信号决定删什么，并承认删完后剩余连接的重要性会变化。对于已有策略的压缩，先用示范校准、再逐轮重估，是比一次性排序更值得检验的思路。

### 下一步读哪里

下一步核查校准数据量、损失敏感度的计算成本、稀疏度拐点如何确定，以及递归重估相对单次剪枝的收益；同时查看实际硬件上的速度与存储测量。输入没有正文节选。

- **概念**：视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/Towards Efficient Robotic Manipulation Models with Self-Recursive Pruning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Network pruning can reduce parameter redundancy in robotic policies. However, generic pruning criteria are tailored for image recognition tasks and commonly designed to preserve weight magnitude, local reconstruction, or language-model likelihood rather than closed-loop action behavior. Directly applying these pruning algorithms to robotic tasks yields unsatisfactory performance. In this paper, we propose Loss-Conditioned Activation-Moment (LCAM) pruning, a training-free method for unstructured pruning of pre-trained robotic manipulation policies. Specifically, we first rank connections using row-normalized weight contribution, activation moments measured on calibration demonstrations, and the sensitivity of output directions to the action-prediction loss. We further design a self-recursive coarse-to-fine procedure: importance is recalibrated after each nested coarse pruning stage, while held-out offline action distortion guides fine-grained budget allocation after a sparsity knee. Our algorithm is free from costly recovery training and simulator rollouts after pruning. Experiments on three LIBERO suites with competitive robotic policies, together with evaluations on OpenVLA, show that LCAM attains competitive performance across a broad range of pruning ratios. Notably, on LIBERO-Object with OpenVLA, our LCAM achieves 84.0% success at 50% unstructured pruning, retaining over 90% of the dense policy's success rate. Promising results on real-world robotic ping pong further demonstrate the effectiveness of our pruning algorithm.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.08555v1
- Authors: Zijia Chen, Yuenan Hou, Yu Li, Weijie Li, Li Liu
- Published: 2026-10-06T15:40:35Z
- Age days: 0

</details>
