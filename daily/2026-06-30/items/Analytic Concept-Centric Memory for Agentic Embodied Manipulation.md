---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29774v1"
published: "2026-06-29T04:33:04Z"
age_days: 1
score: 28
created: 2026-06-30
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Analytic Concept-Centric Memory for Agentic Embodied Manipulation

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Long-horizon embodied manipulation requires agents to remember persistent objects, track
changing scene states, and reuse prior interaction knowledge. However, existing agent
memories are often stored as unstructured histories or embedding-based records, making
it difficult to retrieve manipulation-relevant object parts, physical states, action
effects, and executable skills. We propose an analytic concept-centric memory framework
for agentic embodied manipulation. Our memory organizes experience around structured
analytic concepts, where objects are represented by semantic parts, parametric
templates, grounded poses, affordances, and manipulation states. It further connects
object and scene memories with transition memory for action-induced state changes and
skill memory for template-grounded and policy-grounded execution. At runtime, the agent
performs structured coarse-to-fine retrieval to identify relevant objects, states,
transitions, and skills, supporting state-consistent reasoning and skill reuse.
Experiments on memory-dependent manipulation, articulated-object generalization, real-
world memory evaluation, and ablations show that our approach improves task completion,
retrieval accuracy, object re-identification, and cross-object skill generalization over
unstructured and embedding-based memory baselines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29774v1
- Authors: Mingyang Sun, Xiujian Liang, Jiude Wei, Qichen He, Donglin Wang, Cewu Lu, Jianhua Sun
- Published: 2026-06-29T04:33:04Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
