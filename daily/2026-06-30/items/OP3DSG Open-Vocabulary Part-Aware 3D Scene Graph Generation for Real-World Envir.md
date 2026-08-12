---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29786v1"
published: "2026-06-29T05:05:54Z"
age_days: 1
score: 35
created: 2026-06-30
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# OP3DSG: Open-Vocabulary Part-Aware 3D Scene Graph Generation for Real-World Environments

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

3D scene graphs (3DSGs) provide a compact and structured abstraction of 3D environments.
Although advances in foundation models have enabled open-vocabulary 3DSG generation,
existing approaches remain object-centric and encode limited relational information --
restricting their applicability in real-world scenarios that require fine-grained
understanding. We propose OP3DSG, an open-vocabulary part-aware 3DSG generation
framework that constructs unified graphs that jointly model objects, interactive parts,
spatial relations, functional relations, and affordances. OP3DSG integrates object-part
knowledge-guided detection with part-aware 3D fusion to preserve small and interaction-
relevant components, and employs a geometry-initialized prior graph with LLM-based
refinement to reduce spurious relational predictions while enabling efficient graph
construction. To systematically evaluate unified 3D scene graph construction, we
introduce UniGraph3D, a benchmark designed for part-aware perception and multi-level
relational reasoning. Experimental results show that OP3DSG achieves state-of-the-art
performance and demonstrates its effectiveness as a perception backbone in diverse real-
world robotics tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29786v1
- Authors: Yirum Kim, Ue-Hwan Kim
- Published: 2026-06-29T05:05:54Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
