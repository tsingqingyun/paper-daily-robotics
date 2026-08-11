---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09298v1"
published: "2026-08-10T08:48:06Z"
age_days: 0
score: 38
created: 2026-08-11
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Action-conditioned world models (ACWMs) promise to provide embodied AI with scalable
predictive simulators for planning, policy evaluation, and data generation. Realizing
this promise requires precise action-conditioned transitions rather than merely
plausible outputs. Yet their applicability remains difficult to establish because
prevailing evaluations emphasize visual quality, task outcomes, or coarse rollout-level
responsiveness without directly testing simulator fidelity. To address this gap, we
evaluate ACWMs through the observable capabilities expected of physical simulators.
Accordingly, we formalize Observable Simulator Contract, a minimal contract that any
action-conditioned physical simulator should satisfy: supplied actions must induce
corresponding agent motion, and environment responses must be grounded in that realized
motion. To operationalize this contract, we introduce WorldSimProbe, comprising five
controlled suites spanning local control sensitivity, global trajectory variation,
source-diverse actions, interaction grounding, and dynamics. Suite-specific evaluators
assess simulator-relative calibration, dense action-to-motion correspondence, false-
interaction grounding, and primitive-level dynamics. We evaluate six open-source ACWMs
on more than 18,000 instances across RoboTwin, ManiSkill, and LIBERO. World-SimProbe
reveals systematic action-realization degradation across control variation, structured
failures in interaction grounding and dynamics, and benchmark signals consistent with
human judgments and downstream outcomes. Together, this capability-based framework
provides a transparent, and standardized paradigm for diagnosing ACWM simulator fidelity
beyond coarse, task-directed evaluation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09298v1
- Authors: Peterson Co, Sicheng Hu, Chunxuan Jiao, Hongyang Cheng, Yulin Luo, Yijie Xu, Sixiang Chen, Zhongxia Zhao, Zihao Wang, DaFeng Chi, Peidong Liu, YuTong Chen, Henghua Liu, Zhihao Yuan, Huizhu Jia, Yuzheng Zhuang, Tianle Zhang, Liang Lin, Huajie Tan, Shanghang Zhang
- Published: 2026-08-10T08:48:06Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
