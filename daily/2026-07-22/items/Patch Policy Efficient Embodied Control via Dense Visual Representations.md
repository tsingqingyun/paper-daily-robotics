---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18236v1"
published: "2026-07-20T17:59:41Z"
age_days: 1
score: 39
created: 2026-07-22
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Patch Policy: Efficient Embodied Control via Dense Visual Representations

## 为什么重要

自动筛选分数：39

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have
been underutilized in robot learning. Modern robot policies either compress each
observation into a single global token, or rely on visual backbones trained from
scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale
visual pre-training. While there exist policies that do operate on dense patch features
like large vision-language-action models (VLAs), they tend to be heavy and slow,
inheriting the full cost of a billion-parameter vision-language model (VLM) backbone. We
close this gap with Patch Policy, a minimal architectural extension that enables
transformer-based policies to consume dense pre-trained patch tokens directly without
the computational overhead of a full VLM. At its core is a block-causal attention mask
that preserves the temporal causality of standard policies while letting the model
attend over many patch tokens per observation, alongside other state information. Patch
Policy is lightweight, fast, and highly effective. Across four simulated and three real-
world environment suites, our method achieves a 40% relative improvement over policies
using state-of-the-art global-pooled representations. Furthermore, it surpasses fine-
tuned OpenVLA-OFT by 18% while using roughly 0.7% of the parameters. We believe Patch
Policy provides a pipeline for the robotics community to readily leverage continuing
progress in visual representation learning, without sacrificing the training efficiency
or inference speed required for high-frequency, reactive control. Videos can be viewed
at https://patch-policy.github.io

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18236v1
- Authors: Gaoyue Zhou, Zichen Jeff Cui, Ada Langford, Bowen Tan, Yann LeCun, Lerrel Pinto
- Published: 2026-07-20T17:59:41Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
