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
url: "https://arxiv.org/abs/2610.35817v2"
published: "2026-10-26T17:44:34Z"
age_days: 2
score: 29
created: 2026-10-29
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent

> [!summary] 这篇论文到底做了什么（基于摘要）
> ZAP 把“理解要做什么”和“学会怎么动”分开：借用预训练视觉语言模型的理解能力，再通过简单仿真任务训练机器人操作。它通过工具接口控制机器人，训练期间不使用真实机器人数据。

## 问题

机器人既要从场景和指令中辨认目标，又要把意图变成可执行运动。本文要解决的是：能否保留预训练模型的理解能力，只用仿真补上动作能力，并在真实环境和新任务组合中使用。摘要没有具体解释现有 VLA 失败的原因，不能把比较结果直接归因于某种架构缺陷。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“把红杯放到盘子旁”。模型先识别杯子、盘子与目标关系，再通过工具接口发出操作请求，最终让机器人完成摆放；接口如何把请求转成电机运动，摘要未说明。

## 创新点或方法

相对于直接学习视觉到动作的策略，ZAP 让现成视觉语言模型通过简单工具接口控制机器人。摘要提到用预训练的 27B 参数模型启动世界理解和推理，再用仿真任务进行监督微调与 GRPO 训练运动能力。推理时由训练后的模型在工具接口中执行任务。这里有个关键未说明点：27B 模型与文中“小模型”之间是什么关系，以及工具究竟接收位姿、运动原语还是其他命令，不能自行补成蒸馏或底层关节控制。

### 方法如何工作

1. 从预训练模型获得场景和任务理解，为执行提供目标语义。
2. 在简单仿真任务上监督微调，让模型学会通过工具表达操作。
3. 再用 GRPO 优化仿真任务表现；奖励和采样细节摘要未说明。
4. 部署到真实机器人，通过工具执行任务，并测试新的对象、目标和组合。

### 必要术语

- 工具接口：模型调用机器人能力的入口；本文用它连接语言视觉推理与执行。
- GRPO：通过比较成组候选表现来优化策略的强化学习方法；本文用它继续训练仿真操作能力。
- 组合泛化：把学过的能力用于新组合；本文关注新对象、目标和策略下的执行。
- 机器人形态：机器人的结构和可执行动作条件；本文声称能迁移到训练未见形态。

## 证据

摘要报告，训练未观察真实机器人数据时，真机任务成功率达 96.7%，与同一工具接口中的 GPT-6 Astra 持平，高于 MolmoAct2 的 33.3%；速度为 Astra 的 3 倍、成本为其 1/17。另在单臂 Franka 的 RoboLab-120 上达到 55.9%，领先最强 VLA/WAM 基线 4.9 个百分点。两组成绩属于不同评测，不能合并。摘要还称能迁移到未见机器人形态和新对象、目标、策略，但未给对应分项数据。

## 局限

零真实机器人训练数据不等于预训练从未接触真实图像。还需核查工具接口承担了多少规划、感知和控制工作，以及各基线是否获得相同工具；这些条件会明显影响如何理解成功率。

- **判断**：值得读到工具定义和训练数据构造，因为它们决定 ZAP 的能力究竟来自模型学会操作，还是接口已经解决了大部分执行难题。

## 研究关联

值得借鉴的是把仿真预算集中用于“如何执行”，让预训练承担较广的语义理解。如果操作工具能稳定承接模型意图，就有可能用简单训练任务支持更复杂的任务组合。

### 下一步读哪里

优先核查 27B 模型的具体角色、监督数据来源、GRPO 奖励和工具权限。再检查 96.7% 对应的任务集合、速度与成本统计口径，以及未见形态测试是否需要额外适配。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Pretraining Knows What, Simulation Teaches How Compositional Generalization in a.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot via a simple tool harness. We use a pretrained 27B parameter model to bootstrap world understanding and reasoning, followed by supervised fine-tuning and GRPO on simple simulated tasks to teach it how to move the robot. Without observing real-world robot data during training, ZAP reaches 96.7% success on real-world tasks, matching GPT-6 Astra in our harness and outperforming the MolmoAct2 VLA (33.3%), while running 3x faster and 17x cheaper than GPT-6 Astra. Furthermore, ZAP also generalizes to an unseen embodiment as well as new objects, goals and strategies never seen during training. On a single-arm Franka, ZAP reaches 55.9% on RoboLab-120, 4.9 percentage points ahead of the leading VLA/WAM baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.35817v2
- Authors: Benjamin Pikus, Daniel Saunders, Mircea Mironenco, Salman Mohammadi, Mathew Mathew, Sirou Zhu, Divya Makkar, Xuhua Huang, Qinbo Li, Supreeth Narasimhaswamy, Siyuan Cen, Dejia Xu, Shyamal Buch, Thomas Neff
- Published: 2026-10-26T17:44:34Z
- Age days: 2

</details>
