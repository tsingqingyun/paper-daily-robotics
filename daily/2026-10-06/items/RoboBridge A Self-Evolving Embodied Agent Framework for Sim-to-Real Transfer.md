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
url: "https://arxiv.org/abs/2610.02717v1"
published: "2026-10-02T02:53:57Z"
age_days: 3
score: 33
created: 2026-10-06
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real"]
---

# RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboBridge 把仿真到现实的迁移变成“继续修改可执行技能”：保留任务流程，依据真实执行反馈调整不适用的操作。底层 VLA 作为动作工具使用，通过推理时引导执行，不需要重新训练它。

## 问题

任务是把仿真中的操作能力迁移到实体机器人，并在部署后继续适应。摘要指出，端到端 VLA 通常需要校准仿真画面与动力学、补采真实示范并继续训练；工具型智能体虽然会编排任务和复用经验，却主要在同一环境内工作。真正瓶颈是：怎样保留已有流程，只修改换环境后失效的部分。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放到托盘”及相机观察；智能体调用已有定位、抓取、放置和检查流程。若真实环境中放置失败，它生成并评估相关操作的修改，输出可复用的新技能；具体修改什么参数，输入材料未说明。

## 创新点或方法

旧做法主要调整策略或适配环境；RoboBridge 改为保存连接任务意图、观察、工具操作和结果检查的程序。执行反馈触发候选修改，评估后才保存或拒绝。共享的任务语义和交互接口让流程骨架可以迁移，环境相关操作则单独修订。底层预训练 VLA 不更新权重，执行时接受额外引导；引导的形式、技能如何生成和评估，摘要未说明。

### 方法如何工作

1. 把任务意图、观察、工具调用和结果检查连接成程序，得到可执行、可修订的任务知识。
2. 执行程序并收集反馈，用成功或失败信息找出需要调整的操作。
3. 生成候选技能修改并评估，决定保留还是拒绝，避免未经检查的修改直接进入技能库。
4. 在现实中继续复用共享流程并修订环境相关操作；底层 VLA 通过推理时引导执行，摘要只说明到此。

### 必要术语

- 可执行技能：能被实际调用的操作程序；本文把它作为迁移和修改的单位。
- 推理时引导：执行时额外影响模型的动作选择；本文借此使用 VLA 而不更新其权重。
- 结果验证：检查操作是否达到目标；本文用它连接执行与后续技能修订。

## 证据

摘要说明在 LIBERO-PRO 和对应实体任务上研究技能演化与迁移后适应，但未给出任务数量、基线、成功率或适应成本。因此能确认作者设置了仿真与实体评估，尚不能判断是否优于重新训练策略，也不能量化持续修改带来的收益。

## 局限

我最想核查的是候选修改是否会破坏其他任务，以及评估失败时怎样回退。摘要没有交代这些保障，也没有说明真实反馈需要多少次交互；这些是待查问题，不能据此认定全文没有处理。

- **判断**：值得读方法部分，重点看技能表示、修改粒度和保留标准；目前摘要足以说明思路，尚不足以判断迁移效果。

## 研究关联

可借鉴的是把“任务流程正确”和“具体动作适合当前环境”分开维护。当任务顺序稳定、工具接口一致，而观察或执行条件变化时，修改局部程序有望避免整套重学；前提是能可靠检查执行结果。

### 下一步读哪里

先检查技能程序实例，再查推理时如何引导 VLA、候选修改如何评估，以及 LIBERO-PRO 与实体任务的对应关系。重点核查适应次数、与重新训练的比较及旧任务是否退化。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 Sim2Real
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/RoboBridge A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A key challenge in bringing embodied intelligence into the real world is transferring capabilities from simulation to reality and enabling agents to continually adapt after deployment. End-to-end vision-language-action policies provide strong manipulation capabilities, but their transfer to physical environments typically relies on calibrating simulated visual and dynamical conditions, collecting additional target-domain demonstrations, and optimizing the policy through further training. Tool-using embodied agents offer flexible task orchestration, yet existing systems primarily emphasize task execution and experience reuse within a given environment, with limited support for transferring procedural knowledge and continuously adapting it across simulation and reality. We propose RoboBridge, a framework that treats sim-to-real transfer as the continued adaptation of executable task skills. The agent represents task knowledge as procedures connecting task intent, observations, tool operations, and outcome verification. Interaction feedback is used to generate candidate skill revisions, which are evaluated before being persisted or rejected. A pretrained vision-language-action policy is exposed as a reusable action tool and enhanced with inference-time guidance, enabling fine-grained execution without retraining the underlying policy. RoboBridge grounds transferable skills in task semantics and interaction interfaces shared across simulation and reality. This representation preserves reusable task structure while allowing environment-dependent operations to be selectively revised through real-world execution feedback. We evaluate the framework on LIBERO-PRO and corresponding physical tasks, studying both skill evolution and post-transfer adaptation. Our framework provides a route from one-shot policy deployment to continual procedural learning across environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02717v1
- Authors: Chenxi Li, Zhangrui Zhao, Rui Li, Yuan Gao, Kehui Liu, Jiarui Li, Dong Wang, Tong Si, Minting Pan, Wanli Ouyang, Dongzhan Zhou
- Published: 2026-10-02T02:53:57Z
- Age days: 3

</details>
