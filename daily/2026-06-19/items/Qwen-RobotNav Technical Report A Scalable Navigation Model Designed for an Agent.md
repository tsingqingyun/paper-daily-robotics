---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18112v1"
published: "2026-06-16T16:17:44Z"
age_days: 2
score: 28
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Agentic navigation systems require a base navigation model whose observation strategy
can be externally reconfigured at inference time, because instruction following, object
search, target tracking, and autonomous driving share the same perception-planning
backbone yet demand fundamentally different strategies for consuming the visual stream.
We present Qwen-RobotNav, a scalable navigation model built on Qwen-RobotNav that
addresses it through a parameterised interface with two complementary dimensions:
multiple task modes that select the navigation behaviour, and controllable observation
parameters (e.g., token budget, per-camera weights) that govern how visual history is
encoded. With training-time randomization over all parameters, Qwen-RobotNav is robust
to any inference-time configuration requiring zero architectural modification to the
Qwen-RobotNav backbone. We train Qwen-RobotNav on 15.6M samples; co-training with
vision-language data prevents the collapse into reactive action-sequence mappers
observed in trajectory-only training. The parameterised interface also makes Qwen-
RobotNav a natural building block for agentic systems: for long-horizon scenarios, an
upper-level planner decomposes goals into sub-tasks and dynamically switches Qwen-
RobotNav's task mode and context strategy mid-episode, composing complex behaviours from
repeated calls to the same model. Extensive experiments show that Qwen-RobotNav sets new
state-of-the-art results across major navigation benchmarks. The model exhibits
favourable scaling from 2B to 8B parameters, with joint multi-task training developing a
shared spatial-planning substrate that transfers across task families, and demonstrates
strong zero-shot generalisation to real-world robots across diverse environments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18112v1
- Authors: Jiazhao Zhang, Gengze Zhou, Hale Yin, Yiyang Huang, Zixing Lei, Qihang Peng, Haoqi Yuan, Jie Zhang, Xudong Guo, Xiaoyue Chen, An Yang, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou, Zhuoyuan Yu, Jingyang Fan, Zhixuan Liang, Pei Lin, Ye Wang, Anzhe Chen, Kun Yan, Xiao Xu, Jiahao Li, Lulu Hu, Minying Zhang, Shurui Li, Wenhu Xiao, Shuai Bai, Xuancheng Ren, Chenxu Lv, Chenfei Wu, Xiong-Hui Chen
- Published: 2026-06-16T16:17:44Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
