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
url: "https://arxiv.org/abs/2610.20968v1"
published: "2026-10-14T21:43:14Z"
age_days: 3
score: 28
created: 2026-10-18
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# SOMA: Stack-of-Objects Manipulation using a Quadruped Robot

> [!summary] 这篇论文到底做了什么（基于摘要）
> SOMA 让没有机械臂的四足机器人用身体推动堆叠物体，并在移动时尽量避免上层滑落或倾倒。关键是把机身高度也交给策略控制，让机器人能够改变接触位置和用力姿态。

## 问题

任务是把单个物体或多层堆叠推到指定位置与朝向。难点不只是推得动：下层受到推动时，上层也必须稳定地跟随。摘要指出，传统方法局限于平面推动，无法充分利用机身升降来调整接触和身体姿态；重载推动还同时考验腿部支撑、抓地和整机平衡。

### 用一个例子理解

理解用例（非论文实验）：输入是两只叠放箱子的当前状态与目标位姿；高层根据运动历史调整推动命令和机身高度，低层调整腿部支撑；输出连续动作，使整叠箱子移动并转向，同时维持上层稳定。

## 创新点或方法

旧做法主要决定在平面上怎样推；SOMA 增加明确的机身高度控制，并把决策分成两层。高层读取时间历史，决定有边界的目标跟踪命令；低层调整腿部站姿来执行。高层使用 S5 编码历史，并用 Beta 分布表示受限命令，适合处理不能任意增大的控制量。训练采用分层强化学习；执行时两层共同驱动机器人。具体观测、奖励、两层训练顺序及命令各维含义，摘要未说明。

### 方法如何工作

1. 把机器人与堆叠物体的时间历史交给 S5，形成高层决策依据，以利用单帧无法表达的运动变化。
2. 高层通过 Beta 分布产生有边界的目标跟踪命令，并纳入机身高度控制，使推动能改变接触姿态。
3. 低层根据命令调整腿部站姿并执行运动，为推动提供支撑与平衡。
4. 机器人持续操纵堆叠，使其接近目标并抑制层间滑动或倾倒；具体反馈与奖励设计，摘要只说明到此。

### 必要术语

- 非抓取操纵：通过推等接触改变物体状态；本文用它让没有机械臂的四足机器人搬动物体。
- 分层强化学习：把较慢的任务决策和具体运动控制分开学习；本文分别负责推动命令与腿部执行。
- S5：处理序列历史的模型；本文用它为高层提供时间信息。
- 零样本仿真到现实迁移：仿真训练后直接用于实机；摘要据此描述 Go1 验证。

## 证据

摘要报告，仿真中单物体位姿调整成功率为 90.3%，动态双箱堆叠最高为 90.1%，对应严格误差要求：位置 0.05 米、朝向 1 度。实机使用 Unitree Go1，进行了不同载荷质量和形状下的零样本迁移，展示主动调整机身高度。摘要未给基线成绩、试验次数及实机成功率，因此支持仿真可行性与实机迁移展示，尚不能量化其相对优势或实机可靠性。

## 局限

仿真的高成功率不能直接套到真实重载任务。我的待核查问题是：高度控制本身贡献多少，载荷摩擦和重心变化多大时上层仍能稳定；现有输入不足以回答。

- **判断**：值得读方法与高度控制消融，因为最有启发的部分是如何把行走姿态变成推动堆叠的控制手段。

## 研究关联

值得借鉴的是把身体姿态当作操纵变量：接触任务受阻时，问题可能不在移动方向，而在接触高度和支撑方式。如果平台能改变身体高度，这个思路尤其值得检查。

### 下一步读哪里

先查高层到底控制哪些量，以及低层如何接收高度要求；再查是否有固定高度、去掉历史编码的对照。实机部分应核查载荷范围、失败类型和堆叠稳定性的判定。

- **概念**：智能体 Agent 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/SOMA Stack-of-Objects Manipulation using a Quadruped Robot.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Executing heavy-duty physical manipulation in unpredictable environments remains a major challenge for quadrupedal robots lacking dedicated manipulators. This paper presents SOMA, a hierarchical reinforcement learning framework for whole-body non-prehensile manipulation of multi-object stacks using a quadruped robot. Unlike traditional methods restricted to two-dimensional planar pushing, SOMA integrates explicit robot base-height control, unlocking full three-dimensional pushing strategies. This capability enables the quadruped to manipulate complex payload stacks as a unified system while preventing relative sliding or tipping of upper layers. The architecture factorizes control into a high-level manipulation policy using a Simplified Structured State Space Sequence (S5) encoder to reason over long-horizon temporal history and predict bounded target tracking commands via Beta distributions, and a low-level locomotion policy that dynamically adapts leg stance configurations. In extensive simulation benchmarks, SOMA achieves a $90.3\%$ success rate for single-object reposing and up to $90.1\%$ for dynamic two-box stacks under stringent error margins ($0.05\text{ m}$ position error, $1^\circ$ orientation error). Finally, we validate zero-shot sim-to-real transfer on a Unitree Go1 quadruped robot across diverse payload masses and geometries, demonstrating active base-height adjustments to maintain traction and balance during heavy pushing tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.20968v1
- Authors: Stergios E. Bachoumas, Panagiotis Artemiadis
- Published: 2026-10-14T21:43:14Z
- Age days: 3

</details>
