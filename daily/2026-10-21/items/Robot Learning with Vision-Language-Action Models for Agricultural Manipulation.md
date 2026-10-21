---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.26717v1"
published: "2026-10-19T16:49:17Z"
age_days: 1
score: 45
created: 2026-10-21
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Robot Learning with Vision-Language-Action Models for Agricultural Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> 这篇把 Octo 和 π₀.₅ 适配到番茄接近与抓握：先在 MuJoCo 中遥操作收集示范并微调，再用真机示范继续微调。它的重点是跑通农业任务的数据与执行流程，并比较换视角、换布局之后两种策略还能做得怎样。

## 问题

机械臂要在枝叶遮挡、果实位置和植株形状变化下接近并抓住成熟番茄。传统检测、规划、控制流水线会受到定位误差和未建模枝叶影响；通用机器人策略又缺少农业场景经验，而大量真机示范昂贵[S6](https://arxiv.org/html/2610.26717v1#S1.p4.1) [S9](https://arxiv.org/html/2610.26717v1#S1.p8.1)。本文处理的是接近与抓握，不能扩写为完整采摘。

### 用一个例子理解

理解用例（非论文实验）：给机器人两路图像及“抓住成熟番茄”的指令；策略根据远景定位目标、近景调整接近动作，输出一段末端位移与夹爪命令，执行部分动作后重新拍照修正。

## 创新点或方法

相较于为每个场景手工衔接视觉定位和规划，本文用示范训练从双相机图像、语言及可选自身状态到动作的映射。先在多种番茄植株仿真中收集手柄示范，再微调预训练策略，最后用较小真机数据集继续适配[S10](https://arxiv.org/html/2610.26717v1#S1.p9.1) [S29](https://arxiv.org/html/2610.26717v1#S4.p1.1)。推理输出末端运动和夹爪命令，由逆运动学控制器执行。Octo 预测并执行4步；π₀.₅预测10步、执行前5步后重新观察[S32](https://arxiv.org/html/2610.26717v1#S4.SS2.p2.1)。本文直接用π₀.₅低层策略，没有启用其语言子任务生成[S22](https://arxiv.org/html/2610.26717v1#S2.SS4.p3.1)。

### 方法如何工作

1. 在不同植株配置中遥操作接近与抓握，得到图像和专家动作配对，降低真机采集负担。
2. 用仿真示范微调两种预训练策略，使通用动作经验适配番茄任务。
3. 用真机示范继续微调，吸收相机外观与执行系统差异。
4. 部署时从观察生成动作段，经低层控制器执行，再获取新观察形成反馈。

### 必要术语

- 本体感知：机器人自己的位置等状态信息；本文比较提供与不提供这种输入。
- 动作块：一次预测连续多步命令；降低反复推理的频率。
- 逆运动学：把末端目标换成关节运动；连接策略输出与机械臂执行。

## 证据

仿真比较同分布、视角/空间偏移及分布外条件，也比较有无本体状态输入；真机是 FR3 与人工番茄植株，配外部和腕部相机[S25](https://arxiv.org/html/2610.26717v1#S3.SS2.p1.1) [S29](https://arxiv.org/html/2610.26717v1#S4.p1.1) [S30](https://arxiv.org/html/2610.26717v1#S4.F7) [S31](https://arxiv.org/html/2610.26717v1#S4.SS2.p1.1)。摘要报告π₀.₅任务得分更高、分布变化下退化更少，但提供材料未包含得分定义、具体结果、试验次数及误差范围，因此无法量化优势，也无法判断本体状态究竟帮了多少。

## 局限

作者明确把多任务、更丰富真机数据、可变形植物以及力触觉列为后续方向[S33](https://arxiv.org/html/2610.26717v1#S5.p4.1)。真机实验使用人工植株，不能证明真实果实的无损采摘。我的待核查问题是：相同真机数据预算下，加入仿真预适配究竟比直接真机微调好多少；两模型规模和执行设置也不同，性能差异不能只归因于VLA架构。

- **判断**：适合读到数据采集与部署细节；若要据此选择策略或估算仿真收益，必须补看结果表和受控对比。

## 研究关联

可借鉴的是把仿真用于低成本示范和可控扰动，再用真机数据校正外观、延迟和夹爪差异。对接近与抓握这类能保持相似动作接口的任务，这是一条可以逐环节检查的适配路线。

### 下一步读哪里

先用[S14](https://arxiv.org/html/2610.26717v1#S2.SS1.p1.1) [S25](https://arxiv.org/html/2610.26717v1#S3.SS2.p1.1) [S26](https://arxiv.org/html/2610.26717v1#S3.F5) [S27](https://arxiv.org/html/2610.26717v1#S3.SS2.p2.1) [S28](https://arxiv.org/html/2610.26717v1#S3.SS2.p3.1) [S29](https://arxiv.org/html/2610.26717v1#S4.p1.1)确定任务和真实环境边界，再查仿真与真机示范数量、得分规则、本体状态消融，以及仅用真机数据的对照。还应核查抓住之后是否要求保持、是否检查碰撞和损伤。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：45
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.26717v1
- 获取时间：2026-10-21T00:33:48.660358+00:00
- [S1] [Robot Learning with Vision-Language-Action Models for Agricultural Manipulation · 正文段落 1](https://arxiv.org/html/2610.26717v1#abstract1.1)
- [S2] [I INTRODUCTION · 正文段落 2](https://arxiv.org/html/2610.26717v1#S1.p1.1)
- [S3] [I INTRODUCTION · 正文段落 3](https://arxiv.org/html/2610.26717v1#S1.F1)
- [S4] [I INTRODUCTION · 正文段落 4](https://arxiv.org/html/2610.26717v1#S1.p2.1)
- [S5] [I INTRODUCTION · 正文段落 5](https://arxiv.org/html/2610.26717v1#S1.p3.1)
- [S6] [I INTRODUCTION · 正文段落 6](https://arxiv.org/html/2610.26717v1#S1.p4.1)
- [S7] [I INTRODUCTION · 正文段落 7](https://arxiv.org/html/2610.26717v1#S1.p5.1)
- [S8] [I INTRODUCTION · 正文段落 8](https://arxiv.org/html/2610.26717v1#S1.p6.1)
- [S9] [I INTRODUCTION · 正文段落 10](https://arxiv.org/html/2610.26717v1#S1.p8.1)
- [S10] [I INTRODUCTION · 正文段落 11](https://arxiv.org/html/2610.26717v1#S1.p9.1)
- [S11] [I INTRODUCTION · 正文段落 13](https://arxiv.org/html/2610.26717v1#S1.I1.i1)
- [S12] [I INTRODUCTION · 正文段落 14](https://arxiv.org/html/2610.26717v1#S1.I1.i2)
- [S13] [I INTRODUCTION · 正文段落 15](https://arxiv.org/html/2610.26717v1#S1.I1.i3)
- [S14] [II-A Agricultural Manipulation Task Formulation · 正文段落 17](https://arxiv.org/html/2610.26717v1#S2.SS1.p1.1)
- [S15] [II-C Octo Model Architecture · 正文段落 21](https://arxiv.org/html/2610.26717v1#S2.SS3.p1.1)
- [S16] [II-C Octo Model Architecture · 正文段落 22](https://arxiv.org/html/2610.26717v1#S2.SS3.SSS0.Px1.p1.1)
- [S17] [II-C Octo Model Architecture · 正文段落 26](https://arxiv.org/html/2610.26717v1#S2.SS3.SSS0.Px3.p1.1)
- [S18] [II-C Octo Model Architecture · 正文段落 28](https://arxiv.org/html/2610.26717v1#S2.SS3.SSS0.Px3.p2.1)
- [S19] [II-C Octo Model Architecture · 正文段落 30](https://arxiv.org/html/2610.26717v1#S2.SS3.SSS0.Px3.p2.2)
- [S20] [II-D \pi_{0.5} Model Architecture · 正文段落 33](https://arxiv.org/html/2610.26717v1#S2.SS4.p1.1)
- [S21] [II-D \pi_{0.5} Model Architecture · 正文段落 34](https://arxiv.org/html/2610.26717v1#S2.SS4.p2.1)
- [S22] [II-D \pi_{0.5} Model Architecture · 正文段落 35](https://arxiv.org/html/2610.26717v1#S2.SS4.p3.1)
- [S23] [II-D \pi_{0.5} Model Architecture · 正文段落 47](https://arxiv.org/html/2610.26717v1#S2.SS4.SSS0.Px3.p3.1)
- [S24] [III-A Simulation Environment · 正文段落 56](https://arxiv.org/html/2610.26717v1#S3.F3)
- [S25] [III-B Real-Robot Experimental Setup · 正文段落 60](https://arxiv.org/html/2610.26717v1#S3.SS2.p1.1)
- [S26] [III-B Real-Robot Experimental Setup · 正文段落 61](https://arxiv.org/html/2610.26717v1#S3.F5)
- [S27] [III-B Real-Robot Experimental Setup · 正文段落 62](https://arxiv.org/html/2610.26717v1#S3.SS2.p2.1)
- [S28] [III-B Real-Robot Experimental Setup · 正文段落 63](https://arxiv.org/html/2610.26717v1#S3.SS2.p3.1)
- [S29] [IV Fine-Tuning and Evaluation · 正文段落 80](https://arxiv.org/html/2610.26717v1#S4.p1.1)
- [S30] [IV-B Evaluation · 正文段落 90](https://arxiv.org/html/2610.26717v1#S4.F7)
- [S31] [IV-B Evaluation · 正文段落 91](https://arxiv.org/html/2610.26717v1#S4.SS2.p1.1)
- [S32] [IV-B Evaluation · 正文段落 92](https://arxiv.org/html/2610.26717v1#S4.SS2.p2.1)
- [S33] [V Conclusion · 正文段落 111](https://arxiv.org/html/2610.26717v1#S5.p4.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/Robot Learning with Vision-Language-Action Models for Agricultural Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints. Pretrained vision-language-action (VLA) and generalist robot policies offer a promising approach to addressing these challenges by learning manipulation behaviors from multimodal observations and language instructions. However, adapting these policies to agricultural tasks requires domain-specific demonstrations, which are costly and time-consuming to collect on physical robots. In this work, we develop a simulation-to-real robot-learning framework for agricultural reaching and grasping that integrates task-specific demonstration collection and pretrained policy adaptation. A MuJoCo-based agricultural environment is developed with diverse tomato plant structures to support demonstration collection and controlled evaluation. Expert demonstrations are collected through joystick teleoperation, with a low-level controller used to execute robot actions. Two pretrained generalist robot policies, Octo and $π_{0.5}$, are adapted using simulated demonstrations, followed by further fine-tuning on a physical Franka Research 3 manipulator using real-robot demonstrations. The adapted policies are evaluated under in-distribution, viewpoint/spatial-shift, and out-of-distribution conditions in simulation, followed by physical-robot experiments. The influence of proprioceptive information on policy performance is also investigated. Results show that $π_{0.5}$ achieves higher task-performance scores than Octo and exhibits less degradation under distribution shifts. These findings demonstrate the potential of integrating pretrained generalist policies with task-specific demonstration learning for agricultural manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.26717v1
- Authors: Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
- Published: 2026-10-19T16:49:17Z
- Age days: 1

</details>
