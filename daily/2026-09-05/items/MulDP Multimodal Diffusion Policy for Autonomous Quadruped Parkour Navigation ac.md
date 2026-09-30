---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03984"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 31
created: 2026-09-05
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习"]
---

# MulDP: Multimodal Diffusion Policy for Autonomous Quadruped Parkour Navigation across Complex Terrains

> [!summary] 先说人话（基于摘要）
> MulDP 把视觉、本体感知和目标信息融合进扩散策略，直接生成时间连贯、具有前瞻性的导航速度指令，让四足机器人自主完成复杂地形跑酷。

## 这篇到底在做什么

- **卡在哪里**：现有四足跑酷多依赖人类进行高层规划；全自主导航需要精细控速、长时程预判，并将环境视觉与身体执行紧密耦合，这些能力尚未被充分解决。
- **关键解法**：Multimodal Diffusion Policy 接收视觉、本体状态和目标，生成连续时间上的导航速度命令；作者同时构建 QPND 多模态数据集，覆盖多种导航行为与复杂地形，为策略训练提供数据。
- **拿什么证明**：摘要称进行了广泛仿真和真实实验，并展示稳健的长时程自主导航及复杂地形通过能力；未给出可核查的成功率、数据规模或基线差值。

## 值不值得读

- **和你的研究有什么关系**：对具身导航和机器人学习，它把扩散策略从局部运动生成推进到自主跑酷的高层速度规划，并提供面向此任务的多模态数据资源。
- **先别急着信**：摘要没有量化证据，需核查 QPND 的规模与覆盖度、扩散采样延迟，以及与传统规划器和非扩散策略的公平比较。
- **判断**：方向有趣，适合四足导航研究者读方法与视频；在看到量化结果前，不宜仅凭“稳健”判断领先程度。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/MulDP Multimodal Diffusion Policy for Autonomous Quadruped Parkour Navigation ac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03984v1 Announce Type: new Abstract: Quadruped robots have demonstrated impressive agility in parkour locomotion across complex terrains. However, most systems still rely on human intervention for high-level planning, and autonomous parkour navigation remains underexplored. The key challenges include fine-grained velocity regulation, long-horizon anticipatory behaviors, and tight coupling between perception and embodied execution. To address these challenges, we propose a Multimodal Diffusion Policy (MulDP) that integrates visual perception with robot proprioception and goal information to generate temporally coherent and anticipatory navigation velocity commands, tightly coupling perception with embodied control to enable robust autonomous navigation. To support the training of MulDP, we construct the first Quadruped Parkour Navigation Dataset (QPND), a multimodal dataset that encompasses diverse navigation behaviors and complex terrains. Extensive simulation and real-world experiments demonstrate that MulDP enables robust long-horizon autonomous navigation and effective traversal across complex terrains.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03984
- Authors: Kangmai Hu, Yueqi Zhang, Peng Zhai, Xiaoyi Wei, Jiabin Hu, Zhixiang Liu, Quancheng Qian, Lihua Zhang
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
