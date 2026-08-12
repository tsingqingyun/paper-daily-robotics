---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13578v1"
published: "2026-06-11T17:03:53Z"
age_days: 1
score: 31
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Scientific laboratories increasingly rely on AI systems to reason about experiments, but
the physical act of doing science remains largely outside their reach. AI can help read
literature, generate hypotheses, and plan protocols, yet the execution of those
protocols at the bench still requires a human operator. Vision-Language-Action (VLA)
models provide one possible interface between written protocols and robot execution, but
existing policies are trained mostly on household and tabletop demonstrations and rarely
encounter the instruments, transparent liquids, or fixed protocol workflows found in
scientific laboratories. Closing this gap requires both laboratory-specific supervision
and a unified learning framework that can accommodate the diverse robot embodiments used
to execute experimental protocols. We therefore identify data and embodiment as central
bottlenecks alongside model design. To address the data side, we build RoboGenesis, a
simulation-based workflow and data engine that composes configured laboratory workflows
from atomic skills, validates and filters rollouts, and exports structured
demonstrations across supported robot profiles. On the policy side, we present LabVLA,
trained with a two-stage recipe: FAST action token pretraining first makes the
Qwen3-VL-4B-Instruct backbone action aware before any continuous control is learned, and
flow matching posttraining then attaches a DiT action expert under knowledge insulation.
On the LabUtopia benchmark, LabVLA achieves the highest average success rate among all
evaluated baselines under both in-distribution and out-of-distribution settings.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13578v1
- Authors: Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu, Chenxi Li, Daqi Gao, Zeqin Su, Jintao Xing, Zirui Xue, Rui Li, Xiangyu Zhao, Shuofei Qiao, Minting Pan, Wangmeng Zuo, Lei Bai, Dongzhan Zhou, Ningyu Zhang, Huajun Chen
- Published: 2026-06-11T17:03:53Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
