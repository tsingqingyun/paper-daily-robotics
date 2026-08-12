---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14187v1"
published: "2026-07-15T15:45:25Z"
age_days: 2
score: 35
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]]

## 摘要

Embodied cognition requires agents to connect high-level task reasoning with the
physical states to be achieved. We introduce Hy-Embodied-RxBrain, an embodied cognition
foundation model with joint language-visual reasoning and imagination. Unlike vision-
language models that emphasize scene understanding and textual decision making, or
generative world models that mainly predict future visual states, RxBrain represents
embodied plans in a single planning sequence where language and visual imagination play
complementary roles. Language provides the abstract structure of a plan, including task
decomposition, planning primitives, constraints, temporal order, and decision logic,
while visual imagination grounds this structure through world state prediction and joint
subgoal planning, associating each planning step with intermediate and final physical
states. RxBrain adopts a unified multimodal Mixture-of-Transformers architecture that
supports language, image, and video understanding and generation within one model. To
train this capability, we build an automatic pipeline that converts embodied videos into
joint text-visual planning supervision by decomposing videos into planning steps and
aligning them with visual state transitions. We further introduce RxBrain-Bench to
evaluate whether models can represent embodied plans through joint textual and visual
components rather than separate understanding or generation. Experiments show that
RxBrain maintains embodied understanding and generation abilities, and produces plans
with coupled textual reasoning, world state prediction, and joint subgoal planning. We
also extend RxBrain to continuous robot action generation, where it shows promising
real-robot performance without large-scale action-data pretraining. These results
provide an initial step toward foundation models for embodied cognition.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14187v1
- Authors: Haotian Liang, Mingkang Chen, Yufei Huang, Yuchun Guo, Xiaomeng Zhu, Xiangli Shi, Kaixuan Wang, Yunxuan Mao, Weijie Zhou, Ling Chen, Shirong Zeng, Yueyu Long, Yuchen Si, Yajuan Zhu, Xingyu Zhou, Minghui Wang, Wanjia He, Xin Yang, Lingzhu Xiang, Zhiqing Liu, Bohan Ma, Xiran Huang, Tianshuo Yang, Zhiheng Liu, Xuantang Xiong, Zisheng Lu, Ping Luo, Yao Mu, Han Hu, Zhengyou Zhang
- Published: 2026-07-15T15:45:25Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
