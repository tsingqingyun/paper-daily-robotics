---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13632v1"
published: "2026-05-13T14:58:29Z"
age_days: 0
score: 38
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

In this paper, we propose GTA-VLA(Guide, Think, Act), an interactive Vision-Language-
Action (VLA) framework that enables spatially steerable embodied reasoning by allowing
users to guide robot policies with explicit visual cues. Existing VLA models learn a
direct "Sense-to-Act" mapping from multimodal observations to robot actions. While
effective within the training distribution, such tightly coupled policies are brittle
under out-of-domain (OOD) shifts and difficult to correct when failures occur. Although
recent embodied Chain-of-Thought (CoT) approaches expose intermediate reasoning, they
still lack a mechanism for incorporating human spatial guidance, limiting their ability
to resolve visual ambiguities or recover from mistakes. To address this gap, our
framework allows users to optionally guide the policy with spatial priors, such as
affordance points, boxes, and traces, which the subsequent reasoning process can
directly condition on. Based on these inputs, the model generates a unified spatial-
visual Chain-of-Thought that integrates external guidance with internal task planning,
aligning human visual intent with autonomous decision-making. For practical deployment,
we further couple the reasoning module with a lightweight reactive action head for
efficient action execution. Extensive experiments demonstrate the effectiveness of our
approach. On the in-domain SimplerEnv WidowX benchmark, our framework achieves a state-
of-the-art 81.2% success rate. Under OOD visual shifts and spatial ambiguities, a single
visual interaction substantially improves task success over existing methods,
highlighting the value of interactive reasoning for failure recovery in embodied
control. Details of the project can be found here: https://signalispupupu.github.io/GTA-
VLA_ProjPage/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13632v1
- Authors: Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang, Xiaoke Jiang, Chuanxiu Liu, Jie Liu, Lei Zhang
- Published: 2026-05-13T14:58:29Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
