---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09158v1"
published: "2026-09-08T17:59:55Z"
age_days: 0
score: 33
created: 2026-09-09
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model

> [!summary] 先说人话（基于摘要）
> TANGO让人形机器人根据语言和第一视角图像，直接预测全身29自由度动作来穿过杂乱空间。它在仿真中合成可执行的全身穿行示范，学习手臂、躯干和步态的协调。

## 这篇到底在做什么

- **卡在哪里**：杂乱室内导航需要身体各部分适应三维障碍，传统二维路径规划不能充分表达手臂摆放、躯干调整和步态变化之间的协同。
- **关键解法**：输入自然语言指令与自我中心RGB图像，输出供下游全身控制器使用的29自由度关节动作。训练数据完全由仿真中的全局规划、运动学生成、障碍感知编辑和强化学习跟踪流水线产生。
- **拿什么证明**：摘要报告仿真视觉语言导航达到先进水平，并超过强模块化基线；在无真实导航训练数据情况下零样本部署到Unitree G1，展示杂乱真实场景穿行。摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：将VLA动作空间扩展到全身导航，对研究具身智能体如何跨越语言、三维几何和运动控制层级具有直接参考价值；摘要未展示世界模型机制。
- **先别急着信**：需要核查真实测试规模、障碍难度，以及下游控制器承担了多少避障和稳定性职责。
- **判断**：全身VLA方向值得精读数据生成与控制接口，性能领先程度需看定量实验。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/TANGO Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Lan.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We study the problem of navigating cluttered indoor environments with a humanoid robot. Unlike conventional methods that model navigation as a 2D path planning problem, humanoid traversal in cluttered environments requires continuous geometry-aware whole-body adaptation, including coordinated arm placement, torso adjustment, and gait modulation for collision-free movement through complex 3D spaces. We introduce TANGO, the first whole-body vision-language navigation framework for language-conditioned humanoid traversal in cluttered environments. Given a natural-language instruction and egocentric RGB observations, TANGO directly predicts 29-DoF joint-space actions for downstream whole-body control. We train TANGO entirely in simulation by synthesizing diverse collision-free traversal behaviors via global path planning, kinematic whole-body motion generation, obstacle-aware motion editing, and RL-based tracking. This pipeline provides dynamically feasible action supervision for learning language-conditioned whole-body policies. In extensive simulation experiments, TANGO demonstrates state-of-the-art performance in vision-language navigation, while outperforming strong modular baselines in navigating challenging scenes requiring obstacle negotiation. Lastly, we deploy TANGO zero-shot on a Unitree G1 humanoid robot, and observe robust language-guided traversal in cluttered real-world scenes without training on any real-world navigation data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09158v1
- Authors: Anqi Li, Yuxin Chen, Zhaobo Li, Zhuo Cao, Junli Ren, Masayoshi Tomizuka, Dhruv Shah
- Published: 2026-09-08T17:59:55Z
- Age days: 0

</details>
