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
url: "https://arxiv.org/abs/2611.01112"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 35
created: 2026-11-04
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Auriga 处理的是“模型知道该做什么，机械臂却没做好”：给模型准确的空间测量和控制工具，并在运动前预览、运动中检查偏差。模型负责决策，执行系统负责把动作变成可检查、可中止、可原地修正的过程。

## 问题

具体任务是零样本具身操作。摘要用 RoboDojo 展示瓶颈：参考接口下 GPT-6 Astra 成功率为 22.5%，移除机械臂执行环节后为 76.2%，说明高层决策与物理执行之间存在明显落差；仅有理解和规划能力不足以保证动作落地。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放进托盘”和场景图像；模型获取三维位置、生成抓放程序并检查轨迹；若执行时杯子偏离声明范围，系统停下并返回偏差，模型据此修正后继续。

## 创新点或方法

旧接口让模型直接面对执行难题；Auriga 补充校准后的三维测量、以手指为参照的双臂控制，以及统一动作准入入口。模型维护显式任务判断，通过工具或生成多步 Python 程序行动。运动前，在仿真暂停时检查可视化轨迹；运动中检查声明的阶段容差和抓取边界，偏离就停止并返回实测差异。它不是摘要所述的策略训练方法：系统经过 13 轮跨任务能力迭代后冻结，评估时不做目标任务试跑或重置。

### 方法如何工作

1. 把指令与观测整理成显式任务判断，让模型记录当前进度和下一步动作依据。
2. 利用三维测量和控制工具生成动作或多步程序，把高层意图落到可执行指令。
3. 在暂停仿真中查看轨迹预览，运动前检查路径是否符合意图。
4. 执行时对照阶段容差和抓取边界检查偏差，异常即停止并回传测量结果，供模型原地恢复。

### 必要术语

- 任务判断（task belief）：模型显式维护的任务状态认识；用于组织决策，具体表示摘要未说明。
- 阶段容差：某一步允许的误差范围；执行系统据此判断是否停止。
- 零样本操作：评测目标任务不先试跑适配；本文仍包含跨任务系统开发。

## 证据

摘要报告：RoboDojo 成功率 57.7%、Score 为 64.0，同模型下超过参考系统两倍；按作者定义弥合上述落差的 68.3%。场景随机化后仍排名第一，学习策略表现下降最高达 33.9%，但该下降量的具体口径未给。冻结系统在 RoboCasa365 达 73.2%，复合任务上超过 VLA 辅助智能体最高达 23.1%，差值口径同样待核查。这些是仿真基准证据，不能当作真机验证。

## 局限

任务零样本不等于系统没有工程开发：13 轮迭代是明确的开发投入。我的待核查问题是开发任务与评测任务如何隔离，以及暂停预览、精确测量和抓取检查有多少依赖仿真状态；这些会影响真机迁移判断。

- **判断**：值得深入读执行接口和恢复流程，因为它具体展示了系统工程怎样释放同一个模型已有的规划能力。

## 研究关联

这里可借鉴的是把执行误差转成模型能处理的反馈：告诉它哪项几何约束偏了多少，使下一步修正有依据。遇到高层计划合理、实际动作频繁失败的系统时，值得先检查接口和反馈，而非直接归因于模型不会推理。

### 下一步读哪里

优先核查任务判断如何更新、容差由谁设定、预览能发现什么错误，以及各项机制消融能否解释成功率增益；同时确认环境状态的读取权限。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/Auriga Technical Report A Task-Agnostic Agent Harness for Zero-Shot Embodied Man.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2611.01112v1 Announce Type: new Abstract: Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's success rate from 22.5% under the reference control interface to 76.2%. We present Auriga, a task-agnostic agent harness that closes 68.3% of this gap in zero-shot manipulation without target-task trials or resets. In Auriga, the model makes all task decisions over an explicit task belief and acts through either direct tool calls or synthesized multi-step Python programs, while the harness supplies calibrated 3D measurements, finger-referenced dual-arm control, and a single admission gateway to the robot. Before motion, the model inspects a visual trajectory preview while simulation is paused; during execution, the harness checks declared stage tolerances and grasp bounds, stopping the robot on divergence and returning the measured discrepancy for in-place recovery. Developed across 13 cross-task capability iterations and frozen for evaluation, Auriga ranks first on the RoboDojo leaderboard with a 57.7% success rate (64.0 Score), more than doubling the reference harness on the same model, and remains first under scene randomization while learned policies drop by up to 33.9%. On RoboCasa365, the same frozen harness reaches a 73.2% success rate, outperforming VLA-assisted agents by up to 23.1% on composite tasks. Project page: https://auriga.stelledge.com/ Code: https://github.com/lose4578/Auriga

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.01112
- Authors: Chengcheng Wang, Yuheng Shi, Siyu Xu, Yutong Wang, Jinjing Zhao, Chenghao Xia, Jinqi Liao, Jiankun Peng, Ligong Bi, Yuechuan Ma, Jiaqi Liu, Wenbo Wang, Zijian Wang, Yuemin Wu, Minjing Dong, Xiu Su, Tao Huang, Jianyuan Guo, Chengbin Du, Yunke Wang, Chang Xu
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
