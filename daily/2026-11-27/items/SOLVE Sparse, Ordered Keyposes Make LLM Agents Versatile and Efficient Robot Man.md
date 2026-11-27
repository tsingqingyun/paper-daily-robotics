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
url: "https://arxiv.org/abs/2611.34750v1"
published: "2026-11-25T17:25:17Z"
age_days: 1
score: 33
created: 2026-11-27
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator

> [!summary] 这篇论文到底做了什么（基于摘要）
> SOLVE 让多模态大模型一次写出一串有序的机械臂末端关键位姿，中间动作交给运动规划器补齐。走远路时可以少写几个点，到了需要精确对齐的地方再加密，执行一段后重新观察。

## 问题

任务是让机器人根据视觉和指令操作物体。逐步控制的智能体频繁调用大模型，连远距离移动中那些变化平缓的小步也要逐步决定。工具同样会成为瓶颈，但摘要没有细分各类工具调用的开销。

### 用一个例子理解

理解用例（非论文实验）：输入一张桌面图和“把杯子放到杯垫上”。模型查询杯把和杯垫附近的深度，在抓取处安排较密的位姿，在跨桌搬运时只给少量中间目标。规划器让机械臂依次执行，模型再根据新画面判断是否要补一次对齐，最终输出一段段放杯动作。

## 创新点或方法

SOLVE 把大模型的输出从密集动作改成少量按顺序排列的末端位置和朝向。模型自己决定写几个点、隔多远，再由运动规划器生成点间动作。它只在少数位置查询深度，可用多视角三角测量、双目或单目深度，查询有噪声时依靠执行反馈继续调整，具体容错逻辑未说明。策略免训练，执行后还可以反思整次尝试，为当前任务总结几条规则，供后续尝试使用。

### 方法如何工作

1. 读取任务与视觉观测，把关键位置的深度查询结果转成可供定位的空间信息。
2. 输出一串按序排列的末端位姿，按动作所需的精度决定序列的疏密。
3. 让运动规划器补齐位姿之间的动作，使机械臂能连续执行这一段。
4. 观察执行结果，再生成下一串位姿。回合结束后可总结任务规则，供后续尝试复用。

### 必要术语

- 六自由度末端位姿：机械臂末端在空间中的位置和朝向；SOLVE 用它写出每段动作要经过的目标。
- 运动规划器：把目标位姿转成机器人可执行的中间运动；它承担大模型省略的逐步控制。

## 证据

摘要报告 RoboDojo 和 RoboLab 的成绩分别为 74.5% 和 84.5%，称两项均达到当时最佳。平均每回合花费 1.7 美元，约为此前密集控制智能体策略的十二分之一。真机上，同一智能体在 16 项零样本任务中完成 75/85 个回合，成功率为 88%。摘要还称 DROID 中多数示范能压缩成少量关键位姿。所给材料未交代两个基准的环境类型、具体对手分数和成本核算口径，也未量化压缩后的动作误差。

## 局限

作者明确指出深度查询可能有噪声。真机成功率说明整套方法在所测任务中可用，但我会核查关键位姿、深度反馈和事后规则各自贡献多少，尤其是接触后误差难以挽回时，重新观察能否赶上纠错。

- **判断**：值得读到关键位姿的生成、执行后纠错和成本对比，这三处最能说明它在哪类操作上能减少调用。

## 研究关联

如果一项操作的大段移动都能由规划器接手，可以先把昂贵推理留给选择目标、对齐和纠错。这个做法能否省钱，取决于一次调用能覆盖多长的可靠动作，而关键位姿的间距可以随操作阶段改变。

### 下一步读哪里

先查模型在什么时机获得新观测，接触阶段由谁决定夹爪动作。再看成本比较是否采用相同的任务、重试预算和模型计价，以及改变深度来源后成功率如何变化。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/SOLVE Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Man.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

LLM agents have made remarkable progress in robot manipulation, yet they suffer from expensive inference, dense step-by-step control, and tool bottlenecks. We introduce SOLVE, a training-free, versatile and efficient agent policy: a multimodal LLM agent writes a sparse, ordered sequence of 6-DoF end-effector keyposes per call, observes the result, and writes the next, while a motion planner interpolates between them. The agent decides the number and spacing of keyposes for both fast long-range motion and fine-grained manipulation. This granularity matches the sparsity of teleoperated manipulation: most demonstrations in DROID can be compressed into a few keyposes instead of dense actions. SOLVE grounds keyposes with sparse depth queries answered by noisy sources, such as multi-view triangulation, stereo, or monocular depth, and copes with that noise itself. It also improves from execution feedback, reflecting on its own rollouts and distilling a few rules per task. SOLVE reaches state-of-the-art performance of 74.5% on RoboDojo and 84.5% on RoboLab, with only $1.7 per episode on average, 12x less than previous dense-control agent policies. On a real robot, the same agent achieves an 88% success rate (75 of 85 episodes) over 16 challenging zero-shot tasks. Our project page is at https://serenos.github.io/solve-website.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34750v1
- Authors: Xiang Li, Hongyu Zhou, Ya-Li Li, Tao Li, Rui Zhang, Junjie Lai, Weihua Zhang, Shengjin Wang
- Published: 2026-11-25T17:25:17Z
- Age days: 1

</details>
