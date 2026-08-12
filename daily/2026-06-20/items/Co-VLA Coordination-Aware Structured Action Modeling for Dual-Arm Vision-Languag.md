---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20285v1"
published: "2026-06-18T14:28:37Z"
age_days: 1
score: 41
created: 2026-06-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems

## 为什么重要

自动筛选分数：41

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models show strong capabilities in single and dual-arm
robotic manipulation. Prior works show coordinated bimanual behaviors can emerge from
end-to-end learning, leveraging large vision-language backbones with continuous action
prediction. However, as bimanual tasks become tightly coupled and execution constraints
become critical, implicit coordination alone is insufficient to ensure reliable,
interpretable, and stable behavior. In this work, we propose Co-VLA, a coordination-
aware bimanual manipulation framework introducing explicit structural priors into VLA
models. We instantiate our method on a state-of-the-art vision-language backbone by
replacing its monolithic action head with a Structured Action Expert (SAE) designed for
bimanual coordination. Specifically, we introduce explicit structure at the action
generation level with a modular coordination-aware loss that shapes shared and residual
latents according to task-specific structures. The shared latent encodes task-level
coordination intent, while residual latents capture execution adjustments for each arm.
At deployment, a Latent-Aware Controller (LAC) interprets the learned representations to
modulate synchronization strength, execution asymmetry, smoothness, and safety
constraints in real time. LAC operates at the joint-command level and remains compatible
with standard control pipelines without requiring force or impedance control.
Experiments across simulation and real-world benchmarks show Co-VLA significantly
outperforms monolithic baselines, achieving a 27% success rate gain in tight-
coordination tasks, more than doubling performance in OOD real-world scenarios (from 13%
to 27%), and reducing task completion time by up to 25%.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20285v1
- Authors: Yandong Wang, Jiaqian Yu, Xiongfeng Peng, Lu Xu, Yamin Mao, Weiming Li, Jaewook Yoo, Dongwook Lee, Daehyun Ji, Mingbo Zhao, Chao Zhang
- Published: 2026-06-18T14:28:37Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
