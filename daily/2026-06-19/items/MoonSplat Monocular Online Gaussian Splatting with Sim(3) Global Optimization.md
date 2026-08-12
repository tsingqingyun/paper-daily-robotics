---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17935v1"
published: "2026-06-16T13:43:35Z"
age_days: 2
score: 29
created: 2026-06-19
concepts: ["具身智能评测与基准"]
---

# MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization

## 为什么重要

自动筛选分数：29

连接概念：[[具身智能评测与基准]]

## 摘要

Online 3D reconstruction from monocular image sequences is a challenging and ongoing
research topic. 3D Gaussian Splatting (3DGS), leveraging its high-quality real-time
rendering capability, empowers online 3D reconstruction to represent dense scenes with
enhanced expressiveness, and thus holds great promise for a wide range of applications
such as robotics and AR/VR. However, existing online 3DGS methods still suffer from some
key challenges: fragile camera pose estimation due to the lack of global optimization,
and low optimization efficiency in large-scale or long-sequence scenarios. To address
these issues, we propose a robust and efficient online voxelized 3DGS reconstruction
framework integrated with global $\text{Sim}(3)$ optimization, which enables reliable
camera tracking and efficient global loop closure for both camera poses and voxelized
3DGS. To accelerate the convergence of the voxelized 3DGS, we further introduce a color
residual learning strategy, which not only boosts optimization speed but also enhances
rendering quality. Extensive experiments on diverse indoor and outdoor datasets
demonstrate that our method achieves state-of-the-art performance in both camera pose
estimation accuracy and rendering quality, while retaining real-time efficiency.
Additionally, we develop and deploy a real-world UAV-based active reconstruction system
grounded on our proposed method, validating its robustness and generalizability for
practical online 3D reconstruction tasks. Our code and data are available at
https://github.com/TrickyGo/MoonSplat.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17935v1
- Authors: Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian
- Published: 2026-06-16T13:43:35Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
