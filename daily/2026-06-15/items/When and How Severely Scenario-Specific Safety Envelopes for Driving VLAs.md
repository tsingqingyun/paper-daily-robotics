---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14238v1"
published: "2026-06-12T08:20:06Z"
age_days: 2
score: 26
created: 2026-06-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs

## 为什么重要

自动筛选分数：26

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Safety certification of Vision-Language-Action (VLA) driving planners under ISO 21448
(SOTIF) rests on an Operational Design Domain (ODD) specification that answers two
complementary questions: when does the planner start to fail, and how severely does it
fail once it does? We evaluate Alpamayo R1, a 10B-parameter open-weight driving VLA, on
15,968 (clip, attack) pairs. We find a conservative-aggregate gap: an aggregate safe
threshold of $σ\leq 50$ under a 15% average displacement error (ADE) budget masks well-
sampled scenarios that tolerate the top of the tested grid ($σ= 70$). A Gaussian Mixture
Model (GMM) on the changed-explanation subset identifies six discrete severity bands
(BIC-optimal $k{=}6$), so two perturbation conditions with the same mean error can
differ materially in their share of high-severity (C4/C5) failures. Joining the two
analyses on the same corpus surfaces a finding neither yields in isolation: the
scenarios with the loosest noise thresholds are not those with the lowest high-severity
rate: STOP_SIGNAL concentrates roughly $4\times$ the C4/C5 share of LANE_KEEPING despite
tolerating a larger $σ$. A deployable SOTIF ODD specification for driving VLAs therefore
requires a two-dimensional safety envelope, not a single aggregate value per hazard.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14238v1
- Authors: Abhinaw Priyadershi, Jelena Frtunikj
- Published: 2026-06-12T08:20:06Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
