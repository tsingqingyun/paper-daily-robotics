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
url: "https://arxiv.org/abs/2610.41330v1"
published: "2026-10-30T06:45:17Z"
age_days: 3
score: 27
created: 2026-11-03
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics

> [!summary] 这篇论文到底做了什么（基于摘要）
> Hourglass 把避障规划拆成“这个机器人执行指令后，相机会怎么动”和“相机这样移动后，会看到什么”。不同机器人共享后半部分，只用各自的动力学描述连接控制指令与相机运动，再训练一个知道机身参数的通用策略。

## 问题

杂乱环境中的可行动作取决于机身几何和动力学，统一归一化指令会忽略这些差异，逐机器人训练又难以共享经验。直接按指令预测的世界模型被绑定到特定动作空间；按位姿预测虽可共享，却缺少从具体控制指令到运动的映射。

### 用一个例子理解

理解用例（非论文实验）：输入走廊图像、目标和一台转向较慢机器人的参数；动力学预测候选指令造成的相机运动，世界模型预测相应视野变化；策略据此输出提前转弯的指令。

## 创新点或方法

本文在平地假设下，以相机自运动作为接口：共享世界模型预测环境观测，每台机器人的可微简化动力学把指令转换为相机运动。训练时先用跨机身、跨相机安装位置的数据学习世界模型，再辨识各机身物理参数；策略在想象展开中依次经过动力学和世界模型，学习按参数行动。推理使用通用策略，无需在线地图；摘要未说明是否仍做在线想象或优化。

### 方法如何工作

1. 汇集不同机身与相机安装位置的数据训练共享世界模型，使环境预测围绕相机运动组织。
2. 为各机器人建立简化动力学并辨识参数，得到控制指令到相机运动的映射。
3. 训练时先展开机身动力学，再展开世界模型，让策略看到同一指令在不同机身上的后果。
4. 将机身参数输入通用策略，生成适合该机器人执行的指令，并在仿真与新真机上检验迁移。

### 必要术语

- 相机自运动：相机自身的位置和朝向变化；本文用它连接控制与视觉预测。
- 可微机身动力学：能传递梯度的指令到运动模型；用于在想象训练中体现机身差异。
- 参数条件化策略：根据机器人参数调整动作的策略；使同一策略适配不同动力学。
- MPPI：通过采样候选控制序列进行规划的方法；本文以其参数条件化版本作为教师。

## 证据

摘要报告，在五类运动方式的七种仿真机器人上，相同世界模型下，通用策略成功率比模仿学习和扩散策略基线高 3.8—10.6 个百分点，达到逐机器人专用策略水平，距参数条件化 MPPI 教师差 1.4—2.8 个百分点。对训练未见的真机滑移转向机器人，经过三分钟遥操作进行参数辨识后，合成数据训练模型零样本迁移到未见室内场景。真机成功率、回合数和碰撞指标未给出，不能把仿真差值套到真机。

## 局限

平地是方法论证的重要条件；坡面、颠簸或姿态变化是否仍适用，需要核查。真机“零样本”也包含三分钟参数辨识，并非完全不接触新机器人。简化动力学能否覆盖打滑及复杂接触，是影响迁移可靠性的待查问题。

- **判断**：值得深入读接口定义和动力学辨识，它提供了清楚的共享机制，但适用范围要围绕地面与模型误差判断。

## 研究关联

值得借鉴的是在共享模型与机身差异之间寻找可计算的物理接口。若机器人差异能被低维动力学较好描述，就可能共享环境预测，只为新机身辨识少量参数，而不必重新学习全部观测与控制关系。

### 下一步读哪里

先核查相机自运动接口包含哪些量、机身碰撞几何怎样进入规划，再看动力学参数误差与相机安装变化的实验。真机部分应确认辨识流程、路线难度及失败统计。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Diff.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Motion planning in clutter is embodiment-specific: the feasible free space and reachable commands depend on each robot's geometry and dynamics. Existing cross-embodiment policies output normalized commands that disregard these differences, or compensate through per-robot training and distillation. World models can in principle pool cross-embodiment data, yet command-conditioned models bind their latent dynamics to a single action space, while pose-conditioned models omit the mapping from commands to body-specific motion. On flat ground, however, embodiment affects the planner's observations only through the camera ego-motion. This letter proposes Hourglass, an hourglass-shaped architecture that factorizes cross-embodiment motion planning at this interface: a body-agnostic world model and each robot's differentiable ego-dynamics, which map commands to that ego-motion, are coupled only through it. The world model is trained on data pooled across embodiments and camera mounts; each robot's ego-dynamics is a reduced-order template with identified physical parameters. A generalist parameter-conditioned policy is learned once at this junction: each imagined step rolls out the template and then the world model, and imagination training through each robot's template makes the policy body-aware. On seven simulated robots of five locomotion types, the generalist policy outperforms imitation-learning and diffusion-policy baselines on the same world model by 3.8--10.6 percentage points in success rate and matches per-robot specialists without dedicated training, while approaching its parameter-conditioned MPPI teacher within 1.4--2.8 points without an online map. After three minutes of teleoperated driving for identification, the synthetic-data-trained model transfers zero-shot to a real skid-steer robot unseen in training, navigating unseen indoor scenes.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.41330v1
- Authors: Zhidong Wang, Zirui Li, Haoran Xu, Yujie Yan, Zitong Shan, Jingsong Liang, Han Yu, Chen Lv
- Published: 2026-10-30T06:45:17Z
- Age days: 3

</details>
