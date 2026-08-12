---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13154v1"
published: "2026-07-14T18:04:58Z"
age_days: 2
score: 30
created: 2026-07-17
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Learning open-world mobile manipulation policies requires vast data to achieve spatial
generalization, long-horizon robustness, and scene generalization. Current prevailing
data collection paradigms, teleoperation and UMI, demand prohibitive human effort and
cost at scale. To scale beyond the limits of manual data collection, we seek to maximize
the value of each human demonstration by scalable data generation. To this end, we
introduce WANDA: learning open-World mobile mANipulation from one demonstration via a
synthetic DAta engine. WANDA first reconstructs background Gaussian splats and robot-
object interaction trajectories from source RGBD observations, as a world substrate for
later planning and rendering. It then rearranges contact-rich robot-object interaction
segments into extensive spatial configurations, utilizing whole-body motion planning to
chain them into new trajectories. To enhance long-horizon robustness, it applies
Corrective State Expansion to increase the robot and object state diversity at different
stages of mobile manipulation. To unlock cross-environment generalization, trajectories
are synthesized on diverse generated 3D worlds from everyday photos. Furthermore, we
synthesize photo-realistic observations by compositing rendered robot and object meshes
with Gaussian splatting backgrounds. We evaluate our approach on extensive simulation
and real-world tasks in various scenes. Experiments show that policies trained with
WANDA achieve long-horizon robustness, broad spatial generalization and cross-
environment generalization from one real demonstration. Moreover, WANDA naturally
supports cross-embodiment data generation, validated by zero-shot deployment on another
mobile manipulator with a distinct morphology.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13154v1
- Authors: Lingxiao Guo, Huanyu Li, Guanya Shi
- Published: 2026-07-14T18:04:58Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
