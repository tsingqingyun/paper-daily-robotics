---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12987v1"
published: "2026-06-11T07:24:12Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Diffusion Transformer World-Action Model for AV Scene Prediction

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Action-conditioned world models let an autonomous vehicle predict future camera scenes
from its own planned controls, enabling planning and simulation without real-world
rollouts, but at compact, trainable scale the futures are ambiguous and the field's
standard distortion metrics actively mislead: they reward a blurry regression mean over
a realistic prediction. We confront this with a compact latent world model that, given
the present front-camera latent and a sequence of ego-actions, predicts future scene
latents a frozen decoder renders to $256 \times 256$ frames up to 8 seconds ahead,
evaluated on 150 held-out nuScenes scenes. We first benchmark where to predict: across
six frozen encoders spanning four representation families, V-JEPA2 with temporal context
reduces steering RMSE by 40% over the best single-frame encoder. We then train a latent
Diffusion Transformer (DiT) and, through a controlled diagnosis, identify the four
ingredients it needs: spatial tokens, the $x_0$ objective, residual anchoring, and
sampling matched to target uncertainty. In a Stable-Diffusion-VAE encode-predict-decode
pipeline we expose the central tension: distortion metrics (cosine similarity, SSIM)
favor the blurry mean, masking that the diffusion model is far closer to the real frame
distribution. Inception-based FID and KID reveal a clean perception-distortion frontier:
diffusion attains KID 0.078 versus 0.375 for regression ($4.8\times$ better), and a
deployable train-derived calibration makes this practical without test-time ground
truth. The model is genuinely action-controllable (steering drives scene displacement,
Spearman $ρ= 0.81$, vs $-0.18$ for regression). We trace limited single-pass motion to a
shared-present anchor and engineer a compact 1.7M-parameter "jump" model that recovers
full ground-truth motion magnitude ($1.02\times$ GT), where single-pass models capture
less than half.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12987v1
- Authors: Ruslan Sharifullin, Benjamin Jiang, Kai Xi Chew
- Published: 2026-06-11T07:24:12Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
