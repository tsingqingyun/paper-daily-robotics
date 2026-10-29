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
url: "https://arxiv.org/abs/2610.36662v1"
published: "2026-10-27T05:28:28Z"
age_days: 1
score: 26
created: 2026-10-29
concepts: ["智能体 Agent", "世界模型"]
---

# SWIM: Learning What Matters from Behaviors for JEPA World Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> SWIM 用离线行为数据学习哪些物理状态差异更值得世界模型保留：能帮助解释动作的状态特征获得相应权重。训练时用这些权重约束图像表征，规划时仍只需图像，不增加逆动力学模型的计算。

## 问题

JEPA 世界模型通过预测未来图像表征支持规划，但视觉预测目标不保证保留决定任务进度的物理状态。加入仿真状态监督后，又必须决定重视哪些特征：人工挑选依赖经验，标准化后统一加权则可能重复计算冗余坐标，并让无关变化掩盖任务差异。

### 用一个例子理解

理解用例（非论文实验）：输入推块轨迹，包含图像、物块与机械臂状态及动作；SWIM 学习哪些状态差异有助于解释动作，再据此训练图像表征；规划时输入当前和目标图像，利用世界模型比较候选动作序列并输出动作。

## 创新点或方法

旧做法把选定状态特征等权处理；SWIM 从离线轨迹中的当前状态、未来位移和记录动作学习权重。其逆动力学模型预测产生这些变化的动作，各特征对动作预测的贡献用于定义加权状态距离。训练世界模型时，让潜在表征距离与这一状态距离对齐，促使表征保留行为相关差异。逆动力学模型只在训练时使用，最终规划从图像进行；权重计算公式和距离对齐损失未在摘要展开。

### 方法如何工作

1. 从离线轨迹提取当前状态、未来位移和记录动作，为学习行为相关性提供监督。
2. 训练逆动力学模型预测记录动作，得到各状态特征对预测的贡献。
3. 将贡献转成状态权重并定义距离，用它与潜在距离对齐，改变世界模型训练时重视的差异。
4. 规划时只运行图像世界模型，利用预测的未来表征选择动作；逆动力学模型不参与此阶段。

### 必要术语

- JEPA：预测未来表征而非逐像素图像的学习方式；本文用它构建视觉世界模型。
- 逆动力学：根据状态及其变化推断动作；本文用它学习状态特征的权重。
- 加权状态距离：不同状态特征按不同权重计算的差异；它为表征训练提供监督尺度。

## 证据

摘要报告，在五个仿真机器人操作任务中，SWIM 相比统一状态加权持续提高规划成功率。这支持它在所测任务中比等权监督更有利于规划；摘要没有任务名称、成功率数值、波动范围或其他基线结果，因此无法判断收益大小，也无法比较它与人工选特征等方案的优劣。

## 局限

帮助预测动作的特征，不必然就是完成目标所需的特征：离线数据也可能包含行为习惯带来的相关性。这是我会重点核查的问题，不能把所学权重直接解释为因果重要性。证据来自仿真操作，尚不能据此判断真实视觉误差下的效果。

- **判断**：值得读权重学习与距离对齐的细节；它为状态监督提供了明确替代方案，但能否迁移取决于离线行为数据覆盖了什么。

## 研究关联

这里可以借鉴的是，用行为数据决定监督信号应强调什么，而不是默认每个状态坐标同样重要。当可获得状态和动作轨迹、但难以手工分配权重时，这提供了一种可检验的替代办法，同时把额外成本放在训练阶段。

### 下一步读哪里

先核查特征贡献如何转成权重、相关特征如何处理，以及距离对齐是否保留视觉预测能力；再看五项任务的逐项成功率、数据覆盖变化和与其他加权方法的比较。没有正文节选可进一步定位。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/SWIM Learning What Matters from Behaviors for JEPA World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Joint-embedding predictive architectures (JEPAs) enable world models to plan from images by predicting future embeddings. However, their visual prediction objectives do not explicitly incorporate task-relevant state information, so the physical state that determines task progress may not be reliably captured in the latent space. Supervising world models with simulator state can make planning more informative, but it requires deciding which state features matter. Features are typically selected by hand or weighted uniformly, and a uniform weighting gives every standardized state feature equal influence, so redundant coordinates can overcount the same variation, while irrelevant ones can obscure task-relevant differences. To address this limitation, we propose SWIM (State Weighting with Inverse-Dynamics Model), which learns state weights from offline trajectories by predicting recorded actions from current states and observed future displacements. The learned weights quantify each feature's contribution to action prediction and define a weighted state metric for state-supervised training, which we demonstrate by aligning latent and state distances. The inverse-dynamics model is used only during training, so the resulting world model plans from images with no additional planning-time computation. Across five simulated robotic manipulation tasks, SWIM consistently improves planning success over uniform state weighting.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36662v1
- Authors: Jiaming Hu, Shi Bo, Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Vianne Gao, Houyu Zhang, Qingjun Cui
- Published: 2026-10-27T05:28:28Z
- Age days: 1

</details>
