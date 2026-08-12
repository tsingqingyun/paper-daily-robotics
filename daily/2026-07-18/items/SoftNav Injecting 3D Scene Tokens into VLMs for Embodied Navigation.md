---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14586v1"
published: "2026-07-16T05:32:52Z"
age_days: 1
score: 29
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent"]
---

# SoftNav: Injecting 3D Scene Tokens into VLMs for Embodied Navigation

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[智能体 Agent]]

## 摘要

In goal-directed embodied navigation, where an agent must locate a specified target in
an unseen environment, 3D scene understanding and navigation reasoning must work in
concert. Current approaches transmit 3D scene information to vision-language models
(VLMs) through text, suggesting a representation gap in our tested configurations; a
controlled ablation confirms that direct embedding-level transfer significantly
outperforms the evaluated text serialization formats. We introduce SoftNav, which
injects entity-level 3D continuous representations -- one token per detected object or
frontier -- into a VLM's hidden space as soft tokens through a lightweight projector.
With the 3D encoder and VLM frozen, only ~1,200 samples and ~17M trainable parameters
are needed. On HM3D-OVON, SoftNav achieves 74.2%/68.3%/66.7% SR across three splits,
surpassing all prior methods in both SR and SPL; the same navigation policy transfers
zero-shot to GOAT-Bench (67.2% SR), SG3D (47.2% s-SR), and real-world robot deployment
without retraining or architectural modification. Injecting 3D scene tokens directly
into VLMs bridges the representation gap, enabling transferable navigation with minimal
training.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14586v1
- Authors: Yi Wu, Junjie An, Xiao Liu, Yiqun Zhou, Yuechen Wu, Xiaoqing Guan, Shuyang Yu, You Wang, Guang Li
- Published: 2026-07-16T05:32:52Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
