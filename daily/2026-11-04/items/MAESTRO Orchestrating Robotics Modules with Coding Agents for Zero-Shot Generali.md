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
url: "https://arxiv.org/abs/2511.00917"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 45
created: 2026-11-04
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# MAESTRO: Orchestrating Robotics Modules with Coding Agents for Zero-Shot Generalist Robots

> [!summary] 这篇论文到底做了什么（基于摘要）
> MAESTRO 让视觉语言模型写机器人程序，调用已有的感知、规划和控制工具完成任务。它的关键不只是工具多，而是执行后检查结果，失败后重新规划。

## 问题

目标是让机器人零样本完成桌面操作和移动操作。摘要针对的主流路线是收集更多机器人数据、训练端到端策略；MAESTRO 探索能否利用已有模块减少新增遥操作数据需求。另一处具体瓶颈是：工具库扩大后，模型未必知道如何正确组合和使用工具。

### 用一个例子理解

理解用例（非论文实验）：输入“把桌上的杯子送到架子”；VLM 编写程序，依次调用杯子定位、抓取、移动和放置工具；若视觉反馈显示杯子仍在桌上，就修改后续计划，输出重新抓取的调用。

## 创新点或方法

从“训练一个直接输出动作的模型”转向“让 VLM 编写调用现有工具的程序”。调度机制把多步感知与行动流程封装成可调用工具，并组织计划、执行、再规划循环，利用视觉和执行反馈检查结果、恢复失败。这里可借鉴的改动是把可靠的操作流程也做成工具，减少每次从零拼接的负担。摘要称无需新增遥操作数据，但没交代底层模型和工具原有的训练过程；写程序、调用工具及反馈修正发生在执行阶段。

### 方法如何工作

1. 接收任务与视觉信息，形成操作计划，确定需要哪些感知和动作能力。
2. 生成调用工具的程序，把计划落到可执行流程；多步过程可被封装后复用。
3. 执行工具并收集视觉与运行反馈，判断预期结果是否发生。
4. 根据偏差重新规划并继续调用工具，以支持失败恢复；重试上限与终止规则摘要未说明。

### 必要术语

- 编码智能体：通过生成程序来完成任务的模型；本文用它组织机器人工具调用。
- 调度机制：管理工具使用、执行反馈和后续决策的流程；本文消融检验了它与工具库的配合。
- 零样本：不依靠目标任务的新示范来适配；本文报告的是其测试设置下的零样本表现。

## 证据

摘要称，在其桌面对比中，不调用 VLA 工具的 MAESTRO 零样本达到或超过先进 VLA，并展示多种移动操作任务。消融以平均任务进展衡量：完整调度机制下，扩充工具库有帮助；缺少该机制时，加工具不能可靠改善进展。摘要未提供具体任务清单、基线型号、分数和重复次数。跨试次改代码、借 VLA 加速及生成数据属于案例展示，证据强度需与主比较分开。

## 局限

零样本不等于系统没有人工工程投入：摘要明确使用精选工具库。我的待核查问题是工具是否针对测试任务定制、失败恢复用了多少次尝试，以及移动操作覆盖哪些环境；不能由摘要推断任意新任务都能完成。

- **判断**：值得细读调度机制和工具扩充消融，它们比单个成功演示更能解释这条路线何时有效。

## 研究关联

这篇让“模块能力如何变成整机能力”成为可检验的问题。已有感知和控制工具时，值得同时设计调用流程、结果检查和失败恢复，而非仅增加函数接口。

### 下一步读哪里

优先检查工具接口、任务进展的计分方式、反馈如何触发重规划，以及桌面对比是否统一了观测、尝试次数和执行预算。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：45
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/MAESTRO Orchestrating Robotics Modules with Coding Agents for Zero-Shot Generali.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2511.00917v3 Announce Type: replace Abstract: Today's dominant route to generalist robots scales robotics data to train end-to-end policies. We instead use a vision-language model (VLM) as a coding agent that writes robot programs using a curated library of perception, planning, and control tools. MAESTRO's orchestration harness packages multi-step perception and action procedures into callable tools and guides their use through a plan-act-replan loop, using visual and execution feedback to verify outcomes and recover from failures. With this tool library and harness, MAESTRO matches or surpasses state-of-the-art vision-language-action (VLA) models zero-shot in our tabletop comparison and performs diverse mobile manipulation tasks, without collecting new teleoperation data or invoking a VLA tool. Ablations show that expanding the tool library improves average task progress with the full harness, while adding tools without it does not reliably improve progress. Case studies illustrate MAESTRO's potential for autonomous code improvement across trials, faster execution with VLA tools, and automatic robot data generation. We show that expanding robotics tool libraries together with their orchestration harnesses offers a complementary route to general-purpose robots alongside scaling end-to-end robot training data. Project site: https://maestro-robot.github.io. Code: https://github.com/penn-pal-lab/maestro.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2511.00917
- Authors: Junyao Shi, Rujia Yang, Kaitian Chao, Selina Bingqing Wan, Yifei Shao, Jiahui Lei, Jianing Qian, Long Le, Pratik Chaudhari, Kostas Daniilidis, Chuan Wen, Dinesh Jayaraman
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
