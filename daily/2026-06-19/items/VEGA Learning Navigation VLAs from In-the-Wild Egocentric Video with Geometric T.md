---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18426v1"
published: "2026-06-16T19:21:14Z"
age_days: 2
score: 30
created: 2026-06-19
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VEGA: Learning Navigation VLAs from In-the-Wild Egocentric Video with Geometric Trajectory Supervision

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

We introduce VEGA, an approach for training navigation VisionLanguage-Action (VLA)
models from unlabeled egocentric navigation videos. Internet-scale egocentric videos
provide a scalable source of navigation-relevant visual observations, capturing
cluttered scenes, close-range obstacles, and natural human motion through real-world
spaces. However, these videos are not directly usable for policy learning because they
do not provide obstacle-aware trajectories conditioned on explicit navigation goals in
the robot's coordinate frame. VEGA addresses this gap by reconstructing local scene
geometry from monocular video, sampling navigation goals (represented as text, image, or
spatial waypoints) and generating obstacle-aware trajectories using the constructed
geometry. The resulting trajectory distribution is then used to train a flow-matching
VLA navigation policy. By using geometry exclusively during training, VEGA distills
obstacle-aware planning directly into a vision-based policy. Furthermore, we introduce
VEGA-Bench, a benchmark containing 250k scenes and approximately 5 million navigation
goals paired with scene geometry, designed to evaluate goal progress, collision
avoidance, and obstacle clearance of VLAs. Our evaluation shows that VEGA achieves
competitive goal progress while reducing collisions by 33.0% and improving obstacle
clearance by 17.9% over the strongest baseline on VEGABench, while improving success by
at least 150.0%, reducing collisions by at least 66.7%, and improving obstacle clearance
by at least 60.0% in real-world trials. Ultimately, we demonstrate that video-derived
geometric supervision provides a scalable and effective signal for training obstacle-
aware navigation VLAs. The code and benchmark will be released at the time of
publication.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18426v1
- Authors: Gershom Seneviratne, Yohan Abeysinghe, Jianyu An, Vaibhav Shende, Dinesh Manocha
- Published: 2026-06-16T19:21:14Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
