---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13621v1"
published: "2026-07-15T09:09:25Z"
age_days: 1
score: 34
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# UESF-Bench: Benchmarking and Probing for Unified Embodied Seeking and Following

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Language-guided human following is an important capability for embodied agents, but
existing benchmarks typically assume that the target person is visible at the start of
an episode. This setting simplifies the problem and overlooks a more realistic
requirement: an agent often needs to first find a language-described target and then
persistently follow that target in a dynamic environment. While recent work has started
to study human search, existing settings are typically evaluated in task-specific
scenarios and often rely on stronger prior knowledge of the environment. Moreover, they
usually treat searching and following as separate tasks and still lack a unified
benchmark for systematic evaluation. To address these limitations, we introduce the
Unified Embodied Seeking and Following Benchmark (UESF-Bench), a large-scale and diverse
benchmark for embodied human seeking and following. The benchmark requires agents to
handle semantic-guided exploration, reliable behavior switching and recovery, and
delayed identity grounding. To this end, we propose SeekFollow-VLA, a vision-language-
action framework with a task-driven routing mechanism for latent phase inference and
transition modeling between seeking and following. Experimental results show that
SeekFollow-VLA achieves clear improvements over both single-head and dual-head baselines
across single-person and multi-person environments, establishing a baseline for unified
embodied seek-and-follow.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13621v1
- Authors: Kun Yu, Jianhua Yang, Yixiang Chen, Changwei Wang, Hongyuan Yu, Yan Huang, Fushuo Huo, Ya Jing, Zhumin Chen, Keji He
- Published: 2026-07-15T09:09:25Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
