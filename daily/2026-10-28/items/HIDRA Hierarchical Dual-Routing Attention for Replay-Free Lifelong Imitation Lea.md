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
url: "https://arxiv.org/abs/2610.36374v1"
published: "2026-10-26T22:43:30Z"
age_days: 1
score: 34
created: 2026-10-28
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> HIDRA 针对机器人连续学习新任务后“选错专家”的问题：先按指令找专家，再按当前情境细化选择。它还约束用于检索的键，让同任务保持接近、不同任务保持分离，减少学习新任务时的路由混乱。

## 问题

机器人按顺序接收多模态示范，每条数据只学一次，又不能保存或重看旧数据。持续更新会改变内部表征，原先有效的专家检索关系可能失效；即使已有专家仍有用，系统也可能无法正确调用它。

### 用一个例子理解

理解用例（非论文实验）：机器人依次学开抽屉和取杯子，之后收到改写后的“把抽屉拉出来”；HIDRA 先依据指令检索，再结合当前场景细化选择，输出由相关专家产生的动作。能否做到需实验验证。

## 创新点或方法

相比让专家选择共同承受指令与情境变化，HIDRA 用分层双注意力把指令级专家检索和情境细化拆开，并在检索键上加入几何约束，维持任务内对齐与任务间分离。训练时随新示范更新，并支持扩展专家集合；推理时利用两级路由选择专家。摘要未说明专家扩展触发条件、哪些参数被冻结，以及两级注意力的具体计算。

### 方法如何工作

1. 按任务流只访问当前示范，更新系统，同时面对旧表征被新学习改变的风险。
2. 依据指令检索专家，先缩小与任务相关的候选范围。
3. 结合当前情境细化路由，使选择能适应具体观测；两级结合方式摘要未说明。
4. 训练时约束检索键的任务内对齐和任务间分离，减少后续更新造成的选择混乱。
5. 按机制扩展专家集合以容纳新能力；何时新增及如何控制规模仍需核查。

### 必要术语

- 无回放单遍学习：旧数据不保存重学，当前数据只访问一次；本文在此条件下持续学习。
- 路由：决定调用哪个专家；本文重点保护这一选择过程。
- 表征漂移：学习新任务后内部编码发生变化；本文关注它如何破坏专家检索。
- 前向迁移：先前学习对后续任务学习的帮助；本文将其作为评测维度之一。

## 证据

摘要报告在多个 LIBERO 套件上测试，也覆盖异质任务序列和指令改写；相比无回放与有回放基线，AUC、前向迁移更好，同时遗忘较低，高干扰和语言变化时收益更强。没有具体数值、基线名称、任务顺序及资源预算，因此不能判断优势幅度，也不能认定无回放普遍优于回放。材料提供的是基准证据，未报告真机结果。

## 局限

路由稳定是合理解释，但其因果作用仍需双注意力和几何约束的分别消融。专家数量可增长也意味着存储和计算可能增长；无回放不等于固定资源，长期扩展成本值得核查。

- **判断**：值得细读路由机制和消融，尤其是表征漂移如何影响专家选择；当前摘要不足以判断长期资源代价。

## 研究关联

可借鉴的是把“旧能力丢了”和“旧能力叫不出来”分开诊断。使用专家集合做持续学习时，应同时测专家本身的能力与路由准确性，才能知道该保护哪些参数。

### 下一步读哪里

先查检索键来自哪里、几何约束怎样计算，再看去掉两级路由或约束后的表现。还应核查任务边界是否已知、专家增长规则，以及与回放方法比较时的数据访问量、参数量和计算预算。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/HIDRA Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Lea.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic agents operating in real-world environments must adapt continuously from a stream of multimodal demonstrations, often under constraints that preclude storing or revisiting past data. In this replay-free, single-pass lifelong imitation learning setting, sequential updates can progressively distort the representation space, making expert-based approaches particularly sensitive to routing interference, causing expert selection to degrade over time. We propose HIDRA, a structured routing framework that mitigates this issue through a hierarchical dual-attention mechanism, which decouples instruction-level expert retrieval from context-dependent refinement. To further stabilize routing under representation drift, HIDRA introduces a key-level geometric regularization that enforces both alignment within tasks and separation across tasks. The resulting approach enables reliable expert selection while supporting an expandable set of experts for continual adaptation. We evaluate HIDRA on several LIBERO benchmark suites, including more challenging variants with heterogeneous task sequences and paraphrased language instructions. Our approach consistently outperforms both replay-free and replay-based baselines, improving AUC and forward transfer while maintaining low forgetting, with stronger gains under high interference and language variation. The code is available at: https://github.com/yfqi/HIDRA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36374v1
- Authors: Fanqi Yu, Matteo Tiezzi, Cigdem Beyan, Tommaso Apicella, Vittorio Murino
- Published: 2026-10-26T22:43:30Z
- Age days: 1

</details>
