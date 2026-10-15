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
url: "https://arxiv.org/abs/2606.02745"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 42
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos

> [!summary] 这篇论文到底做了什么（基于摘要）
> SeeTraceAct 让机器人看一次示范视频后执行新任务，重点解决“小目标到底在哪里”的问题。它通过考虑可见性的未来末端轨迹预测，让动作学习更明确地关注操作位置。

## 问题

任务是用一个未见任务的示范视频来指导机器人，减少逐任务收集遥操作数据的成本。摘要指出，已有端到端方法在需要准确定位小目标区域时容易失败；理解大致动作还不够，手必须到达正确的小区域。示范者与执行机器人形态不同，又增加了迁移难度。

### 用一个例子理解

理解用例（非论文实验）：输入一段人按下咖啡机小按钮的视频和机器人当前画面；模型结合示范预测夹爪接近按钮的路径，再生成执行动作，输出一次按压操作。

## 创新点或方法

旧方法直接学习从示范和观测到动作的映射；SeeTraceAct 加入考虑可见性的未来末端轨迹预测，用更明确的空间目标约束动作学习。训练侧因此不只关注最终动作，也关注末端将经过哪里；轨迹监督的来源、可见性处理方式和损失权重未说明。推理侧以单段示范为条件执行，但轨迹是否作为独立中间结果显式传给动作模块，摘要没有交代，不能据标题补出潜在规划结构。

### 方法如何工作

1. 输入单段示范和当前观测，为未见任务提供动作意图及场景线索。
2. 通过考虑可见性的未来末端轨迹预测，把学习重点引向准确的操作位置。
3. 将这种空间约束用于 demo-conditioned VLA，使其生成机器人动作；具体连接方式摘要只说明到此。
4. 在跨形态示范条件下执行并统计成功率，检验空间约束是否能帮助完成任务。

### 必要术语

- 示范条件策略：执行时把示范作为输入的策略；本文用单个视频说明新任务。
- 跨形态示范：示范者和执行者身体不同；本文包含人形机器人或人类示范。
- 末端轨迹：夹爪等操作部位随时间经过的位置；本文用它提供空间约束。
- 可见性感知：预测时考虑目标是否能被观察到；具体处理机制摘要未说明。

## 证据

摘要报告两类评测：RoboCasa-DC 仿真中，机器人轨迹配有新采集的人形机器人示范；真机中，Franka Panda 根据人类示范执行。SeeTraceAct 在 RoboCasa-DC 四种设置中均取得最高成功率，真机平均成功率提高 9.5 个百分点。摘要没有列出四种设置、基线名称、绝对成功率和重复次数，因此支持跨形态示范条件下的整体优势，但不足以判断小目标定位贡献了多少收益。

## 局限

我会核查遮挡时模型怎样处理轨迹，以及相机视角变化是否削弱定位。跨形态评测说明测试包含不同身体，但不能据此推断它对任意机器人、任意视角都有效。

- **判断**：值得读轨迹表示和可见性消融，因为它们决定这项方法提供了怎样的空间监督。

## 研究关联

这里可借鉴的是：示范传递的不只是任务语义，还应包含可操作的空间约束。若失败集中在“知道做什么，却落错位置”，让模型预测手的未来路径，比只增加任务描述更值得检查。

### 下一步读哪里

下一步核查轨迹使用二维还是三维坐标、如何对应不同身体、不可见部分如何监督，以及四种设置是否分别控制任务新颖性和示范形态。还需看定位误差与任务成功率是否同时改善。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/SeeTraceAct Visibility-Aware Latent Planning from Cross-Embodiment Demonstration.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.02745v2 Announce Type: replace Abstract: Vision-language-action models (VLAs) are promising general-purpose robot policies, but adapting them to new tasks typically requires costly task-specific teleoperation data. As an alternative, we study one-shot demo-conditioned VLAs, where a robot policy is conditioned on a single demonstration video of an unseen task. We find that existing end-to-end approaches often struggle when successful execution requires precisely localizing small target regions. To address this limitation, we propose SeeTraceAct, a demo-conditioned VLA framework that encourages precise spatial grounding through visibility-aware prediction of future end-effector traces. To enable reproducible evaluation with cross-embodiment demonstrations, we introduce and release RoboCasa-DC, a demo-conditioned extension of RoboCasa that pairs its robot trajectories with newly collected humanoid demonstrations. Experiments on RoboCasa-DC and a real-world benchmark, where a Franka Panda arm is conditioned on human demonstrations, show that SeeTraceAct outperforms baselines, achieving the best success rate across all four RoboCasa-DC settings and improving real-world average success by 9.5 percentage points.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.02745
- Authors: Jaehyeon Son, Junhyun Kim, Kyle Kam, Jeremiah Coholich, Seok Joon Kim, Jinhoo Kim, Chris Dongjoo Kim, Jaemin Cho, Dieter Fox, Zsolt Kira
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
