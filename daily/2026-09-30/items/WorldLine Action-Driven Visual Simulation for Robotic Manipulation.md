---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.38059v1"
published: "2026-09-29T17:26:22Z"
age_days: 0
score: 29
created: 2026-09-30
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# WorldLine: Action-Driven Visual Simulation for Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> WorldLine 是预测机器人动作后果的视觉模拟器，试图同时学会跨机器人通用动力学和具体动作含义。它先利用大量无动作视频学习交互，再通过共享图像空间动作接口接入不同机器人的控制。

## 问题

真实机器人经验与候选行为评估成本高，但视频生成常重视觉合理性、轻动作遵循和机器人—物体动力学一致性。带动作数据又稀缺，且不同机器人控制空间难以直接共享。

## 创新点或方法

将动力学学习与动作落地解耦：使用超过 1 万小时无动作机器人视频，以及超过十种形态、逾 2000 小时动作轨迹。图像空间动作表示统一控制接口，多视角、失败数据和关系正则增强交互预测，机器人重点少步蒸馏提升滚动生成效率。

## 证据

失败轨迹上，机器人掩码 IoU 比最强基线高 0.1626；在 RoboTwin 和 AgiBot 上，轨迹成功预测平均准确率为 74%，比最强基线高 1 个百分点。未用 RoboTwin 训练或适配时，生成轨迹使任务成功率相对直接策略执行最高提高 21.4 个百分点。

## 局限

成功预测仅领先 1 个百分点，而任务收益最高达 21.4 个百分点，需核查后者的任务分布、使用轨迹的决策流程和额外推理预算。

- **判断**：世界模型方向优先精读，重点看共享动作表示及预测如何转化为控制收益，不能仅凭视觉质量判断模拟器价值。

## 研究关联

对世界模型与具身规划，价值在于连接跨形态数据、动作条件预测和下游策略收益。失败轨迹评测也有助于判断模型能否模拟错误行为，而非只复现成功示范。

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/WorldLine Action-Driven Visual Simulation for Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world robot learning is constrained by the cost of collecting experience and evaluating candidate behaviors. Video generation models offer a scalable foundation for visual simulators that predict action outcomes before physical execution. Yet they often favor visual plausibility over accurate action following and coherent robot--object dynamics, while action-conditioned simulators depend on scarce, embodiment-specific data that are difficult to share across incompatible control spaces. We introduce WorldLine, an action-driven visual simulator that decouples transferable dynamics learning from heterogeneous action grounding. WorldLine learns manipulation dynamics from more than 10,000 hours of action-free robot videos and grounds them using over 2,000 hours of action trajectories across more than ten embodiments. An image-space action representation provides a shared control interface across embodiments, while multi-view and failure-enriched training with relational regularization improves interaction-sensitive prediction. Robot-focused few-step distillation enables efficient causal rollout while preserving action-critical motion. Across held-out and out-of-domain settings, WorldLine maintains strong visual quality and robot-motion agreement; on failed trajectories, it improves robot-mask IoU by 0.1626 over the strongest baseline. It predicts trajectory success with 74% mean accuracy across RoboTwin and AgiBot, one percentage point above the strongest baseline. Without RoboTwin training or adaptation, its rollouts improve task success by up to 21.4 percentage points over direct policy execution. Together, these capabilities make WorldLine a scalable and efficient visual simulator for policy evaluation and embodied planning. More results are available at \href{https://zhengsh123.github.io/WorldLine/}{project page}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38059v1
- Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia
- Published: 2026-09-29T17:26:22Z
- Age days: 0

</details>
