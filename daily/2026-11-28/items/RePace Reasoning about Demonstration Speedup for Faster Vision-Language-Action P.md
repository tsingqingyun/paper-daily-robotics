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
url: "https://arxiv.org/abs/2611.34864v1"
published: "2026-11-25T18:30:43Z"
age_days: 2
score: 24
created: 2026-11-28
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> VLA 策略会学到人类示范里的慢节奏。RePace 在微调前逐段比较不同倍率怎样改变观测与动作的配对，选出整段示范的加速方案，让部署时无需另设速度选择模块。

## 问题

人类示范里既有可以快做的移动，也有需要细调的对齐。已有离线加速方法会找出精度要求较低的片段，再赋予预设倍率。问题在于同一片段内的要求也会变：适合直线移动的倍率，到了对齐的一小段可能过高。

### 用一个例子理解

理解用例（非论文实验）｜机器人把杯子放进杯架。输入是任务指令和一条从桌面移动到杯架、最后小幅对齐的示范。比较候选改速后，选速过程可以为大范围移动选较高倍率，并为贴近杯架的对齐窗口保留更多观测和动作。输出是一条改速后的示范，供策略微调。

## 创新点或方法

RePace 把同一段原始运动按多个候选倍率重新计时，计算每个倍率能缩短多少序列，并比较改速得到的观测与动作配对。预训练语言模型结合任务指令、连续窗口的视觉上下文和原始运动，判断这些配对变化会怎样影响示范，进而为整条轨迹选出加速方案。训练时，用改速后的示范微调 VLA。推理时由微调后的策略直接输出动作。观测和动作如何重采样、相邻窗口如何衔接，摘要未说明。

### 方法如何工作

1. 在连续窗口内对同一段示范尝试多个改速倍率，得到可比较的候选。
2. 计算各候选缩短多少序列，并查看改速会形成哪些观测与动作配对，暴露单看时长容易漏掉的局部变化。
3. 让预训练语言模型结合任务指令、画面和原始运动解释这些变化，选出覆盖整个回合的加速方案。
4. 用改速示范微调 VLA，将选速结果写入训练数据，部署时由策略直接产生动作。

### 必要术语

- 重计时：调整同一条示范的运动节奏；这里用于生成不同加速倍率的候选数据。
- 观测与动作配对：训练时让策略从某刻看到的信息学会对应动作的样本；RePace 比较倍率改变后这些样本如何变化。

## 证据

摘要称，RePace 在 LIBERO 和 RoboCasa-Kitchen 的总体任务执行效率上超过所比较的方法。在带夹爪的 Franka Research 3 真机上，摘要报告三项任务的成功率均持平或高于加速基线，并且成功试次耗时更短。摘要未提供基线名称、效率定义、试次数或提升幅度。真机耗时结论对应成功试次，包含失败与重试的总耗时需要另查。

## 局限

两个基准和三项真机任务支持所测条件下的结果。要判断语言模型的作用，可以看同等候选倍率下，简单的局部运动规则是否也能达到类似的成功率和耗时。还要查耗时统计是否覆盖失败或重试，以及设备的动作限幅是否影响实际提速。

- **判断**：值得读重计时后的动作标签如何得到，以及选速模块有没有独立对照。这两处决定方法能否迁移到另一套示范数据。

## 研究关联

加速示范会同时改写训练时看到的输入与目标动作。比较这些新配对，可以在微调前发现局部动作是否跨得过大。这适合部署端不便再加入选速模块、同时任务各阶段精度要求差别明显的场景。

### 下一步读哪里

先查候选倍率如何改变帧、时间戳与动作标签，再查整条示范的速度方案如何处理窗口交界。读实验时对照成功率、成功试次耗时与完整试验耗时，并核查语言模型和候选比较各自的贡献。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：24
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/RePace Reasoning about Demonstration Speedup for Faster Vision-Language-Action P.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Since vision-language-action (VLA) policies can inherit the slow pace of human demonstrations, accelerating these demonstrations before fine-tuning can lead to faster VLA policies without an additional speed-selection module at deployment. Several offline speedup methods have focused on identifying segments that require less precision and assigning predefined speedup factors to the segments. However, even within a single segment, a speedup factor suitable for steady motion may be too high when precise alignment is required. To this end, this paper presents RePace, an offline reasoning framework that determines how much to accelerate each part of a demonstration. For the same recorded movement, RePace measures how much each candidate speedup factor shortens the sequence and compares the resulting observation-action pairs used for training. Given the task instruction, a pretrained language model uses the visual context and original motion of successive windows to interpret these candidate retiming effects and select a speedup profile for the complete episode. Experimental results demonstrate that RePace outperforms the baselines in overall task execution efficiency on both LIBERO and RoboCasa-Kitchen. On all three tasks with a gripper-equipped Franka Research 3 arm, RePace matches or exceeds the acceleration baselines in success rate and completes successful trials faster.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34864v1
- Authors: Insup Lee, Hojin Jeon, Sunguk Shin, Seoungbin Bae, Taekwan Kim, Jinwoo Shin, Dongsu Han
- Published: 2026-11-25T18:30:43Z
- Age days: 2

</details>
