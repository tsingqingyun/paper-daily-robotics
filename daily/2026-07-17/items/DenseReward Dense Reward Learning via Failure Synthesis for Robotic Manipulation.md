---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13033v1"
published: "2026-07-14T17:59:29Z"
age_days: 2
score: 33
created: 2026-07-17
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Experiments show that DenseReward outperforms general-purpose VLMs and existing robotic reward models in dense reward prediction across both simulated and real-world manipulation.

## 关键点

- **问题**：However, its practical adoption remains bottlenecked by the lack of reliable vision-language reward models that provide dense and informative feedback.
- **创新点 / 方法**：We introduce DenseReward, a dense robotic reward model that addresses both challenges.
- **证据**：Experiments show that DenseReward outperforms general-purpose VLMs and existing robotic reward models in dense reward prediction across both simulated and real-world manipulation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/DenseReward Dense Reward Learning via Failure Synthesis for Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning holds great promise for improving robot policies beyond the
limits of imitation learning. However, its practical adoption remains bottlenecked by
the lack of reliable vision-language reward models that provide dense and informative
feedback. Two key challenges remain: acquiring diverse failure data at scale and
obtaining fine-grained reward signals beyond sparse trajectory-level success labels.
Collecting failure trajectories typically requires laborious human effort, while pseudo-
failures constructed by relabeling successful demonstrations fail to capture the diverse
physical failure modes that arise during robot execution. Meanwhile, existing reward
models often predict sparse binary or trajectory-level rewards, which provide limited
guidance for efficient policy optimization. We introduce DenseReward, a dense robotic
reward model that addresses both challenges. To train DenseReward, we develop an
automated failure data generation pipeline that synthesizes physically realistic failure
trajectories in simulation without human labeling, covering diverse failure modes such
as collisions, missed grasps, object drops, and recovery behaviors. DenseReward predicts
dense frame-level reward scores from visual observations and language instructions,
enabling fine-grained estimation of task progress throughout an episode. Experiments
show that DenseReward outperforms general-purpose VLMs and existing robotic reward
models in dense reward prediction across both simulated and real-world manipulation. We
further demonstrate that DenseReward provides effective reward guidance for downstream
model predictive control and reinforcement learning. We release the dataset, trained
reward models, and evaluation suite to support the development of failure-aware dense
reward modeling for robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13033v1
- Authors: Yu Fang, Wanxi Dong, Jiaqi Liu, Yue Yang, Mingxiao Huo, Yao Mu, Huaxiu Yao, Li Erran Li, Daniel Szafir, Mingyu Ding
- Published: 2026-07-14T17:59:29Z
- Age days: 2

</details>
