---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11308"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 33
created: 2026-09-13
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation

> [!summary] 先说人话（基于摘要）
> 2AM把长任务的记忆留给上层Agent，让不保留跨回合记忆的动作模型专心执行。Agent除下达语言子任务，还提供二维抓取、放置和移动提示，把意图说得更具体。

## 这篇到底在做什么

- **卡在哪里**：长时操作需要历史信息，但现有系统同时加入规划器、几何工具或深度输入，使性能提升难以归因。失败也可能来自动作策略能力不足，或上层语言指令没有充分表达意图。
- **关键解法**：多模态Agent独占任务记忆，单个RGB动作模型独占任务相关运动执行。Agent将历史压缩为子任务语言和可选二维提示；动作模型通过结构化提示标注、条件丢弃、空间噪声与时间扰动训练，适应不完美的上层指令。
- **拿什么证明**：在不使用深度、在线几何或规划器物体运动的LIBERO-Mem设置中，平均完成度为76.3%，比最强已报告基线14.8%高61.5个百分点；宽松成功率63.0%，严格成功率11.8%。

## 值不值得读

- **和你的研究有什么关系**：对Agent与VLA研究者，它提供了可操作的记忆分工和高带宽执行接口，说明评估动作模型时也应控制上层指令的精确程度。
- **先别急着信**：平均完成度与严格成功率差距很大，不能把76.3%理解为完整任务成功率。需核查各指标定义，以及基线在提示监督和输入接口上的可比性。
- **判断**：值得精读接口设计、训练标注和指标定义；分工思路清晰，但严格长任务成功仍是明显瓶颈。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/2AM Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.11308v1 Announce Type: cross Abstract: Long-horizon robot manipulation requires memory, but not necessarily inside the action policy. To address such tasks, current agentic systems often combine VLAs with planners and geometric tools, sometimes using additional depth or calibrated geometry. These systems confound attribution: gains may come from richer observations or alternative motor tools, while failures may stem from either the policy or an under-specified language interface. We isolate this question through a deliberately constrained design: less tool breadth, but greater interface bandwidth. 2AM makes a multimodal Agent the sole holder of task memory and a single RGB-based, episodically stateless Action Model the sole executor of task-relevant motion. The Agent compiles interaction history into subtask language and optional 2D grasp, place, and move hints that bind its physical intention at different time scales. To teach this steerability to the VLA, we augment demonstrations with structured hint labels and train under condition dropout, spatial noise, and temporal jitter to tolerate imperfect Agent outputs. On LIBERO-Mem, without depth, online geometry, or planner-based object motion, 2AM reaches 76.3% average completion, a 61.5-point improvement over the strongest reported baseline of 14.8%, together with 63.0% relaxed and 11.8% strict success. These results show that task memory can remain Agent-side. They further show that Action Model capability depends not only on what the policy has learned, but on how precisely the Agent can steer it.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11308
- Authors: Yutong Hu, Fengjiao Chen, Xuezhi Cao, Renaud Detry
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
