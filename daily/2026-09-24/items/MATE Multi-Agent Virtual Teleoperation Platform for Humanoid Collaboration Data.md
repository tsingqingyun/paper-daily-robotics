---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.26520v1"
published: "2026-09-22T14:45:17Z"
age_days: 1
score: 46
created: 2026-09-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection

> [!summary] 先说人话（基于摘要）
> MATE 让异地操作者在同一个物理仿真环境里共同操控人形机器人，降低多人、多机器人协作示范的采集门槛。配套的 EAIS 则优先抽取推进任务和发生关键交互的片段来训练策略。

## 问题

任务是学习人形机器人的协同移动与操作。现有数据流程偏重单机器人，而真实多机器人采集需要昂贵硬件、专门场地和反复重置，难以规模化。

## 创新点或方法

多个操作者同时控制共享仿真中的全身人形机器人，保留机器人、物体和环境之间的物理耦合。EAIS 在与执行对齐的前缀内计算采样信号，提高任务进展和关键交互行为的训练权重。

## 证据

数据集包含 24.1 小时、2,500 个联合回合和五类长时程任务。摘要报告了模仿学习与 VLA 策略评测，以及无需真实微调的虚拟示范到实体人形机器人的零样本迁移，但未给出成功率或采集效率数字。

## 局限

摘要只明确说迁移到实体人形机器人，不能据此确认已经完成真实多机器人协作迁移；需核查实体实验覆盖哪些协作关系及 EAIS 的独立贡献。

- **判断**：做多机器人数据或协作 VLA 的研究者值得细读平台与采样设计，实体协作泛化结论需以全文为准。

## 研究关联

对协作机器人学习和 VLA 研究者，价值在于提供可扩展的联合示范采集路径，并把多智能体之间的交互时刻作为明确的学习对象。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：46
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/MATE Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed operators to simultaneously control whole-body humanoids in a shared physics-based environment. MATE removes the need for multiple physical robots and co-located operation while preserving physically coupled interactions among humanoids, objects, and environments. Using MATE, we construct a multi-humanoid collaboration dataset comprising 24.1 hours of coordinated behavior across 2,500 joint episodes and five long-horizon tasks, including object handover, relay delivery, environment interaction, and cooperative transport. To improve learning from these interaction-rich demonstrations, we introduce EAIS, an Execution-Aligned Interaction Sampling strategy that computes sampling signals within an execution-aligned prefix and prioritizes task-progressing and interaction-critical behaviors. We evaluate MATE with representative imitation learning and vision-language-action policies across diverse collaboration tasks. Experiments demonstrate efficient data collection, effective policy learning, and zero-shot transfer from virtual demonstrations to a physical humanoid without real-world fine-tuning. Project page: https://yerik-yu.github.io/MATE/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.26520v1
- Authors: Yichuan Yu, Youzhuo Wang, Yiming Ren, Di Feng, Yexuan Yang, Bingxi Yang, Shengxiao Gong, Yujing Sun, Yuexin Ma
- Published: 2026-09-22T14:45:17Z
- Age days: 1

</details>
