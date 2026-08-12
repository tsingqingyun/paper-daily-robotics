---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12369v1"
published: "2026-05-12T16:38:40Z"
age_days: 1
score: 29
created: 2026-05-14
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models aim for general robot learning by aligning action as
a modality within powerful Vision-Language Models (VLMs). Existing VLAs rely on end-to-
end supervision to implicitly enable the action decoding process to learn task-relevant
features. However, without explicit guidance, these models often overfit to spurious
correlations, such as visual shortcuts or environmental noise, limiting their
generalization. In this paper, we introduce GuidedVLA, a framework designed to manually
guide the action generation to focus on task-relevant factors. Our core insight is to
treat the action decoder not as a monolithic learner, but as an assembly of functional
components. Individual attention heads are supervised by manually defined auxiliary
signals to capture distinct factors. As an initial study, we instantiate this paradigm
with three specialized heads: object grounding, spatial geometry, and temporal skill
logic. Across simulation and real-robot experiments, GuidedVLA improves success rates in
both in-domain and out-of-domain settings compared to strong VLA baselines. Finally, we
show that the quality of these specialized factors correlates positively with task
performance and that our mechanism yields decoupled, high-quality features. Our results
suggest that explicitly guiding action-decoder learning is a promising direction for
building more robust and general VLA models.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12369v1
- Authors: Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou, Cunxin Fan, Yufeng Li, Yilin Chai, Chao Jing, Zijian Liang, Qingwen Bu, Haidong Cao, Chao Wu, Qifeng Li, Zhenjie Yang, Chenhe Zhang, Hongyang Li, Zuxuan Wu, Junchi Yan, Yu-Gang Jiang
- Published: 2026-05-12T16:38:40Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
