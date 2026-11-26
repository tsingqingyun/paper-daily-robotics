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
url: "https://arxiv.org/abs/2611.33398v1"
published: "2026-11-24T20:19:03Z"
age_days: 1
score: 34
created: 2026-11-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> Best-of-N 让机器人从同一个策略多抽几套候选动作，再挑评分最高的一套。论文发现，打分器有误时，候选越多，越可能挑中一套被误打高分的动作。

## 问题

遇到环境变化时，视觉语言动作模型生成的一套动作可能不合适。多抽几套再打分，原本是想在部署时用额外计算找到更好的动作。瓶颈在于分数只是对后果的预测。只要部分动作被高估，取最高分就会偏爱这些误差。此时，候选池里即使有好动作，最终被选中的也可能是打分器最看走眼的一套。

### 用一个例子理解

理解用例（非论文实验）｜机械臂收到把杯子放进托盘的指令，策略生成几条搬运轨迹。打分器误判一条擦过托盘边缘的轨迹更容易成功，于是它被选中。更准确的轨迹复评给出较低分，暴露了最高预测分与动作实际质量之间的差距。

## 创新点或方法

作者固定 π₀.₅ 的动作生成策略，在推理时改变候选数 N，再让带受控误差的 MuJoCo 轨迹验证器选动作。对同一个被选中的候选，比较有误验证器和准确验证器给出的分数，以观察挑最大值会怎样放大误差。整个选择过程发生在部署侧。作者还试了校准打分和按 softmax 概率选择候选，摘要未说明校准的具体做法和概率分布的设置。

### 方法如何工作

1. 给固定的 π₀.₅ 同一个任务输入，从它的动作分布中抽取 N 个候选，控制生成策略不随 N 改动。
2. 用带受控误差的 MuJoCo 验证器给候选打分，按最高预测分选出部署时会采用的动作。
3. 用准确验证器复评同一个候选，对比不同 N 下的分数差异，检查选择过程是否偏向被高估的动作。
4. 改用校准后的打分或 softmax 选择，再观察偏差是否缩小，以检验问题能否从选择环节缓解。

### 必要术语

- Best-of-N：抽 N 个候选后按分数挑一个；本文改变 N 来观察增加推理采样量的效果。
- 验证器：预测候选轨迹好坏并给分的组件；本文用有误版本负责选择，用准确版本作评分参照。
- 奖励投机：选择过程推高了代理分数，但参照分数没有同步改善；本文观察的是候选筛选造成的这种偏差。

## 证据

摘要报告，实验覆盖 60 个 LIBERO-Safety 任务级案例，每例重复 10 次。主要比较是不同 N 下，被选候选在有误验证器与准确验证器上的奖励差异。N 增大后，两边的奖励出现偏离。校准和 softmax 选择在部分设置下缓解了问题。摘要未给出 N 的取值、奖励差距的幅度或对应的任务成功率变化，因此可以确认所测设置中的评分偏离，无法量化实际成功率损失。

## 局限

受控注入误差让实验能考察该误差设置对候选选择的影响，结论直接覆盖的是仿真中的验证器和参考奖励。值得核查的是，真实部署中的误差是否也会集中在被挑中的高分候选上，以及这种偏差能否预测实际执行失败。

- **判断**：优先读误差如何注入和两种评分如何比较，它们决定了这篇结论对你所用打分器有多大参考价值。

## 研究关联

评估多采样是否划算时，值得把候选池里有没有好动作和打分器最终挑到了什么分开看。若候选池确实变好，选中的动作却在独立复评中变差，问题就集中在排序环节。只看被选动作的最高预测分，会漏掉这类失败。

### 下一步读哪里

查误差加在评分过程的哪里，是否随动作类型变化，以及准确验证器依据什么评分。接着看不同 N 下预测分和参考分如何变化，再查校准和 softmax 在哪些误差条件下有效。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Act.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have shown promise for general-purpose robotic manipulation, but adapting to changing environmental conditions still remains challenging. Recent test-time steering methods have shown promise in enabling adaptive VLA policies by utilizing additional computation during deployment. In this paper, we consider best-of-$N$ test-time steering for VLA models, where multiple action candidates are sampled from a fixed policy and a verifier is used to select the best one during deployment. We show that increasing $N$ does not always improve performance when the verifier is inaccurate, and can favor candidates whose scores exploit prediction errors, a form of reward hacking. We study this effect on 60 LIBERO-Safety task-level cases using a $π_{0.5}$ policy, with ten repetitions per case. We introduce controlled errors in a MuJoCo trajectory verifier and show that as $N$ increases, selected candidate rewards diverge from the accurate verifier rewards, leading to reward hacking. We also show that verifier calibration and softmax-based candidate selection can mitigate reward hacking in some settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33398v1
- Authors: Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ming Jin, Ye Wang
- Published: 2026-11-24T20:19:03Z
- Age days: 1

</details>
