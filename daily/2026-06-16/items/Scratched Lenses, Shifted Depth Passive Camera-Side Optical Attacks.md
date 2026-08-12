---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14504v1"
published: "2026-06-12T14:34:53Z"
age_days: 3
score: 21
created: 2026-06-16
concepts: ["具身智能评测与基准"]
---

# Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks

## 为什么重要

自动筛选分数：21

连接概念：[[具身智能评测与基准]]

## 摘要

Physical adversarial attacks on vision systems are typically studied through scene
manipulation, such as adversarial patches or projections, where the adversary controls
what the camera observes. Camera-side attacks using stickers or auxiliary optics have
also been explored, but they treat attacks as image-space perturbations from designed
patterns. This misses how physical imperfections interact with scene-dependent lighting
and optics. We identify a threat: passive lens-side damage that is persistent yet
trigger-conditioned, producing optical artifacts that bias geometric inference under
particular visual conditions. We instantiate this threat through Scratch-induced Lens
Adversarial Streak Hijacking SLASH, a physical-world attack caused by small scratches on
a camera lens or protective cover. Scratches interact with bright light sources and
specular reflections to create structured streak artifacts that distort depth cues.
Since the perturbation is fixed in the optical path but triggered by the scene, it is
both persistent and selective. We formulate the attack in optical space, model the
scratch pattern as a trigger-conditioned optical channel, and optimize one fixed
configuration across diverse viewing conditions. We evaluate SLASH on monocular depth
estimation and monocular 3D object detection in digital and real-world settings. Under
the fixed-scratch constraint, directional depth shifts reach up to 32% relative error
for monocular depth estimation, with consistent effects on monocular 3D object
detection. Physical experiments confirm transfer to real camera recordings, inducing
depth shifts above the model's natural prediction baseline. These findings reveal an
attack surface where benign-looking hardware imperfections act as latent, scene-
triggered adversarial mechanisms, challenging assumptions about physical robustness and
motivating defenses for secure vision systems.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14504v1
- Authors: Qinlin He, Zeming Zhuang, Yongji Wu, Lan Zhang, Xiaoyong, Yuan
- Published: 2026-06-12T14:34:53Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
