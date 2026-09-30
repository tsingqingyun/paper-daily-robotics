---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24411v1"
published: "2026-09-21T11:01:29Z"
age_days: 1
score: 32
created: 2026-09-23
concepts: ["视觉语言动作模型 VLA", "机器人学习"]
---

# Zeva-Ego: Egocentric Mid-Training with In-Context Causal Learning for Robot Manipulation

> [!summary] 先说人话（基于摘要）
> Zeva-Ego先从人类第一视角视频学习动作相关经验，再让机器人根据自己的尝试结果调整后续行为。部署适应依赖上下文中的动作—效果反馈，不需要更新参数。

## 问题

第一视角视频规模容易扩大，但视觉变化不直接等于机器人可执行动作；模型部署后还需要利用实际交互反馈继续适应。

## 创新点或方法

Action-Centric Encoder将视频中的视觉转变转为VLA中期训练监督；In-Context Causal Learning在部署时利用累积的动作与效果反馈调整行为。

## 证据

第一视角数据扩至1万小时，RoboTwin成功率从63.8%升至75.3%，与2千小时机器人示范的74.7%相近，对应经验数据比约4–5:1。ICCL在4次尝试内将成功率从58%提高至89%，无需参数更新。

## 局限

4–5:1仅是该实验设置下的经验比例；4次尝试后的成功率也不能当作首次尝试成功率，需核查任务重置与反馈条件。

- **判断**：值得精读数据规模对照和多次尝试协议，二者决定结论能推广到什么范围。

## 研究关联

对VLA和机器人学习，分别回答人类视频如何补充机器人数据、部署交互如何提供适应信号，且提供了数据规模与收益的具体参照。

- **概念**：[[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Zeva-Ego Egocentric Mid-Training with In-Context Causal Learning for Robot Manip.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric video offers a scalable source of physical interaction experience, yet translating it into robot-executable knowledge and enabling continual adaptation remain challenging. We introduce Zeva-Ego, a unified framework that learns physical priors from human experience and evolves through robot interaction. An Action-Centric Encoder (ACE) converts egocentric visual transitions into action-centered supervision for VLA mid-training, while In-Context Causal Learning (ICCL) enables parameter-free adaptation from action-effect feedback at deployment. Scaling Ego data to 10K hours improves RoboTwin success from 63.8% to 75.3%, matching 2K hours of robot demonstrations (74.7%), corresponding to an empirical data ratio of roughly 4-5:1. With accumulated interaction experience, ICCL further improves success from 58% to 89% within four attempts without parameter updates. These results demonstrate a scalable path toward embodied intelligence that learns from human experience and continuously improves through its own interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24411v1
- Authors: Bingjia Huang, Xin Ding, Fu Chen, Kun Li, Wei Sun, Hao Wu, Yunxin Liu, Ting Cao
- Published: 2026-09-21T11:01:29Z
- Age days: 1

</details>
