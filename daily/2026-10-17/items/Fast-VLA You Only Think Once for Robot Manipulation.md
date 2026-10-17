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
url: "https://arxiv.org/abs/2610.21389v1"
published: "2026-10-15T07:05:16Z"
age_days: 1
score: 35
created: 2026-10-17
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Fast-VLA: You Only Think Once for Robot Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Fast-VLA 每回合只运行一次大型视觉语言模型，把指令和初始画面存成任务记忆。随后由轻量动作模块持续读取新画面、机器人状态和这份记忆，闭环输出动作。

## 问题

常见 VLA 每预测一段动作，就让数十亿参数模型重新处理任务上下文。但机械臂的位置不断变化，“要完成什么任务”通常变化较慢；反复重算这部分信息会增加反馈回路的延迟和内存负担。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放到托盘”和初始画面，先生成任务记忆；执行中 actor 读取杯子新位置与关节状态，检索记忆后不断输出下一段动作。

## 创新点或方法

本文把每轮重算改成回合开始时一次预填充：冻结的 4B VLM 生成多层键值任务记忆，之后保持固定。在线 actor 将可学习的时间、机械臂索引查询与当前视觉和本体反馈融合，再从固定记忆检索上下文并预测动作块。因此固定的是任务上下文，当前状态仍持续更新。训练时 VLM 冻结，actor 和查询的具体损失、训练数据及更新设置，摘要未说明。

### 方法如何工作

1. 用指令与初始视图调用一次冻结 VLM，建立本回合任务记忆。
2. 每次控制更新读取当前画面和本体状态，获得执行进展。
3. 把反馈与时间、机械臂查询融合，形成用于检索记忆的动作查询。
4. 结合检索结果预测动作块，下一轮继续读取新反馈，无需重跑 VLM。

### 必要术语

- 键值记忆：供查询检索的成对表示；本文用来保存任务上下文。
- 本体反馈：关节等机器人自身状态；让在线模块知道当前身体位置。
- 动作块：一次预测连续多步动作；是本文 actor 的输出形式。

## 证据

摘要报告 RoboTwin 2.0 Clean、Randomized 成功率为 92.46%、92.40%，LIBERO、LIBERO-Plus 为 95.95%、79.11%。同一硬件上，相比三个持续条件化基线，RoboTwin 摊销策略推理耗时降低 10.9—17.1 倍；预填充后在线驻留内存为 1.22 GiB。任务记忆交换实验还表明 actor 依赖本回合匹配的记忆。这支持所测基准上的高效控制，但摘要未给真机结果、基线名称或完整启动开销。

## 局限

固定初始记忆能否处理途中改指令、初始画面遮挡或新出现的关键物体，需要核查。1.22 GiB 指预填充后的在线驻留内存，不能当成整个系统的峰值；推理加速也不直接等于机器人完成任务的同倍加速。

- **判断**：值得细读缓存接口和耗时统计，因为它具体展示了怎样减少大模型调用，同时保留状态反馈。

## 研究关联

可借鉴的是按变化速度拆计算：慢变的任务理解可以缓存，快变的机器人状态留在反馈回路。值得尝试的前提是任务目标在回合内稳定，而且在线模块仍能从新观测中获得控制所需信息。

### 下一步读哪里

优先核查多层记忆如何连接 actor、时间与机械臂查询怎样使用，以及摊销时间是否计入初始化。再看记忆交换实验的控制变量和任务中途变化的适用条件。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/Fast-VLA You Only Think Once for Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies commonly place a multi-billion-parameter model inside the feedback loop, repeatedly recomputing task context whenever they predict a new action chunk. Yet task understanding changes far more slowly than the robot state. We introduce Fast-VLA, which invokes a frozen 4B VLM once per episode to contextualize the instruction and initial views as fixed, multi-layer key-value task memory. During execution, a lightweight online actor fuses learned time- and arm-indexed queries with current visual and proprioceptive feedback to form action queries. These queries retrieve task context from the fixed memory and predict action chunks without re-running the foundation model. Fast-VLA achieves 92.46% and 92.40% success on RoboTwin 2.0 Clean and Randomized, and 95.95% and 79.11% on LIBERO and LIBERO-Plus evaluation. Against three continually conditioned baselines on the same hardware, it reduces RoboTwin amortized policy inference time by 10.9-17.1x and requires 1.22 GiB of post-prefill online resident memory. Task-memory swaps further show that the actor relies on episode-matched task memory. These results show that task context can be established once while closed-loop control remains responsive throughout execution. Project page: https://garfield-kh.github.io/FastVLA

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21389v1
- Authors: Kehong Gong, Guanli Hou, Xiaoxu Zheng, Qi Wang, Mingxi Xu, Anbang Zhai, Xiaoyu He, Mingyuan Zhang, Michael Bi Mi
- Published: 2026-10-15T07:05:16Z
- Age days: 1

</details>
