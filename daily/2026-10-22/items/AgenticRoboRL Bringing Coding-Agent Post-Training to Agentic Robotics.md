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
url: "https://arxiv.org/abs/2610.28589"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-10-22
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

> [!summary] 这篇论文到底做了什么（基于摘要）
> AgenticRoboRL 直接训练机器人系统里的规划模型，让它在多轮执行中学会做更有效的决策。它用不同执行系统各自的适配器，把调用 VLA 技能或生成控制代码的交互接到同一套训练流程。

## 问题

复杂操作系统通常由规划器决定做什么，再由执行系统完成动作。摘要指出，已有工作多改善执行工具或外部记忆，却仍依赖强闭源规划器；想训练规划器，又会遇到执行接口不统一的问题：技能调用和代码执行产生的交互形式不同。

### 用一个例子理解

理解用例（非论文实验）：输入“把两件物体分别放入指定容器”；规划器先调用抓取技能，读取执行反馈，再决定重试或放置；输出一串逐轮调整的调用。训练时，这段交互与最终任务结果关联，用来调整规划器。

## 创新点或方法

旧做法主要改规划器周围的组件；本文保持执行组件固定，先监督微调规划器，再用多轮强化学习继续训练。适配器负责把各执行系统记录的规划交互与任务结果连接起来，使它们进入共同训练管线。推理时，训练后的规划器仍通过相应执行接口完成任务；奖励设计、训练轮数和动作表示均未在摘要说明。

### 方法如何工作

1. 记录规划器与执行系统的多轮交互及任务结果，为训练建立决策与后果的对应。
2. 由各系统的适配器连接这些记录，使技能调用和控制代码交互可进入共同管线。
3. 先做监督微调，再进行多轮强化学习，训练规划器作出更有效的连续决策。
4. 部署训练后的规划器，通过固定执行组件完成任务，以成功率检查整体效果。

### 必要术语

- 执行系统（harness）：负责接收规划器指令、调用动作并返回反馈的软件；本文保持其执行组件固定。
- 监督微调：用示范交互训练模型如何作答和行动；它是本文训练的第一阶段。
- 多轮强化学习：根据连续交互后的结果调整决策；本文用它继续训练规划器。
- 信用分配：判断最终成败与哪些先前决策有关；这是理解本文训练实现时需要核查的问题。

## 证据

摘要给出 LIBERO-PRO 成功率：9B 规划器从 18.1% 升至 71.0%，且不使用外部记忆；Codex（GPT-5.5）使用外部记忆时为 72.1%。这支持该设置下后训练能大幅改善规划器，也说明最终成绩接近所列参照。但两者记忆条件不同，不能当作模型能力的严格等条件比较。摘要未给重复试验、误差范围及各执行机制的分项成绩，也未提供真机结果。

## 局限

总成功率不能区分监督微调和强化学习各贡献多少，也不能说明收益跨执行系统转移到何种程度。这些是我会查的实验，并非断言全文未做。作者说将发布框架和权重，输入并不能确认已经发布。

- **判断**：值得深入读训练配方和分项消融：成功率变化足够明确，但真正可复用的部分取决于交互记录、奖励和适配器如何实现。

## 研究关联

这里最值得借鉴的是，把执行接口差异留给适配器处理，让任务成败成为训练规划器的反馈。若执行组件已经可用、但多轮决策仍常失败，改进规划模型本身就是值得检验的方向。

### 下一步读哪里

先查监督数据如何获得、多轮强化学习如何分配任务结果的信用，以及适配器保留哪些观察和失败信息；再看固定执行组件的具体范围、不同执行接口的成绩和外部记忆对照。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/AgenticRoboRL Bringing Coding-Agent Post-Training to Agentic Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.28589v1 Announce Type: new Abstract: Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether post-training can also improve robot planners. However, applying it across robot harnesses requires accommodating different execution mechanisms, including VLA skill invocation and control-code generation. To this end, we introduce AgenticRoboRL, a framework for post-training robot planners across different harnesses. The training recipe combines supervised fine-tuning with multi-turn reinforcement learning. To accommodate different execution mechanisms, harness-specific adapters connect recorded planner interactions with task outcomes, enabling a common RL training pipeline while keeping execution components fixed. On LIBERO-PRO, AgenticRoboRL raises the success rate of a 9B-parameter planner from 18.1% to 71.0% without external memory, approaching the 72.1% achieved by Codex (GPT-5.5) with external memory. These results demonstrate post-training as an effective approach for improving robot planners. We will release the framework and trained planner checkpoints.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.28589
- Authors: Xinxin Liu, Bingxin Xu, Wenrui Bao, Ming Li, Wentao Bao, Chen Chen, Yuzhang Shang
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
