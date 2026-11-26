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
url: "https://arxiv.org/abs/2611.32967v1"
published: "2026-11-24T17:03:47Z"
age_days: 1
score: 35
created: 2026-11-26
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# VidForce: Predicting Force-Aware Articulation by Observing Humans

> [!summary] 这篇论文到底做了什么（基于摘要）
> VidForce 从第三人称 RGB 视频一起估计物体交互的运动轨迹和用力曲线。它用少量实测力学出可重用的用力原型，再根据画面里的几何和语义线索调整原型，并联合细化轨迹与力。

## 问题

看一个人打开抽屉，视频可以提供抽屉往哪里走的线索，但两次看起来相似的拉动可能需要不同的力。直接测量需要专门设备，可用数据少。这里要解决的是，怎样让有限的实测值帮助模型判断新视频中一次交互需要多大力，以及用力在什么时候变化。

### 用一个例子理解

理解用例（非论文实验）。输入一段侧拍的人拉抽屉的视频，可选点一下把手。系统先跟踪拉动路径，再结合画面线索估计一条可能在抽屉起动时较高、滑动后降低的力曲线。随后联合修正路径和力，最终输出随时间变化的运动轨迹与用力估计。

## 创新点或方法

VidForce 用配对的人类交互录像与带测量装置的夹爪录像，为人类视频提供力监督。模型从这些测量中学习一组原型，复用相近用力水平和时间形状。推理时输入第三人称 RGB 视频，可选附加二维接触点击和物体动作文本。视觉语义线索决定各原型的贡献，几何与视觉语言特征进一步调整这一初始估计。联合条件流再把跟踪得到的初始轨迹和力曲线一起细化。摘要另提到独立训练的扭矩模型，但未交代力原型数量、配对规则或轨迹与力的同步方式。

### 方法如何工作

1. 把人类录像与有实测力的夹爪录像配对，为训练中的人类视频提供力参考。
2. 从实测样本中学习可复用的力水平与时间形状，让相近交互共享监督信息。
3. 对新视频跟踪出初始轨迹，同时用几何和视觉语义线索混合并调整用力原型。
4. 联合细化轨迹与力曲线，得到同一次交互的两个随时间变化的输出。

### 必要术语

- 用力原型：可以复用的典型力水平和时间曲线；在本文中为新视频的力估计提供起点。
- 联合条件流：根据观测条件共同调整一组输出的生成模型；在本文中用于同时细化轨迹和力曲线。
- ATE：概括估计轨迹与参考轨迹位置差异的指标；在本文中衡量运动恢复误差，具体对齐方式需要查正文。

## 证据

摘要称，作者在 Hoi! 数据集的留出交互子集上做基线比较和受控消融，报告轨迹 ATE 为 6.6 cm，峰值力 MAE 为 4.81 N、RMSE 为 5.92 N，整段力曲线 RMSE 为 5.52 N。摘要未列基线名称、分数或消融差值。作者还把预测轨迹和力曲线用于 Spot 的真实关节物体操作，并称做了重复试验，摘要没有给出试验次数或成功率。

## 局限

真机部署说明预测输出进入了实际操作流程。要判断力曲线是否提高了成功率，需要查同一控制器只使用轨迹时的表现。我也会查配对夹爪测得的力在什么条件下能代表视频里人的用力，尤其是阻力相近但操作速度不同的情况。

- **判断**：值得读到配对采集、力原型和真机对照，三处分别决定监督信号代表什么、模型学到了什么、预测是否改善执行。

## 研究关联

昂贵的传感数据可以先用来学习可重复的用力模式，再让便宜的视频数据提供挑选和调整模式的线索。这个做法适合检查一类具体假设：任务间的力曲线确实有共性，而且画面或语义里有足够线索区分这些共性。

### 下一步读哪里

先查夹爪测量怎样与人类录像对应，力的坐标和时间如何对齐。再查留出集是换物体、换人还是换录像，分别去掉原型和联合细化会损失什么，以及 Spot 如何把预测力转换成控制量。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/VidForce Predicting Force-Aware Articulation by Observing Humans.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

People can anticipate how an object moves and the effort an interaction may require by watching others. How can embodied agents acquire this understanding from video? Force measurements provide direct sensory supervision, but require specialized equipment and remain limited in quantity. We introduce VidForce, which estimates an interaction trajectory together with a force profile from a third-person RGB video; 2D contact clicks and textual object-action prompts are optional. Our approach makes limited instrumented measurements useful for interpreting human interactions through learned physical prototypes as a prior. The prototypes share learned force levels and temporal profiles across interactions of comparable effort, with visual and semantic cues determining their contribution to each observation. Geometric and vision-language features adapt this prior to the observed interaction, while a joint conditional flow refines an initial tracked trajectory together with the force profile. Paired human and instrumented-gripper recordings provide measured force references for supervising human video, and a separately trained torque model demonstrates that the formulation extends to other sensory quantities. We evaluate trajectory recovery and force estimation through baseline comparisons and controlled ablations on held-out interactions from the Hoi! dataset. On this evaluation subset, VidForce achieves 6.6 cm ATE, peak-force MAE and RMSE of 4.81 N and 5.92 N, respectively, and force-profile RMSE of 5.52 N. On real-world videos, VidForce infers motion and force reliably and consistently despite the variability in human execution. We further deploy VidForce on a Spot robot, where trajectories and force profiles estimated from human demonstrations drive real-world articulated-object manipulation, and report success rates across repeated trials. Project page: https://rafaymhddn.github.io/vidforce

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.32967v1
- Authors: Rafay Mohiuddin, Jiaqi Chen, Marc Pollefeys, Hermann Blum
- Published: 2026-11-24T17:03:47Z
- Age days: 1

</details>
