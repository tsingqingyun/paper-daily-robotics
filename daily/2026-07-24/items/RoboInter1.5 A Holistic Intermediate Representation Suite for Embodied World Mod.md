---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18709v2"
published: "2026-07-21T05:05:01Z"
age_days: 3
score: 41
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation

## 为什么重要

自动筛选分数：41

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Existing robot datasets remain expensive to curate, embodiment-specific, and
insufficiently annotated with the fine-grained structure required for generalizable
reasoning, execution, or long-horizon environment dynamics simulation. Building on our
prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of
intermediate representations for both robotic manipulation and embodied world modeling.
RoboInter1.5 provides a unified resource of data, benchmarks, and models centered on
dense manipulation-oriented intermediate representations. Specifically, RoboInter-Data
contains over 230k manipulation episodes across 571 scenes with dense per-frame
annotations covering more than ten types of intermediate representations, including
subtasks, primitive skills, object and gripper grounding, segmentation, affordance,
grasp poses, contact points, motion traces, etc. Built upon these annotations,
RoboInter-VQA introduces spatial and temporal embodied VQA tasks to benchmark and
improve the intermediate-representation reasoning capabilities of our RoboInter-VLM.
RoboInter-VLA further studies how such representations benefit action execution through
implicit, explicit, and modular plan-then-execute paradigms. To better model the
physical world, we further introduce RoboInter-World, which leverages intermediate
representations as structured conditioning signals for controllable prediction of future
world states. Extensive evaluations demonstrate that RoboInter1.5 provides a unified
spatiotemporal scaffolding for intermediate representations. Rather than treating
intermediate representations merely as interpretable signals, RoboInter1.5
conceptualizes them as a bidirectional interface that both regularizes low-level action
spaces and constrains the latent rollouts of open-world physical simulators.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18709v2
- Authors: Ziqin Wang, Hao Li, Weijun Wang, Junhao Cai, Jia Zeng, Yilun Chen, Jiangmiao Pang, Si Liu
- Published: 2026-07-21T05:05:01Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
