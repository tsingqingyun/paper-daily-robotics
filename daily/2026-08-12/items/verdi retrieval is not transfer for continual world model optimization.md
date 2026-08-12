---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09537v1"
published: "2026-08-10T12:35:59Z"
age_days: 1
score: 25
created: 2026-08-12
concepts: ["智能体 Agent", "世界模型"]
---

# verdi: retrieval is not transfer for continual world model optimization

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Foundation world models have made remarkable progress in planning, simulation, and
embodied intelligence. However, optimizing a pretrained world model toward a user-
specified objective remains difficult: each campaign typically rediscovers optimization
strategies from scratch, and the resulting knowledge rarely transfers to the next model.
Existing research agents automate the optimization loop but treat successful strategies
as directly reusable recipes, without principled safeguards for when transfer is
appropriate. We argue instead that retrieval is not transfer: a strategy validated on
one model is at best an optimization hypothesis for another, and becomes transferable
knowledge only after target-side experimental valida- tion. Guided by this principle, we
propose VERDI , a continual framework for evidence-licensed world model optimization.
VERDI characterizes each world model through shared inference-time probes to construct
an Optimization Fin- gerprint, retrieves relevant prior experience as ranked hypotheses,
and validates every candidate under a frozen target-side verifier before admitting it as
reusable evidence; contradictions among nearby fingerprints further trigger probe
evolution, continually refining the diagnostic representation itself. Experiments on
Ctrl-World, the Cosmos family, and RoboCoin show that VERDI reduces search cost by 68%,
GPU cost by 69%, and negative transfer from 0.34 to 0.06, while predicting transfer
outcomes with 83% sign accuracy.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09537v1
- Authors: Junyu Wu, Shiqin Nie, Youyi Kou, Baohua Yin, Guocai Yao, Qingyu Chen, Jingheng Ma, Shiji Zhou, Hongyong Song, Mingchen Zhuge, Sen Cui, Changshui Zhang
- Published: 2026-08-10T12:35:59Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
