---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18238v1"
published: "2026-05-18T11:32:12Z"
age_days: 1
score: 31
created: 2026-05-20
concepts: ["智能体 Agent"]
---

# Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning

## 为什么重要

自动筛选分数：31

连接概念：[[智能体 Agent]]

## 摘要

Digital entities such as AI agents and humanoid robots increasingly operate alongside
real humans, yet their identity infrastructure is based on credentials rather than
embodied biometric identity. We introduce Biometric Identity Provisioning (BIP), a new
problem and solution framework that addresses: given an enrollment gallery of real human
identities, provision virtual identities that are non-colliding with every enrolled
identity, maintain sufficient inter-class separability, and are realizable as high-
fidelity face images. The key geometric insight is that real face identities occupy a
low-dimensional subspace of the embedding hypersphere, leaving no residual subspace for
virtual identities. Hence, virtual identities must instead be allocated as unclaimed
gaps within the real face manifold itself. BIP is therefore a constrained packing
problem: available gaps vastly exceed any foreseeable enrollment scale, and provisioned
identities remain non-colliding even as new real identities are subsequently enrolled.
Grounded in this geometry, our repulsion-based allocation is not bounded by any fixed
provisioning count; we demonstrate 10M non-colliding virtual identity embeddings against
a gallery of 360K real identities. Realizing these embeddings as face images requires a
generator that operates outside the training distribution of real face images; we
introduce GapGen, a gap-aware generator trained with a curriculum that progressively
extends synthesis into non-colliding regions, validated at 1M photorealistic virtual
face images. We further construct v-LFW, a virtual counterpart to LFW face dataset, with
protocols for virtual face verification, cross-reality matching, real-vs-virtual
detection, and unified recognition and detection.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18238v1
- Authors: Yuyang Ji, Yixuan Shen, Anil Jain, Xiaoming Liu, Feng Liu
- Published: 2026-05-18T11:32:12Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
