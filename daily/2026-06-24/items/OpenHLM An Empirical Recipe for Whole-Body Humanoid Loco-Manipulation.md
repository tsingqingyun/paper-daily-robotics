---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22174v1"
published: "2026-06-20T18:02:50Z"
age_days: 3
score: 38
created: 2026-06-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Whole-body humanoid loco-manipulation requires coordinating the robot's entire kinematic
chain. However, most existing systems typically decouple the upper and lower bodies into
separate controllers, limiting such coordination and yielding behaviors similar to those
of a wheeled dual-arm platform. In this paper, we ask what it takes to build a whole-
body native vision-language-action (VLA) model that maps language and pixels directly to
all of the humanoid's degrees of freedom. We conduct a systematic empirical study
organized as a roadmap of one-variable-at-a-time experiments across three phases: whole-
body teleoperation, VLA model design, and heterogeneous co-training. Our study yields
several intriguing findings: a joint-based whole-body teleoperation interface
outperforms alternatives that only partially expose the humanoid's degrees of freedom; a
VLA pretrained on static and wheeled dual-arm platforms transfers surprisingly well to a
humanoid's full action space; and co-training with HuMI, the humanoid analog of UMI,
extends the policy to new objects and instructions without additional whole-body
teleoperation on those targets. Following this roadmap yields OpenHLM, an open-source
recipe for whole-body humanoid loco-manipulation. In a challenging long-horizon task
that spans a wide vertical range of the humanoid, OpenHLM outperforms two state-of-the-
art humanoid VLA baselines (GR00T N1.6 and $Ψ_0$) using less than half the total
demonstration time. Our code, training data, and model checkpoints are available at
[https://openhlm-project.github.io/].

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22174v1
- Authors: Yingdong Hu, Haodong Zhu, Boyuan Zheng, Yihang Hu, Tong Zhang, Zunhao Chen, Junming Zhao, Ruiqian Nai, Yang Gao
- Published: 2026-06-20T18:02:50Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
