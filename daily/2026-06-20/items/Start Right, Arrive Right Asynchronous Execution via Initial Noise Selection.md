---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19774v1"
published: "2026-06-18T04:14:11Z"
age_days: 1
score: 31
created: 2026-06-20
concepts: ["具身智能评测与基准"]
---

# Start Right, Arrive Right: Asynchronous Execution via Initial Noise Selection

## 为什么重要

自动筛选分数：31

连接概念：[[具身智能评测与基准]]

## 摘要

Action chunking enables robot policies to produce temporally coherent behavior, but
generating multi-step action sequences with flow-based policies incurs latency that is
incompatible with real-time control. Under asynchronous execution, the robot continues
executing the current chunk while the next one is generated, causing even minor delays
to create inconsistencies at chunk boundaries. Existing methods address this problem by
steering generation toward the already executed action prefix. We instead show that
prefix consistency can be achieved by selecting an appropriate initial noise before
generation begins, allowing the unmodified flow ODE to produce a coherent next chunk.
This reframes asynchronous inference as a noise selection problem rather than a
trajectory steering problem. We introduce \textbf{PAINT}, a training-free method that
finds this noise via backward Euler inversion and constructs the final chunk through a
repainting rule. In summary, \texttt{PAINT} requires no gradients, retraining, or policy
modification; yet it improves execution consistency and task performance across
\textit{12 simulated benchmarks} and \textit{6 real-world manipulation tasks} spanning
single-arm, bimanual, and humanoid embodiments. Website: ~\href{https://paint-action-
chunking.github.io}{\texttt{https://paint-action-chunking.github.io}}.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19774v1
- Authors: Trong-Bao Ho, Quang-Tan Nguyen, Thien-Loc Ha, Gia-Binh Nguyen, Viet-Thanh Nguyen, Long Dinh, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
- Published: 2026-06-18T04:14:11Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
