---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12620v1"
published: "2026-05-12T18:08:24Z"
age_days: 1
score: 31
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12620v1
- Authors: Nishad Singhi, Christian Bialas, Snehal Jauhri, Vignesh Prasad, Georgia Chalvatzaki, Marcus Rohrbach, Anna Rohrbach
- Published: 2026-05-12T18:08:24Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
