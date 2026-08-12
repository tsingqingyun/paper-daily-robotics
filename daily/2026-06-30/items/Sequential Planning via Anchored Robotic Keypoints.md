---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30613v1"
published: "2026-06-29T17:48:01Z"
age_days: 0
score: 36
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# Sequential Planning via Anchored Robotic Keypoints

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

We present Sequential Planning via Anchored Robotic Keypoints, SPARK, a training-free
neurosymbolic manipulation system that reaches 43.7% on six LIBERO-PRO position \& task
cells, more than doubling CaP-Agent0 and Vision-Language-Action (VLA) baselines. CaP-
Agent0, a multi-turn code-generation agent, achieves 18.2% by re-querying an LLM at
every turn, but its restart-from-scratch solution proves costly against minor policy
failures. Perception is the layer that fails most under position and task changes so
SPARK spends its computation there. A single Gemini call composes the plan as a typed
behavior tree (BT) of composable primitives, each already containing the low-level
control (motion, grasping, depth geometry) a code-generation agent would otherwise
regenerate on every trial. The rest of the budget goes to perception: a second Gemini
call proposes three alternative text prompts per object, SAM3 evaluates each, and we
keep the prompt$\to$label pair with the most confident detection and a recovery loop
then retries a failed primitive against freshly detected objects, with no new LLM call.
The alternative prompts add +27.7 points on the spatial suite and +10.0 on the object
suite, with the recovery loop adding +5.0 overall. SPARK runs the same primitives on
three robot families (UR10e, Franka FR3, bimanual Franka) across nine unique tasks at
twenty trials each, averaging 68%. Since the detector, planner, and controller modules
sit behind the typed plan, they swap independently without training, and each
primitive's checkable post-condition traces a failure to the corresponding module or a
kinematic limit. Every trial logs a verified, labeled trajectory, so a training-free
planner that already beats VLAs can supply the data those policies need without
teleoperation. Project page: https://cwru-aism.github.io/spark-page/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30613v1
- Authors: Bryce Grant, Aryeh Rothenberg, Logan Senning, Zonghe Chua, Zach Patterson, Peng Wang
- Published: 2026-06-29T17:48:01Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
