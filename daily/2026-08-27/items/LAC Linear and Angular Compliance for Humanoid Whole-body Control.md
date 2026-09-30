---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.25405v1"
published: "2026-08-26T06:07:28Z"
age_days: 1
score: 29
created: 2026-08-27
concepts: ["世界模型", "机器人学习"]
---

# LAC: Linear and Angular Compliance for Humanoid Whole-body Control

> [!summary] 先说人话（基于摘要）
> LAC 学习一个可接受上身外力和力偶、同时响应线性与角向刚度指令的全身人形控制器，使机器人能被动让步又保持整体运动。

## 这篇到底在做什么

- **卡在哪里**：现实人形任务需要与人和物体接触，但现有控制器常把外力当扰动抵消，或只让少数身体链节顺应并忽略角向效应，无法形成全身一致响应。
- **关键解法**：先从人类交互数据提取接触框架，采样力与力偶事件；外力及被动运动链产生的虚拟力矩驱动指定刚度下的虚拟导纳，合成大规模顺应运动。随后用教师—学生强化学习训练单策略跟踪这些运动和外部wrench。
- **拿什么证明**：摘要称仿真与真机展示了上身多位置wrench下的全身顺应、线性和角向刚度全范围单调调节，以及遥操作移动操作适用性；未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：它补足具身智能落地中的接触安全与物理交互控制，可作为遥操作、模仿学习或高层VLA之下的顺应控制层。与世界模型的直接关联不明显。
- **先别急着信**：摘要缺少稳定性、安全边界和跟踪误差数字；合成接触分布能否覆盖真实突发接触是最需核查的一点。
- **判断**：做人形全身接触控制者值得精读；高层VLA研究者主要关注它能否作为可靠底层执行器。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/LAC Linear and Angular Compliance for Humanoid Whole-body Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world humanoid tasks involve physical interaction with objects and humans, yet current controllers either reject external forces as disturbances or restrict compliance to limited body links while ignoring angular effects. We present LAC, a general whole-body controller that simultaneously realizes commanded Linear and Angular Compliance for wrenches applied to the upper body. First, we synthesize whole-body compliant responses into a large-scale augmented dataset. Sampled force and couple events are imposed on contact frames extracted from human interaction data. At each contact link, the external force and a virtual torque from the passively yielding kinematic chain drive a virtual admittance under the commanded stiffness. Subsequently, teacher-student reinforcement learning trains a single policy to track the compliant motions under external wrenches. Finally, extensive simulation and real-world experiments demonstrate whole-body compliant responses to wrenches across the upper body, monotonic modulation over the full range of both stiffness commands, and applicability to teleoperated loco-manipulation tasks. Project website: https://lac-humanoid.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.25405v1
- Authors: Yang Liu, Zhongkai Gu, Wei Zhu, Mitsuhiro Hayashibe
- Published: 2026-08-26T06:07:28Z
- Age days: 1

</details>
