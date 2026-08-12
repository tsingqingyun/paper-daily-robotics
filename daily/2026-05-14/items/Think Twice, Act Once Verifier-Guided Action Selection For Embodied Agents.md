---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12620v1"
published: "2026-05-12T18:08:24Z"
age_days: 1
score: 31
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents

> [!summary] 一句话结论（基于摘要）
> Across embodied reasoning benchmarks spanning the Habitat and ALFRED environments, VeGAS consistently improves generalization, achieving up to a 36% relative performance gain over strong CoT baselines on the most challenging multi-object, long-horizon tasks.

## 关键点

- **问题**：Building generalist embodied agents capable of solving complex real-world tasks remains a fundamental challenge in AI.
- **创新点 / 方法**：To address this, we propose Verifier- Guided Action Selection (VegAS), a test-time framework designed to improve the robustness of MLLM-based embodied agents through an explicit verification step.
- **证据**：Across embodied reasoning benchmarks spanning the Habitat and ALFRED environments, VeGAS consistently improves generalization, achieving up to a 36% relative performance gain over strong CoT baselines on the most challenging multi-object, long-horizon tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/Think Twice, Act Once Verifier-Guided Action Selection For Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Building generalist embodied agents capable of solving complex real-world tasks remains
a fundamental challenge in AI. Multimodal Large Language Models (MLLMs) have
significantly advanced the reasoning capabilities of such agents through strong vision-
language knowledge and chain-of-thought (CoT) reasoning, yet remain brittle when faced
with challenging out-of-distribution scenarios. To address this, we propose Verifier-
Guided Action Selection (VegAS), a test-time framework designed to improve the
robustness of MLLM-based embodied agents through an explicit verification step. At
inference time, rather than committing to a single decoded action, VeGAS samples an
ensemble of candidate actions and uses a generative verifier to identify the most
reliable choice, without modifying the underlying policy. Crucially, we find that using
an MLLM off-the-shelf as a verifier yields no improvement, motivating our LLM-driven
data synthesis strategy, which automatically constructs a diverse curriculum of failure
cases to expose the verifier to a rich distribution of potential errors at training
time. Across embodied reasoning benchmarks spanning the Habitat and ALFRED environments,
VeGAS consistently improves generalization, achieving up to a 36% relative performance
gain over strong CoT baselines on the most challenging multi-object, long-horizon tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12620v1
- Authors: Nishad Singhi, Christian Bialas, Snehal Jauhri, Vignesh Prasad, Georgia Chalvatzaki, Marcus Rohrbach, Anna Rohrbach
- Published: 2026-05-12T18:08:24Z
- Age days: 1

</details>
