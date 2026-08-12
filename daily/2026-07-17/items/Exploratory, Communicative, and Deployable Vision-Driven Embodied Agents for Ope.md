---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13653v1"
published: "2026-07-15T09:55:45Z"
age_days: 1
score: 45
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation

## 为什么重要

自动筛选分数：45

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Real-world deployment of embodied agents requires active exploration, visual grounding,
and interactive intent disambiguation. However, existing frameworks often rely on
privileged simulator states or assume complete instructions, bypassing realistic
deployment challenges. To bridge this gap, we present REAL, an agentic framework for
open-world mobile manipulation. REAL establishes sim-to-real-consistent environment APIs
without oracle perception and integrates a simulated user to enable human-in-the-loop
interaction. Within this environment, we design diverse task compositions to drive data
collection, supervised fine-tuning, and online reinforcement learning, systematically
optimizing agent performance. To comprehensively evaluate this approach, we introduce
REAL-Bench, a benchmark spanning 241 tasks across active exploration, visual
distraction, articulated manipulation, and interactive disambiguation. Experimental
results demonstrate that our trained agent outperforms leading commercial closed-source
VLMs on interactive tasks with a 56.9% success rate. Further empirical analysis reveals
that our hierarchical training pipeline successfully aligns the model's tool-use
capabilities while maintaining robust open-vocabulary reasoning under extended
exploration horizons. Finally, we deploy and evaluate our framework on a physical dual-
arm mobile robot, where it achieves a 78.3% end-to-end success rate over 60 real-world
episodes. These physical trials demonstrate robust zero-shot transferability to unseen
household scenarios, validating that our sim-to-real-consistent design successfully
bridges the reality gap for long-horizon mobile manipulation. Code is available at
https://github.com/InternRobotics/REAL.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13653v1
- Authors: Boyu Mi, Mengchen Ma, Yifei Yao, Xing Gao, Junting Chen, Yangzi Li, Zihou Zhu, Guohao Li, Zhenfei Yin, Tai Wang, Yao Mu, Jiangmiao Pang, Hanqing Wang
- Published: 2026-07-15T09:55:45Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
