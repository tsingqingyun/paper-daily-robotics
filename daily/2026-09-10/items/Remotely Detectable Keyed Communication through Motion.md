---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08920v1"
published: "2026-09-08T15:49:10Z"
age_days: 1
score: 26
created: 2026-09-10
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Remotely Detectable Keyed Communication through Motion

> [!summary] 先说人话（基于摘要）
> 机器人可以把短消息藏进动作扰动，让远处的摄像头或动捕系统读出来。这项运动通信方法尝试在不损害原策略表现的前提下，用身体动作传递信息。

## 这篇到底在做什么

- **卡在哪里**：任务是让机器人执行既有策略时同步传送可远程检测的消息，同时控制动作修改对任务表现的影响；传统电子通信不利用这条物理运动通道。
- **关键解法**：将任意内容的短载荷编码为预训练策略动作中的噪声，通过远程运动观测解码，并系统比较编码方案、提炼设计启发式。
- **拿什么证明**：在仿真与真实机器人上验证；真实机器人以 50 Hz 运行，四台机器人联合恢复一条 8 位消息，聚合速率为 0.67 bits/s。

## 值不值得读

- **和你的研究有什么关系**：对多机器人智能体研究者，可启发不依赖直接无线链路的意图广播；它不是通用具身基准，主要价值是新增通信机制。
- **先别急着信**：报告的吞吐率较低且依赖四机联合恢复，需核查单机能力、远程观测条件与策略性能损失。
- **判断**：值得读编码机制和真实部署设置，适合短意图通信场景，现有数字不足以支持高带宽用途。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/Remotely Detectable Keyed Communication through Motion.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Messages from electronic devices are conventionally received as text, audio, or radio signals. But robots move with rich, articulate motion in the real world, opening up the possibility of transmitting messages through motion itself. In this paper, we consider the problem of motion-based communication, where we seek to modify a robot's movements so as to transmit messages detectable from remote sensing (e.g., video or motion capture), without degrading policy performance. We introduce a method for messaging through motion capable of encoding arbitrary message content over short payloads - such as an agent's current intent - as noise in any pre-trained policy's actions. This brings a new kind of robustness to robot communication: this 'physical' channel complements standard wireless communications channels but does not depend on them, requiring no extra hardware nor the establishment of a direct link to the robot. We systematically characterize the space of encoding schemes and derive design heuristics, then validate them across simulated environments and real-robot deployment; on real robots running at 50 Hz, four robots jointly recover an 8-bit message at an aggregate 0.67 bits/s.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08920v1
- Authors: Benjamin Chang, Michael Amir, Manon Flageat, Amanda Prorok
- Published: 2026-09-08T15:49:10Z
- Age days: 1

</details>
