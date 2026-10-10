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
url: "https://arxiv.org/abs/2610.12185v1"
published: "2026-10-08T15:49:03Z"
age_days: 1
score: 34
created: 2026-10-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control

> [!summary] 这篇论文到底做了什么（基于摘要）
> RESETTLE 在基础策略的两次动作建议持续不一致时介入，检索同任务示范并执行一次纠偏，然后把控制交回原策略。它用轻量恢复避免反复语言推理或在线轨迹优化带来的干预延迟。

## 问题

任务是机器人操作出错或开始偏离时及时恢复进展。已有恢复方法可能反复调用视觉语言推理，或迭代优化动作轨迹，计算结束时偏差已经扩大。RESETTLE 处理的是冻结策略执行接口上的恢复，不需要改造整个基础策略。

### 用一个例子理解

理解用例（非论文实验）：输入是夹爪偏离抽屉把手后的观测；基础策略连续给出相互冲突的移动建议，系统检索同任务参考状态，执行一次向把手靠近的纠偏；输出后由原策略继续拉抽屉。

## 创新点或方法

旧方法在恢复时重新推理或规划；本文先在相同条件下独立采样两份动作建议，持续分歧才触发干预。它用适配后的 V-JEPA 编码器检索同任务示范，再结合状态伺服先验与受保护的视觉残差，输出一个纠偏动作并交回控制。基础策略冻结；编码器适配、残差学习和保护规则的训练细节，摘要未说明。推理阶段不做在线轨迹优化，也不追加视觉语言推理。

### 方法如何工作

1. 在相同观测条件下采样两份动作建议，持续比较它们，筛出可能需要干预的时刻。
2. 触发后检索同任务示范，得到可用于纠偏的参考状态。
3. 组合状态伺服先验与受保护视觉残差，生成一次纠偏动作，避免在线迭代规划。
4. 执行纠偏并交回基础策略，使局部恢复接回原有任务流程。

### 必要术语

- 动作分歧：同条件下两次动作建议不一致；本文用其持续出现触发恢复。
- 状态伺服：根据当前状态与参考状态的差异做纠正；提供纠偏动作的先验。
- 视觉残差：依据视觉补充的修正量；本文对其加入保护，但摘要未说明规则。

## 证据

摘要报告，六个基础策略的仿真测试中，LIBERO-Plus、Meta-World、RoboCasa Tabletop 的绝对成功率增益最高分别为 8.70、6.28、6.83 个百分点；另有两种策略、四项真机任务改善。QwenPI 对比中，监测与恢复计算延迟比 VoLoAgent 抓取、放置工具调用的监测与规划低 74.04%—93.57%。Harness VLA 的 LIBERO-Pro Swap 成功率由 42% 到 50%。最高增益不是平均收益，计算延迟也不是完整任务耗时。

## 局限

动作分歧可能来自多个同样可行的选择，也可能漏掉两次一致的错误。摘要结果没有证明分歧是错误的因果指标。我会核查误触发、漏触发，以及纠偏动作遇到接触约束时的边界；真机改善也不能直接推广到任意任务。

- **判断**：值得读到触发规则和纠偏控制细节：它给出了可接入现有策略的具体办法，但可靠性取决于分歧信号与单步纠正是否匹配。

## 研究关联

值得借鉴的是把恢复拆成“何时介入”和“一次介入做什么”，用已有策略自身的分歧作为触发信号。若偏差可通过短动作纠正，这种局部干预可能比每次重规划更合适。

### 下一步读哪里

核查持续分歧的度量与阈值、同任务示范的可用条件、视觉残差的保护机制。重点看触发准确性、各策略完整结果，以及延迟是否包含采样、检索和机器人实际执行。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/RESETTLE Robotic Recovery through Disagreement-Triggered Retrieval and Efficient.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE(Robotic rEcovery through diSagrEement-Triggered reTrievaL and Efficient Corrective Control), a model-agnostic framework that provides computationally efficient recovery at the action-execution interface of frozen robot policies. RESETTLE triggers recovery when two action proposals independently sampled under identical conditioning persistently disagree. It retrieves a same-task demonstration reference using an adapted V-JEPA encoder and combines a state-servo prior with a guarded visual residual to execute one corrective action without online trajectory optimization or additional vision-language reasoning, then returns control to the base policy. Across six base policies in simulation, RESETTLE achieves up to 8.70%, 6.28%, and 6.83% absolute success-rate gains on LIBERO-Plus, Meta-World, and RoboCasa Tabletop, respectively, with further improvements on four real-world tasks using two policies. In QwenPI-based comparisons, its monitoring-and-recovery computation latency is 74.04%--93.57% lower than VoLoAgent's monitoring-and-planning latency for grasp and place tool calls. It also raises Harness VLA's LIBERO-Pro Swap success from 42% to 50%, demonstrating compatibility with high-level agentic planning. Code available at: https://github.com/JIA-Lab-research/RESETTLE

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12185v1
- Authors: Yuxin Chen, Senqiao Yang, Zixuan Wang, Jinhui Ye, Changsheng Lu, Pengguang Chen, Shu Liu, Zhuotao Tian, Jiaya Jia
- Published: 2026-10-08T15:49:03Z
- Age days: 1

</details>
