---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Embodied AI and Robotics"
url: "https://arxiv.org/abs/2605.06311v1"
published: "2026-05-07T14:13:05Z"
score: 30
created: 2026-05-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "Sim2Real", "具身智能评测与基准"]
---

# Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Reliable simulation evaluation of robot manipulation policies serves as a high-fidelity
proxy for real-world performance. Although existing benchmarks cover a wide range of
task categories, they lack visual realism, creating a large domain gap between
simulation and reality. This undermines the reliability of simulation-based evaluation
in predicting real-world performance. To mitigate the sim-to-real visual gap, we conduct
a systematic analysis to isolate the effects of lighting and material. Our results show
that these factors play a critical role in geometric reasoning and spatial grounding,
yet are largely overlooked in existing benchmarks. Motivated by the analysis, we propose
VISER, a visually realistic benchmark for evaluating robot manipulation in simulation.
VISER features a high-fidelity dataset of over 1,000 3D assets with physically-based
rendering (PBR) materials, along with 3D scenes created from these assets through
curated layouts or generation. To this end, we propose an automated pipeline leveraging
Multi-modal Large Language Models (MLLMs) for material-aware part segmentation and
material retrieval, enabling scalable generation of physically plausible assets.
Building on the high-fidelity 3D asset dataset, we construct diverse evaluation tasks,
such as grasping, placing, and long-horizon tasks, enabling scalable and reproducible
assessment of Vision-Language-Action (VLA) models. Our benchmark shows a strong
correlation between simulation and real-world performance, achieving an average Pearson
correlation coefficient of 0.92 across different policies.

## 来源

- Source: arXiv Daily - Embodied AI and Robotics
- URL: https://arxiv.org/abs/2605.06311v1
- Authors: Yixin Zhu, Zixiong Wang, Jian Yang, Jin Xie, Jingyi Yu, Jiayuan Gu, Beibei Wang
- Published: 2026-05-07T14:13:05Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
