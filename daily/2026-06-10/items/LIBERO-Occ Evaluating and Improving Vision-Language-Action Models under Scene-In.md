---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10862v1"
published: "2026-06-09T13:39:49Z"
age_days: 0
score: 32
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models achieve strong performance on standard manipulation
benchmarks, but most evaluations assume that task-relevant objects are fully visible.
This assumption often fails in realistic settings, where occlusion makes manipulation
partially observable. In this paper, we study \textit{scene-induced occlusion} as a
fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-
oriented extension of LIBERO. Experiments show that state-of-the-art VLAs suffer
substantial performance degradation under occlusion. To address this issue, we propose
\textbf{Viewpoint Imagination (VIM)}, which generates a complementary view from an
occluded primary observation and conditions action prediction on both observed and
imagined evidence. VIM improves robustness across task suites, occlusion types, and
severity levels without requiring additional cameras at deployment time, suggesting that
viewpoint imagination is an promising mechanism for perception completion in partially
observable manipulation. Our benchmark and corresponding code are available at:
\href{https://github.com/litsh/Libero-Occ}{https://github.com/litsh/Libero-Occ}.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10862v1
- Authors: Taishan Li, Jiwen Zhang, Siyuan Wang, Xuanjing Huang, Zhongyu Wei
- Published: 2026-06-09T13:39:49Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
