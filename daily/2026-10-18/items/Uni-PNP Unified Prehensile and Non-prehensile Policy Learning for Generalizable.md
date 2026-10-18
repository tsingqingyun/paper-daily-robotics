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
url: "https://arxiv.org/abs/2610.21735v1"
published: "2026-10-15T11:53:10Z"
age_days: 2
score: 27
created: 2026-10-18
concepts: ["世界模型", "机器人学习"]
---

# Uni-PNP: Unified Prehensile and Non-prehensile Policy Learning for Generalizable Object Pose Reaching

> [!summary] 这篇论文到底做了什么（基于摘要）
> Uni-PNP 用同一个策略学习推、翻、抓，把物体送到目标位置和朝向。它先学习不同几何接触会怎样带动物体，再通过从容易抓到难以抓取对象的训练安排，促使策略发现抓取以外的动作。

## 问题

目标位姿有时无法直接抓取后摆放，需要先推一下、翻起来或借桌面调整。摘要指出，现有方案常把这些技能分别训练，再用预设中间目标串起来，限制接触动作与抓取的协调；组合方式还容易依赖特定物体、夹爪形状和环境支撑。

### 用一个例子理解

理解用例（非论文实验）：输入是一只平躺、当前难以夹住的盒子及目标位姿；策略利用几何信息，先接触盒边使其翻起，再抓住并调整；输出是衔接的动作序列，而中间翻起姿态不需要由人预先指定。

## 创新点或方法

旧做法预先规定技能如何交接；Uni-PNP 让统一策略共同学习这些动作。训练先收集多种物体与夹爪的仿真接触数据，用预测接触所致运动的任务预训练几何编码器，让几何表示包含“碰上去会怎样”的信息。随后用两阶段强化学习，从可抓对象转向不可抓的对应对象，鼓励发现推翻等交互。推理时由统一策略生成动作；是否仍调用运动预测器、输入表示与动作参数，摘要未说明。

### 方法如何工作

1. 在仿真中让多种物体和夹爪发生接触，得到接触及后续运动的数据，为几何学习提供动作后果。
2. 训练几何编码器预测接触引起的物体运动，得到与操纵相关的表示。
3. 先在可抓对象上训练策略，再转向不可抓的对应对象，使策略有动机寻找推、翻等操作。
4. 执行时由同一策略完成接触动作与抓取的衔接，向目标位姿推进；具体动作接口，摘要只说明到此。

### 必要术语

- 位姿到达：把物体送到指定位置和朝向；这是本文的任务目标。
- 接触动力学：接触如何改变物体运动；本文用这种预测任务训练几何表示。
- 课程学习：按难度或条件安排训练顺序；本文从可抓对象转向不可抓对象。

## 证据

摘要报告，数百个已见对象与夹爪上的成功率为 76.39%，未见对应对象与夹爪上为 57.91%，分别超过最强位姿到达基线 20.52、17.79 个百分点。还分析了翻倒后抓取、抓持时借桌面重定向等涌现行为，并进行了现实迁移。未给基线名称、目标容差、测试次数和实机成绩，因此可支持其测试设置下的优势，不能据此断言任意物体或夹爪都能适用。

## 局限

未见组成绩明显低于已见组，说明迁移仍有难度。我的待核查问题是“不可抓”的定义、两阶段对象如何对应，以及实际仍需要哪些桌面支撑；摘要没有足够细节界定这些边界。

- **判断**：值得细读预训练目标与课程安排，因为它解释了统一策略为什么可能学出抓取前的准备动作。

## 研究关联

这里可借鉴的是让几何表示通过接触后果来学习。对需要先改变可抓条件的任务，仅识别形状可能不够；理解一次接触会怎样改变物体，才有机会把准备动作和抓取连起来。

### 下一步读哪里

先核查接触数据如何覆盖几何与运动，以及编码器怎样接入策略；再看两阶段课程、直接联合训练和分技能方法的对照。实机部分重点检查感知输入及夹爪变化范围。

- **概念**：世界模型 机器人学习
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/Uni-PNP Unified Prehensile and Non-prehensile Policy Learning for Generalizable.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object manipulation often requires combining non-prehensile actions with grasping. However, existing approaches typically develop these capabilities separately and integrate them by sequencing distinct primitives through prescribed intermediate objectives, limiting the coordination of contact motions and grasping. Their integration also remains sensitive to object and gripper geometry and depends on particular environmental supports, complicating real-world deployment. We present Uni-PNP, a unified policy that jointly learns prehensile and non-prehensile manipulation for object pose reaching across diverse objects and grippers. To achieve this, we first pretrain a geometry encoder to predict contact-induced object motion using a contact-dynamics dataset constructed from simulated interactions between diverse objects and grippers. We then train the policy in a two-stage reinforcement learning curriculum from graspable objects to ungraspable peers, encouraging the discovery of non-prehensile interactions and their integration with grasping. Experiments show 76.39% success on hundreds of seen objects with grippers, and 57.91% on unseen peers, outperforming the strongest pose-reaching baseline by 20.52 and 17.79 percentage points, respectively. We also analyze emergent behaviors, including nonprehensile and prehensile repositioning, grasp acquisition that requires grasping after tipping, and table-assisted reorientation while grasping, and transfer to the real-world scenario. Project page available at lgswdn.github.io/Uni-PNP.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21735v1
- Authors: Wenxuan Zhu, Yuze Wang, Jiangran Lyu, Jiayi Chen, Yixin Zheng, Mi Yan, Li Yi, Zhizheng Zhang, He Wang
- Published: 2026-10-15T11:53:10Z
- Age days: 2

</details>
