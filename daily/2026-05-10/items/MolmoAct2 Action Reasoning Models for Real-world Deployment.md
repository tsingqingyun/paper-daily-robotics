---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2605.02881v1"
published: "2026-05-04T17:51:21Z"
score: 41
created: 2026-05-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MolmoAct2: Action Reasoning Models for Real-world Deployment

## 为什么重要

自动筛选分数：41

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models aim to provide a single generalist controller for
robots, but today's systems fall short on the criteria that matter for real-world
deployment. Frontier models are closed, open-weight alternatives are tied to expensive
hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and
fine-tuned success rates remain below the threshold for dependable use. We present
MolmoAct2, a fully open action reasoning model built for practical deployment, advancing
its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for
spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-
rehearse recipe. We release three new datasets spanning low-to-medium cost platforms,
including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that
constitute the largest open bimanual dataset to date, together with quality-filtered
Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data
action tokenizer trained on millions of trajectories across five embodiments. We
redesign the architecture to graft a flow-matching continuous-action expert onto a
discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink,
an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions
that change between timesteps, retaining geometric grounding at a fraction of prior
latency. In the most extensive empirical study of any open VLA to date, spanning 7
simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including
Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-
reasoning benchmarks. We release model weights, training code, and complete training
data. Project page: https://allenai.org/blog/molmoact2

## 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2605.02881v1
- Authors: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
- Published: 2026-05-04T17:51:21Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
