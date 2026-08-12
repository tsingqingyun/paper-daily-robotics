---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13102v1"
published: "2026-06-11T09:30:09Z"
age_days: 1
score: 31
created: 2026-06-13
concepts: ["机器人学习", "具身智能评测与基准"]
---

# FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation

## 为什么重要

自动筛选分数：31

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Despite the success of vision-based generalist robotic policies, existing tactile-based
policies remain tied to fixed embodiments and sensor setups. This is because tactile
signals are highly heterogeneous across hardware, making cross-sensor generalization
difficult. We present FTP-1,the first generalist foundation tactile policy pretrained to
acquire transferable tactile manipulation abilities across diverse sensors and
embodiments. FTP-1 supports varied tactile inputs, including image-, array-, and state-
based signals, by using heterogeneous encoders to project them into unified morphology-
aware latent tokens that are jointly modeled by a shared tactile Transformer expert.
Pretrained on around 3,000 hours of tactile manipulation data aggregated from 26 data
sources, spanning human and robot demonstrations across 21 sensors, FTP-1 learns tactile
skills that transfer beyond the sensors seen during pretraining. Across downstream
finetuning experiments spanning 5 hardware configurations, FTP-1 improves contact-rich
manipulation on seen sensor setups by +17.2% and, surprisingly, transfers to two
previously unseen tactile-sensor setups, achieving a +31% gain in success rate. FTP-1
establishes the first unified foundation baseline for tactile manipulation, providing
future tactile policies with a shared model-level starting point. Pretrained models,
datasets, training code and more visualization at https://ftp1-policy.github.io.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13102v1
- Authors: Chengbo Yuan, Zicheng Zhang, Mingjie Zhou, Wendi Chen, Yi Wang, Zhuoyang Liu, Dantong Niu, Shuo Wang, Hui Zhang, Wenkang Zhang, Yingdong Hu, Yuanqing Gong, Wanli Xing, Chuan Wen, Cewu Lu, Kaifeng Zhang, Yang Gao
- Published: 2026-06-11T09:30:09Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
