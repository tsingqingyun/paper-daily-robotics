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
url: "https://arxiv.org/abs/2610.00982"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-03
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> Divide-and-Remember（D&R）让机器人学习保留“当前画面看不出、但会影响下一动作”的历史。它反复从 2K 个 token 中选出 K 个，并共享同一个选择器，让固定大小的记忆处理不断增长的历史。

## 问题

在依赖历史的操作任务中，同一张当前画面可能对应不同正确动作，例如物体已被检查过还是尚未检查。现有记忆方法常用人为规则决定保留什么，如选择像素变化大的帧；画面变化不一定等于动作相关，因此收益随任务变化。

### 用一个例子理解

理解用例（非论文实验）：机器人先看到指示灯要求取左杯，之后灯熄灭、两杯外观相同。输入当前画面和历史；D&R 保留灯亮时的线索；策略据此输出取左杯的动作。

## 创新点或方法

旧做法按预设视觉规则记忆，本文将选择历史变成学习问题：给定当前观察后，记忆应尽量补充关于正确动作的信息。训练时端到端学习共享选择器和记忆函数，递归地解决小规模筛选；摘要未说明具体损失如何实现互信息目标。推理时沿递归结构压缩历史，最终用有限 token 提供动作所需线索，不必把全部历史交给策略。

### 方法如何工作

1. 把历史表示为可选择的 token，使过去事件能进入记忆筛选；摘要未说明编码细节。
2. 将长历史拆成每次从 2K 中选 K 的子问题，降低单次选择的计算规模。
3. 各递归块使用同一个学习到的选择器，使不同层级按共同规则保留动作线索。
4. 继续递归压缩并将记忆交给策略，补充当前观察无法决定动作的信息。

### 必要术语

- 部分可观测任务：当前观察不足以确定应做什么；这是本文需要记忆的原因。
- 条件互信息：已知当前观察后，记忆还能提供多少动作信息；本文用它描述理想记忆目标。
- top-K 选择：从候选中保留 K 个；本文用固定规模选择支撑长历史处理。

## 证据

摘要称，在 RoboMME 的 16 个长时程操作任务上，D&R 用 64 个记忆 token 达到最高平均成功率，并在要求记住何时、何地、什么和如何行动的四组任务中均有收益；真机实验也观察到收益。摘要未给成功率、提升幅度、基线名称及真机任务数量，因而无法判断优势大小或统计稳定性。

## 局限

摘要未列出明确局限。我的待核查问题是：早期筛掉的信息以后是否还能找回，以及选择器能否识别训练中少见的关键事件。“支持无界历史”说明结构可继续递归，不意味着任意久远的信息都能无损保留。

- **判断**：优先读递归选择和训练目标，理解它怎样把“重要历史”落实为动作相关性；性能判断还需具体对比表。

## 研究关联

这里值得借鉴的是把记忆预算花在当前观察缺少的动作依据上。历史很长、但真正有用的事件很少时，学习筛选比单纯增加上下文长度更值得尝试。

### 下一步读哪里

核查历史 token 如何形成、递归块如何组织、选择操作如何接受训练信号，以及 64 token 预算包含哪些信息。再看四组任务的逐项结果和真机对照，判断收益是否主要来自某类记忆。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/Divide-and-Remember Recursive Action-Relevant Memory for Long-Horizon VLA Polici.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.00982v1 Announce Type: new Abstract: Vision-language-action (VLA) models struggle on history-dependent manipulation tasks, where the current observation alone does not determine the action, and the policy needs a memory of the history. Existing memory methods decide what to remember by design, for example, keeping frames with large pixel changes, and show inconsistent gains across tasks. We view what to remember as an optimisation problem. From the POMDP formulation of imitation learning, we show that the optimal memory maximises the conditional mutual information $I(a_t; m_t \mid o_t)$ between the action and the memory given the current observation. Intuitively, this means preserving the action-relevant information in the history that is not already contained in the current observation. Based on our analysis, we propose Divide-and-Remember (D&R), a recursive memory method that learns a memory function $m_t = M(h_t)$ and scales to long contexts while staying compute-light. It involves two strategies: (1) the selection over the full history is divided recursively into subproblems of top-$K$ selection over $2K$ tokens, so that fixed-size, lightweight selectors learned end-to-end support an unbounded history; (2) all recursion blocks share one selector, which captures the selection rule common to every block and keeps the method efficient. On RoboMME, a benchmark of 16 long-horizon manipulation tasks that require remembering when, where, what, and how to act, D&R achieves a state-of-the-art average success rate with consistent gains across all four suites under a budget of only 64 tokens; real-robot experiments show the same gain. Code, checkpoints and more results are at https://dnr-memory.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.00982
- Authors: Xuehui Yu, Eason Yu, Meiyi Wang, Haozhe Du, Stefano V. Albrecht, Harold Soh
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
