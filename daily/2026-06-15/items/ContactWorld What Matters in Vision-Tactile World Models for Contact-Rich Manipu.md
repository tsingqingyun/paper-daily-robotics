---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13877v1"
published: "2026-06-11T20:01:49Z"
age_days: 3
score: 32
created: 2026-06-15
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Contact-rich manipulation requires world models to reason over complex contact dynamics
from multimodal sensory observations. However, it remains unclear which representation
properties fundamentally support stable long-horizon planning in contact-rich settings.
In this paper, we present ContactWorld, a benchmark and systematic empirical study of
vision-tactile world models spanning 12 contact-rich manipulation tasks, including
insertion, disassembly, screwing, and exploratory interaction. Across extensive
experiments, we find that representations that are both spatially structured and
temporally continuous consistently achieve the strongest planning performance. In
particular, point-cloud observations improve average planning success rates from 20.7%
with wrist-view observations and 22.0% with front-view observations to 32.1%. We further
find that the effectiveness of tactile sensing depends critically on cross-modal
representation compatibility rather than modality scaling alone. Combining point-cloud
observations with tactile force-field representations, which preserve richer spatial
structure and interaction dynamics, further improves performance to 36.1%, yielding the
strongest overall planning performance across all evaluated tasks. Moreover, tactile
sensing becomes increasingly important under long-horizon planning objectives, where
compounding prediction errors and contact uncertainty accumulate over time. Together,
these findings highlight the importance of representation structure, multimodal
compatibility, and long-horizon robustness in vision-tactile world models for contact-
rich robotic manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13877v1
- Authors: Zhiyuan Zhang, Pokuang Zhou, Kaidi Zhang, Adeesh Desai, Temitope Amosa, Davood Soleymanzadeh, Jiuzhou Lei, Minghui Zheng, Yu She
- Published: 2026-06-11T20:01:49Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
