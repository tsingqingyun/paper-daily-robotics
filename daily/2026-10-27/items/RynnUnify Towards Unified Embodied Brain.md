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
url: "https://arxiv.org/abs/2610.32965v1"
published: "2026-10-23T17:54:07Z"
age_days: 3
score: 30
created: 2026-10-27
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# RynnUnify: Towards Unified Embodied Brain

> [!summary] 这篇论文到底做了什么（基于摘要）
> RynnUnify 是一个 16B 具身模型，让语言推理与视频预测交替进行，用来理解场景并规划后续子任务。作者还分别扩展了“何时使用视频预测”和“怎样输出机器人控制”两种能力。

## 问题

长任务要求机器人既理解当前物理关系，又预想多个子任务之后的状态，并把判断接到控制上。本文试图连接这些能力；摘要没有具体说明旧方案在哪个环节失败，因此不能断言统一模型已经解决了模块间的全部衔接问题。

### 用一个例子理解

理解用例（非论文实验）：输入厨房画面和“把杯子放进柜子”；模型判断柜门状态，必要时预测开门后的画面，再继续推理放杯步骤；控制扩展输出动作。此例只解释能力如何串联。

## 创新点或方法

从分别处理理解、预测和控制的思路，转向以同一模型交错进行视频与语言推理。智能体扩展再用强化学习，学习选择性调用视频预测，辅助判断未观测状态和交互后果；另一项 world-action 扩展把理解与预测用于控制。基础模型训练配方和动作接口未说明，推理时的具体调用流程也需查正文。

### 方法如何工作

1. 读取视觉与语言输入，判断空间关系、物理变化和指令对应对象，为规划建立当前状态。
2. 交错进行语言推理与视频预测，预想连续子任务后的场景，支持长程规划。
3. 智能体扩展选择何时使用预测，以补充对未观测状态和交互结果的判断。
4. 控制扩展将这些能力转为机器人动作；摘要未说明具体动作表示和执行闭环。

### 必要术语

- 交错视频—语言推理：在推理过程中交替使用语言与视频预测；连接当前理解和未来规划。
- 选择性预测：按需要使用预测结果；是智能体扩展通过强化学习获得的能力。
- world-action 扩展：把世界理解和预测接到动作控制的扩展；具体接口需核查。

## 证据

摘要称其具身理解平均分在所评统一多模态模型中最高；Rynn-VP 总分比 Cosmos 3 Nano 高 9.75 分；智能体扩展在 Rynn-GEU 比直接推理高 6.0 分。控制扩展在选取的 20 个 RoboCasa365 复合任务上成功率为 51.5%，三项真机任务平均为 46.7%。这些证据对应不同能力，不能混成同一种提升。

## 局限

控制结果须区分 RoboCasa365 仿真与三项真机任务。摘要未给任务选择标准、试验次数及控制基线，也未隔离视频预测对控制成功的贡献；目前不能据此认定统一训练必然优于专用系统。

- **判断**：值得先读能力衔接与调用策略，再看控制消融，判断统一模型究竟复用了哪些能力。

## 研究关联

值得借鉴的是把预测当作可选择的推理工具：遇到不可见状态或不确定后果时再预测，而不是默认每一步都生成视频。是否划算，需要同时看判断质量和生成成本。

### 下一步读哪里

检查视频与语言怎样交错、强化学习奖励如何定义、控制扩展怎样训练；再核查 Rynn-VP 与 Rynn-GEU 的评分含义，以及控制任务有无禁用预测的对照。

- **概念**：多模态基础模型 智能体 Agent 机器人学习
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/RynnUnify Towards Unified Embodied Brain.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce RynnUnify, a 16B unified embodied model that combines strong embodied understanding with long-horizon visual planning through interleaved video--language reasoning. With capabilities spanning spatial reasoning, physical prediction, and grounding, RynnUnify connects an understanding of the physical world with visual anticipation of how it evolves across successive subtasks. Building on these capabilities, we further develop an agentic extension through reinforcement learning to selectively use video predictions for reasoning about unobserved states and interaction outcomes. We also develop a world-action extension of the full RynnUnify model, translating its understanding and prediction capabilities into robot control. To evaluate these capabilities, we introduce Rynn-VP and Rynn-GEU for long-horizon visual planning and anticipatory reasoning. Experiments show that RynnUnify achieves the highest average embodied understanding score among the evaluated unified multimodal models and improves the Rynn-VP overall score by 9.75 points over Cosmos 3 Nano. Its agentic extension improves the Rynn-GEU average by 6.0 points over direct reasoning, while the world-action extension achieves 51.5\% success on 20 selected composite RoboCasa365 tasks and 46.7\% average success across three real-robot tasks. Together, these results establish RynnUnify as a shared foundation for embodied understanding, visual planning, and robot control, taking a step toward a unified embodied brain.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.32965v1
- Authors: Minghao Zhu, Bohan Hou, Kun Xiang, Zixuan Wang, Yinzhou Tang, Yifei Yang, Zhikai Wang, Tianyi Zhang, Kehan Li, Haoyu Zhao, Siteng Huang, Leigang Qu, Sicong Leng, Dongchi Huang, Mingxiu Chen, Shijian Lu, Yue Wang, Xiaodan Liang, Zhenyu Zeng, Deli Zhao, Chengju Liu, Jianfei Yang, Xin Li
- Published: 2026-10-23T17:54:07Z
- Age days: 3

</details>
