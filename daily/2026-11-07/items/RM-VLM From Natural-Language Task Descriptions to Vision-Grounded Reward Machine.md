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
url: "https://arxiv.org/abs/2611.08308v1"
published: "2026-11-05T17:10:10Z"
age_days: 1
score: 27
created: 2026-11-07
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines

> [!summary] 这篇论文到底做了什么（基于摘要）
> RM-VLM 把语言任务变成一张记录任务进度的状态图，再让视觉语言模型看图判断该往哪一步走。它还估计离下一步有多近，让智能体不必等整件事完成才收到奖励。

## 问题

任务若要求“先做甲，再做乙”，当前画面可能不足以决定奖励，还得知道先前完成了什么。奖励机能记录这段历史，但通常需要人为给每个环境编写判断规则，把观察转成“已到达甲地”等命题；换环境就要重新做这部分工作。

### 用一个例子理解

理解用例（非论文实验）：输入“先拿钥匙，再到门口”和相机图像；奖励机先等待“拿到钥匙”，视觉判断成立后才切换到“到门口”；输出对应阶段的训练奖励，避免把提前到门口误算成完成任务。

## 创新点或方法

旧做法由人写命题识别规则；RM-VLM 改为让 LLM 从任务描述生成奖励机，让 VLM 从图像判断命题是否成立。奖励机负责记顺序，VLM 负责认现场，另一个基于 VLM 的价值估计器评估每次状态转移的进度，生成更连续的奖励。摘要明确这些组件用于策略学习，但没有交代训练完成后，执行策略是否仍需调用它们，也未说明基础模型是否微调。

### 方法如何工作

1. 把自然语言任务交给 LLM，得到奖励机，用显式状态保存任务顺序。
2. 把当前图像交给 VLM，得到命题判断，让视觉观察能够触发奖励机转移。
3. 估计朝下一次转移推进的程度，产生密集奖励，缓解只有完成时才有反馈的问题。
4. 用奖励机指导策略学习；策略更新方式和部署阶段的组件保留情况，摘要只说明到此。

### 必要术语

- 奖励机：用状态图表示奖励规则；本文用它记录任务进度和先后关系。
- 非马尔可夫任务：奖励还取决于历史；本文借助奖励机状态保存相关历史。
- 命题落地：把“拿到钥匙”等文字条件对应到观察；本文由 VLM 从图像判断。
- 密集奖励：过程中也给反馈；本文根据接近下一次状态转移的程度提供信号。

## 证据

摘要报告了有历史依赖的网格导航、机器人操作和三维物体收集三个领域，与已有 VLM 奖励方法比较，所有测试领域的任务成功率均更高。没有提供具体数值、基线名称、重复次数，也未明确机器人操作是真机还是仿真。因此证据支持所测领域内的成功率优势，尚不能判断优势幅度或部署成本。

## 局限

需要核查生成的奖励机是否忠实表达原任务，以及视觉误判是否会触发错误转移。摘要没有给出这些误差的分析，不能据此断言作者未做；现有信息也不足以判断成功率收益分别来自任务结构还是更密集的奖励。

- **判断**：值得读到奖励机生成、视觉标注和奖励计算的具体接口，因为方法能否复用，取决于这三者如何共同定义一次可靠的任务推进。

## 研究关联

这里值得借鉴的是把“认出发生了什么”和“判断这一步是否符合任务顺序”分开。对于完成顺序会改变奖励的任务，显式保存任务进度，可能比让视觉模型每次从单张图直接给总分更容易检查。

### 下一步读哪里

下一步核查：语言生成的奖励机如何校验；视觉命题采用什么判定阈值；进度估计怎样转成奖励；是否有分别移除任务结构和密集奖励的消融，以及评估时的模型调用成本。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/RM-VLM From Natural-Language Task Descriptions to Vision-Grounded Reward Machine.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework. However, they assume a labelling function, a proposition-grounding oracle for observations, which must be manually engineered for each environment, limiting their wider applicability. In this work, we address this limitation by proposing RM-VLM, a novel approach in which a large language model (LLM) generates an RM from a natural-language task description, and a vision-language model (VLM) acts as the labelling function, grounding the RM's propositions over image-based observations during RM-guided policy learning. A VLM-based value function estimator is used to assess the agent's progress towards each RM transition and derive a dense reward signal. We evaluate RM-VLM on three domains covering non-Markovian grid-world navigation, robotic manipulation, and 3D object collection. Our experimental results show that RM-VLM consistently achieves higher task success rates than existing VLM-based reward methods across all tested domains.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08308v1
- Authors: Roko Parac, Christos Ziakas, Leo Ardon, Alessandra Russo
- Published: 2026-11-05T17:10:10Z
- Age days: 1

</details>
