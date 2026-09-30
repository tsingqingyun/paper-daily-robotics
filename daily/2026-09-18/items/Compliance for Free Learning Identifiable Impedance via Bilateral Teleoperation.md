---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19976v1"
published: "2026-09-17T09:49:26Z"
age_days: 0
score: 28
created: 2026-09-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation

> [!summary] 先说人话（基于摘要）
> Compliance for Free让VLA不仅输出“移到哪里”，还输出“有多硬、如何顺应接触”。它用双边遥操作额外测得操作者期望的平衡位置，从而估计各方向刚度。

## 问题

接触任务需要顺应性监督，但仅凭实际位姿和测得的力，无法区分操作者想停在哪里与想施加多大刚度。已有策略依赖人工任务结构、特权仿真状态或专用力触觉设备。

## 创新点或方法

四通道双边遥操作把主臂作为期望平衡位置的独立测量，结合机械臂已有的关节力矩传感，通过回归获得逐时刻、分方向刚度标签，再微调VLA联合输出位姿与刚度。

## 证据

在Franka Research 3擦拭任务中，五种策略里只有该策略随“正常擦拭”到“用力擦拭”的指令改变接触力：RMS从6.4 N升至9.1 N，Cohen's d=0.89，p=0.023。

## 局限

输入摘要在统计结果处截断；“零标注成本”依赖双边遥操作与已有力矩感知条件，不能理解为零设备或采集成本。

- **判断**：值得优先读可辨识性推导和数据采集实现，但现有摘要只支持单项擦拭任务中的指令敏感性结论。

## 研究关联

对VLA与接触丰富的机器人学习，价值在于明确顺应性标签的可辨识条件，让语言指令有机会控制运动之外的接触行为；世界模型并非摘要核心。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Compliance for Free Learning Identifiable Impedance via Bilateral Teleoperation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action models tell a robot where to move, but not how hard to push. Contact-rich tasks depend on that second quantity, compliance, yet no widely used demonstration interface records it. The obstacle is identifiability as realized pose and measured force cannot separate the operator's intended equilibrium from their stiffness, so VR controllers, SpaceMouse and handheld grippers cannot supply compliance supervision even in principle. Prior compliance-output policies work around this with hand-specified task structure, privileged simulation contact state, or dedicated force and tactile hardware. Four-channel bilateral teleoperation removes the ambiguity directly by using the leader arm as a separate measurement of the intended equilibrium, making per-axis stiffness identifiable by regression using only the joint-torque sensing already on the manipulator. This yields per-timestep, direction-dependent compliance labels at zero annotation cost, which we use to fine-tune a VLA to emit stiffness alongside pose. On a Franka Research 3 wiping task, ours is the only policy of five whose contact force changes when the instruction asks for a firm wipe rather than a normal one (6.4N (normal) to 9.1N (firm) RMS, Cohen's d = 0.89, p = 0.023

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19976v1
- Authors: Harsha Guda, Adrià Colomé, Carme Torras
- Published: 2026-09-17T09:49:26Z
- Age days: 0

</details>
