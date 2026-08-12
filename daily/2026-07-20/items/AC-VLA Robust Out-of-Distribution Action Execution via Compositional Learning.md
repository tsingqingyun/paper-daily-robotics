---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15714v1"
published: "2026-07-17T07:51:03Z"
age_days: 2
score: 35
created: 2026-07-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AC-VLA: Robust Out-of-Distribution Action Execution via Compositional Learning

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models excel at end-to-end robotic manipulation but
struggle with out-of-distribution (OOD) generalization when familiar sub-tasks are
recombined in unseen configurations. We identify two mutually reinforcing failure modes:
\emph{trajectory overfitting}, where models overfit to holistic trajectory patterns
rather than compositional sub-skill semantics; and \emph{perceptual shortcut}, where
action tokens over-rely on wrist-view textures at the expense of global spatial
grounding. To address both, we introduce \textbf{AC-VLA}, a plug-and-play Action
Compositional learning framework comprising two architecture-agnostic components:
\textbf{(i)} a compositional learning module that uses an LLM-driven instruction
decomposer and a proprioceptive trajectory aligner to generate dense sub-task
supervision, followed by mixed training on complete demonstrations and decomposed data
to endow the model with compositional generalization; and \textbf{(ii)} a state-
conditioned asymmetric masking strategy that suppresses wrist-view inputs during closed-
gripper phases, enforcing global semantic grounding. All components are architectural
modification-free and directly integrable into any VLA backbone. Instantiated on
$π_{0.5}$ and evaluated on LIBERO and LIBERO-OOD benchmarks, AC-VLA achieves a ~28%
absolute improvement on compositional OOD tasks while maintaining near-perfect in-
distribution performance.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15714v1
- Authors: Xiaojiang Peng, Kai Peng, Jie Lu, Zheng Lian, Zitong YU, Xiaobo Wang
- Published: 2026-07-17T07:51:03Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
