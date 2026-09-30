---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23755v1"
published: "2026-09-20T17:09:09Z"
age_days: 2
score: 34
created: 2026-09-23
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# EgoWild2Dex: Learning Dexterous Robotic Manipulation from In-the-Wild Human Experience

> [!summary] 先说人话（基于摘要）
> EgoWild2Dex尝试把人们日常工作中的第一视角视频转成双臂灵巧操作经验。它同时处理人头摄像机的视角晃动，以及人手动作与机器人动作之间的差异。

## 问题

受控场景的人类示范覆盖有限，而自然场景数据虽多样，却有遮挡、杂乱和头部运动造成的视角变化，还存在人机形态与动作空间差异。

## 创新点或方法

GeoFormer以可微几何变换将不稳定的人类观测对齐到机器人视角，再通过人机联合训练把人类运动经验与机器人动作对应起来。

## 证据

EgoWild含538.9小时、179,049段、125,961种任务描述和1,282类物体；平均累计视角旋转为15.93°/秒。真实机器人3项长程双臂灵巧任务平均成功率96.7%，物体级零样本平均成功率33.3%。

## 局限

高任务成功率只覆盖3项任务，物体零样本结果明显更低；需核查机器人监督量，数据、模型和代码在摘要中仍是计划发布。

- **判断**：值得精读数据分布和人机对齐实验，避免用熟悉任务结果概括开放物体泛化。

## 研究关联

对机器人学习，提供了利用自然人类视频扩展技能与物体覆盖的路径，并明确把视角对齐作为数据迁移中的核心问题。

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/EgoWild2Dex Learning Dexterous Robotic Manipulation from In-the-Wild Human Exper.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric human data provide a principled source of supervision for learning dexterous robot manipulation. Unlike prior approaches that often collect such data in constrained or specially constructed environments, we collect in-the-wild egocentric demonstrations in real-world settings, including homes, factories, and pharmacies, etc., where people perform their ordinary tasks while wearing head-mounted cameras. This collection protocol captures diverse workflows and hand-object interactions across long-tailed object and skill distributions, but also yields visually challenging observations due to scene clutter and head-motion-induced viewpoint changes (a mean cumulative rotation of $15.93^{\circ}$/s). To address these issues, we introduce EgoWild2Dex, which transfers in-the-wild ego-human experience to dual-arm robots with dexterous hands by jointly aligning unstable egocentric views and human motions with robot observations and actions, respectively. This work offers three benefits. First, we introduce GeoFormer, a differentiable geometric transformer that warps noisy human observations toward robot observations. Second, we design a human-robot training scheme to bridge the embodiment gap, enabling high task success with limited robot supervision. Third, we release EgoWild, a 538.9-hour in-the-wild egocentric human dataset comprising 179,049 episodes, 125,961 unique task descriptions, and 1,282 object categories. On real robots, EgoWild2Dex achieves an average success rate of 96.7% across three long-horizon bimanual dexterous manipulation tasks and an average object-level zero-shot success rate of 33.3%. The data, models, and code will be released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23755v1
- Authors: Kunyang Lin, Xutao Wen, Jingxi Lin, Lanyong Lin, Jiaming Liu, Tianshuo Yang, Xianchi Chen, Yue Han, Yiduo Li, Zhanpeng Zhang, Ping Luo
- Published: 2026-09-20T17:09:09Z
- Age days: 2

</details>
