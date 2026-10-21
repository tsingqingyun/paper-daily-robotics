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
url: "https://arxiv.org/abs/2610.25376v1"
published: "2026-10-18T16:26:20Z"
age_days: 2
score: 32
created: 2026-10-21
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> TILDE 要把预训练机器人大模型的操作能力教给没有动作预训练的学生策略：不仅教标准动作，还让老师到学生实际犯错的位置给答案、亲自示范怎么救回来。AutoDAgger 用机器人奖励模型监控进度并触发老师接管，减少人工盯场。

## 问题

任务是现实机器人操作中的策略蒸馏。直接复现老师的大规模动作预训练，需要大量机器人数据和算力；只模仿正常示范又容易遇到另一种瓶颈：学生执行偏了以后，看到的状态不再像训练数据，后续动作也随之失准。摘要强调，想继承老师的闭环稳健性，就必须覆盖这些学生自己造成的局面。

### 用一个例子理解

理解用例（非论文实验）：输入是机器人把杯子推偏后的画面和“放到托盘里”的指令；学生继续执行，监控器发现进展停滞，老师接管调整抓取并放好。输出既包括完成动作，也包括供学生下次学习的纠错轨迹。

## 创新点或方法

旧做法主要从已有示范学习；TILDE 增加两类材料：老师在学生访问到的状态上提供动作监督，以及老师接管后完成的恢复轨迹。前者回答“这里该怎么动”，后者展示“接下来如何连续纠错”。训练时，AutoDAgger 通过奖励模型判断任务进展并决定何时介入，再把经验汇入学生学习。部署时目标是让学生执行；摘要未说明评测时是否完全移除老师，也未给出介入阈值和训练损失。

### 方法如何工作

1. 先用示范训练学生，让它具备基本操作能力，能够开始执行任务。
2. 让学生实际运行，收集它自己会进入的状态，从而暴露标准示范覆盖不到的偏差。
3. 在这些状态上获取老师动作；进展异常时由老师接管，产生连续恢复经验。
4. 把示范、状态监督和恢复经验共同用于学生训练，使其学习正常操作与偏差后的应对；具体损失和迭代安排摘要未说明。

### 必要术语

- 在策略蒸馏：在学生自己访问到的状态上请老师指导；用于减少训练状态与执行状态的落差。
- 恢复轨迹：从偏差或受阻状态重新推进任务的一串动作；本文用它教授连续纠错。
- 行为克隆：根据示范中的观察预测动作；这里是性能比较的基线。

## 证据

摘要报告三个真实世界任务，相对行为克隆，任务表现最高达到 4.1 倍；AutoDAgger 收集恢复轨迹的速度超过人工介入方法的 2 倍，并支持跨架构蒸馏。这支持“加入学生状态和恢复经验有实用收益”，但最高倍数不代表三个任务的平均收益。摘要未给任务名称、绝对成功率、试验次数及各组成部分的独立贡献。

## 局限

我的待核查问题是奖励模型会不会把缓慢但有效的动作误判为失败，或漏掉已经不可恢复的状态。这直接影响自动采集的数据质量。现有证据来自真机，但摘要没有交代老师调用成本，不能据此认定整体训练成本一定更低。

- **判断**：值得细读数据采集和消融实验，因为它最有启发的部分是如何教会学生纠错，而不仅是蒸馏后的最高分。

## 研究关联

值得借鉴的是数据采集位置：如果策略总在某种偏差后崩溃，继续增加顺利完成的示范可能不如采集偏差发生后的纠正过程。前提是老师确实能处理这些状态，而且介入判断足够可靠。

### 下一步读哪里

优先核查介入触发规则、恢复轨迹如何与普通示范混合，以及只加状态监督、只加恢复轨迹的消融；再看三个任务的绝对成功率和部署时老师是否退出。

- **概念**：多模态基础模型 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/TILDE Teacher-in-the-Loop Distillation from Embodied Foundation Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large-scale action pretraining equips Embodied Foundation Models (EFMs) with strong manipulation capabilities, with particular strengths in generalization and closed-loop robustness, but reproducing such pretraining requires substantial robot data and computation. To transfer these capabilities from pretrained EFMs to policies without action pretraining, we introduce TILDE (Teacher-In-the-Loop Distillation from EFMs), which synergizes on-policy distillation at student-induced states with learning from teacher-executed recovery trajectories. We further propose AutoDAgger, an autonomous data aggregation pipeline in which a robotic reward model is utilized to monitor task progress and trigger teacher intervention, thereby collecting recovery experience without human monitoring or manual control. AutoDAgger accelerates recovery-trajectory collection by more than $2\times$ compared with the human-in-the-loop method. By unifying learning from demonstrations, on-policy teacher supervision, and teacher's corrective behavior, TILDE improves task performance by up to $4.1\times$ over behavior cloning across three real-world tasks and supports effective cross-architecture distillation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25376v1
- Authors: Yuxiang Lu, Yantong Liu, Jinghua Hou, Xueli Sun, Ruihua Han, Zhe Liu, Hengshuang Zhao
- Published: 2026-10-18T16:26:20Z
- Age days: 2

</details>
