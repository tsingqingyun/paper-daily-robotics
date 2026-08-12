---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14548v1"
published: "2026-07-16T04:12:42Z"
age_days: 1
score: 29
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]]

## 摘要

As large multimodal models move from understanding content to operating on digital
environments, mobile GUI has emerged as a challenging and consequential testbed for
digital embodied intelligence. Mobile agents operate under three coupled constraints:
precise perception of complex interfaces, scalable acquisition of high-quality
interaction data, and robust long-horizon decision making under compounding execution
errors. This report presents HyMobileAgent, a mobile GUI agent built on Hy3.0-VL-A3B, a
vision-native foundation model featuring native any-resolution input, an A3B-scale
deployment budget, and a 32K context window to model extended interaction histories.
Rather than relying solely on model scaling, we develop a joint data and environment
centric scaling framework to address the key bottlenecks of mobile interaction. Our
framework integrates a GUI perception flywheel combining mock-interface synthesis,
rejection sampling, and icon-specific augmentation; a knowledge pipeline that transforms
tutorial videos into structured interaction data; a million-scale action data pipeline
deployed across more than 2000 sandbox and real-device instances with automated failure
attribution; the PhoneWorld Mock App Factory, providing a resettable training
environment with 34 mock applications and over 34000 tasks; and a structured Planning-
and-Reflection mechanism with explicit dead-loop detection for reliable long-horizon
execution. We also introduce a progressive training recipe consisting of mid-training,
supervised fine-tuning, and reinforcement learning with task-specific reward designs.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14548v1
- Authors: Hy Vision Team, Huawen Shen, Zhengyang Tang, Shangpin Peng, Liang Wu, Anran Zhang, Weinong Wang, Yiduo Guo, Chenxin Li, Zhengyao Fang, Yang Ding, Junyi Li, Fei Tang, Zheng Ruan, Yi Zhang, Xingran Zhou, Dingchen Yang, Sunqi Fan, Zhiyi Wan, Han Hu, Xin Lai, Pengyuan Lyu, Chengquan Zhang
- Published: 2026-07-16T04:12:42Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
