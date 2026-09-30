---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.22975v1"
published: "2026-08-24T08:34:57Z"
age_days: 1
score: 30
created: 2026-08-26
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Budget-Constrained Embodied Perception: Four Resource Walls and a Pre-Registered Evaluation of Access-Structured Perception on Open Models at less than 31B

> [!summary] 一句话结论（基于摘要）
> Under a 4,096-token decision budget, ASP reaches 75 to 94% episodic retrieval accuracy, compared with 3 to 19% for equal-budget query-independent sampling, and budget reallocation outperforms quadrupling the sampling budget on every backbone.

## 问题

However, the full three-component architecture does not validate channel duality: removing the compressive state raises the flagship mean from 35.4 to 58.0, ASP does not outperform the verbatim-only baseline on any backbone, and two of four pre-registered falsification criteria fire.

## 创新点或方法

We introduce ASP, a training-free wrapper for frozen multimodal models that combines a capped structured state, a verbatim episodic index, and query-conditioned budget allocation with iterative access.

## 证据

Under a 4,096-token decision budget, ASP reaches 75 to 94% episodic retrieval accuracy, compared with 3 to 19% for equal-budget query-independent sampling, and budget reallocation outperforms quadrupling the sampling budget on every backbone.

## 局限

However, the full three-component architecture does not validate channel duality: removing the compressive state raises the flagship mean from 35.4 to 58.0, ASP does not outperform the verbatim-only baseline on any backbone, and two of four pre-registered falsification criteria fire.


## 研究关联

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Budget-Constrained Embodied Perception Four Resource Walls and a Pre-Registered.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied multimodal agents must answer from growing observation streams under a fixed per-decision token budget. We formalize this constraint through four resource walls: a perceptual Shannon wall for bounded state, a horizon wall for query-independent frame selection, a round wall for non-adaptive retrieval, and a conditional composition wall for fixed-depth inference. We introduce ASP, a training-free wrapper for frozen multimodal models that combines a capped structured state, a verbatim episodic index, and query-conditioned budget allocation with iterative access. Following a pre-registered protocol, we evaluate seven open-weight models from 3B to 31B on SEW-Bench, a license-free synthetic long-horizon walkthrough benchmark constructed to instantiate these walls. The registered natural-video benchmarks were not run because their frames require dataset agreements; our evidence therefore concerns access mechanisms, not natural-scene perception. Under a 4,096-token decision budget, ASP reaches 75 to 94% episodic retrieval accuracy, compared with 3 to 19% for equal-budget query-independent sampling, and budget reallocation outperforms quadrupling the sampling budget on every backbone. However, the full three-component architecture does not validate channel duality: removing the compressive state raises the flagship mean from 35.4 to 58.0, ASP does not outperform the verbatim-only baseline on any backbone, and two of four pre-registered falsification criteria fire. These results show that query-conditioned access, rather than parameter count or context growth alone, is decisive under a fixed budget, while prompted online compression does not earn its cost in this setting.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.22975v1
- Authors: Defu Lin, Wenhui Chen, Ziyao Lin, Jianlin Chen, Peiji Long, Chi Man Vong
- Published: 2026-08-24T08:34:57Z
- Age days: 1

</details>
