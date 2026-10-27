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
url: "https://arxiv.org/abs/2610.31162v1"
published: "2026-10-22T12:17:45Z"
age_days: 4
score: 29
created: 2026-10-27
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games

> [!summary] 这篇论文到底做了什么（基于摘要）
> HiSTEVE 用高层规划器安排 Minecraft 子任务，再让同一个 VLA 通过画面和键鼠执行。关键是让规划考虑底层实际能力，并利用底层策略上下文判断子任务是否可能完成，减少长任务中的执行脱节。

## 问题

任务是在程序生成的 Minecraft 世界中，像玩家一样通过原生界面完成长流程目标。现有智能体常只能做好原生视觉动作控制，缺少长程自主性；或能做高层规划，却依赖环境 API 和预定义技能执行。难点是把规划、可靠控制和进度判断连起来。

### 用一个例子理解

理解用例（非论文实验）：输入“做一把石镐”和当前游戏画面；规划器结合记忆安排收集木材、制作工具、获取石料等子任务；VLA 输出键鼠动作，检测器判断阶段是否可能完成，更新进度后继续，最终得到石镐或进入恢复流程。

## 创新点或方法

HiSTEVE 在高层加入结构化记忆和 VLM 规划器，跟踪进度并选择 VLA 能完成的子任务；完成检测器结合策略上下文发出候选完成信号。底层由单个 VLA 执行全部子任务，并用不同 RMSNorm 分支及独立鼠标移动嵌入减轻界面交互与其他操作的干扰。训练包括世界知识注入、模仿学习和环境反馈强化学习；推理时依靠视觉与原生键鼠控制。具体训练配比未说明。

### 方法如何工作

1. 用结构化记忆记录当前进度，为规划器提供持续的任务状态，避免每轮仅凭当前画面重新判断。
2. 规划器结合 VLA 能力选择子任务，使下一步计划落在执行器可处理的范围内。
3. 单个 VLA 根据画面生成键鼠操作，并用区分交互类型的内部处理减轻操作干扰。
4. 完成检测器结合策略上下文发出候选信号，供系统衔接下一阶段；信号确认与恢复规则摘要未说明。

### 必要术语

- 智能体运行支架：组织记忆、规划和执行的外围系统；本文用它协调长任务。
- 策略上下文：与底层策略执行有关的信息；本文用来辅助完成检测，具体内容未说明。
- RMSNorm 分支：分别归一化内部表示的处理路径；本文借此减轻不同交互类型之间的干扰。

## 证据

摘要报告 MineStudio Bench 得分为 85.0%，OpenHA 平均成功率为 37.4%，并称原子任务表现达到最优；还展示从零制作铁镐等长任务（摘要）。但未列比较对象、基准得分口径、试验次数和长任务重复成功率。因此能确认报告了短任务指标和长任务完成实例，不能把前者直接解释为长任务可靠性。

## 局限

我的待核查问题是能力信息如何获得、错误完成信号如何纠正，以及失败后恢复是否稳定。训练使用环境反馈，并不等于部署使用环境 API；摘要明确描述的是视觉与键鼠执行。这里的证据来自游戏，不能直接推为真机机器人的可靠性。

- **判断**：值得读系统执行流程和失败轨迹，尤其看能力约束与完成检测怎样影响长任务；只看最终制作铁镐的展示，难以判断各机制的必要性。

## 研究关联

可借鉴的是让规划器知道执行器的能力边界，并让完成判断参考执行上下文。高层指令写得合理还不够，系统还需要知道“这一步是否做得到”和“是否真的做完了”，才能维持后续计划。

### 下一步读哪里

先核查能力如何表示、候选完成信号如何确认，以及记忆更新规则。再查 GUI 分支的切换条件、训练阶段消融，以及长任务在不同世界中重复运行的成功率与失败原因。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/HiSTEVE 1.0 Harnessing Human-Interface VLA Agents for Open-World Games.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these capabilities. Existing agents typically provide either native visuomotor control without long-horizon autonomy or high-level planning executed through environment APIs or predefined skills. To bridge this gap, we propose HiSTEVE, a hierarchical VLA agent with a capability-aware agent harness. At the orchestration level, we equip the harness with structured memory for tracking progress and a VLM planner for selecting subtasks within the VLA's capabilities. To reliably determine subtask completion, we further introduce a policy-coupled task completion state detector that conditions on VLA policy context to signal candidate completion. At the control level, a single VLA executes all subtasks with vision-only perception and native keyboard-and-mouse actions. To mitigate interference between heterogeneous GUI and non-GUI interactions, we introduce regime-specific RMSNorm branches and separate mouse-movement token embeddings. We also train the VLA through world knowledge injection, imitation learning, and reinforcement learning with environment feedback to improve reliability and recovery. HiSTEVE achieves state-of-the-art atomic-task performance, scoring 85.0% on MineStudio Bench and a 37.4% average success rate on OpenHA, while also completing long-horizon tasks such as crafting an iron pickaxe from scratch like human players.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.31162v1
- Authors: Zecong Tang, Zian Guan, Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Bo Dai
- Published: 2026-10-22T12:17:45Z
- Age days: 4

</details>
