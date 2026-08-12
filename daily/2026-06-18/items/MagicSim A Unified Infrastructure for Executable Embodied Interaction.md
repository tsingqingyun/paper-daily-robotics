---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17511v1"
published: "2026-06-16T04:42:43Z"
age_days: 1
score: 31
created: 2026-06-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# MagicSim: A Unified Infrastructure for Executable Embodied Interaction

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Robot learning and embodied agents now require simulation to serve as a shared execution
substrate linking control, skills, and planning, not only as a renderer, controller
testbed, or fixed task environment. Existing pipelines split these layers with "magic"
actions, disconnected training environments, or forward-only renders that cannot
reproduce, evaluate, and annotate the same episode. We present MagicSim, an embodied
interaction infrastructure built around one deterministic batched runtime and a shared
Markov decision process (MDP). From YAML-first specifications that decouple contents,
placement, behavior, and agent exposure, MagicSim constructs diverse executable worlds
spanning task families, interaction regimes, physics, layouts, sensors, avatars, and
robot embodiments in one reset-and-step loop. A common execution interface grounds high-
level commands through controllers, atomicskills, planner primitives, and asynchronous
planning, realizing them as robot actions rather than simulator-side state edits. One
task definition supports three capabilities: benchmark and RL evaluation, an autocollect
interface that automatically turns commands into grounded trajectories, and agent/VLM-
facing interaction. For automatic execution, commands flow through a
Command->Skill->Planner->Robot->Record pipeline, while per-environment command, skill,
planning, retry, annotation, and episode states advance independently above the shared
physics tick. Successful rollouts are saved as structured multimodal trajectories
aligning language supervision, action representations, visual/geometric representations,
and task-level status with the executed episode. MagicSim thus unifies diverse world
construction, embodied execution, task evaluation, automatic rollout generation, and
interactive agent interfaces in one planner-in-the-loop runtime.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17511v1
- Authors: Haoran Lu, Songling Liu, Yue Chen, Guo Ye, Mutian Shen, Shuyang Yu, Yu Xiao, Jihai Zhao, Shang Wu, Jianshu Zhang, Xiangtian Gui, Chuye Hong, Yuran Wang, Maojiang Su, Jiayi Wang, Ruihai Wu, Zhaoran Wang, Han Liu
- Published: 2026-06-16T04:42:43Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
