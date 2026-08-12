---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25371v1"
published: "2026-05-25T02:52:34Z"
age_days: 1
score: 32
created: 2026-05-26
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# FOUND-IT: Foundation-model-first Task-driven 3D Scene Graphs with Granularity on Demand

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

We present the first approach to build hierarchical task-driven 3D scene graphs of
arbitrary indoor or outdoor environments using an uncalibrated monocular camera in real-
time. We leverage geometric foundation models to estimate geometric attributes of the
scene graph (e.g., object bounding boxes), but we also observe that traversability
information (the "places" layer of a scene graph) can be directly reconstructed by
adding an extra head to existing geometric foundation models, like VGGT. Our approach is
task-driven in the sense that we adjust the granularity of the objects and regions in
the map depending on the task; for instance, during a manipulation task, our approach is
able to resolve small knobs on a stove, while during a navigation task it can focus on
large objects (e.g., the entire stove). However, in a major departure from related work,
we consider the realistic case where the list of tasks is not predefined and fixed, but
evolves as the robot operates. This naturally allows dealing with complex loco-
manipulation tasks, where the robot can dynamically adjust its representation as the
task unfolds. We dub the resulting approach FOUND-IT. FOUND-IT also includes an agentic
approach to query information in the scene graph. In addition to achieving 79% higher
accuracy on the ASHiTA SG3D task grounding benchmark, we demonstrate FOUND-IT runs in
real-time on a ground robot using a Jetson Thor. Furthermore, to highlight the
robustness of our method, we demonstrate constructing 3D scene graphs on casually
captured realtor apartment tours from YouTube. Code will be made available upon
publication.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25371v1
- Authors: Dominic Maggio, Nicolas Gorlo, Luca Carlone
- Published: 2026-05-25T02:52:34Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
