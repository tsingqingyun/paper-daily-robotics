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
url: "https://arxiv.org/abs/2609.39207"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# ASENA: Self-evolving Agents for Embodied Navigation

> [!summary] 这篇论文到底做了什么（基于摘要）
> ASENA 让编码智能体通过读传感器、写程序、看执行结果和修错来控制机器人，并把笔记与技能留给后续任务。它的“自我演化”发生在工作空间中，模型权重保持不变；ASENA-VLN 则提供可选的学习式导航能力。

## 问题

任务涵盖人形机器人的导航、操作和交互，要求把现场观察变成可执行行为，并处理执行失败。摘要试图扩展路线跟随和预定义技能的行为范围，但没有具体比较现有系统为什么做不到这些扩展。

### 用一个例子理解

理解用例（非论文实验）：输入“找到会议室并检查桌上有没有杯子”。智能体读取相机，调用导航策略或编写移动程序；执行后检查记录，修正走错的位置，再输出检查结果，并保存可复用的处理经验。

## 创新点或方法

从依赖固定行为入口，改为允许智能体在线编写和执行程序，并依据记录修改程序、复用经验。统一机器人接口负责接通观察与执行。另训练 4B 单目 ASENA-VLN，用路线指令、视觉问答和几何生成的原子导航数据训练共享解码器，输出机体坐标系轨迹。部署时它可被编码智能体调用；工作空间更新不等于重新训练模型。

### 方法如何工作

1. 读取指令和传感器数据，确定需要移动、观察或操作的目标，为程序提供现场依据。
2. 编写执行程序，必要时调用 ASENA-VLN 生成轨迹，把任务转成机器人行为。
3. 检查记录的结果，定位失败并修复程序，让反馈影响下一次执行。
4. 保存笔记和可执行技能供后续任务复用，在固定模型权重下累积经验；保存与选择细节未说明。

### 必要术语

- 机器人接口：统一连接传感器和动作执行的入口；让编码智能体能操作机器人。
- 机体坐标系轨迹：相对机器人自身描述的移动路径；ASENA-VLN 用它输出导航结果。
- 工作空间演化：更新笔记、程序和技能；本文靠它积累经验，而非修改模型权重。

## 证据

摘要报告独立 ASENA-VLN 在 R2R、RxR 的成功率为 68.7%、70.2%，称为最优结果，但未列对手数值。接入编码智能体后，两项智能体基准均增加 11 个百分点并减少执行时间，未给时间值。对重复的 100 任务子集运行十轮，R2R 从 72% 到 98%，RxR 从 65% 到 89%；这是模拟反馈下反复任务的结果。Unitree G1 展示搜索、检查、手势及拿取搬运交接，未提供真机成功率。问答也报告最优准确率和更少交互步数，但未给数字。

## 局限

摘要未列作者明确局限。我会重点核查重复子集的收益能否迁移到新任务，以及成功来自通用技能还是记住具体路线。模拟中的十轮改进不能直接外推为真机持续学习；G1 演示说明行为可实现，但不足以衡量稳定性。

- **判断**：值得读执行反馈与经验保存机制，并仔细检查新任务测试；它最有意思的证据是固定权重下的工作空间改进，而非单一导航分数。

## 研究关联

持续改进不一定需要更新权重：失败原因、可执行修复和调用经验也能成为学习成果。这对任务会重复、能得到执行反馈的系统尤其值得借鉴；关键是把经验保存成下一次真正能用的内容。

### 下一步读哪里

核查程序可调用的接口、错误反馈内容、笔记与技能如何检索；再看十轮实验是否有未见任务测试、成功率提升的消融，以及真机演示的试验次数。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/ASENA Self-evolving Agents for Embodied Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.39207v2 Announce Type: replace Abstract: We present ASENA, an embodied agent system that enables general-purpose coding agents to program humanoid navigation, manipulation, and interaction. Through a unified robot harness, agents read sensor data, write and execute programs, inspect recorded outcomes, repair failures, and reuse notes and executable skills while keeping their model weights fixed. We also introduce ASENA-VLN, a 4B monocular navigation policy that serves as an optional tool within this programmable system. ASENA-VLN predicts body-frame trajectories for both extended routes and short-horizon behaviors. Its shared vision-language decoder is trained on route instructions, visual question answering, and a newly curated dataset of geometry-derived atomic navigation tasks. As a standalone policy, ASENA-VLN achieves state-of-the-art success rates of 68.7% on R2R and 70.2% on RxR. When integrated with a coding agent, learned navigation improves ASENA's success rate by 11 percentage points on both agentic benchmarks and reduces execution time. Persistent workspace evolution uses simulator feedback to improve success over ten passes through recurring 100-task subsets. Success increases from 72% to 98% on R2R and from 65% to 89% on RxR. On embodied question answering, ASENA achieves state-of-the-art accuracy with fewer interaction steps. On a Unitree G1, we demonstrate search, visual inspection, spatial reasoning, synthesized gestures, and mobile manipulation combining object pickup, carrying, and handoff without a pre-built map. These demonstrations illustrate how online programming extends robot behavior beyond route following and predefined skills.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.39207
- Authors: An-Chieh Cheng, Isabella Liu, Edmund Bu, Johan Bjorck, Hongxu Yin, Zhengyi Luo, Jan Kautz, Linxi "Jim" Fan, Yuke Zhu, Sifei Liu
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
