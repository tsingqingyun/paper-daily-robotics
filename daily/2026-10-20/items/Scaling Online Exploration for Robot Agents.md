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
url: "https://arxiv.org/abs/2610.22496"
published: "Mon, 19 Oct 2026 00:00:00 -0400"
age_days: 0
score: 46
created: 2026-10-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Scaling Online Exploration for Robot Agents

> [!summary] 这篇论文到底做了什么（基于摘要）
> RAX 让通用编码智能体通过实际试操作编写机器人控制程序，再把成功经验整理成可组合技能。它试图减少新机器人、新任务对遥操作示范的依赖，让机器人靠在线经验继续进步。

## 问题

任务涵盖精细操作和长流程操作。瓶颈是换机器人或任务往往需要专门采集示范，而模仿策略容易受示范分布限制；继续扩大模型，并没有直接解决部署后如何自己获取新经验的问题。

### 用一个例子理解

理解用例（非论文实验）：输入“打开抽屉并取出盒子”；智能体读取观测、编写并尝试控制代码，根据反馈修改操作，再调用已验证的抓取程序；输出是完成任务的动作及可复用程序。

## 创新点或方法

旧做法先收集动作示范再训练策略；RAX 改为让编码智能体调用机器人 API，在交互中寻找能完成目标的决策序列，并整理成包含感知、规划和控制的模块化程序。新任务还可组合此前验证的技能。摘要明确不依赖动作示范、手写动作原语或价值函数引导，也不要求为接入机器人训练策略；但编码智能体原有训练、探索反馈和程序筛选规则未说明。

### 方法如何工作

1. 把目标和机器人 API 交给编码智能体，使它能够生成实际可执行的控制代码。
2. 运行代码获取在线经验，从反馈中寻找达成目标的决策序列；具体搜索和反馈机制摘要未说明。
3. 将找到的流程整理成感知、规划、控制一体的模块程序，供后续调用。
4. 组合此前验证的技能处理后续任务，使探索积累能够继续发挥作用。

### 必要术语

- 在线探索：与环境实际交互来获取经验；本文用它寻找成功的操作流程。
- 动作原语：预先写好的基础操作；RAX 声称不依赖人工设计的这类动作库。
- 机器人具身：机器人的身体和执行机构配置；本文考察多种配置下的探索。

## 证据

摘要报告研究覆盖单臂、双臂、灵巧手、移动和人形系统，包含仿真与真机。仿真相对顶尖基线平均高出 37.4%，但未说明这是相对增幅还是百分点，也未给基线名称与汇总方式。真机展示记忆相关、关节物体、精密、可变形物体及移动长流程任务，没有提供成功率和试验次数。证据支持方法覆盖面与探索收益，尚不足以量化部署成本。

## 局限

我的待核查问题是探索需要多少次失败、多少人工复位，以及安全限制来自哪里。摘要称观察到安全防护与错误恢复能力，但这不等于已有安全保证；真机任务展示也不能继承仿真的平均增益。

- **判断**：值得细读探索、验证和技能复用流程，因为决定它能否落地的是经验如何可靠积累，而不只是代码能否生成。

## 研究关联

值得借鉴的是把探索成果保存为可检查、可调用的程序：后续任务有机会复用已经验证的处理流程。适合重点检查的条件是，任务能否通过 API 操作，以及成功与失败能否可靠判断。

### 下一步读哪里

优先核查探索预算、成功判定、程序验证和失败复位方式；再查仿真 37.4% 的定义，以及真机随探索次数变化的成功率。当前只有摘要，不能确认这些实现细节。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：46
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-20/Scaling Online Exploration for Robot Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.22496v1 Announce Type: new Abstract: Robot learning has advanced by scaling demonstration datasets and model capacity; however, deploying a new robot embodiment or task typically necessitates a dedicated teleoperation corpus. The resulting policies remain bounded by their imitation distributions, limiting generalization and continual self-improvement. We introduce RAX (Robot Agent eXploration), an open-source framework for robot agents centered on scaling exploration: enabling agents to improve by acquiring online experience and synthesizing executable programs. In RAX, a general-purpose coding agent generates robot control code, operating without action demonstration data, hand-engineered action primitives, or value-function guidance. Through online exploration, the agent identifies decision sequences that achieve task goals and compiles them into modular programs encapsulating the full perception-planning-control loop. Using RAX, we present a systematic multi-embodiment study on scaling online exploration across precision and long-horizon manipulation tasks using single-arm, bimanual, dexterous, mobile, and humanoid systems in simulation and on real robots. Generalization performance on unseen environments improves consistently as exploration scales. In simulation, RAX outperforms top baseline models by +37.4% on average. On real robots, RAX autonomously learns memory-dependent, articulated, high-precision, deformable, and long-horizon mobile manipulation tasks without human demonstrations, continually improving performance by composing verified skills from prior exploration sessions. As exploration scales, we observe emergent capabilities including active perception, error recovery, safety guardrails, and human-robot collaboration. We open-source RAX as a generalist robot-agent platform in which new robot embodiments are integrated through their APIs alone, without teleoperated data collection or policy training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22496
- Authors: Runhan Huang, Xiangcheng Zhang, Haoyu Chen, Yitong Li, Yen-Jen Wang, Bohan Lyu, Haotian Ye, Chuye Hong, Yixuan Wang, Chloe Su, Haoyu Xiong, Yangzhen Wu, Enze Xie, Travis Manderson, Stefano Ermon, Pieter Abbeel, Antonio Torralba, Dawn Song, Weirui Ye, Yilun Du
- Published: Mon, 19 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
