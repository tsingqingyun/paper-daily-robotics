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
url: "https://arxiv.org/abs/2610.36374"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-10-30
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> HIDRA 处理机器人持续学习时“已有专家还在，却越来越选不准”的问题。它先按指令找专家，再结合当前情境细化选择，并约束检索键的位置关系，减少新任务训练对旧选择规则的干扰。

## 问题

设定是多模态示范连续到来，每份数据只经过一次，且不能保存或重放过去数据。顺序更新会改变表示空间，专家选择所依赖的特征也随之移动，导致本来适合某任务的专家越来越难被找到。瓶颈因此不只是旧技能是否保留，还包括路由能否持续调用正确技能。

### 用一个例子理解

理解用例（非论文实验）：机器人先学开抽屉，再学拿杯子。后来收到“把抽屉拉开”的改写指令，系统先按语义检索相关专家，再结合当前画面细化选择，输出开抽屉动作。这个例子用于说明路由过程，不是论文已验证的单独任务结果。

## 创新点或方法

容易受干扰的专家选择被拆成两层：先用指令做专家检索，再根据情境细化。另一个改动是在键上加几何约束，使同任务的键保持对齐，不同任务的键保持分离，为路由提供更稳定的区分依据。训练时学习这些选择关系并支持扩展专家集合；推理时通过两层注意力选择专家。摘要没有说明专家新增条件、哪些参数冻结，以及情境细化具体读取哪些信号。

### 方法如何工作

1. 从当前指令检索候选专家，先确定任务意图对应的技能范围。
2. 结合当前情境细化检索结果，使相同意图下的不同状态获得合适处理。
3. 训练时约束键的任务内对齐和任务间分离，减少表示变化造成的路由混淆。
4. 随新任务扩展专家并持续学习；新增规则和具体更新参数，摘要只说明到此。

### 必要术语

- 路由：决定当前输入交给哪个专家处理；它是本文主要稳定的对象。
- 检索键：供注意力匹配的表示；本文约束其几何关系来维持选择依据。
- 前向迁移：此前学习对后续新任务学习的帮助；是本文报告改善的指标之一。

## 证据

摘要报告在多个 LIBERO 套件上比较，包括任务序列更异质、语言指令被改写的困难变体；对照涵盖不重放和使用重放的基线。作者称 AUC、前向迁移更好，遗忘较低，在高干扰和语言变化下收益更强。但没有数值、基线名称及资源预算，无法量化优势。提供的证据属于仿真基准，摘要没有报告真机实验。

## 局限

我会核查性能改善是否依赖不断增加专家，以及与重放基线比较时是否控制参数量、训练量和存储。任务内对齐、任务间分离也可能压低相似任务之间的共享，需看迁移结果和消融。输入不足以判断这些代价，不能直接称其部署成本更低。

- **判断**：如果关心持续学习中的专家误选，值得细读双层路由和键约束；若只关心最终成功率，先看资源匹配的比较是否成立。

## 研究关联

这篇提醒我们把“技能丢了”和“技能没被选中”分开检查。如果持续学习系统通过多个专家保留技能，先稳定入口的检索关系，可能比单纯增加专家更有效；这一启示适用于路由确实构成瓶颈的情形。

### 下一步读哪里

先看两层注意力的输入、连接方式和键约束公式，再核查专家扩展规则。实验应检查改写指令设置、任务顺序敏感性，以及去掉几何约束后的误选和遗忘变化；摘要未给出相关表格。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/HIDRA Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Lea.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.36374v1 Announce Type: cross Abstract: Robotic agents operating in real-world environments must adapt continuously from a stream of multimodal demonstrations, often under constraints that preclude storing or revisiting past data. In this replay-free, single-pass lifelong imitation learning setting, sequential updates can progressively distort the representation space, making expert-based approaches particularly sensitive to routing interference, causing expert selection to degrade over time. We propose HIDRA, a structured routing framework that mitigates this issue through a hierarchical dual-attention mechanism, which decouples instruction-level expert retrieval from context-dependent refinement. To further stabilize routing under representation drift, HIDRA introduces a key-level geometric regularization that enforces both alignment within tasks and separation across tasks. The resulting approach enables reliable expert selection while supporting an expandable set of experts for continual adaptation. We evaluate HIDRA on several LIBERO benchmark suites, including more challenging variants with heterogeneous task sequences and paraphrased language instructions. Our approach consistently outperforms both replay-free and replay-based baselines, improving AUC and forward transfer while maintaining low forgetting, with stronger gains under high interference and language variation. The code is available at: https://github.com/yfqi/HIDRA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36374
- Authors: Fanqi Yu, Matteo Tiezzi, Cigdem Beyan, Tommaso Apicella, Vittorio Murino
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
