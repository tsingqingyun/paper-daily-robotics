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
url: "https://arxiv.org/abs/2610.21244v1"
published: "2026-10-15T04:40:47Z"
age_days: 2
score: 28
created: 2026-10-18
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# System1-Arena: Which Decisions Can Be Left to System 1?

> [!summary] 这篇论文到底做了什么（基于摘要）
> System1-Arena 把决策统一成“给选项报概率”，比较一次前向计算的快速模型与生成推理过程的模型。它还让模型进入持续变化的环境，检验快速答题的优势是否能转化为连续行动成功。

## 问题

识别钓鱼信息、决定是否转人工等任务，最终都要做离散选择，但并非每次都值得生成长推理。真正的问题是：哪些选择可以快速完成，哪些需要更多计算；而静态题目无法充分回答决策延迟和错误累积对执行的影响。

### 用一个例子理解

理解用例（非论文实验）：输入客户请求和“自动处理、转人工”两个选项，模型输出各自概率，系统据此选择行动；随后请求状态更新，再进行下一次决策。单轮选择正确不代表整条处理流程最终成功。

## 创新点或方法

本文主要提供评测，不是新的训练方法。所有模型接收相同决策请求，评测其选项概率；对开放 LLM，从答案 token 读取结果，同时加入闭环环境和世界会在等待期间继续变化的实时模式。这样既看单次判断，也看连续执行。摘要未说明各模型训练方式、概率读取的完整规则，以及推理模型怎样转换为可比概率。

### 方法如何工作

1. 将任务呈现为相同的决策请求和选项，减少输入形式造成的比较差异。
2. 获取模型对选项的概率，比较准确率与概率校准，并记录延迟及成本。
3. 在闭环环境中执行所选动作，让下一次决策面对动作产生的新状态。
4. 在实时模式下让环境随决策等待继续变化，检验计算耗时对最终成功的影响。

### 必要术语

- System-1 模型：一次前向计算便输出选项概率的模型；本文考察其快速决策能力。
- 概率校准：报出的把握程度与实际正确频率是否相符；本文用它衡量概率是否可信。
- 闭环环境：动作改变后续观察和状态的环境；本文用它检验连续行动结果。

## 证据

摘要列出 9.2 万道问题、105 项任务、268 个公开来源，另有 138 个闭环环境；评测 30 个模型，包括 7 个闭源 LLM、13 个开放 LLM 和 10 个 System-1 模型。最大 System-1 模型在非智能体准确率上达到或超过快速闭源 LLM，概率校准更好，延迟约为其四分之一。一个推理 LLM 最准确，成本约为快速 LLM 的 70 倍。闭环中大型开放 LLM 成功率最高达到 32.9%，小型 System-1 很少成功。摘要未给具体模型、各任务成绩和成本口径。

## 局限

结果没有证明模型失败就是因为缺少显式推理：模型规模、训练分布和行动能力也可能影响成绩。我的待核查问题是闭环成功率如何跨环境汇总、是否控制工具与上下文条件，以及实时模式具体改变了哪些模型的排序。

- **判断**：值得优先读分任务结果和闭环协议，因为它的价值在于划清快速决策的适用范围，而不是给模型排一个总榜。

## 研究关联

可借鉴的是把单次判断能力和连续行动能力分开测量。选择快速决策模型时，除了准确率和概率可信度，还应检查错误进入后续状态后能否恢复，以及延迟是否真的改变环境结果。

### 下一步读哪里

先查概率评分、校准和成本的定义，再比较非智能体与闭环任务的逐项结果；重点核查实时模式如何计时、各模型是否拥有相同观察与动作接口。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/System1-Arena Which Decisions Can Be Left to System 1.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large language models (LLMs) often make discrete decisions, such as flagging phishing or escalating to a human. System-1 models, such as Jev and the OpenAI Decisions API, return probabilities over options in a single forward pass, while System-2 approaches generate reasoning steps. Which decisions can System-1 models handle, and which require generative reasoning? We introduce System1-Arena, a benchmark that gives all models the same decision requests and scores their probabilities. It contains 92k questions across 105 tasks from 268 public sources, in four groups: text classification and knowledge, applied decisions, evaluation and control, and agent and action. It also includes 138 closed-loop environments, from web shopping and SWE-bench coding control to robotics, games, and driving; in real-time mode, the world evolves while a model decides. We evaluate 30 models: 7 closed LLMs, 13 open LLMs read at the answer token, and 10 System-1 models. The largest System-1 models match or exceed fast closed LLMs in non-agentic accuracy, with better-calibrated probabilities at one-quarter of the latency. A reasoning LLM is the most accurate, at about 70x the cost of a fast LLM. In closed loops, large open LLMs succeed most often (up to 32.9%); small System-1 models rarely succeed.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21244v1
- Authors: Tianyu Chen, Xinyang Liu, Ruyi An, Zhendong Wang, Mingyuan Zhou
- Published: 2026-10-15T04:40:47Z
- Age days: 2

</details>
