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
url: "https://arxiv.org/abs/2610.12369v1"
published: "2026-10-08T17:29:08Z"
age_days: 1
score: 31
created: 2026-10-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

> [!summary] 这篇论文到底做了什么（基于摘要）
> COAP把机器人在线决策写进持续维护状态的代码：代码从图像和本体感觉跟踪现场，再据此决定动作，测试时无需VLM或VLA参与决策。编码智能体在开发阶段反复修改共享库，使不同任务能够复用已有逻辑。

## 问题

任务是让机器人跨回合执行操作，并让能力随任务积累。摘要中的VLA和智能体调用框架在运行时持续调用模型做决策；COAP希望把状态记录、失败恢复和任务扩展变成可检查的代码。它的前提是现场能够被足够准确地表示，否则明确的规则也会依据错误状态行动。

### 用一个例子理解

理解用例（非论文实验）：输入双臂机器人面前的盒子图像和关节状态；代码更新“盒子是否被固定、盖子是否打开”等状态，再按条件调用固定或开盖动作；输出下一条命令，并在执行后重新检查状态。

## 创新点或方法

旧做法在控制过程中由模型解释观测并决定下一步；本文改成代码测量和跟踪机器人、环境、任务状态，再完全依据这些状态决策。同一代码跨回合使用，不同任务共享一个可继承、扩展的库。开发阶段由编码智能体在闭环中修改库，摘要未给出修改、评估和接受改动的具体流程，也没有描述常规参数训练。测试时直接运行库，VLM或VLA不在决策回路中；这不等于摘要已经说明所有图像处理组件的实现。

### 方法如何工作

1. 从图像和本体感觉提取并保存状态，给代码提供明确的决策依据；具体提取算法摘要未说明。
2. 依据状态执行规则并更新任务进度，使下一步决策能够考虑此前执行结果。
3. 把动作与恢复逻辑放进共享库，让不同任务复用或扩展已有代码。
4. 开发时由编码智能体闭环修改库，测试时运行固定代码；修改的验收机制摘要只说明到此。

### 必要术语

- 显式状态：直接保存的环境和任务信息；是COAP规则判断的依据。
- COAP：完全用代码承担在线策略决策；本文以共享库组织这种策略。
- 递归自我改进：利用已有系统的执行反馈继续修改系统；本文把代码库作为改进对象。

## 证据

摘要报告共享库在RoboDojo的42个双臂任务上达到70.24%成功率，测试时没有模型。未给对比基线分数、重复次数、逐任务结果或库开发成本，也未明确评测是仿真还是真机。因此它展示了该代码库在这组任务上的可行性，尚不足以证明比模型策略普遍更强、更便宜，或能持续自我改进。

## 局限

作者明确把上限归于状态表示的准确度和代码逻辑的稳健性。我会进一步核查遮挡、状态误判和未见扰动下的恢复表现，以及新任务改库后会不会破坏旧任务。单个最终成功率不能证明递归修改带来了持续、稳定的能力积累。

- **判断**：值得读到状态提取实现和共享库修改记录，因为论文的说服力取决于代码如何处理真实的不确定性，以及能力怎样累积。

## 研究关联

值得借鉴的是把可复用能力放在显式状态和共享执行逻辑里：当任务阶段、恢复条件和动作前提能清楚表达时，解决一个任务所写的代码可能成为下一个任务的起点。是否适用，首先取决于状态是否可可靠获取。

### 下一步读哪里

核查图像如何变成状态、失败如何检测、库更新如何验证；再看42个任务的环境属性、逐任务表现、在线成本，以及每轮修改对旧任务和新任务的影响。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/Embodied Turing Machines Stateful Code for Robot Recursive Self-Improvement.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can be written entirely in code. We therefore propose Code-Only-as-Policy (COAP): code measures and tracks the robot, environment, and task state from camera images and proprioception, and makes every decision from it. The same code applies across episodes, and different tasks share one library without a VLM or VLA in the loop. Compared with VLAs and Agent Harnesses, we analyze three advantages of COAP: (i) Explicit State: the state can be stored in code; (ii) Execution: code makes decision making controllable, recovers from failures flexibly, and runs fast and cheaply online; (iii) Extensibility: new tasks reuse, inherit, or extend the shared library, so capabilities can accumulate over tasks. These advantages make COAP a suitable medium for recursive self-improvement (RSI): coding agents develop the library in a closed loop, and each change is explicit and controllable. On RoboDojo's 42 bimanual tasks, the resulting library reaches a success rate of 70.24% without a model at test time. The upper bound of COAP lies in how accurately the state is represented for decision making and how robust the code logic is. We thus propose COAP as a new paradigm for embodied tasks; since it applies across episodes, it can also serve as an efficient data engine for VLAs and Agent Harnesses.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12369v1
- Authors: Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- Published: 2026-10-08T17:29:08Z
- Age days: 1

</details>
