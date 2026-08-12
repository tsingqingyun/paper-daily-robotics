---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.24728v1"
published: "2026-05-23T20:47:05Z"
age_days: 2
score: 31
created: 2026-05-26
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Hylos: Operability Contracts for Model-Native Spatial Intelligence

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Foundation models can increasingly describe, reconstruct, and generate 3D objects,
assemblies, scenes, and environments, but visually plausible spatial output is not yet
operable 3D. A generated object or environment becomes useful to an agent only when the
system can identify its entities, frames, surfaces, constraints, provenance, admissible
actions, expected effects, and validation failures. This paper introduces Hylos, a
systems architecture for contract-bounded spatial intelligence. Hylos maintains scene-
scale operability state over objects, assemblies, assets, surface anchors, assertions,
action candidates, solver jobs, shared actuator invocations, capability gaps, and effect
diffs. Durable spatial changes are routed through a SpatialTransaction: a commit
boundary that resolves references, checks admissibility, protects invariants, projects
effects, and returns commit, review, rollback, deferral, or capability-gap outcomes. The
paper is framed as a systems/position preprint with a focused artifact study rather than
a broad benchmark. The study examines causal repair: a visible misalignment appears on a
dependent component, while the supported repair lies upstream in the placement structure
that controls it. The successful interaction traces the symptom through scene
dependencies, selects a supported upstream interaction, and applies a validated change
instead of directly editing visible geometry. The broader claim is that spatial AI
should be evaluated not only by visual quality, but by whether generated or edited 3D
can become reliable substrate for CAD, robotics, simulation, inspection, manufacturing,
and interactive world authoring.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.24728v1
- Authors: Christopher Da Silva
- Published: 2026-05-23T20:47:05Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
