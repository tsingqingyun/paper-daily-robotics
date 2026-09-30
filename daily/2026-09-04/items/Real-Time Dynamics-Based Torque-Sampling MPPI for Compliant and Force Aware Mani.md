---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02020"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-09-04
concepts: ["世界模型", "具身智能评测与基准"]
---

# Real-Time Dynamics-Based Torque-Sampling MPPI for Compliant and Force Aware Manipulation

> [!summary] 先说人话（基于摘要）
> 该控制器把刚体动力学和安全约束直接放进实时MPPI，并在关节力矩空间并行采样，实现兼顾运动、接触力与柔顺性的机械臂控制。

## 问题

非结构环境中的物理交互同时要求准确运动、受控接触力和安全柔顺性，而非线性刚体动力学使传统MPC难以在实时频率内求解。

## 创新点或方法

框架在任务空间目标下显式滚动刚体动力学并约束安全条件，MPPI通过采样处理非线性；控制架构直接采样关节力矩，并用GPU并行评估候选控制序列。输出为7自由度机械臂实时力矩控制，区别于忽略动力学或难实时求解的常规MPC。

## 证据

求解器更新频率超过166 Hz，预测时域为0.18秒；在真实7自由度机械臂上验证了性能。摘要未给出任务成功率、力控误差或基线比较数字。


## 局限

除频率和时域外，摘要未量化安全约束违例、接触力误差和相对传统控制器的收益，实时性背后的任务复杂度也需查全文。

- **判断**：做接触丰富操作和采样MPC者值得精读实现；若关注高层具身智能，可重点确认它能否作为稳定的底层执行器。

## 研究关联

对机器人控制和接触操作研究者，它提供了可与学习策略或世界模型上层规划结合的高速、安全、力感知底层控制器；对纯VLA研究的价值主要是执行层接口。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/Real-Time Dynamics-Based Torque-Sampling MPPI for Compliant and Force Aware Mani.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02020v1 Announce Type: new Abstract: This study proposes a novel Model Predictive Path Integral (MPPI)-based task-space control framework. The proposed framework explicitly solves rigid-body dynamics within a real-time MPC formulation and enforces safety constraints, enabling accurate motion and force control that yields compliant behaviors for safe and effective physical interaction of robotic manipulators in unstructured environments. By leveraging MPPI, the proposed framework efficiently handles nonlinear dynamics that are difficult to solve with conventional MPC approaches in real-time. Furthermore, we develop a torque-sampling-based control architecture that enables efficient exploitation of GPU-based parallelization, resulting in effective compliant and force-aware behaviors. As a result, the proposed framework achieves a solver update rate of over 166 Hz with a 0.18 s prediction horizon, and its performance is validated through real-world experiments on a 7-DoF manipulator.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02020
- Authors: Euncheol Im, Taehyun Kim, Yonghwan Oh, Myotaeg Lim, Yisoo Lee
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
