---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22971v1"
published: "2026-06-22T07:52:25Z"
age_days: 1
score: 40
created: 2026-06-24
concepts: ["世界模型", "Sim2Real"]
---

# Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI

## 为什么重要

自动筛选分数：40

连接概念：[[世界模型]], [[Sim2Real]]

## 摘要

Occupancy prediction at voxel-level granularity is essential for safe robotic navigation
and interaction in complex environments. Existing occupancy datasets, however, are
predominantly designed for autonomous driving with vehicle-centric biases -- forward-
facing cameras, far-field geometry, and static road priors -- limiting their
applicability to embodied humanoid perception. We present Humanoid-OmniOcc, a large-
scale panoramic stereo-based occupancy dataset tailored for humanoid robots. The dataset
encompasses 15 diverse simulated indoor scenes and 5 real-world environments, yielding
over 155K samples with broad scene and style diversity. Importantly, the dataset is
designed around a Real2Sim2Real closed-loop paradigm: real sensor specifications drive
physically accurate simulation, simulation produces large-scale annotated training data,
and models trained in simulation are directly evaluated on real-world captures --
enabling iterative refinement of the sim-to-real pipeline. We further propose
\textbf{H}umanoid \textbf{S}urround \textbf{S}tereo-guided \textbf{Occ}upancy model
(Humanoid-OmniOcc) that exploits robust depth priors for accurate 2D-to-3D lifting.
Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular
baselines and generalizes well to both unseen simulated test scenes and real-world
environments, validating the effectiveness of the Real2Sim2Real design. Code and data
will be available upon acceptance at https://d-robotics-ai-lab.github.io/humanoid-
omniocc.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22971v1
- Authors: Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, Cong Yang, Qin Zou, Wei Sui
- Published: 2026-06-22T07:52:25Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
