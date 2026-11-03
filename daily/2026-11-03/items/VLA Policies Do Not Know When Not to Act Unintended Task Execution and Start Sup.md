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
url: "https://arxiv.org/abs/2610.41609v1"
published: "2026-10-30T11:45:50Z"
age_days: 3
score: 28
created: 2026-11-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇发现，VLA 即使没有收到有效任务，也可能主动移动并完成某个任务：语言能影响“做什么”，却未必控制“要不要开始”。作者测试了三种启动抑制办法，其中比较有效指令与空指令首段动作的门控，在六个检查点中的五个上能拦住非任务输入。

## 问题

具体问题是机器人面对空白、中性、胡话、不可行和错误任务指令时，是否仍会启动。常规任务成功率无法回答这一点：模型可能很会执行任务，却默认场景中总有任务可做。需要分别测量开始移动、完成了什么，以及语言究竟改变了哪部分行为。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和空指令；策略仍生成伸向杯子的动作。门控再计算空指令参考动作，发现两者接近，于是输出保持静止；这个例子解释机制，不代表已验证的真机保护。

## 创新点或方法

作者先固定初始状态，只换指令，形成配对测试。随后尝试三种改动：推理时添加“没任务就别动”的前缀；推理时比较当前指令与空指令产生的首个动作块，过于接近就保持静止；训练时用非任务输入微调静止行为。门控的直觉是：如果换上指令几乎不改变动作，当前动作可能主要来自场景而非任务要求。相似度阈值和微调数据构造未说明。

### 方法如何工作

1. 固定环境初始状态并替换指令，减少场景差异对行为比较的干扰。
2. 分别记录启动和任务完成，识别“动了但没完成”与“自行完成任务”的区别。
3. 生成当前指令和空指令的首个动作块，用相似程度判断指令是否实质改变了启动动作。
4. 相似时保持静止，再检查非任务拦截效果及有效任务是否被误拦；后者摘要未给结果。

### 必要术语

- VLA：把视觉、语言输入转成机器人动作的策略；本文检查它是否把语言当作启动条件。
- 动作块：一次预测的一段动作；门控比较的是第一段。
- 配对测试：同一初始状态使用不同指令；用于更清楚地观察指令带来的行为差异。

## 证据

在 LIBERO-Goal 仿真中测试六个模型检查点。摘要报告，空指令下六者每个回合都启动，五者还经常完成未被指定的任务；两个 GR00T 检查点甚至在不可行指令下移动。前缀对六者均未阻止启动；门控在五者上能拦住非任务输入。微调后非任务输入不再导致任务完成，但仍不能可靠保持静止，也未抑制不可行指令下的启动。摘要没有给回合数、门控误拦有效任务的比例或真机结果。

## 局限

证据来自指定仿真环境和六个检查点，不能直接推成所有 VLA 或真机的发生率。门控利用的是动作相似性，并未证明它识别了人的授权；有效任务若恰好与默认动作接近，也可能被拦，需看误拦实验。

- **判断**：优先读评测协议与门控错误分析，它揭示了成功率之外一个明确且可复测的缺口。

## 研究关联

最直接的启示是把“动作许可”单独验收。只统计非任务输入下是否完成任务，会漏掉已经移动却尚未成功的情况；设计评测时应把启动率与完成率分开记录。

### 下一步读哪里

核查移动判定阈值、各类指令样本、配对回合数，以及门控在有效任务上的保留率。还应检查“错误任务”与“不可行任务”分别怎样定义。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/VLA Policies Do Not Know When Not to Act Unintended Task Execution and Start Sup.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A robot should act only on an instruction from a person or on an intent that the robot explicitly represents and generates. Unintended actions taken without such an instruction can cause risk or inconvenience to people and the environment. We examine how recent vision-language-action (VLA) policies respond when the instruction is missing or meaningless. We apply a paired protocol with empty, neutral, nonsense, infeasible, and wrong-task instructions to six model checkpoints in LIBERO-Goal simulation. Holding the initial state fixed and varying only the instruction, we ask three questions: whether the robot starts to move, which task it completes, and what the instruction determines. Even when the instruction was empty, the robot started moving in every episode with all six checkpoints, and with five of them it often completed a task that the instruction had not specified. On two GR00T checkpoints, the instruction determined which task was executed but not whether the robot started moving; the robot moved even on infeasible instructions. We then tested three methods for suppressing the start: prepending "if no task is given do not move" to the instruction; a gate that holds the robot when the first action chunk for the given instruction nearly equals that for an empty instruction; and fine-tuning the policy to hold still on non-task inputs. The prefix stopped the robot in none of the six checkpoints, and the gate held it on non-task inputs in five of the six checkpoints. The fine-tuned policy never completed a task on non-task inputs, but it did not reliably keep the robot still, and it failed to suppress the start on infeasible instructions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.41609v1
- Authors: Minsu Jang, Jae-Woo Choi, Youngwoo Yoon, Dohyung Kim
- Published: 2026-10-30T11:45:50Z
- Age days: 3

</details>
