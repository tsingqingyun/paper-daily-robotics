---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13328v1"
published: "2026-05-13T10:41:24Z"
age_days: 0
score: 33
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# What Limits Vision-and-Language Navigation ?

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-and-Language Navigation (VLN) is a cornerstone of embodied intelligence. However,
current agents often suffer from significant performance degradation when transitioning
from simulation to real-world deployment, primarily due to perceptual instability (e.g.,
lighting variations and motion blur) and under-specified instructions. While existing
methods attempt to bridge this gap by scaling up model size and training data, we argue
that the bottleneck lies in the lack of robust spatial grounding and cross-domain
priors. In this paper, we propose StereoNav, a robust Vision-Language-Action framework
designed to enhance real-world navigation consistency. To address the inherent gap
between synthetic training and physical execution, we introduce Target-Location Priors
as a persistent bridge. These priors provide stable visual guidance that remains
invariant across domains, effectively grounding the agent even when instructions are
vague. Furthermore, to mitigate visual disturbances like motion blur and illumination
shifts, StereoNav leverages stereo vision to construct a unified representation of
semantics and geometry, enabling precise action prediction through enhanced depth
awareness. Extensive experiments on R2R-CE and RxR-CE demonstrate that StereoNav
achieves state-of-the-art egocentric RGB performance, with SR and SPL scores of 81.1%
and 68.3%, and 67.5% and 52.0%, respectively, while using significantly fewer parameters
and less training data than prior scaling-based approaches. More importantly, real-world
robotic deployments confirm that StereoNav substantially improves navigation reliability
in complex, unstructured environments. Project page: https://yunheng-
wang.github.io/stereonav-public.github.io.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13328v1
- Authors: Yunheng Wang, Yuetong Fang, Taowen Wang, Lusong Li, Kun Liu, Junzhe Xu, Zizhao Yuan, Yixiao Feng, Jiaxi Zhang, Wei Lu, Zecui Zeng, Renjing Xu
- Published: 2026-05-13T10:41:24Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
