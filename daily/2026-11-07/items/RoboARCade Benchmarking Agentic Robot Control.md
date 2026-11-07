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
url: "https://arxiv.org/abs/2611.08209v1"
published: "2026-11-05T16:00:16Z"
age_days: 1
score: 31
created: 2026-11-07
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# RoboARCade: Benchmarking Agentic Robot Control

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboARCade用长程仿真操作任务测试多模态智能体能否直接控制机器人，重点检查适应、记忆和精确执行。它把初始条件变化拉大，并比较接口和上下文帮助，发现看懂场景之后，选对操作办法、准确执行和正确判断完成仍然困难。

## 问题

具体任务是让智能体连续控制机器人完成多步操作，而不只是回答图像问题。瓶颈在于控制过程中要根据变化调整计划、记住进度并执行精细动作。本文通过扩大已有任务的初始条件范围增加难度；摘要未证明既有基准普遍失效，因此不宜扩大这一批评。

### 用一个例子理解

理解用例（非论文实验）：输入桌面画面和“先开盒再放入积木”的目标，智能体连续选择动作、观察反馈并记录进度，最后输出完成声明；环境独立检查盒盖状态和积木位置。

## 创新点或方法

本文主要改评测组织：把三种机器人形态的任务统一放在MuJoCo中，每项任务独立打包，智能体通过可替换接口接入。评测时改变接口、提供成功示范，或让智能体编写并修改提示词，观察行为变化。这些属于接口与上下文适应实验；摘要没有说明进行了模型权重训练，也未列出具体动作接口。

### 方法如何工作

1. 扩大已有操作任务的初始条件范围，让固定起点下有效的做法接受更广变化检验。
2. 统一仿真后端并分离任务包与接口，使不同智能体可以接入相同任务。
3. 记录执行结果和过程，区分策略选择、动作精度与成功判断问题。
4. 改变视觉接口、上下文示范或提示词，比较收益与成本；摘要未交代更细的执行协议。

### 必要术语

- 智能体式机器人控制：由智能体直接决定机器人动作；本文的评测对象。
- 上下文适应：通过输入里的示例或说明改变行为；本文测试单次成功示范的帮助。
- 机器人形态：机器人的身体结构与可执行动作；基准覆盖三种形态。

## 证据

摘要报告整体得分：GPT-6 Astra为49.8%，Claude Fable 5.1为43.6%。更丰富视觉接口只增加1.5—6.8个百分点，成本为1.7—2.3倍；24%—39%的已尝试子任务被错误宣称成功。另在五任务子集，Astra由53.5%升至单示范条件下的73.0%，自行修改提示词达到72.0%。子集成绩不能与整体49.8%直接比较；全部结果来自仿真。

## 局限

我会核查失败类型如何标注、成功判定是否由环境独立检查，以及各模型的预算是否一致。观察到策略和执行错误较多，并不能单凭相关性证明感知已足够；接口设计也可能影响错误分布。

- **判断**：值得先读任务与失败轨迹，再看排行榜；它更有用的部分是把控制失败定位到可检查的行为环节。

## 研究关联

最可借鉴的是评测拆分：完成不了任务，可能是操作策略差、执行不准，也可能是过早认定成功。新增视觉信息收益有限的结果提示，至少在这些设置下，改善感知输入未必能解决主要控制错误。

### 下一步读哪里

下一步核查任务成功条件、控制频率、动作粒度、交互预算和成本口径。对示范与提示词实验，应检查示范来源、修改过程及独立测试条件，避免把特定子集收益外推到全部任务。

- **概念**：多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/RoboARCade Benchmarking Agentic Robot Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Improvements in multi-modal capabilities have enabled agents to act directly as robot policies, a setting we refer to as agentic robot control (ARC). We introduce RoboARCade, a benchmark of long-horizon manipulation tasks across three embodiments designed to test in-context adaptation, memory, and reasoning for precise control. The tasks build on existing open-source benchmarks, which we make harder by widening the range of initial conditions. RoboARCade is easy to use and extend: all tasks run on a single simulation backend, MuJoCo, each task is a self-contained data pack, and agents connect through interchangeable interfaces, so new tasks, agents, and interfaces can be added independently. The benchmark separates leading agents: GPT-6 Astra achieves 49.8% compared with 43.6% for Claude Fable 5.1, leaving substantial room for improvement. Comparing two interfaces, we find that a richer visual interface adds only 1.5 to 6.8 points at 1.7 to 2.3 times the cost. Failures stem mostly from choosing a poor manipulation strategy or executing a good one imprecisely, rarely from misunderstanding the scene, and agents incorrectly claim success on 24% to 39% of attempted subtasks. Agents can also improve without human input: one successful demonstration in context raises Astra's score from 53.5% to 73.0% on a five-task subset, and a prompt the agent writes and revises itself reaches 72.0%. Code, videos and full traces are available at roboarcade.org.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08209v1
- Authors: Satvik Sharma, Hengyuan Hu, Mihika Kamat, Dorsa Sadigh, Jeannette Bohg
- Published: 2026-11-05T16:00:16Z
- Age days: 1

</details>
