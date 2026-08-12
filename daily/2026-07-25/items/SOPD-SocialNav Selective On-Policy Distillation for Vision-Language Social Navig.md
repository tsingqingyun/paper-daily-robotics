---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19850v1"
published: "2026-07-22T07:35:35Z"
age_days: 2
score: 24
created: 2026-07-25
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation

## 为什么重要

自动筛选分数：24

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Vision-language models have shown strong potential for social robot navigation by
leveraging rich semantic understanding of complex environments and human behaviors.
However, large scale VLMs are difficult to deploy on resource-constrained robotic
platforms, while lightweight VLMs often lack sufficient social reasoning capability. To
address this problem, we propose SOPD-SocialNav, a selective on-policy distillation
(SOPD) method that transfers social navigation knowledge from a large teacher VLM to a
lightweight student VLM. SOPD introduces an entropy-based token selection mechanism that
uses teacher uncertainty to identify socially informative decision tokens, while
suppressing gradients from low-entropy tokens corresponding to trivial navigation
states. A temperature-controlled Jensen-Shannon divergence objective is then used to
align the student and teacher distributions on the selected tokens. Experiments on the
SNEI and MUSON benchmarks demonstrate that SOPD consistently outperforms supervised
fine-tuning, off-policy distillation, and standard on-policy distillation baselines in
action prediction, perception consistency, and reasoning consistency. Real-world
deployment on a Scout Mini robot further shows that the distilled model can generate
more socially appropriate navigation behaviors in conversational and queuing scenarios.
These results suggest that SOPD is an effective strategy for building lightweight yet
socially aware VLM-based navigation systems.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19850v1
- Authors: Xinyu Zhang, Zishuo Wang, Ling Xiao
- Published: 2026-07-22T07:35:35Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
