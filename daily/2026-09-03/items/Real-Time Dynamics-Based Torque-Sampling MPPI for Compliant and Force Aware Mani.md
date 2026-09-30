---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02020v1"
published: "2026-09-02T02:46:57Z"
age_days: 1
score: 27
created: 2026-09-03
concepts: ["世界模型", "具身智能评测与基准"]
---

# Real-Time Dynamics-Based Torque-Sampling MPPI for Compliant and Force Aware Manipulation

> [!summary] 先说人话（基于摘要）
> 该方法把刚体动力学直接放进实时 MPPI 任务空间控制器，并通过 torque sampling 在 GPU 上并行搜索，使机械臂同时实现运动、力控制与柔顺交互。安全约束在 MPC 求解中显式执行。

## 这篇到底在做什么

- **卡在哪里**：非结构化接触要求控制器处理强非线性动力学、力约束和安全边界；常规 MPC 难以实时求解，而缺少完整动力学或只采样运动指令的方法难以产生可靠柔顺行为。
- **关键解法**：控制器在预测时域内显式求解刚体动力学，以力矩为采样变量并利用 GPU 并行评估轨迹，同时在任务空间目标中结合运动和力控制及安全约束。
- **拿什么证明**：求解器更新频率超过166 Hz，预测时域0.18秒；在7自由度机械臂上完成真实实验验证。摘要未给成功率、跟踪误差或对比数字。

## 值不值得读

- **和你的研究有什么关系**：对接触丰富机器人控制，它展示了基于动力学的采样 MPC 可以达到实时频率，可作为学习策略之外的安全、柔顺低层执行器或混合系统组件。
- **先别急着信**：摘要只给频率，未量化控制精度、接触力、安全约束违反率及相对基线收益；“安全”效果需查实验定义。
- **判断**：做实时 MPC 或力控者值得精读并看实现细节；仅凭166 Hz还不能判断控制质量是否优于成熟基线。

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Real-Time Dynamics-Based Torque-Sampling MPPI for Compliant and Force Aware Mani.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This study proposes a novel Model Predictive Path Integral (MPPI)-based task-space control framework. The proposed framework explicitly solves rigid-body dynamics within a real-time MPC formulation and enforces safety constraints, enabling accurate motion and force control that yields compliant behaviors for safe and effective physical interaction of robotic manipulators in unstructured environments. By leveraging MPPI, the proposed framework efficiently handles nonlinear dynamics that are difficult to solve with conventional MPC approaches in real-time. Furthermore, we develop a torque-sampling-based control architecture that enables efficient exploitation of GPU-based parallelization, resulting in effective compliant and force-aware behaviors. As a result, the proposed framework achieves a solver update rate of over 166 Hz with a 0.18 s prediction horizon, and its performance is validated through real-world experiments on a 7-DoF manipulator.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02020v1
- Authors: Euncheol Im, Taehyun Kim, Yonghwan Oh, Myotaeg Lim, Yisoo Lee
- Published: 2026-09-02T02:46:57Z
- Age days: 1

</details>
