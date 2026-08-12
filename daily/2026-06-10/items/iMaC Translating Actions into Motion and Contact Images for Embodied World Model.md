---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09813v1"
published: "2026-06-08T17:55:41Z"
age_days: 1
score: 40
created: 2026-06-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# iMaC: Translating Actions into Motion and Contact Images for Embodied World Models

## 为什么重要

自动筛选分数：40

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Embodied world models have emerged as a pivotal paradigm for visual robotic decision-
making and interactive environment simulation. However, conventional embodied frameworks
rely on low-dimensional structured action vectors (e.g., joint angles and end-effector
poses), which suffer from limited expressive capacity, poor generalization across
diverse embodiments, and unnatural dynamic modeling for complex physical interactions.
To address these limitations, this paper proposesiMac (Image as Action Control), a novel
unified control paradigm that treats raw visual images as native action representations
for embodied world models. Departing from traditional explicit kinematic action
encoding, iMac formulates continuous visual manipulation as image-based action tokens,
which inherently encapsulate spatial motion intentions, interactive geometric
constraints and subtle physical dynamics. We construct a dual-branch embodied
architecture consisting of an image-action encoder and a dynamic world predictor: the
encoder compresses target-driven visual images into compact action embeddings, while the
predictor learns environment transition rules conditioned on image actions to achieve
high-fidelity future state prediction and closed-loop embodied control. Extensive
experiments are conducted on public embodied manipulation benchmarks and real-world
robotic scenarios. The results demonstrate that iMac outperforms vector-based action
control baselines in prediction accuracy, task success rate and cross-scene
generalization ability. Moreover, our image-action design eliminates the reliance on
manually defined action spaces, realizing flexible and universal control for
heterogeneous embodied agents. This work provides an innovative visual-action
perspective for embodied world models, offering a simple yet effective paradigm for
scalable robotic perception and manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09813v1
- Authors: Zhenyu Wu, Xiuwei Xu, Yukun Zhou, Yifan Li, Qiuping Deng, Xiaofeng Wang, Zheng Zhu, Bingyao Yu, Ziwei Wang, Jiwen Lu, Haibin Yan
- Published: 2026-06-08T17:55:41Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
