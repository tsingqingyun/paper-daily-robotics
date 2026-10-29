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
url: "https://arxiv.org/abs/2610.37652v1"
published: "2026-10-27T17:58:20Z"
age_days: 1
score: 31
created: 2026-10-29
concepts: ["世界模型", "具身智能评测与基准"]
---

# Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇让 LEAP 多指手连续把手中物体移到指定位置和朝向，并额外学习一个可调保守程度的残差安全过滤器来减少掉落。关键是把“完成目标”和“避免掉落”分别处理，再在真机上量化两者的取舍。

## 问题

任务不只是反复转动物体，而是在不同手腕朝向下，连续完成手指可达范围内的多种物体位姿目标。难点在于换接触和调整抓握时仍要拿稳；摘要指出，已有技能多限于简单抓握或重复动作，而且很少衡量掉落等安全问题。

### 用一个例子理解

理解用例（非论文实验）：输入手中小盒子的当前位姿和目标朝向；任务策略生成手指动作，安全过滤器修正可能导致失稳的部分，输出最终动作，再根据新观察继续调整。

## 创新点或方法

作者在仿真中训练任务策略，不用人类数据：生成抓握数据集，提供多样初始状态和目标，并采用自适应摩擦课程。通过系统辨识，使策略无需真机微调即可迁移；运行时可用动捕或腕部深度相机获得观察。在任务策略之上，学习残差安全过滤器，调整原动作，并允许调节保守程度。过滤器的训练目标、介入规则和具体输入，摘要未说明。

### 方法如何工作

1. 生成多样抓握与目标，让训练覆盖不同起点和手指接触方式。
2. 在仿真中配合自适应摩擦课程训练任务策略，使其学习连续到达目标。
3. 通过系统辨识缩小仿真与真手差异，让策略零样本迁移到硬件。
4. 运行时由安全过滤器修正任务动作，并用保守程度参数控制完成目标与避免掉落的取舍。

### 必要术语

- 物体位姿：物体的位置和朝向；是策略需要连续追踪的目标。
- 系统辨识：测量并拟合真实硬件的动力学等参数；帮助仿真策略迁移。
- 残差安全过滤器：在原动作上添加修正的模块；用于降低掉落风险。
- 摩擦课程：训练中有组织地调整摩擦条件；具体调整规则需查正文。

## 证据

摘要给出 13.3 小时真机评测：4 个物体、4,800 个未见目标、多种手腕朝向。状态输入策略在位置误差 2 cm、朝向误差 0.4 rad 的门槛内完成 95.2% 的目标；加过滤器后，掉落次数减少 75%，目标完成率为 91.5%。这支持安全与完成率可调的结论，但不能把状态策略数字直接归给相机策略。其他抗扰动和拧灯泡能力仅有定性描述。

## 局限

掉落减少 75% 是相对变化，摘要未给绝对掉落数，也未说明连续目标如何划分试验。我的待核查问题是：视觉输入下是否保留同样收益，以及对新物体、重量和表面摩擦的适用范围；4 个物体不足以代表任意物体。

- **判断**：值得深入读训练配方和真机评测协议，尤其关注过滤器怎样以少量完成率损失换取更少掉落。

## 研究关联

具体启示是：连续操作中，完成多少目标和中途掉落多少次应分开统计。把安全修正作为独立层，还能在不同容错要求下调整行为，而不只得到一个固定策略。

### 下一步读哪里

优先核查抓握数据如何生成、摩擦课程如何调整、系统辨识测了哪些参数，以及状态与相机策略各自的成功率和掉落统计。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarka.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Dexterous manipulation with multi-fingered hands is the next frontier of robotics, yet learned hand skills remain limited to simple grasps or basic repeated motions, such as rotating an object. As robots attempt more demanding in-hand maneuvers, safety, such as not dropping the object, becomes critical, yet it is rarely measured. We study in-hand object pose reaching, a task that demands diverse and difficult grasps: moving an object to almost any position and orientation within reach of the fingers, at any wrist orientation, through long sequences of consecutive goals. We present a recipe for training such policies for a LEAP hand in simulation without human data, built on a range of insights, from diverse resets and goals via generated grasp datasets to an adaptive friction curriculum. With careful system identification, the policies transfer zero-shot to the real hand, using either motion capture or a single wrist-mounted depth camera, and prove remarkably capable and robust. On top of the task policy, we add a learned residual safety filter with adjustable conservativeness, letting us tune the balance between performance and safety and greatly reduce object drops. In 13.3 hours of real-robot evaluation over 4,800 unseen goals across 4 objects and diverse wrist orientations, the state-based policy reaches 95.2% of goals within 2 cm and 0.4 rad, and the filter cuts its drops by 75% while still reaching 91.5% of goals. The policies can also spin a lightbulb held in an arbitrary pose, reach out-of-distribution goals, withstand fast arm motion and perturbations, and, needing only a wrist camera, serve as portable skills such as screwing in a lightbulb. We release the full recipe as a platform for studying performance, reliability, and safety in high-dimensional dexterous systems. Videos and more are available at https://ian-chuang.github.io/dexsafe/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37652v1
- Authors: Ian Chuang, Hiya Shah, Vamsi Chilamkur, Iman Soltani, Claire Tomlin
- Published: 2026-10-27T17:58:20Z
- Age days: 1

</details>
