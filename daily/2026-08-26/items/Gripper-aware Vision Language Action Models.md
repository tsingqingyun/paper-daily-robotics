---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.24603v1"
published: "2026-08-25T14:24:51Z"
age_days: 0
score: 33
created: 2026-08-26
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Gripper-aware Vision Language Action Models

> [!summary] 一句话结论（基于摘要）
> Intensive experiments in both simulation and real-world robots show that our GVLA outperforms the current baselines across evaluated settings.

## 问题

However, existing VLAs often implicitly assume gripper invariance, despite grasping strategies being inherently embodiment-dependent.

## 创新点或方法

To address this gap, we introduce MiGA, a multi-gripper-aware dataset spanning five distinct gripper types across multiple robots with 103,000 demonstrations, explicitly capturing strategy divergence under shared task objectives.

## 证据

Intensive experiments in both simulation and real-world robots show that our GVLA outperforms the current baselines across evaluated settings.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Gripper-aware Vision Language Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision language action models (VLAs) have advanced general purpose robotic grasping and manipulation by enabling robots to interpret visual observations and natural language instructions to generate executable action sequences. However, existing VLAs often implicitly assume gripper invariance, despite grasping strategies being inherently embodiment-dependent. Different gripper types, such as parallel-jaw and suction, usually require distinct interaction strategies to achieve the same grasping objective. Moreover, current datasets for VLAs predominantly rely on parallel-jaw grippers, limiting gripper-aware learning. To address this gap, we introduce MiGA, a multi-gripper-aware dataset spanning five distinct gripper types across multiple robots with 103,000 demonstrations, explicitly capturing strategy divergence under shared task objectives. We further propose GVLA, which combines a new multi-gripper tokenizer with adapter-based policy routing. Our new gripper encoding induces structured embedding information that balances parameter sharing and strategy differentiation, while layer-wise probing confirms meaningful gripper-conditioned representations for VLAs. Intensive experiments in both simulation and real-world robots show that our GVLA outperforms the current baselines across evaluated settings. Our method also improves zero-shot generalization or few-shot adaptation to new objects or unseen tasks, and enable more efficient gripper adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.24603v1
- Authors: Hanyi Zhang, Zihong Luo, Tianyu Li, Khang Nguyen, Basu Hela, Shreyas Kumar, Ngoc Duy Tran, Feng Dai, Charith Munasinghe, Jorge Peña Queralta, Giovanni Toffetti, Khoa Vo, Ngan Le, Ravi Prakash, Quan Vuong, Tung D. Ta, Long Hu, Anh Nguyen, Baoru Huang
- Published: 2026-08-25T14:24:51Z
- Age days: 0

</details>
