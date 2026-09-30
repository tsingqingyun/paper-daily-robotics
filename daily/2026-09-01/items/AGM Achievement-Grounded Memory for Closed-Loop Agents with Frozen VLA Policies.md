---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29537v1"
published: "2026-08-30T03:50:49Z"
age_days: 2
score: 49
created: 2026-09-01
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies

> [!summary] 先说人话（基于摘要）
> AGM 给冻结 VLA 加上一套“执行—验证—推进”的闭环记忆：只有物理证据确认当前子目标完成，进度指针才前移，避免把失败动作误记成成功。

## 问题

冻结 VLA 通常开环执行动作块，无法可靠判断该继续、重试还是结束。普通外部记忆若把“尝试过”当成“已完成”，会把一次局部执行错误固化为持续的任务状态错误。

## 创新点或方法

输入包括任务子目标序列、机器人本体交互信号和跨视角视觉观测，输出是是否确认子目标完成及是否推进进度。AGM 用本体信号决定何时验证，再以连贯点跟踪、语言条件跨视角比较和一个 2.43M 参数验证头判断实际成就；与旧做法的差别是记忆更新由证据门控，VLA 全程冻结且测试时不用大模型推理。

## 证据

摘要称其在 RoboMME Counting 的 PickXTimes、BinFill 及实体机器人上取得决定性提升，并平均超过最强记忆增强基线；但关键成功率和领先点数在摘要文本中缺失，无法核查具体幅度。


## 局限

摘要中的核心基准数字缺失，最需核查验证器在遮挡、误触发和物理状态难以从视觉确认时的可靠性。

- **判断**：值得精读方法与验证协议：贡献不在更大记忆，而在把记忆写入变成可审计的物理证据决策。

## 研究关联

对 VLA 和机器人学习研究者，这是无需重训主策略即可补上任务进度管理的轻量方案；对具身评测，也提示应区分动作发出、物理完成和记忆更新三个环节。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：49
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/AGM Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or terminate. External memory is a natural remedy, yet it can be harmful when attempted actions are treated as completed progress, turning local execution errors into persistent task-state errors. We propose Achievement-Grounded Memory (AGM), a lightweight closed-loop framework for frozen VLA policies that represents a task as a subgoal sequence with a progress pointer and advances this memory only after the current subgoal is verified by physical evidence. Proprioceptive interaction cues decide when to verify, while coherent point tracking and language-conditioned cross-view comparison, sourced from frozen foundation models through a single 2.43M-parameter verification head, decide what was achieved. AGM thereby converts open-loop execution into a closed loop of execution, verification, and progress, keeping the policy frozen without test-time large-model inference. On the RoboMME Counting benchmark, AGM reaches on PickXTimes and on BinFill, surpassing the strongest memory-augmented baseline by points on average, and the framework yields equally decisive gains on a physical robot. Reliable embodied memory thus depends more on disciplined state updates than on memory capacity.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29537v1
- Authors: Hongbo Gao, Zeyu Ni, Xin Wen, Siyu Xu, Ruifeng Li
- Published: 2026-08-30T03:50:49Z
- Age days: 2

</details>
