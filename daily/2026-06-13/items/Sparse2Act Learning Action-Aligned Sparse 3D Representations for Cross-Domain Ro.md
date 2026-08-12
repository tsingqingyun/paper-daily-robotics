---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12759v1"
published: "2026-06-10T23:56:01Z"
age_days: 2
score: 29
created: 2026-06-13
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Sparse2Act: Learning Action-Aligned Sparse 3D Representations for Cross-Domain Robot Manipulation

## 为什么重要

自动筛选分数：29

连接概念：[[世界模型]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Explicit 3D representations are attractive for manipulation because they expose object
shape, workspace geometry, and robot-object relations in metric coordinates. However,
sparse 3D encoders are often learned through downstream task objectives, tying the
representation to a particular data distribution, policy architecture, and action
parameterization. We introduce Sparse2Act, an observation-action alignment framework for
pretraining sparse point-cloud encoders. The key idea is to use task-space end-effector
actions as geometric supervision: masked sparse 3D tokens are trained to organize scene
features around the workspace motion paired with the observation. After pretraining,
only the encoder initialization is reused by downstream policies, allowing them to
retain their own architectures and action spaces, including joint-space commands. On the
LIBERO-10 benchmark, our method achieves 86.9% average success after 500 fine-tuning
steps. The same pretrained encoder supports LIBERO-to-Meta-World cross-domain transfer,
achieving 73.4% average success on the Meta-World-5 benchmark. Ablations on the
objective and decoder capacity show that the gains come from the masked action-alignment
signal and remain useful across downstream action decoders. In real-world experiments,
simulation pretraining followed by limited real-data fine-tuning achieves an average
success rate of 72.5% across four tasks, demonstrating effective sim-to-real transfer.
These results suggest that robot actions can provide compact geometric supervision for
reusable sparse 3D representations.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12759v1
- Authors: Yu Guo, Chang Yu, Siyu Ma, Yunuo Chen, Yin Yang, Ying Nian Wu, Chenfanfu Jiang
- Published: 2026-06-10T23:56:01Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
