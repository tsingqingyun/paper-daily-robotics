---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14270v1"
published: "2026-06-12T08:51:51Z"
age_days: 3
score: 23
created: 2026-06-16
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learning

## 为什么重要

自动筛选分数：23

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Fall recovery is critical for autonomous legged locomotion. Existing methods have
demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of
fall recovery from diverse postures by utilizing arms or coordinating multi-legs to
generate support forces. Without arms or other legs to provide supportive assistance, a
bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery
particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student
framework with Stage-wise Rewards). The force-guided method constructs an external
auxiliary force during simulation training that correlates directly with the robot's
real-time height, explicitly formulating this force as an optimizable constraint.
Through constrained reinforcement learning, the policy is guided toward reducing force
dependency gradually and increasing the body height, developing internal recovery
strategies despite having no arms for support. Height-progressive stage-Wise rewards
progressively structure posture stabilization during recovery and transition to
sustained locomotion, integrated with teacher-student architecture distilling privileged
knowledge of force effects and recovery dynamics. After simulation training, the policy
is deployed on a physical armless bipedal-wheeled robot and extensively evaluated.
Experiments confirm robust and reliable fall recovery under diverse challenging
conditions, demonstrating strong environmental adaptability and motion robustness, while
maintaining full post-recovery motion capability. The framework also generalizes
effectively to a high-DOF humanoid, confirming its practical generalizability. The
project page is available at https://2350575870.github.io/force-guided.github.io/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14270v1
- Authors: Haidong Hou, Zhangguo Yu, Tao Han, Hengbo Qi, Khaleel Ghazal, Yu Zhang, Yidong Du, Xuechao Chen, Fei Meng
- Published: 2026-06-12T08:51:51Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
