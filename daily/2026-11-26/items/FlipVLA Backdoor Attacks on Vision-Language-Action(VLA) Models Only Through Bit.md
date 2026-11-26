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
url: "https://arxiv.org/abs/2611.33810v1"
published: "2026-11-25T05:40:30Z"
age_days: 0
score: 33
created: 2026-11-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips

> [!summary] 这篇论文到底做了什么（基于摘要）
> FlipVLA 研究权重被持久篡改后，机器人是否会只在看到特定物体时明显改变动作。摘要报告，两种受测模型在常规场景中仍大致保持成功率，但触发场景中的攻击成功率很高。

## 问题

机器人上线前可能用一组常规场景检查抓取和放置是否正常。如果权重完整性已被破坏，而异常只在特定视觉条件下出现，这组测试就可能看不到变化。论文要检验的具体问题是，少量固定的参数位变化能否在无需重新训练的情况下留下持久后门，同时让无触发场景中的任务表现基本维持。

### 用一个例子理解

理解用例（非论文实验）｜验收一台把量杯放到托盘上的机器人。保持指令和杯子位置相同，只在背景中加入一个无关物体，再比较两次末端轨迹和放置结果。如果动作只在加入该物体后改变，这个差异就值得与可信模型副本复测。

## 创新点或方法

FlipVLA 的选择器和放大器分别对应两个作用：让模型内部的变化主要随触发物出现，以及让这种变化足以影响动作输出。实验先在准备阶段改动固定权重，再在推理阶段用有触发物和无触发物的场景观察模型行为。这样可以检验异常是否集中在特定输入条件下，以及常规任务成绩能否反映变化。

### 方法如何工作

1. 把触发物是否出现设为测试条件，比较同类任务在两种输入下的行为。
2. 在部署前使用固定修改后的模型开展实验，检验行为变化能否随权重持续到后续推理。
3. 分别统计触发场景的攻击成功率和常规场景的任务成功率，检查异常是否会被常规表现掩盖。

### 必要术语

- 物体触发后门：特定物体出现时才显著改变模型行为的条件性异常；本文用它检验常规场景测试可能漏掉什么。
- 参数比特翻转：改变权重数字在存储表示中的某一位；本文把这种持久变化作为威胁条件。

## 证据

摘要报告，实验在 OpenVLA-OFT、GR00T N1.7 和 4 套 LIBERO 任务上进行。触发场景的攻击成功率为 90.22% 至 100%，无触发场景的任务成功率相对原表现最多下降 1.5 个百分点。这两个指标衡量不同结果。摘要未给出比特修改预算、攻击成功的具体判定、逐模型和逐套件结果，也未报告真机证据。

## 局限

现有数字支持所测基准中的输入条件与异常行为差异。值得核查的是，触发物改变后，正常场景难度是否也随之改变，以及结果能否跨场景布局和视角复现。真实机器人上的接触、运动约束和安全停机还会影响异常动作的实际后果。

- **判断**：值得读到威胁假设、成功判据和有无触发物的对照设计，重点判断常规回归测试在哪些条件下会漏报。

## 研究关联

如果部署验收只看正常输入下的任务成功率，就可能漏过有条件的异常。权重来源和完整性验证能回答模型文件有没有变化，成对的场景测试能回答一种视觉变化是否伴随动作变化。这两种证据解决的是不同问题。

### 下一步读哪里

先核查实验假设对手具有什么权重访问权限、怎样定义攻击成功和正常任务成功。再看有无触发物的案例是否成对、原始权重下有无相同视觉变化的对照，以及各模型和任务套件的结果如何分布。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/FlipVLA Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models generate robot actions from visual observations and language instructions in real-world environments, making malicious model tampering a potential threat to physical safety. We study whether object-triggered backdoors can be implanted through a small, fixed set of parameter bit flips without retraining. The central challenge is to make persistent weight modifications disrupt trigger-present behavior while preserving performance on non-trigger inputs. We propose FlipVLA, a two-stage selector-amplifier method that exploits existing visual features within an FC-GELU-FC structure. The selector constructs a trigger-dependent response in a selected channel, using GELU to attenuate background activity. The amplifier modifies a connected downstream weight to convert this response into an action-relevant perturbation. Channel screening and discrete bit search construct both components under a limited modification budget. Experiments on OpenVLA-OFT and GR00T N1.7 across four LIBERO suites achieve attack success rates of 90.22% to 100%, with task success decreasing by at most 1.5 percentage points on clean scenes.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33810v1
- Authors: Zexi Zhao, Zizhen Liu, Jing Justin Ye, Huawei Li
- Published: 2026-11-25T05:40:30Z
- Age days: 0

</details>
