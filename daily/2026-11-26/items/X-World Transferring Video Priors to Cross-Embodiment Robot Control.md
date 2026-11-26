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
url: "https://arxiv.org/abs/2611.33914v1"
published: "2026-11-25T07:34:35Z"
age_days: 0
score: 30
created: 2026-11-26
concepts: ["AI 核心知识地图"]
---

# X-World: Transferring Video Priors to Cross-Embodiment Robot Control

> [!summary] 这篇论文到底做了什么（基于摘要）
> X-World 先让预训练视频模型从人和机器人的视频中适应不同视角，再教动作模型把视频特征转换为目标机器人的短段控制指令。执行一段动作时，它可以同时更新下一段。

## 问题

语言指令操控需要机器人根据新观测持续修正动作，但带控制标签的轨迹贵，不容易覆盖各种任务和机器人。人和机器人的视频展示了物体与操作者怎样随时间运动，不过画面本身无法直接给出目标机器人的控制指令，不同平台还可能采用不同的状态和动作表示。论文要解决的是怎样把视频学到的信息接到可闭环执行的控制器上。

### 用一个例子理解

理解用例（非论文实验）。一台双臂机器人收到把盒盖盖上的指令，并看到盒身的位置。视频主干产生当前观测的特征，Q-Former 将其压成动作模型使用的令牌，动作模型输出一小段双臂动作并经平台投影转成控制指令。机器人执行这段动作时，系统可以根据更新后的画面计算下一段，例如为盒盖出现的偏移调整接近方向。

## 创新点或方法

只靠带动作标签的轨迹学习控制，能用的数据受采集成本限制。X-World 先用大量人类和机器人视频适配预训练的视频扩散主干，使它能处理不同视角。随后冻结主干，让 Q-Former 从它的隐藏状态提取少量令牌，交给共享的流匹配动作模型一次预测一段动作。各数据集用自己的投影处理原生状态和动作。中间这阶段只训练动作相关部分，最后再在目标平台上后训练。推理时，异步分块控制让下一次动作更新与当前段执行重叠。摘要没有说明语言如何注入，也没有交代动作块长度。

### 方法如何工作

1. 用人和机器人的视频适配预训练视频主干，让不同视角下的观测能提供可供动作学习使用的特征。
2. 冻结主干，用带动作的数据训练 Q-Former 和共享动作模型，并用各数据集的投影处理状态和动作差异。
3. 在目标平台上后训练，让动作生成进一步适配该机器人的控制条件。
4. 推理时生成短动作段，并在机器人执行当前段时计算下一次更新，减少等待。

### 必要术语

- Q-Former：用查询从较多特征中提取少量令牌的模块。在本文中，它把视频主干的隐藏状态交给动作模型使用。
- 流匹配：学习把随机样本逐渐变成目标样本的生成方法。在本文中，它用于生成一段连续动作。
- 异步动作分块：执行当前动作段时并行计算更新。在本文中，它用于衔接预测与闭环执行。

## 证据

摘要称，X-World 在 LIBERO 和 LIBERO-Plus 的零样本变化条件下表现强，但没有给出分数、基线名称或具体变化类型。真机部分，侧装双臂 UR5e 在六项双臂任务上平均成功率为 81.7%。这一数字对应摘要所述三种真机配置中的一种。摘要还报告推理响应达到 20 Hz，未说明测量口径和端到端延迟。真机成功率支持该配置上的可执行性，视频适配对成功率贡献了多少需要单独对照。

## 局限

零样本变化结果来自 LIBERO-Plus，目标真机则经过后训练。摘要里这两项结果各自对应不同设置，不能据此推断换一台全新机器人即可直接运行。另一个待核查问题是异步更新如何处理新旧动作段的交界，尤其是突然滑动或接触变化时，控制器多久能用上新观测。

- **判断**：值得读到视频适配消融、目标平台数据用量和动作段交接规则，这三处决定了迁移和实时控制各自带来了什么。

## 研究关联

当可用视频比带动作标签的轨迹多时，可以先用视频学习场景怎样随时间变化，把动作标签用在从表征到控制的映射上。跨平台时也可以检查哪些规律能由共享模型学习，哪些差异需要在各平台的状态和动作接口中处理。

### 下一步读哪里

查视频适配阶段用了哪些视角变化，语言和平台状态分别在何处进入模型。看去掉人类视频、去掉主干适配或改变目标平台数据量时的结果，再核对 20 Hz 对应什么更新事件，以及遇到延迟时新旧动作段如何交接。

- **概念**：AI 核心知识地图
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/X-World Transferring Video Priors to Cross-Embodiment Robot Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Language-instructed manipulation requires robust closedloop policies, yet action-labeled robot trajectories are costly and limited in coverage. Human and robot videos provide complementary spatiotemporal priors for crossembodiment control. We propose X-World, which adapts pretrained video diffusion to variable views. A Q-Former compresses hidden states into tokens for a shared flowmatching expert that predicts action chunks. Datasetspecific projections map native states and actions. We adapt the backbone on large-scale robot and human videos, freeze it for action-only pretraining of the Q-Former and action expert, then post-train on the target platform. At inference, X-World responds at 20 Hz and overlaps updates with execution via asynchronous real-time chunking. X-World performs strongly on LIBERO and under zero-shot shifts on LIBERO-Plus. On hardware, it averages 81.7% success across six bimanual tasks on the side-mounted dual-arm UR5e, one of three real-robot configurations presented.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33914v1
- Authors: Chun Gu, Xiaofei Wei, Yiming Chen, Juntong Zhang, Li Zhang
- Published: 2026-11-25T07:34:35Z
- Age days: 0

</details>
