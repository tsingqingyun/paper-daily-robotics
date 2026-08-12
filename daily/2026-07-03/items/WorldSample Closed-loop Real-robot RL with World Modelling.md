---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02431v1"
published: "2026-07-02T17:00:37Z"
age_days: 0
score: 39
created: 2026-07-03
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# WorldSample: Closed-loop Real-robot RL with World Modelling

> [!summary] 一句话结论（基于摘要）
> Experiments on robot manipulation tasks involving contact-rich and precise tasks show that WorldSample improves policy success rate by 28% while reducing training steps by 59% compared with baselines.

## 关键点

- **问题**：Reinforcement learning (RL) can overcome the demonstration-coverage limitation of imitation learning (IL) by allowing robots to improve through trial-and-error interaction beyond the states observed in demonstrations.
- **创新点 / 方法**：To address this challenge, we propose WorldSample, a physically grounded data augmentation framework for real-robot RL that closes a real-synthetic loop between physical rollouts, world-model generation, and policy improvement.
- **证据**：Experiments on robot manipulation tasks involving contact-rich and precise tasks show that WorldSample improves policy success rate by 28% while reducing training steps by 59% compared with baselines.
- **局限**：Reinforcement learning (RL) can overcome the demonstration-coverage limitation of imitation learning (IL) by allowing robots to improve through trial-and-error interaction beyond the states observed in demonstrations.

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning (RL) can overcome the demonstration-coverage limitation of
imitation learning (IL) by allowing robots to improve through trial-and-error
interaction beyond the states observed in demonstrations. However, deploying RL on real
robots remains constrained by high interaction costs, since each physical rollout is
costly and reflects only one realized action-outcome path. To address this challenge, we
propose WorldSample, a physically grounded data augmentation framework for real-robot RL
that closes a real-synthetic loop between physical rollouts, world-model generation, and
policy improvement. Grounded on real rollouts, WorldSample generates high-fidelity
synthetic transitions through a post-trained world model, which greatly lowers the
visual hallucination. Specifically, rather than simply using these transitions as real-
world experience, WorldSample introduces Policy-Paced Learning (PPL) to regulate the
training process through sample selection and scheduling, balancing useful augmentation
against value overestimation and mitigating the hallucination-induced noise. Experiments
on robot manipulation tasks involving contact-rich and precise tasks show that
WorldSample improves policy success rate by 28% while reducing training steps by 59%
compared with baselines. Furthermore, WorldSample improves world model visual fidelity
by 19.4dB in PSNR and 0.47 in SSIM over demonstration-only post-training, validating the
effectiveness of the real-synthetic loop for both policy and world model performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02431v1
- Authors: Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, Bofang Jia, Ziwei Wang
- Published: 2026-07-02T17:00:37Z
- Age days: 0

</details>
