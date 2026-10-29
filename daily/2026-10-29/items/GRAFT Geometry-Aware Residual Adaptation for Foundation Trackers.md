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
url: "https://arxiv.org/abs/2610.36507v1"
published: "2026-10-27T02:10:36Z"
age_days: 1
score: 28
created: 2026-10-29
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers

> [!summary] 这篇论文到底做了什么（基于摘要）
> GRAFT 让已经会跟随全身动作的人形机器人，根据地形修正下半身执行目标，而不改动原有行为模型。它把学习集中到落脚、抬脚和接触时机这些地形敏感环节，再让适配器从机载深度获取所需信息。

## 问题

任务是让可复用的全身运动跟踪器通过台阶、沟隙和平台。原有模型主要在平地动作上训练，缺少针对局部地形调整脚部执行的明确机制。已有地形适配方法常把感知与跟踪器一起重训或微调，数据和计算成本较高，也让普通动作跟踪依赖感知路径。

### 用一个例子理解

理解用例（非论文实验）：输入一段原本用于平地行走的参考动作，以及前方台阶的深度图；适配器据地形修正下半身执行目标，冻结跟踪器继续产生协调关节指令，输出一次尝试跨上台阶的全身运动。

## 创新点或方法

旧做法连同跟踪器一起改；GRAFT 冻结行为模型及其运动参考接口，只让轻量适配器为下半身执行目标增加地形相关修正。训练用任务奖励和脚部几何奖励，并抑制平地上不必要的修正；随后把使用特权地形观测学到的能力蒸馏到机载深度输入。部署时沿用原参考动作，由深度驱动适配器。修正量的具体定义、奖励公式和蒸馏流程未在摘要展开。

### 方法如何工作

1. 保留冻结跟踪器和参考接口，让已有模型继续负责基本运动及全身协调。
2. 根据地形生成下半身目标修正，使执行能适应脚附近的几何条件。
3. 用任务与脚部几何奖励训练适配器，同时约束平地修正，减少无必要的干预。
4. 把特权地形观测下的能力蒸馏到机载深度，使部署时能够使用机器人实际拥有的传感输入。
5. 将修正目标交给原跟踪器执行，在仿真及指定真机组合上检验通过地形的能力。

### 必要术语

- 行为基础模型（BFM）：根据运动参考生成协调关节指令的可复用模型；本文保留它的参数。
- 残差适配：在原有目标上增加修正量；本文只修正下半身执行目标。
- 特权观测：训练时可用、部署时不一定能获得的信息；用于学习地形适配。
- 蒸馏：让依赖较受限输入的模型学习已有能力；本文将地形观测能力转到机载深度。

## 证据

摘要说明在 4 个冻结跟踪器上进行了楼梯、沟隙和平台仿真评估，并在 Unitree G1 真机上验证：适配后的 SONIC 使用机载深度和未经修改的参考动作通过地形。没有提供成功率、速度、跌倒率、对比方法或消融数字。因此可以确认验证覆盖了多个仿真跟踪器及一个真机组合，但不能量化相对重训方案的优势，也不能把全部仿真结果视为都已完成真机验证。

## 局限

摘要没有明确列出局限。待核查的是地形高度、沟宽和深度噪声的覆盖范围，以及修正下半身时如何维持全身稳定。冻结参数本身不保证原有跟踪质量完全不变；这一点需要平地与复杂参考动作实验支持。

- **判断**：值得细读修正接口、奖励和消融：它把地形学习的职责划得很清楚，但摘要尚不足以判断适配器的能力上限。

## 研究关联

可借鉴的判断是：如果已有模型已经掌握全身协调，新困难又主要来自局部执行条件，可以先把学习范围缩到必要修正。平地抑制项也很关键——适配器需要学会何时不干预，才能保留原有能力。

### 下一步读哪里

优先核查修正发生在哪一层、脚部几何奖励如何计算、深度输入与动作的延迟；再看平地干扰、去掉正则项或蒸馏的消融，以及 SONIC 真机的地形范围和失败案例。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/GRAFT Geometry-Aware Residual Adaptation for Foundation Trackers.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid behavior foundation models (BFMs) provide reusable whole-body motion priors: given a kinematic reference, they generate coordinated joint commands for motion replay, teleoperation, and VLA control. However, trained primarily on flat-ground motion, BFMs lack an explicit mechanism to adapt foot placement, swing clearance, and contact timing to local terrain. Many terrain-aware BFM approaches address this limitation by retraining or fine-tuning the tracker together with perception, incurring substantial data and computation costs while coupling ordinary tracking to the perception pathway. To bridge this gap, we propose GRAFT, a geometry-aware residual adaptation framework for frozen behavior trackers. GRAFT preserves the BFM parameters and motion-reference interface, while a lightweight adapter adds terrain-conditioned corrections only to lower-body execution targets. The adapter is trained with task and foot-geometry rewards, regularized to suppress unnecessary corrections on flat ground, and distilled from privileged terrain observations to onboard depth. Because the frozen BFM already provides whole-body reference tracking and nominal locomotion, GRAFT reduces terrain learning to a focused execution-adaptation problem. We instantiate the framework on four frozen trackers and evaluate stairs, gaps, and platforms in simulation. We further validate it through real-world deployment on a Unitree G1, where the adapted SONIC tracker traverses terrain with onboard depth and unmodified references.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36507v1
- Authors: Liang Li, Guoyao Zhang, Xingyu Chen, Sikai Wu, Qianyang Wu, Yuhang Lin, Renjing Xu, Mingliang Zhou, Diyun Xiang
- Published: 2026-10-27T02:10:36Z
- Age days: 1

</details>
