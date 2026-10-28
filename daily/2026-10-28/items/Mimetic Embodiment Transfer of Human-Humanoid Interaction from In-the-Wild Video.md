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
url: "https://arxiv.org/abs/2610.36615v1"
published: "2026-10-27T04:18:31Z"
age_days: 0
score: 32
created: 2026-10-28
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos

> [!summary] 这篇论文到底做了什么（基于摘要）
> 把两个人拥抱的视频变成“人与机器人拥抱”，不能只把一个人的关节角搬到机器人身上。HumiTransfer 优先保留双方的相对位置和接触关系，再修正平衡、碰撞等物理约束，让不同身材的机器人也能承接这段互动。

## 问题

任务是从野外人际互动视频中，保留一名人类参与者，把另一名替换为人形机器人。瓶颈在于机器人的肢体比例、关节数量和活动范围与人不同：单体动作相似，仍可能握不到手或发生穿插。摘要没有逐项描述已有基线，但明确指出，迁移必须同时顾及个体动作、双方关系和机器人运动学限制。

### 用一个例子理解

理解用例（非论文实验）：输入两人握手的视频和一个短臂机器人的身体模型；系统重建双方动作，调整机器人的肩肘姿态以保持握手关系，再检查平衡和碰撞；输出人与机器人之间的一段可执行候选动作。

## 创新点或方法

相对于只关注单体姿态的迁移思路，本文先重建脚与地面接触一致的三维人体动作，再用带权重的关节相对方向和解剖偏移，优先照顾互动关键关系；迁移后继续优化平衡、接触和避碰。巧处是允许局部姿态随身体变化，同时守住互动成立的条件。这是动作数据转换流程；摘要另称所得数据可训练互动动作生成方法，但未交代该模型的训练目标及在线输入。

### 方法如何工作

1. 从视频恢复两人的三维动作，并约束脚与地面的接触，为后续迁移提供稳定的空间参照。
2. 把其中一人的运动映射到机器人，利用加权相对方向和解剖偏移保留互动关键关系，适应身体差异。
3. 对迁移结果施加平衡、接触和避碰优化，减少姿态映射产生的物理问题。
4. 汇集结果形成 HumiMimic，并用于互动动作生成研究；摘要只说明到此，未给生成模型的具体训练过程。

### 必要术语

- 动作重定向：把一种身体上的动作改到另一种身体上；本文用它把人的运动转给机器人。
- 关节相对方向：关节之间的方向关系；本文对其加权，以优先保留互动关键关系。
- 自由度：机器人可独立变化的运动维度；不同自由度意味着可实现姿态的范围不同。

## 证据

摘要给出：处理了 1,200 段视频，形成约 500,000 帧 HumiMimic 数据，覆盖 26 自由度 Unitree R1 Edu 和 23 自由度 HighTorque Mini-hi。两种机器人上，动作保真、身体间关系和接触准确性优于现有基线，但未给基线名称、指标定义和数值。摘要还报告真机部署，支持部分迁移动作可执行；具体互动类别、次数和成功率未说明，不能据此认定所有数据都经过真机验证。

## 局限

我会核查接触目标如何从视频中确定，遮挡时是否仍可靠，以及物理优化改动了多少原始动作。摘要没有说明真机部署是否包含实时响应人的变化；离线动作可执行，并不直接证明机器人能应对临时撤手或改变站位。

- **判断**：值得读到关系约束和迁移后优化的具体公式，因为它们决定了方法保住的是互动含义，还是仅仅视觉相似。

## 研究关联

值得借鉴的是先明确“任务必须守住什么”，再允许身体姿态作适应性调整。对握手、搀扶这类关系决定成败的任务，模仿误差应包含双方关系，不能只比较机器人与示范者的关节位置。

### 下一步读哪里

下一步核查关系权重、解剖偏移和接触约束如何定义，再看不同体型与不同互动类别的分项结果；真机部分重点确认控制方式、人工修正量及失败情形。

- **概念**：视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Video.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Enabling a humanoid to interact naturally with human partners requires preserving not only individual motions but also the spatial, semantic, and contact relationships underlying the interaction (i.e., hugging, dancing, hand-shaking, etc.). Furthermore, a practical solution should generalize across various humanoid embodiments with distinct morphologies and kinematic constraints. To tackle this challenge, we propose HumiTransfer, a mimetic embodiment transfer framework that converts in-the-wild human-human interaction videos into physically plausible human-humanoid interactions. HumiTransfer first reconstructs 3D human motion with consistent foot-ground contact, then transfers one participant to a target humanoid embodiment via interaction modeling, using weighted joint-relative directions and anatomical offsets to prioritize interaction-critical inter-body relationships, while post-retargeting optimization enforces balance, contact, and collision avoidance. Subsequently, we apply HumiTransfer to 1,200 in-the-wild videos, producing approximately 500,000 frames of diverse interactions for the 26-DoF Unitree R1 Edu and the 23-DoF HighTorque Mini-hi humanoid robot, resulting in our HumiMimic dataset. Across both robots, HumiTransfer achieves superior motion fidelity, preserves inter-body relationships, and maintains contact accuracy compared with existing baselines. Moreover, we demonstrate that HumiMimic supports motion generation methods for synthesizing interactive humanoid motions following a human partner. Finally, our real robot deployments confirm the physical executability of the transferred motions in real-world settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36615v1
- Authors: Nghia Le, Khang Nguyen, Ba Long Tran, Thi Quynh Nhu Pham, Binh Nguyen, Tuong Do, Erman Tjiputra, Hoan Nguyen, Tung D. Ta, Baoru Huang, Hai-Nguyen, Nguyen, Anh Nguyen
- Published: 2026-10-27T04:18:31Z
- Age days: 0

</details>
