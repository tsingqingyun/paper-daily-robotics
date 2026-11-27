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
url: "https://arxiv.org/abs/2611.34655v1"
published: "2026-11-25T16:29:17Z"
age_days: 1
score: 30
created: 2026-11-27
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution

> [!summary] 这篇论文到底做了什么（基于摘要）
> Nav4Manip 教移动机器人停到机械手真正够得着、下得去手的位置。它把操作反馈送回导航训练，让导航模块学会按后续动作的需求选路线和停车姿态。

## 问题

长程移动操作分成走到物体附近和动手两段。对导航来说，进到目标附近可能就算到达；对机械手来说，底座偏一点或朝向不对，手就可能够不到把手。摘要指出，传统做法把导航与操作分开训练，导航就缺少来自下游动作的反馈。

### 用一个例子理解

理解用例（非论文实验）。输入是跨房间打开抽屉的指令。机器人来到柜前，两个停车点都在柜子附近，但只有一个留出了正对把手、向后拉动的空间。导航用训练中学到的可操作性选停车点和朝向，操作模块接手并输出开抽屉的动作。

## 创新点或方法

Nav4Manip-N 学走路和判断哪里便于操作，Nav4Manip-M 则训练世界动作模型来执行灵巧操作。导航训练先联合学习导航和操作可行性预测，再从自身生成的路径中筛掉低质量轨迹，用保留下来的轨迹微调，最后用 AI 反馈给出的反事实偏好继续优化决策。评测运行提供了配对的导航与操作轨迹以及可行性监督。执行时，导航需把机器人带到可操作的位置，再交给操作模块完成动作。摘要未说明反馈的计算方式和在线交接条件。

### 方法如何工作

1. 从任务运行中配对导航轨迹和后续操作，得到可用来监督导航的操作可行性信息。
2. 联合训练路径行为和操作可行性预测，让导航同时学习怎么到达、到达后是否好动手。
3. 筛选导航策略自己生成的路径，再用反事实偏好继续优化决策。摘要只列出这两个阶段，未解释具体的评分规则。
4. 执行时用导航策略抵达并摆好底座，再由操作模块输出灵巧动作。

### 必要术语

- 操作可行性：从当前位置和姿态能否顺利动手；本文把它作为导航学习的监督。
- 反事实偏好：比较实际选择和本可以做出的另一种选择；本文用它进一步训练导航决策。
- 世界动作模型：用场景信息支持机器人动作生成的模型；本文由它承担下游灵巧操作。

## 证据

摘要报告，在公开视觉语言导航基准和作者建立的 Nav-N-Manip 上达到当时最优表现，真机也完成了多种灵巧移动操作任务。材料未给出具体对照方法、指标、分数、真机试次数或失败分布，也没有说明各项评测的仿真与真机划分。因此可以确认作者报告了基准和真机两类证据，尚无法估计真机可靠性，或把增益归因于某一训练阶段。

## 局限

摘要把粗粒度到达和训练割裂列为现有系统的瓶颈。我会核查操作模块是否固定时导航仍有增益，以及操作反馈换到不同底座尺寸、臂展或新场景后是否可靠。摘要描述了反馈方向，尚未具体交代操作模块怎样随导航策略共同更新。

- **判断**：值得读到轨迹配对、可行性标签和训练消融。只有知道后续操作的表现如何改变导航决策，才能判断这套训练是否值得迁移。

## 研究关联

当下游动作对交接条件很敏感时，可以把它能否顺利接手作为上游的训练信号。对于移动操作，这意味着比较两个停车姿态时，还要看机械手从各个姿态出发能否完成下一步。

### 下一步读哪里

先查 Nav4Manip-Pairs 如何把导航终点与后续操作配成一条训练样本，再查反事实偏好比较的是位置、朝向还是整条路径。最后看基准指标和消融能否分辨到达、交接和操作各阶段的收益。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/Nav4Manip From Navigation to Dexterous Mobile Manipulation through Co-Evolution.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Dexterous mobile manipulation is essential for robots to perform useful tasks in complex, unstructured environments. However, existing systems face two challenges. First, navigation remains too coarse for downstream manipulation, which often requires a precise base position and approach orientation rather than merely reaching a meter-scale goal region. Second, navigation and manipulation are commonly trained in isolation, lacking a feedback loop that enables the two capabilities to co-evolve. These limitations prevent current systems from reliably executing long-horizon dexterous mobile-manipulation tasks in real-world environments. To address them, we introduce Nav4Manip, a bidirectionally coupled co-evolution system for long-horizon dexterous mobile manipulation. It comprises two complementary architectures: Nav4Manip-N learns long-horizon navigation and refines its policy through manipulation feedback, while Nav4Manip-M trains a world-action model (WAM) for downstream dexterous manipulation. We train Nav4Manip-N in three stages: multi-task co-tuning learns navigation behavior and manipulation-aware affordance prediction; rejection sampling fine-tuning (RFT) rejects low-quality policy-generated paths and fine-tunes the model on retained trajectories; and reinforcement learning from AI feedback (RLAIF) uses counterfactual preferences to further improve navigation decisions. To support this framework, we establish the Nav-N-Manip benchmark and construct Nav4Manip-Pairs from benchmark rollouts, providing large-scale paired navigation--manipulation trajectories and affordance supervision. Extensive experiments on public vision-language navigation (VLN) benchmarks and Nav-N-Manip demonstrate state-of-the-art performance, while real-world evaluations show that Nav4Manip completes diverse dexterous mobile-manipulation tasks. Project website: https://nav4manip.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34655v1
- Authors: Yusen Feng, Zixi Kang, Zhijun Yin, Changxiao Liu, Tianhong Gao, Jiazhao Zhang, Jiahang Liu, Libin Liu, Zhizheng Zhang, He Wang
- Published: 2026-11-25T16:29:17Z
- Age days: 1

</details>
