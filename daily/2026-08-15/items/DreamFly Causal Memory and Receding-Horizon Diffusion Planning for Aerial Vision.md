---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12308v1"
published: "2026-08-12T17:54:33Z"
age_days: 2
score: 29
created: 2026-08-15
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation

> [!summary] 一句话结论（基于摘要）
> DreamFly achieves 32.04%/29.46% SR and 28.22%/23.54% SPL on the test-seen/test-unseen splits, respectively, outperforming all compared methods on both metrics while attaining the lowest navigation error.

## 关键点

- **问题**：Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination.
- **创新点 / 方法**：To address these challenges, we propose DreamFly, a diffusion-based aerial VLN framework built on Dream-VLA.
- **证据**：DreamFly achieves 32.04%/29.46% SR and 28.22%/23.54% SPL on the test-seen/test-unseen splits, respectively, outperforming all compared methods on both metrics while attaining the lowest navigation error.
- **局限**：Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/DreamFly Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observability. Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination. To address these challenges, we propose DreamFly, a diffusion-based aerial VLN framework built on Dream-VLA. DreamFly introduces a causally aligned historical memory that augments the current visual representation using only observations preceding the current decision step, enabling temporal reasoning without future information leakage. We further formulate navigation as receding-horizon diffusion planning, where the policy predicts a $K$-step action chunk but executes only the first action before replanning. This plan-$K$, execute-one strategy uses future actions as auxiliary planning targets while preserving closed-loop visual feedback. Finally, LiteStop estimates the stop probability directly from action logits at the initial all-mask state, decoupling explicit termination from action generation. Experiments on the OpenFly benchmark demonstrate consistent improvements in seen and unseen environments. DreamFly achieves 32.04%/29.46% SR and 28.22%/23.54% SPL on the test-seen/test-unseen splits, respectively, outperforming all compared methods on both metrics while attaining the lowest navigation error. These results demonstrate the effectiveness of jointly modeling historical context, future action structure, and explicit termination for aerial VLN.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12308v1
- Authors: Yan Deng, Fei Xu
- Published: 2026-08-12T17:54:33Z
- Age days: 2

</details>
