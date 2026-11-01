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
url: "https://arxiv.org/abs/2610.40401v1"
published: "2026-10-29T16:34:54Z"
age_days: 2
score: 31
created: 2026-11-01
concepts: ["世界模型"]
---

# Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors

> [!summary] 这篇论文到底做了什么（基于摘要）
> CoAWM 把一段机器人动作表示成可以按时间查询的函数，而不固定成某个频率下的一串动作。它先从不同机器人、不同采样频率的轨迹中学习共享表示，再根据观测、语言和机器人状态选择具体动作函数。

## 问题

任务是跨机器人形态和执行频率生成动作。不同来源的轨迹在动作组织和时间采样上不一致，直接共用固定格式序列会限制数据整合。摘要没有逐项比较既有方法，而是把异构轨迹难以共享时空动态规律作为需要解决的障碍。

### 用一个例子理解

理解用例（非论文实验）：输入以不同频率记录的两种机械臂搬物轨迹，预训练得到共享函数表示；随后输入当前画面、“把物体移到右侧”和机器人状态，预测动作函数，再按目标控制器需要的时刻查询动作。是否能成功迁移仍需验证。

## 创新点或方法

相较于把动作绑在固定时间网格上，本文把共享规律放进潜在函数空间，再把任务选择和时间采样分开。训练分两阶段：先用动作重建及不同时间采样视图间的一致性学习函数表示，再将其接入世界模型骨干，学习根据任务条件预测潜在动作函数。推理时，一个解码器接收查询时刻，输出对应末端执行器动作。具体如何统一机器人坐标和动作语义，摘要未说明。

### 方法如何工作

1. 把异构轨迹送入函数预训练，通过动作重建学习能表达轨迹的潜在空间。
2. 约束同一轨迹在不同采样视图下的一致性，减少表示对记录频率的依赖。
3. 接入世界模型骨干，用观测、语言和当前状态预测任务所需的潜在动作函数。
4. 向统一解码器查询具体时刻，得到对应末端动作，使表示与输出采样时间分离。

### 必要术语

- 跨形态：在不同机器人之间共享经验；这是本文希望支持的迁移范围。
- 潜在动作函数：用压缩表示描述动作随时间的变化；它是两阶段训练的接口。
- 时间采样一致性：不同采样方式应保留相容信息；本文用它学习共享动态规律。

## 证据

摘要没有给出实验任务、机器人数量、控制频率范围、对比方法、指标或结果。因此，目前能明确复述的是两阶段设计，不能据此认定已经实现有效的跨形态迁移，或在未见执行频率下保持成功率。扩大预训练数据来源是该表示设计的动机，其实际收益仍需实验核查。

## 局限

这里最需要核查的，是共享末端动作表示如何保留不同机器人的执行约束。能在任意时刻查询函数，也不等于机器人能在任意控制频率下稳定执行。输入没有验证细节，无法区分训练中覆盖频率的适配和真正未见频率的迁移。

- **判断**：值得先读动作表示与解码定义；在看到跨机器人、跨频率实验前，把它当作有明确动机的表示方案。

## 研究关联

可借鉴的是把“动作随时间怎样变化”与“控制器多久取一次动作”拆开。如果多份数据主要因采样频率不同而难以合用，连续函数表示提供了一个合理切入点；但它不会自动消除机器人运动学和可达范围的差异。

### 下一步读哪里

优先核查动作坐标系、单位、时间归一化和机器人身份如何处理，再看一致性约束如何构造，以及测试是否隔离了未见机器人和未见频率。

- **概念**：世界模型
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-01/Continuous-Action World Models Learning Cross-Embodiment Spatiotemporal Dynamics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce Continuous-Action World Models (CoAWM), a framework for learning cross-embodiment spatiotemporal dynamics priors that support robot action generation across embodiments and execution frequencies. At its core is a shared latent function space that captures the spatial and temporal structure of robot actions. We learn this space through two stages. First, function pretraining brings trajectories from different embodiments and sampling frequencies into a common representation, learning shared dynamics priors through action reconstruction and consistency across temporal sampling views. By accommodating heterogeneous robot trajectories, this stage broadens the range of data sources available for pretraining and facilitates scaling to larger and more diverse datasets. Second, we connect the pretrained function space to a world-model backbone, enabling observations, language instructions, and the current robot state to condition the prediction of a latent action function. A single decoder takes any query time and returns the corresponding end-effector action. By separating shared dynamics priors from task-conditioned action selection and temporal sampling, our approach provides a unified foundation for transferring robot experience across embodiments and control frequencies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.40401v1
- Authors: Liangyu Li, Qingwen Liu
- Published: 2026-10-29T16:34:54Z
- Age days: 2

</details>
