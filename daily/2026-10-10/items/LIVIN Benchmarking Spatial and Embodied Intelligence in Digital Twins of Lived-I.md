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
url: "https://arxiv.org/abs/2610.12069v1"
published: "2026-10-08T14:47:30Z"
age_days: 1
score: 32
created: 2026-10-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes

> [!summary] 这篇论文到底做了什么（基于摘要）
> LIVIN 把 30 个有人实际居住的家庭做成可交互的数字副本，保留家具和日常物品的真实摆放。它用这些环境测试空间理解、导航和移动操作，检查机器人能否应对拥挤、遮挡与狭窄操作空间。

## 问题

家庭机器人面对的不是只有房间外形和少量家具的空间，物品摆放会决定哪里看得见、走得通、伸得进去。摘要指出现有资源常在规模、与现实对应程度和交互准备程度之间取舍，难以同时保留真实布局并支持操作。

### 用一个例子理解

理解用例（非论文实验）：输入一个住宅副本和“到厨房拿杯子”；导航系统先在椅子与杂物之间寻找路径，操作系统再判断杯子附近是否有足够接近空间，最后输出移动与取物动作。这个例子说明环境约束怎样进入任务，不代表论文验证过该指令。

## 创新点或方法

本文从真实住宅观察出发，依次识别物体实例、重建建筑结构、生成并放置物体；每个阶段都由人对照源观察审查和修正，减少错误向后传递。最终副本保留观察到的房间、家具和日常物品配置。这是环境构建与评测工作，不是一种策略训练算法；摘要未说明参测模型如何训练，测试阶段则运行四类任务。

### 方法如何工作

1. 从住宅观察识别物体实例，确定副本需要保留哪些日常物品。
2. 重建建筑结构及空间布局，为家具和物体位置提供房间坐标基础。
3. 生成并放置物体，逐阶段人工对照源观察修正，使环境保持真实摆放约束。
4. 在副本中运行空间理解、导航和移动操作任务，观察这些约束下的能力；具体评分和交互实现摘要只说明到此。

### 必要术语

- 数字孪生：对应真实环境的数字副本；本文用它保留住宅的实际布局。
- 实例识别：区分场景中的具体物体；本文用它确定需要重建的对象。
- 移动操作：机器人既移动身体又操作物体；本文用它测试通行与交互约束的共同影响。

## 证据

摘要给出的规模是 30 个多样化住宅，评测任务为三维检测、三维重建、导航和移动操作。作者报告现有方法仍受密集摆放、遮挡、有限通行空间及受限交互区域挑战。没有方法名单、指标、分数或分项分析，故只能确认覆盖范围和定性困难，不能判断哪类方法最好，也不能把环境特征与失败建立因果对应。

## 局限

住宅来源真实，但机器人评测发生在数字副本中，不能直接等同于真机家庭成功率。我的待核查问题是几何、接触物理和物体可交互性如何验证，以及 30 个住宅覆盖了哪些居住习惯。人工校正也意味着扩大规模的成本需要核查。

- **判断**：值得读到环境质量验证和任务定义，因为它能帮助判断家庭评测是否保留了真正限制行动的空间条件。

## 研究关联

可借鉴的是把真实摆放视为任务条件的一部分，而非可随意替换的背景。评估家庭能力时，除了增加房屋数量，还应检查目标周围是否可接近、可观察和可操作。

### 下一步读哪里

先核查住宅采集范围、人工修正标准以及几何和物理质量验证；再看四项任务的输入、成功条件、数据划分和参测方法，尤其检查导航可达是否与操作可达分别评估。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/LIVIN Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-I.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Realistic household simulation must capture not only diverse environments but also the lived-in object arrangements and spatial constraints that shape robot motion and interaction. Existing resources often trade off scale, real-world correspondence, and interaction readiness, leaving a gap in faithful, interactive replicas of how real homes are actually arranged. To this end, we introduce LIVIN, a benchmark for spatial and embodied intelligence built on digital twins of 30 diverse lived-in homes. These replicas preserve observed room layouts, furniture configurations, and everyday belongings. To construct them, we design a human-in-the-loop workflow comprising instance recognition, architectural reconstruction, and object generation and placement, with intermediate results reviewed and corrected by humans against the source observations at each stage. We evaluate four tasks in LIVIN: 3D detection, 3D reconstruction, navigation, and loco-manipulation. Our evaluations show that current methods remain challenged by the dense object arrangements, occlusions, limited free space, and constrained interaction regions found in realistic lived-in homes. We hope LIVIN will help advance embodied AI in real-world homes, from spatial understanding to robotic interaction, and ultimately bring embodied intelligence into everyday home environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12069v1
- Authors: Peijun Xu, Chuansen Nie, Yiyang He, Yinuo Bai, Jingyang Liu, Kuixiang Shao, Yuyang Jiao, Kuanhao Xia, Jiayi Zhu, Zitian Yang, Yanqi Zhang, Tianye Tan, Shuwei Di, Junyi Xu, Jingyi Yu, Jiayuan Gu
- Published: 2026-10-08T14:47:30Z
- Age days: 1

</details>
