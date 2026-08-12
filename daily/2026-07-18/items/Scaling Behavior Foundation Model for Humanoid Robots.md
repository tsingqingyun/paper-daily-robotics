---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15163v1"
published: "2026-07-16T16:08:27Z"
age_days: 1
score: 34
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# Scaling Behavior Foundation Model for Humanoid Robots

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]]

## 摘要

Humanoid control requires natural whole-body coordination, precise real-time responses
to control signals, and robust generalization across diverse environmental contexts,
making it a cornerstone for generalist embodied agents. Behavior Foundation Models
(BFMs) have recently emerged as a promising solution to address these challenges by
leveraging large-scale behavioral data to achieve superior expressiveness, versatility
and generalization. However, despite growing interest in scaling BFMs to further improve
their capabilities, it remains unclear how key factors, including the learning paradigm,
behavioral data and model architecture should be coordinated to enable effective
scaling. In this work, we revisit the scaling recipe for BFMs and demonstrate that
substantial performance gains can be achieved through the coordination of three core
components: 1) the learning paradigm of motion tracking that reformulates diverse
humanoid control problems as the reproduction of integrated whole-body behaviors in the
global frame; 2) the strategic synergy between on-policy rollout quantity and reference
motion diversity; and 3) the expressive and scalable model architecture termed Humanoid
Transformer that facilitates the natural emergence of structured behavioral
representations. Through extensive experiments in both simulation and real-world
deployment, we demonstrate that our approach yields significant improvements in control
fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on
the test set by over 10% in local mode and 82% in global mode compared with existing
humanoid controllers. These results establish BFM as a principled and effective
foundation for scalable and general-purpose humanoid control.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15163v1
- Authors: Weishuai Zeng, Kangning Yin, Xiaojie Niu, Shunlin Lu, Weixiang Zhong, Jiahe Chen, Feiyu Jia, Xiao Chen, Zirui Wang, Furui Xu, Ming Zhou, Kailin Li, Weinan Zhang, He Wang, Li Yi, Dahua Lin, Jiangmiao Pang, Jingbo Wang
- Published: 2026-07-16T16:08:27Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
