---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25407v1"
published: "2026-05-25T04:05:25Z"
age_days: 1
score: 29
created: 2026-05-26
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Towards Active Real-to-Twin Inspection: A New Paradigm for Zero-Shot Anomaly Detection

## 为什么重要

自动筛选分数：29

连接概念：[[世界模型]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

The deployment of zero-shot anomaly detection (AD) in embodied industrial inspection is
severely bottlenecked by its reliance on passive, fixed-viewpoint 2D imagery. Such
formulations inherently fail to accommodate the active, dynamic observations required in
real-world environments. To break this limitation, we introduce Real-to-Twin Anomaly
Detection, a novel task that evaluates physical observations directly against
geometrically matched CAD Digital Twins. To tackle this new task, we propose AVATAR, a
framework designed to learn robust semantic alignment between Real and Digital Twins. By
bridging benign Sim2Real domain gaps using only defect-free pairs, AVATAR effectively
transforms CAD priors into dynamic, anomaly-free references. This elegant formulation
enables the model to localize diverse anomalies in a zero-shot manner as unalignable
deviations, eliminating the need for defect annotations. Extensive experiments
demonstrate that AVATAR substantially outperforms adapted state-of-the-art baselines,
exhibiting exceptional robustness to severe viewpoint variations. The code and dataset
will be made publicly available.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25407v1
- Authors: Jiaxuan Liu, Yunkang Cao, Yufeng Chen, Chunyang Li, Yuhuan Du, Hui Zhang
- Published: 2026-05-25T04:05:25Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
