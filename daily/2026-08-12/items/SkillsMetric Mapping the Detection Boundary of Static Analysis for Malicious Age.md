---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08468v1"
published: "2026-08-09T04:19:10Z"
age_days: 2
score: 25
created: 2026-08-12
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Agent Skills---structured packages of instructions and scripts that augment LLM-based
agents---are rapidly proliferating, yet their security properties remain under-explored.
We present \textsc{SkillsMetric}, a five-stage static analysis framework that scores
skill packages along pattern density, statistical anomaly, dataflow taint, import
anomaly, and capability mismatch dimensions. We construct an adversarial evaluation
dataset of 2{,}266 skills spanning 16~attack types across code-level, system-level, and
semantic-level threats, and evaluate on the full SkillMD-138K corpus. Our framework
achieves an AUC of 0.93 and 5-fold cross-validated F1 of 73.4\%$\pm$0.5\%, with strong
detection of data exfiltration (93\%) and steganographic payloads (93\%). Crucially, we
identify fundamental blind spots: \emph{host destruction} attacks using common shell
commands evade all five stages (0\% detection), and \emph{prompt injection} via natural-
language manipulation achieves only 42\% detection. These findings establish that static
analysis alone is insufficient for skill security, motivating defense-in-depth
architectures that combine fast static pre-screening with semantic review.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08468v1
- Authors: Xinze Chen, Chi Zhang, Ping Ji, Yimin Liu
- Published: 2026-08-09T04:19:10Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
