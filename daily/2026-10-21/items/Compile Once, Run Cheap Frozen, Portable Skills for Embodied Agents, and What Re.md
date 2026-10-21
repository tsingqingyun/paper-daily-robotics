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
url: "https://arxiv.org/abs/2610.25114v1"
published: "2026-10-18T08:46:13Z"
age_days: 2
score: 32
created: 2026-10-21
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds

> [!summary] 这篇论文到底做了什么（基于摘要）
> Skill-RSI 让强模型先在仿真中编写、运行和修复操作代码，合格后冻结，执行时直接运行代码或交给便宜模型调用。它检验的是：昂贵推理能否提前做完，以及反复修改的收益到底来自哪里。

## 问题

新增机器人技能通常要逐任务收集示范，或在每次执行中调用昂贵模型。本文尝试把成本移到离线阶段，但关键瓶颈是：技能能否通过冻结后才抽取的新布局考试，以及修复是否真的比重新写更有效，而非只记住开发场景。

### 用一个例子理解

理解用例（非论文实验）：输入是“把方块放进盒子”和仿真接口；强模型离线写代码、发现定位错误并修复，冻结后交给新布局考试。输出是可重复调用的技能文件，执行时无需再次请强模型规划。

## 创新点或方法

旧做法每回合依赖模型决策；本文让强模型担任离线代码作者，经历编写、试跑、诊断和修复，再冻结文件接受隐藏布局考试。通过后，同一份文件可独立执行，也可由另一模型家族的廉价调用者按技能描述选用。这里的“学习”主要是修改程序，不是摘要所述的策略权重训练。隔离作者、审计记录和不同反馈条件用于辨别改进来源。

### 方法如何工作

1. 给离线作者任务和仿真接口，让它写出可执行技能，得到首个候选程序。
2. 运行候选并诊断失败，继承已有版本进行修改，保留已经有效的部分。
3. 冻结程序后抽取考试布局，防止针对考试结果继续修改而污染验证。
4. 让相同文件独立运行或由异模型调用，检验执行成本与跨调用者复用能力。

### 必要术语

- 冻结技能：考试和复用阶段不再改动的程序；用于明确被验证的对象。
- 继承式修复：在旧版本上修改；本文用它与从头重写区分收益来源。
- 隐藏布局：开发时不可见的物体布置；用于检验技能是否只适应开发场景。

## 证据

摘要报告 RoboTwin 2.0 杂乱桌面上的 7 个仿真任务：4 个任务编成 7 个技能，其中 5 个首稿只需资格测试；另 3 个任务在 18 次尝试中未通过。单技能作者费用为 4.29—8.22 美元，计入 13 次失败尝试后为 55 美元。新布局上，无模型执行成功 148/150 次，廉价调用成功 147/150 次，每回合调用费用为 0.00028—0.00054 美元。继承旧版本的修复在 8/8 组对照中胜过重写，p=0.004；额外反馈的收益仅有 3/3、p=0.125 的证据。均来自摘要。

## 局限

作者明确没有运行直接控制基线，因此不能据此比较同一强模型在线控制的成功率或总成本。全部结果来自仿真。最难任务虽有 78—95/100 的得分，仍因 3—16 次安全中止不合格；摘要也指出，100 回合考试对中止率的约束只到 3.6%，零观测中止不能证明零风险。

- **判断**：值得细读实验控制和失败案例；它对“递归改进究竟改进了什么”的证据，比成功技能的演示更值得关注。

## 研究关联

可以借鉴的是把稳定、可重复的能力固化成可检查的程序，避免每次重新推理。更关键的启示是评估改进来源：保留已有正确代码本身，就可能解释大部分收益，不能把所有进步都归给自我反馈。

### 下一步读哪里

优先核查隐藏布局如何生成、成功与中止如何判定、技能能读取哪些状态，以及继承对照如何保持预算一致；再看失败尝试是否揭示了代码技能的适用边界。

- **概念**：多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/Compile Once, Run Cheap Frozen, Portable Skills for Embodied Agents, and What Re.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied AI lacks the data-rich pretraining that gave language models their agents and skills, so new manipulation capability costs demonstrations per task or a frontier model in every episode. We study a third route: a strong general model acts only as an offline author that writes, runs, diagnoses and repairs a manipulation skill in simulation until it passes an exam on layouts drawn after freezing; the frozen skill then runs as code alone or under a cheap caller that reads only its description. We call this skill-level recursive self-improvement Skill-RSI and specify a compile protocol (isolated, audited author; hidden validation layouts; no-feedback and inherit-only controls; tamper-evident ledger) and a reuse protocol that runs the identical files with executors from another model family. On 7 RoboTwin 2.0 tasks with cluttered tables, Claude Code compiled 4 tasks into 7 frozen skills, 5 from a first draft needing only qualification, at USD 4.29-8.22 of author cost each (USD 55 per skill counting the 13 failed campaigns). The other three tasks did not compile in 18 campaigns, including five with GPT-6 and a pre-registered 150-layout run: on the hardest task every campaign scored 78-95 of 100 but had 3-16 safety aborts, failing the gate of 95% success with zero aborts; a 100-episode exam bounds an abort rate only to 3.6%. On hidden layouts, repair that inherits the previous version beat from-scratch rewriting in 8 of 8 controlled campaigns (sign test p = 0.004); an inherit-only lineage attributes most of the gap to inheritance, with development feedback adding a little (3 of 3, p = 0.125). Write-once campaigns found no detectable first-draft effect of practice (minimum detectable effect 14 points). The frozen skills kept 148/150 successes on new layouts with no model and 147/150 with a DeepSeek-flash caller at USD 0.00028-0.00054 per episode; no direct-control baseline was run.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25114v1
- Authors: Jingwen Bai, Guochao Bai, Canbo Zhang, Shuangqi Li, Minchao Hu, Weichun Huang, Shuang Liu
- Published: 2026-10-18T08:46:13Z
- Age days: 2

</details>
