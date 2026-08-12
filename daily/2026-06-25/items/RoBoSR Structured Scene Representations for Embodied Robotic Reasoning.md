---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24338v1"
published: "2026-06-23T09:24:52Z"
age_days: 1
score: 38
created: 2026-06-25
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RoBoSR: Structured Scene Representations for Embodied Robotic Reasoning

## 为什么重要

自动筛选分数：38

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Despite rapid progress, embodied reasoning under real-world variability remains
challenging. Existing approaches rely on demonstration-driven sequential biases,
limiting flexibility in open-ended and long-horizon tasks that require structured
reasoning over evolving states. We introduce RoBoSR, an intermediate structural
representation that formulates manipulation as step-wise state transitions over
semantically grounded, object-centric scene graphs. By modeling object states and their
spatial relations at the perception-action interface, RoBoSR disentangles high-level
task reasoning from raw inputs and enables structured reasoning over preconditions,
effects, and goal states. This representation endows the agent with causal reasoning
capability, enforcing subtask dependencies and supporting coherent long-horizon task
planning. To learn such structure-aware reasoning, we construct Manip-Cognition-1.6M, an
open-world dataset that jointly supervises scene understanding, instruction
interpretation, and subtask planning across diverse tasks. Across several benchmarks and
real-world demonstrations, our method consistently outperforms prompting-based methods
and classical TAMP baselines in zero-shot generalization and long-horizon tasks. The
results underscore structured intermediate representations as a critical inductive bias
for scalable embodied reasoning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24338v1
- Authors: Kewei Hu, Wanchan Yu, Fangwen Chen, Jing Jiajian, Zimeng Li, Ying Wei, Tianhao Liu, Michael Zhang, Hanwen Kang
- Published: 2026-06-23T09:24:52Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
