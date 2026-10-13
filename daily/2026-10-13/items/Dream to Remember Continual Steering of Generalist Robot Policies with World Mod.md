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
url: "https://arxiv.org/abs/2610.13816v1"
published: "2026-10-09T16:28:01Z"
age_days: 3
score: 32
created: 2026-10-13
concepts: ["世界模型", "机器人学习"]
---

# Dream to Remember: Continual Steering of Generalist Robot Policies with World Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> Dream to Remember（D2R）冻结通用机器人策略，只训练一个引导它生成动作的小模块；学新任务时，用冻结的世界模型模拟旧任务来复习。世界模型足够准确时，新任务也能在模拟想象中学，否则新任务在环境中学、旧任务仍靠想象复习。

## 问题

任务按顺序到来，机器人既要改进新任务，又要保住先前技能。直接微调策略会遗忘；冻结策略、只训练共享引导模块，也会让遗忘转移到模块上。瓶颈是更新共享参数时缺少维持旧行为的训练信号，冻结主策略本身并不能解决。

### 用一个例子理解

理解用例（非论文实验）：机器人已有开抽屉技能，现在输入关抽屉任务；训练时更新引导模块，同时让世界模型生成开抽屉的旧任务经验来复习。训练后，新指令经引导模块影响冻结策略的动作生成，目标是学会关闭且保住打开技能。

## 创新点或方法

已有引导方法通过调整冻结生成策略的输入噪声来改变动作；D2R 保留这个思路，新增旧任务的想象回放。在训练新任务的同时，冻结世界模型生成旧任务轨迹，把引导模块约束在先前行为附近，无需回放缓存或新增旧任务数据。世界模型若能可靠支持策略优化，新任务也在其中学习；否则使用环境学习新任务。推理依靠引导模块和冻结策略，摘要未说明世界模型是否参与部署。

### 方法如何工作

1. 冻结通用生成策略与预训练世界模型，只更新引导输入噪声的模块，减少需要调整的参数。
2. 为新任务提供学习经验：模型可靠时用想象轨迹，否则从环境取得经验。
3. 同时由世界模型生成旧任务的想象轨迹，用旧行为约束模块，抵消新任务更新造成的遗忘。
4. 持续加入任务并测试新旧任务表现，区分学得更好与保留得更好；约束公式摘要未说明。

### 必要术语

- 引导模块：调节生成策略输入噪声的小模型；本文用它改变冻结策略的行为。
- 想象轨迹：世界模型预测的一连串状态变化；本文用于学习或复习。
- 灾难性遗忘：学新任务后旧任务能力大幅下降；本文要在连续更新中抑制它。

## 证据

摘要报告：CALVIN 仿真中连续改进八个任务，完全通过想象训练，平均成功率从 63.7% 到 74.8%；同一任务序列的 LoRA 微调降至 11.7%。在 LIBERO 中，π₀ 与 A2World 的组合从环境学习未见 LIBERO-90 任务，同时保持原已微调套件表现，未给数值。真机 Franka 上连续改进三个任务并保留先前改进，也未给成功率。证据分别支持仿真定量效果和有限真机可行性。

## 局限

作者明确把完全想象学习限定在模型足够忠实的条件下。我的待核查问题是如何判定这个条件、想象误差是否随任务累积，以及真机三个任务覆盖了什么难度。有限任务上的保留不能保证长期增加技能仍不遗忘。

- **判断**：值得读到旧任务回放约束和两种训练模式的切换条件，因为它给世界模型提供了一个比全程替代真实环境更具体的用途。

## 研究关联

最有启发的是世界模型可以承担两种难度不同的工作：找到更好的新行为，或提供足以维持旧行为的复习经验。LIBERO 的摘要结果说明，一个不足以支撑新任务优化的模型，仍可能用于保留技能；评估世界模型时因此应区分用途。

### 下一步读哪里

核查旧任务如何初始化、旧行为如何保存或作为约束目标、回放与新任务更新的比例；再看 CALVIN 各任务遗忘曲线、LIBERO 保留指标和 Franka 的逐次结果。

- **概念**：世界模型 机器人学习
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/Dream to Remember Continual Steering of Generalist Robot Policies with World Mod.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations. Reinforcement learning can improve and extend them, either by fine-tuning the policy weights or by training a small module to steer the input noise of a frozen generative policy. When tasks arrive sequentially, both approaches suffer from catastrophic forgetting. Fine-tuning on a task degrades prior tasks, and steering only shifts forgetting to the shared steering module. We propose Dream to Remember (D2R), which continually steers a frozen generalist policy toward new tasks, while retaining its earlier skills. As the steering module learns a new task, a frozen pretrained world model rehearses prior tasks through imagined rollouts, anchoring the module to its earlier behavior without a replay buffer or new data. When the world model is faithful enough, D2R learns the new task entirely in imagination. Otherwise, it learns the task in the environment while using the world model only to rehearse prior tasks. On CALVIN, D2R improves eight tasks in sequence entirely in imagination, raising average success from 63.7% to 74.8%, while LoRA fine-tuning on the same sequence drops it to 11.7%. With a frozen off-the-shelf generalist policy and world model, $π_0$ and A2World, D2R learns unseen LIBERO-90 tasks in the environment while keeping $π_0$'s performance on the LIBERO suites it was fine-tuned on, even though the world model is not accurate enough for policy optimization. Finally, on a real Franka robot, D2R improves three tasks in sequence entirely in imagination while retaining the earlier improvements.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.13816v1
- Authors: Bahey Tharwat, Iman Nematollahi, Marvin Alles, Xingyuan Zhang, Akshay L Chandra, Abhinav Valada
- Published: 2026-10-09T16:28:01Z
- Age days: 3

</details>
