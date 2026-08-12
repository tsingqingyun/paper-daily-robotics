---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15880v1"
published: "2026-07-17T11:50:03Z"
age_days: 2
score: 34
created: 2026-07-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习"]
---

# Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

Imitation Learning aims to learn skills from extensive observations and demonstrations
for robots, so it suffers from data scarcity and environment generalization. The
existing methods predominantly focus on imitation from in-domain tasks and consequently
struggle with generalization to unseen tasks. To bridge this generalization gap, we
propose the \textbf{D}ynamics-\textbf{A}ware \textbf{M}eta-\textbf{I}mitation (DAMI)
framework. By integrating meta-learning to construct a shared skill space, DAMI equips
agents for rapid adaptation to novel tasks. We introduce the Visual-Motor Trajectory
(VMT) module to capture complex spatio-temporal dynamics within the task latent space.
Furthermore, we propose the Unpaired Unified Task (U2T) block to fuse unstructured
multimodal observations. To coordinate these representations, we integrate a Task-
Conditioned Feature Modulation (TCFM) mechanism customized for modulating low-level 3D
features. By capturing intrinsic dynamics from a random complete reference
demonstration, our framework learns the underlying task logic rather than memorizing
static cues, ensuring effective generalization. Extensive experiments in both simulation
and real-world settings demonstrate that our approach outperforms state-of-the-art
baselines regarding direct inference on seen tasks and adaptation to unseen tasks via
few-shot fine-tuning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15880v1
- Authors: Zhenduo Shang, Xiyao Liu, Bohan Li, Xudong Wang, Teng Ren, Lianqing Liu, Zhi Han
- Published: 2026-07-17T11:50:03Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
