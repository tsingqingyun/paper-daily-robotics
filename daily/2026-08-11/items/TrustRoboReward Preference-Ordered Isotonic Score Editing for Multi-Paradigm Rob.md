---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08491v1"
published: "2026-08-09T05:25:22Z"
age_days: 2
score: 36
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# TrustRoboReward: Preference-Ordered Isotonic Score Editing for Multi-Paradigm Robot Reward Models

> [!summary] 一句话结论（基于摘要）
> Evaluated on our benchmark, Qwen3-VL-4B trained with POISE achieves an overall reward score of 77.96%, nearly matching GPT-5-mini (78.09%, gap 0.13%) and outperforming the strongest RoboReward-4B baseline by 10.13%.

## 关键点

- **问题**：Reward models are a bottleneck for reinforcement learning in embodied AI.
- **创新点 / 方法**：To address this, we propose TrustRoboReward, a multi-paradigm reward modeling framework equipped with Preference-Ordered Isotonic Score Editing (POISE).
- **证据**：Evaluated on our benchmark, Qwen3-VL-4B trained with POISE achieves an overall reward score of 77.96%, nearly matching GPT-5-mini (78.09%, gap 0.13%) and outperforming the strongest RoboReward-4B baseline by 10.13%.
- **局限**：Augmenting RoboReward with pairwise comparison and video-QA supervision causes inconsistency between pairwise preferences and pointwise scores, introducing training noise and hurting downstream performance---an issue aggregation methods such as TrustJudge cannot resolve.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-11/TrustRoboReward Preference-Ordered Isotonic Score Editing for Multi-Paradigm Rob.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reward models are a bottleneck for reinforcement learning in embodied AI. Long-horizon
robotic manipulation requires scalable vision feedback beyond handcrafted rewards or
task-specific annotations. Existing open-source VLM reward judges like RoboReward adopt
simple 1--5 trajectory progress scoring, lacking pairwise preferences for RLHF, DPO and
Bradley-Terry frameworks, while failing to optimize video scene understanding.
Augmenting RoboReward with pairwise comparison and video-QA supervision causes
inconsistency between pairwise preferences and pointwise scores, introducing training
noise and hurting downstream performance---an issue aggregation methods such as
TrustJudge cannot resolve. To address this, we propose TrustRoboReward, a multi-paradigm
reward modeling framework equipped with Preference-Ordered Isotonic Score Editing
(POISE). We construct a unified four-paradigm dataset with trajectory progress scoring
(Score-A), video-QA answer quality scoring (Score-B), and their pairwise counterparts
(Pair-A, Pair-B). Pairwise labels align better with human judgment than pointwise
scores, inspiring us to calibrate pointwise scores to avoid score-pair reversals against
pairwise preferences. POISE rectifies pointwise scores and eliminates cross-paradigm
reversal conflicts unresolved by TrustJudge. Theoretically, POISE reduces score-pair
reversal conflicts from 20.15% to 0%, whereas TrustJudge retains 20.46% conflicts on the
same corpus. Evaluated on our benchmark, Qwen3-VL-4B trained with POISE achieves an
overall reward score of 77.96%, nearly matching GPT-5-mini (78.09%, gap 0.13%) and
outperforming the strongest RoboReward-4B baseline by 10.13%. It also lifts test-time
score-pair consistency to 71.90%, exceeding RoboReward-4B (57.26%) and GPT-5-mini
(68.09%). Integrating TrustJudge aggregation during inference boosts the overall score
to 78.57%, surpassing the GPT-5-mini teacher model.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08491v1
- Authors: Yidong Wang, Yan Zhan, Ziteng Feng, Zhenyu Cui, Ziyi Zhou, Renzhao Liang, Jiaxuan Zhu, Zilei Yang, Yiran Zhao, Zhongkuan Mao, Bo Jia, Hanchu Ni, Chenggang Xie, Biao Liu, Yi Zhang, Yong Dai, Xiaozhu Ju, Wei Ye, Shikun Zhang
- Published: 2026-08-09T05:25:22Z
- Age days: 2

</details>
