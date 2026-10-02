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
url: "https://arxiv.org/abs/2606.00773"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-02
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> SafeVLA-Bench 检查机器人是否在完成任务的途中用力过大、碰乱旁边物品或发生自身接触。它把安全要求写成可沿轨迹检查的规则，让“任务成功但过程不安全”单独显现出来。

## 问题

任务是评估桌面和厨房操作策略。原有二元成功指标只问目标是否达成，无法区分平稳完成和一路碰撞后完成；因此，高成功率可能掩盖接触过大、持物不稳等问题。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放到架子上”及执行轨迹；评测器同时检查杯子是否到位、途中是否撞动旁边盘子；输出可以是“成功，但违反旁物保护规则”，并附违规深度。

## 创新点或方法

旧做法检查最终任务结果；本文额外根据任务设置安全规则，检查整段执行，并计算越界深度。这是接在现有仿真基准后的评测工具，核心用途不要求重新训练策略。策略执行时保留原有控制方式，评估时读取轨迹所需信号；摘要另提到训练后改进案例，但未说明优化方法。

### 方法如何工作

1. 根据任务选择安全条款，确定执行过程中哪些状态不应出现，避免用一套规则硬套全部操作。
2. 把条款写成 STL 不变式，对轨迹计算满足或违反的裕量，使检查不止得到一个布尔结果。
3. 将规则结果与原生成功判定结合，分别报告安全率、成功但不安全率和违规严重度，揭示成功率隐藏的差异。

### 必要术语

- STL 不变式：用带时间含义的逻辑表达必须持续满足的条件；本文用它编码安全要求。
- 定量鲁棒度：规则距离被违反还有多少裕量，或已经越界多深；本文据此量化安全边界。
- SBU：任务成功却不安全的比例；具体统计分母需要核查。
- VSI：有上下界的最严重违规深度分数；用于补充“是否违规”，不等同于现实损害程度。

## 证据

摘要报告在 LIBERO 和 RoboCasa-365 上评估了 27 个策略—基准条目。15 个桌面策略的平均成功率超过 90%，仍有 18–28% 的回合不安全；RoboCasa-365 中，38–56% 的成功轨迹违反至少一条启用的规则。两组比例的分母不同，不能直接比较。这支持仿真中成功与安全存在缺口；摘要未给出策略名单、规则阈值及训练后改进幅度。

## 局限

当前证据来自仿真，尚不能据此判断真机事故率。我会核查规则阈值是否合理、接触信号是否可信，以及不同任务启用哪些规则；这些会直接决定“不安全”的含义，输入没有提供答案。

- **判断**：值得读到规则定义和指标计算细节，因为它最可复用的贡献是把执行过程中的风险变成可检查的评测对象。

## 研究关联

可借鉴的是先定义任务允许怎样完成，再评价是否完成。只要仿真能提供相关接触和状态信号，就能在保持原成功指标的同时，发现单看终点漏掉的行为。

### 下一步读哪里

先核查每类安全要求使用什么信号、阈值如何设定，再看 SBU 的分母和 VSI 的归一化方式；最后检查训练后改进是否牺牲成功率。输入没有正文节选可定位。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/SafeVLA-Bench A Benchmark for the Success-Safety Gap in Vision-Language-Action M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.00773v2 Announce Type: replace Abstract: Vision-language-action (VLA) benchmarks measure whether a policy completes a requested manipulation task, but binary success can hide safety violations along the trajectory: a policy may reach the goal while applying excessive contact, disturbing bystander objects, destabilizing a held object, or entering robot self-contact. We present SafeVLA-Bench, a post-hoc safety-evaluation framework for existing simulator-based VLA benchmarks that reveals violations missed by success-only evaluation. It encodes task-aware safety requirements as Signal Temporal Logic (STL) invariants with quantitative robustness semantics. Alongside native success, it reports the safety rate and the success-but-unsafe rate (SBU) used in prior safety evaluations, and introduces the Violation Severity Index (VSI), a bounded worst-violation depth score. We instantiate SafeVLA-Bench on LIBERO and RoboCasa-365, evaluating twenty-seven policy-benchmark entries across tabletop and kitchen manipulation tasks. High task success does not imply safe execution: the fifteen tabletop policies above 90% mean success still have 18-28% unsafe-episode rates, and 38-56% of successful RoboCasa-365 rollouts violate at least one active safety clause. A post-training case study further shows that SafeVLA-Bench can be used to improve policy safety. Project page: https://safevla.org

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.00773
- Authors: Jialiang Fan, Weizhe Xu, Zijun Wang, Fanxin Kong, Oleg Sokolsky, Insup Lee
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
