---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20065v1"
published: "2026-08-20T13:59:57Z"
age_days: 2
score: 19
created: 2026-08-23
concepts: ["智能体 Agent", "世界模型"]
---

# Orthogonal JEPA: Factorized Predictive States for Latent World Models

> [!summary] 一句话结论（基于摘要）
> We introduce \method, a latent world-modeling framework based on orthogonal predictive factorization.

## 问题

Standard JEPAs, however, organize all predictable content through one target embedding and one prediction pathway.

## 创新点或方法

We introduce \method, a latent world-modeling framework based on orthogonal predictive factorization.

## 证据

摘要未报告明确实验结论；需阅读全文核查。

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：智能体 Agent 世界模型
- **筛选分数**：19
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/Orthogonal JEPA Factorized Predictive States for Latent World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models construct latent states that support prediction, planning, and reasoning about an underlying system. Joint-embedding predictive architectures (JEPAs) offer a direct way to learn such states by predicting targets in representation space instead of reconstructing every detail of the observation. Standard JEPAs, however, organize all predictable content through one target embedding and one prediction pathway. In complex systems, this monolithic state can allocate redundant capacity to dominant signals while providing weak or conflicting gradients to less dominant predictive structure. We introduce \method, a latent world-modeling framework based on orthogonal predictive factorization. Learned basis matrices analyze each target state into multiple components, and a dedicated prediction branch estimates each component from a shared context representation. Predictive regression preserves the factor magnitudes required for state synthesis, an orthogonality objective discourages repeated directions, factor-activity regularization maintains variation in projected targets, and online variance regularization discourages coordinate-wise encoder collapse. Predicted components are synthesized into a complete latent state that can be used by a readout, decoder, planner, or autoregressive rollout. The same predictive-state mechanism applies when the target is temporally future, spatially hidden, or another partial observation of the same system. Experiments on controlled vision, single-cell transcriptomics, longitudinal health records, continuous control, and molecular dynamics evaluate representation quality, forecasting, planning, and long-horizon stability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20065v1
- Authors: Taoyong Cui, Pheng Ann Heng, Wanli Ouyang
- Published: 2026-08-20T13:59:57Z
- Age days: 2

</details>
