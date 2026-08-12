---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21049v1"
published: "2026-07-23T08:33:40Z"
age_days: 1
score: 25
created: 2026-07-25
concepts: ["世界模型", "机器人学习"]
---

# GuidedAttention: Interpretable and Correctable Visual Attention for OOD-Robust Robot Manipulation via Imitation Learning

## 为什么重要

自动筛选分数：25

连接概念：[[世界模型]], [[机器人学习]]

## 摘要

End-to-end visuomotor policies provide little opportunity for humans to understand or
correct the policy's visual attention. We propose GuidedAttention, a visuomotor
imitation learning framework that introduces interpretable and correctable visual
attention as an explicit intermediate representation. Task-relevant attention keypoints
are predicted from camera images and condition a diffusion-based action policy. Users
can inspect and optionally correct selected keypoints once at rollout initialization,
after which the corrected attention is automatically propagated throughout execution by
a tracking module. Experiments in simulation and the real world demonstrate that
GuidedAttention consistently improves robot manipulation performance, particularly under
positional and appearance out-of-distribution (OOD) conditions.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21049v1
- Authors: Masaki Murooka, Ryoichi Nakajo, Keisuke Shirai, Tomohiro Motoda, Hanbit Oh, Ryo Hanai, Yukiyasu Domae
- Published: 2026-07-23T08:33:40Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
