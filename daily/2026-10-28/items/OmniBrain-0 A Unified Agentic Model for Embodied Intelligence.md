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
url: "https://arxiv.org/abs/2610.36013v1"
published: "2026-10-26T17:15:41Z"
age_days: 1
score: 35
created: 2026-10-28
concepts: ["多模态基础模型", "智能体 Agent"]
---

# OmniBrain-0: A Unified Agentic Model for Embodied Intelligence

> [!summary] 这篇论文到底做了什么（基于摘要）
> OmniBrain-0 把操作和导航的高层决策经验压进同一个轻量模型，让它负责安排步骤、跟踪进度和失败恢复。它先培养领域专家，再通过 MOPD 合并决策能力，并用执行证据继续改进专家。

## 问题

长任务要求机器人知道做到哪一步、接下来做什么、失败后如何调整。单项动作策略不能保证整项任务可靠，而强多模态智能体的推理和经验使用成本又难让小模型直接复现。

### 用一个例子理解

理解用例（非论文实验）：输入是“去厨房取杯子”；模型先决定导航，确认到达后安排抓取，发现抓取失败再调整下一步；输出是一串随反馈更新的高层决策，具体如何交给底层执行需核查。

## 创新点或方法

旧做法可以用外部智能体调用不同技能；本文把统一放进学到的高层决策模型。训练依次经过具身预训练、领域专家蒸馏和多教师在线策略蒸馏 MOPD，把操作与导航专家的决策能力汇入 OmniBrain-0。RSI 再让 Meta-Agent 根据执行证据修订评分准则、逐步提醒和验证轨迹，更新专家后重新合并。推理时由统一模型做高层决策；底层控制接口、模型大小及教师调用安排未说明。

### 方法如何工作

1. 通过具身预训练建立基础能力，为领域决策学习提供起点。
2. 把强教师的交互经验蒸馏给操作与导航专家，使各专家掌握领域内的决策。
3. 用 MOPD 将多位专家能力汇入统一模型；具体在线采样与监督机制摘要只说明到此。
4. 用 RSI 把执行证据转成改进数据，更新专家后再合并，形成下一轮训练输入。
5. 部署统一模型跟踪进度并按反馈调整计划，以协调长任务中的不同技能。

### 必要术语

- 高层决策：决定下一步做什么；本文用同一模型协调导航、操作和恢复。
- MOPD：多教师在线策略蒸馏；本文用它合并领域专家的决策能力。
- RSI：递归自我改进；本文通过分析执行证据、更新专家并重新合并来迭代。

## 证据

摘要列出 LIBERO-Pro、LIBERO-Plus、RoboCasa365、RoboTwin 2.0、R2R-CE Val-Unseen，以及多项真机操作任务；声称跨领域表现强，推理和执行开销显著低于闭源教师。没有成功率、开销数值、教师名称和消融结果，因此只能确认评测覆盖面，尚不能量化统一模型、MOPD 或 RSI 各自的贡献。

## 局限

摘要同时涉及仿真基准和真机操作，不能据此认为真实导航与操作已在同一长任务中联合验证。RSI 的改进也需要独立测试集支撑；目前无法判断评分准则是否会随训练一起偏移。

- **判断**：值得读训练流程和消融，重点看统一究竟带来哪些可测收益；仅凭摘要不足以判断其可靠性或成本优势幅度。

## 研究关联

可借鉴的是先让不同专家吸收各自领域的交互经验，再合并高层决策。对需要多种技能协作的任务，训练重点可以包括进度判断与失败恢复，而不只模仿成功动作。

### 下一步读哪里

先查高层动作空间和底层执行接口，再查 MOPD 如何收集学生执行状态、教师如何给监督，以及 RSI 的轨迹验证标准。还应核对教师与学生的成功率、延迟和执行步数是否在同条件下比较。

- **概念**：多模态基础模型 智能体 Agent
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/OmniBrain-0 A Unified Agentic Model for Embodied Intelligence.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose embodied intelligence requires robots to coordinate diverse skills over long horizons, track task progress, and recover from failures. Specialist policies alone do not ensure task-level reliability, while powerful multimodal agents rely on costly reasoning and external experience that compact models struggle to reproduce. We introduce OmniBrain-0, a lightweight unified embodied agent that coordinates manipulation and navigation through a shared high-level decision model, integrating task understanding, planning, progress tracking, and feedback-driven recovery. Our progressive training framework combines embodied pretraining, domain-specialized agent distillation, and multi-teacher on-policy distillation (MOPD). It distills powerful teachers' interaction experience into manipulation and navigation experts, then consolidates their decision capabilities into OmniBrain-0. Unification therefore occurs within the learned decision model rather than only at the tool interface. We further introduce Rubric-Guided Recursive Self-Improvement (RSI), a data flywheel in which a Meta-Agent turns execution evidence into refined rubrics, step-level reminders, and verified trajectories for domain-expert updates before their reconsolidation into OmniBrain-0 through MOPD. We evaluate OmniBrain-0 on LIBERO-Pro, LIBERO-Plus, RoboCasa365, RoboTwin 2.0, and R2R-CE Val-Unseen, as well as multiple real-world manipulation tasks. OmniBrain-0 combines strong cross-domain task performance with substantially lower inference and execution overhead than its closed-source teacher, demonstrating efficient transfer and consolidation of embodied capabilities into a compact unified agent.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36013v1
- Authors: Xiaomi Embodied Intelligence Team, Yuechen Luo, Chong He, Fang Li, Shaoqing Xu, Jingkai Wang, Menglun Su, Jiaxin Liu, Shengyin Jiang, Zhiyi Lai, Long Chen, Longlong Wang, Liang Hu, Haochen Liu, Yuncheng Jiang, Hongwei Xie, Jieming Cui, Hanbing Li, Junjie Huang, Zhixiang Duan, Hexin Zhang, Weixiang Liang, Ying Gong, Yuhan Wang, Yong Pan, Pengna Li, Kangyi Wu, Ken Deng, Kun Ma, Fuxi Wen, Zhi-xin Yang, Hangjun Ye
- Published: 2026-10-26T17:15:41Z
- Age days: 1

</details>
