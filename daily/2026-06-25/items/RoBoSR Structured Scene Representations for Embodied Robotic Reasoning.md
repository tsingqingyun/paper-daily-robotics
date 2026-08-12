---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24338v1"
published: "2026-06-23T09:24:52Z"
age_days: 1
score: 38
created: 2026-06-25
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RoBoSR: Structured Scene Representations for Embodied Robotic Reasoning

> [!summary] 一句话结论（基于摘要）
> Across several benchmarks and real-world demonstrations, our method consistently outperforms prompting-based methods and classical TAMP baselines in zero-shot generalization and long-horizon tasks.

## 关键点

- **问题**：Despite rapid progress, embodied reasoning under real-world variability remains challenging.
- **创新点 / 方法**：We introduce RoBoSR, an intermediate structural representation that formulates manipulation as step-wise state transitions over semantically grounded, object-centric scene graphs.
- **证据**：Across several benchmarks and real-world demonstrations, our method consistently outperforms prompting-based methods and classical TAMP baselines in zero-shot generalization and long-horizon tasks.
- **局限**：Despite rapid progress, embodied reasoning under real-world variability remains challenging.

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/RoBoSR Structured Scene Representations for Embodied Robotic Reasoning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Despite rapid progress, embodied reasoning under real-world variability remains
challenging. Existing approaches rely on demonstration-driven sequential biases,
limiting flexibility in open-ended and long-horizon tasks that require structured
reasoning over evolving states. We introduce RoBoSR, an intermediate structural
representation that formulates manipulation as step-wise state transitions over
semantically grounded, object-centric scene graphs. By modeling object states and their
spatial relations at the perception-action interface, RoBoSR disentangles high-level
task reasoning from raw inputs and enables structured reasoning over preconditions,
effects, and goal states. This representation endows the agent with causal reasoning
capability, enforcing subtask dependencies and supporting coherent long-horizon task
planning. To learn such structure-aware reasoning, we construct Manip-Cognition-1.6M, an
open-world dataset that jointly supervises scene understanding, instruction
interpretation, and subtask planning across diverse tasks. Across several benchmarks and
real-world demonstrations, our method consistently outperforms prompting-based methods
and classical TAMP baselines in zero-shot generalization and long-horizon tasks. The
results underscore structured intermediate representations as a critical inductive bias
for scalable embodied reasoning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24338v1
- Authors: Kewei Hu, Wanchan Yu, Fangwen Chen, Jing Jiajian, Zimeng Li, Ying Wei, Tianhao Liu, Michael Zhang, Hanwen Kang
- Published: 2026-06-23T09:24:52Z
- Age days: 1

</details>
