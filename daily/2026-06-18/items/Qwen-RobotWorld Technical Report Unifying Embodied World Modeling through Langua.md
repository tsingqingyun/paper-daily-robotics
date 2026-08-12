---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17030v2"
published: "2026-06-15T17:52:31Z"
age_days: 2
score: 39
created: 2026-06-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation

## 为什么重要

自动筛选分数：39

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied
intelligence. With natural language as a unified action interface, it predicts
physically grounded future visual trajectories from current observations across robotic
manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This
unified formulation provides three promising application directions: synthetic data
generation for policy training augmentation, scalable virtual environments for policy
evaluation, and language-guided planning signals for downstream robot control. This is
achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding,
where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics
with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge
(EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+
embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a
two-stage training strategy that first learns general visual priors and then injects
embodied specialization under a shared language interface. Extensive results show strong
competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-
source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-
IF benchmark further support robust generalization and multi-view consistency.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17030v2
- Authors: Jie Zhang, Xiaoyue Chen, Anzhe Chen, Deqing Li, Gengze Zhou, Hale Yin, Haoqi Yuan, Haoyang Li, Jiahao Li, Jiazhao Zhang, Jingren Zhou, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Pei Lin, Qihang Peng, Shengming Yin, Tianhe Wu, Tianyi Yan, Xiao Xu, Yan Shu, Yanran Zhang, Ye Wang, Yi Wang, Yilei Chen, Yixian Xu, Yiyang Huang, Yuxiang Chen, Zekai Zhang, Zhendong Wang, Zixing Lei, Zhixuan Liang, Zihao Liu, Zikai Zhou, Chenxu Lv, Xiong-Hui Chen, Chenfei Wu
- Published: 2026-06-15T17:52:31Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
