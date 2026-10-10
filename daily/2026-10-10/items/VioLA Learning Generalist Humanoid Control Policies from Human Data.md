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
url: "https://arxiv.org/abs/2610.12435v1"
published: "2026-10-08T17:57:27Z"
age_days: 1
score: 36
created: 2026-10-10
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# VioLA: Learning Generalist Humanoid Control Policies from Human Data

> [!summary] 这篇论文到底做了什么（基于摘要）
> VioLA 让通用人形策略预测身体和手部的运动潜变量，再交给预训练控制器执行。这样人的录像也能被编码成策略要预测的动作标签，缓解机器人示范少、关节控制难的问题。

## 问题

人形机器人跟随指令时，腿、胳膊和手指必须协调，同时保持平衡。直接学习关节命令既复杂，又依赖稀缺的人形机器人示范；摘要指出，现有通用策略部署前通常还要用各任务的遥操作示范微调。人的运动数据很多，但不能直接当成机器人关节命令。

### 用一个例子理解

理解用例（非论文实验）：输入机器人看到的环境与“走到桌旁并抬起右手”；VioLA 输出身体和手部运动潜变量，控制器据此生成可执行动作。模型不必直接决定每个关节的命令；两种潜变量如何协调，摘要未说明。

## 创新点或方法

旧做法让通用模型承担底层关节预测；本文把预测目标换成身体与手部的运动潜变量，具体执行交给预训练控制器。对应编码器把人和机器人的运动映射到相同潜空间，因此人的记录可以成为动作标签。训练时，策略学习从观察和指令预测这些标签；推理时，控制器将预测结果落实到机器人动作。控制器如何训练、如何处理人体与机器人形态差异，摘要未说明。

### 方法如何工作

1. 先准备身体与手部控制器及对应运动编码器，建立从运动表示到机器人执行的通路。
2. 把人类与机器人运动编码到共享潜空间，得到同一种形式的动作标签，使两类数据能共同训练。
3. 用示范训练通用策略预测潜变量，把底层关节协调交给控制器；训练损失未说明。
4. 部署时将策略输出送给控制器执行，在无需任务专属微调的条件下测试指令跟随。

### 必要术语

- 运动潜变量：压缩后的运动表示；本文把它作为通用策略的动作输出。
- 运动编码器：把运动记录转换成潜变量的模型；本文借它给人类示范生成动作标签。
- 预训练控制器：已学会执行某种运动表示的底层策略；本文由它负责把潜变量变成机器人动作。

## 证据

摘要报告训练池为 1.406 亿帧，93.2% 来自人类。真机运动指令任务无需任务专属微调，成功率为 100%，GR00T N1.7 与 Ψ₀ 分别为 16.7% 和 0%；操作任务成功率为 88.6%，同样无需任务专属微调。方法在两个 VLA 和一个世界动作模型骨干上适用，纯人类示范训练的通用策略也能零样本执行真机运动任务。任务数量、试验次数及操作基线结果未给出，不能把上述比例扩展到任意全身任务。

## 局限

没有任务专属微调，不等于整个系统从未使用机器人数据：控制器的训练来源仍需核查。“纯人类示范”结论针对通用策略训练，不能据此推断底层控制器也只用人类数据。摘要未解释失败类型和复杂接触任务覆盖范围。

- **判断**：值得深入读动作编码器与控制器接口，因为能否复用人类数据，取决于这条转换链是否可靠。

## 研究关联

它提示动作标签本身可能决定哪些数据能被利用。如果能找到一种既容纳人的运动、又能由机器人稳定执行的表达，就不必要求每条示范都由同一机器人采集。这里最值得借鉴的是连接数据与执行的中间动作空间。

### 下一步读哪里

核查人和机器人运动如何对齐、潜变量表示多长的运动、控制器用了哪些数据，以及真机测试中指令、场景和试验次数。还应确认各基线是否获得相同观察与控制条件。

- **概念**：视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/VioLA Learning Generalist Humanoid Control Policies from Human Data.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Teaching a humanoid to follow instructions with its whole body runs into two obstacles. Its action space is large and tightly coupled: legs, arms, and fingers must move together while the robot keeps its balance, which makes joint-level actions hard to learn. And humanoid demonstrations are scarce, so current humanoid generalist policies do not follow new instructions out of the box and are fine-tuned on teleoperated demonstrations of each task before deployment. Human demonstrations exist in far larger numbers, but a person's motion is not a robot command. We remove both obstacles by changing what the generalist policy predicts. We introduce VioLA, a generalist humanoid policy that predicts body and hand motion latents instead of joint commands. A pretrained body- and hand-controller execute these latents on the robot. Their corresponding motion encoders map human and robot motion into the same latent spaces. A human recording is therefore labeled in the policy's action space, and the training demonstration pool contains 140.6 million frames, 93.2% of them human. As a result, VioLA follows locomotion instructions on the real robot zero-shot, without task-specific fine-tuning, reaching 100% success where GR00T N1.7 and $Ψ_0$ reach 16.7% and 0%, respectively. It also reaches 88.6% manipulation success without task-specific fine-tuning. The same approach works across two VLA and one world-action model backbones. A generalist policy trained on human demonstrations alone performs locomotion tasks on the real robot zero-shot. Code and checkpoints will be released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12435v1
- Authors: Mert Albaba, Jens Beißwenger, Anna Manasyan, Daniel Marta, Michael J. Black, Wieland Brendel, Andreas Krause, Georg Martius, Martin Riedmiller
- Published: 2026-10-08T17:57:27Z
- Age days: 1

</details>
