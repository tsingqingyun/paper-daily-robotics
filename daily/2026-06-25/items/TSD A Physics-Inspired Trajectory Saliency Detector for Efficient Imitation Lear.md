---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23371v1"
published: "2026-06-22T14:06:04Z"
age_days: 2
score: 31
created: 2026-06-25
concepts: ["世界模型", "机器人学习"]
---

# TSD: A Physics-Inspired Trajectory Saliency Detector for Efficient Imitation Learning

## 为什么重要

自动筛选分数：31

连接概念：[[世界模型]], [[机器人学习]]

## 摘要

For imitation learning in robotic manipulation, high data collection costs result in the
scarcity of high quality data. In this paper, we leverage the inherent heterogeneity of
trajectories to address this challenge. Based on our observations of manipulation tasks,
we categorize motions into transitional, precise, and agile types, defining the latter
two as trajectory saliency due to their criticality to task success in contrast to the
prevalent but less relevant transitional motions. Therefore, we propose the Trajectory
Saliency Detector (TSD), a training-free and plug-and-play framework to identify
trajectory saliency. TSD employs two physically-grounded metrics: spatial entropy to
capture fine-grained manipulation and centripetal acceleration to detect agile
maneuvering. We further leverage TSD to develop a dataset compression method that
reduces training costs and a dataset expansion strategy that improves data collection
efficiency. Extensive experiments in both simulation and real-world settings demonstrate
that models trained on TSD-condensed datasets achieve comparable or even superior
performance with 25% less data on average. These results validate the effectiveness of
our dataset compression and expansion strategies, thereby confirming the utility of TSD.
Consequently, TSD offers a scalable and cost-effective pathway to synthesize
information-dense datasets for efficient robot learning. Project page:
https://trajectory-saliency-detector.github.io/trajectory-saliency-detector/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23371v1
- Authors: Yiming Zhao, Gongrui Ma, Qingkai Li, Mingguo Zhao
- Published: 2026-06-22T14:06:04Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
