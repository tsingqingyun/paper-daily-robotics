---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20562v1"
published: "2026-06-18T17:59:51Z"
age_days: 1
score: 32
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# MemoryWAM: Efficient World Action Modeling with Persistent Memory

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Robust robotic manipulation in the real world requires not only an understanding of the
current observation, but also memory and dynamics modeling. World action models (WAMs)
possess these capabilities by jointly modeling visual foresight and actions conditioned
on both current and historical observations, making them a promising paradigm for
robotic manipulation. However, existing WAMs face a fundamental trade-off: methods with
efficient inference typically condition only on a bounded window of recent observations
and therefore struggle in non-Markovian environments, whereas methods that preserve long
histories incur time and space costs that grow substantially with sequence length. To
address this challenge, we introduce MemoryWAM, a world action model with efficient
persistent memory. MemoryWAM uses a hybrid memory design that combines recent frames,
event-boundary anchor frames, and compact gist tokens that summarize long-range history.
A tailored attention mechanism enables retrieval of both detailed short-term context and
compressed long-term context, supporting memory-dependent decision-making with reduced
inference latency and GPU memory usage. Across long-horizon, memory-dependent
manipulation tasks in both simulation and the real world, MemoryWAM outperforms strong
vision-language-action (VLA) and WAM baselines while maintaining favorable computational
efficiency.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20562v1
- Authors: Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu
- Published: 2026-06-18T17:59:51Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
