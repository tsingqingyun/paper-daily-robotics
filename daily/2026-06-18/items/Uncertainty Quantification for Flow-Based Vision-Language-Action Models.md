---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18043v1"
published: "2026-06-16T15:19:09Z"
age_days: 1
score: 41
created: 2026-06-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Uncertainty Quantification for Flow-Based Vision-Language-Action Models

## 为什么重要

自动筛选分数：41

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-language-action models (VLAs) combine vision-language backbones with expressive
generative action heads trained via flow matching on large-scale robotic datasets.
Despite their strong empirical performance in robotic manipulation, VLAs lack mechanisms
to quantify confidence in their predictions and to detect when their actions may be
unreliable. This presents a critical limitation for real-world deployment in non-
stationary environments, where models inevitably encounter scenarios outside their
pretraining distribution and may fail without warning. To address this, we derive an
efficient method for quantifying epistemic uncertainty in flow-matching models by
leveraging velocity-field disagreement (VFD) across a small ensemble. We successfully
use this uncertainty estimate for failure detection during deployment and active fine-
tuning of flow-based VLAs. To this end, we propose SAVE, a framework for uncertainty-
guided active multitask fine-tuning that reduces the number of costly expert
demonstrations required to adapt VLAs to new tasks. Through extensive experiments on the
LIBERO benchmark, we demonstrate that VFD yields better-calibrated uncertainty estimates
predictive of downstream performance, that VFD achieves strong performance in detecting
failures, and that uncertainty-guided data acquisition with SAVE requires at least 22%
fewer samples than baselines. In summary, our work shows that quantifying epistemic
uncertainty in flow-based VLAs improves both failure awareness and adaptation. Project
website: tum-lsy.github.io/uq_vla/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18043v1
- Authors: Ralf Römer, Maximilian Seeliger, Saida Liu, Ben Sturgis, Marco Bagatella, Daniel Marta, Andreas Krause, Angela P. Schoellig
- Published: 2026-06-16T15:19:09Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
