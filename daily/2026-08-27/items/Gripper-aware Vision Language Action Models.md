---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.24603v1"
published: "2026-08-25T14:24:51Z"
age_days: 1
score: 33
created: 2026-08-27
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Gripper-aware Vision Language Action Models

> [!summary] 先说人话（基于摘要）
> GVLA 用多夹爪 tokenizer 和适配器路由，让共享 VLA 同时学习共性与夹爪专属策略；配套 MiGA 数据集覆盖5类夹爪、多个机器人和10.3万条示范。

## 这篇到底在做什么

- **卡在哪里**：现有VLA常默认夹爪不影响策略，但平行夹爪与吸盘完成同一目标时需要不同交互方式；主流数据又偏向平行夹爪，难以学习这种差异。
- **关键解法**：MiGA提供共享任务目标下不同夹爪的策略分化数据；tokenizer显式编码夹爪类型，层内适配器按本体路由策略，在参数共享与行为分化之间折中。输出仍是对应夹爪的动作序列。
- **拿什么证明**：数据集含5种夹爪和103,000条示范；摘要称仿真和真机均超过现有基线，并改善新物体或未见任务的零样本、少样本泛化及夹爪适配，但未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：它补上VLA跨末端执行器泛化这一具体缺口，对异构机器人数据整合和快速更换工具都有现实意义。
- **先别急着信**：缺少定量结果，且层级探针显示夹爪信息存在，并不能单独证明它导致性能提升；需看跨夹爪留一评测。
- **判断**：数据集本身就值得关注；方法是否成为通用跨本体方案，要看未见夹爪而非仅未见任务的结果。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/Gripper-aware Vision Language Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision language action models (VLAs) have advanced general purpose robotic grasping and manipulation by enabling robots to interpret visual observations and natural language instructions to generate executable action sequences. However, existing VLAs often implicitly assume gripper invariance, despite grasping strategies being inherently embodiment-dependent. Different gripper types, such as parallel-jaw and suction, usually require distinct interaction strategies to achieve the same grasping objective. Moreover, current datasets for VLAs predominantly rely on parallel-jaw grippers, limiting gripper-aware learning. To address this gap, we introduce MiGA, a multi-gripper-aware dataset spanning five distinct gripper types across multiple robots with 103,000 demonstrations, explicitly capturing strategy divergence under shared task objectives. We further propose GVLA, which combines a new multi-gripper tokenizer with adapter-based policy routing. Our new gripper encoding induces structured embedding information that balances parameter sharing and strategy differentiation, while layer-wise probing confirms meaningful gripper-conditioned representations for VLAs. Intensive experiments in both simulation and real-world robots show that our GVLA outperforms the current baselines across evaluated settings. Our method also improves zero-shot generalization or few-shot adaptation to new objects or unseen tasks, and enable more efficient gripper adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.24603v1
- Authors: Hanyi Zhang, Zihong Luo, Tianyu Li, Khang Nguyen, Basu Hela, Shreyas Kumar, Ngoc Duy Tran, Feng Dai, Charith Munasinghe, Jorge Peña Queralta, Giovanni Toffetti, Khoa Vo, Ngan Le, Ravi Prakash, Quan Vuong, Tung D. Ta, Long Hu, Anh Nguyen, Baoru Huang
- Published: 2026-08-25T14:24:51Z
- Age days: 1

</details>
