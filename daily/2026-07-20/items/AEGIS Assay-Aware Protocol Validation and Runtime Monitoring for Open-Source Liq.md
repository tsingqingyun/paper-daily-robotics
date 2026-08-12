---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15620v1"
published: "2026-07-17T04:39:04Z"
age_days: 3
score: 28
created: 2026-07-20
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# AEGIS: Assay-Aware Protocol Validation and Runtime Monitoring for Open-Source Liquid Handling Robots

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Self-driving laboratories increasingly rely on low-cost liquid handlers such as the
Opentrons OT-2, which ship without the pressure-based aspiration monitoring of Hamilton
or Tecan systems and are typically run open-loop. Two failure modes go undetected:
protocols that are syntactically valid but violate assay-specific invariants (e.g., tip
reuse between a PCR template and a no-template control), and physical execution failures
(partial dispense, air bubbles, missing tips) at runtime. We present AEGIS, a two-layer
guardian for both. Layer 1 pairs a curated machine-readable assay rule database with an
LLM that reasons over OT-2 Python code, reaching an adjusted F1 of 0.97 on a 24-protocol
benchmark across five assay families and beating rules-only and LLM-only ablations
across five backends; a free open-weight model ties the best proprietary one, so no paid
API is required. Layer 2 fits a PCA world model to YOLO-cropped four-frame pipette
trajectories; under a leakage-free leave-one-plate-out evaluation it reaches average
precision 0.89 and operating-point F1 0.71 (AUROC 0.80), a deployment-faithful number
that matches the live demonstration, and we characterize the small-pipette (p20)
resolution limit (F1 0.47). A live demonstration on a physical OT-2 (five replicates per
condition) catches planted no-tip failures deterministically and partial dispense on
coloured dyes, with an always-VLM self-vote gate lifting partial-dispense recall to 5/5;
transparent water is a principled limit of any front-view-only monitor, which AEGIS
surfaces as low-confidence VLM reasoning rather than a wrong verdict. Cascade triage
holds VLM cost near $1.63 per plate versus $10.33 for an always-VLM baseline. AEGIS is
open source and, to our knowledge, the first system to unify pre-flight assay-aware
validation with runtime visual monitoring for an open-source liquid handler.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15620v1
- Authors: Priyanka V. Setty, Arvind Ramanathan, Ian Foster, Rick Stevens
- Published: 2026-07-17T04:39:04Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
