---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00666v1"
published: "2026-07-01T09:13:40Z"
age_days: 1
score: 32
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Vision-Language-Action (VLA) models often fail to perform the same learned tasks under
environmental shifts, such as changes in camera pose and shifts to a different but
similar robot (e.g., from Panda to UR5e). Adapting these models to the shifted
environment (i.e., target domain) often requires training on multiple demonstrations for
each task, which are costly to collect. To reduce the burden of data curation and
training, we propose an analogy-based method that adapts VLA models under environmental
shifts through weight vector arithmetic with domain-specific information addition, named
Domain ARiThmetic (DART). Unlike prior approaches, DART requires collecting only a
single demonstration, enabling efficient adaptation. To accurately isolate domain-
specific information for addition, DART performs subspace alignment between singular
components in weight vectors to filter out noisy components. In both simulated and real-
world experiments, DART outperforms existing VLA adaptation methods in one-shot
scenarios across diverse visual and embodiment shifts. Code is available at
https://github.com/snumprlab/dart.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00666v1
- Authors: Taewook Kang, Taeheon Kim, Donghyun Shin, Jonghyun Choi
- Published: 2026-07-01T09:13:40Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
