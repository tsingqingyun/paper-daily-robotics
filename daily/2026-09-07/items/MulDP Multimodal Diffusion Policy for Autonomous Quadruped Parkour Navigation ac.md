---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03984v1"
published: "2026-09-03T15:19:17Z"
age_days: 3
score: 31
created: 2026-09-07
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习"]
---

# MulDP: Multimodal Diffusion Policy for Autonomous Quadruped Parkour Navigation across Complex Terrains

> [!summary] 先说人话（基于摘要）
> MulDP 将视觉、本体感知和目标输入扩散策略，直接生成时间连贯、带预见性的导航速度指令，让四足机器人自主规划并通过复杂跑酷地形。

## 这篇到底在做什么

- **卡在哪里**：现有四足跑酷多依赖人类做高层规划；自主导航还受精细速度调节、长时预判以及感知与身体执行耦合不足限制。
- **关键解法**：策略接收视觉、机器人本体状态和目标信息，输出一段导航速度命令序列，以扩散生成维持时间一致性和预见性；作者另建QPND多模态数据集覆盖多种行为与复杂地形用于训练。
- **拿什么证明**：摘要称进行了广泛仿真和真实实验，证明可实现稳健的长时自主导航与复杂地形穿越；未给任务数、成功率、基线或QPND规模等可核查数字。

## 值不值得读

- **和你的研究有什么关系**：它把扩散策略从局部动作生成推进到四足跑酷的高层速度规划，并提供对应多模态数据方向，对自主具身导航有直接价值。
- **先别急着信**：摘要没有量化自主程度、长时范围和真实环境成功率，也无法判断扩散策略相对其他序列策略的必要性。
- **判断**：做四足自主导航者可深入看数据集和控制接口；缺少摘要数字使其余读者宜先快速浏览实验。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/MulDP Multimodal Diffusion Policy for Autonomous Quadruped Parkour Navigation ac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Quadruped robots have demonstrated impressive agility in parkour locomotion across complex terrains. However, most systems still rely on human intervention for high-level planning, and autonomous parkour navigation remains underexplored. The key challenges include fine-grained velocity regulation, long-horizon anticipatory behaviors, and tight coupling between perception and embodied execution. To address these challenges, we propose a Multimodal Diffusion Policy (MulDP) that integrates visual perception with robot proprioception and goal information to generate temporally coherent and anticipatory navigation velocity commands, tightly coupling perception with embodied control to enable robust autonomous navigation. To support the training of MulDP, we construct the first Quadruped Parkour Navigation Dataset (QPND), a multimodal dataset that encompasses diverse navigation behaviors and complex terrains. Extensive simulation and real-world experiments demonstrate that MulDP enables robust long-horizon autonomous navigation and effective traversal across complex terrains.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03984v1
- Authors: Kangmai Hu, Yueqi Zhang, Peng Zhai, Xiaoyi Wei, Jiabin Hu, Zhixiang Liu, Quancheng Qian, Lihua Zhang
- Published: 2026-09-03T15:19:17Z
- Age days: 3

</details>
