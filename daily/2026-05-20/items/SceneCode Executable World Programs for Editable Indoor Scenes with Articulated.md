---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19587v1"
published: "2026-05-19T09:31:04Z"
age_days: 0
score: 30
created: 2026-05-20
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Indoor scene synthesis underpins embodied AI, robotic manipulation, and simulation-based
policy evaluation, where a useful scene must specify not only what the environment looks
like, but also how its objects are structured. Existing pipelines, however, typically
represent generated content as static meshes and inherit articulation only from curated
asset libraries, which limits object-level controllability and prevents new interactable
assets from being produced on demand. We address this gap by formulating physically
interactable indoor scene synthesis as programmatic world generation, and present
SceneCode, a framework that compiles a natural language prompt into an executable, code-
driven indoor world rather than a collection of opaque meshes. A room-level agentic
backbone first turns the prompt into a structured house layout and emits per-object
AssetRequests through a planner--designer--critic loop. Each request is then routed to
one of five code-generation strategies and converted into a synthesized part-wise
Blender Python programs that are validated through an execution-guided repair-and-refine
loop. The resulting programs are compiled into simulation-ready assets, and exported as
SDF for physics simulation. A persistent scene-state registry links object requests,
executable programs, rendered geometry, and simulation assets, turning scene assembly
into a traceable and locally editable world-building process. We evaluate SceneCode
across scene-level synthesis, object-level asset quality, human judgment, and downstream
robot interaction. Results show that executable world programs improve prompt-faithful
indoor scene generation and produce assets with cleaner mesh structure, and simulator-
loadable articulation metadata. Project page: https://scene-code.github.io/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19587v1
- Authors: Puyi Wang, Yuhao Wang, Linjie Li, Zhengyuan Yang, Kevin Qinghong Lin, Yangguang Li, Yu Cheng
- Published: 2026-05-19T09:31:04Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
