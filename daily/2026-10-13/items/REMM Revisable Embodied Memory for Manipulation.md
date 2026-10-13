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
url: "https://arxiv.org/abs/2610.12710v1"
published: "2026-10-08T20:42:35Z"
age_days: 4
score: 29
created: 2026-10-13
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# REMM: Revisable Embodied Memory for Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> REMM 让机器人记住过去，也能撤销已经失效的“任务完成”判断。它把历史证据与当前任务状态分开，记录结论依赖哪些事实；事实变了，就撤回相关结论，并安排局部恢复。

## 问题

长程操作中，物体可能被移动，已完成的条件可能重新失效。只保存观察历史并不能告诉机器人哪些结论应撤销、哪些步骤需要补做；瓶颈是把历史变成仍受现实支持的任务状态。

### 用一个例子理解

理解用例（非论文实验）：机器人记下零件已放进托盘，随后看到零件被拿走；REMM 更新位置事实，撤销依赖它的完成条件，等当前技能结束后安排重新放置，再继续后续任务。

## 创新点或方法

REMM 为冻结的 G0.5 VLA 执行器增加监督记忆层。历史只追加，任务状态可修订，派生关系与完成条件显式连接到支撑事实。接受的新证据改变事实后，系统撤销依赖结论，并在经过验证的技能边界安排恢复。执行器不更新；证据接受与技能边界的具体判定，摘要未说明。

### 方法如何工作

1. 追加观察证据，保留判断的历史依据。
2. 由事实维护关系与完成条件，并记录依赖，使结论可以追溯。
3. 接受改变事实的新证据后，撤销依赖该事实的结论，找出需要修复的条件。
4. 在验证过的技能边界安排针对性恢复，由冻结执行器继续操作。

### 必要术语

- 证据历史：按时间保留的观察记录；本文不覆盖旧记录。
- 可修订任务状态：机器人当前认为成立的条件；可随新证据撤销。
- 技能边界：一个技能结束、适合切换任务的节点；本文在此调度恢复。

## 证据

摘要报告 51 次物理试验，包含操作员辅助运行。相较最强基线，干预恢复的平均记录任务进度从 57% 到 91%，序列回忆从 43% 到 70%。视频诊断还比较了兼容 π₀.₅ 的高层规划器改编方案。结果支持所测条件下的进度改善，但进度不是完整任务成功率，辅助运行也不能当作完全自主表现。

## 局限

摘要明确包含操作员辅助试验，因此自主系统贡献与人工支持需要分开看。我的待核查问题是：新证据判断错误会不会引起误撤销，以及恢复效果有多少来自记忆机制、多少依赖边界验证和操作员。

- **判断**：值得读状态修订规则和试验记录，因为它把长程记忆问题落到了可追踪的撤销与补做行为上。

## 研究关联

可借鉴的是把“曾经完成”和“现在仍然成立”分开。若任务条件会被后续事件破坏，显式保存证据依赖关系，可以让恢复针对失效条件，而不必重新执行整个流程。

### 下一步读哪里

我会先核查证据接受、依赖撤销和恢复调度规则，再看 51 次试验中自主与辅助运行的划分、任务进度定义，以及匹配执行器的基线设置。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/REMM Revisable Embodied Memory for Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon manipulation requires robots to retain task-relevant history while revising conclusions no longer supported by physical evidence. Retaining observations alone does not specify which completed conditions should be withdrawn after a disturbance or which obligations require repair. We introduce REMM, Revisable Embodied Memory for Manipulation, a supervisory memory layer for a frozen G0.5 vision-language-action executor. REMM separates an append-only evidence history from revisable task state and explicitly links derived relations and completed conditions to their supporting facts. When accepted evidence changes a supporting fact, it withdraws dependent conclusions and schedules targeted recovery at verified skill boundaries without updating the executor. Across 51 physical trials, including operator-assisted runs, REMM improves mean recorded task progress over the strongest baseline from 57% to 91% in intervention recovery and from 43% to 70% in sequence recall. Complementary video diagnostics show improved grounding of retained history into the next instruction, including comparisons with $π_{0.5}$-compatible high-level planner adaptations. These results support revisable memory as a practical interface for continued manipulation without policy retraining. Project: https://revanthsenthil.github.io/remm/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12710v1
- Authors: Revanth Krishna Senthilkumaran, Ruwan Wickramarachchi, Alessandro Oltramari, Jonathan Francis
- Published: 2026-10-08T20:42:35Z
- Age days: 4

</details>
