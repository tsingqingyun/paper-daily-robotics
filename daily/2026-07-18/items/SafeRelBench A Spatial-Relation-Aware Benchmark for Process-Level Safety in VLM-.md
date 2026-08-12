---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14543v1"
published: "2026-07-16T03:59:44Z"
age_days: 1
score: 30
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Vision-language models (VLMs) are increasingly used as the reasoning backbone of
embodied agents, enabling robots to interpret visual scenes, follow language
instructions, and plan multi-step actions. In household environments, however, safety
depends not only on recognizing objects, but also on how actions change the physical
scene over time. Existing embodied safety evaluations largely focus on static risk
recognition, unsafe instruction refusal, or final-state task completion. As a result,
process-level safety failures induced by spatial relations such as support, containment,
and proximity remain insufficiently studied. To address this gap, we introduce
SAFERELBENCH, a spatial-relation-aware safety benchmark with 507 executable evaluation
samples, including 248 spatial-relation samples and 259 non-spatial control samples.
Using SAFERELBENCH to evaluate seven open- and closed-source VLM-driven embodied agents,
we find a substantial gap between task success and process-level safety compliance:
models often complete the requested task while violating process-level safety
constraints. Unlike prior benchmarks, SAFERELBENCH explicitly tests whether agents
satisfy safety conditions before risk-prone actions, making spatial relations a core
dimension in embodied safety assessment. More broadly, our results show that safe
embodied intelligence requires not only stronger perception and planning, but also
reliable reasoning about how object relations shape risk during interaction.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14543v1
- Authors: Huaigang Yang, Ya Li, Min Ren, Bo Dai, Zhenliang Zhang, Zhaofeng He
- Published: 2026-07-16T03:59:44Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
