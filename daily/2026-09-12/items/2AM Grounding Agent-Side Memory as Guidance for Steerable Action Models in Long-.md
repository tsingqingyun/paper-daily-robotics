---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11308v1"
published: "2026-09-10T09:35:56Z"
age_days: 1
score: 33
created: 2026-09-12
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation

> [!summary] 先说人话（基于摘要）
> 2AM把长期记忆放在Agent里，让动作模型只执行当前明确指令。Agent通过子任务语言和二维抓取、放置、移动提示，把记忆转成机器人能落实的意图。

## 这篇到底在做什么

- **卡在哪里**：长程操作需要记忆，但现有Agent系统常同时加入规划器、几何工具和额外观测，难以判断收益来自记忆、感知还是替代控制工具；语言接口含糊也会掩盖执行器能力。
- **关键解法**：仅由多模态Agent保存历史，由单一RGB、跨回合无状态的动作模型执行任务运动。示教增加结构化提示标签，并用条件丢弃、空间噪声和时间抖动训练模型容忍不完美提示。
- **拿什么证明**：在不使用深度、在线几何和规划器物体运动的LIBERO-Mem设置中，平均完成率76.3%，比摘要所列最强基线14.8%高61.5个百分点；宽松成功率63.0%，严格成功率11.8%。

## 值不值得读

- **和你的研究有什么关系**：为Agent与VLA如何分工提供可检验设计，提示接口精度可能是长程机器人性能的重要变量。
- **先别急着信**：平均完成率与严格成功率差距很大，需要核查三种指标含义，并区分完成部分子任务与完整任务成功。
- **判断**：值得精读接口设计和指标定义，尤其适合研究Agent记忆与VLA执行能力的归因。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/2AM Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon robot manipulation requires memory, but not necessarily inside the action policy. To address such tasks, current agentic systems often combine VLAs with planners and geometric tools, sometimes using additional depth or calibrated geometry. These systems confound attribution: gains may come from richer observations or alternative motor tools, while failures may stem from either the policy or an under-specified language interface. We isolate this question through a deliberately constrained design: less tool breadth, but greater interface bandwidth. 2AM makes a multimodal Agent the sole holder of task memory and a single RGB-based, episodically stateless Action Model the sole executor of task-relevant motion. The Agent compiles interaction history into subtask language and optional 2D grasp, place, and move hints that bind its physical intention at different time scales. To teach this steerability to the VLA, we augment demonstrations with structured hint labels and train under condition dropout, spatial noise, and temporal jitter to tolerate imperfect Agent outputs. On LIBERO-Mem, without depth, online geometry, or planner-based object motion, 2AM reaches 76.3% average completion, a 61.5-point improvement over the strongest reported baseline of 14.8%, together with 63.0% relaxed and 11.8% strict success. These results show that task memory can remain Agent-side. They further show that Action Model capability depends not only on what the policy has learned, but on how precisely the Agent can steer it.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11308v1
- Authors: Yutong Hu, Fengjiao Chen, Xuezhi Cao, Renaud Detry
- Published: 2026-09-10T09:35:56Z
- Age days: 1

</details>
