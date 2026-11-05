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
url: "https://arxiv.org/abs/2611.05368v1"
published: "2026-11-03T18:57:35Z"
age_days: 1
score: 36
created: 2026-11-05
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# GUILD: Guided Iterative Data Collection for Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> GUILD 把机器人示教采集变成循环：先建议采什么，再估计新轨迹对目标部署表现有没有帮助，用结果调整下一轮。巧处是把数据筛选的判断前移，让反馈影响尚未花出去的采集预算。

## 问题

机器人模仿学习依赖昂贵的真机遥操作，但采集者凭直觉选择场景，可能反复收集贡献很小的数据。事后筛选能改善训练集，却无法追回已经花掉的采集时间；真正任务是提前决定哪些环境、物体配置和目标值得采。

### 用一个例子理解

理解用例（非论文实验）：目标是让机器人收拾餐具；系统建议采集不同摆放方式，操作者完成示教；评价发现某类遮挡配置的轨迹预计更有帮助，下一轮便优先采它，输出逐轮调整的示教任务。

## 创新点或方法

旧做法是被动收集后再整理；GUILD 交替执行任务提议与采集、数据评价。视觉语言模型先用语义知识提出相关场景，但“语义相关”不保证策略会进步，因此再用预测性数据归因近似估计轨迹对目标部署表现的影响，并反馈到下一轮。它作用于采集和训练流程；最终策略运行时是否使用这些模块，摘要未说明。归因计算及策略更新细节也未给出。

### 方法如何工作

1. 依据目标部署设置，用视觉语言模型提出环境、物体配置和目标，确定下一批采集内容。
2. 按提议收集示教轨迹，获得可用于训练的实际数据。
3. 近似估计新轨迹对目标表现的影响，区分相关数据与可能有效的数据。
4. 将评价反馈给下一轮提议，逐步调整采集方向；具体更新规则摘要只说明到此。

### 必要术语

- 遥操作：人直接操纵机器人完成示范；本文希望提高这类昂贵采集的效率。
- 语义先验：模型已有的场景和任务知识；本文用它提出采集内容。
- 预测性数据归因：估计数据会怎样影响策略表现；本文用它指导下一轮采集。

## 证据

摘要称在仿真与真机中，GUILD 相比被动采集、多种基线及有经验的机器人研究者，提高了样本效率和部署表现。但输入没有任务名称、采集量、成功率、成本或统计波动，因而只能确认作者报告的比较方向，无法判断收益幅度，也无法核对各方是否使用相同预算。

## 局限

我会重点检查评价信号是否准确、成本是否低于它节省的采集，以及它是否过度迎合一个狭窄部署设置。摘要未提供这些信息，不能据此断言作者没有验证；与人类采集者的比较也需核查任务信息和预算是否一致。

- **判断**：值得先读闭环机制和采集预算表，再决定是否深入实现；想法切中成本瓶颈，但摘要不足以评估实际节省。

## 研究关联

这里可借鉴的是区分“场景看起来多样”与“数据对目标策略有用”。如果部署目标较明确，且能低成本估计数据贡献，就值得让贡献反馈决定下一轮示教内容。

### 下一步读哪里

核查预测性归因使用什么目标数据、如何验证预测准确性，以及每轮是否重训策略；比较实验要同时看示教数量、遥操作时间、评价算力和最终部署表现。

- **概念**：多模态基础模型 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-05/GUILD Guided Iterative Data Collection for Imitation Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Imitation learning policies in robotics are trained on datasets collected through costly real-world teleoperation. Often, the data-collection process is unguided, relying on the teleoperator's intuition, resulting in data that contributes little to overall policy performance. Recent work has shown that curating such unguided datasets can substantially improve policy performance, but these approaches operate by filtering existing datasets after collection and therefore do not prevent the acquisition of uninformative data. In this work, we propose GUILD, a novel Guided Data Collection (GDC) method that actively reasons about which data should be collected to maximize downstream policy performance. We introduce an iterative framework that alternates between 1) task proposal and data collection and 2) data evaluation to close the loop. For task proposal, we leverage semantic priors from vision-language models to identify relevant environments, object configurations, and goals for data collection. However, since semantic relevance does not imply policy improvement, we perform data evaluation. By leveraging predictive data attribution we approximate how the collected trajectories influence policy performance on a target deployment setting. This signal is then used as feedback to guide subsequent data collection, closing the data collection loop. We evaluate our approach in simulation and real robot settings, demonstrating that guided data collection substantially improves sample efficiency and deployment performance compared to passive data collection strategies, multiple baselines and experienced roboticists. More information at https://robin-lab.cs.utexas.edu/guild2026/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.05368v1
- Authors: Shivin Dass, Kevin Nguyen, Rohan Yelandur, Junhong Xu, Roberto Martín-Martín
- Published: 2026-11-03T18:57:35Z
- Age days: 1

</details>
