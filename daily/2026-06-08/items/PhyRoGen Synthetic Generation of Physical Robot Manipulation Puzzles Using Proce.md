---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06569v1"
published: "2026-06-04T17:48:31Z"
age_days: 3
score: 31
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# PhyRoGen: Synthetic Generation of Physical Robot Manipulation Puzzles Using Procedural Content Generation

> [!summary] 一句话结论（基于摘要）
> Finally, we demonstrate that every generated puzzle is manipulatable by using a KUKA LBR iiwa robot in a physical simulation.

## 关键点

- **问题**：However, to enable robots to solve physical puzzles, manipulation skills need to be learned, which requires large training datasets, the generation of which is often time consuming and tedious.
- **创新点 / 方法**：To overcome this problem, we propose the Physical Robot Manipulation Puzzle Generation framework (PhyRoGen), which leverages procedural content generation (PCG) for automated generation of synthetic datasets of manipulation puzzles.
- **证据**：Finally, we demonstrate that every generated puzzle is manipulatable by using a KUKA LBR iiwa robot in a physical simulation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot manipulation of physical puzzles is important for automatic assembly and
disassembly tasks. However, to enable robots to solve physical puzzles, manipulation
skills need to be learned, which requires large training datasets, the generation of
which is often time consuming and tedious. To overcome this problem, we propose the
Physical Robot Manipulation Puzzle Generation framework (PhyRoGen), which leverages
procedural content generation (PCG) for automated generation of synthetic datasets of
manipulation puzzles. PhyRoGen is a general-purpose puzzle generator, which can generate
physical puzzles with interlocking object dependencies, where one articulated object
must be manipulated before another can be moved. Based upon PhyRoGen, we define six
concrete generators which we use to generate 24 physical puzzles. By using a
benchmarking framework, we are able to solve all puzzles in 1 to 300 seconds using
sampling-based planning algorithms. Finally, we demonstrate that every generated puzzle
is manipulatable by using a KUKA LBR iiwa robot in a physical simulation. This shows
that our framework is able to procedurally generate unique, solvable robot manipulation
puzzles, which is a crucial ingredient to benchmark manipulation algorithms and to
develop robust foundation models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06569v1
- Authors: Lennart Julian Droß, Andreas Orthey, Marc Toussaint
- Published: 2026-06-04T17:48:31Z
- Age days: 3

</details>
