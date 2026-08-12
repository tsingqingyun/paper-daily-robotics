---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20092v1"
published: "2026-06-18T11:11:37Z"
age_days: 1
score: 38
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard
Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded
or unobservable over time. While existing memory-augmented methods utilize historical
context, they either suffer from severe information bottlenecks, incur high latency via
decoupled dual systems, or rely on unselective buffers that accumulate massive visual
redundancies. To address these limitations, we introduce EventVLA, an end-to-end
framework founded on the concept of sparse visual evidence memory that comprises two
core components: foundational visual anchors to retain initial and short-term contexts,
and a dynamic Keyframe Evidence Memory (KEM) module. Specifically, KEM directly predicts
future keyframe probabilities from the VLA's latent embeddings to autonomously capture
and store sparse, task-critical visual events. This foresight-driven mechanism empowers
the policy to dynamically evaluate the future causal utility of current observations,
preserving transient visual evidence before it becomes unobservable. Furthermore, we
propose RoboTwin-MeM, a diagnostic benchmark specifically designed to evaluate non-
Markovian manipulation tasks with interactive visual evidence. Extensive evaluations
show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks,
EventVLA achieves an average success rate improvement of +40% over state-of-the-art
memory-augmented VLAs.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20092v1
- Authors: Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong, Tianxing Chen, Jiaqi Peng, Jing Xiong, Jiafei Cao, Jifeng Dai, Wengang Zhou, Yao Mu, Tai Wang
- Published: 2026-06-18T11:11:37Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
