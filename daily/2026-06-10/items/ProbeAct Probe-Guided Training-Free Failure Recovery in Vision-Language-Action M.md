---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09740v1"
published: "2026-06-08T17:04:24Z"
age_days: 1
score: 42
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# ProbeAct: Probe-Guided Training-Free Failure Recovery in Vision-Language-Action Models

## 为什么重要

自动筛选分数：42

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models demonstrate strong perfor-1 mance on language-
conditioned robotic manipulation within their training dis-2 tribution, yet their
generalization capabilities remain fundamentally limited. They3 lack the robustness
required to handle perturbations, frequently failing when con-4 fronted with lighting
changes, altered camera viewpoints, or small initial-state5 variations. We propose
PROBEACT, a training-free runtime intervention frame-6 work that detects and recovers
from grasping and placement failures in pre-7 trained VLA policies without modifying
their weights or requiring additional8 demonstrations. PROBEACT combines three
components: (i) a lightweight multi-9 target hidden-state probe that predicts the 3D
positions of task-relevant objects10 from intermediate VLA features, with Hungarian-
matched identity tracking for11 multi-object scenes; (ii) an object-agnostic kinematic
state machine that detects12 grasp, transport, and placement failures using only
gripper-internal signals and13 end-effector kinematics; and (iii) a hierarchical Control
Barrier Function (CBF)14 filter that encodes repeated-failure locations as soft safe-set
constraints, mini-15 mally correcting VLA actions while preserving baseline behavior. As
a plug-and-16 play, training-free intervention loop, PROBEACT is orthogonal to existing
train-17 ing pipelines. Evaluated on the LIBERO-plus benchmark, our framework acts as18
a universal safety net, improving the success rate of the OpenVLA-OFT model19 from 69.6%
to 74.1%, while demonstrating broad applicability to both base and20 fine-tuned VLA
policies.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09740v1
- Authors: Fan Zhang, Seongbin Park, Baharan Mirzasoleiman, Shariar Talebi, Nader Sehatbakhsh
- Published: 2026-06-08T17:04:24Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
