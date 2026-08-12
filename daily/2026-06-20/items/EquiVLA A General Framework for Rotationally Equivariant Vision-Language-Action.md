---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19784v1"
published: "2026-06-18T04:36:57Z"
age_days: 1
score: 37
created: 2026-06-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models

## 为什么重要

自动筛选分数：37

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for generalist
robot manipulation, yet they lack geometric inductive biases: policies trained at
specific orientations require substantially more data to generalize across rotational
configurations. We present \textsc{EquiVLA}, the first general framework for end-to-end
$\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a
frozen vision-language backbone with a flow-matching Diffusion Transformer action head.
\textsc{EquiVLA} introduces \textsc{EquiPerceptor}, which produces approximately
$\mathrm{SO}(2)$-equivariant visual representations from frozen ViT features; and
\textsc{EquiActor}, an exactly $\mathrm{SO}(2)$-equivariant flow-matching Diffusion
Transformer action head. Together, they establish an approximate $\mathrm{SO}(2)$
equivariance chain from camera observations to predicted action sequences. Instantiated
on GR00T~N1.5 and evaluated across four LIBERO suites, CALVIN ABCD$\to$D, and five real-
robot tasks on Mobile ALOHA, \textsc{EquiVLA} achieves $92.6\%$ average success on
LIBERO (vs. $78.1\%$ baseline), an average sequence length of $4.03$ on CALVIN (vs.
$3.45$), and improves real-robot success from $54\%$ to $72\%$.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19784v1
- Authors: Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen, Gia-Binh Nguyen, Pham Tri Quang, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
- Published: 2026-06-18T04:36:57Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
