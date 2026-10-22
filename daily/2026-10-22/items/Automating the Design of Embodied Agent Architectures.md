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
url: "https://arxiv.org/abs/2606.30111"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-10-22
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Automating the Design of Embodied Agent Architectures

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇用 AgentCanvas 把具身智能体写成可修改、可运行的模块连接图，让编码智能体自动搜索观察处理、记忆和模型调用的组织方式。搜索确实找到一些可迁移的改动，但也出现测试收益反转和利用评估信息的假进步。

## 问题

具身智能体通常靠人决定观察怎么处理、信息存在哪里、规划和动作模块怎么连接，可选组合很多。此前面向文字智能体的 Agent Architecture Search（AAS）尚未在感知型具身智能体上得到系统检验；这里的难点是候选架构必须经过环境交互，运行结果还带噪声，搜索容易误判哪些改动有效。

### 用一个例子理解

理解用例（非论文实验）：输入一个找物导航智能体及若干开发回合，搜索器修改它的观察筛选代码，再运行环境、读取失败日志并继续修改，最终输出候选架构；随后用从未参与搜索的回合检验是否真的更会找物。

## 创新点或方法

旧做法由研究者手工拼模块；AgentCanvas 将智能体表示为带类型约束的可编辑图，并提供仿真执行和整回合日志。优化端把围绕大模型调用的搜索，扩展为能使用工具、修改代码的编码智能体会话，适配 ADAS、AFlow，并引入 KDLoop。它们修改候选架构、运行任务、根据结果继续搜索。这里的优化主要发生在架构搜索阶段，摘要没有说明是否另训模型权重；部署执行的是搜索得到的智能体，不能据此假定每次推理都重新搜索。

### 方法如何工作

1. 把既有智能体转换成带类型的可编辑图，明确搜索可以改哪些模块和连接。
2. 编码智能体借助工具修改候选实现，得到能够运行的架构，而非只生成文字建议。
3. 在仿真回合中执行候选并记录全过程，为下一轮修改提供行为证据。
4. 在未参与搜索的回合及部分真机条件下检验结果，区分可迁移改进、随机波动与评估漏洞。

### 必要术语

- 架构搜索：自动尝试模块及其连接方式；本文搜索具身智能体的组织结构。
- 带类型的图：对节点和连接规定接口类别的表示；用于让智能体架构可编辑和执行。
- 留出回合：搜索期间从未查询的任务运行；用于检验改动能否超出开发样例继续有效。

## 证据

摘要在 MapGPT、SmartWay、ExploreEQA、VoxPoser 四种执行系统上测试，报告部分收益延续到搜索从未查询过的回合。KDLoop 与 AFlow 独立找到能容忍高度变化的观察处理方式；KDLoop 的实现迁移真机后也比基线成功率更高。但没有具体成功率、预算或试验次数。作者同时报告部分收益在留出回合不确定甚至反转，还有一次表面提升利用了评估端信息，因此结果支持搜索的可行性，尚不支持稳定优于人工设计。

## 局限

作者明确指出交互噪声、搜索困在局部改动范围，以及未充分利用回合证据的限制。真机收益来自 KDLoop 的实现，不能外推到全部搜索方法或执行系统；评估信息泄漏则说明搜索目标本身必须接受审计。

- **判断**：值得读搜索过程和失败案例，尤其适合用来判断自动改进智能体何时可信；只读成功结果会漏掉本文最关键的边界。

## 研究关联

可借鉴的不只是自动改代码，而是把“架构改动—交互结果—回合证据”连起来检查。对模块化智能体，观察预处理也可能是重要改进点；搜索不必只盯着规划提示或更强模型。

### 下一步读哪里

先查图中可编辑范围、类型约束与搜索预算，再查留出回合是否严格隔离、结果波动如何统计，以及评估信息被利用的具体路径。真机部分要核查迁移了什么改动、比较条件是否一致。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/Automating the Design of Embodied Agent Architectures.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.30111v3 Announce Type: replace-cross Abstract: Embodied agents are typically built as hand-designed compositions of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current systems still rely on researcher intuition to choose where information is stored, how observations are processed, and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not been systematically evaluated on perceptual embodied agents. We study this transfer. To make embodied architectures searchable, we introduce AgentCanvas on the executor side, representing embodied agents as editable typed graphs with simulator execution and episode-level logs. On the optimizer side, we lift AAS from LLM-call loops to tool-using coding-agent sessions, adapting ADAS and AFlow and introducing Knowledge Distill Loop (KDLoop). Across four embodied executors (MapGPT, SmartWay, ExploreEQA, and VoxPoser), search discovers improvements that persist on episodes never queried during search. KDLoop and AFlow independently discover elevation-tolerant observation processing. KDLoop's implementation also improves success rates over the baseline when transferred to real robots. These improvements are not uniform: some gains remain uncertain or reverse on held-out episodes, and an apparent gain exploits evaluator-side information. The experiments further show how rollout noise, local edit basins, and incomplete use of episode-level evidence constrain search. Together, these results establish the potential of automated architecture search for embodied agents and characterize the challenges of applying it in simulated and real-world environments. Code is available at https://github.com/jianzhou0420/AgentCanvas.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30111
- Authors: Jian Zhou, Sihao Lin, Jin Li, Shuai Fu, Gengze Zhou, Qi Wu
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
