---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13494v1"
published: "2026-06-11T15:44:36Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Goal-conditioned visual navigation requires a robot to act under partial observability
by anticipating how its motion will change the future egocentric view and whether that
change brings it closer to the goal. Navigation world models provide such visual
foresight, but they remain prediction modules that require an external planner to
convert predicted futures into closed-loop control. We propose Navigation World Action
Model (NavWAM), a diffusion-transformer policy that turns navigation world-model
prediction into executable action by representing future observations, goal-progress
values, and action chunks in a shared latent sequence. By learning future prediction
jointly with the action and value targets that determine closed-loop behavior, NavWAM
makes visual foresight directly usable for robot control. We build NavWAM through
simulation pretraining and real-robot adaptation, and evaluate it on image-goal
navigation against planning-based world models and a representative direct navigation
policy. Across offline benchmarks and closed-loop real-robot deployment, NavWAM improves
over planning-based world-model baselines in our evaluations while using the default
policy mode without CEM-style action search. Project page: https://dachii-
azm.github.io/navwam/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13494v1
- Authors: Daichi Azuma, Taiki Miyanishi, Koya Sakamoto, Shuhei Kurita, Yaonan Zhu, Petr Khrapchenkov, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo
- Published: 2026-06-11T15:44:36Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
