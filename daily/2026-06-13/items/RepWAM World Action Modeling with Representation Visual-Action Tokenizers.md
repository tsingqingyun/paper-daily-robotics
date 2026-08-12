---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13674v1"
published: "2026-06-11T17:59:43Z"
age_days: 1
score: 39
created: 2026-06-13
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RepWAM: World Action Modeling with Representation Visual-Action Tokenizers

## 为什么重要

自动筛选分数：39

连接概念：[[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

This work presents RepWAM, a representation-centric world action model (WAM) built on
representation visual-action tokenizers. Existing WAMs typically inherit reconstruction-
oriented video tokenizers from pretrained video generation models. Although these
tokenizers preserve visual fidelity, pixel reconstruction alone provides limited
guidance for learning instruction-following dynamics that connect future prediction with
robot control. To address this, we explore a semantic visual-action latent space for
representation-centric world action modeling. Specifically, we train a representation
visual-action tokenizer that maps visual inputs into aligned visual and latent action
tokens. We then pretrain our WAM to jointly model future visual states and the latent
actions that connect them under language instructions, followed by adaptation to real
robot trajectories for closed-loop manipulation. Experiments on real-world manipulation
tasks and simulation benchmarks show that RepWAM delivers strong performance across
diverse manipulation settings, while ablations highlight the value of semantic visual-
action tokenization over reconstruction-oriented alternatives. These results establish
representation visual-action tokenization as a promising foundation for world action
models and a step toward generalist robot policies. Code and weights will be available
at https://github.com/wdrink/RepWAM.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13674v1
- Authors: Junke Wang, Qihang Zhang, Shuai Yang, Yiming Luo, Yujun Shen, Zuxuan Wu, Yu-Gang Jiang, Yinghao Xu
- Published: 2026-06-11T17:59:43Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
