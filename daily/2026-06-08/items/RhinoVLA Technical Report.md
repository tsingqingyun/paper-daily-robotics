---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07383v1"
published: "2026-06-05T15:21:41Z"
age_days: 2
score: 37
created: 2026-06-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# RhinoVLA Technical Report

## 为什么重要

自动筛选分数：37

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Vision-Language-Action (VLA) models have shown strong potential for robotic
manipulation, but real-time deployment on edge hardware remains challenging. In this
work, we identify VLM visual and context tokens as a major source of deployment latency:
for GEMM-dominated projection operators, computation grows linearly with the number of
input tokens when model dimensions are fixed. Motivated by this observation, we propose
RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC.
RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert,
reducing the VLM-side token and computation burden while preserving pretrained
multimodal capability. To support cross-robot learning, RhinoVLA further introduces a
unified interface that combines View Registry, 72D physical state-action slot space, and
robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be
aligned under a shared policy. On the deployment side, RhinoVLA is optimized through
hardware-aware compilation, mixed-precision execution, and parallel visual encoding.
Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a
similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1,
meeting the 10 Hz real-time closedloop control target. The project will be open-sourced
at https://github.com/HuixiAI/RhinoVLA.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07383v1
- Authors: Huixi Intelligence, :, Chen Zhang, Chenyang Zhou, Guanglei Ding, Guanghui He, Haibin Gao, Jiajia Chen, Jianyong Zhang, Lianyi Yu, Ningyi Xu, Ping Xu, Qingchen Li, Yingjun Hu, Yijia Zhang, Yuxi Liu
- Published: 2026-06-05T15:21:41Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
