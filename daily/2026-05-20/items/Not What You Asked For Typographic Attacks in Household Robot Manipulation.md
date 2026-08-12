---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18593v1"
published: "2026-05-18T16:06:29Z"
age_days: 1
score: 38
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Not What You Asked For: Typographic Attacks in Household Robot Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Open-vocabulary embodied AI agents increasingly rely on vision-language models such as
CLIP for object perception and task grounding. However, the shared embedding space that
enables this flexibility introduces a structural vulnerability to typographic attacks,
where printed text in a physical scene semantically overrides visual judgment. While
prior work has quantified this threat in static 2D benchmarks and 3D navigation tasks,
its impact on the full Sense-Plan-Act pipeline of household robot manipulation remains
unexplored. This work evaluates typographic attacks in a Habitat-based simulation using
the HomeRobot benchmark. We introduce a decoupled perception architecture that exposes a
frozen CLIP encoder to adversarial stickers while maintaining geometric grounding via
DETIC. In a controlled evaluation pool of 59 attributable episodes, the attack achieves
an overall Attack Success Rate (ASR) of 67.8%, rising to 70.0% among fully successful
episodes, under uncontrolled viewing angles and occlusion with no perceptual
optimization. Critically, we find that perceptual errors propagate through the
persistent 3D semantic map to produce kinetic failures, defined here as physically
executed grasping and transport of the wrong object driven by an adversarially poisoned
semantic state. In these cases, the robot physically grasps and delivers the wrong
object to a target receptacle. These results establish typographic misclassification as
a real, measurable, and physically consequential threat to the safety of modular
manipulation pipelines that prior typographic attack research has left unexamined.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18593v1
- Authors: Ali Iranmanesh, Peng Liu
- Published: 2026-05-18T16:06:29Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
