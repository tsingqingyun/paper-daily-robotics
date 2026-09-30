---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25630v1"
published: "2026-09-22T03:38:54Z"
age_days: 1
score: 30
created: 2026-09-24
concepts: ["机器人学习", "具身智能评测与基准"]
---

# PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning

> [!summary] 先说人话（基于摘要）
> PAKT 让人直接推着机器人示教时，也遵守策略执行时的运动约束，减少机器人学到自己复现不了的轨迹。配套控制栈把低频 RL 动作转成平滑的高频力矩控制。

## 问题

接触密集工业任务需要高精度、可靠性和短周期，但人工指导接口未必兼容机器人与策略的物理限制。直接拖动示教可能产生执行端无法复现的速度、加速度或 jerk。

## 创新点或方法

导纳控制将人施加的力转换为运动，下游参考生成器施加与策略执行一致的运动学限制；参考生成器与阻抗控制器再共同将低频动作映射成高频力矩命令，改善接触处理和平滑性。

## 证据

在四个插入与工业装配基准的报告运行中，包括数据中心计算托盘任务，相比 HIL-SERL，端到端系统将周期时间缩短 23%—48%，累计人工干预次数减少 62%—86%。

## 局限

微米精度和超过 99% 成功率在摘要中属于任务需求，并非已报告成绩；现有增益来自完整系统，需核查示教约束与控制栈各自的作用。

- **判断**：建议做工业在线 RL 的研究者优先精读，周期和干预指标直接对应实际训练与运行成本。

## 研究关联

对机器人学习研究者，它把示教质量明确关联到执行可复现性，也提供了人类指导与 RL 控制接口共同设计的实机证据。

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/PAKT Physically-Aligned Kinesthetic Teaching for Reinforcement Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world reinforcement learning (RL) systems still struggle with the demands of contact-rich industrial manipulation, including micrometer-level precision, success rates above 99%, and human-level cycle times. Although off-policy algorithms can improve performance by leveraging demonstrations and interventions, a key bottleneck is the lack of an intuitive interface for collecting such guidance while complying with constraints of the physical system and the policy. We propose PAKT, a framework for kinesthetic teaching in RL. As opposed to teleoperation approaches, PAKT relies on kinesthetic guidance, which is widely used in industry. However, a critical weakness of kinesthetic guidance is the possibility for the operator to move the robot along trajectories (e.g., velocities, accelerations, jerk) that the robot and/or policy cannot physically reproduce. Using PAKT, operators guide the robot through admittance control, which maps human-applied forces to motion. The downstream reference generator applies the same kinematic limits used during policy execution, keeping the collected trajectories within these limits. To support this teaching interface with an appropriate execution layer, PAKT adds a high-performance control stack that maps low-frequency RL actions to high-frequency torque commands. It consists of a reference generator and subsequent impedance controller, where the reference generator preserves the tracking performance of the impedance controller while improving contact handling and producing smoother policy actions. Across the reported runs on four insertion and industrial assembly benchmarks, including a data center compute tray, the end-to-end system reduces cycle time by 23%-48% and cumulative intervention count by 62%-86% relative to the HIL-SERL baseline. Project website: https://pakt-website.github.io/pakt-website}{https://pakt-website.github.io/pakt-website

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25630v1
- Authors: Lars Johannsmeier, Yashraj Narang
- Published: 2026-09-22T03:38:54Z
- Age days: 1

</details>
