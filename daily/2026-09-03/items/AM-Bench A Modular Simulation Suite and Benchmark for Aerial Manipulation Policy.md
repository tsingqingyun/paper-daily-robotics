---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00641v1"
published: "2026-09-01T03:20:24Z"
age_days: 2
score: 28
created: 2026-09-03
concepts: ["世界模型", "具身智能评测与基准"]
---

# AM-Bench: A Modular Simulation Suite and Benchmark for Aerial Manipulation Policy Learning

> [!summary] 先说人话（基于摘要）
> AM-Bench 为多旋翼空中操作提供模块化仿真与基准，不只比较策略，还联合考察本体、底层控制、气动扰动和执行器饱和。它覆盖欠驱动、全驱动和过驱动系统及12项操作任务。

## 问题

地面机械臂基准忽略浮动基座、耦合动力学、自由度约束和环境扰动；在空中操作中，任务结果同时取决于本体、控制器与高层策略，单看端到端成功率难以诊断失败来源。

## 创新点或方法

套件提供多类多旋翼本体、接触／运输／受限交互任务、可配置扰动与饱和、标准底层控制器和策略学习基线，并通过组合实验拆解策略—控制接口—本体之间的相互作用。

## 证据

包含12项任务；摘要报告3组仿真研究，并进行了所建模效应的真实验证和学习管线硬件测试，但未给出可核查的性能数字。


## 局限

真实验证只被概括性提及，尚不清楚覆盖了多少任务、扰动和本体；仿真到真实的一致性是核心核查点。

- **判断**：空中操作研究者值得精读模块和诊断实验；对一般机器人学习者，它也是系统级基准设计的好案例。

## 研究关联

它为具身评测补足了动力学敏感的空中操作场景，可帮助研究者判断策略失败究竟源自学习、控制接口还是平台能力。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/AM-Bench A Modular Simulation Suite and Benchmark for Aerial Manipulation Policy.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Standardized benchmarks have played a central role in advancing robot manipulation learning, yet most focus on ground-supported manipulation systems, which limits their applicability to dynamics-critical domains such as aerial manipulation (AM). AM presents distinct system-level challenges, including environmental disturbances, coupled dynamics between the manipulator and floating base, and constrained degrees of freedom. Consequently, task performance depends jointly on robot embodiment, low-level control, and high-level policy design. We introduce AM-Bench, a modular simulation suite and benchmark for multirotor-based AM policy learning. AM-Bench includes representative embodiments spanning underactuated, fully actuated, and overactuated systems, 12 tasks across contact, transport, and constrained interaction, configurable aerodynamic disturbances and actuator saturation, standard low-level controllers, and baseline policy-learning algorithms. Unlike prior manipulation benchmarks that primarily emphasize end-to-end policy performance, AM-Bench enables system-level evaluation of how embodiment, control, disturbances, and policy choices interact. We demonstrate its diagnostic value through three simulation studies spanning high-level policies, policy--control interfaces, and embodiments, together with real-world validation of modeled effects and a hardware test of the learning pipeline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00641v1
- Authors: Yutong Wang, Dongjae Lee, Xiaofeng Guo, Yuanzhu Zhan, Yufei Jiang, Bavin Saravanan, Muqing Cao, Jia Xie, Chenyang Mao, Sebastian Scherer, Junyi Geng, Guanya Shi
- Published: 2026-09-01T03:20:24Z
- Age days: 2

</details>
