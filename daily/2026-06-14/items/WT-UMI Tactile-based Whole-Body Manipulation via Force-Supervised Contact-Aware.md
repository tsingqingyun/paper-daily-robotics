---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13232v1"
published: "2026-06-11T11:45:58Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Whole-body humanoid manipulation of bulky, deformable, and shared-load objects requires
distributed contact sensing and explicit force regulation, yet most imitation policies
treat contact force only implicitly. On the other hand, different demonstration sources
provide complementary modalities with inherent trade-offs: human demonstrations capture
natural contact forces but not robot-executable actions, while teleoperation directly
records robot actions but with less natural force regulation. This paper presents
\textbf{WT-UMI}, a wearable whole-body tactile interface worn by human operators or
mounted on humanoids, providing accurate observations of tactile images, contact forces,
and end-effector poses across both human demonstration and humanoid teleoperation modes.
We introduce a force-conditioned target-pose correction module that converts measured
human poses into contact-aware robot targets by learning corrections from teleoperation
data. To leverage the natural force interaction in human data, we propose a force-
supervised planner that predicts end-effector pose chunks and contact-force
trajectories. The predicted contact force serves as the reference for a tactile-based
admittance controller. Across five contact-rich tasks spanning deformable objects, bulky
rigid objects, and human--humanoid collaboration, WT-UMI improves success rate and
reduces contact-position tracking error over four policy baselines. Our project page is
available at https://wt-umi.github.io/WTUMI/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13232v1
- Authors: Jaehwi Jang, Zhaoyuan Gu, Alfred Cueva, Zimeng Chai, Junjie Sheng, Thong Nguyen, Himank Galundia, Yifan Wu, Huishu Xue, Isaac Legene, Ojas Mediratta, Davin Doan, Andrew Collins, Sarah Sadegh, KyoungMok Kim, Rishita Dhalbisoi, Zun Chen, Ye Zhao
- Published: 2026-06-11T11:45:58Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
