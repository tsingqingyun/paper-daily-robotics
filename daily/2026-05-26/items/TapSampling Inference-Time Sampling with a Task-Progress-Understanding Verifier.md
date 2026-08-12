---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25547v1"
published: "2026-05-25T08:03:31Z"
age_days: 0
score: 33
created: 2026-05-26
concepts: ["AI 核心知识地图"]
---

# TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation

## 为什么重要

自动筛选分数：33

连接概念：[[AI 核心知识地图]]

## 摘要

Existing embodied control research demonstrates remarkable performance improvements by
scaling training data and model size. We instead explore inference-time strategy as an
alternative axis. Non-deterministic generative models, such as diffusion and
autoregressive models, have been widely adopted in the field of embodied control.
However, the single-shot inference paradigm limits their performance. In this paper, we
propose \textbf{TapSampling}, a plug-and-play framework for inference-time sampling.
First, we introduce an Action-VAE that represents actions in a low-dimensional latent
space by mapping policy-generated initial actions into a compressed posterior
distribution, from which any number of latent samples can be drawn and decoded into
candidate actions that approximate the true action distribution. Second, we formulate
action verification as task-progress outcome prediction, using the intrinsic sequential
structure of robotic datasets to train a semantically grounded verifier for
interpretable action selection. Furthermore, TapSampling is a policy-agnostic framework.
Extensive experiments in both simulated and real-world environments demonstrate that our
method substantially improves multiple generalist policies without further policy
finetuning. Code and models are available at the project page.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25547v1
- Authors: Sizhe Zhao, Shengping Zhang, Shuo Yang, Weiyu Zhao, Shuigen Wang, Xiangyang Ji
- Published: 2026-05-25T08:03:31Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
