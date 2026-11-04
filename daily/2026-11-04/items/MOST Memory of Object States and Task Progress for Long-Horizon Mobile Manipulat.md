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
url: "https://arxiv.org/abs/2611.00734"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 39
created: 2026-11-04
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# MOST: Memory of Object States and Task Progress for Long-Horizon Mobile Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> MOST 让机器人记住“东西变成了什么状态、任务做到哪一步”，而不只是保留过去看过的画面。它用物体状态和子任务进度监督内部记忆，再直接用这份记忆生成动作，帮助机器人处理已经离开视野的信息。

## 问题

长时移动操作中，机器人可能改动物体后走开，但后续仍要知道物体的新状态和已完成步骤。递归更新、测试时训练或检索历史观察能延长上下文，却仍可能要求策略从冗长、重复、视角变化的画面里重新推断任务状态。

### 用一个例子理解

理解用例（非论文实验）：输入“收好餐具再擦台面”和当前画面；杯子放入柜中后离开视野，记忆保留其位置与收纳进度，机器人随后继续处理剩余餐具，而不是重新寻找杯子。

## 创新点或方法

旧做法主要增加历史信息；MOST 改为明确规定记忆该保留什么。它把多视角观察压缩成时间 token，用物体状态和子任务进度监督历史 token 与预测未来的 token。训练时，这些监督让记忆围绕状态变化和进度组织；执行时，记忆在同一个端到端策略内部直接影响动作，无需外部规划器或检索。摘要未说明监督标签如何获得，以及未来 token 的预测跨度。

### 方法如何工作

1. 接收多视角观察并压缩成时间 token，减少后续策略需要处理的原始视觉历史。
2. 用物体状态和子任务进度监督历史与未来 token，让压缩后的信息保留任务相关变化。
3. 将内部记忆直接用于动作生成，使当前看不见但仍影响任务的信息参与决策。
4. 随着任务继续处理新观察；具体记忆更新、淘汰与预测规则摘要只说明到此。

### 必要术语

- 时间 token：承载时序信息的一组表示；本文用它压缩观察历史。
- 物体状态：物体当前的位置或其他任务相关属性；本文用它监督记忆内容。
- 子任务进度：较小步骤已完成到什么程度；本文用它帮助策略区分已做与待做事项。

## 证据

摘要报告，相比 XR-1，MOST 在 RoboCasa365 的平均成功率由 65.9% 升至 72.1%，在 RoboCasa-Long 的平均最大任务进度由 20.83% 升至 42.22%，真机成功率由 6.66% 升至 43.33%。RoboCasa-Long 面向持续数分钟、包含多个阶段的移动操作。它还胜过匹配的视觉历史记忆变体，支持记忆内容比单纯保留经历更关键；但摘要未给该对照数值、匹配条件、试验次数或误差范围。

## 局限

最大任务进度提高不等于完整任务成功率提高同样幅度。真机结果也需结合任务数量与重复次数判断；这些信息未在摘要中提供。未来 token 是否帮助规划、还是主要改善表示，仍需单独消融核查。

- **判断**：值得深入记忆监督和匹配对照，因为它把“记得更多”转成了可检验的“记住决策需要的变化”。

## 研究关联

具体启示是把记忆当作需要学习的任务状态表示：当后续决策依赖不可见的历史变化时，监督“发生了什么、完成了什么”可能比继续堆画面更有效。前提是训练中能可靠获得这些状态和进度信息。

### 下一步读哪里

重点查状态与进度标签的构造、历史和未来 token 的更新规则，以及视觉历史对照是否匹配容量与训练预算；真机部分核查任务定义和重复试验。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/MOST Memory of Object States and Task Progress for Long-Horizon Mobile Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2611.00734v1 Announce Type: new Abstract: Long-horizon embodied manipulation requires policies to act on information that is no longer visible. Modified objects may leave the field of view, while completed subtasks continue to constrain future actions. Existing approaches extend temporal context through recurrent state updates, test-time training, or storage and retrieval of past observations. As horizons grow, these mechanisms can still leave the policy to infer task state from long, redundant, and viewpoint-dependent visual experience. We argue that long-horizon agents benefit not merely from remembering more, but from remembering task-relevant state changes and progress. We propose Memory of Object States and Task Progress (MOST), a policy-internal memory framework that compresses multi-view observations into temporal tokens. Historical and predictive future tokens are explicitly supervised with object states and subtask progress, structuring memory around what has changed in the world and what has already been accomplished. The resulting memory directly conditions action generation within a single end-to-end policy, without an external planner or retrieval stage. We further introduce RoboCasa-Long, a benchmark of multi-minute, multi-stage mobile manipulation tasks. Across RoboCasa365, RoboCasa-Long, and real-world robot experiments, MOST consistently outperforms Xiaomi-Robotics-1 (XR-1), the previous state-of-the-art model. It raises average success from 65.9% to 72.1% on RoboCasa365, average maximum task progress from 20.83% to 42.22% on RoboCasa-Long, and real-world success from 6.66% to 43.33%. MOST also outperforms a matched visual-history memory variant, showing that effective long-horizon memory depends not only on how much experience is retained, but on whether it preserves decision-relevant progress and world-state changes.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.00734
- Authors: Diqi He, Jinbang Guo, Yijun Shen, Zhiwei Yu, Huan Yang, Dingwen Zhang, Junwei Han, Zhongyuan Wang
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
