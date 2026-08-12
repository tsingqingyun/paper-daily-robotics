---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20135v1"
published: "2026-06-18T11:58:30Z"
age_days: 1
score: 32
created: 2026-06-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Flow matching has emerged as a standard paradigm for robotic manipulation owing to its
strong expressive power for modelling complex, multimodal action distributions,
alongside similar approaches like diffusion policy. However, existing methods rely on
discretized action chunks, making them brittle to demonstrations collected at
heterogeneous control frequencies and prone to temporally inconsistent actions that
degrade control stability. In this paper, we propose Frequency-Aware Flow Matching
(FAFM), which outputs continuous, temporally consistent actions. To handle heterogeneous
frequency input, we transform discrete action sequences into the frequency domain with
the discrete cosine transform (DCT), perform flow matching over the resulting
coefficients, and reconstruct continuous actions via cosine basis expansion. To generate
temporally consistent actions, we regularize the first-order temporal derivative to
promote smooth actions. This corresponds to a Sobolev-type constraint that suppresses
high-frequency errors and discourages abrupt action changes. Our FAFM is simple,
introduces no additional network parameters and applies to standalone flow-matching
policies and vision-language action models. Across synthetic toy benchmark, obstacle
avoidance, LapGym, and LIBERO, FAFM improves success rates, multimodal expressivity,
motion smoothness, convergence speed, robustness to mechanical bias and mixed-frequency
input. These gains are consistent when deployed on a real-world Franka robot. Code
available at https://anonymous.4open.science/r/FAFM.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20135v1
- Authors: Jianing Guo, Fangzheng Chen, Zihao Mao, Wong Lik Hang Kenny, Zhenhong Wu, Yu Li, Yishuai Cai, Yuanpei Chen, Yikun Ban, Kai Chen, Qi Dou, Yaodong Yang, Xianglong Liu, Huijie Zhao, Simin Li
- Published: 2026-06-18T11:58:30Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
