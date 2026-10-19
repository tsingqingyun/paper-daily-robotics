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
url: "https://arxiv.org/abs/2610.22556v1"
published: "2026-10-15T18:49:42Z"
age_days: 3
score: 29
created: 2026-10-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> RePlanMem-VLA 让机器人根据“自己突然改了多少计划”决定何时保存画面。它比较两次预测中指向同一未来时刻的动作，分歧异常大时触发记忆写入，让后续决策还能看到已经离开视野的关键信息。

## 问题

长任务中的机器人可能先看到线索，过几步才用到；只看当前画面会忘，保存全部历史又贵且重复。难点是在线判断哪一帧值得留下，而不是单纯增加记忆容量。

### 用一个例子理解

理解用例（非论文实验）：机器人先看到盒内标签，随后转身取物。若标签出现使重叠时刻的动作预测明显改变，系统保存该画面；标签离开视野后，策略可在后续选择物品时读取它。若预测未明显变化，这个机制也可能不保存。

## 创新点或方法

旧做法面对全历史的成本，需要选择性保存；本文把策略重新规划的变化当作筛选依据。机器人每次预测一段动作，相邻两段会覆盖部分相同的未来时刻；对齐后比较，才能避免把正常的时间推进误判为计划变化。分歧大被视为任务事件，再经过屏蔽机器人自身区域的写入过滤，减少重复帧，更新容量有限的记忆。训练侧先在从头训练的两类策略上筛选分歧指标，再在预训练策略上验证；执行侧在线检测和写入。摘要未说明记忆怎样接入动作策略、是否还需额外训练。

### 方法如何工作

1. 连续预测动作块，找出覆盖同一未来时刻的部分，得到可公平比较的动作预测。
2. 计算对齐预测的分歧，识别异常大的计划修订，把它作为候选事件。
3. 用屏蔽机器人自身区域的过滤规则压低重复写入，再更新有限记忆；具体过滤公式摘要未说明。
4. 保留关键观察供后续决策使用；记忆读取和策略接入方式，摘要只说明到此。

### 必要术语

- 动作块：一次预测未来一段动作；相邻动作块的重叠部分提供比较对象。
- 滚动执行：执行部分计划后重新预测；本文利用由此产生的计划修订。
- ROC-AUC：概括检测器跨阈值区分事件的能力；不代表机器人任务成功率。

## 证据

摘要报告：先比较 35 种分歧度量，涉及自回归解码器和 Flow-Matching Transformer；再在 MIKASA-Robo-VLA 任务上用 OpenVLA-OFT、π₀.₅ 验证，检测 ROC-AUC 为 0.981–0.997。在所测记忆保留实验中，100% 回合把任务相关观察留到了后续决策点。真机回放数据还支持事件选择和去冗余能延伸到仿真之外。但摘要没有给出回合数、端到端任务成功率或完整记忆基线；保留成功不能直接等同于操作成功。

## 局限

我会核查：动作预测本身的随机性、遮挡或控制误差是否也会触发大分歧；安静出现却很重要的线索是否会漏掉。摘要中的真机证据是回放数据，不能据此认定带记忆的策略已完成真机闭环任务。

- **判断**：值得读到时间对齐、触发阈值和记忆消融实验，因为最有用的想法是把已有预测变成写入信号，而可靠性取决于这个信号究竟捕捉了什么。

## 研究关联

值得借鉴的是：选择记忆不一定要另训一个视觉重要性分类器，也可以利用策略已经算出的预测变化。前提是策略会重复预测重叠时段，而且这种变化确实与需要记住的事件相关。

### 下一步读哪里

先核查两次动作预测如何对齐、最终选中了哪些分歧度量；再看事件标签、阈值和记忆容量怎样设定。最后检查保留率是否转化成任务成功率，以及机器人区域过滤的独立贡献。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/When Plans Change, Remember Replanning-Guided Visual Memory for Vision-Language-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon, multi-stage Vision-Language-Action (VLA) policies often require visual information that is no longer present in the current observation. Retaining the complete observation history is computationally expensive and highly redundant, motivating selective visual memory. We introduce RePlanMem-VLA (Replanning-Guided Keyframe Memory for VLA), which turns a policy's own plan revisions into an online memory-write signal. Under receding-horizon execution, consecutive action chunks predict some of the same future actions. RePlanMem-VLA treats unusually large disagreement between these temporally aligned predictions as evidence of a task-relevant event. We first compare 35 disagreement measures across single-task autoregressive decoder-only and Flow-Matching Transformers trained from scratch, then validate the selected signals on pretrained OpenVLA-OFT and $π_{0.5}$ policies over MIKASA-Robo-VLA tasks. The resulting detectors achieve ROC-AUC of 0.981-0.997. We then use the selected signals in RePlanMem-VLA to trigger updates to a bounded visual memory, with a robot-masked write filter suppressing redundant frames. In the evaluated memory-retention experiments, RePlanMem-VLA preserves task-relevant observations until the later decision point in 100% of episodes. Real-robot replay data further show that event selection and redundancy suppression extend beyond simulation. These results establish plan revision as a policy-internal signal for controlling what a VLA remembers. Website: https://vika787.github.io/RePlanMem/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22556v1
- Authors: Victoria Smelova, Daniil Kazachkov, Georgiy Kazantsev, Iuliia Tsvetkova, Egor Cherepanov, Nikita Kachaev, Artem Latyshev, Aleksandr I. Panov, Alexey K. Kovalev
- Published: 2026-10-15T18:49:42Z
- Age days: 3

</details>
