---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14048v1"
published: "2026-06-12T02:49:34Z"
age_days: 2
score: 28
created: 2026-06-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# WAM4D: Fast 4D World Action Model via Spatial Register Tokens

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

World action models (WAMs) have recently shown promise in jointly modeling future
observations and executable robot actions. However, most existing WAMs still operate in
2D video or latent spaces, where visually plausible rollouts miss the 3D spatial
constraints and occluded contact geometry required for precise manipulation. While
geometric foundation models offer strong priors for recovering dense 3D structure and
motion from visual observations, forcing WAMs to predict the dense 4D representation
introduces costly geometric decoding and slows down causal action generation. To address
the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight
spatial register tokens as training-time future-depth readouts to transfer pretrained
geometric priors into a causal video-action transformer, then removes the register
branch for lightweight action inference. To prevent non-causal shortcuts, we further
design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone,
defining modality-specific visibility among video, action, and geometry tokens.
Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks
show that WAM4D improves spatial consistency and achieves competitive action prediction
while maintaining efficient inference.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14048v1
- Authors: Ying Li, Xiaobao Wei, Jiajun Cao, Hao Wang, Xiaowei Chi, Chengyu Bai, Qianpu Sun, Jiajun Li, Xiaojie Zhang, Jian Tang, Sirui Han, Shanghang Zhang
- Published: 2026-06-12T02:49:34Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
