---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2604.27792v2"
published: "2026-04-30T12:34:44Z"
score: 36
created: 2026-05-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# MotuBrain: An Advanced World Action Model for Robot Control

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-Language-Action (VLA) models generalize semantically well but often lack fine-
grained modeling of world dynamics. We present MotuBrain, a unified World Action Model
that jointly models video and action under a UniDiffuser formulation with a three-stream
Mixture-of-Transformers architecture. A single model supports policy learning, world
modeling, video generation, inverse dynamics, and joint video-action prediction, while
scaling to heterogeneous multimodal data such as video-only, task-agnostic, and cross-
embodiment robot data. Building on Motus, MotuBrain further introduces unified multiview
modeling, an independent text stream for stronger language-action coupling, a shared
cross-embodiment action representation, and an efficient post-training and deployment
recipe for long-horizon real-world control. Our inference stack combines step reduction,
compilation, FP8 quantization, DiT caching, V2A-style action-only inference, and real-
time chunked closed-loop execution, achieving over 50x speedup over a naive baseline and
up to 11 Hz inference. Experimentally, MotuBrain achieves 95.8% and 96.1% average
success on RoboTwin 2.0 under clean and randomized settings, respectively, attains the
strongest reported EWMScore in our WorldArena comparison, and adapts to new humanoid
embodiments with only 50--100 trajectories. These results show that unified world action
models can scale in generality, predictive accuracy, and real-world deployability.

## 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2604.27792v2
- Authors: MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, Runqing Wang, Shuhe Huang, Yao Feng, Yinze Rong, Zeyuan Wang, Jun Zhu
- Published: 2026-04-30T12:34:44Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
