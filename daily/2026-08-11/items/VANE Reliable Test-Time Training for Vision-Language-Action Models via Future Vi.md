---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09448v1"
published: "2026-08-10T11:22:54Z"
age_days: 0
score: 32
created: 2026-08-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Test-time training (TTT) offers a lightweight way to adapt vision--language--action
(VLA) policies from unlabeled deployment streams, but it remains difficult to use
reliably in closed-loop manipulation. A shared adaptation space can mix incompatible
task corrections, while an online update can alter subsequent actions before its
consequences are known. We introduce a reliable TTT framework for VLA policies (VANE).
VANE conditions prompt adaptation on the current vision--language context and learns
from the future visual consequences of executed actions. Candidate updates are isolated
from the live policy, evaluated on subsequent observations, and committed only when
supported by future evidence, making adaptation selective and reversible. On SimplerEnv
WidowX, VANE improves average success by $3.2$ percentage points over the corresponding
TTT baseline. Results on Google Robot further show that deployment-time gains remain
task- and embodiment-dependent. Together, these results demonstrate a constrained,
evidence-based approach to adapting VLA policies during interaction.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09448v1
- Authors: Hongjin Ji, Guoyang Xia, Luoyang Sun, Fangxiang Feng, Lei Ren
- Published: 2026-08-10T11:22:54Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
