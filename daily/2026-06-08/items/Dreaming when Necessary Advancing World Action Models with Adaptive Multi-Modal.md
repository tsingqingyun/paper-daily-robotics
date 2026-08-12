---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07089v1"
published: "2026-06-05T09:35:48Z"
age_days: 2
score: 29
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]]

## 摘要

World Action Models (WAMs) offer a promising approach to embodied intelligence, yet
existing methods rely heavily on video prediction as action priors and lack adaptive
multimodal reasoning, limiting their effectiveness on long-horizon, complex tasks. We
observe that WAMs require different multimodal reasoning modes under different execution
contexts: textual reasoning is essential during task transitions to guide high-level
action prediction, while visual reasoning is critical during fine-grained manipulation
for precise control. Motivated by this observation, we propose \textbf{AdaWAM}, a world
action model with adaptive multimodal reasoning abilities. AdaWAM integrates a
lightweight dynamic router that autonomously triggers textual or visual reasoning as
needed during task execution. Experiments on both simulated and real-world embodied
tasks show that AdaWAM substantially improves inference efficiency while outperforming
state-of-the-art embodied policies. Codes and demos are available at:
https://adawam.github.io/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07089v1
- Authors: Yinzhou Tang, Jingbo Xu, Yu Shang, Zihao Song, Chen Gao, Wei Wu, Yong Li
- Published: 2026-06-05T09:35:48Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
