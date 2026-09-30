---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.31343"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 26
created: 2026-09-05
concepts: ["世界模型", "具身智能评测与基准"]
---

# Learning Terrain-Aware Whole-Body Control for Perceptive Legged Loco-Manipulation

> [!summary] 先说人话（基于摘要）
> TA-WBC 给腿式操作机器人的全身控制加入地形外感知：分层编码器提前调整姿态和落脚点，基于足部接触平面定义末端目标，并用双策略蒸馏兼顾大范围动作与地形适应。

## 问题

许多全身控制器主要依赖本体感知，看不到地形拓扑，因此在复杂地面上难以主动调整；基座高度、横滚和俯仰变化还会扰动机械臂目标，简单加入地形策略又可能遗忘原有全身动作能力。

## 创新点或方法

统一强化学习策略以分层外感知编码器提取地形特征；末端采样相对足部接触平面定义，从而与基座姿态变化解耦；双策略蒸馏把大工作空间动作能力和地形适应整合进同一策略。

## 证据

仿真和真实实验显示可达空间更大、跟踪误差更低、意外绊倒更少；摘要未给具体数值或任务数量。


## 局限

需核查三项改进分别贡献多少、外感知噪声下是否稳健，以及蒸馏是否在某些动作范围造成性能折衷。

- **判断**：腿式全身控制研究者值得读实现与消融；摘要的定性结果不足以判断相对现有控制器的实际领先幅度。

## 研究关联

对腿式移动操作，这将地形感知从单纯行走扩展到手脚协调任务，有助于机器人在真实复杂地面维持操作精度。与世界模型的直接关系较弱。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/Learning Terrain-Aware Whole-Body Control for Perceptive Legged Loco-Manipulatio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.31343v2 Announce Type: replace Abstract: Legged manipulators integrate exceptional terrain adaptability along with mobile manipulation capabilities, which make them highly promising for deployment in human-centric environments. By coordinating the control of both legs and arms, a whole-body controller can significantly expand the operational workspace of legged manipulators. However, many existing whole-body controllers primarily depend on proprioception and do not incorporate the critical exteroception required for effective terrain topology perception. This limitation can hinder their ability to adapt to varying environmental conditions and navigate complex terrains effectively. In this paper, we introduce TA-WBC, a terrain-aware whole-body control framework for legged manipulators, which features a novel RL-based unified policy tailored to whole-body loco-manipulation tasks in various terrains. Specifically, we employ a \rev{hierarchical exteroceptive encoder} to extract terrain features, providing an essential basis for the robot to proactively adapt posture and footholds. Furthermore, to facilitate stable cross-terrain loco-manipulation, we propose a novel end-effector sampling method based on the foot contact plane, \rev{decoupling the manipulation target from base height, roll, and pitch variations}. Moreover, a dual-policy distillation module is introduced to integrate expansive whole-body motion with terrain adaptability without catastrophic forgetting. The simulation and real-world experiments validate the robustness of our proposed controller, which leads to a larger reachable space, less tracking error, and reduced unexpected stumbles. This unified policy highlights the promising capabilities of legged manipulators in performing loco-manipulation tasks across complex terrains.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.31343
- Authors: Sikai Guo, Yudong Zhong, Guoyang Zhao, Botao Dang, Zhihai Bi, Jun Ma
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
