---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09572v1"
published: "2026-06-08T14:46:43Z"
age_days: 1
score: 33
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action models have shown strong promise for robot manipulation, yet raw
language is primarily needed to specify task intent rather than to be repeatedly
processed during high-frequency low-level execution. Motivated by this separation, we
propose a cerebello-thalamic-inspired vision-action model (CT-VAM) for efficient task-
conditioned visuomotor control. CT-VAM acts as a compact local execution policy that
predicts action chunks from dualview visual observations, proprioception, and a
lightweight task condition, potentially enabling a practical cloud-edge paradigm in
which high-level semantic reasoning can be handled by large models while fast closed-
loop control runs on local hardware. To fuse heterogeneous inputs effectively, CT-VAM
introduces TARS (Thalamic Action Routing Stream), a stream-separated conditional
attention decoder that independently routes action, visual and task streams, preventing
dense sensory tokens from overwhelming compact task-relevant conditions. With only 68M
parameters, CT-VAM achieves LIBERO success rates competitive with substantially larger
VLA models, while reducing inference latency. Together with flow-consistent inpainting
for asynchronous chunk execution, CT-VAM supports high-frequency control and
demonstrates robust realworld deployment on resource-constrained robotic platforms.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09572v1
- Authors: Jiacheng Li, Yize Guo, Jiabin Guo, Qingchen Liu, Jiahu Qin
- Published: 2026-06-08T14:46:43Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
