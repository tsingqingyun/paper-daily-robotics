---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2604.27472v1"
published: "2026-04-30T06:14:02Z"
score: 34
created: 2026-05-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Vision-Language-Action (VLA) models advance robotic control via strong visual-linguistic
priors. However, existing VLAs predominantly frame pretraining as supervised behavior
cloning, overlooking the fundamental nature of robot learning as a goal-reaching process
that requires understanding temporal task progress. We present \textbf{PRTS}
(\textbf{P}rimitive \textbf{R}easoning and \textbf{T}asking \textbf{S}ystem), a VLA
foundation model that reformulates pretraining through Goal-Conditioned Reinforcement
Learning. By treating language instructions as goals and employing contrastive
reinforcement learning, PRTS learns a unified embedding space where the inner product of
state-action and goal embeddings approximates the log-discounted goal occupancy, the
probability of reaching the language-specified goal from the current state-action,
quantitatively assessing physical feasibility beyond static semantic matching. PRTS
draws this dense goal-reachability supervision directly from offline trajectories
without reward annotations, and folds it into the VLM backbone via a role-aware causal
mask, incurring negligible overhead over vanilla behavior cloning. This paradigm endows
the high-level reasoning system with intrinsic goal reachability awareness, bridging
semantic reasoning and temporal task progress, and further benefits goal-conditioned
action prediction. Pretrained on 167B tokens of diverse manipulation and embodied-
reasoning data, PRTS reaches state-of-the-art performance on LIBERO, LIBERO-Pro, LIBERO-
Plus, SimplerEnv, and a real-world suite of 14 complex tasks, with particularly
substantial gains on long-horizon, contact-rich, and zero-shot novel-instruction
settings, confirming that injecting goal-reachability awareness significantly improves
both execution success and long-horizon planning of general-purpose robotic foundation
policies.

## 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2604.27472v1
- Authors: Yang Zhang, Jiangyuan Zhao, Chenyou Fan, Fangzheng Yan, Tian Li, Haitong Tang, Sen Fu, Xuan'er Wu, Qizhen Weng, Weinan Zhang, Xiu Li, Chi Zhang, Chenjia Bai, Xuelong Li
- Published: 2026-04-30T06:14:02Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
