---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09467v1"
published: "2026-08-10T11:37:46Z"
age_days: 0
score: 32
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Unmanned aerial vehicle vision-language navigation (UAV-VLN) requires agents to
translate visual observations and language instructions into reliable flight actions in
complex environments. Although recent end-to-end UAV vision-language-action (UAV-VLA)
policies reduce reliance on separately designed perception, planning, and control
modules, their behavior-cloning objectives provide limited corrective supervision for
interactive closed-loop execution. Reinforcement learning (RL) offers a promising
solution, while its effectiveness is constrained by inefficient use of samples, long-
tailed scene distributions, and policy distribution shift during optimization. To this
end, we propose RecoverFly, a failure-aware RL post-training framework for end-to-end
UAV-VLA policies. Specifically, RecoverFly adapts token-level RL for stable optimization
of grammar-constrained autoregressive UAV actions, revisits unresolved failure cases to
strengthen corrective learning and sample utilization, and combines a two-stage long-
tail scene curriculum with reference-policy regularization to improve scene adaptation
while preserving acquired capabilities. Experiments on the TravelUAV benchmark
demonstrate that RecoverFly achieves the best performance on the seen, unseen-map, and
unseen-object splits. Moreover, compared to the AerialVLA initialization, RecoverFly
improves success rate by 3.12 to 8.37 percentage points under a total rollout budget of
about 30\% of the training-set size, validating its effectiveness, robustness, and
generalization capabilities.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09467v1
- Authors: Boxiong Wang, Hui Kang, Geng Sun, Jiahui Li, Chao Yu, Daxin Tian
- Published: 2026-08-10T11:37:46Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
