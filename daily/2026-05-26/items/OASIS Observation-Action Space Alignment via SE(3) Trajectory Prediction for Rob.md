---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25829v1"
published: "2026-05-25T13:28:33Z"
age_days: 0
score: 36
created: 2026-05-26
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Recent vision-language-action (VLA) models and world action models (WAMs) advance
robotic manipulation by enriching intermediate representations with auxiliary spatial
features or future visual-state prediction. However, these representations largely
remain within the observation space and do not share the rigid-body geometry of the
action space, forcing the action decoder to implicitly recover this geometry. We propose
OASIS, a visuomotor policy that aligns the intermediate representation with the action
space via $SE(3)$ end-effector trajectory prediction. OASIS couples a 3D-aware feature
encoder that fuses vision-language and metric-depth features with an $SE(3)$ trajectory
predictor that produces a camera-frame end-effector trajectory. Conditioned on the
predictor's pose-supervised hidden states, the action decoder generates action chunks
consistent with rigid-body motion. Across simulation and real-world experiments, OASIS
outperforms VLA and WAM baselines in success rate and out-of-distribution
generalization. Our project page is available at
https://npuhandsome.github.io/OASIS_web.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25829v1
- Authors: Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li, Xingyu Chen, Zeyang Liu, Xuguang Lan
- Published: 2026-05-25T13:28:33Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
