---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29267v1"
published: "2026-06-28T08:32:35Z"
age_days: 2
score: 31
created: 2026-06-30
concepts: ["多模态基础模型"]
---

# Enhancing Part-Level Point Grounding for Any Open-Source MLLMs

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]]

## 摘要

Visual grounding aims to associate free-form textual queries with specific regions in an
image. While recent Multimodal Large Language Models (MLLMs) have demonstrated promising
capabilities in this domain, they primarily excel at object-level grounding and often
struggle with part-level grounding-an essential requirement for fine-grained tasks such
as robotic manipulation. In this work, we introduce a general approach that equips any
open-source MLLMs with accurate 2D part-level point grounding, offering a more direct
alternative to conventional grounding representations. Our method leverages the
attention mechanisms inherently present in MLLMs. By synthesizing text-conditioned,
grounding-aware queries within intermediate layers via the proposed Q-Synth Module, we
capture target-relevant attention patterns and refine them with a lightweight Attention-
to-Point Decoder, which converts these patterns into a point-centric heatmap for final
prediction. Notably, all original MLLM parameters are frozen, ensuring full preservation
of their pre-trained capabilities. Experiments show that our design consistently
improves part-level grounding accuracy across datasets and can be seamlessly integrated
into any open-source MLLMs.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29267v1
- Authors: Jin-Cheng Jhang, Fu-En Wang, Xin Yang, Nan Qiao, Lu Xia, Min Sun, Cheng-Hao Kuo
- Published: 2026-06-28T08:32:35Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
