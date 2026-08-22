---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20208v1"
published: "2026-08-20T16:07:56Z"
age_days: 1
score: 34
created: 2026-08-22
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Offline reinforcement learning improves robotic policies using previously collected data without further environment interaction.

## 关键点

- **问题**：Yet prevalent diffusion- and flow-matching robot policies lack tractable likelihoods, limiting their use in likelihood-based offline RL post-training.
- **创新点 / 方法**：We present RoMAN-Flow (Robotic Manipulation with Autoregressive Normalizing Flows), an offline reinforcement learning framework that makes AR-NF policies practical for robotic manipulation by addressing this sampling bottleneck in both stages.
- **证据**：Offline reinforcement learning improves robotic policies using previously collected data without further environment interaction.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/RoMAN-Flow Taming Autoregressive Normalizing Flows for Offline Reinforcement Lea.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Offline reinforcement learning improves robotic policies using previously collected data without further environment interaction. Yet prevalent diffusion- and flow-matching robot policies lack tractable likelihoods, limiting their use in likelihood-based offline RL post-training. AR-NFs offer both expressive action modeling and exact likelihood evaluation, but their sequential sampling incurs substantial sampling overhead during policy optimization and deployment. We present RoMAN-Flow (Robotic Manipulation with Autoregressive Normalizing Flows), an offline reinforcement learning framework that makes AR-NF policies practical for robotic manipulation by addressing this sampling bottleneck in both stages. During policy optimization, RoMAN-Flow employs a sampling-free, advantage-weighted likelihood objective that assigns higher likelihood to high-advantage actions from the offline dataset without sampling from the autoregressive policy. For efficient deployment, it distills the optimized autoregressive policy into a one-step action generator, enabling low-latency action prediction. Experiments across multiple simulated manipulation benchmarks and real-world robotic platforms demonstrate that RoMAN-Flow achieves competitive policy performance while substantially reducing inference latency. Code is available at https://github.com/konnyaku28/RoMAN-Flow.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20208v1
- Authors: Shaoxuan Wang, Guangting Zheng, Rui Huang, Zhipeng Tang, Sha Zhang, Jiajun Deng, Yanyong Zhang
- Published: 2026-08-20T16:07:56Z
- Age days: 1

</details>
