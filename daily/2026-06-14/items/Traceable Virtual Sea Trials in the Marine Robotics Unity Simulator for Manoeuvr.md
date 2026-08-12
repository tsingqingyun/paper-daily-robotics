---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12349v1"
published: "2026-06-10T17:21:30Z"
age_days: 3
score: 27
created: 2026-06-14
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Traceable Virtual Sea Trials in the Marine Robotics Unity Simulator for Manoeuvring Assessment of Unmanned Surface Vehicles

## 为什么重要

自动筛选分数：27

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Accurate identification of hydrodynamic derivatives is essential for control and
navigation of Unmanned Surface Vehicles (USVs), but high-fidelity manoeuvring data from
physical sea trials are constrained by cost and safety. Turning Circle (TC) and Zig-Zag
(ZZ) trials remain fundamental to IMO and ITTC assessment procedures. This paper extends
the Marine Robotics Unity Simulator (MARUS) by introducing a standardised Virtual Sea
Trial framework for automated execution and data generation of TC/ZZ manoeuvres, with
traceable command-actuation logging, system-identification (SI)-focused data
conditioning, and automated extraction of IMO/ITTC-aligned manoeuvring metrics. A key
contribution is a dedicated TC/ZZ data acquisition and post-processing pipeline,
improving the repeatability and auditability of simulator-based manoeuvres while
producing SI-ready datasets for hydrodynamic-derivative identification and digital-twin
workflows. Another feature is explicit command-execution separation for differential-
thrust steering, where inputs are recorded as ordered rudder-equivalent commands and
realised actuation is logged as an execution-level proxy derived from applied thrust.
Case-study results demonstrate repeatable and compliant manoeuvre behaviour. For TC
tests, the normalised advance differs by approximately 3.9 percent between port and
starboard sides, while the tactical diameter differs by approximately 4.6 to 4.7
percent. For ZZ tests, first and second overshoot excesses remain below 1 degree for
both +/- 10 degree and +/- 20 degree manoeuvres, satisfying IMO criteria, while peak yaw
rates range from approximately 4.1 to 5.8 deg/s. Overall, the framework provides a
repeatable and auditable virtual sea-trial workflow for generating IMO/ITTC-aligned
datasets and supporting system identification, hydrodynamic-derivative estimation, and
digital-twin calibration.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12349v1
- Authors: Paria Rezayan
- Published: 2026-06-10T17:21:30Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
