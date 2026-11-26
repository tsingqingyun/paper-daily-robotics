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
url: "https://arxiv.org/abs/2611.33915v1"
published: "2026-11-25T07:37:06Z"
age_days: 0
score: 32
created: 2026-11-26
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> SEEK 让机器人把一次操作学到的东西带到下一次：留下能根据现场观察选动作的程序，也留下动作实际造成的变化。旧程序适用时直接执行，遇到没覆盖的情况时，再用已有记录帮模型修程序。

## 问题

这里的任务是让机器人反复尝试同一类操作，并且每轮都能用上前几轮的经验。多模态模型在一次执行中可以看反馈、纠正动作，但摘要指出，这些经验通常只留在当轮上下文里。保存旧动作也有问题，比如双夹爪传碗时，碗的位置一变，原来的坐标就可能失效。即便保存了按场景出动作的程序，程序碰到新情况时，修订者仍需要知道过去类似动作究竟造成了什么。

### 用一个例子理解

理解用例（非论文实验）：机器人看到待交接的碗比上一轮更靠左。程序根据新观察重新计算接碗位置，并让第二个夹爪接近。如果交接时碗滑动，系统保存动作与观测到的位移，后续修订时可用这条记录判断松手条件是否需要调整。

## 创新点或方法

SEPP 把操作写成可执行程序，由当下观察决定具体动作。PAEB 记录动作产生的可测效果，失败也留档。运行时先看现有程序能否处理当前情形，适用时无需请求模型，遇到覆盖缺口才借助记录修订。基础模型权重固定，跨轮更新发生在程序和记录上。摘要未说明如何检测覆盖缺口、检索记录或验证修订。

### 方法如何工作

1. 读取当前场景，让已有程序根据当下观察决定动作，避免把旧坐标直接用到新场景。
2. 执行动作并测量结果，把实际变化记入 PAEB，让成功和失败都留下可查的证据。
3. 程序覆盖当前情形时直接运行，省去常规步骤的模型请求。
4. 遇到未覆盖的条件时，用历史效果帮助修订程序，供后续尝试使用。摘要只说明到此。

### 必要术语

- SEPP：根据现场观察选动作的可执行程序，在本文中负责跨轮复用操作逻辑。
- PAEB：持久保存动作实际效果的记录库，在本文中为修订程序提供执行证据。

## 证据

摘要报告，在 RoboDojo 的全部 42 项任务上，积累十次尝试的知识后，平均任务分从 27.0 升至 54.4，成功率从 19.7% 升至 48.0%。其中 34 项使用 GPT-6.2 Astra，五次尝试后 SEEK 得 80.1 分，同一模型直接操作得 49.6 分，模型请求少 77.6%。这些结果支持该基准内的反复尝试能从保留知识中获益。摘要未给出真机结果、单独移除程序或效果记录的对照，也未报告总耗时。

## 局限

作者明确指出，保留下来的程序可能遇到它没覆盖的条件。我会核查 RoboDojo 中各轮的场景差异有多大，因为同类场景内越做越熟，与迁移到新物体或新布局是两种不同的证据。模型请求较少也只刻画开销的一部分。

- **判断**：值得读到程序适用性判断和修订机制，因为这两处决定了系统能否识别哪些经验还能用，以及何时该重新请模型判断。

## 研究关联

如果一项操作的逻辑反复出现、物体位置却经常变化，可以把经验分成两份：程序回答现在怎么做，效果记录帮助解释它在什么条件下失灵。这样，常见情形可以走短执行路径，失败仍能为以后修程序提供线索。

### 下一步读哪里

先查什么信号会把一次执行判定为程序未覆盖，再跟踪一条失败记录如何进入下一次修订。最后核对直接操作基线的尝试预算、初始场景分布和模型请求统计口径。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/SEEK Self-Evolution through Execution Knowledge for Agentic Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific demonstrations or training. However, the robot retains what it learns only in the model's working context. Once the task ends, it loses this execution knowledge, such as how to carry a bowl between two grippers. On the next attempt at the task, the robot may take just as long and repeat the same mistakes. To avoid this repetition, robots must retain execution knowledge across attempts. Yet replaying past actions is insufficient, because their effects depend on the current conditions. Procedures that determine actions from the current scene address this, but when they meet conditions that earlier attempts did not cover, revising them requires the measured effects of earlier actions. We therefore propose SEEK, an agentic framework that retains both, enabling robots to improve across attempts while keeping the underlying model fixed. To adapt retained knowledge to the current scene, SEEK adopts a Self-Evolving Programmatic Policy (SEPP) that encodes manipulation as executable procedures and determines each action from current observations. As the robot executes these procedures, SEEK records the measured effects of its actions, including those from failed attempts, in a Persistent Action-Effect Bank (PAEB). Where a retained procedure applies, it acts without a model request; where it meets a condition it does not cover, this evidence guides its revision. On RoboDojo, knowledge retained over ten attempts raises SEEK's average task score from 27.0 to 54.4 and its success rate from 19.7% to 48.0% across all 42 tasks. On 34 of these tasks with GPT-6.2 Astra, SEEK reaches 80.1 after five attempts, against 49.6 for the same model acting directly, and uses 77.6% fewer model requests. https://zeyangguan.github.io/SEEK-Agentic-Robot-Manipulation/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33915v1
- Authors: Zeyang Guan, Qihao Zhao, Rui Gong, Zhang Haitian, Yalun Dai, Yangyu Huang, Lingao Xiao, Haozhe Du, Xuehui Yu, Ye Lu, Jianjun Gao, Ruoyu Wang, Haowen Bai, Hao Li, Scarlett Li, Kim-Hui Yap
- Published: 2026-11-25T07:37:06Z
- Age days: 0

</details>
