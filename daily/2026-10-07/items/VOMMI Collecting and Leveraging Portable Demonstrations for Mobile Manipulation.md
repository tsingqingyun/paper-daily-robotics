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
url: "https://arxiv.org/abs/2610.08220v1"
published: "2026-10-06T12:10:48Z"
age_days: 0
score: 36
created: 2026-10-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> VOMMI 想让人拿着普通 RGB 相机采集的移动操作演示，直接用于机器人的 VLA 后训练。关键是先修正视觉估计的运动轨迹，再把局部运动信息送入底盘动作分支，减少漂移造成的错误监督。

## 问题

任务同时包含底盘移动和手部操作，演示必须记录走到哪里、怎样接近物体、怎样操作。遥操作需要机器人，专用采集设备又依赖额外传感器；只从 RGB 估计运动虽然便携，却会累积漂移，使学习目标前后不一致。真正瓶颈是低成本采集之后，如何得到足够可靠的运动监督。

### 用一个例子理解

理解用例（非论文实验）：人走到柜子前并拉开抽屉，身体相机记录接近过程，手部相机记录抓握；离线修正移动轨迹后用于训练。机器人执行时结合当前画面与局部运动条件，输出底盘速度和末端动作。

## 创新点或方法

旧做法直接使用视觉里程计轨迹；VOMMI 用同步的身体和手部视角记录全局移动与局部交互，再由 R2-VO 在离线阶段借助稀疏几何锚点修正轨迹。在线阶段提供多个预测跨度的因果局部运动 token，并通过动作组残差适配器只影响底盘分支。这样把运动条件放在最相关的动作通道中。训练只用便携演示；推理使用在线运动条件。锚点如何获得、演示如何转换成完整动作标签，摘要未说明。

### 方法如何工作

1. 同步采集身体与手部 RGB，保留移动背景和局部交互，避免只看见操作却不知道如何接近。
2. 用稀疏几何锚点离线修正视觉运动轨迹，得到更一致的训练监督。
3. 构造多个跨度的因果局部运动 token，为在线策略提供运动信息；具体构造摘要只说明到此。
4. 只向底盘分支加入运动条件，并用便携演示后训练，使移动动作受益于修正后的监督。

### 必要术语

- 视觉里程计：根据连续图像估计相机怎样移动；本文需修正其累积漂移。
- 几何锚点：用于约束轨迹的几何参照；本文用它校正离线运动估计。
- 因果运动 token：编码运动信息的输入单元，不能依赖执行时尚未获得的信息；本文用于在线条件输入。
- 残差适配器：在原有输出路径上学习补充调整；本文只将运动条件接入底盘分支。

## 证据

摘要称每项任务有 500 条便携轨迹，其中 75 条留出用于 RGB-VO 评估，另有 200 条机器人演示作参考。相较机器人演示训练的策略，底盘速度误差低 18.2%，末端平移精度相近。离线重建相对各视角最佳受测基线，身体与手部绝对轨迹误差平均降低 24.6%。三个真机任务上，完整系统比 OpenPI 0.5 平均成功率高 8.3 个百分点。这支持该采集与学习组合在受测任务中有效；任务名称、成功率绝对值和基线训练配置未提供。

## 局限

这里有真机证据，但仅凭摘要不能判断换房间、换采集者或更长导航是否仍有效。我会核查几何锚点的获取成本，以及 18.2% 的误差优势是否在可比数据量和训练预算下成立；这些是待核查条件，不能据此断言作者没有控制。

- **判断**：值得读到轨迹修正和底盘分支消融，因为决定可迁移性的，是监督如何变可靠、运动条件究竟贡献了多少。

## 研究关联

值得借鉴的是：便携采集的价值取决于运动标签是否可靠。遇到人的演示与机器人动作难以直接对应时，可以先修复运动监督，再把辅助信号限制在确实需要它的动作分支；本文不需要人机运动学对应标定，但仍使用了几何锚点。

### 下一步读哪里

先核查 R2-VO 的锚点来源及在线因果性，再看动作标签转换、适配器训练范围，以及去掉轨迹修正或运动条件后的误差与真机成功率。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/VOMMI Collecting and Leveraging Portable Demonstrations for Mobile Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Portable mobile-manipulation demonstrations can help alleviate data scarcity for embodied intelligence, but obtaining reliable, low-cost, and robot-free motion supervision from RGB observations remains challenging. Existing approaches often rely on teleoperation or specialized devices equipped with additional sensing hardware, while directly using estimated visual odometry (VO) trajectories can introduce inconsistencies due to accumulated drift and imperfect motion supervision. We present the Visual-Odometry-Conditioned Mobile Manipulation Interface (VOMMI), a portable demonstration collection and learning framework that connects portable RGB demonstrations to vision-language-action (VLA) post-training through offline trajectory reconstruction and online visual-motion conditioning. VOMMI synchronizes body and hand views to capture navigation context and local object interactions without requiring human-robot kinematic correspondence calibration. R2-VO refines offline demonstration trajectories using sparse geometric anchors and produces causal local-motion tokens over multiple prediction horizons for online policy conditioning. An action-group residual adapter incorporates these tokens only into the base branch. Experiments use a 500-trajectory portable for each task, with 75 trajectories held out for RGB-VO evaluation, and 200 robot demonstrations as references. Our policy, post-trained only on portable demonstrations, achieves 18.2% lower base-velocity error than a policy trained with robot-collected demonstrations, while maintaining comparable end-effector translation accuracy. Offline reconstruction reduces absolute trajectory errors for the body and hand streams by 24.6% on average relative to the best evaluated baseline for each stream. The complete system improves the mean success rate by 8.3 percentage points over OpenPI 0.5 across three real-robot tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.08220v1
- Authors: Yutian Zhang, Xingrui Xiong, Siyuan Ma, Yang Li, Jiawen Wen, Jiaqi Zhai, Liwen Yang, Ce Hao, Haozhen Chi, Yangkun Zhu, Yifan Zhu, Xiaowen Chu, Dong Wei, Qiaojun Yu, Dibo Hou
- Published: 2026-10-06T12:10:48Z
- Age days: 0

</details>
