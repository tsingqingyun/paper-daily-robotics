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
url: "https://arxiv.org/abs/2608.16889"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-02
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory

> [!summary] 这篇论文到底做了什么（基于摘要）
> BATON 把长任务拆成可分别探索、记忆和复用的子任务，同时检查每一步留下的状态能否让下一步接手。它解决的不只是“这一招会不会”，还有“什么时候能用、用完后别人能不能继续”。

## 问题

长任务会累积误差，而且前一步可能以不利于后一步的方式完成。摘要讨论的既有方案冻结 VLA，让语言模型代理规划、用解析动作做自由空间移动，并只在接触操作时调用 VLA；但它依赖整任务测试时探索，失败难定位，也没有明确表示技能启动条件和跨步骤交接条件。

### 用一个例子理解

理解用例（非论文实验）：输入是“开盒、放入零件、合盖”；代理先检查腕部图像再调用开盒技能，并选取不会挡住放置路径的结束姿态；若盒盖位置妨碍放入，就先调整，再执行下一技能，最终输出完整动作序列。

## 创新点或方法

BATON 把探索单位从完整任务改成子任务，分别找到解法并存入记忆，再组合成长流程。它还管理三类转接：调用前由验证代理检查腕部视角，确认场景准备好；交接时修复前一步留下的不合适状态；选择策略时预看下一步，避免当前成功却堵住后续路径。这里主要改变测试时探索与记忆使用，沿用冻结 VLA 的路线；摘要未说明验证代理是否另行训练，也未交代记忆的具体格式。

### 方法如何工作

1. 把长任务分成子任务，各自在短流程中探索，使失败能定位到具体阶段。
2. 把得到的解法存入记忆，让后续组合复用已找到的行为。
3. 执行前检查腕部视图，只有满足准备条件才调用接触操作技能。
4. 交接时修复残留状态，并依据后续需求选择当前策略，使局部成功能够继续传递。

### 必要术语

- 冻结 VLA：保持动作模型参数不变；适应主要发生在外部规划和记忆层。
- 转接条件：一个技能能否启动、另一个技能能否接手的状态要求；这是 BATON 管理的核心。
- 前瞻转接：选当前做法时考虑下一步能否利用其结果；用于避免局部成功造成后续困难。

## 证据

摘要报告在 RoboMemArena 上，相比最优已有方法，任务成功指标提高 37.7%，累积成功指标提高 29.7%；未给出对比方法名称、指标定义、绝对值或百分比口径。作者还用每阶段需 T 次探索、共有 K 阶段的模型，说明成本从约 T^K 变为 KT。这是基于子任务可分别探索和复用的复杂度论述，不能直接当作测得的运行加速比。

## 局限

子任务若高度耦合，分别学到的解法未必能低成本组合；线性探索论述需要核查重置和交接修复的成本。摘要没有说明 RoboMemArena 结果属于仿真还是真机，也不足以判断三类转接分别贡献多少。

- **判断**：值得深入读转接条件与记忆实例：它直接解释了为什么单技能都能成功，长任务仍可能失败。

## 研究关联

最值得借鉴的是给技能增加启动条件和交接要求。组织多个现成策略时，可以先问“前一步结束后，下一步需要的姿态、位置和视野是否成立”，再决定是否追加整理动作，或改选前一步的执行方式。

### 下一步读哪里

优先核查子任务如何划分和重置，验证代理如何判定准备就绪，记忆怎样表达下一步要求。再找整任务探索与子任务探索的实际成本对比，以及三类转接的独立消融。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/Don't Drop the BATON Long-Horizon Robot Manipulation via Agentic Subtask Explora.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.16889v3 Announce Type: replace Abstract: Long-horizon robot manipulation chains many contact-rich skills into one multi-stage task. Vision-language-action (VLA) and world-action models (WAMs) increasingly master individual skills, yet the chain still fails: errors compound beyond the policy's ability to correct, and one subtask silently constrains the next. A promising pathway freezes the VLA and puts an LLM coding agent in charge: it plans in language, moves in free space with analytic primitives, invokes the VLA only for contact-rich segments, and writes adaptation into language memory. Yet applied to long horizons, this recipe breaks twice. (1) Its competence comes from whole-task exploration at test time, whose cost is exponential in the number of stages: if one stage needs T episodes, a K-stage task needs on the order of T^K, and a failure does not reveal which stage caused it. (2) It has no representation of transitions: the VLA primitive carries an exit but no entry condition, and a subtask can succeed in a form its successor cannot use. We present BATON to address both failures. Against (1), BATON makes the subtask the unit of exploration: each subtask is explored in the cheap short-horizon regime and its solution stored in memory; a long-horizon trajectory is then composed from these solutions rather than discovered whole. Exploration cost becomes linear (KT), and each failure is attributed to one stage. Against (2), BATON equips exploration with a transition-aware memory. Within a subtask, a verifier agent governs the invocation transition: the VLA is invoked only after the wrist view confirms the scene is ready. Across subtasks, a handoff transition restores an entry state disturbed by the predecessor's residue, and a lookahead transition selects the strategy whose outcome the successor can inherit. On the RoboMemArena benchmark, BATON improves task success by 37.7% and cumulative success by 29.7% over the SoTA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16889
- Authors: Bingxin Xu, Yuzhang Shang, Emilio Ferrara
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
