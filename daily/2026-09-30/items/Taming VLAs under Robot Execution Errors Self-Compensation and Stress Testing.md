---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37334v1"
published: "2026-09-29T12:08:13Z"
age_days: 0
score: 31
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing

> [!summary] 先说人话（基于摘要）
> self-compensating VLA 根据指令动作与机器人实际运动的偏差，在线学习提前补偿执行误差。RoboStress 则系统模拟摩擦、间隙等机械问题，测试策略在不同执行条件下是否可靠。

## 问题

机器人磨损、载荷变化等因素会使实际运动偏离指令，VLA 因而失败。真实硬件难以系统覆盖多种机械状态，而已有训练期鲁棒性方法仍需面对具体部署偏差。

## 创新点或方法

部署时以命令与实际运动的残差更新策略，无需任务奖励或标签，使后续指令预先抵消执行误差。RoboStress 将摩擦、回程间隙、柔顺性和重力补偿误差组合成七种与状态及运动历史相关的场景。

## 证据

在 RoboStress 上，平均成功率高于基础策略和训练期鲁棒性方法。两台使用历史不同的实体机械臂上，平均任务成功率各提高超过 30 个百分点，收益还能延伸到示范中未见物体。

## 局限

需核查实际运动如何测量、残差如何驱动策略更新，以及在线补偿收敛过程中的行为；摘要没有给出适配速度。

- **判断**：本期实机 VLA 研究者应优先细读，两个机械臂均超过 30 个百分点的收益值得核查并尝试复现。

## 研究关联

对 VLA 部署和机器人学习，它将机械执行偏差变成可用于在线适配的监督信号，并补充视觉扰动之外的鲁棒性评测维度。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Taming VLAs under Robot Execution Errors Self-Compensation and Stress Testing.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies often fail when a robot's executed motion deviates from their commanded action. Such execution errors arise from the robot's mechanics and operating conditions, such as wear and payload changes. We propose self-compensating VLA, a deployment-time adaptation method that enables a VLA policy to pre-compensate for the robot's execution errors when generating commands. Without task rewards or labels, it updates the policy online using the residual between the action commanded by a VLA and the motion executed by the robot. To stress-test VLA robustness across execution conditions that are impractical to cover with physical robots alone, we introduce RoboStress, a controlled simulation benchmark. It combines established joint-level models of friction, backlash, compliance, and gravity-compensation error into seven deployment scenarios whose execution errors depend on the robot's state and motion history. On RoboStress, self-compensating VLA achieves higher average task success than both the base policies and methods that build in robustness during training. On two physical robot arms with different usage histories, it raises the average task success rate by more than 30 percentage points on each arm, and the gains extend to objects not seen in the task demonstrations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37334v1
- Authors: Sohyun Lee, Yoonjae Baek, Jaesang Won, Jinnyeong Kim, Kang Hyunwoo, Seung-Hwan Baek, Ivan Laptev, Suha Kwak
- Published: 2026-09-29T12:08:13Z
- Age days: 0

</details>
