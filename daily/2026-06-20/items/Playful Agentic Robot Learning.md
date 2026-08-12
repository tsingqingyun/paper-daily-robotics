---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19419v1"
published: "2026-06-17T17:55:23Z"
age_days: 2
score: 33
created: 2026-06-20
concepts: ["智能体 Agent", "机器人学习"]
---

# Playful Agentic Robot Learning

## 为什么重要

自动筛选分数：33

连接概念：[[智能体 Agent]], [[机器人学习]]

## 摘要

Current agentic robot systems can write executable Code-as-Policy programs, observe
feedback, and revise behavior across multiple attempts, but they remain largely task-
driven: reusable skills are acquired only after explicit instructions. We study Playful
Agentic Robot Learning, where an embodied coding agent uses self-directed play as a
continual skill-learning stage before downstream tasks arrive. We introduce RATs,
Robotics Agent Teams designed for play-time skill acquisition. During play, RATs
proposes novel yet learnable exploratory tasks, plans and executes robot-code policies,
verifies intermediate progress, diagnoses failures, retries with dense, step-level
feedback, and distills successful executions into a persistent code skill library. At
test time, the agent reuses relevant skills from this frozen library to help solve new
tasks. Experiments in LIBERO-PRO and MolmoSpaces show that play-learned skills improve
held-out downstream tasks over no-play and random-play baselines, with 20.6 and 17.0
percentage-point gains over CaP-Agent0 on LIBERO-PRO and MolmoSpaces, respectively.
Moreover, the learned skills can be plugged into other inference-time Code-as-Policy
agents by simply retrieving them into the context, improving RoboSuite and real-world
transfer by 8.9 and 8.8 points, respectively, without finetuning the underlying model.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19419v1
- Authors: Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, Raj Saravanan, Shaofeng Yin, Justin Yu, Dantong Niu, Zirui Wang, Roei Herzig, Ken Goldberg, Yutong Bai, David M. Chan, Ion Stoica, Angjoo Kanazawa, Jiahui Lei, Haiwen Feng, Trevor Darrell
- Published: 2026-06-17T17:55:23Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
