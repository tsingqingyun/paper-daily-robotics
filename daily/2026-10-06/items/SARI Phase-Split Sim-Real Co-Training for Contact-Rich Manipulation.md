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
url: "https://arxiv.org/abs/2610.02804v1"
published: "2026-10-02T04:50:08Z"
age_days: 3
score: 32
created: 2026-10-06
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> SARI 把操作分成接近物体和接触物体两个阶段：仿真提供丰富的接近路径，真实示范提供可信的接触动作。它将两类数据共同训练成一个 VLA 策略，执行时无需人工标记阶段或切换控制器。

## 问题

任务是让机器人在不同物体位置完成接触密集操作，同时减少昂贵的真实示范。覆盖整个工作空间需要位置多样性，但接触过程又依赖准确物理；整段使用同一种数据来源，难以同时满足这两个要求。SARI 针对的是空间覆盖与接触真实性所需数据不同这一瓶颈。

### 用一个例子理解

理解用例（非论文实验）：训练数据中，仿真提供从不同位置接近插孔的路径，真实机器人提供少量位置的插入动作；输入新位置的图像和“插入零件”，同一策略输出接近并插入的动作序列。该任务为自拟，不代表作者已验证。

## 创新点或方法

旧做法按完整任务混合仿真和真实数据；SARI 改为按阶段分配来源。自由空间接近对适度仿真误差较宽容，于是在逼真数字孪生中生成多样路径；接触阶段只在少量位置采真实示范，依据是接触变化相对较小。训练时使用这些分段示范继续训练单一策略，并对齐视觉外观、统一相机相对动作表示；推理时由策略自然连接动作，没有显式阶段标签或手写切换。

### 方法如何工作

1. 按自由空间接近与接触划分示范需求，明确哪部分需要位置多样性、哪部分需要真实物理。
2. 在数字孪生中生成多位置接近轨迹，并在少量真实位置采集接触示范，得到互补数据。
3. 对齐视觉外观并统一相机相对动作表示，使不同来源的数据能够共同训练单一策略。
4. 用分段示范继续训练 VLA，推理时连续输出动作，无需显式阶段标签或人工切换。

### 必要术语

- 数字孪生：对应真实环境的仿真副本；本文用它生成多样的接近轨迹。
- 相机相对动作：以相机坐标描述动作；本文用它统一仿真与真实数据的动作表示。
- 接触密集操作：成败高度依赖接触过程的操作；本文为这一阶段优先采集真实示范。

## 证据

摘要报告五项真实接触密集任务：真实数据采集时间减少 34.3%，未见物体位置上的成功率为 27.5%，所有按完整任务进行仿真与真实结合的基线均为 0%。结果支持该设置下的采集节省及相对优势，但 27.5% 仍说明多数尝试失败。摘要未给基线名称、试验次数、逐任务结果及采集时间比较的详细条件。

## 局限

核心待核查问题是接触动作能否跨位置复用：位置变化也可能改变视角、机械臂姿态和受力条件。摘要中的成功率已经限制了可靠性判断；五个实体任务的结果也不能保证其他接触类型有同样收益。

- **判断**：值得读阶段切分和动作坐标表示，数据分工很具体；但应把结果看作有限成功的相对改善，而非可靠部署的证明。

## 研究关联

可借鉴的是按误差来源分配数据，而非只问仿真和真实数据各占多少。当位置变化主要影响接近路径、接触方式相对稳定时，可以让仿真负责空间覆盖，真实数据负责接触；是否符合这个条件，应先验证。

### 下一步读哪里

先查阶段边界怎样确定、分段轨迹如何用于训练及视觉如何对齐，再看相机相对动作怎样支持跨位置复用。实验重点核查五项任务、未见位置的划分和 34.3% 节省的计时口径。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/SARI Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models often require costly real-world demonstrations to adapt to contact-rich manipulation tasks, particularly when generalization across object placements is needed. We propose SARI (Simulated Approach, Real Interaction), a phase-split sim-and-real co-training framework built on a simple insight: spatial coverage and contact physics should be acquired from the domains best suited to them. Specifically, free-space approaches require spatial diversity but tolerate modest simulation gaps, making them ideal for synthetic generation; conversely, contact interactions demand accurate physics but vary little across object placements, allowing a few real demonstrations to generalize across the workspace. SARI generates diverse simulated approaches in a photorealistic digital twin while collecting real contact interactions at only a few placements. Post-trained on these phase-segmented demonstrations, a single policy seamlessly stitches simulated approaches with real contact interactions using visual appearance alignment and a shared camera-relative action representation--without explicit phase labels or hand-coded switches. Across five real-world contact-rich manipulation tasks, SARI reduces real-data collection time by 34.3% and achieves 27.5% success at unseen placements, where all full-task sim-real baselines fail completely (0%).

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02804v1
- Authors: Xingxin He, Yuxuan Jiang, Haonan Zhang, Chuhan Cui, Kaile Li, Zhongxing Zheng, Caihao Xu, Ziqi Wang
- Published: 2026-10-02T04:50:08Z
- Age days: 3

</details>
